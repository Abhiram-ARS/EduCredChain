# EduCredChain - Educational Credential Blockchain.<br>A Hybrid Blockchain–PKI Architecture for Educational Credential Validation
---
## DECLARATION  
We Abhiram S, Amarnath Mohan and Mohammed Yaseen hereby declare that, this project report 
entitled “EduCredChain - Educational Credential Blockchain, A Hybrid Blockchain–PKI Architecture 
for Educational Credential Validation” is the bonafide work of mine carried out under the supervision 
of Prof. Haseena M K. We declare that to the best of our knowledge, the work report here in does not 
form part of any project report or dissertation the basis of which a degree or award was conferred on 
an earlier occasion on any other candidate the content of this report is not being presented by any other 
student to this or any other university for the award of degree.

---

## ABSTRACT  
 
EduCredChain is a decentralized and secure digital certificate management 
system designed to address the growing issue of certificate fraud and inefficient 
verification processes. Traditional methods of issuing and validating academic and 
professional credentials are often time-consuming, vulnerable to tampering, and reliant 
on centralized authorities. This project leverages blockchain technology to create a 
tamper-proof, transparent, and verifiable platform for issuing, storing, and validating 
certificates. 
 
The system enables institutions to generate digital certificates that are 
cryptographically secured and stored on a blockchain network, ensuring immutability 
and authenticity. Each certificate is associated with a unique hash and can be verified 
instantly using QR codes or digital identifiers, eliminating the need for manual 
verification. Smart contracts automate the issuance and validation processes, reducing 
administrative overhead and enhancing trust among stakeholders. 
 
EduCredChain improves data integrity, reduces fraud, and provides a scalable 
solution that can be integrated across multiple institutions and platforms. By combining 
blockchain with modern technologies, the project contributes to a more reliable, 
efficient, and secure credential verification ecosystem suitable for academic, corporate, 
and governmental use cases.

---

## CHAPTER-1 <br>INTRODUCTION  
Educational institutions increasingly rely on digital certificates to represent 
academic achievements, qualifications, and training credentials. However, traditional 
certificate management systems are vulnerable to issues such as forgery, unauthorized 
modification, and difficulty in verification. These limitations make it challenging for 
employers and institutions to confirm the authenticity of certificates quickly and reliably. 
As a result, there is a growing need for a secure, transparent, and efficient system that 
can ensure the integrity and trustworthiness of educational credentials. 
The proposed project, EduCredChain, a Hybrid Blockchain–PKI architecture 
designed for secure educational credential verification. The system combines the 
immutability of blockchain technology with the security of cryptographic mechanisms 
such as SHA-256 hashing and public key encryption. When a certificate is issued, its 
data is securely processed and a cryptographic hash is generated. The certificate data is 
encrypted and stored in a database, while the hash is recorded on the blockchain. This 
approach ensures that any alteration to the certificate data can be easily detected, thereby 
preventing tampering and fraud. 
In addition to certificate issuance, the system supports secure verification and 
revocation mechanisms. Users can verify a certificate by entering its unique identifier, 
after which the system checks data integrity and validates the stored hash against the 
blockchain. If necessary, certificates can also be revoked, and the revocation status is 
updated on the blockchain to maintain transparency. By integrating web technologies, 
cryptographic techniques, and blockchain infrastructure, the proposed system provides 
a reliable and tamper-resistant solution for managing and verifying educational 
credentials.

---

## CHAPTER-2 <br>LITERATURE SURVEY 
1. **Verification and Validation of Certificate Using Blockchain** 
_Authors: Krutant Dongare, Shivani Waghmare, Shruti Bobade, Sakshi Gogulwar, 
Achal Gothe, Vaishnavi Jayshingkar, Amol Dhankar 
[Nov 2025, IJRASET]_

This paper proposes a blockchain-based system designed to provide a secure and 
transparent platform for issuing and verifying educational and professional certificates. 
Traditional certificate verification systems rely heavily on centralized databases and 
manual validation processes, which makes them vulnerable to forgery, duplication, and 
manipulation. The authors highlight the growing need for a reliable digital verification 
mechanism to ensure the authenticity of academic credentials and reduce fraudulent 
practices. 
The proposed system uses blockchain technology to store cryptographic hashes of 
certificates, ensuring immutability and tamper resistance. To efficiently store certificate 
files, the system integrates the InterPlanetary File System (IPFS), where the actual 
certificate is stored while the blockchain maintains the reference hash. The system also 
provides an Android-based interface that enables institutions to issue certificates, 
students to manage them, and employers to verify authenticity instantly. This approach 
improves transparency, reduces verification time, and establishes a secure digital 
credential management system.

3. **Blockchain Technology for Secure Digital Certificate Generation and 
Verification** 
_Authors: Kunal Godase, Omkar Ghate, Swapnil Kale, Saurabh Ghadage, Prof. 
Sudhakar Jadhav 
[MAR 2025, IJCRT]_

This research focuses on developing a blockchain-based system to securely generate 
and verify digital academic certificates. The authors emphasize that traditional 
verification methods are inefficient, prone to forgery, and difficult to manage due to 
centralized storage. With the increasing number of graduates each year, institutions 
require a more reliable and scalable solution to verify credentials quickly and securely.
The proposed system uses Ethereum blockchain technology along with smart 
contracts to automate the certificate issuance and verification process. Certificate files 
are stored in the InterPlanetary File System (IPFS), while their cryptographic hash 
values and IPFS links are stored on the blockchain to maintain integrity. The system 
also incorporates technologies such as MetaMask for authentication, ReactJS for 
frontend development, and NodeJS for backend operations. By using decentralized 
technologies, the system ensures transparency, tamper-proof certificate storage, and 
instant verification without relying on centralized authorities.
 
4. **Blockchain Driven Credential Issuing and Verification of Certificates**
_Authors: G. Raju, Lalitha Reddy Buchupalli, Aswini Thudimela, Kaveri 
Kodikondla, Kavitha Palaku, Divya Vadde 
[APR 2025, GJEIIR]_

