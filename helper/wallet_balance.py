import requests
from django.conf import settings
from web3 import Web3
from xrpl.clients import JsonRpcClient
from xrpl.account import get_balance
from tronpy import Tron

def get_usdt_balance(address):
    """
    Get USDT balance for an Ethereum address.
    USDT contract address: 0xdAC17F958D2ee523a2206206994597C13D831ec7 (Ethereum Mainnet)
    """
    try:
        # Connect to Ethereum node
        infura_url = 'https://mainnet.infura.io/v3/'+settings.INFURA
        web3 = Web3(Web3.HTTPProvider(infura_url))

        # USDT Contract ABI (minimal ABI for balanceOf)
        abi = [
            {
                "constant": True,
                "inputs": [{"name": "_owner", "type": "address"}],
                "name": "balanceOf",
                "outputs": [{"name": "balance", "type": "uint256"}],
                "type": "function"
            }
        ]

        # USDT contract address on Ethereum
        contract_address = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
        
        # Create contract instance
        token_contract = web3.eth.contract(
            address=Web3.to_checksum_address(contract_address), 
            abi=abi
        )

        # Get balance
        balance = token_contract.functions.balanceOf(
            Web3.to_checksum_address(address)
        ).call()
        
        # USDT has 6 decimals
        return balance / 1e6
    except Exception as e:
        print(f"Error getting USDT balance: {e}")
        return 0

def get_usdc_balance(address):
    """
    Get USDC balance for an Ethereum address.
    USDC contract address: 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48 (Ethereum Mainnet)
    """
    try:
        # Connect to Ethereum node
        infura_url = 'https://mainnet.infura.io/v3/'+settings.INFURA
        web3 = Web3(Web3.HTTPProvider(infura_url))

        # USDC Contract ABI (minimal ABI for balanceOf)
        abi = [
            {
                "constant": True,
                "inputs": [{"name": "_owner", "type": "address"}],
                "name": "balanceOf",
                "outputs": [{"name": "balance", "type": "uint256"}],
                "type": "function"
            }
        ]

        # USDC contract address on Ethereum
        contract_address = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
        
        # Create contract instance
        token_contract = web3.eth.contract(
            address=Web3.to_checksum_address(contract_address), 
            abi=abi
        )

        # Get balance
        balance = token_contract.functions.balanceOf(
            Web3.to_checksum_address(address)
        ).call()
        
        # USDC has 6 decimals
        return balance / 1e6
    except Exception as e:
        print(f"Error getting USDC balance: {e}")
        return 0

def get_dai_balance(address):
    """
    Get DAI balance for an Ethereum address.
    DAI contract address: 0x6B175474E89094C44Da98b954EedeAC495271d0F (Ethereum Mainnet)
    """
    try:
        # Connect to Ethereum node
        infura_url = 'https://mainnet.infura.io/v3/'+settings.INFURA
        web3 = Web3(Web3.HTTPProvider(infura_url))

        # DAI Contract ABI (minimal ABI for balanceOf)
        abi = [
            {
                "constant": True,
                "inputs": [{"name": "_owner", "type": "address"}],
                "name": "balanceOf",
                "outputs": [{"name": "balance", "type": "uint256"}],
                "type": "function"
            }
        ]

        # DAI contract address on Ethereum
        contract_address = "0x6B175474E89094C44Da98b954EedeAC495271d0F"
        
        # Create contract instance
        token_contract = web3.eth.contract(
            address=Web3.to_checksum_address(contract_address), 
            abi=abi
        )

        # Get balance
        balance = token_contract.functions.balanceOf(
            Web3.to_checksum_address(address)
        ).call()
        
        # DAI has 18 decimals
        return balance / 1e18
    except Exception as e:
        print(f"Error getting DAI balance: {e}")
        return 0
