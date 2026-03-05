# EduCredChain: A Hybrid Blockchain-PKI Credential Ecosystem
# ==========================================================
from web3 import Web3
from solcx import compile_source, install_solc, set_solc_version
import hashlib
import os
import sys
from datetime import datetime



    # ==========================================================
    # 1️⃣ CONFIGURATION
    # ==========================================================
class Blockchain_Module:

    
    SOLC_VERSION = "0.8.17"
    
    

    # ==========================================================
    # 2️⃣ CONNECT TO BLOCKCHAIN
    # ==========================================================

    def connect_blockchain():
        GANACHE_URL = "http://127.0.0.1:7545"
        w3 = Web3(Web3.HTTPProvider(GANACHE_URL))

        if not w3.is_connected():
            print("❌ Ganache not connected.")
            sys.exit()

        w3.eth.default_account = w3.eth.accounts[0]

        print("✅ Connected to Blockchain")
        print("Chain ID:", w3.eth.chain_id)
        print("Active Account:", w3.eth.default_account)

        return w3

    # ==========================================================
    # 3️⃣ COMPILE CONTRACT
    # ==========================================================

    def compile_contract():
        CONTRACT_FILE = "Certificate.sol"
        
        SOLC_VERSION = "0.8.17"

        install_solc(SOLC_VERSION)
        set_solc_version(SOLC_VERSION)

        with open(CONTRACT_FILE, "r") as file:
            source_code = file.read()

        compiled = compile_source(source_code, output_values=["abi", "bin"])
        _, contract_interface = compiled.popitem()

        return contract_interface["abi"], contract_interface["bin"]

    # ==========================================================
    # 4️⃣ DEPLOY OR LOAD CONTRACT
    # ==========================================================

    def deploy_or_load_contract(w3, abi, bytecode):
        ADDRESS_FILE = "contract_address.txt"
        if os.path.exists(ADDRESS_FILE):

            with open(ADDRESS_FILE, "r") as f:
                contract_address = f.read().strip()

            if not Web3.is_address(contract_address):
                print("\n⚠ Invalid address found in contract_address.txt")
                print("Stored value:", contract_address)
                print("🚀 Deploying New Contract...")

                Certificate = w3.eth.contract(abi=abi, bytecode=bytecode)
                tx_hash = Certificate.constructor().transact({
                    "from": w3.eth.default_account,
                    "gas": 3000000
                })
                receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
                contract_address = receipt.contractAddress

                with open(ADDRESS_FILE, "w") as f:
                    f.write(contract_address)

                contract = w3.eth.contract(address=contract_address, abi=abi)

                print("✅ Contract Deployed Successfully")
                print("Address:", contract_address)
                print("Block Number:", receipt.blockNumber)
            else:
                checksum_address = Web3.to_checksum_address(contract_address)
                code_at_address = w3.eth.get_code(checksum_address)

                if code_at_address in [b"", b"0x"]:
                    print("\n⚠ No contract bytecode found at saved address.")
                    print("Saved address:", checksum_address)
                    print("This usually happens after restarting Ganache (new chain state).")
                    print("🚀 Deploying New Contract...")

                    Certificate = w3.eth.contract(abi=abi, bytecode=bytecode)
                    tx_hash = Certificate.constructor().transact({
                        "from": w3.eth.default_account,
                        "gas": 3000000
                    })
                    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
                    contract_address = receipt.contractAddress

                    with open(ADDRESS_FILE, "w") as f:
                        f.write(contract_address)

                    contract = w3.eth.contract(address=contract_address, abi=abi)

                    print("✅ Contract Deployed Successfully")
                    print("Address:", contract_address)
                    print("Block Number:", receipt.blockNumber)
                else:
                    contract = w3.eth.contract(address=checksum_address, abi=abi)

                    print("\n📦 Loaded Existing Contract")
                    print("Address:", checksum_address)

        else:
            print("\n🚀 Deploying New Contract...")

            Certificate = w3.eth.contract(abi=abi, bytecode=bytecode)

            tx_hash = Certificate.constructor().transact({
                "from": w3.eth.default_account,
                "gas": 3000000
            })

            receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
            contract_address = receipt.contractAddress

            with open(ADDRESS_FILE, "w") as f:
                f.write(contract_address)

            contract = w3.eth.contract(address=contract_address, abi=abi)

            print("✅ Contract Deployed Successfully")
            print("Address:", contract_address)
            print("Block Number:", receipt.blockNumber)

        return contract

    # ==========================================================
    # 5️⃣ HASH GENERATOR (SHA-256 WITH GRADE)
    # ==========================================================

    def generate_certificate_hash(name, courseId, certificateNo, issueDate, grade):

        name = name.strip().lower()
        courseId = courseId.strip().lower()
        certificateNo = certificateNo.strip().lower()
        issueDate = issueDate.strip()
        grade = grade.strip().upper()

        data_string = f"{name}|{courseId}|{certificateNo}|{issueDate}|{grade}"

        return hashlib.sha256(data_string.encode()).digest()

    # ==========================================================
    # 6️⃣ ISSUE CERTIFICATE
    # ==========================================================

    def issue_certificate(w3, contract):

        print("\n📜 Issue Certificate")
        print("----------------------")

        name = input("Student Name: ")
        courseId = input("Course ID: ")
        certificateNo = input("Certificate Number: ")
        issueDate = input("Issue Date: ")
        grade = input("Grade: ")

        cert_hash = Blockchain_Module.generate_certificate_hash(
            name, courseId, certificateNo, issueDate, grade
        )

        try:
            tx_hash = contract.functions.issueCertificate(cert_hash).transact({
                "from": w3.eth.default_account,
                "gas": 200000
            })

            receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

            print("\n✅ Certificate Issued Successfully")
            print("Certificate Hash:", cert_hash.hex())
            print("Block Number:", receipt.blockNumber)

        except Exception as e:
            print("\n❌ Error:", e)

    # ==========================================================
    # 7️⃣ VERIFY CERTIFICATE
    # ==========================================================

    def verify_certificate(w3,contract):

        print("\n🔍 Verify Certificate")
        print("----------------------")

        name = input("Student Name: ")
        courseId = input("Course ID: ")
        certificateNo = input("Certificate Number: ")
        issueDate = input("Issue Date: ")
        grade = input("Grade: ")

        cert_hash = Blockchain_Module.generate_certificate_hash(
            name, courseId, certificateNo, issueDate, grade
        )

        try:
            exists, revoked, issuedAt, revokedAt = contract.functions.verifyCertificate(
                cert_hash
            ).call()

            print("\n📊 Verification Result")
            print("------------------------")

            if not exists:
                print("❌ Certificate NOT Found")

            elif revoked:
                revoked_time = datetime.fromtimestamp(revokedAt)
                print("⚠ Certificate Revoked")
                print("Revocation Date:", revoked_time)

            else:
                issued_time = datetime.fromtimestamp(issuedAt)
                print("✅ VALID Certificate")
                print("Issued Date:", issued_time)
                print("Verified Hash:", cert_hash.hex())

        except Exception as e:
            print("\n❌ Error:", e)

    # ==========================================================
    # 8️⃣ REVOKE CERTIFICATE
    # ==========================================================

    def revoke_certificate(w3, contract):

        print("\n🚫 Revoke Certificate")
        print("----------------------")

        name = input("Student Name: ")
        courseId = input("Course ID: ")
        certificateNo = input("Certificate Number: ")
        issueDate = input("Issue Date: ")
        grade = input("Grade: ")

        cert_hash = Blockchain_Module.generate_certificate_hash(
            name, courseId, certificateNo, issueDate, grade
        )

        try:
            tx_hash = contract.functions.revokeCertificate(cert_hash).transact({
                "from": w3.eth.default_account,
                "gas": 200000
            })

            receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

            print("\n✅ Certificate Revoked Successfully")
            print("Block Number:", receipt.blockNumber)

        except Exception as e:
            print("\n❌ Error:", e)

    # ==========================================================
    # 9️⃣ MAIN MENU
    # ==========================================================

    def main(w3,contract):

        while True:
            print("\n===================================")
            print("1️⃣  Issue Certificate")
            print("2️⃣  Verify Certificate")
            print("3️⃣  Revoke Certificate")
            print("q️⃣  Exit")
            print("===================================")

            choice = input("Select Option: ").lower()

            if choice == "1":
                Blockchain_Module.issue_certificate(w3, contract)

            elif choice == "2":
                Blockchain_Module.verify_certificate(w3,contract)

            elif choice == "3":
                Blockchain_Module.revoke_certificate(w3, contract)

            elif choice == "q":
                print("👋 Exiting...")
                break

            else:
                print("❌ Invalid Option")

w3 = Blockchain_Module.connect_blockchain()
abi, bytecode = Blockchain_Module.compile_contract()
contract = Blockchain_Module.deploy_or_load_contract(w3, abi, bytecode)
