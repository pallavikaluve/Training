import random
import string


class TestBase:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_numbers(self, list_of_num):
        total = 0
        for ele in range(0, len(list_of_num)):
            total = total + list_of_num[ele]
        sum_of_numbers = round(total, 3)
        print("Sum of numbers: ", sum_of_numbers)

    def subtract_numbers(self, list_of_num):
        try:
            res = list_of_num[1] - list_of_num[0]
            sub = round(res, 3)
            print("Difference of numbers:", sub)
        except IndexError:
            print("***Error: List index is out of range***")

    def multiply_numbers(self, list_of_num):
        res = 1
        for ele in list_of_num:
            res *= ele
        product = round(res, 3)
        print("Product of numbers: ", product)

    def divide_numbers(self, list_of_num):
        try:
            result = list_of_num[1]/list_of_num[0]
            quotient = round(result, 3)
            print("Quotient of numbers: ", quotient)
        except IndexError:
            print("***Error: List index is out of range***")
        except ZeroDivisionError:
            print("***Error: Cannot divide number by zero***")

    def generate_random_number(self, list_of_num):
        try:
            res = random.randint(list_of_num[0], list_of_num[1])
            print("Random number: ", res)
        except Exception as e:
            print(e, "Exception occured")

    def remove_punctuation(self, string):
        punc = "{}:?><.(@!#$^%&+=)"
        no_punct = ""
        for char in string:
            if char not in punc:
                no_punct = no_punct + char
        print("String without punctuation: ", no_punct)

    def generate_random_string(self, string_length):
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=string_length))
        print("The randomly generated string is : " + str(ran))

