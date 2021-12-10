import os
os.system('pkg install wget')
os.system('pkg install git')
# Color --------
B='\033[0;30m' # Black
R='\033[1;31m' # Red
G='\033[1;32m' # Green
Y='\033[1;33m' # Yellow
Bl='\033[1;34m' # Blue
P='\033[1;35m' # Purple
C='\033[1;36m' # Cyan
W='\033[1;37m' # Whit
# End Color -------

os.system('clear')

# Banner ---------
def banner():

    print(G+'  ____      _                 ____             _ ')
    print(G+' / ___|   _| |__   ___ _ __  |  _ \  __ _ _ __| | __')
    print(G+'''| |  | | | | '_ \ / _ \ '__| | | | |/ _` | '__| |/ / ''')
    print(G+'| |__| |_| | |_) |  __/ |    | |_| | (_| | |  |   < ')
    print(G+' \____\__, |_.__/ \___|_|    |____/ \__,_|_|  |_|\_\ ', R+'Cyber Dark Tools v1.0')
    print(G+'      |___/                                         ',R+'~ Code By Cyber Dark ~')
    print('')
    print(f'{Y}~ Code By Cyber Dark ~')
    print(Y+'~ Instagram: @CyberDarkCrew')
    print(Y+'~ Facebook : @CyberDarkCrew')
    print(Y+'~ Twitter  : @CyberDarkCrew')
    print(Y+'~ Github   : @CyberDarkCrew')
    print(Y+'~ Email    : Cyb3rD4rk@protonmail.com')
    
banner()

# EndBanner -----------
print(' ')
# Select Tool ----------


print(G+'Choose a Tools To Install')
print(G+' ')
print(G+'[00] - Update Tools')
print(G+'[01] - Update Termux or Linux')
print(G+'[02] - Exit')
print(G+'[03] - About')
print(G+'[04] - Remove Tool')
print(G+' ')
print(G+'[1] - Install Hash Encryption')
print(G+'[2] - Install Users Tiktok')
print(G+'[3] - Install DDos Attack')
print(G+'[4] - Install Spam Mail')
print(G+'[5] - Install Guess Facebook Password ')
print(G+'[6] - Install Check Hash')
print(G+' ')
select = input(G+'Select Tool :')
if select == '00':
    os.system(f'rm -r tools-cy.py')
    print(Y+'\nLoading Please Wait...\n')
    os.system('wget http://tools.cy-dark.surge.sh/tools-cy.py')
    print(G+'\n~ Installation finished ~')
    
elif select == '01':
    os.system('clear')
    print(Y+'\nPlease Select...')
    print(' ')
    print(Y+'[1] - Termux')
    print(Y+'[2] - Kali Linux')
    print(Y+'[3] - Wifislax')

    kaliortermux = input(G+'\nPlease Select :')
    
    if kaliortermux == '1':
        print(G+'updating...')
        os.system('pkg update')

    elif kaliortermux == '2':
        print(G+'\nupdating...')
        os.system('sudo apt-get update')
	
    elif kaliortermux == '3':
        print(G+'\nupdating...')
        os.system('sudo slapt-get --update')
	
    else:
    	print(R+'\nError Selected Please Try Again')	
    
elif select == '02':
    print(Y+'\nThank You For install Tools >.<')
    exit()
    
elif select == '03':
    os.system('clear')
    print(W+'''\n
           ~ who are we ! ~
  Cyber ​​Dark is a team of programmers
    and information security experts
    ''')
    print(R+'''
~ Cyber Dark Crew ~
    Telegram : 
        Mr.Dark : @L_N_X_0
        Mixail  : @M3x4il
        Hosin   : @Hosinballo
        Rasas   : @rasas772
        Omer    : @nice_nice

    Facebook :
        Mr.Dark : /L.N.X.01
        Fares   : /vinum.rivera
        Rasas   : /rasas772
        Hota    : /Hota.znta
        Frdinand: /mohamadyasen012

    ''')
elif select == '04':
    os.system('clear')
    print(R+'\nPlease Enter File Name')
    remove = input('\nFile Name :')
    os.system(f'rm -r {remove}')  
    print(G+'\n~ Done Delete File ~')
    
elif select == '1':
    print(Y+'\nLoading Please Wait...\n')
    os.system('rm -r hash-encryption')
    os.system('git clone https://github.com/CyberDarkCrew/hash-encryption.git')
    print(G+'\n~ Installation finished ~')

elif select == '2':
    print(Y+'\nLoading Please Wait...\n')
    os.system('rm -r users-tiktok')
    os.system('git clone https://github.com/CyberDarkCrew/users-tiktok.git')
    print(G+'\n~ Installation finished ~')

elif select == '3':
    print(Y+'\nLoading Please Wait...\n')
    os.system('rm -r ddos-attack')
    os.system('git clone https://github.com/CyberDarkCrew/ddos-attack.git')
    print(G+'\n~ Installation finished ~')

elif select == '4':
    print(Y+'\nLoading Please Wait...\n')
    os.system('rm -r spam-mail')
    os.system('git clone https://github.com/CyberDarkCrew/spam-mail.git')
    print(G+'\n~ Installation finished ~')
elif select == '5':
    print(Y+'\nLoading Please Wait...\n')
    os.system('rm -r guess-password')
    os.system('git clone https://github.com/CyberDarkCrew/guess-password.git')
    print(G+'\n~ Installation finished ~')
elif select == '6':
    print(Y+'\nLoading Please Wait...\n')
    os.system('rm -r check-hash')
    os.system('git clone https://github.com/CyberDarkCrew/check-hash.git')
    print(G+'\n~ Installation finished ~')
else:
    print(R+'\n Error Please Selected Try Again ...')