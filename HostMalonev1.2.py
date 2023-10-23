import os, socket
from text_border import TextBorder

tb = TextBorder()

main_packages = "vim tilix htop nvtop code telegram-desktop nmap neofetch dolphin-emu"
flatpaks = "steam"

aliases = '''\
alias mreset="clear && neofetch"
alias mls="ls -lsar"
alias x="exit"
alias cryptsetup="sudo cryptsetup" 
alias mount="sudo mount"
alias umount="sudo umount" 
alias iftop="sudo iftop" 
alias nmap="sudo nmap"
alias wireshark="sudo wireshark"'''

main_menu = '''\
1) quit
2) install my packages 
3) configure dns
4) configure python venv
5) configure zshrc
6) configure firewall
'''

print("Update pacman mirrorlist?")
print("[Y/N]")
mirror_selection = input("//>")
if mirror_selection.upper() == 'Y': os.system("sudo -S pacman-mirrors --fasttrack 30")
if mirror_selection.upper() == 'N': print("skipping")
else: print("invalid selection. Skipping.")
print("Run System Update?")
print("[Y/N]")
update_selection = input('//>')
if update_selection.upper() == 'Y': os.system('sudo -S pacman -Syyu')
if update_selection.upper() == 'N': print("skipping.")
else: print("invalid selection. Skipping.")


def configure_venv():
    os.mkdir("/home/modeseven/python_venv")
    os.system("python -m venv /home/modeseven/python_venv")
    with open("/home/modeseven/.zshrc", 'a') as zshrc:
        zshrc.write('\n')
        zshrc.write("source /home/modeseven/pyhton_venv/bin/activate")


def install_packages():
    print("Installing main packages")
    os.system(f"sudo -S pacman -S {main_packages}")
    os.system(f"flatpak install {flatpaks}")


def configure_dns():
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


def configure_zshrc():
    print('editing zshrc')
    with open(f'/home/modeseven/.zshrc', 'a+') as zshconf:
        zshconf.write(aliases)
        if socket.gethostname() == 'modeseven-flexbox':
            zshconf.seek(0)
            zshconf.write('neofetch\n')


while True:
    print(tb.single_border(main_menu))
    main_selection =  input("Enter//Selection> ")
    if main_selection == '1': break
    elif main_selection == '2': install_packages()
    elif main_selection == '3': configure_dns()
    elif main_selection == '4': configure_venv()
    elif main_selection == '5': configure_zshrc()
    elif main_selection == '6': print("under construction")
    else: print("Enter a number 1-6")



