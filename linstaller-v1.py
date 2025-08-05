import subprocess
import sys
import time

# Categories
def arch_category():
        subprocess.run("clear", shell=True)
        print("1. Gaming")
        print("2. Productivity")
        print("3. Tweaks")
        print("4. Tools")
        print("0. Exit")
        arch_choice = input("Choose a category (1-4): ").strip().lower()

        match arch_choice:
                case "1":
                        return arch_gaming()
                case "2":
                        return arch_productivity()
                case "3":
                        return arch_tweaks()
                case "4":
                        return arch_tools()
                case "0":
                        sys.exit()
                case _:
                        print("Invalid choice. Please try again.")
                        time.sleep(2)
                        return arch_category()

def arch_gaming():
        subprocess.run("clear", shell=True)
        print("1. Lutris - Managing Game Stores")
        print("2. Steam - Game Marketplace and Launcher")
        print("3. Heroic Games Launcher - Managing Game Stores")
        print("4. WINE - Newest Stable Release")
        print("5. WINE Testing - Experimental Release")
        print("6. WineTricks - Newest Stable Release")
        print("7. Proton-UpQt - Managing Proton, WINE-GE and other compatibility tools")
        print("0. Go Back")

        arch_gaming_choice = input("Choose a gaming package (1-7): ").strip().lower()

        match arch_gaming_choice:
                case "1":
                        subprocess.run("sudo pacman -S lutris", shell=True)
                        return arch_gaming()
                case "2":
                        subprocess.run("sudo pacman -S steam", shell=True)
                        return arch_gaming()
                case "3":
                        subprocess.run("sudo pacman -S heroic-games-launcher", shell=True)
                        return arch_gaming()
                case "4":
                        subprocess.run("sudo pacman -S wine", shell=True)
                        return arch_gaming()
                case "5":
                        subprocess.run("sudo pacman -S wine-staging", shell=True)
                        return arch_gaming()
                case "6":
                        subprocess.run("sudo pacman -S winetricks", shell=True)
                        return arch_gaming()
                case "7":
                        subprocess.run("sudo pacman -S protonup-qt", shell=True)
                        return arch_gaming()
                case "0":
                        return arch_category()
                case _:
                        print("Invalid choice. Please try again.")
                        time.sleep(2)
                        return arch_gaming()

def arch_productivity():
        subprocess.run("clear", shell=True)
        print("1. Office Suites")
        print("2. Photo Editing")
        print("3. Video Editing")
        print("4. Media Players/Viewers")
        print("0. Go Back")

        arch_productivity_choice = input("Choose productivity group (1-4): ").strip().lower()

        match arch_productivity_choice:
                case "1":
                        arch_productivity_officesuites()
                case "2":
                        arch_productivity_photoediting()
                case "3":
                        arch_productivity_videoediting()
                case "4":
                        arch_productivity_mediaplayers()
                case "0":
                        return arch_category()
                case _:
                        print("Invalid choice. Please try again.")
                        time.sleep(2)
                        return arch_productivity()
                
def arch_productivity_officesuites():
        subprocess.run("clear", shell=True)
        print("1. LibreOffice - Office Suite")
        print("2. OnlyOffice - Office Suite")
        print("3. WPS Office - Office Suite")
        print("0. Go Back")

        arch_productivity_officesuites_choice = input("Choose an office suite (1-3): ").strip().lower()

        match arch_productivity_officesuites_choice:
                case "1":
                        subprocess.run("sudo pacman -S libreoffice-fresh", shell=True)
                        return arch_productivity_officesuites()
                case "2":
                        subprocess.run("yay -S onlyoffice-bin", shell=True)
                case "3":
                        print("WPS Office is not available in the official repositories. You're installing it from the AUR, which requires YAY specifically. If you don't have YAY installed, please install it from the Tweaks Category first.")
                        subprocess.run("yay -S wps-office", shell=True)
                case "0":
                        return arch_productivity()
                case _:
                        print("Invalid choice. Please try again.")
                        time.sleep(2)
                        return arch_productivity_officesuites()


def arch_productivity_photoediting():
        subprocess.run("clear", shell=True)
        print("1. GIMP - Photo Editing")
        print("2. Krita - Digital Painting")
        print("3. Digikam - Photo Management")
        print("4. Inkscape - Vector Graphics Editor")
        print("0. Go Back")

        arch_productivity_photoediting_choice = input("Choose a photo editing software (1-4): ").strip().lower()

        match arch_productivity_photoediting_choice:
                case "1":
                        subprocess.run("sudo pacman -S gimp", shell=True)
                        return arch_productivity_photoediting()
                case "2":
                        subprocess.run("sudo pacman -S krita", shell=True)
                        return arch_productivity_photoediting()
                case "3":
                        subprocess.run("sudo pacman -S digikam", shell=True)
                        return arch_productivity_photoediting()
                case "4":
                        subprocess.run("sudo pacman -S inkscape", shell=True)
                        return arch_productivity_photoediting()
                case "0":
                        return arch_productivity()
                case _:
                        print("Invalid choice. Please try again.")
                        time.sleep(2)
                        return arch_productivity_photoediting()
                