This paper presents a blockchain-driven system for issuing and verifying educational 
certificates to address the growing problem of fake credentials and inefficient 
verification processes. The authors discuss how traditional methods require repeated 
submission and manual verification of certificates throughout a student's academic and 
professional journey. This process increases the risk of document loss, fraud, and 
administrative delays. 
The proposed solution uses blockchain technology to create a decentralized and 
tamper-proof credential verification system. Certificates are issued and stored securely 
using cryptographic hashing and smart contracts, ensuring that once data is recorded on 
the blockchain it cannot be altered. The system also introduces a dual-chain architecture 
consisting of a certificate chain for original credentials and a correction chain for 
updates or modifications. This design enhances transparency, traceability, and 
efficiency, allowing students and organizations to verify certificates instantly without 
relying on intermediaries.

5. **Certificate Verification and Validation Using Blockchain**
_Authors: Chittiprolu Saranya, Chittibomma Sai Sindhu, Ikkurthi Chandi Priya, 
Dantu Swathi, Anne Dhatri, Dr. A. Kalavathi 
[APR 2025, JETNR]_

This paper proposes a blockchain-based certificate verification system aimed at 
preventing the widespread issue of counterfeit academic certificates. In the traditional 
system, verification of educational credentials is often time-consuming and prone to 
manipulation due to the lack of transparency and secure storage mechanisms. The 
authors highlight that organizations and educational institutions require a reliable 
system to ensure the authenticity and integrity of academic records. 
The proposed system converts traditional paper certificates into digital certificates 
and stores their cryptographic hash values on a blockchain network. Each certificate is 
assigned a unique digital signature and a QR code that can be scanned to verify its 
authenticity. When a certificate is scanned, the system retrieves the corresponding 
information from the blockchain and confirms whether the certificate is valid. By 
combining blockchain security with QR code verification, the system provides a fast, 
transparent, and tamper-proof solution for academic credential verification.

5. **Blockchain-Based PKI: Making Digital Certificate Management More Secure and Efficient** 
_Authors: Sukhvinder Singh Bamber, Rajeev Kumar Dang, Naveen Dogra, Mohit 
Angurala 
[AUG 2025, IJARSCT]_
 
This paper discusses the role of digital certificates in ensuring secure communication 
and identity verification across digital platforms. Digital certificates form the core 
component of Public Key Infrastructure (PKI), enabling authentication, encryption, and 
secure data exchange across networks. The authors explain how traditional PKI systems 
rely heavily on centralized Certificate Authorities (CAs), which introduces 
vulnerabilities such as single points of failure, certificate authority compromise, and 
inefficient certificate revocation processes. The study also highlights the importance of 
SSL/TLS protocols in securing internet communications and explains how digital 
certificates help establish trust between communicating entities. 
The paper proposes a blockchain-based PKI model to address the limitations of 
traditional certificate management systems. In this approach, blockchain acts as a 
decentralized ledger that securely records certificate issuance, verification, and 
revocation events. Smart contracts automate certificate lifecycle management, while 
distributed consensus ensures transparency and immutability of records. The proposed 
model improves security, scalability, and trust by eliminating reliance on centralized 
authorities. It also enables real-time certificate verification and reduces the risk of fraud, 
making it suitable for applications in e-governance, IoT environments, and secure 
digital identity systems. 

6. **Blockchain-Based Decentralized Document Verification and Its Applications** 
_Authors: Ayush Mishra, Sakshi Mehta, Bhavya Oza, Sumit Kumar, Hemant 
Kasturiwale 
[JAN 2025, JISEM]_
 
This paper presents a blockchain-based decentralized framework for secure and 
efficient document verification, addressing the limitations of traditional methods such 
as high cost, manual effort, and vulnerability to fraud. The system integrates Ethereum 
blockchain and IPFS, where documents are stored off-chain in IPFS while only their 
cryptographic hash is recorded on the blockchain to ensure integrity and scalability. The 
workflow (shown in the system diagram on page 4) involves uploading documents 
through a decentralized application, generating a unique hash, and storing it immutably 
on the blockchain for verification. 
The proposed system demonstrates significant improvements in performance and 
reliability, achieving high accuracy (99.9%), faster verification time, and reduced 
manual effort compared to traditional systems . It also ensures transparency, tamper
proof storage, and secure access control among stakeholders such as applicants, 
institutions, and employers. Overall, the research highlights the potential of blockchain 
technology to revolutionize document verification by providing a scalable, secure, and 
trustworthy solution, while also identifying challenges like scalability and integration 
with legacy systems.

---

## CHAPTER-3 <br>EXISTING SYSTEM 
### 3.1 Introduction 
Several digital credential management systems have been developed to enable 
secure issuance and verification of certificates. Among them, Blockcerts, OpenCerts, 
and DigiLocker are widely recognized models that demonstrate different approaches to 
handling digital credentials. 
Blockcerts is an open standard for issuing and verifying digital certificates using 
blockchain technology. In this model, certificate data is digitally signed and its hash is 
stored on the blockchain, while the actual certificate is shared with the user. Verification 
is performed by matching the certificate’s hash with the blockchain record. OpenCerts 
is a blockchain-based platform that enables institutions to issue certificates as digitally 
signed files with embedded metadata. These certificates can be shared directly by users 
and verified by validating the digital signature and corresponding blockchain entry. The 
system focuses on standardized digital credential formats and verification. DigiLocker 
is a centralized digital document storage system developed by the Government of India 
for storing and accessing official records. Institutions can issue certificates directly to 
users’ accounts, where they are stored securely. Verification is carried out by retrieving 
documents from the centralized system and validating them against issuing authorities. 
These systems represent different architectural approaches to digital credential 
management, ranging from traditional centralized systems to modern blockchain-based 
decentralized models. Traditional systems primarily rely on physical documents or 
centralized databases maintained by institutions, where verification is performed 
manually or through direct authority validation. In contrast, newer approaches such as 
Blockcerts and OpenCerts utilize decentralized blockchain networks for secure and 
tamper-evident verification, while platforms like DigiLocker adopt a centralized digital 
repository for streamlined access and management. Together, these models highlight 
the evolution of credential management from manual and institution-dependent 
processes to more secure, digital, and technology-driven solutions.

