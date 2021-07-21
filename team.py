n = input()
count = 0


for i in range(int(n)):
    attempt = input()

    if(attempt[0] == str(1) and attempt[2] == str(1) ):
        count = count + 1
    elif(attempt[2] == str(1) and attempt[-1] == str(1) ):
        count = count + 1
    elif(attempt[0] == str(1) and attempt[-1] == str(1) ):
        count = count + 1

print(str(count))