import random
p = 23
g = 5
a = random.randint(1, p-1)
b = random.randint(1, p-1)

A = (g**a)%p
B = (g**b)%p

S_A = (B**a)%p
S_B = (A**b)%p

print(f"Public values (p, g): {p}, {g}")
print(f"A's private key: {a}")
print(f"B's private key: {b}")
print(f"A's public key (A): {A}")
print(f"B's public key (B): {B}")
print(f"Shared secret computed by A: {S_A}")
print(f"Shared secret computed by B: {S_B}")

print(f"Shared secret: {S_A}") if (S_A == S_B) else print("Shared secrets don't match!")