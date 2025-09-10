import subprocess
import sys
import time

def arch_category():
        subprocess.run("clear", shell=True)
        
        print(r"""
.____    .__                 __         .__  .__                
|    |   |__| ____   _______/  |______  |  | |  |   ___________ 
|    |   |  |/    \ /  ___/\   __\__  \ |  | |  | _/ __ \_  __ \
|    |___|  |   |  \\___ \  |  |  / __ \|  |_|  |_\  ___/|  | \/
|_______ \__|___|  /____  > |__| (____  /____/____/\___  >__|   
        \/       \/     \/            \/               \/            
""")
        
        print("""
[1] Gaming
[2] Productivity
[3] Tweaks
[4] Tools
[0] Exit
""")
        
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
        
        print(r"""
  ________               .__                
 /  _____/_____    _____ |__| ____    ____  
/   \  ___\__  \  /     \|  |/    \  / ___\ 
\    \_\  \/ __ \|  Y Y  \  |   |  \/ /_/  >
 \______  (____  /__|_|  /__|___|  /\___  / 
        \/     \/      \/        \//_____/  
""")
        
        print("""
[1] Games
[2] Lutris - Managing Game Stores
[3] Steam - Game Marketplace and Launcher
[4] Heroic Games Launcher - Managing Game Stores
[5] WINE - Newest Stable Release
[6] WINE Testing - Experimental Release
[7] WineTricks - Newest Stable Release
[8] Proton-UpQt - Managing Proton, WINE-GE and other compatibility tools
[0] Go Back
""")

        arch_gaming_choice = input("Choose a gaming package (1-8): ").strip().lower()

        match arch_gaming_choice:
                case "1":
                        return arch_gaming_games()
                case "2":
                        subprocess.run("sudo pacman -S lutris", shell=True)
                        return arch_gaming()
                case "3":
                        subprocess.run("sudo pacman -S steam", shell=True)
                        return arch_gaming()
                case "4":
                        subprocess.run("sudo pacman -S heroic-games-launcher", shell=True)
                        return arch_gaming()
                case "5":
                        subprocess.run("sudo pacman -S wine", shell=True)
                        return arch_gaming()
                case "6":
                        subprocess.run("sudo pacman -S wine-staging", shell=True)
                        return arch_gaming()
                case "7":
                        subprocess.run("sudo pacman -S winetricks", shell=True)
                        return arch_gaming()
                case "8":
                        subprocess.run("sudo pacman -S protonup-qt", shell=True)
                        return arch_gaming()
                case "0":
                        return arch_category()
                case _:
                        print("Invalid choice. Please try again.")
                        time.sleep(2)
                        return arch_gaming()
                
def arch_gaming_games():
        subprocess.run("clear", shell=True)
        
        print(r"""
  ________                              
 /  _____/_____    _____   ____   ______
/   \  ___\__  \  /     \_/ __ \ /  ___/
\    \_\  \/ __ \|  Y Y  \  ___/ \___ \ 
 \______  (____  /__|_|  /\___  >____  >
        \/     \/      \/     \/     \/ 
""")
        
        print("""
TIP: Install Flatpak and YAY (Yet Another Yaourt) in this tool first.
[1] Sober - Roblox Launcher by VinegarHQ
[2] Lunar Client - Powerful Minecraft Launcher
[3] Minecraft Launcher - Official Minecraft Launcher by MOJANG
[0] Go Back
""")

        arch_gaming_games_choice = input("Choose a game to install (1-3): ")

        match arch_gaming_games_choice:
                case "1":
                        subprocess.run("flatpak install org.vinegarhq.Sober", shell=True)
                        return arch_gaming_games()
                case "2":
                        subprocess.run("yay -S lunar-client", shell=True)
                        return arch_gaming_games()
                case "3":
                        subprocess.run("yay -S minecraft-launcher", shell=True)
                        return arch_gaming_games()
                case "0":
                        return arch_gaming()
                case _:
                        print("Invalid choice. Please try again.")
                        time.sleep(2)
                        return arch_gaming_games()

def arch_productivity():
        subprocess.run("clear", shell=True)
        
        print(r"""
__________                   .___             __  .__      .__  __          
\______   \_______  ____   __| _/_ __   _____/  |_|__|__  _|__|/  |_ ___.__.
 |     ___/\_  __ \/  _ \ / __ |  |  \_/ ___\   __\  \  \/ /  \   __<   |  |
 |    |     |  | \(  <_> ) /_/ |  |  /\  \___|  | |  |\   /|  ||  |  \___  |
 |____|     |__|   \____/\____ |____/  \___  >__| |__| \_/ |__||__|  / ____|
                              \/           \/                        \/     
""")
        
        print("""
[1] Office Suites
[2] Photo Editing
[3] Video Editing
[4] 3D Modeling
[0] Go Back
""")

        arch_productivity_choice = input("Choose productivity group (1-4): ").strip().lower()

        match arch_productivity_choice:
                case "1":
                        arch_productivity_officesuites()
                case "2":
                        arch_productivity_photoediting()
                case "3":
                        arch_productivity_videoediting()
                case "4":
                        arch_productivity_3dmodeling()
                case "0":
                        return arch_category()
                case _:
                        print("Invalid choice. Please try again.")
                        time.sleep(2)
                        return arch_productivity()
                
