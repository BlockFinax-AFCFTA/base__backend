# API Descriptions

first_description = """
Generates a secure 12/24-word mnemonic phrase that can be imported into any supported wallet application.
This phrase adheres to BIP-39 standards and ensures compatibility across wallets supporting stablecoin transactions.

Usage Example:
{
  "phrase": "abandon ability able about above absent absorb abstract absurd abuse access accident"
}
"""

second_description = """
Generates wallet addresses for the following stablecoins based on the provided mnemonic phrase:
- USDT
- USDC
- DAI

This endpoint ensures deterministic wallet generation for seamless integration with external platforms.
All stablecoins use the same wallet address on the Binance Smart Chain.

Usage Example:
{
  "wallets": {
    "USDT": "0xabc...", //
    "USDC": "0xabc...", //
    "DAI": "0xabc..."   //
  }
}
"""

third_description = """
Fetches the current balance of the provided wallet address for the specified stablecoin (USDT, USDC, or DAI).

Limitations:
- This endpoint has usage restrictions on the number of times it can be called due to API rate limits from blockchain providers.
- Balances are retrieved from Binance Smart Chain token contracts using ERC-20 standard methods.

Usage Example:
{
  "data": 0,
  "status_code": 200,
  "success": true,
  "message": "string"
}
"""

fourth_description = """
Fetches the transaction history for the provided wallet address and stablecoin symbol (USDT, USDC, or DAI).
Each transaction includes an identifier to distinguish between received and sent transactions.

Transaction DTO Example:
{
  "data": [
    {
      "hash": "string",
      "transaction_type": "sent",
      "amount": 0,
      "timestamp": "string",
      "hashUrl": "string",
      "gas_used": 0.0,
      "contract_address": "0x55d398326f99059fF775485246999027B3197955" // Example USDT contract address
    }
  ],
  "status_code": 200,
  "success": true,
  "message": "string"
}
"""

fifth_description = """
Broadcasts a stablecoin transaction to the Binance Smart Chain network.
This endpoint handles the signing and submission of the token transfer transaction.

Supported Stablecoins:
- USDT
- USDC
- DAI

Contract Addresses:
- USDT: 0x55d398326f99059fF775485246999027B3197955
- USDC: 0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d
- DAI: 0x1AF3F329e8BE154074D8769D1FFa4eE058B1DBc3

Usage Example:
{
  "data": {
    "transaction_hash": "0x1234...",
    "gas_used": 100000,
    "gas_price": "5000000000"
  },
  "status_code": 200,
  "success": true,
  "message": "Transaction successfully broadcasted"
}
"""