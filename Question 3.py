Question = ["When was ALU founded?", "Who is the CEO of ALU?", "Where are ALU campuses?", "How many campuses does ALU have?", "What is the name of ALU Rwanda’s Dean?", "Who is in charge of Student Life?", "What is the name of our Lab?", "How many students do we have in Year 2 CS?", "How many degrees does ALU offer?", "Where are the headquarters of ALU?"]

answers = ["2015", "Fred Swaniker", "Rwanda and Mauritius", "2", "Insert dean’s name", "Sila Ogidi", "Insert name here", "put the number of students", "8", "Mauritius"]
right_answer = 0
wrong_answer = 0
for i in range(10):
    answer = input(Question[i])
    if answer == answers[i]:
        right_answer = right_answer+1
    else:
        wrong_answer = wrong_answer+1
        if wrong_answer == 6:
            break

if right_answer == 10:
    print("10/10, congratulations!")
else:
    print("you got " + str(wrong_answer) + " wrong answers")
    print("you got " + str(right_answer) + " right answers")





