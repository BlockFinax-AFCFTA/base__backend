from typing import List
import requests
from django.conf import settings

from home.wallet_schema import TransactionType, TransactionsInfo

# Function to get transactions for USDT on Ethereum
def get_usdt_transactions(address) -> List[TransactionsInfo]:
    """
    Get USDT transaction history for an Ethereum address.
    USDT contract address: 0xdAC17F958D2ee523a2206206994597C13D831ec7 (Ethereum Mainnet)
    """
    try:
        # EtherScan API endpoint for token transactions
        tx_url = f"https://api.etherscan.io/api"
        params = {
            "module": "account",
            "action": "tokentx",
            "contractaddress": "0xdAC17F958D2ee523a2206206994597C13D831ec7",  # USDT contract address
            "address": address,
            "sort": "desc",
            "apikey": settings.ETH_API_KEY
        }
        
        response = requests.get(tx_url, params=params)
        transactions = response.json().get("result", [])

        formatted_transactions: List[TransactionsInfo] = []
        for tx in transactions:
            txHashUrl = f'https://etherscan.io/tx/{tx["hash"]}'
            tx_type = TransactionType.SENT if tx["from"].lower() == address.lower() else TransactionType.RECEIVED
            val = TransactionsInfo(
                hash=tx["hash"], 
                hashUrl=txHashUrl, 
                transaction_type=tx_type, 
                amount=int(tx["value"]) / 1e6,  # USDT has 6 decimals
                timestamp=tx["timeStamp"]
            )
            formatted_transactions.append(val)
        
        return formatted_transactions[:10]  # Return only the 10 most recent transactions
    except Exception as e:
        print(f"Error getting USDT transactions: {e}")
        return []

# Function to get transactions for USDC on Ethereum
def get_usdc_transactions(address) -> List[TransactionsInfo]:
    """
    Get USDC transaction history for an Ethereum address.
    USDC contract address: 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48 (Ethereum Mainnet)
    """
    try:
        # EtherScan API endpoint for token transactions
        tx_url = f"https://api.etherscan.io/api"
        params = {
            "module": "account",
            "action": "tokentx",
            "contractaddress": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",  # USDC contract address
            "address": address,
            "sort": "desc",
            "apikey": settings.ETH_API_KEY
        }
        
        response = requests.get(tx_url, params=params)
        transactions = response.json().get("result", [])

        formatted_transactions: List[TransactionsInfo] = []
        for tx in transactions:
            txHashUrl = f'https://etherscan.io/tx/{tx["hash"]}'
            tx_type = TransactionType.SENT if tx["from"].lower() == address.lower() else TransactionType.RECEIVED
            val = TransactionsInfo(
                hash=tx["hash"], 
                hashUrl=txHashUrl, 
                transaction_type=tx_type, 
                amount=int(tx["value"]) / 1e6,  # USDC has 6 decimals
                timestamp=tx["timeStamp"]
            )
            formatted_transactions.append(val)
        
        return formatted_transactions[:10]  # Return only the 10 most recent transactions
    except Exception as e:
        print(f"Error getting USDC transactions: {e}")
        return []

# Function to get transactions for DAI on Ethereum
def get_dai_transactions(address) -> List[TransactionsInfo]:
    """
    Get DAI transaction history for an Ethereum address.
    DAI contract address: 0x6B175474E89094C44Da98b954EedeAC495271d0F (Ethereum Mainnet)
    """
    try:
        # EtherScan API endpoint for token transactions
        tx_url = f"https://api.etherscan.io/api"
        params = {
            "module": "account",
            "action": "tokentx",
            "contractaddress": "0x6B175474E89094C44Da98b954EedeAC495271d0F",  # DAI contract address
            "address": address,
            "sort": "desc",
            "apikey": settings.ETH_API_KEY
        }
        
        response = requests.get(tx_url, params=params)
        transactions = response.json().get("result", [])

        formatted_transactions: List[TransactionsInfo] = []
        for tx in transactions:
            txHashUrl = f'https://etherscan.io/tx/{tx["hash"]}'
            tx_type = TransactionType.SENT if tx["from"].lower() == address.lower() else TransactionType.RECEIVED
            val = TransactionsInfo(
                hash=tx["hash"], 
                hashUrl=txHashUrl, 
                transaction_type=tx_type, 
                amount=int(tx["value"]) / 1e18,  # DAI has 18 decimals
                timestamp=tx["timeStamp"]
            )
            formatted_transactions.append(val)
        
        return formatted_transactions[:10]  # Return only the 10 most recent transactions
    except Exception as e:
        print(f"Error getting DAI transactions: {e}")
        return []

