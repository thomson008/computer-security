import sys
import os
from common import *
from const import *

mode = sys.argv[1]

dialog = Dialog('print')

socket_a, aes_a = setup('alice', BUFFER_DIR, BUFFER_FILE_NAME)
os.rename(BUFFER_DIR + BUFFER_FILE_NAME, BUFFER_DIR + 'buffer2')

dialog.think('Nice, getting there...')

socket_b, aes_b = setup('bob', BUFFER_DIR, BUFFER_FILE_NAME)

dialog.think('Hehe, it\'s working!')

received_from_alice = receive_and_decrypt(aes_b, socket_b)
dialog.chat('Alice slurred: ' + '"' + received_from_alice + '"')

if mode == '--relay':
    to_send = received_from_alice

elif mode == '--custom':
    dialog.prompt('Input what you would like Alice to say to Bob')
    to_send = input()
else:
    to_send = 'I hate you!'

encrypt_and_send(to_send, aes_a, socket_a)

received_from_bob = receive_and_decrypt(aes_a, socket_a)
dialog.chat('Bob slurred: ' + '"' + received_from_bob + '"')

if mode == '--relay':
    to_send = received_from_bob

elif mode == '--custom':
    dialog.prompt('Input what you would like Bob to say to Alice')
    to_send = input()
else:
    to_send = 'You broke my heart...'

encrypt_and_send(to_send, aes_b, socket_b)

tear_down(socket_a, BUFFER_DIR, 'buffer2')
tear_down(socket_b, BUFFER_DIR, BUFFER_FILE_NAME)