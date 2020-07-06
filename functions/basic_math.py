class Basic_Math():
    """
        A list of basic math methods
    """

    def __init__(self):
        super().__init__()
        # self.number = 2

    def exponentNumber(self, number):
        """
            A good practice is to create a docstring first
            and then write your code.

            This function takes a number and multiplies it by a power of 2
        """
        return number ** 2

if __name__ == '__main__':
    result = Basic_Math.exponentNumber(3,4)
    print(result)

# TODO Create Unit test for this function (In different file)!



