# The Mega Ultra iDoge Batch Sender

A simple Python script to send multiple **iDoge** transactions at once. 

# Important!
Make sure that you create a new wallet with a unique password for this script. Especially when you are not very experienced with programming. Keep only a bit of ICX in this wallet to make sure you can pay the transaction fees. Same for the iDoge, only send the amount you want to send with this script to the wallet you have created for this little program.

## 1. Install requirements

In your terminal run:

`$ pip install -r requirements.txt`

This will install the packages needed by Python to run the script on your computer. You will only have to do this once.

## 2. Replace keystore

The **keystore** is your wallet. You can create a wallet with Hana or Iconex. Make sure to remember the password you use on creation, you will need the password each time you use **Mega Ultra iDoge Batch Sender**.

> Make sure that in the correct keystore file is in the same directory as run.py and that the name of the keystore file is '**keystore**' *(so no extension)*.

## 3. The receive addresses

**Important**: In the `addresses.txt` file you put all the addresses to which you want to send iDoge. Replace the dummy addresses I have put in there with the real addresses.

**Every address needs to be on a seperate line, without any comma's or stuff.**

## 4. Run

Type:

`$ python3 run.py`


## Follow the steps

Follow the program step by step. You will be asked how many iDoge you want to send to each address and what the password of the keystore is.

> do not delete, rename or relocate any files! You only replaced the keystore file with you own keystore file.


## Finished

The program created a transaction hash for every address on each line in the `addresses.txt` file. There is a file created in the /tx_reports directory. This file contains every address and icontracker-link with a matching transaction hash.

If icontracker does not find the transaction hash it means the transaction did not get accepted. This could be because:

* The wallet (/keystore) you are using does not have enough iDoge in it
* Tt has not enough ICX in it (to pay for the transaction fees) 
* The address was not correct.

> Be careful with re-running the program, make sure you update the addresses.txt file before running it again to prevent double pay outs!
