from thirdweb import ThirdwebSDK
from eth_account import Account
from web3 import Web3

# You can switch out this provider and RPC URL for your own
provider = Web3(Web3.HTTPProvider("http://ethereum-rpc.com"))
# This will create a random account to use for signing transactions
signer = Account.create()

sdk = ThirdwebSDK(provider, signer)
contract = sdk.get_marketplace("0x6b7b27E9Cea40055f752b3c365F0ACCA67E91d64")



listings = contract.get_active_listings()
price_of_first = listings[0].price
print(price_of_first)