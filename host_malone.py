import os
import subprocess
from pathlib import Path
## Expand this list
main_programs = '''tilix vim htop nvtop iftop code telegram-desktop chromium steam-native dolphin-emu pcsx2 wireshark-qt \
aircrack-ng nmap neofetch yay
'''

print('optimize mirrorlist?')
print('[y/n]')
selection1 = input('> ')
if selection1 == "y":
    print('optimizing mirrorlist')
    with Bar('Optimizing mirrorlist...') as b:
        pass


elif selection1 == "n":
    print('bypassing...')
print('run system update?')
print('[y/n]')
selection2 = input('> ')
if selection2 == 'y':
    print('running system update')
    os.system('sudo -S pacman -Syyu')
    print('system update complete')
elif selection2 == 'n':
    print('bypassing...')
user = subprocess.getoutput('whoami')
hostname = subprocess.getoutput('hostname')


ssh_host_list = '''\
Host flexbox
    Hostname 98.162.158.190
    user modeseven
    Port 22'''


def ssh_config():
    #MUST BE RUN AS ROOT FOR THIS FUNCTION TO WORK
    print('configuring ssh')
    try:
        os.system(f'mkdir /home/{user}/.ssh/')
        print('directory created successfully')
    except:
        print('could not create .ssh directory')
        print('does it already exist?')
    os.system('ssh-keygen -t ed25519')
    if hostname == 'modeseven-flexbox':
        print('configuring for desktop')
        with open('/etc/ssh/sshd_config', 'r+') as sshd_config:
            sshd_config_lines = sshd_config.readlines()
            sshd_config.seek(0)
            for line in sshd_config_lines:
                if "PasswordAuthentication" not in line:
                    sshd_config.write(line)
            sshd_config.truncate()
            sshd_config.seek(1539)
            sshd_config.write('PasswordAuthentication no')
    else:    
        with open(f'/home/{user}/.ssh/config', 'w') as hostlist:
            hostlist.write(ssh_host_list)


def mypackages():
    print('installing custom package list')
    os.system(f'sudo -S pacman -S {main_programs}')


def dns_config():
    ## uses resolvectl
    print('setting dns nameservers')
    print('set [c]ustom ipv4 address or use [d]efault [dns.adguard.com]')
    os.system('systemctl enable systemd-resolved')
    dns_mode = input('> ')
    if dns_mode.lower() == 'c':
        print('enter some valid ipv4 addresses seperated by spaces')
        custom_dns_ip = input('> ')
        print('enter the interface to configure')
        custom_dns_interface = input('> ')
        os.system(f'resolvectl dns {custom_dns_interface} {custom_dns_ip}')      
    elif dns_mode.lower() == 'd':
        print('setting dns nameserver to adguard dns')
        print('enter the interface to configure')
        auto_interface = input('> ')
        os.system(f'resolvectl dns {auto_interface} 94.140.14.14 94.140.15.15')
    else:
        print('not a valid option')
        print('returning...')


aliases = '''alias mreset="clear && neofetch"
alias mls="ls -lsar"
alias x="exit"
alias cryptsetup="sudo cryptsetup" 
alias mount="sudo mount"
alias umount="sudo umount" 
alias iftop="sudo iftop" 
alias nmap="sudo nmap"
alias wireshark="sudo wireshark"'''


def zsh_config():
    print('editing zshrc')
    with open(f'/home/{user}/.zshrc', 'a+') as zshconf:
        zshconf.write(aliases)
        if hostname == 'modeseven-flexbox':
            zshconf.seek(0)
            zshconf.write('neofetch\n')


modelist = ['ssh_config', 'extension', 'dns_config', 'firewall_config', 'mypackages']
### Expand this list
menulist = '''
    *******************************************
    *******************************************
    *** ssh_config - configure ssh settings ***
    *** extensions - gnome extensions       ***
    *** dns_config - set dns nameservers    ***
    *** firewall_config - configure ufw     ***
    *** mypackages - installs my packaages  ***
    *** quit - exit program                 ***
    *** zshconfig - write to zshrc          ***
    *******************************************
    *******************************************
'''

## fix this shit
while True:
    print('MAIN MENU')
    print(menulist)
    mode = input('> ')
    if mode == 'mypackages':
        mypackages()
    elif mode == 'dns_config':
        dns_config()
    elif mode == 'ssh_config':
        ssh_config()
    elif mode == 'quit':
        break
    elif mode == 'extensions':
        #make that extensions function
        print('still under construction')
    elif mode ==  'firewall_config':
        #make firewall config function
        print('still under construction')
    elif mode == 'zshconfig':
        zsh_config()
    else:
        print('invalid selection')

print('exiting')
