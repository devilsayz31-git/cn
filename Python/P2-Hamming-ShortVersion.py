# Hamming (7,4) Code - Error Detection and Correction
# Bit positions: 1  2  3  4  5  6  7
#                P1 P2 D1 P4 D2 D3 D4


def read_bits(prompt, length):
    bits = input(prompt).strip()
    while len(bits) != length or any(b not in "01" for b in bits):
        print("Invalid input. Enter exactly", length, "bits (0 or 1).")
        bits = input(prompt).strip()
    return list(map(int, bits))


# ---------- Sender side: generate Hamming code ----------
d = read_bits("Enter 4 data bits: ", 4)

p1 = d[0] ^ d[1] ^ d[3]  # checks positions 1, 3, 5, 7
p2 = d[0] ^ d[2] ^ d[3]  # checks positions 2, 3, 6, 7
p4 = d[1] ^ d[2] ^ d[3]  # checks positions 4, 5, 6, 7

code = [p1, p2, d[0], p4, d[1], d[2], d[3]]

print("Parity bits  : P1 =", p1, " P2 =", p2, " P4 =", p4)
print("Hamming Code :", "".join(map(str, code)))

# ---------- Receiver side: detect and correct ----------
r = read_bits("\nEnter received 7 bits: ", 7)

s1 = r[0] ^ r[2] ^ r[4] ^ r[6]
s2 = r[1] ^ r[2] ^ r[5] ^ r[6]
s4 = r[3] ^ r[4] ^ r[5] ^ r[6]

error_position = s4 * 4 + s2 * 2 + s1
print("Syndrome (S4 S2 S1):", s4, s2, s1)

if error_position == 0:
    print("No error detected")
else:
    print("Error detected at position:", error_position)
    r[error_position - 1] ^= 1
    print("Corrected Code:", "".join(map(str, r)))

data_bits = [r[2], r[4], r[5], r[6]]
print("Original Data :", "".join(map(str, data_bits)))