def arch_productivity_officesuites():
        subprocess.run("clear", shell=True)
        
        print(r"""
________   _____  _____.__                 _________     .__  __                 
\_____  \_/ ____\/ ____\__| ____  ____    /   _____/__ __|__|/  |_  ____   ______
 /   |   \   __\\   __\|  |/ ___\/ __ \   \_____  \|  |  \  \   __\/ __ \ /  ___/
/    |    \  |   |  |  |  \  \__\  ___/   /        \  |  /  ||  | \  ___/ \___ \ 
\_______  /__|   |__|  |__|\___  >___  > /_______  /____/|__||__|  \___  >____  >
        \/                     \/    \/          \/                    \/     \/ 
""")
        
        print("""
[1] LibreOffice - Office Suite
[2] OnlyOffice - Office Suite
[3] WPS Office - Office Suite
[0] Go Back
""")

        arch_productivity_officesuites_choice = input("Choose an office suite (1-3): ").strip().lower()

        match arch_productivity_officesuites_choice:
                case "1":
                        subprocess.run("sudo pacman -S libreoffice-fresh", shell=True)
                        return arch_productivity_officesuites()
                case "2":
                        print("OnlyOffice is not available in the official repositories. You're installing it from the AUR, which requires YAY specifically. If you don't have YAY installed, please install it from the Tools Category first.")
                        time.sleep(8)
                        subprocess.run("yay -S onlyoffice-bin", shell=True)
                        return arch_productivity_officesuites()
                case "3":
                        print("WPS Office is not available in the official repositories. You're installing it from the AUR, which requires YAY specifically. If you don't have YAY installed, please install it from the Tools Category first.")
                        time.sleep(8)
                        subprocess.run("yay -S wps-office", shell=True)
                        return arch_productivity_officesuites()
                case "0":
                        return arch_productivity()
                case _:
                        print("Invalid choice. Please try again.")
                        time.sleep(2)
                        return arch_productivity_officesuites()


def arch_productivity_photoediting():
        subprocess.run("clear", shell=True)
        
        print(r"""
__________.__            __           ___________    .___.__  __                       
\______   \  |__   _____/  |_  ____   \_   _____/  __| _/|__|/  |_  ___________  ______
 |     ___/  |  \ /  _ \   __\/  _ \   |    __)_  / __ | |  \   __\/  _ \_  __ \/  ___/
 |    |   |   Y  (  <_> )  | (  <_> )  |        \/ /_/ | |  ||  | (  <_> )  | \/\___ \ 
 |____|   |___|  /\____/|__|  \____/  /_______  /\____ | |__||__|  \____/|__|  /____  >
               \/                             \/      \/                            \/ 
""")
        
        print("""
[1] GIMP - Photo Editing
[2] Krita - Digital Painting
[3] Digikam - Photo Management
[4] Inkscape - Vector Graphics Editor
[0] Go Back
""")

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

        print(r"""
____   ____.__    .___             ___________    .___.__  __                       
\   \ /   /|__| __| _/____  ____   \_   _____/  __| _/|__|/  |_  ___________  ______
 \   Y   / |  |/ __ |/ __ \/  _ \   |    __)_  / __ | |  \   __\/  _ \_  __ \/  ___/
  \     /  |  / /_/ \  ___(  <_> )  |        \/ /_/ | |  ||  | (  <_> )  | \/\___ \ 
   \___/   |__\____ |\___  >____/  /_______  /\____ | |__||__|  \____/|__|  /____  >
                   \/    \/                \/      \/                            \/ 
""")

        print("""
[1] Kdenlive - Video Editing by KDE
[2] Shotcut - Simple Video Editor
[3] OpenShot - Video Editing
[4] Flowblade - Fast Python multi-track Video Editor
[0] Go Back
""")

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

def arch_productivity_3dmodeling():
        subprocess.run("clear", shell=True)

        print(r"""
________ ________         _____             .___     .__  .__                
\_____  \\______ \       /     \   ____   __| _/____ |  | |__| ____    ____  
  _(__  < |    |  \     /  \ /  \ /  _ \ / __ |/ __ \|  | |  |/    \  / ___\ 
 /       \|    `   \   /    Y    (  <_> ) /_/ \  ___/|  |_|  |   |  \/ /_/  >
/______  /_______  /   \____|__  /\____/\____ |\___  >____/__|___|  /\___  / 
       \/        \/            \/            \/    \/             \//_____/
""")
        
        print("""
[1] Blender - 3D Creation Suite
[2] Vinegar - Roblox Studio Launcher via WINE
[0] Go Back
""")
              
        arch_productivity_3dmodeling_choice = input("Choose a 3D modeling software (1-2): ").strip().lower()

        match arch_productivity_3dmodeling_choice:
                case "1":
                        subprocess.run("sudo pacman -S blender", shell=True)
                        return arch_productivity_3dmodeling()
                case "2":
                        print("Roblox Studio is not available in the official repositories. Install flatpak from the Tools Category first. Also install WINE as it's required for Vinegar to function properly.")
                        time.sleep(8)
                        subprocess.run("flatpak install org.vinegarhq.Vinegar", shell=True)
                        return arch_productivity_3dmodeling()       
                case "0":
                        return arch_productivity()
                case _:
                        print("Invalid choice. Please try again.")
                        time.sleep(2)
                        return arch_productivity_3dmodeling()                               
                
