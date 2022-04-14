n = int(input())
name_numbers = [input().split() for _ in range(n)]
phone_book = {k: v for k, v in name_numbers}

for x, y in phone_book.items():
    n= str(input())
    if x == n:
        print(x+'='+y)
    else:
        print('Not found')


#Sample Input

#3
#sam 99912222
#tom 11122222
#harry 12299933
#sam
#edward
#harry
#Sample Output

#sam=99912222
#Not found
#harry=12299933
