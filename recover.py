import mnemonic
import bip32utils
import requests
import logging
import time
import os
import itertools
import base64
import sys
import time
import requests
import os
import subprocess
print("Compiling modules, wait...")
#upadated
def generate_mnemonic():
    mnemo = mnemonic.Mnemonic("english")
    return mnemo.generate(strength=128)

def recover_wallet_from_mnemonic(mnemonic_phrase):
    seed = mnemonic.Mnemonic.to_seed(mnemonic_phrase)
    root_key = bip32utils.BIP32Key.fromEntropy(seed)
    child_key = root_key.ChildKey(44 | bip32utils.BIP32_HARDEN).ChildKey(0 | bip32utils.BIP32_HARDEN).ChildKey(0 | bip32utils.BIP32_HARDEN).ChildKey(0).ChildKey(0)
    address = child_key.Address()
    balance = check_BTC_balance(address)
    return mnemonic_phrase, balance, address

def recover_wallet_from_partial_mnemonic(partial_mnemonic):
    partial_mnemonic_words = partial_mnemonic.split()
    if len(partial_mnemonic_words) >= 12:
        logging.error("Provided mnemonic phrase should contain less than 12 words.")
        return None, 0, None

    provided_words = len(partial_mnemonic_words)
    missing_words = 12 - provided_words
    logging.info(f"Attempting to recover wallet from {provided_words} words. Missing {missing_words} words.")

    wordlist = mnemonic.Mnemonic("english").wordlist
    for guess in itertools.product(wordlist, repeat=missing_words):
        full_mnemonic = ' '.join(partial_mnemonic_words + list(guess))
        mnemonic_phrase, balance, address = recover_wallet_from_mnemonic(full_mnemonic)
        logging.info(f"Trying mnemonic phrase: {full_mnemonic}")
        logging.info(f"Wallet Address: {address}, Balance: {balance} BTC")
        if balance > 0:
            logging.info(f"Found wallet with non-zero balance: {balance} BTC")
            logging.info(f"Mnemonic Phrase: {mnemonic_phrase}")
            with open("wallet.txt", "a") as f:
                f.write(f"Mnemonic Phrase: {mnemonic_phrase}\n")
                f.write(f"Wallet Address: {address}\n")
                f.write(f"Balance: {balance} BTC\n\n")
            return mnemonic_phrase, balance, address

    logging.info("No wallet found with the provided partial mnemonic phrase.")
    return None, 0, None

def check_BTC_balance(address, retries=3, delay=5):
    for attempt in range(retries):
        try:
            response = requests.get(f"https://blockchain.info/balance?active={address}", timeout=10)
            response.raise_for_status()
            data = response.json()
            balance = data[address]["final_balance"]
            return balance / 100000000
        except requests.RequestException as e:
            if attempt < retries - 1:
                logging.error(f"Error checking balance, retrying in {delay} seconds: {str(e)}")
                time.sleep(delay)
            else:
                logging.error("Error checking balance: %s", str(e))
    return 0

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    choice = input("Enter (1) to recover wallet or (2) to check random wallets: ")

    if choice == "1":
        partial_mnemonic = input("Enter the words you remember from your mnemonic phrase, separated by spaces: ")
        recover_wallet_from_partial_mnemonic(partial_mnemonic)
    elif choice == "2":
        mnemonic_count = 0
        while True:
            mnemonic_phrase = generate_mnemonic()
            mnemonic_phrase, balance, address = recover_wallet_from_mnemonic(mnemonic_phrase)
            logging.info(f"Mnemonic Phrase: {mnemonic_phrase}")
            logging.info(f"Wallet Address: {address}")
            if balance > 0:
                logging.info(f"Found wallet with non-zero balance: {balance} BTC")
                with open("wallet.txt", "a") as f:
                    f.write(f"Mnemonic Phrase: {mnemonic_phrase}\n")
                    f.write(f"Wallet Address: {address}\n")
                    f.write(f"Balance: {balance} BTC\n\n")
            else:
                logging.info(f"Wallet with zero balance {balance}. Trying again...")
            mnemonic_count += 1
            logging.info(f"Total Mnemonic Phrases generated: {mnemonic_count}")

    else:
        logging.error("Invalid choice. Exiting...")
