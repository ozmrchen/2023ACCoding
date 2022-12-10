height = int(input("How tall is your tree? "))

for i in range(0, height, 2):
    # add a star on the top
    ...
    # make a tree
    print(" "*(height//2-i//2), "*"*(i+1))
