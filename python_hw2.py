def gradecalc(score):
	if score >= 90 and score <= 100:
		return("Your Grade for the score of", score, " is A")
	elif score >= 80 and score < 90:
		return("Your Grade for the score of", score, " is B")
	elif score >= 70 and score < 80:
		return("Your Grade for the score of", score, " is C")
	elif score >= 60 and score < 70:
		return("Your Grade for the score of", score, " is D")
	elif score < 60 and score >= 0:
		return("Your Grade for the score of", score, " is F")
	else:
		return("Error please enter a score within 0 to 100")
	
		
		
score = 0
while True:
	marks = input("Enter your score or enter done to complete:")
	if marks == 'done':
		print("Thank you for using the program")
		break
	else:	
		grade = gradecalc(int(marks))
		print(grade)