n,k = input().split()
count = 0


scores = input().split()

if(len(scores) == int(n)):
     for x in scores:
        if(int(x) > int(k)):
            count = count + 1
        elif(scores[0] == x):
            if(scores[0] <= k and scores[0] > "0"):
                count = count + 1

            
    
print(count)