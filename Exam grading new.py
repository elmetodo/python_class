file_location="C:/python_tutorials/exam_scores2.txt"


def open_file(file):
	file=open(file_location, "r")
	data=file.readlines()

	i=0
	for i in range (0,1):
		current_file=file_location[i]
		i=i+1
		d=open_file(current_file)

		return d

def list_sort (d):

	list=d
	print list
	names[0,9,18]
	print names