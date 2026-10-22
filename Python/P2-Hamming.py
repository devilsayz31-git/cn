# Hamming Code - Error Detection and Correction (any number of data bits)
# Parity bits sit at positions 1, 2, 4, 8, ... (powers of 2)
# Number of parity bits r: smallest r with 2^r >= m + r + 1


def read_bits(prompt, length):
    bits = input(prompt).strip()
    while len(bits) != length or any(b not in "01" for b in bits):
        print("Invalid input. Enter exactly", length, "bits (0 or 1).")
        bits = input(prompt).strip()
    return list(map(int, bits))


def is_parity_position(pos):
    return (pos & (pos - 1)) == 0  # true for 1, 2, 4, 8, ...


# ---------- Sender side: generate Hamming code ----------
m = int(input("Enter number of data bits: "))

r = 0
while 2 ** r < m + r + 1:
    r += 1
total = m + r

d = read_bits("Enter " + str(m) + " data bits: ", m)

# code[0] is unused so that list index = bit position
code = [0] * (total + 1)
k = 0
for pos in range(1, total + 1):
    if is_parity_position(pos):
        code[pos] = 0
    else:
        code[pos] = d[k]
        k += 1

parity_text = []
for i in range(r):
    p = 2 ** i
    parity = 0
    for j in range(1, total + 1):
        if j & p:
            parity ^= code[j]
    code[p] = parity
    parity_text.append("P" + str(p) + " = " + str(parity))

print("Parity bits needed (r):", r)
print("Total bits (m + r)    :", total)
print("Parity bits  :", "  ".join(parity_text))
print("Hamming Code :", "".join(map(str, code[1:])))

# ---------- Receiver side: detect and correct ----------
received = read_bits("\nEnter received " + str(total) + " bits: ", total)
rc = [0] + received

error_position = 0
syndrome = []
for i in range(r):
    p = 2 ** i
    parity = 0
    for j in range(1, total + 1):
        if j & p:
            parity ^= rc[j]
    syndrome.append(parity)
    if parity != 0:
        error_position += p

print("Syndrome (S" + " S".join(str(2 ** i) for i in reversed(range(r))) + "):",
      *reversed(syndrome))

if error_position == 0:
    print("No error detected")
elif error_position > total:
    print("Error position", error_position, "is out of range. More than one bit is wrong.")
else:
    print("Error detected at position:", error_position)
    rc[error_position] ^= 1
    print("Corrected Code:", "".join(map(str, rc[1:])))

if error_position <= total:
    data_bits = [rc[pos] for pos in range(1, total + 1) if not is_parity_position(pos)]
    print("Original Data :", "".join(map(str, data_bits)))
