from send_sms import *
from collections_text import *
import os

lst = ['feral-file-009-unsupervised-refik-anadol',
       'ratdao-art',
       'lostsoulssanctuary',
       'planetdaos',
       'creativeworkstudios-tokens',
       'rug-radio-membership-pass',
       'cryptoongoonz',
       'ruggenesis-nft',
       'metacard-by-fullsend',
       'wolf-game-migrated']

def main():

    final = final_string(lst)
    send_text(final,os.environ['phone_num'])

if __name__ == "__main__":
    main()