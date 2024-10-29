import argparse
from cryptography import Fernet
from config import Config
import subprocess

parser = argparse.ArgumentParser(description='Decryption script')
parser.add_argument('--key', type=str, help='Pass key to unlock')
arg = parser.parse_args()


def decrypt():
    f = Fernet(arg.key)
    with open('encrypted_file.txt', 'rb') as file:
        open_file = file.read()
    decryption = f.decrypt(open_file)
    with open(Config.ENCRYPTED_CREDENTIALS, 'wb') as file:
        file.write(decryption)

def remove():
    subprocess.call(remove)

