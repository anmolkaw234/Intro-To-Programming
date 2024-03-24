n = int(input())
rows = 2*n
i = (rows // 2) - (n-1)
j = 2*n - 2

while j <= (rows - 2):
        print("*" * i, end="")
        print(" " * j, end="")
        print("*" * i, end="\n")
        i = i + 1
        j = j - 2
        if i ==  n + 1:
            break



