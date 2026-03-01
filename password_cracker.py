import zipfile

def crack_password():

    # Open and read password file
    f = open("Ashley-Madison.txt", "r", encoding="utf-8", errors="ignore")
    passwords = f.read().splitlines()
    f.close()

    print("Total passwords:", len(passwords))

    # Open zip file
    zf = zipfile.ZipFile("whitehouse_secrets.zip")

    # Try each password
    for i in range(len(passwords)):

        password = passwords[i]

        if i % 10000 == 0:
            print("Trying", i, "->", password)

        try:
            zf.extractall(pwd=password.encode())
            print("PASSWORD FOUND:", password)
            zf.close()
            return password

        except:
            continue

    zf.close()
    print("Password not found.")
    return None


crack_password()