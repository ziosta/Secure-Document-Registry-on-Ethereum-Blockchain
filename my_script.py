from web3 import Web3

# Ethereum ağına bağlan
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))  # Yerel Ethereum ağına bağlanıyorsa adresi güncelle

# Akıllı kontrat adresi ve ABI'si
contract_address = "CONTRACT_ADDRESS"  # Akıllı kontrat adresini buraya girin
contract_abi = [
    {
        "inputs": [],
        "name": "registerDocument",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "verifyDocument",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "string",
                        "name": "",
                        "type": "string"
                    },
                    {
                        "internalType": "address",
                        "name": "",
                        "type": "address"
                    }
                ],
                "internalType": "struct DocumentRegistry.Document",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

# Akıllı kontratı yükle
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# DocumentRegistry.sol'da tanımlanan akıllı kontrat fonksiyonlarını kullanarak etkileşime geç
def register_document(hash, name):
    tx_hash = contract.functions.registerDocument(hash, name).transact()
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print("Document registered successfully!")

def verify_document(hash):
    result = contract.functions.verifyDocument(hash).call()
    if result[0]:
        print(f"Document Name: {result[0]}, Owner: {result[1]}")
    else:
        print("Document not found!")

# Örnek kullanım
register_document("DOCUMENT_HASH", "Document Name")
verify_document("DOCUMENT_HASH")