def arch_tools():
        subprocess.run("clear", shell=True)
        
        print(r"""
___________           .__          
\__    ___/___   ____ |  |   ______
  |    | /  _ \ /  _ \|  |  /  ___/
  |    |(  <_> |  <_> )  |__\___ \ 
  |____| \____/ \____/|____/____  >
                                \/ 
""")

        print("""
[1] Media Players
[2] Browsers
[3] System Monitor
[4] Pen Testing
[5] Programming Language
[6] YAY - Yet Another Yaourt AUR Helper
[7] PARU - The AUR Helper Written in RUST
[8] Flatpak - Software Made Easy
[0] Go Back
""")

        arch_tools_choice = input("Choose your tools (1-8): ").strip().lower()

        match arch_tools_choice:
                case "1":
                        return arch_tools_mediaplayers()
                case "2":
                        return arch_tools_browsers()
                case "3":
                        return arch_tools_sysmoni()
                case "4":
                        return arch_tools_pentesting()
                case "5":
                        return arch_tools_languages()
                case "6":
                        subprocess.run("sudo pacman -S git base-devel", shell=True)
                        subprocess.run("git clone https://aur.archlinux.org/yay.git", shell=True)
                        subprocess.run("cd yay && makepkg -si", shell=True)
                        print("YAY setup has finished.")
                        time.sleep(2)
                        return arch_tools()
                case "7":
                        subprocess.run("sudo pacman -S git base-devel rust", shell=True)
                        subprocess.run("git clone https://aur.archlinux.org/paru.git", shell=True)
                        subprocess.run("cd paru && makepkg -si", shell=True)
                        print("PARU setup has finished.")
                        time.sleep(2)
                        return arch_tools()
                case "8":
                        subprocess.run("sudo pacman -S flatpak", shell=True)
                        subprocess.run("flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo", shell=True)
                        print("Flatpak setup has Finished!")
                        time.sleep(2)
                        return arch_tools()
                case "0":
                        return arch_category()
                case _:
                        print("Invalid Choice. Please try again.")
                        time.sleep(2)
                        return arch_tools()

                
def arch_tools_mediaplayers():
        subprocess.run("clear", shell=True)

        print(r"""
   _____             .___.__         __________.__                                    
  /     \   ____   __| _/|__|____    \______   \  | _____  ___.__. ___________  ______
 /  \ /  \_/ __ \ / __ | |  \__  \    |     ___/  | \__  \<   |  |/ __ \_  __ \/  ___/
/    Y    \  ___// /_/ | |  |/ __ \_  |    |   |  |__/ __ \\___  \  ___/|  | \/\___ \ 
\____|__  /\___  >____ | |__(____  /  |____|   |____(____  / ____|\___  >__|  /____  >
        \/     \/     \/         \/                      \/\/         \/           \/ 
""")
        
        print("""
[1] VLC - Media Player
[2] MPV - Media Player
[3] SMPlayer - Media Player
[4] Clementine - Music Player
[5] Gwenview - Image Viewer
[0] Go Back
""")

        arch_tools_mediaplayers_choice = input("Choose a media player (1-5): ").strip().lower()

        match arch_tools_mediaplayers_choice:
                case "1":
                        subprocess.run("sudo pacman -S vlc", shell=True)
                        return arch_tools_mediaplayers()
                case "2":
                        subprocess.run("sudo pacman -S mpv", shell=True)
                        return arch_tools_mediaplayers()
                case "3":
                        subprocess.run("sudo pacman -S smplayer", shell=True)
                        return arch_tools_mediaplayers()
                case "4":
                        subprocess.run("sudo pacman -S clementine", shell=True)
                        return arch_tools_mediaplayers()
                case "5":
                        subprocess.run("sudo pacman -S gwenview", shell=True)
                        return arch_tools_mediaplayers()
                case "0":
                        return arch_tools()
                case _:
                        print("Invalid choice. Please try again.")
                        time.sleep(2)
                        return arch_tools_mediaplayers()
                
