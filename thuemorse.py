def bitwise_negation(num):
    negation = ""
    for digit in num:
        if digit == "0":
            negation = negation + "1"
        elif digit == "1":
            negation = negation + "0"
        else:
            print "Error in the negation loop"
    return negation


def thue(n):
    if n == 0:
        return "0"
    else:
        return (thue(n-1) + flip_bin(thue(n-1)))

def flip_bin(num):
	mask = "1" * len(str(num))
	flipped = bin(int(num,2) ^ int(mask, 2))[2:]
	return flipped	


for num in range(0,6):
    print thue(num)
  
