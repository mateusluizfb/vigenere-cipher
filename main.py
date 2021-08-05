import json

def cipher_plaintext(key, plaintext):
    keystream = generate_keystream(key, plaintext)
    ciphered_chars = []

    for i in range(len(plaintext)):
        new_char = match_char(plaintext[i], keystream[i])
        ciphered_chars.append(new_char)

    ciphered_text = ("".join(ciphered_chars))
    return ciphered_text

def match_char(keystream_char, plaintext_char):
    file = open('./alphabet_table.json')
    data = json.load(file)
    plaintext_char_unicode = ord(plaintext_char)
    keystream_char_unicode = ord(keystream_char)
    position_in_alphabet = (plaintext_char_unicode + keystream_char_unicode) % 26
    return data[position_in_alphabet]

def generate_keystream(key, plaintext):
    plaintext_length = len(plaintext)
    repeated_key = key * plaintext_length
    return repeated_key[0:plaintext_length]

print(cipher_plaintext("key", "Ola"))
