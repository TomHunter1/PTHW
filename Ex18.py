# this one is like scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#that *args is actually pointless, we can do This
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2 %r" % (arg1,arg2)

#this just takes one arguements
def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
    print "I got nothing"

print_two("Tom", "Hunter")
print_two_again("Tom", "Hunter")
print_one("First!")
print_none()