### 3.2 Advantages 
1. Digital Accessibility, Certificates can be accessed, stored, and shared 
electronically without physical handling. 
2. Faster Verification, Digital systems reduce the time required to verify credentials 
compared to manual methods. 
3. Reduced Paperwork, Minimizes reliance on physical documents, simplifying 
storage and management. 
4. Improved Record Management, Structured storage helps institutions organize 
and retrieve data efficiently. 
5. Easy Integration, Systems can be integrated with existing institutional or 
government platforms for streamlined operations. 

### 3.3 Disadvantages 
1. Centralized Dependency, Many systems rely on a single authority, creating a 
potential single point of failure. 
2. Limited Transparency, Verification processes may not always be openly visible 
or independently verifiable. 
3. Security Risks, Centralized databases are vulnerable to data breaches, tampering, 
or unauthorized access. 
4. Scalability Issues, Managing large volumes of certificates across multiple 
institutions can be challenging. 
5. Interoperability Gaps, Lack of standardization makes it difficult for different 
systems to communicate seamlessly.

---

## CHAPTER-4 <br>PROPOSED SYSTEM 
### 4.1 Introduction 
The proposed system, EduCredChain, is a hybrid Blockchain–PKI based 
architecture designed to provide a secure, transparent, and reliable platform for 
managing educational credentials. Traditional certificate management systems often 
depend on manual verification processes or centralized databases, which are prone to 
data tampering, certificate forgery, unauthorized access, and inefficiencies in validation. 
To overcome these limitations, the proposed system integrates blockchain technology 
with robust cryptographic mechanisms to ensure the authenticity, integrity, and 
confidentiality of certificate data. In this system, when a certificate is issued, its data is 
derived to a unique cryptographic hash using SHA-256 algorithm. This hash acts as a 
digital fingerprint of the certificate, ensuring that even the slightest change in data 
results in a completely different hash value. The sensitive certificate data is encrypted 
using the issuer’s private key, ensuring secure storage and controlled access, and is then 
stored in a structured database. Simultaneously, the generated hash is recorded on the 
blockchain, creating an immutable and tamper-proof reference. Since blockchain 
records are inherently immutable and distributed, any attempt to modify the certificate 
data in the database can be easily detected. During verification, the system retrieves the 
stored certificate data, regenerates its hash, and compares it with the hash stored on the 
blockchain. If both hashes match, the certificate is considered authentic; otherwise, it is 
flagged as tampered or invalid. The system also incorporates certificate verification and 
revocation mechanisms to support the complete lifecycle of credentials. Users can verify 
certificates through a web-based interface by entering a unique certificate ID, enabling 
quick and reliable validation. In cases where a certificate needs to be invalidated, 
authorized users can revoke it, and the revocation status is permanently recorded on the 
blockchain. This ensures transparency, prevents misuse of revoked certificates, and 
enhances trust among institutions, employers, and users. Overall, EduCredChain 
provides a scalable, secure, and tamper-resistant solution for modern digital credential 
management.

### 4.2 Advantages  
1. Enhanced Security: Integration of cryptographic hashing and encryption ensures 
protection against certificate tampering and unauthorized access. 
2. Tamper Resistance: Storing certificate hashes on the blockchain ensures data 
immutability and prevents fraudulent modifications. 
3. Reliable Verification: Certificates can be verified quickly and accurately 
through blockchain validation. 
4. Transparency: Blockchain provides a transparent and traceable record of 
certificate issuance and revocation. 
5. Decentralized Trust: Verification does not rely solely on a central authority, 
increasing system reliability. 
6. Efficient Credential Management: Automates certificate issuance, verification, 
and revocation processes. 
7. Scalability: The architecture can be extended to support multiple institutions 
and credential types. 

### 4.3 Limitations 
1. Implementation Complexity: Integrating blockchain, cryptography, and web 
systems requires technical expertise. 
2. Higher Initial Setup Cost: Blockchain network setup and maintenance may 
require additional resources. 
3. Transaction Latency: Blockchain operations may introduce slight delays 
compared to traditional databases. 
4. Dependency on Cryptographic Key Management: Loss or compromise of 
cryptographic keys may affect data accessibility. 
5. System Integration Challenges: Integration with existing institutional systems 
may require additional customization.

---

## CHAPTER-5 <br>SYSTEM REQUIREMENTS 

### 5.1 Hardware Requirements 
The proposed system does not require specialized hardware and can be 
implemented using standard computing resources. The hardware requirements include: 
Processor: Intel Core i3 or higher 
RAM: Minimum 4 GB (8 GB recommended) 
Storage: Minimum 20 GB free disk space 
Network: Stable internet connection for blockchain communication 
Display: Standard monitor with minimum 1366×768 resolution 

### 5.2 Software Requirements 
The system is developed using modern programming and web technologies to 
ensure security and efficiency. 
Operating System: Windows / Linux / macOS 
Programming Language: Python 3.x 
Web Technologies: HTML, CSS, JavaScript 
Database: SQLite 
Cryptography Libraries: Python Cryptography Library (RSA, SHA-256) 
Blockchain Platform: Local or test blockchain network 
Development Environment: VS Code / PyCharm 
Web Browser: Google Chrome / Microsoft Edge / Firefox 

### 5.3 Expected System Requirements 
The expected system requirements define the core functionalities and 
operational behavior of the EduCredChain system. These requirements outline how 
the system performs certificate issuance, verification, and secure data management 
using blockchain and cryptographic techniques.

