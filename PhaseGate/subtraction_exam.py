import random
correct_count = 0;
new_question_count = 0;
wrong_count = 0;
temp = 0;
while True:
	
	minuend = random.randint(0, 100)
	subtrahend = random.randint(0, 101)

	if  subtrahend > minuend:
		temp = subtrahend
		subtrahend = minuend
		minuend = temp

	new_question_count += 1;
	result = minuend - subtrahend;
	print(minuend, " - ", subtrahend, " :" );
	answer = int(input("Enter an answer: "));
	if answer == result:
		correct_count += 1		
			
	else:	
		answer = int(input("Enter an answer: "));
		if answer == result:
			correct_count += 1		
		else:
			wrong_count += 1;		
	
	if new_question_count == 10:
		break;
	

print("Your total score was ",correct_count)
print("You failed" , wrong_count)