def arch_tools_browsers():
        subprocess.run("clear", shell=True)

        print(r"""
__________                                                 
\______   \_______  ______  _  ________ ___________  ______
 |    |  _/\_  __ \/  _ \ \/ \/ /  ___// __ \_  __ \/  ___/
 |    |   \ |  | \(  <_> )     /\___ \\  ___/|  | \/\___ \ 
 |______  / |__|   \____/ \/\_//____  >\___  >__|  /____  >
        \/                          \/     \/           \/ 
""")

        print("""
TIP: INSTALL YAY FIRST!

[1] Firefox - THE Privacy Focused Browser
[2] LibreWolf - A Fork of Firefox focused on enhancing privacy even further than Firefox
[3] Chromium - Open Source Browser made by Google
[4] Mullvad Browser - A Privacy-Focused Browser built on Firefox
[5] Opera - Browser built by Opera Software
[6] Zen Browser - The Browser focused on Privacy and Usability
[7] Chrome - The Most Popular Browser made by Google
[8] Thorium - The Fastest Browser built on Chromium
[9] Brave - A Chromium-built Privacy-Respecting Browser
[10] Microsoft Edge - The New Chromium-based Browser by Microsoft
[11] Vivaldi - A Highly Customizable Chromium-based Browser``````````````````````
[12] Tor Browser - The Privacy-Focused Browser that uses the Tor Network
[0] Go Back
""")

        arch_tools_browsers_choice = input("Choose a Browser (1-8): ").strip().lower()

        match arch_tools_browsers_choice:
                case "1":
                        subprocess.run("sudo pacman -S firefox", shell=True)
                        return arch_tools_browsers()
                case "2":
                        print("LibreWolf is not available in the official repositories. If you don't have YAY installed, please install it from the Tools Category first.")
                        time.sleep(8)
                        subprocess.run("yay -S librewolf-bin", shell=True)
                        return arch_tools_browsers()
                case "3":
                        subprocess.run("sudo pacman -S chromium", shell=True)
                        return arch_tools_browsers()
                case "4":
                        print("Mullvad Browser is not available in the official repositories. If you don't have YAY installed, please install it from the Tools Category first.")
                        time.sleep(8)
                        subprocess.run("yay -S mullvad-browser-bin", shell=True)
                        return arch_tools_browsers()
                case "5":
                        print("Opera is not available in the official repositories. if you don't have YAY installed, please install it from the Tools Category first.")
                        time.sleep(8)
                        subprocess.run("yay -S opera", shell=True)
                        return arch_tools_browsers()
                case "6":
                        print("Zen Browser is not available in the official repositories. if you don't have YAY installed, please install it from the Tools Category first.")
                        subprocess.run("yay -S zen-browser-bin", shell=True)
                        return arch_tools_browsers()
                case "7":
                        print("Chrome is not available in the official repositories. if you don't have YAY installed, please install it from the Tools Category first.")
                        time.sleep(8)
                        subprocess.run("yay -S google-chrome", shell=True)
                        return arch_tools_browsers()
                case "8":
                        print("Thorium is not available in the official repositories. if you don't have YAY installed, please install it from the Tools Category first.")
                        time.sleep(8)
                        subprocess.run("yay -S thorium-browser-bin", shell=True)
                        return arch_tools_browsers()
                case "9":
                        print("Brave is not available in the official repositories. if you don't have YAY installed, please install it from the Tools Category first.")
                        time.sleep(8)
                        subprocess.run("yay -S brave-bin")
                        return arch_tools_browsers()
                case "10":
                        print("Microsoft Edge is not available in the official repositories. if you don't have YAY installed, please install it from the Tools Category first.")
                        time.sleep(8)
                        subprocess.run("yay -S microsoft-edge-stable-bin", shell=True)
                        return arch_tools_browsers()
                case "11":
                        subprocess.run("sudo pacman -S vivaldi", shell=True)
                        return arch_tools_browsers()
                case "12":
                        subprocess.run("sudo pacman -S torbrowser-launcher", shell=True)
                        return arch_tools_browsers()
                case "0":
                        return arch_tools()
                case _:
                        print("Invalid choice. Please try again")
                        time.sleep(2)
                        return arch_tools_browsers()
                
def arch_tools_sysmoni():
        subprocess.run("clear", shell=True)

        print(r"""
  _________               __                      _____                .__  __                
 /   _____/__.__. _______/  |_  ____   _____     /     \   ____   ____ |__|/  |_  ___________ 
 \_____  <   |  |/  ___/\   __\/ __ \ /     \   /  \ /  \ /  _ \ /    \|  \   __\/  _ \_  __ \
 /        \___  |\___ \  |  | \  ___/|  Y Y  \ /    Y    (  <_> )   |  \  ||  | (  <_> )  | \/
/_______  / ____/____  > |__|  \___  >__|_|  / \____|__  /\____/|___|  /__||__|  \____/|__|   
        \/\/         \/            \/      \/          \/            \/                       
""")

        print("""
[1] Htop
[2] Btop
[3] Bpytop
[4] bashtop
[5] glances
[6] conky
[7] neofetch - Fetch system information in an eye candy way
[8] fastfetch - A modern alternative to neofetch
[9] GNOME System Monitor
[0] Go Back
""")

        arch_tools_sysmoni_choice = input("Choose your System Monitoring Tool (1-9): ")

        match arch_tools_sysmoni_choice:
                case "1":
                        subprocess.run("sudo pacman -S htop", shell=True)
                        return arch_tools_sysmoni()
                case "2":
                        subprocess.run("sudo pacman -S btop", shell=True)
                        return arch_tools_sysmoni()
                case "3":
                        subprocess.run("sudo pacman -S bpytop", shell=True)
                        return arch_tools_sysmoni()
                case "4":
                        subprocess.run("sudo pacman -S bashtop", shell=True)
                        return arch_tools_sysmoni()
                case "5":
                        subprocess.run("sudo pacman -S glances", shell=True)
                        return arch_tools_sysmoni()
                case "6":
                        subprocess.run("sudo pacman -S conky", shell=True)
                        return arch_tools_sysmoni()
                case "7":
                        print("Neofetch is not available in the official repositories. You're installing it from the AUR, which requires YAY specifically. If you don't have YAY installed, please install it from the Tools Category first.")
                        time.sleep(8)
                        subprocess.run("yay -S neofetch", shell=True)
                        return arch_tools_sysmoni()
                case "8":
                        subprocess.run("sudo pacman -S fastfetch", shell=True)
                        return arch_tools_sysmoni()
                case "9":
                        subprocess.run("sudo pacman -S gnome-system-monitor", shell=True)
                        return arch_tools_sysmoni()
                case "0":
                        return arch_tools()
                case _:
                        print("Invalid choice. Please try again")
                        time.sleep(2)
                        return arch_tools_sysmoni()

