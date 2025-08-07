score = 0
print("Quiz App".center(120,'_'))
print("Answer in A/B/C/D. This Quiz consists of 5 questions. Best of Luck!!!".center(120,'_'))

# Question 5 called by Q4 function
def Q5(score):
  answer = input("Which celestial body has the strongest gravitational pull? \nA) Sun \nB) Earth \nC) Moon \nD) Black Hole ? : ").upper()
  if answer == 'D':
    print("Correct")
    score += 1
  else:
    print("No, the correct option is \'D\'.")

  print(f"Your score is : {score}/5")
  return score



# Question 4 called by Q3 function
def Q4(score):
  answer = input("Which planet is known as the Red Planet? \nA) Earth  \nB) Mars  \nC) Jupiter \nD) Venus ? : ").upper()
  if answer == 'B':
    print("Correct")
    score += 1
  else:
    print("No, the correct option is \'B\'.")
  return Q5(score)



# Question 3 called by Q2 function
def Q3(score):
  answer = input("What is the full form of RAM? \nA) Random Access Memory \nB) Read Access Memory  \nC) Run Access Memory \nD) Random Allocate Memory ? : ").upper()
  if answer == 'A':
    print("Correct")
    score += 1
  else:
    print("No, the correct option is \'A\'.")
  return Q4(score)


# Question 2 called by Q1 function
def Q2(score):
  answer = input("Which of the following is a programming language? \nA) HTML \nB) Windows \nC) Python \nD) Google ? : ").upper()
  if answer == 'C':
    print("Correct")
    score += 1
  else:
    print("No, the correct option is \'C\'.")
  return Q3(score)


# Question 1 called by once
def Q1(score):
  answer = input("What does CPU stand for? \nA) Central Process Unit  \nB) Central Processing Unit \nC)Computer Personal Unit \nD) Control Processing Unit ? : ").upper()
  if answer == 'B':
    print("Correct")
    score += 1
  else:
    print("No, the correct option is \'B\'.")
  return Q2(score)

# First function call
final_score = Q1(score)

# Wanna play again section
query = input("Wanna play again? (Y/N): ").upper()
if query == 'Y':
  score = 0 
  final_score = Q1(score)
