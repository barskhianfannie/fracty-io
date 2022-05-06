from thirdweb import ThirdwebSDK
from web3 import Web3

from thirdweb import ThirdwebSDK
from eth_account import Account
from dotenv import load_dotenv
from web3 import Web3
import os

# Load environment variables into this file
load_dotenv()

# This PRIVATE KEY is coming from your environment variables. Make sure to never put it in a tracked file or share it with anyone.
PRIVATE_KEY = os.environ.get("PRIVATE_KEY")

# Add your own RPC URL here or use a public one
RPC_URL = "https://rpc-mumbai.maticvigil.com"

# Instantiate a new provider to pass into the SDK
provider = Web3(Web3.HTTPProvider(RPC_URL))

# Optionally, instantiate a new signer to pass into the SDK
signer = Account.from_key(PRIVATE_KEY)

# Finally, you can create a new instance of the SDK to use
sdk = ThirdwebSDK(provider, signer)

nft_collection = sdk.get_nft_collection("0xd9145CCE52D386f254917e481eB44e9943F39138")

RPC_URL = "https://rpc-mumbai.maticvigil.com"


provider = Web3(Web3.HTTPProvider(RPC_URL))


sdk = ThirdwebSDK(provider)

#0xd9145CCE52D386f254917e481eB44e9943F39138