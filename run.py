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


# setting up some initial stuff
addresses = []
now = datetime.now()
PROVIDER = "https://ctz.solidwallet.io"
icon_service = IconService(HTTPProvider(PROVIDER, 3)) # // mainnet

def printDoge():
    print("""
                    ▄              ▄
                  ▌▒█           ▄▀▒▌
                  ▌▒▒█        ▄▀▒▒▒▐
                 ▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐
               ▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐
             ▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌
            ▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌
            ▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐
           ▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌
           ▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌
          ▌▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐
          ▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌
          ▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐
           ▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌
           ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐
            ▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌
              ▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀
                ▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀
                   ▒▒▒▒▒▒▒▒▒▒▀▀ 
    """)

# Welcome message
def step1():
    text = input("""\n
    --------------------------------------------------------------------------------
    **********         Welcome to the awesome iDoge TX Batch Sender       **********
    --------------------------------------------------------------------------------
    You are about to send iDoge to all the addresses in the addresses.txt file.
    I will ask you the amount of iDoge and the password of the keystore file later on.

    
    *** IMPORTANT: Put 1 address per line and put nothing else in there. ***
            
                >>>>>>  *** ONE LINE = ONE ADDRESS ***  <<<<<<\n
            
                    Are you sure you want to continue?\n\n(y/n)\n\n\n"""
    )

    if text == "y":
        step2()
    else:
        print('\n\nOkay whatever, bye.\n\n')
        sys.exit()

# Keystore check
def step2():
    text = input("""\n
    \n\nAre you sure the keystore file is the one of the wallet you want to use?\n\n
    \n\n(y/n)\n\n\n"""
    )
    if text == "y":
        step3()
    else:
        print('\n\nWell check that and come back after! Bye.\n\n')
        sys.exit()

# Amount of iDoge to be send
def step3():
    text = input("""
    \n\nHow much iDoge do you want to send to each address?\n\n"""
    )
    try:
        global amount_to_send
        amount_to_send = int(text)
    except:
        print('\n\nERROR - INPUT IS NOT A NUMBER - Run program again and enter a valid amount.\n\n')
        sys.exit()
    try:
        step4()
    except KeyStoreException as e:
        print(f'{e.code} - plessss try again\n\n')
        try: 
            step4()
        except KeyStoreException as e:
            print(f'{e.code} - Wrong again, shutting down, bye.\n\n\n')
            sys.exit()

# Get the password of the keystore file.
def step4():
    password = getpass.getpass(prompt='\n\nPassword of the Keystore file: ') 
    global wallet 
    wallet = KeyWallet.load("./keystore", password)
    try:
        step5()
    except Exception as e:
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
    text = input(f"""\n\n\n\n
    Are you sure you want to send iDoge to all the addresses in the addresses.txt file?
    
    There are {len(addresses)} addresses in the file. 
    
    (y/n)\n\n""")
    
    if text == "y":
        finalStep()
    else:
        print('\n\nOkay fix your stuff and try again, bye.\n\n')
        sys.exit()

def finalStep():
    text = input(F"""\n\n
    ARE YOU REALLY SURE?
    
    YOU ARE GONNA SEND:
    A TOTAL OF {amount_to_send * len(addresses) } IDOGE TO {len(addresses)} ADDRESSES.

    (y/n)\n\n""")
    
    if text != "y":
        print('\n\nOkay fix your stuff and try again, bye.\n\n')
        sys.exit()

        

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
    
    print("""
    Now I will create transactions and save them in a txt file in the /tx_reports directory. 

    Please realize that the fact a transaction hash is created it does not 
    mean that the transaction was successful. You can check the transaction by
    clicking the link in the file.

    Please wait will I'm working on it... It will take a while. (about 2 seconds per address)
    """)
    for address in addresses:
        try:
            #print(address)
            transact(address)
        except Exception as e:
            print(e)
            print(f'\nSomething went wrong trying to send to {address}\n')
    
    printDoge()
    print('''\n
            All done!\n\n
            Check the /tx_reports directory for the transactions.\n\n
            Make sure to pass on the iDoge love <3!!
    \n\n
    ''')

