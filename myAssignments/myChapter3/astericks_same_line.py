num = "*"
rows = 10

for i in range(1, rows + 1):
    
    for k in range(i):
        print(num, end="")
    for k in range(rows - i):
        print(" ", end="")  
    print("   ", end="")  

    
    for k in range(rows - i + 1):
        print(num, end="")
    for k in range(i - 1):
        print(" ", end="")
    print("   ", end="")

    
    for k in range(i - 1):
        print(" ", end="")
    for k in range(rows - i + 1):
        print(num, end="")
    print("   ", end="")

    
    for k in range(rows - i):
        print(" ", end="")
    for k in range(i):
        print(num, end="")

    print()  