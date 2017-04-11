import socket

'''1.1) Take two arguments, a list and an integer. The list is a series 
of strings; one of those strings will be the filename, the others will 
be the file contents. The integer is the location in the list of the file 
name. (Write each string to a separate line)

list:
a 0 <-contents
b 1 <-contents
c 2 <-contents
d 3 <-contents
e 4 <- filename
f 5 <-contents

item:
4

'''


def journeyman1(str_list, item):
    with open(str(str_list[item]), 'w') as jnf:
        for i in range(len(str_list)):
            if i != item:
                jnf.write(str_list[i])
    return


'''1.2) Write a function which takes a single integer as an argument and 
returns the sum of every integer up to and including that number, use a 
generator.'''


def sum_generator(final_num):
    current = 0
    while current <= final_num:
        yield current
        current += 1
    return  # (Make this a yield)


def journeyman2(final_num):
    # return sum(range(final_num+1))
    return sum(sum_generator(final_num))


'''1.3) Write a python script which connects to the included server 
on port 50001 and returns the message it receives.'''


def journeyman3():
    recv_string = ''
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 50001))
        recv_string = s.recv(1024)
        s.close()
    except Exception as e: pass
    finally:
        return recv_string


'''1.4) Create a class called person, with height, weight, hair color, 
and eye color fields, then implement it to describe yourself.'''


def journeyman4():
    class Person:

        def __init__(self, height=0, weight=0, hair='', eye=''):
            self.height = height
            self.weight = weight
            self.hair = hair
            self.eye = eye

        def describe(self):
            print 'Height:\t\t%d' % self.height
            print 'Weight:\t\t%d' % self.weight
            print 'Hair color:\t%s' % self.hair
            print 'Eye color:\t%s' % self.eye

    Jio = Person(165, 80, 'black', 'dark brown')
    Jio.describe()

    return
