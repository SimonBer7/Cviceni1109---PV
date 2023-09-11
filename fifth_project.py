
day = int(0)
month = int(0)
year = int(0)

running = True
while running:
    d = input("Enter day: ")
    if d.isdigit():
        day = d
        running = False

running = True
while running:
    m = input("Enter month: ")
    if m.isdigit():
        month = m
        running = False

running = True
while running:
    y = input("Enter year: ")
    if y.isdigit():
        year = y
        running = False


print(str(day)+"."+str(month)+"."+str(year))
