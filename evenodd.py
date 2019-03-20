# your code goes here
class node:
	def eo(self, n):
		if (n>0):
			if (n%2==0):
				print("Even")
			else:
				print("Odd")
		else:
			print(Invalid)
hel = node()
hel.eo(int(input()))
