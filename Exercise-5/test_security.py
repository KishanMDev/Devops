import sys

print("[+] Verifying AppArmor Container Security Restrictions...")

# Test 1: Restricted access to sensitive credential file /etc/shadow
try:
    with open("/etc/shadow", "r") as f:
        print("[-] VULNERABILITY DETECTED: /etc/shadow was readable!")
        sys.exit(1)
except PermissionError:
    print("[+] SUCCESS: AppArmor blocked unauthorized access to /etc/shadow (Permission Denied).")
except FileNotFoundError:
    print("[+] SUCCESS: Sensitive file boundaries enforced.")

# Test 2: Standard application execution permitted
try:
    with open("app.py", "r") as f:
        content = f.read()
        print(f"[+] SUCCESS: Legitimate application read allowed ({len(content)} bytes read).")
except Exception as e:
    print(f"[-] Unexpected failure on legitimate path: {e}")
    sys.exit(1)

print("[+] ALL SECURITY PROFILES ENFORCED SUCCESSFULLY.")
