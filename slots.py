from random import randint

array = [[0,0,0],[0,0,0],[0,0,0]]
tokens = 0

while True:
    print("Would you like to buy some tokens? You currently have "
          + str(tokens) + " tokens.\n")
    
    print("Press b to buy some tokens.\n")
    if input() == "b":
        tokens += 5
        print("You now have " + str(tokens) + " tokens.\n")

    print("Fancy a spin? y or n \n")
    answer = input()
    if answer == "y":
        if tokens == 0:
            print("You need to buy more tokens!\n")
            continue
        tokens -= 1
        
        for count, ele in enumerate(array):
            for count2, ele2 in enumerate(array[count]):
                array[count][count2] = randint(1,9)

        for i in array:
            for j in i:
                print(j, end = "")
            print()

        for i in array:
            if i[0] == i[1] and i[1] == i[2]:
                print("Winner!")
                print("Have 10 tokens!")
                tokens += 10

        if array[0][0] == array[1][1] and array[1][1] == array[2][2]:
            print("Winner!")
            print("Have 10 tokens!")
            tokens += 10

        if array[0][2] == array[1][1] and array[1][1] == array[2][0]:
            print("Winner!")
            print("Have 10 tokens!")
            tokens += 10

    elif answer == "n":
        print("Ok, bye!")
        break
    input()
