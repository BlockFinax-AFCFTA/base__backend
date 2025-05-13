from typing import List
from bip_utils import (
   Bip39SeedGenerator, Bip44,
    Bip44Coins
)
from bitcoinlib.keys import HDKey
from mnemonic import Mnemonic
from django.conf import settings
from helper.coingeko_api import get_coins_value
from helper.wallet_balance import get_usdt_balance, get_usdc_balance, get_dai_balance
from home.wallet_schema import Symbols, WalletInfoResponse, TokenType

def generate_mnemonic():
    mnemo = Mnemonic("english")
    return mnemo.generate(strength=128)

def generate_wallets_from_seed(seed_phrase) -> List[WalletInfoResponse]:
    # Generate seed from mnemonic
    seed_bytes = Bip39SeedGenerator(seed_phrase).Generate()

    # Derive wallets for each stablecoin
    wallets = []
    coinValue = get_coins_value()
    base_url = f"{settings.SITE_URL}/media/icons"

    # We'll use Ethereum as the base network for all our stablecoins
    # as they commonly run as ERC-20 tokens on Ethereum
    eth_wallet = Bip44.FromSeed(seed_bytes, Bip44Coins.ETHEREUM).DeriveDefaultPath()
    eth_address = eth_wallet.PublicKey().ToAddress()
    eth_private_key = eth_wallet.PrivateKey().Raw().ToHex()

    # USDT (Tether)
    usdt_balance = get_usdt_balance(eth_address)
    price_usdt = usdt_balance * coinValue['tether']['usd']
    change_usdt_hr = coinValue['tether']['usd_24h_change']
    volume_usdt = coinValue['tether']['usd']

    usdt_info = WalletInfoResponse(
        name="USDT (Tether)", 
        icon_url=f'{base_url}/usdt_icon.svg', 
        idName='tether', 
        symbols=Symbols.USDT, 
        volume=volume_usdt, 
        address=eth_address,
        private_key=eth_private_key,
        balance=round(usdt_balance, 6), 
        price=price_usdt, 
        changes=round(change_usdt_hr, 3),
        token_type=TokenType.TOKEN  # Set to TOKEN type instead of default NATIVE
    )
    wallets.append(usdt_info)

    # USDC (USD Coin)
    usdc_balance = get_usdc_balance(eth_address)
    price_usdc = usdc_balance * coinValue['usd-coin']['usd']
    change_usdc_hr = coinValue['usd-coin']['usd_24h_change']
    volume_usdc = coinValue['usd-coin']['usd']

    usdc_info = WalletInfoResponse(
        name="USDC (USD Coin)", 
        icon_url=f'{base_url}/usdc_icon.svg', 
        idName='usd-coin', 
        symbols=Symbols.USDC, 
        volume=volume_usdc, 
        address=eth_address,
        private_key=eth_private_key,
        balance=round(usdc_balance, 6), 
        price=price_usdc, 
        changes=round(change_usdc_hr, 3),
        token_type=TokenType.TOKEN  # Set to TOKEN type instead of default NATIVE
    )
    wallets.append(usdc_info)

    # DAI
    dai_balance = get_dai_balance(eth_address)
    price_dai = dai_balance * coinValue['dai']['usd']
    change_dai_hr = coinValue['dai']['usd_24h_change']
    volume_dai = coinValue['dai']['usd']

    dai_info = WalletInfoResponse(
        name="DAI", 
        icon_url=f'{base_url}/dai_icon.svg', 
        idName='dai', 
        symbols=Symbols.DAI, 
        volume=volume_dai, 
        address=eth_address,
        private_key=eth_private_key,
        balance=round(dai_balance, 6), 
        price=price_dai, 
        changes=round(change_dai_hr, 3),
        token_type=TokenType.TOKEN  # Set to TOKEN type instead of default NATIVE
    )
    wallets.append(dai_info)

    binance_wallet = Bip44.FromSeed(seed_bytes, Bip44Coins.BINANCE_SMART_CHAIN).DeriveDefaultPath()
    bsc_address = binance_wallet.PublicKey().ToAddress()
    bsc_private_key = binance_wallet.PrivateKey().Raw().ToHex()

    usdt_bep20_balance = get_usdt_balance(bsc_address)  # Assuming this function can handle BEP20 tokens

    usdt_bep20_info = WalletInfoResponse(
        name="USDT BEP20", 
        icon_url=f'{base_url}/usdt_icon.svg', 
        idName='tether-bep20', 
        symbols=Symbols.USDT, 
        volume=volume_usdt,  # Using the same market volume data as ERC20 USDT
        address=bsc_address,
        private_key=bsc_private_key,
        balance=round(usdt_bep20_balance, 6), 
        price=price_usdt,  # Using the same price as ERC20 USDT
        changes=round(change_usdt_hr, 3),  # Using the same price change as ERC20 USDT
        token_type=TokenType.TOKEN  # Set to TOKEN type instead of default NATIVE
    )
    wallets.append(usdt_bep20_info)


    return wallets