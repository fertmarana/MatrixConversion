import csv
import sys
import time
from circledraw import MidPointCirc,SphereCoordCirc, ImplEqCirc

def main():
	r = 5

	sum = 0
	for ntests in range(0,1000):
		start_t = time.time()
		n_pixels = MidPointCirc(r,200,200,(255,255,255))
		end_t = time.time()
		sum = sum + (end_t - start_t)

	print("MP: mean time = %.10lf" %float(sum/100))

	sum = 0
	for ntests in range(0,1000):
		start_t = time.time()
		n_pixels = SphereCoordCirc(r,200,200,(255,255,255))
		end_t = time.time()
		sum = sum + (end_t - start_t)

	print("SP: mean time = %.10lf" %float(sum/100))

	sum = 0
	for ntests in range(0,1000):
		start_t = time.time()
		n_pixels = ImplEqCirc(r,200,200,(255,255,255))
		end_t = time.time()
		sum = sum + (end_t - start_t)

	print("IE: mean time = %.10lf" %float(sum/100))
# Cya !!
if __name__ == '__main__':
    main()