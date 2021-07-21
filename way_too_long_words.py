n = input()
count = 0

for i in range(int(n)):
    string = input()

    if(len(string) > 10):
        print(string[0] + str(len(string) - 2) + string[-1])
    else:
        print(string)

