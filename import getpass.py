import getpass
import random
import os

def connection():
    for i in range(3):
        user = getpass.getpass("Enter your password: ")
        if user == "securepassword123":
            if i < 2:
                print("Password correct. You may proceed.")
                return True
            else:
                code_pin()
                return True
        print("Incorrect password. Try again.")
            
    print("too many incorrect attempts. Access denied.")
    return False

def code_pin():
    pin = random.randint(1000, 9999)
    print("Un code PIN à 4 chiffres a été créé.")
    bureau = os.path.join(os.path.expanduser("~"), "Desktop")
    chemin = os.path.join(bureau, "code pin")
    os.makedirs(chemin, exist_ok=True)

    with open(os.path.join(chemin, "PIN.txt"), "w") as f:
        f.write(f"PIN : {pin}")

    print("Le PIN a été écrit dans le fichier 'PIN.txt'.")
    print("Vous avez 2 essais pour le saisir.")

    for i in range(2):
        user = input("Entrez le PIN : ")
        if user == str(pin):
            print("PIN correct. Accès final accordé.")
            return True
        else:
            print("PIN incorrect.")
    
    with open(os.path.join(bureau, "bruteforce_detected.txt"), "w") as f:
        f.write("2 échecs de saisie du PIN : brute force détecté.\n")
    print("\nÉchec des 2 essais PIN. Tentative de brute force détectée.")

connection()