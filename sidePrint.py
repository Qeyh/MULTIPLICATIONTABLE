multi_table = []
#pipeline test
maxTable=11

#create table
for i in range(maxTable):
    row = []
    for j in range(maxTable):
        row.append(i * j)
    multi_table.append(row)

#delete first row of only 0's to make it better looking
del multi_table[0]

num = input("Please enter a number: ")
try:
    num = int(num)
    if num <= 0 or num > 10:
        print("The number needs to be between 1 and 10")
    else:
        #good looking print
        print("############################################")
        print(f"Your input was: {num}, printing your diagonal line")

        num_row = multi_table[num-1]

        n = len(num_row)
        for i in range(n):
            for j in range(n):
                if i == j:
                    print(num_row[j], end=" ")
                else:
                    print(" ", end=" ")
            print()


        print("############################################")
except ValueError:
    print("I need a number...")