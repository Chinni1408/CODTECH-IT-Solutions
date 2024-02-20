import random
quiz_data={
    "General Knowledge":[ {"question" : "Which of the given cities is located on the bank of river Ganga?",
                                          "options"  : ["Patna","Gwalior","Bhopal","Mathura"],
                                          "answer"  :  "Patna"},
                                        {"question" : "Which planet is known as the Red Planet?",
                                         "options" :  ['Mars', 'Venus', 'Jupiter', 'Saturn'],
                                         "answer" :  "Mars"} ],
    "Aptitude":[ {"question" : "Were you a bird, you _________ in the sky.",
                        "options"  :   ["would fly" ,"shall fly" ,"should fly" ,"shall have flown"],
                         "answer" :    "would fly"},
                      {"question" : "SCD, TEF, UGH, ____, WKL",
                        "options"  :  ["CMN","UJI","VIJ","IJT"],
                        "answer"  :  "VIJ"} ],
    "Mathematics":[ {"question" : "what is the sqrt of 729",
                               "options"  :  ["27","29","23","33"],"answer":"27"},
                            {"question"  :  "What is the average of first 150 natural numbers?",
                             "options"  :  [" 70",'70.5','75',"75.5"],"answer":"75.5"},
                            {"question"  :  "What is 1004 divided by 2?",
                             "options"  :  ["52","502","520","5002"],
                             "answer"  :  "502" } ]
               }
def run_quiz():
    score=0
    #shuffle the categories to occur randomly
    categories=list(quiz_data.keys())
    random.shuffle(categories)

    for category in categories:
        print(category+"  Quiz")
        print('-'*30)
        questions=quiz_data[category]
        random.shuffle(questions)  # in category (list) => 3 questions in dict form
        for question_data in questions:
            question=question_data["question"]
            options=question_data["options"]
            answer=question_data["answer"]
            print(question)
            #shuffle the options
            random.shuffle(options)
            count=1
            for option in options:
                print(f"{count}.{option}")
                count=count+1
            #get the input from the user
            input_data=int(input("Enter the option number (1-4) : "))
            # validating the input_data
            if input_data==options.index(answer)+1:
                print("Correct answer!\n")
                score=score+1
            else:
                print("Wrong answer! The correct one is :"+answer)
            #view the score
    print(f"Quiz completed! Your final score is :{score}/7\n")
run_quiz()    