def arch_tools_pentesting():
        subprocess.run("clear", shell=True)

        print(r"""
__________                ___________              __  .__                
\______   \ ____   ____   \__    ___/___   _______/  |_|__| ____    ____  
 |     ___// __ \ /    \    |    |_/ __ \ /  ___/\   __\  |/    \  / ___\ 
 |    |   \  ___/|   |  \   |    |\  ___/ \___ \  |  | |  |   |  \/ /_/  >
 |____|    \___  >___|  /   |____| \___  >____  > |__| |__|___|  /\___  / 
               \/     \/               \/     \/               \//_____/  
""")

        print("""
[1] Nmap
[2] Metasploit
[3] Wireshark-CLI (Command-Line-Interface)
[4] Aircrack-ng
[5] John the Ripper
[6] netcat
[7] Hashcat
[8] Add BlackArch repository (Not Recommended!)
0] Go Back
""")

        arch_tools_pentesting_choice = input("Choose a pentesting tool (1-8): ").strip().lower()

        match arch_tools_pentesting_choice:
                case "1":
                        subprocess.run("sudo pacman -S nmap", shell=True)
                        return arch_tools_pentesting()
                case "2":
                        print("Metasploit is not available in the official repositories. You're installing it from the AUR, which requires YAY specifically. If you don't have YAY installed, please install it from the Tools Category first.")
                        time.sleep(8)
                        subprocess.run("yay -S metasploit", shell=True)
                        return arch_tools_pentesting()
                case "3":
                        subprocess.run("sudo pacman -S wireshark-cli", shell=True)
                        return arch_tools_pentesting()
                case "4":
                        subprocess.run("sudo pacman -S aircrack-ng", shell=True)
                        return arch_tools_pentesting()
                case "5":
                        subprocess.run("sudo pacman -S john", shell=True)
                        return arch_tools_pentesting()
                case "6":
                        subprocess.run("sudo pacman -S gnu-netcat", shell=True)
                        return arch_tools_pentesting()
                case "7":
                        subprocess.run("sudo pacman -S hashcat", shell=True)
                        return arch_tools_pentesting()
                case "8":
                        subprocess.run("curl -sSfL https://blackarch.org/strap.sh | sudo bash", shell=True)
                        subprocess.run("sudo pacman -Syyu")
                        return arch_tools_pentesting()
                case "0":
                        return arch_tools()
                case _:
                        print("Invalid choice. Please try Again")
                        time.sleep(2)
                        return arch_tools_pentesting()

