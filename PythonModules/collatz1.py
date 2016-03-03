
print('type a positive integer')
eggs = input()
def collatz(number):
    if number % 2 == 0:
        number = number // 2
        return number
    elif number % 2 == 1:
        number = 3 * number + 1
        return number
while eggs != 1:
    try:
        eggs = collatz(int(eggs))
        print(eggs)
    except ValueError:
        print(str(eggs) + ' isn\'t a proper counting number')
        break
    if int(eggs) < 1:
        print(str(eggs) + ' isn\'t gonna work')
        break
