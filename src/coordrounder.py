from math import log, copysign

def round_coord(x: float) -> float:
	return copysign(pow(0.5, int(log(abs(x)) / log(0.5))), x)
