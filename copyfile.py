#Program to copying the contents of one file to another file
from sys import argv
from os.path import exists
print """
======================================================
Program:Copying contents of one file to another file
======================================================
"""

def file_operations() :
	try :
		#Command line arguements
		script_name, source_file,destination_file =argv
		#Printing the source file and destination file
		print "Copying from %s to %s "% (source_file ,destination_file)

		#Open the source file 
		input=open(source_file,'r')

		#Read the contnents of file to data
		data=input.read() 
		#Size of file contents
		print "Size of file is %d bytes long" % len(data)

		#Checking for existance of file
		print "Does the output file exist? %r"% exists(destination_file)
		raw_input() 

		#Opening the destination file in write mode
		output=open(destination_file,'w')
		output.write(data)

		print "Done"
		#Done with task

		#Close
		output.close()
		input.close()
	except Exception ,err :
		sys.stderr.write("ERROR---->%s\n"%str(err))
		

file_operations()
