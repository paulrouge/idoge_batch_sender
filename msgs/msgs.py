class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
msg_step_one = f"""{bcolors.HEADER}{bcolors.BOLD}\n
    --------------------------------------------------------------------------------
    **********         Welcome to the awesome iDoge TX Batch Sender       **********
    {bcolors.HEADER}--------------------------------------------------------------------------------
    
    {bcolors.WARNING}You are about to send iDoge to all the addresses in the addresses.txt file.
    I will ask you the amount of iDoge and the password of the keystore file later on.
    {bcolors.ENDC}
    
    {bcolors.FAIL}*** IMPORTANT: Put in 1 address per line and put nothing else in there. ***
            
                >>>>>>  *** ONE LINE = ONE ADDRESS ***  <<<<<<\n {bcolors.ENDC}
            
                     {bcolors.BOLD}{bcolors.OKBLUE}Are you sure you want to continue?{bcolors.ENDC}\n
                     {bcolors.BOLD}(y/n)\n"""
    

msg_step_two = f"""{bcolors.BOLD}{bcolors.OKBLUE}\n
        Are you sure the keystore file is the one of the wallet you want to use?\n\n{bcolors.ENDC}
 
        {bcolors.BOLD}(y/n)\n\n\n"""
    

msg_step_three = f"""{bcolors.BOLD}{bcolors.OKBLUE}\n
        How much iDoge do you want to send to each address?\n\n{bcolors.ENDC}{bcolors.BOLD}"""
    

def msg_step_six(addresses):
    return input(f"""\n{bcolors.BOLD}
    {bcolors.OKBLUE}Are you sure you want to send iDoge to all the addresses in the addresses.txt file?
    {bcolors.ENDC}{bcolors.BOLD}
    There are {bcolors.OKGREEN}{len(addresses)}{bcolors.ENDC}{bcolors.BOLD} addresses in the file. 
    
    {bcolors.BOLD}(y/n)\n\n""")

def msg_final(amount_to_send, addresses):
    return input(F"""\n\n{bcolors.BOLD}{bcolors.WARNING}
    ARE YOU REALLY SURE?
    
    YOU ARE ABOUT TO SEND:

    A TOTAL OF {bcolors.OKBLUE}{amount_to_send * len(addresses) }{bcolors.WARNING} IDOGE TO {bcolors.OKBLUE}{len(addresses)} {bcolors.WARNING}ADDRESSES.
    {bcolors.ENDC}

    {bcolors.BOLD}(y/n)\n\n""")
    
msg_main = f"""{bcolors.OKBLUE}
    
    
    Now I will create transactions and save them in a txt file in the {bcolors.OKGREEN}{bcolors.UNDERLINE}/tx_reports{bcolors.ENDC}{bcolors.BOLD}{bcolors.OKBLUE} directory. 
    Please wait while I'm working on it... It will take a while. (about 2 seconds per address)
    """

msg_done = f'''\n{bcolors.WARNING}
            All done!\n\n
            {bcolors.OKBLUE}Check the {bcolors.OKGREEN}{bcolors.UNDERLINE}/tx_reports{bcolors.ENDC}{bcolors.BOLD}{bcolors.OKBLUE} directory for the transactions.
                
            Please realize that the fact a transaction hash is created, {bcolors.WARNING}it does not 
            mean that the transaction was successful.{bcolors.OKBLUE}You can check the transaction by
            clicking the link in the file.

            Make sure to pass on the iDoge love <3!!
    \n\n
    '''
def printDoge():
    print(f"""{bcolors.OKCYAN}
                    ▄              ▄
                  ▌▒█           ▄▀▒▌
                  ▌▒▒█        ▄▀▒▒▒▐
                 ▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐
               ▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐
             ▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌        {bcolors.WARNING}WOOW, SO VERY EASY!{bcolors.OKCYAN}
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