def arch_productivity_videoediting():
        subprocess.run("clear", shell=True)
        print("1. Kdenlive - Video Editing by KDE")
        print("2. Shotcut - Simple Video Editor")
        print("3. OpenShot - Video Editing")
        print("4. Flowblade - Fast Python multi-track Video Editor")
        print("0. Go Back")

        arch_productivity_videoediting_choice = input("Choose a video editing software (1-4): ").strip().lower()

        match arch_productivity_videoediting_choice:
                case "1":
                        subprocess.run("sudo pacman -S kdenlive", shell=True)
                        return arch_productivity_videoediting()
                case "2":
                        subprocess.run("sudo pacman -S shotcut", shell=True)
                        return arch_productivity_videoediting()
                case "3":
                        subprocess.run("sudo pacman -S openshot", shell=True)
                        return arch_productivity_videoediting()
                case "4":
                        subprocess.run("sudo pacman -S flowblade", shell=True)
                        return arch_productivity_videoediting()
                case "0":
                        return arch_productivity()
                case _:
                        print("Invalid choice. Please try again.")
                        time.sleep(2)
                        return arch_productivity_videoediting()
                
def arch_productivity_mediaplayers():
        subprocess.run("clear", shell=True)
        print("1. VLC - Media Player")
        print("2. MPV - Media Player")
        print("3. SMPlayer - Media Player")
        print("4. Clementine - Music Player")
        print("5. Gwenview - Image Viewer")
        print("0. Go Back")

        arch_productivity_mediaplayers_choice = input("Choose a media player (1-5): ").strip().lower()

        match arch_productivity_mediaplayers_choice:
                case "1":
                        subprocess.run("sudo pacman -S vlc", shell=True)
                        return arch_productivity_mediaplayers()
                case "2":
                        subprocess.run("sudo pacman -S mpv", shell=True)
                        return arch_productivity_mediaplayers()
                case "3":
                        subprocess.run("sudo pacman -S smplayer", shell=True)
                        return arch_productivity_mediaplayers()
                case "4":
                        subprocess.run("sudo pacman -S clementine", shell=True)
                        return arch_productivity_mediaplayers()
                case "5":
                        subprocess.run("sudo pacman -S gwenview", shell=True)
                        return arch_productivity_mediaplayers()
                case "0":
                        return arch_productivity()
                case _:
                        print("Invalid choice. Please try again.")
                        time.sleep(2)
                        return arch_productivity_mediaplayers()

def arch_tweaks():
        subprocess.run("clear", shell=True)
        print("1. Firewalls")
        print("2. Universal Debloater (Removes Unwanted Services)")
        print("3. Linux Kernel Manager")
        print("4. YAY (Yet Another Yaourt) - AUR Helper (THIS TOOL PROVIDED IS REQUIRED FOR A LOT OF OTHER PACKAGES FOR THIS TOOL, AUR ONLY PACKAGES DONT YET SUPPORT PARU IN MY TOOL, SO PLEASE USE YAY INSTEAD)")
        print("5. PARU - AUR Helper written in Rust")
        print("0. Go Back")

        arch_tweaks_choice = input("Choose a tweak category (1-5): ").strip().lower()
        
        match arch_tweaks_choice:
                case "1":
                        arch_tweaks_firewalls()
                case "2":
                        subprocess.run("sudo systemctl disable cups.service avahi-daemon.service ModemManager.service nfs-server.service smb.service chronyd.service remote-fs.target lvm2-monitor.service accounts-daemon.service upower.service bluetooth.target geoclue.service systemd-binfmt.service systemd-rfkill.service pppd-dns.service speech-dispatcher.service lm-sensors.service apport.service snapd.service", shell=True)
                        print("Unwanted services removal has finished.")
                        time.sleep(2)
                        return arch_tweaks()
                case "3":
                        arch_tweaks_kernelmanager()
                case "4":
                        subprocess.run("sudo pacman -S git base-devel", shell=True)
                        subprocess.run("git clone https://aur.archlinux.org/yay.git", shell=True)
                        subprocess.run("cd yay && makepkg -si", shell=True)
                        print("YAY setup has finished.")
                        time.sleep(2)
                        return arch_tweaks()
                case "5":
                        subprocess.run("sudo pacman -S git base-devel rust", shell=True)
                        subprocess.run("git clone https://aur.archlinux.org/paru.git", shell=True)
                        subprocess.run("cd paru && makepkg -si", shell=True)
                        print("PARU setup has finished.")
                        time.sleep(2)
                        return arch_tweaks()
                case "0":
                        return arch_category()
                case _:
                        print("Invalid choice. Please try again.")
                        time.sleep(2)
                        return arch_tweaks()

