"""
Project Title : EduCredChain
Description   : Blockchain-Based Certificate Verification System

File Name     : BlkChain_ECC.py
Description   : Core blockchain module handling smart contract deployment, certificate hashing, issuance, verification, and revocation using Web3

Author(s)     : ABHIRAM_S, AMARNATH MOHAN, MOHAMMED YASEEN

Last Modified : 18-04-2026
"""

from datetime import datetime
import hashlib
import os
import sys
from web3 import Web3
from solcx import compile_source, install_solc, set_solc_version
import SQL_ECC
from datetime import datetime



class BlkChain_funct:
    def __init__(self):
        ganache_url = "http://127.0.0.1:7545"

        self.CONTRACT_FILE = "Certificate.sol"
        self.SOLC_VERSION = "0.8.17"
        self.w3 = Web3(Web3.HTTPProvider(ganache_url))

        self.abi, self.bytecode = self.compile_contract()
        self.w3 = self.connect_blockchain()
        self.contract = self.deploy_or_load_contract()

        self.sqlecc = SQL_ECC.Sql_db()

    def connect_blockchain(self):
        if not self.w3.is_connected():
            print("Ganache not connected.")
            sys.exit()

        self.w3.eth.default_account = self.w3.eth.accounts[0]

        print("Connected to Blockchain")
        print("Chain ID:", self.w3.eth.chain_id)
        print("Active Account:", self.w3.eth.default_account)

        return self.w3


    def compile_contract(self):
        install_solc(self.SOLC_VERSION)
        set_solc_version(self.SOLC_VERSION)

        with open(self.CONTRACT_FILE, "r", encoding="utf-8") as file:
            source_code = file.read()

        compiled = compile_source(source_code, output_values=["abi", "bin"])
        _, contract_interface = compiled.popitem()

        return contract_interface["abi"], contract_interface["bin"]


    def deploy_or_load_contract(self):
        address_file = "contract_address.txt"
        if os.path.exists(address_file):
            with open(address_file, "r", encoding="utf-8") as f:
                contract_address = f.read().strip()

            if not Web3.is_address(contract_address):
                print("Invalid address found in contract_address.txt")
                print("Stored value:", contract_address)
                print("Deploying New Contract...")

                certificate = self.w3.eth.contract(abi=self.abi, bytecode=self.bytecode)
                tx_hash = certificate.constructor().transact(
                    {"from": self.w3.eth.default_account, "gas": 3000000}
                )
                receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
                contract_address = receipt.contractAddress

                with open(address_file, "w", encoding="utf-8") as f:
                    f.write(contract_address)

                contract = self.w3.eth.contract(address=contract_address, abi=self.abi)

                print("Contract Deployed Successfully")
                print("Address:", contract_address)
                print("Block Number:", receipt.blockNumber)
            else:
                checksum_address = Web3.to_checksum_address(contract_address)
                code_at_address = self.w3.eth.get_code(checksum_address)

                if code_at_address in [b"", b"0x"]:
                    print("No contract bytecode found at saved address.")
                    print("Saved address:", checksum_address)
                    print("This usually happens after restarting Ganache (new chain state).")
                    print("Deploying New Contract...")

                    certificate = self.w3.eth.contract(abi=self.abi, bytecode=self.bytecode)
                    tx_hash = certificate.constructor().transact(
                        {"from": self.w3.eth.default_account, "gas": 3000000}
                    )
                    receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
                    contract_address = receipt.contractAddress

                    with open(address_file, "w", encoding="utf-8") as f:
                        f.write(contract_address)

                    contract = self.w3.eth.contract(address=contract_address, abi=self.abi)

                    print("Contract Deployed Successfully")
                    print("Address:", contract_address)
                    print("Block Number:", receipt.blockNumber)
                else:
                    contract = self.w3.eth.contract(address=checksum_address, abi=self.abi)

                    print("Loaded Existing Contract")
                    print("Address:", checksum_address)

        else:
            print("Deploying New Contract...")

            certificate = self.w3.eth.contract(abi=self.abi, bytecode=self.bytecode)

            tx_hash = certificate.constructor().transact(
                {"from": self.w3.eth.default_account, "gas": 3000000}
            )

            receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
            contract_address = receipt.contractAddress

            with open(address_file, "w", encoding="utf-8") as f:
                f.write(contract_address)

            contract = self.w3.eth.contract(address=contract_address, abi=self.abi)

            print("Contract Deployed Successfully")
            print("Address:", contract_address)
            print("Block Number:", receipt.blockNumber)

        return contract
    

    def issue_certificate(self,data):

        """
        Data : {"studentName":"_","course":"_","certid":"_","grade":"_"}

        """
        now = datetime.now()

        name = data["studentName"]
        course_id = data["course"]
        certificate_no = data["certid"]
        issue_date = now.strftime("%d-%m-%y")
        grade = data["grade"]

        cert_hash = self.generate_certificate_hash(
            name, course_id, certificate_no, issue_date, grade
        )
        
        self.sqlecc.add_record([certificate_no,name, course_id, issue_date, grade,cert_hash.hex()])

        try:
            tx_hash = self.contract.functions.issueCertificate(cert_hash).transact(
                {"from": self.w3.eth.default_account, "gas": 200000}
            )

            receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)

            return{"status":1,
                   "Message": "issued",
                   "certhash":cert_hash.hex(), 
                   "blockno": receipt.blockNumber}

        except Exception as exc:
            return{"status":0,
                   "Error":"EB01",
                   "Message": "BlockChianError : "+ exc}

    # ==========================================================
    # 7 VERIFY CERTIFICATE
    # ==========================================================

    def fetch_certificate(self,certid):
        row = self.sqlecc.select_record(str(certid))
        print("=",row)
        if not row:
            print("Certificate not found in DB")
            return{"status":0,
                   "Error":"EDB01",
                   "Message": "Data_not_Found"}
        
        
        cert_hash_db = row[5]
        
        # Recompute hash from DB fields and compare with stored hash before chain check.
        recalculated_hash = self.generate_certificate_hash(
            row[1], row[2], row[0], row[3], row[4]
        )

        if cert_hash_db != recalculated_hash.hex():
            return{"status":0,
                   "Error":"EDB02",
                   "certhash":cert_hash_db,
                   "recalculated_hash":recalculated_hash.hex(),
                   "Message": "DB_Tampered"}


        return row

    
    def verify_certificate(self, data):
        # Accept either a DB row tuple/list or API payload dict.
        #{name}|{course_id}|{certificate_no}|{issue_date}|{grade}
        print(data)
        row = [data['studentName'],data['course'],data['certid'],data['date'],data['grade']]
        
        # Recompute hash from DB fields and compare with stored hash before chain check.
        recalculated_hash = self.generate_certificate_hash(
            row[0], row[1], row[2], row[3], row[4]
        )

        recalculated_hash = recalculated_hash.hex()
        # Normalize DB value -> bytes32
        if isinstance(recalculated_hash, bytes):
            # could be raw digest bytes OR hex bytes
            try:
                text = recalculated_hash.decode("utf-8")
                cert_hash = bytes.fromhex(text)  # if stored as hex in bytes form
            except Exception:
                cert_hash = recalculated_hash          # raw bytes already
        elif isinstance(recalculated_hash, str):
            cert_hash = bytes.fromhex(recalculated_hash)
        else:
            
            return{"status":0,
                   "Error":"EB02",
                   "Message": "DB_Decryption_Error"}

        try:
            exists, revoked, issued_at, revoked_at = self.contract.functions.verifyCertificate(
                cert_hash
            ).call()
            
            

            if not exists:
                status = "NotFound"
            elif revoked:
                status = "Revoked"
            else:
                status = "Active"
            print("\n\n ********",status,"********\n\n")
            return{"status":1,
                   "certificate_status":status,
                   "issuedat":issued_at,
                   "revokedat":revoked_at,
                   "certhash":cert_hash.hex()}

        except Exception as exc:
            print("\nError:", exc)
            return {"status": 0,
                    "Error": "EB05",
                    "Message": "Blockchain_Verify_Error"}


    def revoke_certificate(self, data):
        row = self.sqlecc.select_record(str(data['certid']))
        print(1)
        if not row:
            return {"status": 0,
                    "Error": "EDB01",
                    "Message": "Data_not_Found"}

        cert_hash_hex = row[5]
        try:
            print(2)
            cert_hash = bytes.fromhex(cert_hash_hex)
        except Exception:
            return {"status": 0,
                    "Error": "EDB03",
                    "Message": "Hash_Decode_Error"}

        try:
            print(3)
            tx_hash = self.contract.functions.revokeCertificate(cert_hash).transact(
                {"from": self.w3.eth.default_account, "gas": 200000}
            )
            receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)

            return {"status": 1,
                    "Message": "Revoked",
                    "certhash": cert_hash_hex,
                    "blockno": receipt.blockNumber}

        except Exception as exc:
            print("\nError:", exc)
            return {"status": 0,
                    "Error": "EB03",
                    "Message": "BlockChain_Revoke_Error"}

    def generate_certificate_hash(self, name, course_id, certificate_no, issue_date, grade):
        name = name.strip().lower()
        course_id = course_id.strip().lower()
        certificate_no = certificate_no.strip().lower()
        issue_date = issue_date.strip()
        grade = grade.strip().upper()

        data_string = f"{name}|{course_id}|{certificate_no}|{issue_date}|{grade}"
        return hashlib.sha256(data_string.encode()).digest()


    def main(self):
        while True:
            print("\n===================================")
            print("1 Issue Certificate")
            print("2 Verify Certificate")
            print("3 Revoke Certificate")
            print("q Exit")
            print("===================================")

            choice = input("Select Option: ").lower()

            if choice == "1":
                data = {
                    "studentName": input("Student Name: ").strip(),
                    "course": input("Course ID: ").strip(),
                    "certid": input("Certificate Number: ").strip(),
                    "grade": input("Grade: ").strip(),
                }
                print(self.issue_certificate(data))
            elif choice == "2":
                certid= input("Certificate Number: ").strip()
                print(self.fetch_certificate(certid))
            elif choice == "3":
                certid= input("Certificate Number: ").strip()
                self.revoke_certificate(certid)
            elif choice == "q":
                print("Exiting...")
                break
            else:
                print("Invalid Option")

#bk = BlkChain_funct()
#bk.main()
