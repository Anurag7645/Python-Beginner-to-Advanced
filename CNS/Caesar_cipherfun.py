def caesar_cipher_encrypt(char, key, text_list):
    for letter, value in text_list.items():
        if char == letter:
            Enc = (value + key) % 26
            for enc_letter, enc_value in text_list.items():
                if enc_value == Enc:
                    return enc_letter
    return char

def caesar_cipher_decrypt(char, key, text_list):
    for letter, value in text_list.items():
        if char == letter:
            Enc = (value - key) % 26
            for enc_letter, enc_value in text_list.items():
                if enc_value == Enc:
                    return enc_letter
    return char

original_msg = "Anurag Pandey"
key = 4
text_list = {
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25
}

Enc_Msg = ""
Dec_Msg = ""
for char in original_msg.upper():
    Enc_Msg += caesar_cipher_encrypt(char, key, text_list)
for char in Enc_Msg.upper():
    Dec_Msg += caesar_cipher_decrypt(char, key, text_list)

print("Original message:", original_msg)
print("Encrypted message:", Enc_Msg)
print("Decrypted message:", Dec_Msg)
