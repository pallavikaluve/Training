from helper.test_base import TestBase

list_for_sum = [34, 56, 93.89, 130, 4]
list_for_difference = [56, 98.98765]
list_for_product = [67, 3.4, 23, 5]
list_for_quotient = [678, 12]
list_for_random = [9, 89]
string = "Current System: Windows."
number = -8
file_path= "D:\Training\Module_practice\Documents\Write"
write_row = ['Dog', 'Cat', 'Elephant', 'Fish']

class Module(TestBase):
    def call_functions(self):
        self.add_numbers(list_for_sum)
        self.subtract_numbers(list_for_difference)
        self.multiply_numbers(list_for_product)
        self.divide_numbers(list_for_quotient)
        self.generate_random_number(list_for_random)
        self.remove_punctuation(string)
        self.generate_random_string(10)
        self.check_number(number)
        self.write_into_csv_file(write_row, file_path)
        self.read_csv_file(file_path)


obj = Module()
obj.call_functions()
