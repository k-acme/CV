def is_prime(number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break
    return prime


number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Number is even!")
else:
    print("Number is odd!")

print("Number is prime: {}".format(is_prime(number)))

