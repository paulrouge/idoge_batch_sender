from iconsdk.icon_service import IconService
from iconsdk.providers.http_provider import HTTPProvider
from iconsdk.builder.transaction_builder import (
    CallTransactionBuilder,  
)
from iconsdk.exception import KeyStoreException
from iconsdk.signed_transaction import SignedTransaction
from iconsdk.wallet.wallet import KeyWallet
import sys
import getpass
from datetime import datetime
from msgs.msgs import *
import os
import time

# setting up some initial stuff
addresses = []
now = datetime.now()
PROVIDER = "https://ctz.solidwallet.io"
icon_service = IconService(HTTPProvider(PROVIDER, 3)) # // mainnet

os.system('cls||clear')

# Welcome message
def step1():
    text = input(msg_step_one)
    if text == "y":
        os.system('cls||clear')
        step2()
    else:
        os.system('cls||clear')
        print('\n\nOkay whatever, bye.\n\n')
        sys.exit()

# Keystore check
def step2():
    text = input(msg_step_two)
    if text == "y":
        os.system('cls||clear')
        step3()
    else:
        os.system('cls||clear')
        print('\n\nWell check that and come back after! Bye.\n\n')
        sys.exit()

# Amount of iDoge to be send
def step3():
    text = input(msg_step_three)
    try:
        global amount_to_send
        amount_to_send = int(text)
    except:
        print('\n\n         ERROR - INPUT IS NOT A NUMBER - Run program again and enter a valid amount.\n\n')
        sys.exit()
    try:
        os.system('cls||clear')
        step4()
    except KeyStoreException as e:
        os.system('cls||clear')
        print(f'{e.code} - plessss try again\n\n')
        try: 
            os.system('cls||clear')
            step4()
        except KeyStoreException as e:
            os.system('cls||clear')
            print(f'{e.code} - Wrong again, shutting down, bye.\n\n\n')
            sys.exit()

# Get the password of the keystore file.
def step4():
    password = getpass.getpass(prompt=f'''
    \n\n        Password of the Keystore file: ''') 
    global wallet 
    wallet = KeyWallet.load("./keystore", password)
    try:
        os.system('cls||clear')
        step5()
    except Exception as e:
        os.system('cls||clear')
        print('Something went wrong, check the addresses.txt file and try again. Bye\n\n')
        sys.exit()

# get addresses from addresses.txt file
def step5():
    with open('addresses.txt', 'r') as f:
        _addresses = f.readlines()

    for address in _addresses:
        addresses.append(address.strip())
    
    step6()

def step6():
    text = msg_step_six(addresses)
    
    if text == "y":
        os.system('cls||clear')
        finalStep()
    else:
        print('\n\n     Okay fix your stuff and try again, bye.\n\n')
        sys.exit()

def finalStep():
    text = msg_final(amount_to_send, addresses)
    if text != "y":
        os.system('cls||clear')
        print('\n\n     Okay fix your stuff and try again, bye.\n\n')
        sys.exit()
    os.system('cls||clear')

        

def transact(address):
    amount = amount_to_send * 10**18
    
    params = {
        "_to": address,
        "_value": amount,
    }

    transaction = CallTransactionBuilder()\
        .from_(wallet.get_address())\
        .to("cx3fd4769e413657304d4928b95b88fd6eb53f9a8b")\
        .step_limit(1000000)\
        .nid(1)\
        .nonce(100)\
        .method("transfer")\
        .params(params)\
        .build()
    
    # Returns the signed transaction object having a signature
    signedtx = SignedTransaction(transaction, wallet)
    txhash = icon_service.send_transaction(signedtx)
    append_to_file(address, txhash)

def append_to_file(address, txhash):
    date_time = now.strftime("%Y-%m-%d_%H%M%S")
    with open(f'tx_reports/idoge_batch_{date_time}', 'a') as f:
        f.write(f'{address} -> https://tracker.icon.foundation/transaction/{txhash}\n')

def main():
    step1()

if __name__ == '__main__':
    main()
    
    print(msg_main)

    for address in addresses:
        try:
            transact(address)
        except Exception as e:
            print(e)
            print(f'\nSomething went wrong trying to send to {address}\n')
    
    printDoge()
    time.sleep(2)
    print(msg_done)

