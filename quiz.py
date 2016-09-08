	
def has_teen(teen):
	if teen <= 19 and teen >=13:
		return True
	else:
		return False

print has_teen(13) # expect True
print has_teen(14) # expect True
print has_teen(5) # expect False
print has_teen(58) # expect False


def icy_hot(icy, hot):
	if icy < 0 and hot > 100:
		return True
	else:
		return False

print icy_hot(-1, 125) # expect True
print icy_hot(52, 48) # expect False
print icy_hot(52, 524) # expect False
print icy_hot(-5, 24) # expect False

def closer_to(a,b,n):
	if a < n and b > n:
		return "a"
	if b < n and a > n:
		return "b"
	if a < n or b > n:
		return 0

print closer_to(3, 5, 6) # expect b
print closer_to(5, 3, 6) # expect a
print closer_to(5, 5, 6) # expect 0

def two_as_one(a,b,c):
	if a + b == c or b + c == a or a + c == b:
		return True
	else: 
		return False

print two_as_one(1, 2, 3) # expect True
print two_as_one(5, 2, 3) # expect True
print two_as_one(1, 4, 3) # expect True
print two_as_one(1, 7, 3) # expect False

# TODO - write pig_latinify
