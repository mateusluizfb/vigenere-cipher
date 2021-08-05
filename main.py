import json

def encrypt_plaintext(key, plaintext):
    keystream = generate_keystream(key, plaintext)
    encrypted_chars = []

    for i in range(len(plaintext)):
        new_char = find_new_chipered_char(keystream[i], plaintext[i])
        encrypted_chars.append(new_char)

    encrypted_text = ("".join(encrypted_chars))
    return encrypted_text

def find_new_chipered_char(keystream_char, plaintext_char):
    file = open('./alphabet_table.json')
    data = json.load(file)
    plaintext_char_unicode = ord(plaintext_char)
    keystream_char_unicode = ord(keystream_char)
    position_in_alphabet = (plaintext_char_unicode + keystream_char_unicode) % 26
    return data[position_in_alphabet]

def decrypt_plaintext(key, encrypted_plaintext):
    keystream = generate_keystream(key, encrypted_plaintext)
    decrypted_chars = []

    for i in range(len(encrypted_plaintext)):
        decrypted_char = find_encrypted_char(keystream[i], encrypted_plaintext[i])
        decrypted_chars.append(decrypted_char)

    decrypted_text = ("".join(decrypted_chars))
    return decrypted_text

def find_encrypted_char(keystream_char, encrypted_char):
    file = open('./alphabet_table.json')
    data = json.load(file)
    encrypted_char_unicode = ord(encrypted_char)
    keystream_char_unicode = ord(keystream_char)
    position_in_alphabet = (encrypted_char_unicode - keystream_char_unicode) % 26
    return data[position_in_alphabet]


def generate_keystream(key, plaintext):
    plaintext_length = len(plaintext)
    repeated_key = key * plaintext_length
    return repeated_key[0:plaintext_length]

print(encrypt_plaintext("KEY", "OLA"))
print(decrypt_plaintext("KEY", "YPY"))
