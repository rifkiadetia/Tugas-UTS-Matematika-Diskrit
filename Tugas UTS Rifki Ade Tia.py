print("NAMA    : RIFKI ADE TIA")
print("NIM     : 312510334")
print("KELAS   : TI.25.C5")

# Pembuktian dengan pemrograman Python
# Jika n bilangan genap, maka n^2 juga genap

def is_even(n):
    return n % 2 == 0

def test_statement(limit=20):
    for n in range(-limit, limit + 1):
        if is_even(n):
            print(f"n = {n}, n^2 = {n*2}, genap? {is_even(n*2)}")

test_statement()