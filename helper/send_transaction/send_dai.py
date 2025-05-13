from web3 import Web3
from home.wallet_schema import SendTransactionDTO

# Connect to Binance Smart Chain RPC
web3 = Web3(Web3.HTTPProvider("https://bsc-dataseed.binance.org/"))

# DAI Contract address on BSC
DAI_CONTRACT_ADDRESS = "0x1AF3F329e8BE154074D8769D1FFa4eE058B1DBc3"
DAI_ABI = [
    {
        "constant": False,
        "inputs": [
            {"name": "_to", "type": "address"},
            {"name": "_value", "type": "uint256"}
        ],
        "name": "transfer",
        "outputs": [{"name": "", "type": "bool"}],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]

def send_dai(req: SendTransactionDTO):
    try:
        account = web3.eth.account.from_key(req.private_key)
        if not web3.is_address(req.to_address):
            raise Exception("Invalid Address")
        if account.address != req.from_address:
            raise Exception("Incorrect address")
            
        # Create contract instance
        contract = web3.eth.contract(address=DAI_CONTRACT_ADDRESS, abi=DAI_ABI)
        
        # Get token decimals
        decimals = contract.functions.decimals().call()
        
        # Convert amount to token units
        token_amount = int(req.amount * (10 ** decimals))
        
        # Check token balance
        token_balance = contract.functions.balanceOf(account.address).call()
        if token_amount > token_balance:
            raise Exception("Insufficient DAI Balance")
            
        # Get nonce
        nonce = web3.eth.get_transaction_count(account.address)
        
        # Prepare transaction
        txn = contract.functions.transfer(
            req.to_address,
            token_amount
        ).build_transaction({
            'chainId': 56,
            'gas': 100000,
            'gasPrice': web3.eth.gas_price,
            'nonce': nonce,
        })
        
        # Sign and send transaction
        signed_txn = web3.eth.account.sign_transaction(txn, req.private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        tr = web3.eth.get_transaction_receipt(tx_hash)
        
        return tr, txn["gasPrice"]
    except Exception as ex:
        raise ex