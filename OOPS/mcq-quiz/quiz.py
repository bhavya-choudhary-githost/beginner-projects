from mcq_classes import Question

questions_prompt = [
    "What color is the sky?\n (a) Ay mi amor, ay mi amor\n (b) Red\n (c)Blue\n (d)idk man",
    "You tell me that it's red\n (a) Ay mi amor, ay mi amor\n (b) what\n (c)I didn't say none of that\n (d)idk woman",
    "Where should I put my shoe?\n (a) Ay mi amor, ay mi amor\n (b) in the shoe rack?\n (c)wherever you want\n (d)idc",
    "You say put them on your head! ay mi amor, ay mi amor🎶🥁🎶...\nYou make me un poco loco\n (a) whats that\n (b) poco loco\n\
 (c)thats ok\n (d)Un poquititio loco"
]

questions = [
    Question(questions_prompt[0],'a'),
    Question(questions_prompt[1],'a'),
    Question(questions_prompt[2],'a'),
    Question(questions_prompt[3],'d')
]

def run_test(questions):
    score = 0
    for question in questions:
        user_ans = input(question.prompt + "\n")
        if user_ans.lower() == question.answer:
            score += 1
    print("You scored" + str(score) + "/" + str(len(questions)) + "!")

run_test(questions)
