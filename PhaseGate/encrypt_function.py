def lower_case(word):
	word.lower
	
def encrypt(word):
	result = []
	position = 0
	lower_case(word)
	alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for ch in word:
		for index, each in enumerate(alphabets):
			if ch == each:
				position = index + 1
				encrypt = (position + 13) % 26			
				alphabets[(encrypt-1)], end='')						result.append()
	return f''
			
print(encrypt("hello"))		
	
	

