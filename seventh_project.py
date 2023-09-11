


running = True
while running:
    number = input("Zadejte cislo: ")
    if number.isdigit() and (int(number) > 0):
        running = False
running = True
while running:
    exponent = input("Zadejte mocnitele: ")
    if exponent.isdigit() and (int(exponent) > 0):
        running = False

result = number
for i in range(int(exponent)-1):
    result = int(result) * int(number)

print("Vysledek: "+str(result))
