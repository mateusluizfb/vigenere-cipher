import json

def cipher_plaintext(key, plaintext):
    file = open('./alphabet_table.json')
    data = json.load(file)

def generate_keystream(key, plaintext):
    plaintext_length = len(plaintext)
    repeated_key = key * plaintext_length
    return repeated_key[0:plaintext_length]
