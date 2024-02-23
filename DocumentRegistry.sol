pragma solidity ^0.8.0;

contract DocumentRegistry {
    struct Document {
        string name;
        address owner;
        bool exists;
    }

    mapping(string => Document) private documents;

    event DocumentRegistered(string indexed hash, string name, address indexed owner);
    
    modifier documentExists(string memory _hash) {
        require(documents[_hash].exists, "Document not found");
        _;
    }

    function registerDocument(string memory _hash, string memory _name) public {
        require(bytes(_hash).length > 0, "Hash cannot be empty");
        require(bytes(_name).length > 0, "Name cannot be empty");
        require(!documents[_hash].exists, "Document already exists");

        documents[_hash] = Document(_name, msg.sender, true);
        emit DocumentRegistered(_hash, _name, msg.sender);
    }

    function verifyDocument(string memory _hash) public view documentExists(_hash) returns (string memory, address) {
        Document memory doc = documents[_hash];
        return (doc.name, doc.owner);
    }
}
