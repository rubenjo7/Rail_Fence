from railFence import decryptRailFence

def railBreak(encrypted):
	cipherLen = len(encrypted)
	for i in range(2, cipherLen+1):
		bestGuess = decryptRailFence(encrypted,i,0)
		print(bestGuess)
	return bestGuess
	

