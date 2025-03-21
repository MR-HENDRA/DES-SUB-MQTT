# Tabel Hexa to Biner
tabel_hex2bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

# Tabel Biner to Hexa
tabel_bin2hex = {
    "0000": "0",
    "0001": "1",
    "0010": "2",
    "0011": "3",
    "0100": "4",
    "0101": "5",
    "0110": "6",
    "0111": "7",
    "1000": "8",
    "1001": "9",
    "1010": "A",
    "1011": "B",
    "1100": "C",
    "1101": "D",
    "1110": "E",
    "1111": "F",
}

# Tabel Initial Permutation
tabel_ip = [
    58,
    50,
    42,
    34,
    26,
    18,
    10,
    2,
    60,
    52,
    44,
    36,
    28,
    20,
    12,
    4,
    62,
    54,
    46,
    38,
    30,
    22,
    14,
    6,
    64,
    56,
    48,
    40,
    32,
    24,
    16,
    8,
    57,
    49,
    41,
    33,
    25,
    17,
    9,
    1,
    59,
    51,
    43,
    35,
    27,
    19,
    11,
    3,
    61,
    53,
    45,
    37,
    29,
    21,
    13,
    5,
    63,
    55,
    47,
    39,
    31,
    23,
    15,
    7,
]

# Tabel Expansion
tabel_expansion = [
    32,
    1,
    2,
    3,
    4,
    5,
    4,
    5,
    6,
    7,
    8,
    9,
    8,
    9,
    10,
    11,
    12,
    13,
    12,
    13,
    14,
    15,
    16,
    17,
    16,
    17,
    18,
    19,
    20,
    21,
    20,
    21,
    22,
    23,
    24,
    25,
    24,
    25,
    26,
    27,
    28,
    29,
    28,
    29,
    30,
    31,
    32,
    1,
]

# Tabel P-Box
tabel_pbox = [
    16,
    7,
    20,
    21,
    29,
    12,
    28,
    17,
    1,
    15,
    23,
    26,
    5,
    18,
    31,
    10,
    2,
    8,
    24,
    14,
    32,
    27,
    3,
    9,
    19,
    13,
    30,
    6,
    22,
    11,
    4,
    25,
]

# Tabel S-Box
tabel_sbox = [
    # S1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    ],
    # S2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
    ],
    # S3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
    ],
    # S4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
    ],
    # S5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
    ],
    # S6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
    ],
    # S7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
    ],
    # S8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ],
]

# Tabel Invers Initial Permutation
tabel_iip = [
    40,
    8,
    48,
    16,
    56,
    24,
    64,
    32,
    39,
    7,
    47,
    15,
    55,
    23,
    63,
    31,
    38,
    6,
    46,
    14,
    54,
    22,
    62,
    30,
    37,
    5,
    45,
    13,
    53,
    21,
    61,
    29,
    36,
    4,
    44,
    12,
    52,
    20,
    60,
    28,
    35,
    3,
    43,
    11,
    51,
    19,
    59,
    27,
    34,
    2,
    42,
    10,
    50,
    18,
    58,
    26,
    33,
    1,
    41,
    9,
    49,
    17,
    57,
    25,
]

# Tabel Permutation Compression 1
tabel_pc1 = [
    57,
    49,
    41,
    33,
    25,
    17,
    9,
    1,
    58,
    50,
    42,
    34,
    26,
    18,
    10,
    2,
    59,
    51,
    43,
    35,
    27,
    19,
    11,
    3,
    60,
    52,
    44,
    36,
    63,
    55,
    47,
    39,
    31,
    23,
    15,
    7,
    62,
    54,
    46,
    38,
    30,
    22,
    14,
    6,
    61,
    53,
    45,
    37,
    29,
    21,
    13,
    5,
    28,
    20,
    12,
    4,
]

# Tabel Permutation Compression 2
tabel_pc2 = [
    14,
    17,
    11,
    24,
    1,
    5,
    3,
    28,
    15,
    6,
    21,
    10,
    23,
    19,
    12,
    4,
    26,
    8,
    16,
    7,
    27,
    20,
    13,
    2,
    41,
    52,
    31,
    37,
    47,
    55,
    30,
    40,
    51,
    45,
    33,
    48,
    44,
    49,
    39,
    56,
    34,
    53,
    46,
    42,
    50,
    36,
    29,
    32,
]

# Tabel Left Shift Operations
tabel_lso = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


# Fungsi untuk konversi heksadesimal ke biner
def hex2bin(s):
    s = s.upper()  # Konversi ke huruf besar
    return "".join(tabel_hex2bin[c] for c in s)


# Fungsi untuk konversi biner ke heksadesimal
def bin2hex(s):
    return "".join(tabel_bin2hex[s[i : i + 4]] for i in range(0, len(s), 4))


# Fungsi untuk konversi biner ke desimal
def bin2dec(binary):
    return int(binary, 2)


# Fungsi untuk konversi desimal ke biner
def dec2bin(num, bits=4):
    return format(num, f"0{bits}b")


