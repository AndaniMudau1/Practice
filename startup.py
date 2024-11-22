# Name: 

def calculate_product_or_sum(num1, num2):
    """
    Calculate the multiplication and sum of two numbers.
    If the product is <= 1000, return it; otherwise, return the sum.
    """
    multiplication = num1*num2
    if multiplication <=1000:
        return multiplication
    else:
        return num1+num2
    
result1 = calculate_product_or_sum(20, 30)  
result2 = calculate_product_or_sum(40, 30)  
print("Result 1:", result1)
print("Result 2:", result2)

numbers=[1,2,3,4]


def sum_of_list(numbers):
    c=0
    for x in numbers:
        c=c+x
    return c

print(sum_of_list(numbers))

print("Hello")
def multiply_list(numbers):
    """
    Multiply all the numbers in a given list.
    """
    result = 1 # Replace with your code
    for num in numbers:
        result *= num
    return result

print("Product of List:", multiply_list([1,2,3,4]))


def characters_at_even_indices(input_string):
    """
    Display characters at even index positions.
    """
    return input_string[::2]  # Replace with your code

print("Characters at Even Indices:", characters_at_even_indices("Python")) 

print('_____')

def check_first_last_same(numbers):
    """
    Check if the first and last elements of a list are the same.
    """
    return numbers[0] == numbers[-1] if numbers else False # Replace with your code

print("First and Last Same:", check_first_last_same([10, 20, 30, 100, 10])) 

def numbers_divisible_by_five(numbers):
    """
    Display numbers divisible by 5 from a list.
    """
    for x in numbers:
        if x%5==0:
            print(x)
            
print(numbers_divisible_by_five([10,25,44,63,80,100]))

# Intermediate Exercises

def count_even_odd(numbers):
    """
    Count even and odd numbers in a list.`  
    """
    numbers = [1,2,3,4,5]
    even = 0
    odd = 0
    for x in numbers:
        if x%2 ==0:
            even += 1 
        else:
            odd += 1    
    return even , odd
even, odd = count_even_odd(numbers)
#odd = count_even_odd
print("Counted even numbers:", even)
print("Counted odd numbers:", odd)

def skip_numbers():
    """
    Print all numbers from 0 to 6 except 3 and 6.
    """
    numbers = [0,1,2,3,4,5,6] 
    for x in numbers:
        if x == 3 or x == 6:
            continue
        print(x)

#print("All numbers from 0 to 6 except 3 and 6:", skip_numbers())
skip_numbers()

def reverse_string(input_string):
    """
    Reverse a given string.
    """
    return input_string[::-1]

print("Reversed string:", reverse_string("python"))

def remove_first_n_chars(input_string, n):
    """
    Remove the first n characters from a string.
    """
    return input_string[n:]

print("First n characters removed:", remove_first_n_chars("Hello there!",6))

def max_of_three(num1, num2, num3):
    """
    Find the maximum of three numbers.
    """
    return max(num1,num2,num3)

print("The maximum of three numbers is:", max_of_three(20,30,40))

                                                                                                                                                        

# Advanced Exercises

def count_upper_lower(input_string):
    """
    Count uppercase and lowercase letters in a string.
    """
    uppercase_count = 0
    lowercase_count = 0
    for char in input_string:
        if char.isupper():
           uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
    return uppercase_count, lowercase_count  

result = count_upper_lower("Hello World!")

print("The uppercase is:", result[0])
print("The lower case:", result[1])      

        
              


def distinct_elements(numbers):
    """
    Return distinct elements from a list.
    """
    return list(set(numbers))

print("Distinct elements:", distinct_elements([1,1,2,3,4,5,2,3,4,5,6]))

def is_prime(number):
    """
    Check if a number is prime.
    """
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5 ) + 1): 
        if number % i == 0:
           return False
    return True 

print("Is 7 prime?:",is_prime(7))
print("Is 10 prime?:", is_prime(10))  

def factorial(number):
    """
    Find the factorial of a number.
    """
    if number == 0 or number == 1:
        return 1
    result = 1
    for i in range(2, number +1):
        result *= i
    return result

print("Factorial of 6:", factorial(6)) 

def check_voting_eligibility(name, age):
    """
    Check if a person is eligible to vote.
    """
    if age >= 18:
        return f"{name} is eligible to vote."
    else:
        return f"{name} is not eligible to vote."
    
print(check_voting_eligibility("Andani", 56))    
print(check_voting_eligibility("Murendeni", 4)) 

# Bonus Exercises

def fibonacci_sequence(n):
    """
    Print the Fibonacci sequence up to n terms. 

    """
    pass  # Replace with your code

def common_elements(list1, list2):
    """
    Find common elements in two lists.
    """
    pass  # Replace with your code

def is_palindrome(input_string):
    """
    Check if a string is a palindrome.
    """
    pass  # Replace with your code

def second_largest(numbers):
    """
    Find the second largest number in a list.
    """
    pass  # Replace with your code

def sum_of_digits(number):
    """
    Calculate the sum of digits in an integer.
    """
    pass  # Replace with your code



# Do not touch the following section *****
# Main function to test the solutions
if __name__ == "__main__":
    print("Python Practice Problems")
    print("Implement the functions and test them here!")
