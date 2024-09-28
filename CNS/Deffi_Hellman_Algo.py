import random
p = 23
g = 5
a = random.randint(1, p-1)
b = random.randint(1, p-1)

A = pow(g, a, p)
B = pow(g, b, p)

S_A = pow(B, a, p)
S_B = pow(A, b, p)

print(f"Public values (p, g): {p}, {g}")
print(f"A's private key: {a}")
print(f"B's private key: {b}")
print(f"A's public key (A): {A}")
print(f"B's public key (B): {B}")
print(f"Shared secret computed by A: {S_A}")
print(f"Shared secret computed by B: {S_B}")

assert S_A == S_B, "Shared secrets don't match!"
print(f"Shared secret: {S_A}")