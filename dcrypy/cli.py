#      _  ___                    
#   __| |/ __|_ _ _  _ _ __ _  _ 
#  / _` | (__| '_| || | '_ \ || |
#  \__,_|\___|_|  \_, | .__/\_, |
#                 |__/|_|   |__/ 

__author__ = "Stealth.py"

try:
    import click
    from dcrypy.helper.decrypt_cli import decryption
except Exception as e:
    print(e)

@click.group()
def cli():
    """
    \b
     _  ___                    
  __| |/ __|_ _ _  _ _ __ _  _ 
 / _` | (__| '_| || | '_ \ || |
 \__,_|\___|_|  \_, | .__/\_, |
                |__/|_|   |__/ 

    \u001b[34mdCrypy\u001b[0m is a CLI based \u001b[33mdecryption and encryption tool\u001b[0m, which enables the user to decrypt a certain ciphertext or encrypt a certain plaintext to a ciphertext, using the ciphers provided.

    \b
    \u001b[36m
    affine cipher
    atbash cipher
    caesar cipher
    keyword cipher
    substitution cipher
    vigenere cipher\u001b[0m
    """
    pass

cli.add_command(decryption)