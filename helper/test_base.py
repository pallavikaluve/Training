

class TestBase():

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_numbers(self, list_of_num):
        print("----------")

        total = 0
        for ele in range(0, len(list_of_num)):
            total = total + list_of_num[ele]
        print("Sum of numbers: ", total)

    def 