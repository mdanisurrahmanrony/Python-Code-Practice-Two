num = int(input("Enter the number of rows: "))
for row in range(num,0,-1):
    for col in range(1,row+1):
        print(col,end=" ")
    print()