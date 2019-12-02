from math import log, copysign

def round_coord(x: float) -> float:
	return copysign(int(abs(x)) + pow(0.5, int(log(abs(x) - int(abs(x))) / log(0.5))), x)

if __name__ == '__main__':
	print('Input coord to prettify: ', end='')
	print('Pretty coord =', round_coord(float(input())))