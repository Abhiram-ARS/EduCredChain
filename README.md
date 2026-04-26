# EduCredChain - Educational Credential Blockchain <br> *A Hybrid Blockchain–PKI Architecture for Educational Credential Verification*

---

## 📕 Project Overview

EduCredChain is a secure and tamper-resistant educational credential verification system that integrates **Blockchain technology with Public Key Infrastructure (PKI)** to prevent certificate forgery and enable reliable verification.

Traditional certificate verification processes are often manual, slow, and vulnerable to fraud. EduCredChain addresses these issues by storing **cryptographic hashes of certificate data on a blockchain**, ensuring immutability and transparency, while the encrypted certificate data is securely stored in a database.

The system enables institutions to issue certificates digitally and allows third parties such as employers or organizations to verify their authenticity instantly.

---

## ⚙️ Technology Stack

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

## System Architecture

The system architecture consists of the following modules:

* Web Interface
* Backend Application
* Cryptographic Processing Module
* Database Storage
* Blockchain Network


### Architecture Diagram


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

## Module Description

- Web Interface, Provides user interaction for certificate issuance and verification through a browser-based interface.
- Backend Server, Handles request processing, data validation, cryptographic operations, and communication with the database and blockchain.
- Cryptographic Module, Responsible for generating hashes, performing RSA encryption/decryption, and ensuring secure credential processing.
- Database, Stores encrypted certificate data along with metadata for retrieval during verification.
- Blockchain Network, Stores certificate hashes to ensure **immutability and tamper resistance**.


## Project Structure

```
EduCredChain
|
code
│
├── BackEnd
│   ├── API_ECC.py
│   ├── BlkChain_ECC.py
│   ├── Certificate.sol
│   └── SQL_ECC.py
│   
├──Database_Bypass_Application
│       ├── dbBypass.py
│       └── Readme.md
│
├── FrontEnd
│   └── index.html
│
├── Database
│   └── certificates.db
│
└──  requirements.txt

```

---

## Security Mechanisms

* **SHA-256 hashing** ensures certificate data integrity.
* **RSA encryption** protects sensitive credential information.
* **Blockchain storage** prevents modification of certificate records.
* **Digital signatures** verify the authenticity of the issuing authority.

---

## Authors 
🧑‍💻**Abhiram S**,BTech Student

🧑‍💻**Amarnath Mohan**,BTech Student

🧑‍💻**Mohammed Yaseen**,BTech Student

## License

Project is licensed under MIT license
### 👉 [License](https://github.com/Abhiram-ARS/EduCredChain/blob/8077076a761129c5b68ca0b1da8ad9ec876ada0b/LICENSE)
---