REQ 1: Certificate Issuance 
Description: The system must allow authorized users to issue digital certificates 
through a web interface. 
Input: Certificate details such as name, course ID, certificate number, issue date, 
and grade. 
Output: Encrypted certificate data stored in the database and corresponding hash 
recorded on the blockchain 
REQ 2: Certificate Hash Generation 
Description: The system must generate a unique SHA-256 hash for each 
certificate to ensure integrity. 
Input: Normalized certificate data fields. 
Output: A fixed-length cryptographic hash representing the certificate data. 
REQ 3: Secure Data Storage 
Description: The system must securely store certificate data using encryption in 
an off-chain database. 
Input: Certificate details from the issuance module. 
Output: Encrypted records stored in the SQL database with associated certificate 
ID. 
REQ 4: Blockchain Integration 
Description: The system must record certificate hashes on a blockchain network 
for immutability. 
Input: Generated certificate hash. 
Output: Transaction recorded on the blockchain with hash and identifier. 
REQ 5: Certificate Verification 
Description: The system must allow users to verify certificates using a unique 
certificate ID. 
Input: Certificate ID provided by the user. 
Output: Verification result indicating whether the certificate is valid, tampered, or 
invalid.
REQ 6: Certificate Revocation 
Description: The system must enable authorized users to revoke certificates when 
required. 
Input: Certificate ID selected for revocation. 
Output: Updated revocation status stored in the database and recorded on the 
blockchain. 
REQ 7: User Interface Interaction 
Description: The system must provide a user-friendly web interface for certificate 
operations. 
Input: User actions such as issuing, verifying, or revoking certificates. 
Output: Display of results, confirmations, and status messages. 
REQ 8: Data Integrity Validation 
Description: The system must validate certificate integrity by comparing 
recalculated hashes with blockchain records. 
Input: Stored certificate data and blockchain hash. 
Output: Confirmation of data integrity or detection of tampering. 
REQ 9: Blockchain Transaction Monitoring 
Description: The system must log and track blockchain transactions related to 
certificate operations. 
Input: Blockchain transaction details. 
Output: Transaction status and logs for transparency and auditing. 
### 5.4 Feasibility Study 
A feasibility study evaluates whether the proposed system is practical and 
beneficial for implementation. 
1. Technical Feasibility 
The proposed system is technically feasible as it utilizes widely available 
technologies such as Python, web development frameworks, cryptographic libraries, 
and blockchain platforms. The required tools and libraries are open-source and well
documented, making development and implementation achievable with available 
resources.
2. Operational Feasibility 
The system is designed with a simple and intuitive web interface, allowing issuers 
and users to interact with the system easily. Institutions can issue certificates digitally, 
and users can verify them quickly using the certificate ID. This improves operational 
efficiency and reduces manual verification processes. 
3. Economic Feasibility 
The system is economically feasible because it primarily uses open-source 
technologies and does not require expensive infrastructure. Implementation costs are 
minimal, limited mainly to development time and basic computing resources. 
4. Legal Feasibility 
The proposed system complies with general digital security and data protection 
principles. It ensures the confidentiality and integrity of certificate data using encryption 
and cryptographic techniques. Additionally, blockchain provides a transparent and 
verifiable record of credential issuance and revocation. 
5. Schedule Feasibility 
The development of the proposed system can be completed within a reasonable 
timeframe using available technologies. Since the system components such as web 
interfaces, database management, and cryptographic libraries are readily available, the 
project can be implemented within the planned academic project schedule.

### 5.5 Work Plan  
The development of the EduCredChain: A Hybrid Blockchain–PKI Architecture 
for Educational Credential Verification was planned and executed in a systematic 
manner. The project was divided into several phases to ensure smooth progress and 
timely completion. The following work plan outlines the major tasks carried out during 
the development process.  
1. Requirement Analysis & Feasibility Study 
Gather functional and non-functional requirements. Analyze system feasibility 
(technical, operational, economic, legal). Identify required technologies and tools 
Duration: 1 Week 
2. System Design & Architecture Planning 
Design overall system architecture and module structure. Plan database schema 
for certificate storage. Design blockchain interaction workflow. Prepare UML 
diagrams and system flow diagrams 
Duration: 1 Week 
3. Backend Development 
Develop backend logic using Python. Implement certificate issuance, verification, 
and revocation modules. Integrate cryptographic functions such as SHA-256 hashing 
and RSA encryption. Implement API communication between frontend and backend 
Duration: 2 Weeks 
4. Database and Blockchain Integration 
Implement SQLite database for certificate data storage. Store encrypted 
certificate 
data and hash values in the database. Integrate blockchain network for storing 
certificate hashes. Implement blockchain-based verification and revocation 
mechanisms 
Duration: 1 Week 
5. Web Interface Development 
Design and implement user interface using HTML, CSS, and JavaScript. Develop 
pages for certificate issuance, verification, and revocation. Ensure smooth interaction 
between frontend and backend through APIs 
Duration: 1 Week
6. System Integration and Testing 
Integrate all system modules including frontend, backend, database, and 
blockchain. Perform functionality testing and debugging. Verify the accuracy of 
certificate verification and revocation processes. Conduct security and integrity 
validation 
Duration: 1 Week 
7. Documentation and Final Deployment 
Prepare project documentation and technical report. Create system diagrams, 
flowcharts, and explanations. Deploy the system for demonstration and presentation 
Duration: 1 Week

---

