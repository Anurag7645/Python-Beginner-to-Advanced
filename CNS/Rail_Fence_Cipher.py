def rail_cipher_encryption(pt,key):
    rail = [['\n' for i in range(len(pt))]for j in range(key)]
    dir_down = False
    row,col = 0,0
    for i in range(len(pt)):
        if(row == 0) or (row == key-1):
            dir_down = not dir_down
        rail[row][col] = pt[i]
        col += 1
        if(dir_down):
            row += 1
        else:
            row -= 1

    result = []
    for i in range(key):
        for j in range(len(pt)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return("".join(result))


def rail_cipher_decrypt(encrypted,key):
    rail = [['\n' for i in range(len(encrypted))]for j in range(key)]
    dir_down = None
    row, col = 0, 0
    for i in range(len(encrypted)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        rail[row][col] = '*'
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(key):
        for j in range(len(encrypted)):
            if ((rail[i][j] == '*') and (index < len(encrypted))):
                    rail[i][j] = encrypted[index]
                    index += 1

    result = []
    row, col = 0, 0
    for i in range(len(encrypted)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    return("".join(result))


key = 4
pt = "THIS IS A SECRET MESSAGE"

encrypted = rail_cipher_encryption(pt, key)
print(f"Encrypted: {encrypted}")

decrypted = rail_cipher_decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")