def arch_tools_languages():
        subprocess.run("clear", shell=True)

        print(r"""
__________                                                   .__                 .____                                                              
\______   \_______  ____   ________________    _____   _____ |__| ____    ____   |    |   _____    ____    ____  __ _______     ____   ____   ______
 |     ___/\_  __ \/  _ \ / ___\_  __ \__  \  /     \ /     \|  |/    \  / ___\  |    |   \__  \  /    \  / ___\|  |  \__  \   / ___\_/ __ \ /  ___/
 |    |     |  | \(  <_> ) /_/  >  | \// __ \|  Y Y  \  Y Y  \  |   |  \/ /_/  > |    |___ / __ \|   |  \/ /_/  >  |  // __ \_/ /_/  >  ___/ \___ \ 
 |____|     |__|   \____/\___  /|__|  (____  /__|_|  /__|_|  /__|___|  /\___  /  |_______ (____  /___|  /\___  /|____/(____  /\___  / \___  >____  >
                        /_____/            \/      \/      \/        \//_____/           \/    \/     \//_____/            \//_____/      \/     \/ 
""")

        print("""
[1] Z Shell - Modern and Powerful Shell
[2] PowerShell - Modern Shell by Microsoft
[3] Fish Shell - Fast, Customizable Shell
[4] python-pip - Python Package Manager
[5] Java (OpenJDK) - Programming Language by ORACLE
[6] GO - Popular Dev Programming Language
[7] RUST - Modern, Memory-Safe Programming Language
[8] Node.js
[0] Go Back
""")

        arch_tools_languages_choices = input("Choose a Language to install (1-8): ")

        match arch_tools_languages_choices:
                case "1":
                        subprocess.run("sudo pacman -S zsh", shell=True)
                        return arch_tools_languages()
                case "2":
                        print("Powershell is not available in the official repositories. You're installing it from the AUR, which requires YAY specifically. If you don't have YAY installed, please install it from the Tools Category first.")
                        time.sleep(8)
                        subprocess.run("yay -S powershell-bin", shell=True)
                        return arch_tools_languages()
                case "3":
                        subprocess.run("sudo pacman -S fish", shell=True)
                        return arch_tools_languages()
                case "4":
                        subprocess.run("sudo pacman -S python-pip", shell=True)
                        return arch_tools_languages()
                case "5":
                        subprocess.run("sudo pacman -S jdk-openjdk", shell=True)
                        return arch_tools_languages()
                case "6":
                        subprocess.run("sudo pacman -S go", shell=True)
                        return arch_tools_languages()
                case "7":
                        subprocess.run("sudo pacman -S rust", shell=True)
                        return arch_tools_languages()
                case "8":
                        subprocess.run("sudo pacman -S nodejs npm", shell=True)
                        return arch_tools_languages()
                case "0":
                        return arch_tools()
                case _:
                        print("Invalid choice. Please try Again")
                        time.sleep(2)
                        return arch_tools_languages()

def arch_tweaks():
        subprocess.run("clear", shell=True)

        print(r"""
___________                      __            
\__    ___/_  _  __ ____ _____  |  | __  ______
  |    |  \ \/ \/ // __ \\__  \ |  |/ / /  ___/
  |    |   \     /\  ___/ / __ \|    <  \___ \ 
  |____|    \/\_/  \___  >____  /__|_ \/____  >
                       \/     \/     \/     \/ 
""")

        print("""
[1] Firewalls
[2] Drivers
[3] Universal Debloater (Removes Unwanted Services)
[4] Linux Kernel Manager
[0] Go Back
""")

        arch_tweaks_choice = input("Choose a tweak category (1-4): ").strip().lower()
        
        match arch_tweaks_choice:
                case "1":
                        arch_tweaks_firewalls()
                case "2":
                        arch_tweaks_drivers()
                case "3":
                        subprocess.run("sudo systemctl disable cups.service avahi-daemon.service ModemManager.service nfs-server.service smb.service chronyd.service remote-fs.target lvm2-monitor.service accounts-daemon.service upower.service bluetooth.target geoclue.service systemd-binfmt.service systemd-rfkill.service pppd-dns.service speech-dispatcher.service lm-sensors.service apport.service snapd.service", shell=True)
                        print("Unwanted services removal has finished.")
                        time.sleep(2)
                        return arch_tweaks()
                case "4":
                        arch_tweaks_kernelmanager()
                case "0":
                        return arch_category()
                case _:
                        print("Invalid choice. Please try again.")
                        time.sleep(2)
                        return arch_tweaks()

def arch_tweaks_firewalls():
        subprocess.run("clear", shell=True)

        print(r"""
___________.__                              .__  .__          
\_   _____/|__|______   ______  _  _______  |  | |  |   ______
 |    __)  |  \_  __ \_/ __ \ \/ \/ /\__  \ |  | |  |  /  ___/
 |     \   |  ||  | \/\  ___/\     /  / __ \|  |_|  |__\___ \ 
 \___  /   |__||__|    \___  >\/\_/  (____  /____/____/____  >
     \/                    \/             \/               \/ 
""")

        print("""
[1] UFW
[2] NFTables
[3] firewalld
[4] REMOVE SUPPORTED FIREWALLS
[0] Go Back

WARNING! Before Installing, you should definitely disable and remove the other firewalls with 4. as multiple firewalls won't work with each other
""")

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
                        return arch_removefirewalls()
                case "0":
                        return arch_tweaks()
                case _:
                        print("Invalid choice. Please try again.")
                        time.sleep(2)
                        return arch_tweaks_firewalls()
                
def arch_removefirewalls():
        subprocess.run("clear", shell=True)

        print(r"""
___________.__                              .__  .__          
\_   _____/|__|______   ______  _  _______  |  | |  |   ______
 |    __)  |  \_  __ \_/ __ \ \/ \/ /\__  \ |  | |  |  /  ___/
 |     \   |  ||  | \/\  ___/\     /  / __ \|  |_|  |__\___ \ 
 \___  /   |__||__|    \___  >\/\_/  (____  /____/____/____  >
     \/                    \/             \/               \/ 
""")

        print("[0] Go Back")                                
        removefirewalls_choice = input("Choose a firewall to uninstall (ufw, nftables, firewalld): ")
        
        match removefirewalls_choice:
                case "ufw":
                        subprocess.run("sudo systemctl disable ufw", shell=True)
                        subprocess.run("sudo pacman -Rns ufw", shell=True)
                        return arch_removefirewalls()
                case "nftables":
                        subprocess.run("sudo systemctl disable nftables", shell=True)
                        subprocess.run("sudo pacman -Rns nftables", shell=True)
                        return arch_removefirewalls()
                case "firewalld":
                        subprocess.run("sudo systemctl disable firewalld", shell=True)
                        subprocess.run("sudo pacman -Rns firewalld", shell=True)
                        return arch_removefirewalls()
                case "0":
                        return arch_tweaks_firewalls()
                case _:
                        print("Invalid choice. Please try again.")
                        time.sleep(2)
                        return arch_removefirewalls()
                