## CHAPTER-6 <br>SYSTEM MODEL 
### 6.1 ARCHITECTURE DESIGN 
Architecture Design refers to the high-level structure of a software system, 
defining its components, modules, and their interactions. The architecture of 
EduCredChain follows a hybrid model integrating a web-based user interface, backend 
processing system, database, and blockchain network. Users interact through the 
interface to issue, verify, or revoke certificates, while the backend handles data 
processing, hashing, and encryption. Certificate data is securely stored in the database, 
and its cryptographic hash is recorded on the blockchain to ensure immutability and 
integrity. This layered architecture enables secure communication between components 
and provides a reliable, tamper-resistant credential management system.
![GitHub Logo](https://github.com/Abhiram-ARS/EduCredChain/blob/main/Documents/Diagrams/Architecture_Diagram.jpg)

### 6.2 USE CASE DIAGRAM 
A Use Case Diagram is a visual representation of the interactions between users 
(actors) and the system. It shows the functional requirements of the system by depicting 
the various use cases (functions) that users can perform and how they interact with 
different components. 
![GitHub Logo](https://github.com/Abhiram-ARS/EduCredChain/blob/main/Documents/Diagrams/UseCase_Diagram.jpg)

### 6.3 SEQUENCE DIAGRAM 
The sequence diagram shows interactions between the user, backend, database, 
and blockchain. The system processes certificate data, generates a hash, and stores it 
securely while recording the hash on the blockchain. During verification, the hash is 
recalculated and compared with the blockchain record to confirm authenticity.
![GitHub Logo](https://github.com/Abhiram-ARS/EduCredChain/blob/main/Documents/Diagrams/Sequence_Diagram.jpg)

### 6.4 ACTIVITY DIAGRAM 
An Activity Diagram is a flowchart that models the workflow of a system or 
process. It shows the sequence of activities, decisions, and parallel processes, helping 
to visualize the logic of complex operations and the flow of control from one activity to 
another. 
![GitHub Logo](https://github.com/Abhiram-ARS/EduCredChain/blob/main/Documents/Diagrams/flowchart_1.png)

### 6.5 ENTITY-RELATIONSHIP DIAGRAM 
The ER diagram of the EduCredChain system represents the relationships 
between key entities such as certificates, users (issuers/verifiers), and blockchain 
records. It illustrates how certificate details are stored in the database along with 
associated attributes like certificate ID, student information, course data, and issue date. 
The diagram also shows the linkage between certificate records and their corresponding 
hash values stored on the blockchain. This structured representation helps in 
understanding data organization, relationships, and efficient management of certificate 
information within the system.
![GitHub Logo](https://github.com/Abhiram-ARS/EduCredChain/blob/main/Documents/Diagrams/ER_Diagram.jpg)

---

## CHAPTER-7 <br>IMPLEMENTATION 
The system is implemented using a combination of web technologies, Python
based backend processing, cryptographic techniques, and a blockchain network to 
ensure secure and efficient certificate management. This chapter describes the key 
components of the implementation, including the certificate processing module, secure 
data storage, and blockchain-based verification and revocation mechanisms. 

### 7.1 Blockchain Infrastructure Module 
7.1.1 Core Blockchain Framework 
The Blockchain Infrastructure Module acts as the core foundation, 
enabling 
secure, 
decentralized, 
and 
tamper-proof 
certificate 
management.Blockchain technology is used to store cryptographic hashes of 
issued certificates, ensuring immutability. Once recorded on the blockchain, 
certificate data cannot be altered or deleted. 
7.1.2 Distributed Ledger Implementation 
Ethereum (locally implemented via Ganache) is used to maintain a 
distributed ledger. The ledger is accessible to authorized users, ensuring 
transparency and trust. This setup enables a controlled blockchain environment 
for development and testing. 
7.1.3 Transaction Validation Mechanism 
Certificate-related processes such as issuance and verification are validated 
through blockchain mechanisms. transaction is recorded securely, maintaining 
consistency across the network. This eliminates the need for centralized control 
in verification processes. 
7.1.4 Security and Integrity Features 
The infrastructure enhances data integrity by ensuring tamper-proof 
storage of certificate hashes. It enables real-time verification of credentials using 
blockchain records. The system remains reliable, scalable, and resistant to fraud 
due to its decentralized design. 

### 7.2 Certificate Hash Generation 
7.2.1 Input Normalization 
Certificate fields are preprocessed by converting text values to lowercase 
and removing unnecessary spaces. The name, Course ID, and certificate number 
are normalized, while issue date and grade are preserved in original format. This 
ensures consistency and prevents mismatches during verification. 
7.2.2 Hash Generation 
The concatenated data is passed into the SHA-256 algorithm. A fixed
length, tamper-proof hash is generated for each certificate. 
7.2.3 Mathematical Representation 
The hash generation process is defined as: 
**H = 𝐒𝐇𝐀𝟐𝟓𝟔(𝐥𝐨𝐰𝐞𝐫(𝐧) || 𝐥𝐨𝐰𝐞𝐫(𝐜) || 𝐥𝐨𝐰𝐞𝐫(𝐜𝐧) || 𝐝 || 𝐠)** 
Where: 
H = Generated certificate hash 
n = Name 
c = Course ID 
cn = Certificate Number 
d = Issue Date 
g = Grade 
|| = Concatenation operator 

### 7.3 Data Storage Architecture 
7.3.1 Hybrid Storage Model 
The system uses a hybrid architecture dividing data between off-chain and on
chain storage. This approach ensures efficiency, scalability, and security in 
managing certificates. 
7.3.2 On-Chain Storage Layer 
Only cryptographic hashes of certificates are stored on the blockchain 
(Ethereum). Minimal identifiers are stored along with the hash to ensure 
immutability and tamper resistance. This reduces storage cost and avoids 
inefficiency of storing full certificates on-chain. 
7.3.3 Off-Chain Storage Layer 
Actual certificate data and metadata are encrypted and stored in a SQL
based database. Stored details include student information, course data, certificate 
number, issue date, and grade. This enables faster access and reduces storage 
overhead. 
7.3.4 Certificate Issuance Process 
Certificate data is first stored securely in the database. A hash is generated 
from the stored data. The generated hash is recorded on the blockchain using 
smart contracts. 
7.3.5 Verification Process 
The system retrieves certificate data from the database during verification. 
A new hash is generated and compared with the blockchain record. Matching 
hashes confirm the authenticity of the certificate. 
7.3.6 System Benefits 
Ensures data integrity through hash validation. Reduces blockchain load 
and operational costs. Provides high performance and scalability for large-scale 
adoption. 

---

## CHAPTER-8 <br>RESULT & DISCUSSION 

### 8.1 Index Page
![GitHub Logo](https://github.com/Abhiram-ARS/EduCredChain/blob/main/Documents/Output/1_IndexPage.jpg)
illustrates the index page of the EduCredChain system, which serves 
as the main interface for users to access different functionalities. It provides navigation 
options for certificate issuance, verification, and revocation. The interface is designed 
to be simple and user-friendly, allowing users to interact with the system efficiently. 
This page acts as the entry point for all certificate management operations. 

### 8.2 Certificate Issue Page 
![GitHub Logo](https://github.com/Abhiram-ARS/EduCredChain/blob/main/Documents/Output/2_CertificateIssue.jpg)
Illustrates the certificate issuance interface where authorized users 
input essential certificate details such as name, course ID, certificate number, issue date, 
and grade through a structured web form. Once the data is submitted, the backend 
system preprocesses and normalizes the inputs before generating a unique cryptographic 
hash using the SHA-256 algorithm. The certificate data is then securely encrypted and 
stored in the database, ensuring confidentiality and efficient retrieval. Simultaneously, 
the generated hash is recorded on the blockchain using smart contracts, providing an 
immutable reference for future verification. This interface ensures a secure, consistent, 
and tamper-resistant process for issuing digital certificates while maintaining data 
integrity and transparency.

### 8.3 Certificate Verification Page
![GitHub Logo](https://github.com/Abhiram-ARS/EduCredChain/blob/main/Documents/Output/3_CertifiacateVerification.jpg)
Illustrates the certificate verification interface that allows users to 
validate the authenticity of a certificate using its unique identifier. When a request is 
submitted, the system retrieves the corresponding certificate data from the database and 
processes it through the backend. A new cryptographic hash is generated using the same 
method applied during issuance, ensuring consistency in verification. This recalculated 
hash is then compared with the hash stored on the blockchain to check for any 
discrepancies. Based on the comparison, the system determines whether the certificate 
is valid, tampered, or invalid, providing a reliable and secure verification mechanism.

### 8.4 Certificate Revocation 
![GitHub Logo](https://github.com/Abhiram-ARS/EduCredChain/blob/main/Documents/Output/4_CertificateRevocation.jpg)
Illustrates the certificate revocation interface used by authorized users 
to invalidate a certificate when required. Through this interface, users can specify the 
certificate to be revoked using its unique identifier, after which the backend processes 
the request securely. The system updates the certificate status in the database and 
records the revocation status on the blockchain to ensure immutability and transparency. 
During future verification attempts, the system checks this status to prevent the use of 
revoked certificates. This mechanism strengthens the overall integrity and 
trustworthiness of the credential management system.

### 8.5 Retrieving Tampered Data from Database
![GitHub Logo](https://github.com/Abhiram-ARS/EduCredChain/blob/main/Documents/Output/5_TamperedDB.jpg)
Illustrates the process of retrieving tampered certificate data from the 
database to demonstrate the system’s integrity validation mechanism. When certificate 
data is accessed, the system recalculates its cryptographic hash using the stored values. 
This newly generated hash is then compared with the original hash recorded on the 
blockchain. If any mismatch is detected, it indicates that the certificate data has been 
altered or compromised. This process highlights the system’s ability to identify 
tampering and effectively prevent fraudulent use of modified certificates.

### 8.6 Checking an invalid Certificate
![GitHub Logo](https://github.com/Abhiram-ARS/EduCredChain/blob/main/Documents/Output/6_BlockNotFound.jpg)
Illustrates the validation of an invalid certificate within the system, 
where a certificate that does not correspond to any stored or recognized record is 
submitted for verification. The system attempts to retrieve the associated data and 
generate a hash, but fails to find a matching blockchain entry. As a result, the certificate 
is identified as invalid and rejected by the system. This process ensures that only 
legitimate and registered certificates are accepted. It enhances the reliability and 
robustness of the verification mechanism by preventing unauthorized or fake credentials.

### 8.7 Checking a Revoked Certificate
![GitHub Logo](https://github.com/Abhiram-ARS/EduCredChain/blob/main/Documents/Output/7_RevokedCertVerify.jpg)
Illustrates the verification of a revoked certificate in the system, where 
a certificate with valid data is checked against its current status. During the verification 
process, the system retrieves the certificate details and compares the generated hash with 
the blockchain record to confirm integrity. In addition to hash validation, the system 
checks the revocation status stored on the blockchain. If the certificate is marked as 
revoked, it is flagged as invalid despite having correct data. This ensures that revoked 
credentials cannot be reused or misused, maintaining the integrity of the system.

---

## CHAPTER-8  <br>FUTURE SCOPE 
EduCredChain system lies in expanding its capabilities to support a wider range of 
institutions and real-world applications. The system can be scaled to integrate multiple 
universities, certification authorities, and organizations into a unified blockchain 
network. Advanced technologies such as smart contracts can be incorporated to 
automate certificate issuance, verification, and revocation processes. Additionally, 
mobile applications and QR code-based verification can be developed to enhance 
accessibility and user convenience. The adoption of scalable blockchain solutions and 
cloud deployment can further improve system performance and reliability. 
**1. Multi-Institution Integration** 
The system can be extended to support multiple educational institutions and 
certification bodies on a shared platform. This allows different organizations to issue 
and verify certificates within a unified blockchain network. It enhances interoperability 
and reduces duplication of verification efforts. Such integration increases trust and 
collaboration between institutions. It also enables a standardized approach to digital 
credential management. 
**2. Smart Contract Automation** 
Smart contracts can be implemented to automate certificate issuance, verification, 
and revocation processes. These contracts execute predefined rules without human 
intervention, ensuring transparency and consistency. Automation reduces manual errors 
and speeds up operations. It also enhances security by eliminating reliance on 
centralized control. This makes the system more efficient and reliable. 
**3. Mobile Application Development** 
Developing a mobile application can improve accessibility and user convenience. 
Users can issue, verify, and manage certificates directly from their smartphones. Mobile 
apps can provide real-time notifications and quick verification features. This enhances 
usability for both institutions and end-users. It also increases adoption by making the 
system more user-friendly.
**4. Integration with Government Systems** 
The system can be integrated with government databases and digital identity 
platforms. This ensures official validation and increases the credibility of issued 
certificates. It can help in streamlining national-level education and employment 
verification processes. Such integration reduces fraudulent claims and enhances trust. It 
also supports wider adoption across public sectors. 
**5. Enhanced Security Mechanisms** 
Advanced security techniques can be incorporated to strengthen the system. Features 
like multi-signature authentication and zero-knowledge proofs can be implemented. 
These methods provide additional layers of protection for sensitive data. Proper key 
management practices can further improve security. This ensures that the system 
remains robust against cyber threats. 
**6. Scalable Blockchain Solution** 
To handle a large number of transactions, scalable blockchain solutions can be 
adopted. Technologies like Layer-2 scaling or efficient consensus mechanisms can 
improve performance. This reduces transaction latency and operational costs. It ensures 
that the system can support growth in users and institutions. Scalability is essential for 
real-world deployment. 
**7. QR Code-Based Verification** 
QR codes can be added to certificates for instant verification. Scanning the QR code 
can directly fetch certificate details and blockchain validation status. This simplifies the 
verification process for employers and institutions. It also reduces the need for manual 
input of certificate IDs. QR-based systems improve speed and user experience. 
**8. AI-Based Fraud Detection**
Artificial Intelligence can be integrated to detect fraudulent activities and anomalies. 
AI models can analyze patterns in certificate usage and identify suspicious behavior. 
This adds an intelligent layer of security to the system. It helps in preventing misuse and 
unauthorized modifications. AI can continuously improve system reliability through 
learning.

---

## CHAPTER-9 <br>CONCLUSION 
The proposed system, EduCredChain, successfully demonstrates a secure and 
efficient approach to digital certificate management using a combination of blockchain 
technology and cryptographic techniques. By generating and storing certificate hashes 
on the blockchain while maintaining encrypted data in a database, the system ensures 
data integrity, authenticity, and resistance to tampering. The implementation of issuance, 
verification, and revocation mechanisms provides a complete lifecycle solution for 
managing educational credentials. 
The system addresses major limitations of traditional certificate verification 
methods, such as fraud, manual verification delays, and lack of transparency. Through 
automation and decentralized validation, it enhances trust among institutions, employers, 
and users. Additionally, the use of widely available technologies makes the system 
practical and feasible for real-world deployment. 
In conclusion, EduCredChain provides a reliable, scalable, and future-ready 
solution for secure credential verification. With further enhancements such as smart 
contracts, mobile applications, and large-scale integration, the system has the potential 
to significantly transform the way educational and professional credentials are issued 
and verified.

---

## CHAPTER -10  <br>REFERENCES 
1. Dongare, Krutant, et al. “Verification and Validation of Certificate Using Blockchain." 
International Journal for Research in Applied Science and Engineering Technology (IJRASET), vol. 13, no. 11, 2025, doi:10.22214/ijraset.2025.75385. 
2. Godase, Kunal, et al. “Blockchain Technology for Secure Digital Certificate Generation and Verification."
International Journal of Creative Research Thoughts (IJCRT), vol. 13, no. 3, Mar. 2025, 
3. Raju, G., et al. “Blockchain Driven Credential Issing and Verification of Certificates."
Global Journal of Engineering Innovations & Interdisciplinary Research, vol. 5, no. 2, 2025, 
4. Saranya, C., et al. "Certificate Verification and Validation Using Blockchain." 
International Research Journal of Modernization in Engineering Technology and Science (2023). 
5. Bamber, Sukhvinder Singh, et al. “Blockchain-Based PKI: Making Digital Certificate Management More Secure and Efficient." 
International Journal of Advanced Research in Science, Communication and Technology, vol. 5, no. 2, Aug. 2025, doi:10.48175/IJARSCT-28707. 
6. Mishra, Ayush, et al. “Blockchain-Based Decentralized Document Verification and Its Applications." 
Journal of Information Systems Engineering and Management, vol. 10, no. 10s, 2025. 
7. Rao, M. Chandra, et al. "VERIFICATION AND VALIDATION OF CERTIFICATE USING BLOCKCHAIN." 
Turkish Journal of Computer and Mathematics Education 14.3 (2023): 1211-1216. 
8. Gayathiri, A., J. Jayachitra, and S. Matilda. "Certificate validation using blockchain."
2020 7th International Conference on Smart Structures and Systems (ICSSS). IEEE, 2020.
9. Saleh, Omar S., Osman Ghazali, and Muhammad Ehsan Rana. "Blockchain based framework for educational certificates verification." 
Journal of critical reviews (2020). 
10.  Kubilay, Murat Yasin, Mehmet Sabir Kiraz, and Hacı Ali Mantar. "CertLedger: A new PKI model with Certificate Transparency based on blockchain." 
Computers & Security 85 (2019): 333-352. 
11.  Kumar, K. Dinesh, P. Senthil, and D. M. Kumar. "Educational certificate verification system using blockchain." 
international journal of scientific & technology research 9.3 (2020): 82-85. 
12.  Garba, Abba, et al. "LightLedger: A novel blockchain-based domain certificate authentication and validation scheme." 
IEEE Transactions on Network Science and Engineering 8.2 (2021): 1698-1710.

---

## APPENDIX – I 

### A.1.1 Python code to Connect to Blockchain Network 
The Python code establishes a connection to the blockchain network (Ethereum via 
Ganache) using Web3 to enable interaction with smart contracts and transaction 
processing.
```
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
```

### A.1.2 Certificate Issue  
 
The Python code handles certificate issuance by processing input data, generating a 
SHA-256 hash, storing certificate details in the database, and recording the hash on the 
blockchain. 

 ```
def issue_certificate(self,data): 
 
        now = datetime.now() 
 
        name = data["studentName"] 
        course_id = data["course"] 
        certificate_no = data["certid"] 
        issue_date = now.strftime("%d-%m-%y") 
        grade = data["grade"] 
 
        cert_hash = self.generate_certificate_hash( 
            name, course_id, certificate_no, issue_date, grade 
        ) 
         
        self.sqlecc.add_record([certificate_no,name, course_id, issue_date,  
                                                                                                         
grade,cert_hash.hex()]) 
 
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

```

### A.1.3 Certificate Verification 
 
The Python code performs certificate verification by retrieving stored data, regenerating 
the hash, and comparing it with the blockchain record to validate authenticity. 
```
def verify_certificate(self, data): 
 
        print(data) 
        row = 
[data['studentName'],data['course'],data['certid'],data['date'],data['grade']] 
         
        # Recompute hash  
        recalculated_hash = self.generate_certificate_hash( 
            row[0], row[1], row[2], row[3], row[4] 
        ) 
 
        recalculated_hash = recalculated_hash.hex() 
 
        if isinstance(recalculated_hash, bytes): 
             
            try: 
                text = recalculated_hash.decode("utf-8") 
                cert_hash = bytes.fromhex(text)   
 
            except Exception: 
                cert_hash = recalculated_hash 
 
        elif isinstance(recalculated_hash, str): 
            cert_hash = bytes.fromhex(recalculated_hash) 
        else: 
             
            return{"status":0, 
                   "Error":"EB02", 
                   "Message": "DB_Decryption_Error"} 
 
        try: 
            exists, revoked, issued_at, revoked_at = 
self.contract.functions.verifyCertificate( 
                cert_hash 
            ).call() 
```

### A.1.4 Certificate Revocation 
 
The Python code handles certificate revocation by updating the certificate status in the 
database and recording the revocation on the blockchain to prevent further use. 

```
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

```

### A.1.5 Database Operations 
 
The Python code performs database operations by inserting certificate data into the 
database and retrieving records for verification and management processes. 
 
```
def add_record(self, data): 
        cert_no, name, course_id, issue_date, grade, hash_val = data 
 
        name_enc = self.rsa_encrypt(name) 
        course_enc = self.rsa_encrypt(course_id) 
        grade_enc = self.rsa_encrypt(grade) 
 
        self.cursor.execute(""" INSERT INTO records (Certificate_No, Name,    
                Course_ID, Issue_Date, Grade, Hash) VALUES (?, ?, ?, ?, ?, ?) """,  
               (cert_no, name_enc, course_enc, issue_date, grade_enc, hash_val)) 
        self.conn.commit() 
 
def select_record(self, cert_no): 
        self.cursor.execute("SELECT * FROM records WHERE Certificate_No = ?", 
                          
(cert_no,)) 
        row = self.cursor.fetchone() 
        if row:            
            cert_no, name, course_id, issue_date, grade, hash_val = row 
 
            name = self.rsa_decrypt(name) 
            course_id = self.rsa_decrypt(course_id) 
            grade = self.rsa_decrypt(grade) 
 
            return (cert_no, name, course_id, issue_date, grade, hash_val)   
         
        return None
```

### A.1.6 RSA Encryption & Decryption 
 
The Python code implements RSA encryption and decryption to securely protect 
certificate data and ensure that only authorized parties can access or read the information. 

``` 
def rsa_encrypt(self,data): 
        key_path = os.path.join(os.path.dirname(__file__), "key", "public.pem") 
        with open(key_path, "rb") as f: 
            public_key = serialization.load_pem_public_key(f.read()) 
 
        encrypted = public_key.encrypt( 
            data.encode(), 
            padding.OAEP( 
                mgf=padding.MGF1(algorithm=hashes.SHA256()), 
                algorithm=hashes.SHA256(), 
                label=None 
            ) 
        ) 
 
        return base64.b64encode(encrypted).decode() 
     
def rsa_decrypt(self,data): 
 
        key_path = os.path.join(os.path.dirname(__file__), "key", "private.pem") 
        with open(key_path, "rb") as f: 
            private_key = serialization.load_pem_private_key( 
                f.read(), 
                password=None 
            ) 
 
        decrypted = private_key.decrypt( 
            base64.b64decode(data), 
            padding.OAEP( 
                mgf=padding.MGF1(algorithm=hashes.SHA256()), 
                algorithm=hashes.SHA256(), 
                label=None 
            ) 
        ) 
 
        return decrypted.decode()

```

---

## APPENDIX – II 
### A.II.1 Ganache Local Blockchain Setup Screenshot 
The Ganache Local Blockchain Setup Screenshot displays the simulated Ethereum 
environment used for testing the EduCredChain system. It shows multiple generated 
accounts along with their respective addresses, private keys, and available balances. The 
interface also presents details of transactions, blocks, and gas usage, providing a clear 
view of blockchain activity. This setup enables a controlled environment for deploying 
smart contracts and recording certificate hashes without using a live network. 

![GitHub Logo](https://github.com/Abhiram-ARS/EduCredChain/blob/main/Documents/Output/GanacheInterface.jpg)

### A.II.2 SQLite Database Structure (certificates.db) 
 
The screenshot displays the structure of the certificates.db SQLite database used in the 
EduCredChain system. It shows the records table where only the certificate ID is visible 
in readable form, while all other fields such as name, course ID, issue date, grade, and 
hash are stored in encrypted format. This ensures confidentiality and protects sensitive 
certificate data from unauthorized access. The database functions as the off-chain 
storage layer, supporting secure storage and retrieval during certificate operations. 

![GitHub Logo](https://github.com/Abhiram-ARS/EduCredChain/blob/main/Documents/Output/DataBase_Raw.jpg)

### A.II.3 Flask Backend Execution and Server Logs 
The screenshot displays the Flask backend server running the EduCredChain 
application along with real-time execution logs. It shows the server initialization, API 
request handling, and responses generated during certificate operations such as issuance, 
verification, and revocation. The logs provide insight into backend processing, 
including data handling, hashing, and blockchain interactions. This demonstrates the 
proper functioning and communication between the frontend, backend, database, and 
blockchain components.

![GitHub Logo](https://github.com/Abhiram-ARS/EduCredChain/blob/main/Documents/Output/Backend_Log.jpg)

---
