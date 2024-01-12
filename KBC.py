import random

questions=[
    {
        "question":"what is the capital of France?",
        "options":["Paris","Berlin","London","Rome"],
        "Correct_answer":0
    },
    {
        "question":"Who is the longest serving ruler of Indonesia?",
        "options":["General Suharto", "Joko Widodo", "Sukamo", "None of These"],
        "Correct_answer":0
    },
    {
        "question":"The height of Manaslu mountain is ",
        "options":["8163m/26,781ft","8516m/27,940ft","8463m/27,766ft","8167m/26,795ft"],
        "Correct_answer":0
    },
    {
        "question":"The height of Dhaulagiri mountain is ",
        "options":["8586m/28,169ft","8516m/27,940ft","8463m/27,766ft","8167m/26,795ft"],
        "Correct_answer":3
    },
    {
        "question":"Who inaugurated the State Bank of Pakistan?",
        "options":[" Liaquat Ali Khan","Malik Ghulam Muhammad","Quaid-e-Azam","Allama Muhammad Iqbal"],
        "Correct_answer":2
    },
    {
        "question":"Sardar Abdur Rub Nishtar was the Governor of?",
        "options":["Gilgit Baltistan","Sindh","Punjab","B. KPK"],
        "Correct_answer":2
    },
    {
        "question":"National code of Pakistan is?",
        "options":["PAK 1","PK","None of them","PAK"],
        "Correct_answer":1
    },
    {
        
        "question":"Where is Warsak Dam of Pakistan situated?",
        "options":["Khyber Pakhtunkhwa","Punjab","Sindh","Balochistan"],
        "Correct_answer":0
    },
    {
        "question":"Shakarparrian is situated in?",
        "options":["Peshawar","Murree","Rawalpindi","Islamabad"],
        "Correct_answer":3
    }
    
    ]

def ask_questions(question_obj):
    print(question_obj["question"])
    for i, option in enumerate(question_obj["options"]):
        print(f"{i+1}. {option}")
    user_answer=int(input("Your answer (Enter the option Nummber):  "))
    return user_answer-1

def main():
    score=0
    random.shuffle(questions)

    for q in questions:
        user_choice=ask_questions(q)
        if user_choice==q["Correct_answer"]:
            print("Correct!\n")
            score+=1
        else:
            print(f"wrong! Ther correct answer was: {q['options'][q['Correct_answer']]}\n")
    print(f"Quiz Completed! Your Score is: {score}/{len(questions)}")
if __name__=="__main__":
    main()