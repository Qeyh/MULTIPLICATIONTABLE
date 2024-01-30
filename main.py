multi_table = []

maxTable=11

#create table
for i in range(maxTable):
    row = []
    for j in range(maxTable):
        row.append(i * j)
    multi_table.append(row)

#delete first row of only 0's to make it better looking
del multi_table[0]

#good looking print
print("############################################")
print("MULTIPLICATION TABLE by Dary, Sela H.W ")
for row in multi_table:
    for i in row:
        print(i, end=" ")
    print("\n")

print("############################################")

#auto pipeline #