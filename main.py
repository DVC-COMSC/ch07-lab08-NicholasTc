# check if there is more than 1 values
try:
    numbers = [5,20,30,30,50]
    num = int(input("Enter number from list to be removed: "))

    if numbers.count(num) > 1:
        # removing all the duplicate element first
        numbers = list(set(numbers))
        
        for n in numbers:
            if n == num:
                numbers.remove(n)
            print(n)
    else:
        numbers.remove(num)
except ValueError:
    numbers.clear()

print(numbers)
