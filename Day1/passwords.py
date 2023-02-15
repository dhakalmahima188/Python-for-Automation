#! python

import sys, pyperclip


passwords = {
'email' : 'dsfsfsa6',
'fb' : 'd4s6ds6ds6d' 

    }

# sys.argv[0] --> pw sys.argv[1] ---> aid1

account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])

