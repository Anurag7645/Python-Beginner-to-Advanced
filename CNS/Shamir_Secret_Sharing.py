from math import prod
def polynomial(x):
    a = 3 
    b = 5 
    c = 65
    return a * (x ** 2) + b * x + c

def generate_shares(n):
    shares = [(i, polynomial(i)) for i in range(1, n+1)]
    return shares

def reconstruct(shares):
    x_s = []
    y_s = []
    for share in shares:
        x_s.append(share[0])
        y_s.append(share[1])
    def lagrange_interpolation(x):
        total = 0
        for i in range(len(x_s)):
            x_i = x_s[i]
            y_i = y_s[i]
            terms = []
            for j in range(len(x_s)):
                if j != i:
                    x_j = x_s[j]
                    term = (x - x_j) / (x_i - x_j)
                    terms.append(term)
            total += y_i * prod(terms) 
        return total
    return lagrange_interpolation(0)

n = 4
t = 3

shares = generate_shares(n)

selected_shares = shares[:t]
reconstructed_secret = reconstruct(selected_shares)

shares, reconstructed_secret