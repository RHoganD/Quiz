# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

q1 = """What's the biggest animal in the world?

a.Elephant

b.Giraffe

c.The blue whale

d.Mouse"""

q2 = """What is the largest country in the world?

a.Russia

b.The UK

c.Germany

d.Africa"""

q3 = """What is the most sold flavour of Walker's crisps?

a.Cheese

b.Cheese and Onion

c.Sea salt

d.None"""

q4 = """What is the capital of spain?

a.Berlin

b.London

c.Paris

d.Madrid"""

q5 = """What does IPA stand for?

a.Inter pool Action

b.Indian Pale Ale

c.Investment Policy Ammedments

d.Intercom Policy American

"""

#creating the diccionaries

 

questions ={q1:"c", q2:"a", q3:"b", q4:"d", q5:"b"}

 

name = input("Enter your name: ")

print("Hello", name, "Welcome to the quiz")

playing = input("Do you want to play the quiz? ")

if playing != "yes":
   
   print("Sorry you are leaving, lets play another time")
   quit()
   
print("Okay! Let's Play! :) \n")

score = 0

for i in questions:

    print()
# if i want the program to ask about quiting the quiz place code hre


    print(i)

    flag1 = input("Do you want to skip this question (yes /no):")

    if flag1=="yes":

       continue

    ans = input("Enter the answer (a/b/c/d):")
if ans==questions[i]:

      print("Correct answer, you got 1 point")

      score = score+1

      print("Current score is: ", score)

else:

      print("Wrong answer, you lost 1 point")

      score = score-1

      print("Current score is: ", score)

 

flag2 = input("Do you want to quit the quiz (yes/no):")
if flag2 == "yes":
     # break
    quit()
print("Final score is:", score)

print("Thanks for playing")