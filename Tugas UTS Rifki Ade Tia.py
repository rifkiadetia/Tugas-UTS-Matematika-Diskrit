print("NAMA    : RIFKI ADE TIA")
print("NIM     : 312510334")
print("KELAS   : TI.25.C5")

# Pernyataan: Jika n genap maka n genap (tautologi)

def is_even(n):
    return n % 2 == 0

def tautologi(limit=10):
    print("n\t| P (n genap?)\t| P -> P")
    print("-"*35)
    for n in range(limit+1):
        P = is_even(n)
        result = (not P) or P  # logika implikasi P -> P
        print(f"{n}\t| {P}\t\t| {result}")
    print("\nKesimpulan: Pernyataan selalu benar (tautologi).")

tautologi()