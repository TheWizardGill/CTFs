#!/usr/bin/python3
from datetime import datetime, timezone
import random
from binascii import unhexlify

encrypted_hex = "22ECCDB90936D5C2454A65A5BB4C120FB1C8567381C6DB368EB57D4C6BE8B6D8C860E5C6FAC1F48BF2291A5C9EA3C354715857E7"

# Seconds from epoch, need to figure this piece out
seed = 1710550800

encrypted_bytes = unhexlify(encrypted_hex)
# Convert the datetime to a timestamp (Unix time)
random.seed(seed)

random_buffer = [random.randint(0, 255) for _ in range(len(encrypted_bytes))]
flag_bytes = bytes([encrypted_bytes[i] ^ random_buffer[i] for i in range(len(encrypted_bytes))])

try:
    flag = flag_bytes.decode("ASCII")
    print("Decrypted Flag:", flag)
except UnicodeDecodeError:
    # If the data isn't ASCII, you might handle it differently, for example, printing the hex representation
    print("The flag contains non-ASCII bytes:", flag_bytes.hex())
