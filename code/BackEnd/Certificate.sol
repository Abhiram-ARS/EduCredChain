/*
Project Title : EduCredChain
Description   : Blockchain-Based Certificate Verification System

File Name     : Certificate.sol
Description   : Smart contract for managing certificate issuance, verification, and revocation on the blockchain

Author(s)     : ABHIRAM_S, AMARNATH MOHAN, MOHAMMED YASEEN

Last Modified : 18-04-2026
*/

pragma solidity ^0.8.17;

contract CertificateRegistry {

    address public owner;

    struct Certificate {
        uint256 issuedAt;
        bool exists;
        bool revoked;
        uint256 revokedAt;
    }

    mapping(bytes32 => Certificate) private certificates;

    event CertificateIssued(bytes32 certHash, uint256 issuedAt);
    event CertificateRevoked(bytes32 certHash, uint256 revokedAt);

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    function issueCertificate(bytes32 certHash) public onlyOwner {

        require(!certificates[certHash].exists, "Certificate already exists");

        certificates[certHash] = Certificate(
            block.timestamp,
            true,
            false,
            0
        );

        emit CertificateIssued(certHash, block.timestamp);
    }

    function revokeCertificate(bytes32 certHash) public onlyOwner {

        require(certificates[certHash].exists, "Certificate not found");
        require(!certificates[certHash].revoked, "Already revoked");

        certificates[certHash].revoked = true;
        certificates[certHash].revokedAt = block.timestamp;

        emit CertificateRevoked(certHash, block.timestamp);
    }

    function verifyCertificate(bytes32 certHash)
        public
        view
        returns (
            bool exists,
            bool revoked,
            uint256 issuedAt,
            uint256 revokedAt
        )
    {
        Certificate memory cert = certificates[certHash];

        return (
            cert.exists,
            cert.revoked,
            cert.issuedAt,
            cert.revokedAt
        );
    }
}
