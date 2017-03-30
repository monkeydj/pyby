import operator

saved_string = ''


def remove_letter():  # Remove a selected letter from a string
    global saved_string
    letter = str(raw_input('A letter to remove: '))
    saved_string = saved_string.replace(letter, '')
    print "String after remove: " + saved_string
    return


def num_compare():  # Compare 2 numbers to determine the larger
    fst_num = int(raw_input('First number: '))
    snd_num = int(raw_input('Second number: '))
    if fst_num == snd_num:
        print "Two numbers are equal"
    elif fst_num > snd_num:
        print "The first number is greater then the second"
    else:
        print "The second number is greater then the first"
    return


def print_string():  # Print the previously stored string
    print "Entered string: " + saved_string
    return


def calculator():  # Basic Calculator (addition, subtraction, multiplication, division)
    signs = {'+': operator.add, '-': operator.sub,
            '*': operator.mul, '/': operator.div}
    fst_num = int(raw_input('First number: '))
    opt = str(raw_input("Operation: "))
    snd_num = int(raw_input('Second number: '))
    print "Result: %f" % signs[opt](fst_num, snd_num)
    return


def accept_and_store():  # Accept and store a string
    global saved_string
    saved_string = str(raw_input('Enter a string: '))
    return


def main():  # menu goes here
    opts = [accept_and_store,
            print_string,
            calculator,
            num_compare,
            remove_letter]
    while True:
        print "\nChoose one of the procedures:"
        print "1: Store a string"
        print "2: Print the stored string"
        print "3: Run calculator"
        print "4: Compare 2 numbers"
        print "5: Remove a letter from stored string"
        opts[int(raw_input("\nEnter: ")) - 1]()
    return

main()
