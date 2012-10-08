import sys
import os
sys.path += [os.path.dirname(os.path.dirname(__file__))]
from util.Combination import CombinationMatrix


def main():
	c = CombinationMatrix(40)
	print c[40][20]


if __name__ == '__main__':
	main()
