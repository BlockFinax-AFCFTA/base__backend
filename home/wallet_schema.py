from ninja import Schema
from typing import Generic, TypeVar
from enum import Enum

T = TypeVar("T")

class PhraseRequest(Schema):
  phrase: str

class UserRequest(Schema):
  userId: str
  walletPin: str
  
class SendTransactionDTO(Schema):
  private_key: str
  amount: float
  to_address: str
  from_address: str
  coin_symbol: str = "usdt"

class Symbols(str, Enum):
  USDT = "usdt"
  USDC = "usdc"  # Added USDC
  DAI = "dai"    # Added DAI

class TokenType(str, Enum):
  NATIVE = "native"  # For native blockchain currencies (BTC, ETH, BNB, etc.)
  TOKEN = "token"    # For tokens on blockchains (USDT, USDC, DAI)

class HTTPStatusCode(int, Enum):
  OK = 200
  CREATED = 201
  BAD_REQUEST = 400
  UNAUTHORIZED = 401
  FORBIDDEN = 403
  NOT_FOUND = 404
  INTERNAL_SERVER_ERROR = 500

class WalletResponseDTO(Schema, Generic[T]):
  data: T = None
  status_code: HTTPStatusCode = HTTPStatusCode.OK
  success: bool = True
  message: str

class WalletInfoResponse(Schema):
  name: str
  address: str
  private_key: str
  balance: float
  symbols: Symbols
  price: float
  changes: float
  volume: float
  idName: str
  icon_url: str
  token_type: TokenType = TokenType.NATIVE

class TransactionType(str, Enum):
  SENT = "sent"
  RECEIVED = "received"

class TransactionsInfo(Schema):
  hash: str
  transaction_type: TransactionType
  amount: float
  timestamp: str
  hashUrl: str
  gas_used: float = 0.0
  contract_address: str = None