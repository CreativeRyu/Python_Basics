#Write your code below this line 👇
isPrime = "It's a prime number."
isNotPrime = "It's not a prime number."

def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime == True:
    print(isPrime)
  else:
    print(isNotPrime)

  input()

#Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)