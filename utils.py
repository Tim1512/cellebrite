import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Mors translator app')
    parser.add_argument("-p", "--port", help="app port")
    args = parser.parse_args()
    return args

def encrypt(message, mors_code_dict: dict):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += mors_code_dict[letter] + ' '
        else:
            cipher += ' '
 
    return cipher
