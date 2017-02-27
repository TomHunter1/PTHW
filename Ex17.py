#This script makes a copy of an existing file

from sys import argv
from os.path import exists

#pass in arguements to allow to be run as a script
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes longs" % len(indata)

print "Does the output file exist %r?" % exists(to_file)
print "Ready, hit RETURN to contine, CTRL-C to abort"
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright I'm done"

out_file.close()
in_file.close()