def arch_tweaks_firewalls():
        subprocess.run("clear", shell=True)
        print("1. UFW")
        print("2. NFTables")
        print("3. firewalld")
        print("4. REMOVE SUPPORTED FIREWALLS")
        print("Before Installing, you should definitely disable and remove the other firewalls with 4. as multiple firewalls won't work with each other")

        arch_tweaks_fw_choice = input("Choose a firewall to install (1-4): ").strip().lower()

        match arch_tweaks_fw_choice:
                case "1":
                        subprocess.run("sudo pacman -S ufw", shell=True)
                        subprocess.run("sudo systemctl enable --now ufw", shell=True)
                        print("UFW setup has finished.")
                        time.sleep(2)
                        return arch_tweaks_firewalls()
                case "2":
                        subprocess.run("sudo pacman -S nftables", shell=True)
                        subprocess.run("sudo systemctl enable --now nftables", shell=True)
                        print("nftables setup has finished.")
                        time.sleep(2)
                        return arch_tweaks_firewalls()
                case "3":
                        subprocess.run("sudo pacman -S firewalld", shell=True)
                        subprocess.run("sudo systemctl enable --now firewalld", shell=True)
                        print("firewalld setup has finished.")
                        time.sleep(2)
                        return arch_tweaks_firewalls()
                case "4":
                        removefirewalls()
                case _:
                        print("Invalid choice. Please try again.")
                        time.sleep(2)
                        return arch_tweaks_firewalls
                
def removefirewalls():
        subprocess.run("clear", shell=True)
        print("0. Go Back")                                
        removefirewalls_choice = input("Choose a firewall to uninstall(ufw, nftables, firewalld) or exit: ")
        
        match removefirewalls_choice:
                case "ufw":
                        subprocess.run("sudo systemctl disable ufw", shell=True)
                        subprocess.run("sudo pacman -Rns ufw", shell=True)
                        print("UFW Removal Script has completed.")
                        return removefirewalls()
                case "nftables":
                        subprocess.run("sudo systemctl disable nftables", shell=True)
                        subprocess.run("sudo pacman -Rns nftables", shell=True)
                        print("Nftables Removal Script has completed.")
                        return removefirewalls()
                case "firewalld":
                        subprocess.run("sudo systemctl disable firewalld", shell=True)
                        subprocess.run("sudo pacman -Rns firewalld", shell=True)
                        print("FirewallD Removal Script has completed.")
                        return removefirewalls()
                case "0":
                        return arch_tweaks_firewalls()

time.sleep(0.5)

def main():
    subprocess.run("clear", shell=True)
    print(r"""
.____    .__                 __         .__  .__                
|    |   |__| ____   _______/  |______  |  | |  |   ___________ 
|    |   |  |/    \ /  ___/\   __\__  \ |  | |  | _/ __ \_  __ \
|    |___|  |   |  \\___ \  |  |  / __ \|  |_|  |_\  ___/|  | \/
|_______ \__|___|  /____  > |__| (____  /____/____/\___  >__|   
        \/       \/     \/            \/               \/            
""")
    
# guys... its over... I opened vim

    print("It's important to update your system before installing packages.")
    print("What's your desired package manager? (apt, dnf, pacman)")
    print("IMPORTANT: You can use 'apt' for Debian-based Distributions, whereas Ubuntu, it's flavours and other Distributions like Kali, Parrot Security etc. are also based on Debian, 'dnf' for RedHat-based Distributions, whereas Fedora and it's flavours are based on RedHat, and 'pacman' for Arch Linux-based Distributions like CachyOS, EndeavourOS, Artix Linux and others.")
    pkgman = input("Enter your package manager:").strip().lower()

    match pkgman:
        case "apt":
                print("Updating package list...")
                subprocess.run("sudo apt update && sudo apt upgrade -y", shell=True)
                print("Packages Updated!")
                time.sleep(2)
                debian_category()
        case "dnf":
                print("Updating package list...")
                subprocess.run("sudo dnf update && sudo dnf upgrade -y", shell=True)
                print("Packages Updated!")
                time.sleep(2)
                fedora_category()
        case "pacman":
                print("Updating package list...")
                subprocess.run("sudo pacman -Syu", shell=True)
                print("Packages Updated!")
                time.sleep(2)
                arch_category()
        case _:
                print("Unsupported package manager. Try again.")
                time.sleep(2)
                main()

if __name__ == "__main__":
    main()