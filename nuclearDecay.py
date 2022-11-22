import math
import random
from random import randrange

class atom(object):
	def __init__(self):
		self.lamda = float(input("Enter your decay constant: "))
		self.t = float(input("Enter your time constant: "))
		self.N = int(input("Enter your number of n*n atoms you want: "))
		self.probability = (self.lamda)*(self.t)
		self.matrix = [[1 for x in range(0, self.N)] for y in range(0, self.N)]
		self.initialnum = (self.N)*(self.N)
		self.halflive = ((math.log(2))/self.lamda)
	
					
		

	def decaycompletion(self):
		self.decayednumb = 0
		self.n = self.t
		while (self.decayednumb) < (((self.N)*(self.N))/2):
			self.n += self.t
			for y in range(self.N):
				for x in range(self.N):
					if (self.matrix[y][x] == 1):
						if random.randrange(0,100000000,1) <= ((self.probability)*100000000):
							self.decayednumb += 1
							self.matrix[y][x] = 0
		print(self.matrix)
		print("More than half of your atoms have decayed")
		self.halflifeSim = (self.n)
		self.finalnum =  (self.N)*(self.N) - (self.decayednumb)

	

test = atom()
test.decaycompletion()
print("The initial number of undecayed nuclei was: " + str(test.initialnum))
print("The final number of undecayed nuclei is: " + str(test.finalnum))
print("The simulated value of the halflife is: " + str(test.halflifeSim))
print("The actual halflife is: " + str(test.halflive))



 
