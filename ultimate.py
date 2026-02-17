import os
import time
import json
import urllib.request

# පාටවල් (Colors)
G = "\033[92m" # Green
R = "\033[91m" # Red
C = "\033[96m" # Cyan
Y = "\033[93m" # Yellow
W = "\033[0m"  # White

def update_tool():
    print(f"{Y}[+] Checking for updates...{W}")
    try:
        # මෙතන ඔයාගේ GitHub එකේ 'raw' link එක දාන්න ඕනේ
        # උදා: https://raw.githubusercontent.com/Achiachiofficial/MAFI-VIP-/main/ultimate.py
        url = "https://raw.githubusercontent.com/Achiachiofficial/MAFI-VIP-/main/ultimate.py"
        urllib.request.urlretrieve(url, "ultimate.py")
        print(f"{G}[+] Update Successful! Please restart the tool.{W}")
        time.sleep(2)
        exit()
    except:
        print(f"{R}[!] Update Failed! Check your internet connection.{W}")
        time.sleep(2)

def banner():
    os.system("clear")
    print(f"{C}")
    print(r"""
    ███╗   ███╗ █████╗ ███████╗██╗██╗   ██╗██╗██████╗ 
    ████╗ ████║██╔══██╗██╔════╝██║██║   ██║██║██╔══██╗
    ██╔████╔██║███████║█████╗  ██║██║   ██║██║██████╔╝
    ██║╚██╔╝██║██╔══██║██╔══╝  ██║╚██╗ ██╔╝██║██╔═══╝ 
    ██║ ╚═╝ ██║██║  ██║██║     ██║ ╚████╔╝ ██║██║     
    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═══╝  ╚═╝╚═╝     
    """)
    print(f"{Y}          ⚡ MAFI-VIP ⚡ ULTIMATE TOOLKIT{W}")
    print(f"{G}      ----------------------------------------{W}")

def login():
    banner()
    key = input(f"{C}Enter Login Key: {W}")
    if key == "mafi": # මෙතන ඔයාට ඕන Key එක දෙන්න
        return True
    else:
        print(f"{R}Wrong Key!{W}")
        return False

def main():
    if not login(): return
    while True:
        banner()
        print(f"{G}[01]{W} Nmap         {G}[09]{W} Red Hawk")
        print(f"{G}[02]{W} Metasploit   {G}[10]{W} Slowloris")
        print(f"{G}[03]{W} SQLmap       {G}[11]{W} Admin Finder")
        print(f"{G}[04]{W} Zphisher     {G}[12]{W} Wifite")
        print(f"{G}[05]{W} Sherlock     {G}[13]{W} Hydra")
        print(f"{G}[06]{W} IP Tracer    {G}[14]{W} Crunch")
        print(f"{G}[07]{W} PhoneInfoga  {G}[15]{W} READ MANUALS (A-Z)")
        print(f"{G}[08]{W} SocialFish   {G}[16]{W} Payload Creator")
        print(f"{C}----------------------------------------{W}")
        print(f"{Y}[17] Update Tool {R} [00] Exit{W}")
        
        choice = input(f"\n{Y}MAFI-VIP > {W}")

        if choice == '17': update_tool()
        elif choice == '00': break
        # අනිත් සියලුම elif කොටස් කලින් වගේම මෙතනට දාන්න...

if __name__ == "__main__":
    main()

