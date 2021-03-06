from genericpath import exists
from sys import argv


from_file = "F:/pyfile/from_file.txt"
to_file = "F:/pyfile/to_file.txt"

print("Copying from %s to %s" % (from_file, to_file))

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print("The input file is %d bytes long" % len(indata))

print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, "a")
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()

