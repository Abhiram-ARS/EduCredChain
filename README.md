# EduCredChain - Educational Credential Blockchain <br> *A Hybrid Blockchain–PKI Architecture for Educational Credential Verification*

---

# 📕 Project Overview

EduCredChain is a secure and tamper-resistant educational credential verification system that integrates **Blockchain technology with Public Key Infrastructure (PKI)** to prevent certificate forgery and enable reliable verification.

Traditional certificate verification processes are often manual, slow, and vulnerable to fraud. EduCredChain addresses these issues by storing **cryptographic hashes of certificate data on a blockchain**, ensuring immutability and transparency, while the encrypted certificate data is securely stored in a database.

The system enables institutions to issue certificates digitally and allows third parties such as employers or organizations to verify their authenticity instantly.

---

# ⚙️ Technology Stack

| Component            | Technology                         |
| -------------------- | ---------------------------------- |
| Programming Language | Python                             |
| Web Interface        | HTML, CSS, JavaScript              |
| Backend Framework    | Python (Flask / API-based backend) |
| Cryptography         | RSA Encryption, SHA-256 Hashing    |
| Database             | SQLite                             |
| Blockchain           | Private Blockchain Network (Ganache)|
| API Communication    | REST API                           |

---

# ✏️ System Flow

The system operates through two main processes: **Certificate Issuance** and **Certificate Verification**.

![Flowchart](https://github.com/Abhiram-ARS/EduCredChain/blob/3e75aafd0d19c7cba48baea4d8f085a578bd377f/Documents/Diagrams/flowchart.png)

## 1️⃣ Certificate Issuance

1. The issuer enters certificate details through the web interface.
2. The certificate data is sent to the backend server.
3. The backend generates a **SHA-256 hash** of the certificate data.
4. Certificate data (excluding certificate ID and date) is **encrypted using the issuer's private key**.
5. The encrypted data and hash are stored in the **SQLite database**.
6. The generated hash is added to the **blockchain network**.
7. The system confirms successful certificate issuance.


## 2️⃣ Certificate Verification

1. The user enters the **Certificate ID** on the verification portal.
2. The backend retrieves the encrypted certificate data from the database.
3. The corresponding hash is fetched from the blockchain.
4. The certificate data is **decrypted using the public key**.
5. A new SHA-256 hash is generated from the decrypted data.
6. The newly generated hash is compared with the blockchain hash.

**Matching hashes → Certificate is valid**
**Non-matching hashes → Certificate has been tampered**

---

# System Architecture

The system architecture consists of the following modules:

* Web Interface
* Backend Application
* Cryptographic Processing Module
* Database Storage
* Blockchain Network


## Architecture Diagram

![Architecture_Diagram](https://github.com/Abhiram-ARS/EduCredChain/blob/7b91ef3dd5d7f87f39e7ad49a8cfe97778278f58/Documents/Diagrams/architecture_diagram.png)

```
[ Web Interface ]
        │
        ▼
[ Backend Server / API ]
        │
        ├── Cryptographic Module (RSA + SHA256)
        │
        ├── SQLite Database
        │
        ▼
[ Blockchain Network ]
```

---

# Module Description

- Web Interface, Provides user interaction for certificate issuance and verification through a browser-based interface.
- Backend Server, Handles request processing, data validation, cryptographic operations, and communication with the database and blockchain.
- Cryptographic Module, Responsible for generating hashes, performing RSA encryption/decryption, and ensuring secure credential processing.
- Database, Stores encrypted certificate data along with metadata for retrieval during verification.
- Blockchain Network, Stores certificate hashes to ensure **immutability and tamper resistance**.


# Project Structure

```
EduCredChain
│
├── backend
│   ├── encryption.py
│   ├── blockchain.py
│   ├── api.py
│
├── database
│   └── certificates.db
│
├── web
│   ├── index.html
│   ├── issue.html
│   ├── verify.html
│
├── utils
│   ├── hash_generator.py
│   └── rsa_keys.py
│
└── README.md
```

---

# Security Mechanisms

* **SHA-256 hashing** ensures certificate data integrity.
* **RSA encryption** protects sensitive credential information.
* **Blockchain storage** prevents modification of certificate records.
* **Digital signatures** verify the authenticity of the issuing authority.

---

# Future Improvements

* Smart contract based certificate management
* Multi-institution blockchain network
* QR code based certificate verification
* IPFS integration for decentralized storage
* Mobile verification application

---

# Authors 
🧑‍💻**Abhiram S**,BTech Student
🧑‍💻**Amarnath Mohan**,BTech Student
🧑‍💻**Mohammed Yaseen**,BTech Student

# License

Project is licensed under MIT license
### 👉 [License](https://github.com/Abhiram-ARS/EduCredChain/blob/8077076a761129c5b68ca0b1da8ad9ec876ada0b/LICENSE)
---