def arch_tweaks_drivers():
        subprocess.run("clear", shell=True)

        print(r"""
________        .__                           
\______ \_______|__|__  __ ___________  ______
 |    |  \_  __ \  \  \/ // __ \_  __ \/  ___/
 |    `   \  | \/  |\   /\  ___/|  | \/\___ \ 
/_______  /__|  |__| \_/  \___  >__|  /____  >
        \/                    \/           \/ 
""")

        print("""
WARNING! MAKE SURE THE DRIVER SUITS YOUR HARDWARE CONFIGURATION(GPU) AND KERNEL VERSION! YOU ALSO NEED TO REBUILD INITRAMFS AFTER SWITCHING DRIVER VERSIONS OR REMOVING DRIVERS! IF YOU'RE UNSURE ABOUT WHAT TO INSTALL, PLEASE RESEARCH IT FIRST!

[1] Rebuild Initramfs - REQUIRED AFTER SWITCHING DRIVER VERSIONS!!
[2] Delete (NVIDIA) Drivers
[3] Install CUDA
[4] Install OpenCL (NVIDIA)

-- NVIDIA PROPRIETARY DRIVERS FOR PASCAL AND OLDER --

[5] nvidia - linux kernel
[6] nvidia-lts - linux-lts kernel
[7] nvidia-dkms - for the gaming focused linux-zen kernel or the secure linux-hardened kernel

-- NVIDIA OPEN KERNEL MODULE DRIVERS FOR TURING AND NEWER GPUS --

[8] nvidia-open - linux kernel
[9] nvidia-open-lts - linux-lts kernel
[10] nvidia-open-dkms - for the gaming focused linux-zen kernel or the secure linux-hardened kernel
[0] Go Back
""")

        arch_tweaks_driver_choice = input("Choose an option (1-10): ")

        match arch_tweaks_driver_choice:
                
                case "1":
                        subprocess.run("sudo mkinitcpio -P", shell=True)
                        return arch_tweaks_drivers()
                case "2":
                        return arch_removedrivers()
                case "3":
                        subprocess.run("sudo pacman -S cuda nvidia-utils nvidia-settings", shell=True)
                        return arch_tweaks_drivers()
                case "4":
                        subprocess.run("sudo pacman -S opencl-nvidia opencl-headers", shell=True)
                        return arch_tweaks_drivers()
                case "5":
                        subprocess.run("sudo pacman -S nvidia", shell=True)
                        print("nvidia setup has finished. Please make sure the driver matches your hardware configuration and kernel version. You Should Also Rebuild the initramfs!")
                        time.sleep(10)
                        return arch_tweaks_drivers()
                case "6":
                        subprocess.run("sudo pacman -S nvidia-lts", shell=True)
                        print("nvidia-lts setup has finished. Please make sure the driver matches your hardware configuration and kernel version. You Should Also Rebuild the initramfs!")
                        time.sleep(10)
                        return arch_tweaks_drivers()
                case "7":
                        subprocess.run("sudo pacman -S nvidia-dkms", shell=True)
                        print("nvidia-dkms setup has finished. Please make sure the driver matches your hardware configuration and kernel version. You Should Also Rebuild the initramfs!")
                        time.sleep(10)
                        return arch_tweaks_drivers()
                case "8":
                        subprocess.run("sudo pacman -S nvidia-open", shell=True)
                        print("nvidia-open setup has finished. Please make sure the driver matches your hardware configuration and kernel version. You Should Also Rebuild the initramfs!")
                        time.sleep(10)
                        return arch_tweaks_drivers()
                case "9":
                        subprocess.run("sudo pacman -S nvidia-open-lts", shell=True)
                        print("nvidia-open-lts setup has finished. Please make sure the driver matches your hardware configuration and kernel version. You Should Also Rebuild the initramfs!")
                        time.sleep(10)
                        return arch_tweaks_drivers()
                case "10":
                        subprocess.run("sudo pacman -S nvidia-open-dkms", shell=True)
                        print("nvidia-open-dkms setup has finished. Please make sure the driver matches your hardware configuration and kernel version. You Should Also Rebuild the initramfs!")
                        time.sleep(10)
                        return arch_tweaks_drivers()
                case "0":
                        return arch_tweaks()
                case "67":
                        print("six... seven! 67 boi ts is so tuff! everyone coem back we are having a retrial!! objection!!! boii this is how we defending schlep in court. but seriously, you can't choose 67, it's not a valid option, noob")
                        time.sleep(6)
                        return arch_tweaks_drivers()
                case _:
                        print("Invalid choice. Please try again")
                        time.sleep(2)
                        return arch_tweaks_drivers()

