color = ["red","white","yellow","blue"]
for i in range(1, 2401):
    print(i,color[i%4-1])

n = int(input("Please enter a number of the locker: "))
for i in range(4):
    if (n-1) % 4 == i:
        print(f"The color is {color[i]}.")

col = input("Please enter a color and make sure the spelling is correct: ")
if col not in color:
    print("The lockers are not painted in this color.")

while col in color:
    numbers = []
    for n in range(1,5):
        if color.index(col)+1 == n:
            while 0 < n < 601:
                for n in range(n,2401,4):
                    numbers.append(n)
                print(f"The {col} locker numbers are {numbers}")

    break
