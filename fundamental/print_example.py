
class print_it(object):

    def get_input(self):
        value = input("Enter a value may be number, alphabet or anything for printing: \n")
        return value

    def get_print(self, value):
        print("The passed value is {0}".format(value))


if __name__ == '__main__':
    p = print_it()
    p.get_print("Hello World!")
    fn_input = p.get_input()
    p.get_print(fn_input)

# single line comment



"""
multi line comment
------
output 
------

The passed value is Hello World!
Enter a value may be number, alphabet or anything for printing: 
new value
The passed value is new value
"""

'''
multi line comment with single triple quotes
'''