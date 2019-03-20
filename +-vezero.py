# your code goes here
class node:
	def pnz(self, n):
		if (n>0):
			print("Positive")
		elif (n<0):
			print("Negative")
		else:
			print("Zero")
hel = node()
hel.pnz(int(input()))
