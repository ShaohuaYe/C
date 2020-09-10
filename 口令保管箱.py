
import sys,pyperclip
print(sys.argv)

PASSWORDS = {'github':{'ShaohuaYe':'lenovoreaper123'},
             'B站':'lenovoreaper'
             }

if len(sys.argv) < 2 :
    print('Usage:python 口令保管箱.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

print(account)

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('PASSWORD for '+ account + 'copied to clipboard')
else:
    print('There is no account named '+ account)

# print(pyperclip.paste())































