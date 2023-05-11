# User input for the total number of lines
num_lines = int(input("Enter the total number of lines: "))

# Roman numeral ‘5’ ( ‘Ⅴ’ )
for i in range(num_lines):
    for j in range(num_lines-i):
        print(" ", end="")
    for k in range(i+1):
        print("Ⅴ", end="")
    print()

# Roman numeral ‘4’ ( ‘IV’ )
for i in range(num_lines):
    for j in range(num_lines-i):
        print(" ", end="")
    for k in range(i+1):
        if k == 0 or k == i:
            print("Ⅳ", end="")
        else:
            print(" ", end="")
    print()

# Diamond symbol ( ‘◆’ )
for i in range(num_lines):
    for j in range(num_lines-i):
        print(" ", end="")
    for k in range(i*2+1):
        print("◆", end="")
    print()
for i in range(num_lines-2, -1, -1):
    for j in range(num_lines-i):
        print(" ", end="")
    for k in range(i*2+1):
        print("◆", end="")
    print()

