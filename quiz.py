	
def has_teen(a,b,c):
	if a <= 19 and a >=13 or b <= 19 and b >=13 or c <= 19 and c >=13:
		return True
	else:
		return False

print has_teen(19, 1, 3) # expect True
print has_teen(5, 15, 4) # expect True
print has_teen(9, 5, 18) # expect False
print has_teen(58, 60, 85) # expect False

def not_string(note):
	if note.startswith ("not"):
		return note + ("not")
	else: 
		return ("not") + note

print not_string("friendly") # expect not friendly
print not_string("not a good ") # expect not a good not

def icy_hot(temp, temp2):
	if (temp < 0 and temp2 > 100) or (temp > 100 and temp2 < 0) :
		return True
	else:
		return False

print icy_hot(-1, 125) # expect True
print icy_hot(52, 48) # expect False
print icy_hot(-4, 101) # expect True
print icy_hot(-5, 24) # expect False

def closer_to(a,b,n):
	if abs(a - b) < abs(a - n):
		return b
	if abs(a - b) > abs(a - n):
		return n
	if abs(a - b) == abs(a - n):
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

def pig_latinify(word):
	if word.startswith ("a"):
		return word + ("way")
	if word .startswith ("e"):
		return word + ("way")
	if word .startswith ("i"):
		return word + ("way")
	if word .startswith ("o"):
		return word + ("way")
	if word .startswith ("u"):
		return word + ("way")


print pig_latinify("apple") # expect appleway
print pig_latinify("unicorn") # expect unicornway
print pig_latinify("iguana") # expect iguanaway
print pig_latinify("octupus") # expect octupusway
print pig_latinify("eagle") # expect eagleway

