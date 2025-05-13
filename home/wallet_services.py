from typing import List
from helper.generate_wallet import generate_mnemonic, generate_wallets_from_seed
from helper.send_transaction.send_usdt import send_usdt
from helper.send_transaction.send_usdc import send_usdc
from helper.send_transaction.send_dai import send_dai
from helper.wallet_balance import get_usdt_balance, get_usdc_balance, get_dai_balance
from helper.wallet_transaction import get_usdt_transactions, get_usdc_transactions, get_dai_transactions
from home.wallet_schema import HTTPStatusCode, SendTransactionDTO, Symbols, TransactionsInfo, WalletInfoResponse, WalletResponseDTO
import traceback

def generate_secrete_phrases()->WalletResponseDTO[str]:
  try:
    phrases = generate_mnemonic()
    return WalletResponseDTO(data=phrases, message="Phrases generated")
  except Exception as ex:
    return WalletResponseDTO(message=str(ex), status_code=HTTPStatusCode.BAD_REQUEST, success=False)

def import_from_phrases(phrase:str)->WalletResponseDTO[List[WalletInfoResponse]]:
  try:
    val = generate_wallets_from_seed(phrase)
    return WalletResponseDTO(data=val, message="Wallet Generated")
  except Exception as ex:
    error_message = f"{str(ex)}\n{traceback.format_exc()}"
    return WalletResponseDTO(message=error_message, success=False, status_code=HTTPStatusCode.BAD_REQUEST)

def get_wallet_balance(symbols:Symbols, address:str)->WalletResponseDTO[float]:
  try:
    switch={
      Symbols.USDT: lambda: get_usdt_balance(address=address),
      Symbols.USDC: lambda: get_usdc_balance(address=address),
      Symbols.DAI: lambda: get_dai_balance(address=address),
    }
    value = switch.get(symbols, lambda: "Invalid Symbols")()

    if not isinstance(value, float):
      raise Exception("Invalid Symbol")

    return WalletResponseDTO(data=value, message="Ballance gotten")
  except Exception as ex:
    return WalletResponseDTO(message=str(ex), success=False, status_code=HTTPStatusCode.BAD_REQUEST)

def get_all_transactions_history(symbols:Symbols, address:str)-> WalletResponseDTO[List[TransactionsInfo]]:
  try:
    switch = {
      Symbols.USDT: lambda: get_usdt_transactions(address),
      Symbols.USDC: lambda: get_usdc_transactions(address),
      Symbols.DAI: lambda: get_dai_transactions(address),
    }
    value = switch.get(symbols, lambda: "Invalid Symbols")()

    return WalletResponseDTO(data=value, message="Transaction List")
  except Exception as ex:
    return WalletResponseDTO(message=str(ex), success=False, status_code=HTTPStatusCode.BAD_REQUEST)

def send_crypto_transaction(symbols:Symbols, req:SendTransactionDTO)->WalletResponseDTO[str]:
  try:
    switch = {
      Symbols.USDT: lambda: send_usdt(req),
      Symbols.USDC: lambda: send_usdc(req),
      Symbols.DAI: lambda: send_dai(req),
    }
    send_function = switch.get(symbols, None)
    
    if send_function is None:
      raise ValueError(f"Invalid symbol: {symbols}")

    send_function()
    return WalletResponseDTO(data="Successful", message="Transaction sent Successfully")
  except Exception as ex:
    error_message = f"{str(ex)}\n{traceback.format_exc()}"
    print(error_message)
    return WalletResponseDTO(message=error_message, success=False, status_code=HTTPStatusCode.BAD_REQUEST)