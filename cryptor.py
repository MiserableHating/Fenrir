import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import secrets

decryptkey = secrets.token_hex(15)

def encrypt(key, filename):
    chunksize = 64*1024
    outputFile = "(encrypted)"+filename
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = Random.new().read(16)

    encryptor = AES.new(key, AES.MODE_CBC, IV)

    with open(filename, 'rb') as infile:
        with open(outputFile, 'wb') as outfile:
            outfile.write(filesize.encode('utf-8'))
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - (len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))
                with open('decryptkey', 'w+') as f:
                    f.write(decryptkey)
                    f.close()
        infile.close()
        outfile.close()

    os.remove(filename)


def decrypt(key, filename):
    chunksize = 64*1024
    outputFile = filename[11:]

    with open(filename, 'rb') as infile:
        filesize = int(infile.read(16))
        IV = infile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(outputFile, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(filesize)
            outfile.close()
    infile.close()
    os.remove(filename)

def getKey(password):
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()

def presentation():
    print(" ")
    print(" ")
    print("--------------------------------------------------")
    print("| Encryptor                                      |")
    print("|                                                |")
    print("|             By Alice Hakussura                 |")
    print("|                                                |")
    print("|                                        (c)2018 |")
    print("--------------------------------------------------")
    print("(E) Encrypter, (D) Décrypter, (P) pour avoir la clé, (Q) pour quitter")
    print(" ")
    print(" ")

def Main():
    presentation()
    choice = input("Voulez-vous (E)ncrypter ou (D)crypter ?: ")

    if choice == "E":
        filename = input("Fichier à Encrypter: ")
        password = decryptkey
        encrypt(getKey(password), filename)
        print("Fait.")
        Main()
    elif choice == 'D':
        filename = input("Fichier à Décrypter: ")
        password = input("Clé de décryptage: ")
        decrypt(getKey(password), filename)
        print("Fait.")
        Main()
    elif choice == 'P':
        print(decryptkey)
        Main()
    elif choice == 'Q':
        return
    else:
        print("Aucune option valide séléctionée.")
        Main()

if __name__ == '__main__':
    Main()