def arch_removedrivers():
        subprocess.run("clear", shell=True)

        print(r"""
________        .__                           
\______ \_______|__|__  __ ___________  ______
 |    |  \_  __ \  \  \/ // __ \_  __ \/  ___/
 |    `   \  | \/  |\   /\  ___/|  | \/\___ \ 
/_______  /__|  |__| \_/  \___  >__|  /____  >
        \/                    \/           \/ 
""")

        print("""
WARNING: If you're planning to run the system without gpu drivers, make sure to rebuld initramfs after deleting the gpu driver. Also rebuild initramfs after you install a different driver.
-- NVIDIA PROPRIETARY DRIVERS FOR PASCAL AND OLDER --
        
[1] nvidia - standard driver
[2] nvidia-lts - longterm support
[3] nvidia-dkms - driver for the gaming focused linux-zen kernel or the secure linux-hardened kernel

-- NVIDIA OPEN KERNEL MODULE DRIVERS FOR TURING AND NEWER GPUS --

[4] nvidia-open - standard driver
[5] nvidia-open-lts - longterm support
[6] nvidia-open-dkms - driver for the gaming focused linux-zen kernel or the secure linux-hardened kernel
[0] Go Back
""")

        arch_remdrivers_choice = input("Please choose which driver to delete (1-6): ")

        match arch_remdrivers_choice:
                case "0":
                        return arch_tweaks_drivers()
                case "1":
                        subprocess.run("sudo pacman -Rns nvidia", shell=True)
                        return arch_removedrivers()
                case "2":
                        subprocess.run("sudo pacman -Rns nvidia-lts", shell=True)
                        return arch_removedrivers()
                case "3":
                        subprocess.run("sudo pacman -Rns nvidia-dkms", shell=True)
                        return arch_removedrivers()
                case "4":
                        subprocess.run("sudo pacman -Rns nvidia-open", shell=True)
                        return arch_removedrivers()
                case "5":
                        subprocess.run("sudo pacman -Rns nvidia-open-lts", shell=True)
                        return arch_removedrivers()
                case "6":
                        subprocess.run("sudo pacman -Rns nvidia-open-dkms", shell=True)
                        return arch_removedrivers()
                case "0":
                        return arch_tweaks_drivers()
                case _:
                        print("Invalid choice. Please try again.")
                        time.sleep(2)
                        return arch_removedrivers()

def arch_tweaks_kernelmanager():
        subprocess.run("clear", shell=True)

        print(r"""
 ____  __.                         .__          
|    |/ _|___________  ____   ____ |  |   ______
|      <_/ __ \_  __ \/    \_/ __ \|  |  /  ___/
|    |  \  ___/|  | \/   |  \  ___/|  |__\___ \ 
|____|__ \___  >__|  |___|  /\___  >____/____  >
        \/   \/           \/     \/          \/ 
""")

        print("""
[1] linux
[2] linux-lts
[3] linux-zen
[4] linux-hardened
[0] Go Back
""")

        arch_tweaks_km_choice = input("Choose a kernel to install (1-4): ")

        match arch_tweaks_km_choice:
                case "1":
                        subprocess.run("sudo pacman -S linux linux-headers", shell=True)
                        print("Later you will also require to go into Tweaks -> Drivers and Install Drivers compatible with the Kernel and GPU")
                        time.sleep(5)
                        return arch_tweaks_kernelmanager()
                case "2":
                        subprocess.run("sudo pacman -S linux-lts linux-lts-headers", shell=True)
                        print("Later you will also require to go into Tweaks -> Drivers and Install Drivers compatible with the Kernel and GPU")
                        time.sleep(5)
                        return arch_tweaks_kernelmanager()                        
                case "3":
                        subprocess.run("sudo pacman -S linux-zen linux-zen-headers", shell=True)
                        print("Later you will also require to go into Tweaks -> Drivers and Install Drivers compatible with the Kernel and GPU")
                        time.sleep(5)
                        return arch_tweaks_kernelmanager()
                case "4":
                        subprocess.run("sudo pacman -S linux-hardened linux-hardened-headers", shell=True)
                        print("Later you will also require to go into Tweaks -> Drivers and Install Drivers compatible with the Kernel and GPU")
                        time.sleep(5)
                        return arch_tweaks_kernelmanager()
                case "0":
                        return arch_tweaks()
                case _:
                        print("Invalid Option. Try Again")
                        time.sleep(2)
                        return arch_tweaks_kernelmanager()

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

    print("""
It's important to update your system before installing packages.
What's your Distro Based on?
IMPORTANT: Check GitHub Documentation for Which Distributions are supported!
""")
    
    pkgman = input("Enter your distribution:").strip().lower()

    match pkgman:
        case "arch":
                print("Updating package list...")
                subprocess.run("sudo pacman -Syu", shell=True)
                print("Packages Updated!")
                time.sleep(2)
                arch_category()
        case _:
                print("Unsupported package manager. Try again.")
                time.sleep(2)
                main()

main()
