# ******************************
# Make your Code
# ******************************
numbers = list(map(int, input().split()))

userInput = int(input())
prev_num = numbers[0]

# numbers.insert(2, 20)
for y in range(5):
    if userInput > prev_num and userInput < numbers[y]:
        numbers.insert(y, userInput)
        

    prev_num = numbers[y]

for n in numbers:
    print(n, end=" ")
