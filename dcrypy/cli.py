__author__ = "Stealth.py"

try:
    import click
    from dcrypy.helper.decrypt_cli import decryption
except Exception as e:
    print(e)

@click.group()
def cli():
    """
    \u001b[34mdCrypy\u001b[0m is a CLI based \u001b[33mdecryption and encryption tool\u001b[0m, which enables the user to decrypt a certain ciphertext or encrypt a certain plaintext to a ciphertext, using the ciphers provided.

    \b
    \u001b[36maffine cipher
    caesar cipher
    keyword cipher
    substitution cipher
    vigenere cipher\u001b[0m
    """
    pass

cli.add_command(decryption)