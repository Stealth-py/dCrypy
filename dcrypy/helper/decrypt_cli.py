#  /$$$$$$$                                                      /$$     /$$                    
# | $$__  $$                                                    | $$    |__/                    
# | $$  \ $$  /$$$$$$   /$$$$$$$  /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$   /$$  /$$$$$$  /$$$$$$$ 
# | $$  | $$ /$$__  $$ /$$_____/ /$$__  $$| $$  | $$ /$$__  $$|_  $$_/  | $$ /$$__  $$| $$__  $$
# | $$  | $$| $$$$$$$$| $$      | $$  \__/| $$  | $$| $$  \ $$  | $$    | $$| $$  \ $$| $$  \ $$
# | $$  | $$| $$_____/| $$      | $$      | $$  | $$| $$  | $$  | $$ /$$| $$| $$  | $$| $$  | $$
# | $$$$$$$/|  $$$$$$$|  $$$$$$$| $$      |  $$$$$$$| $$$$$$$/  |  $$$$/| $$|  $$$$$$/| $$  | $$
# |_______/  \_______/ \_______/|__/       \____  $$| $$____/    \___/  |__/ \______/ |__/  |__/
#                                          /$$  | $$| $$                                        
#                                         |  $$$$$$/| $$                                        
#                                          \______/ |__/                                        

import click
from dcrypy.helper import decrypt

@click.group('decryption')
def decryption():
    """
    \u001b[34mDecrypt\u001b[0m a \u001b[33mciphertext.\u001b[0m
    """
    pass

@decryption.command("affine", short_help = "You would need a ciphertext and two constant integers A and B.")
def affine():
    ciphertext = click.prompt("\u001b[36m[+] Enter the ciphertext\u001b[0m", type = str)
    dc = decrypt.Decryption(ciphertext=ciphertext)
    a = click.prompt("\u001b[36mEnter the first constant(a, in INTEGER) here\u001b[0m", type = int)
    b = click.prompt("\u001b[36mEnter the second constant(b, in INTEGER) here\u001b[0m", type = int)
    ans = dc.affine(a, b)
    click.secho(f"-> The plaintext for the given ciphertext: {ciphertext} and constants: {a} & {b} is: {ans}", fg = 'blue')


@decryption.command("caesar", short_help = "You would need a ciphertext, and an optional shift, if shift not given, the program will output the caesar cipher for all 26 shifts.")
def caesar():
    ciphertext = click.prompt("\u001b[36m[+] Enter the ciphertext\u001b[0m")
    dc = decrypt.Decryption(ciphertext=ciphertext)
    if not click.confirm("Do you have a shift for the given ciphertext?"):
        ans = dc.caesar_without_shift()
        click.secho(f"[+] The plaintext for each shift from 1...26 for the given ciphertext {ciphertext}: ", fg = 'green')
        for i in range(len(ans)):
            click.secho(f"-> The plaintext for shift: {i+1} is: {ans[i]}", fg = 'blue')
    else:
        shift = click.prompt("\u001b[36mEnter the shift(in INTEGER) here\u001b[0m", type = int)
        ans = dc.caesar_with_shift(shift)
        click.secho(f'-> The plaintext for the given ciphertext: {ciphertext} and shift: {shift} is: {ans}', fg = 'blue')

@decryption.command("keyword", help = "You would need a ciphertext, and a key(STRING).")
def keyword():
    ciphertext = click.prompt("\u001b[36m[+] Enter the ciphertext\u001b[0m", type = str)
    dc = decrypt.Decryption(ciphertext=ciphertext)
    key = click.prompt("\u001b[36m[+] Enter the key\u001b[0m", type = str)
    ans = dc.keyword(key=key)
    click.secho(f"-> The plaintext for the given ciphertext: {ciphertext} and key: {key} is: {ans}", fg = 'blue')

@decryption.command("substitution", help = "You would need a ciphertext, and a key(INTEGER).")
def substitution():
    ciphertext = click.prompt("\u001b[36m[+] Enter the ciphertext\u001b[0m", type = str)
    dc = decrypt.Decryption(ciphertext=ciphertext)
    key = click.prompt("\u001b[36m[+] Enter the key\u001b[0m", type = int)
    ans = dc.substitution(key=key)
    click.secho(f"-> The plaintext for the given ciphertext: {ciphertext} and key: {key} is: {ans}", fg = 'blue')

@decryption.command("vigenere", help = "You would need a ciphertext, and a key(STRING).")
def vigenere():
    ciphertext = click.prompt("\u001b[36m[+] Enter the ciphertext\u001b[0m", type = str)
    dc = decrypt.Decryption(ciphertext=ciphertext)
    key = click.prompt("\u001b[36m[+] Enter the key\u001b[0m", type = str)
    ans = dc.vigenere(key=key)
    click.secho(f"-> The plaintext for the given ciphertext: {ciphertext} and key: {key} is: {ans}", fg = 'blue')