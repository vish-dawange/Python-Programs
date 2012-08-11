import sys
print """
=========================================
Program:Calculation of sum of list items
=========================================
"""
class sum_of_list(object) :
	def __init__(self) :
		self.count=0
		self.sum_of_list=0
		self.list_items=[]
		self.average=0
	def calc_sum(self) :
		try :
			print "Enter set of numbers(Enter 0 to exit):"
			while  True:
				self.list_input = float(input())
				if self.list_input==0:break
				self.list_items.append(self.list_input)
				self.sum_of_list = self.sum_of_list + self.list_items[self.count]
				self.count=self.count+1
			self.average=self.sum_of_list/self.count
			return self.list_items,self.sum_of_list,self.count,self.average
		except Exception ,err :
			sys.stderr.write("ERROR---->%s\n" %str(err))
			return 0
			
def main():
	try :
		sum_object=sum_of_list()
		list_items,list_sum,count,avg=sum_object.calc_sum()
		print "========================================="
		print "List=",list_items
		print "Sum=", list_sum
		print "Average=" ,avg
		print "Count=", count
		print "========================================="
	except Exception ,err:
		sys.stderr.write("ERROR---->%s\n" %str(err))
main()
