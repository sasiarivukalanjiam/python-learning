
# Add two values and print the result
class doc_strings(object):

    def add_it(self, a, b):
        """
        Adds two value and returns the result
        :param a: 
        :param b: 
        :return: 
        """
        c = a+b
        return c

    def print_message(self, value):
        """
        gets a value and prints it
        :param value: 
        :return: 
        """
        print("The sum is {0}".format(value))

if __name__ == '__main__':
    d = doc_strings()
    res = d.add_it(5,6)
    d.print_message(res)



"""
outptut 

The sum is 11

Process finished with exit code 0

"""