# Fungsi untuk konversi ASCII ke heksadesimal
def ascii2hex(s):
    return "".join(f"{ord(c):02X}" for c in s)


# Fungsi untuk konversi heksadesimal ke ASCII
def hex2ascii(s):
    return "".join(chr(int(s[i : i + 2], 16)) for i in range(0, len(s), 2))


# Fungsi untuk permutasi
def permute(k, arr, n):
    return "".join(k[i - 1] for i in arr)


# Fungsi untuk pergeseran bit ke kiri
def shift_left(k, nth_shifts):
    return k[nth_shifts:] + k[:nth_shifts]


# Fungsi untuk operasi XOR
def xor(a, b):
    return "".join(str(int(x) ^ int(y)) for x, y in zip(a, b))


# Fungsi untuk menghasilkan round keys
def generate_round_keys(key_hex):
    key = hex2bin(key_hex)
    print(f"Key (Binary): {key}\n")
    key = permute(key, tabel_pc1, 56)
    print(f"Key after PC1: {key}")
    left = key[:28]
    print(f"C0: {left}")
    right = key[28:56]
    print(f"D0: {right}\n")
    rkb = []
    print(f"=== KEY GENERATION ===\n")
    for i in range(16):
        print(f"--- Round {i+1} ---")
        left = shift_left(left, tabel_lso[i])
        print(f"C{i+1}: {left}")
        right = shift_left(right, tabel_lso[i])
        print(f"D{i+1}: {right}")
        combine_str = left + right
        print(f"C{i+1}D{i+1}: {combine_str}")
        round_key = permute(combine_str, tabel_pc2, 48)
        rkb.append(round_key)
        print(f"Key{i+1}: {round_key}\n")
    return rkb


# Fungsi untuk substitusi S-Box
def sbox_substitution(xor_result):
    sbox_str = ""
    for j in range(8):
        row = bin2dec(xor_result[j * 6] + xor_result[j * 6 + 5])
        col = bin2dec("".join(xor_result[j * 6 + 1 : j * 6 + 5]))
        val = tabel_sbox[j][row][col]
        sbox_str += dec2bin(val, 4)
    return sbox_str


# Fungsi untuk permutasi P-Box
def pbox_permutation(sbox_str):
    return permute(sbox_str, tabel_pbox, 32)


# Fungsi untuk dekripsi DES
def decrypt(ct, rkb):
    ct = hex2bin(ct)
    print(f"\nCiphertext (Binary): {ct}\n")
    ct = permute(ct, tabel_ip, 64)
    print(f"Ciphertext after IP: {ct}\n")
    left, right = ct[:32], ct[32:]
    print(f"R16: {left}")
    print(f"L16: {right}\n")
    for i in range(16):
        round_number = i + 1
        key_used = 16 - i
        print(f"--- Round {round_number} (K{key_used}) ---")
        right_expanded = permute(right, tabel_expansion, 48)
        print(f"E(R{key_used}): {right_expanded}")
        xor_result = xor(right_expanded, rkb[i])
        print(f"A{key_used}: {xor_result}")
        sbox_str = sbox_substitution(xor_result)
        print(f"B{key_used}: {sbox_str}")
        pbox_str = pbox_permutation(sbox_str)
        print(f"P(B{key_used}): {pbox_str}")
        print(f"L{key_used - 1}: {right}")
        left = xor(left, pbox_str)
        print(f"R{key_used - 1}: {left}")
        left, right = right, left
        combined = right + left
        if i != 15:
            print(f"L{key_used - 1}R{key_used - 1}: {left} {right}\n")
        else:
            print(f"R0L0: {right} {left}\n")
    pt = permute(combined, tabel_iip, 64)
    return pt


def validate_input(s):
    if len(s) != 8:
        print("Error: Plaintext must be exactly 8 ASCII characters.")
        return False
    if not all(ord(c) < 128 for c in s):
        print("Error: Plaintext must be an ASCII char (0-127).")
        return False
    return True


def validate_key(s):
    if len(s) != 16:
        print("Error: Key must be exactly 16 hexadecimal char.")
        return False
    try:
        int(s, 16)
        return True
    except ValueError:
        print("Error: Key must be hexadecimal (0-9, A-F).")
        return False


def get_valid_input(prompt, validation_func):
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input


def main():
    ct = get_valid_input("Enter ciphertext (16 hexadecimal characters): ", validate_key)
    key = get_valid_input("Enter key (16 hexadecimal characters): ", validate_key)

    print(f"\nCiphertext (Hex): {ct}")
    rkb = generate_round_keys(key)
    reversed_rkb = rkb[::-1]  # Reverse round keys untuk dekripsi

    print("\n--- DECRYPTION ---\n")
    pt = decrypt(ct, reversed_rkb)
    pt_hex = bin2hex(pt)
    print("\nPlaintext (Binary):", pt)
    print("Plaintext (Hex):", pt_hex)
    print("Plaintext (ASCII):", hex2ascii(pt_hex))


# Main
if __name__ == "__main__":
    main()
