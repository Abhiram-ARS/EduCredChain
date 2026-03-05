# **EduCredChain: A Hybrid Blockchain-PKI Credential Ecosystem**

## Unified Multi-Layer Credential Verification System (UMCVS)


A Hybrid System Combining Blockchain, NFTs, Hyperledger Fabric, and PKI for Tamper-Proof Academic Certificate Management


# ✅ Project Overview

This project creates a single, multi-layered certificate verification ecosystem that uses:

✔ *PKI* — for digital signatures & authenticity

✔ *Hyperledger Fabric* — for private consortium ledger among institutions

✔ *Public Blockchain NFTs* — for global proof of ownership

✔ *Blockchain Verification Portal* — for public tamper-proof validation

This makes it enterprise-grade, scalable, secure, and future-proof.


🧩 Why This Project Is Unique

Most certificate systems use only blockchain or only PKI, but this project uses all four, giving:

* Tamper-proof storage
* Verifiable ownership
* Decentralized trust
* Cross-institution collaboration
* Public transparency + private control


### 🛠 Architecture (Combined Model)

1️⃣ PKI Layer – Authentication & Signing

* Every institution acts as a Certificate Authority (CA).
* Certificates are generated and digitally signed using the institution’s private key.
* The verifier checks authenticity with the public key.

Role: Ensures cryptographic trust & authenticity.

2️⃣ Hyperledger Fabric Layer – Consortium Network

* A private network connecting:

  * Universities
  * Colleges
  * Verification agencies
  * Government bodies
* Fabric stores:

  * Certificate hashes
  * Student metadata
  * Issuer signatures
  * Revocation status

Role: Secure inter-institution record sharing without exposing private data.



3️⃣ NFT Layer – Ownership Proof

* Each certificate is minted as a non-transferable NFT (Soulbound Token) on a public blockchain.
* NFT contains:

  * Certificate hash
  * Institution ID
  * Issuer signature
  * Verification link

Role: Public proof that the certificate belongs to the student & cannot be forged or traded.


4️⃣ Blockchain Verification Portal

A web portal that performs:

✔ PKI verification
✔ Hash comparison with Hyperledger
✔ NFT ownership validation

Users enter:

* Certificate ID
* QR code scan
* NFT ID

System automatically verifies authenticity across all 3 layers

➤ Step 1: Certificate Creation

1. Institution issues certificate.
2. Certificate is hashed (SHA-256).
3. Institution signs hash with its private key (PKI).

➤ Step 2: Storage in Hyperledger Fabric*

* Certificate hash + student ID stored in Fabric ledger.
* Smart contract ensures:

  * No duplicate entries
  * Revocation support
  * Audit trails


➤ Step 3: NFT Minting

* Certificate hash is minted as a non-transferable NFT.
* NFT metadata includes:

  * Hash
  * Issuer signature
  * Student blockchain address
  * Hyperledger reference ID



➤ Step 4: Verification Portal

When a verifier (employer, university) scans QR / enters ID:

System checks:

1. PKI:

Verifies signature is valid.

2. Hyperledger Fabric:

Matches certificate hash and status.

3. NFT Blockchain:

Checks public NFT ownership & immutability.

Verification result: Authentic / Tampered / Revoked / Suspicious



 📦 Modules in the Project

 ✔ Certificate Issuance Module
 ✔ PKI Signing Engine
 ✔ Hyperledger Fabric Smart Contract
 ✔ NFT Minting Module (ERC-721 / Soulbound)
 ✔ QR Code Generator
 ✔ Certificate Verification Portal
 ✔ Revocation Management System
 ✔ Student Wallet



 🧪 Technologies to Use

Backend: Python / JS
Frontend: Classic HTML+CSS+JS
Databases: JSON



🌟 Advantages of This Unified System

✔ Near-zero forgery
✔ Immutable history
✔ Strong cryptographic trust
✔ Public + private blockchain combined
✔ Verifiable from anywhere
✔ Inter-college collaboration
✔ Zero-trust, decentralized model
