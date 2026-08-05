# marks1 = [10,20,30]
# print(marks1)

marks=[
    [10,20,30],
    [40,50,60],
    [70,80,90],
    [71,81,91]
]

print(marks[2][1])

print(len(marks))

for i in range(len(marks)):
    for j in range(len(marks[i])):
        print(marks[i][j], end="\t")
    print()

for j in range(len(marks[0])):
    for i in range(len(marks)):
        print(marks[i][j] , end="\t")   
        # end="\t") is ka use isliya ka ki end="\t" ka use output ko same line me tab (space) ke saath print karne ke liye kiya jata hai.
    print()



# marks[0][0]
# marks[1][0]
# marks[2][0]
# marks[3][0]