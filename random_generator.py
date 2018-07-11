import random

#randoms.txt will contain 1000 arrays of size 100
with open("randoms.txt","w+") as random_arrays:
	for i in range(0,1000):
		for j in range(0,400):
			random_arrays.write("%d,"%random.randint(0,1000))
		random_arrays.write("\n")