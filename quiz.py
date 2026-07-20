import random
import time


quiz_data = {

   "python": {

"easy": [

{
"question": "Which keyword is used to create a function in Python?",
"options": ["a) function", "b) def", "c) define"],
"answer": "b"
},

{
"question": "Which function is used to display output in Python?",
"options": ["a) print()", "b) display()", "c) output()"],
"answer": "a"
},

{
"question": "Which symbol is used for comments in Python?",
"options": ["a) //", "b) #", "c) /* */"],
"answer": "b"
},

{
"question": "Which data type stores text?",
"options": ["a) int", "b) str", "c) float"],
"answer": "b"
},

{
"question": "Which function takes input from user?",
"options": ["a) input()", "b) scan()", "c) get()"],
"answer": "a"
},

{
"question": "Python is a ______ language.",
"options": ["a) Programming", "b) Markup", "c) Database"],
"answer": "a"
},

{
"question": "Which data type stores whole numbers?",
"options": ["a) int", "b) bool", "c) list"],
"answer": "a"
},

{
"question": "Which operator is used for addition?",
"options": ["a) +", "b) -", "c) *"],
"answer": "a"
},

{
"question": "Which keyword is used for conditions?",
"options": ["a) if", "b) check", "c) condition"],
"answer": "a"
},

{
"question": "Which loop repeats over items?",
"options": ["a) for", "b) repeat", "c) loop"],
"answer": "a"
},

{
"question": "Which brackets create a list?",
"options": ["a) ()", "b) []", "c) {}"],
"answer": "b"
},

{
"question": "Which keyword stops a loop?",
"options": ["a) stop", "b) break", "c) exit"],
"answer": "b"
},

{
"question": "Which keyword skips an iteration?",
"options": ["a) continue", "b) skip", "c) pass"],
"answer": "a"
},

{
"question": "Which value represents nothing?",
"options": ["a) Null", "b) None", "c) Empty"],
"answer": "b"
},

{
"question": "Which function finds length?",
"options": ["a) len()", "b) size()", "c) count()"],
"answer": "a"
},

{
"question": "Python file extension is?",
"options": ["a) .java", "b) .py", "c) .html"],
"answer": "b"
},

{
"question": "Which keyword imports modules?",
"options": ["a) include", "b) import", "c) module"],
"answer": "b"
},

{
"question": "True and False belong to?",
"options": ["a) bool", "b) int", "c) float"],
"answer": "a"
},

{
"question": "Which method adds item to list?",
"options": ["a) add()", "b) append()", "c) push()"],
"answer": "b"
},

{
"question": "Python was created by?",
"options": ["a) Guido van Rossum", "b) Bill Gates", "c) Dennis Ritchie"],
"answer": "a"
},

{
"question": "Multiplication operator is?",
"options": ["a) x", "b) *", "c) %"],
"answer": "b"
},

{
"question": "Integer conversion function?",
"options": ["a) int()", "b) str()", "c) float()"],
"answer": "a"
},

{
"question": "String conversion function?",
"options": ["a) text()", "b) str()", "c) string()"],
"answer": "b"
},

{
"question": "Python supports OOP?",
"options": ["a) Yes", "b) No", "c) Only C"],
"answer": "a"
},

{
"question": "Which keyword creates a loop?",
"options": ["a) for", "b) create", "c) repeat"],
"answer": "a"
}

],


"hard": [

{
"question": "Which keyword defines a class?",
"options": ["a) class", "b) object", "c) define"],
"answer": "a"
},

{
"question": "Which operator checks equality?",
"options": ["a) =", "b) ==", "c) !="],
"answer": "b"
},

{
"question": "Which concept allows code reuse?",
"options": ["a) Inheritance", "b) Printing", "c) Input"],
"answer": "a"
},

{
"question": "Which method initializes object?",
"options": ["a) __init__", "b) start()", "c) init()"],
"answer": "a"
},

{
"question": "Which keyword handles exceptions?",
"options": ["a) try", "b) error", "c) catch"],
"answer": "a"
},

{
"question": "Which block executes always?",
"options": ["a) finally", "b) except", "c) try"],
"answer": "a"
},

{
"question": "Lambda functions are?",
"options": ["a) Anonymous functions", "b) Classes", "c) Loops"],
"answer": "a"
},

{
"question": "Which library is used for data analysis?",
"options": ["a) pandas", "b) turtle", "c) random"],
"answer": "a"
},

{
"question": "Which keyword creates generator?",
"options": ["a) yield", "b) return", "c) generate"],
"answer": "a"
},

{
    "question": "Decorator in Python starts with?",
    "options": ["a) @", "b) #", "c) &"],
    "answer": "a"
},
 {
"question": "Which keyword is used to create an anonymous function?",
"options": ["a) lambda", "b) def", "c) function"],
"answer": "a"
},

{
"question": "Which data structure stores key-value pairs?",
"options": ["a) List", "b) Dictionary", "c) Tuple"],
"answer": "b"
},

{
"question": "Which method removes an item from a list?",
"options": ["a) remove()", "b) delete()", "c) erase()"],
"answer": "a"
},

{
"question": "Which keyword is used to create a generator?",
"options": ["a) yield", "b) generate", "c) return"],
"answer": "a"
},

{
"question": "Which module is used for mathematical functions?",
"options": ["a) math", "b) random", "c) os"],
"answer": "a"
},

{
"question": "Which method is used to open a file?",
"options": ["a) open()", "b) file()", "c) read()"],
"answer": "a"
},

{
"question": "Which keyword is used to handle exceptions?",
"options": ["a) try", "b) error", "c) exception"],
"answer": "a"
},

{
"question": "Which concept hides internal details of a class?",
"options": ["a) Encapsulation", "b) Looping", "c) Printing"],
"answer": "a"
},

{
"question": "Which Python collection is immutable?",
"options": ["a) List", "b) Tuple", "c) Dictionary"],
"answer": "b"
},

{
"question": "Which function converts string into integer?",
"options": ["a) int()", "b) str()", "c) float()"],
"answer": "a"
},

{
"question": "Which operator is used for exponentiation?",
"options": ["a) **", "b) //", "c) %%"],
"answer": "a"
},

{
"question": "Which keyword creates a module?",
"options": ["a) import", "b) module", "c) create"],
"answer": "a"
},

{
"question": "Which method returns dictionary keys?",
"options": ["a) keys()", "b) values()", "c) items()"],
"answer": "a"
},

{
"question": "Which Python library is used for machine learning?",
"options": ["a) scikit-learn", "b) turtle", "c) pygame"],
"answer": "a"
},

{
"question": "Which concept allows multiple forms of an object?",
"options": ["a) Polymorphism", "b) Inheritance", "c) Compilation"],
"answer": "a"
},

        ]

    },


    "ai": {

        "easy": [

{
"question": "What is the full form of AI?",
"options": ["a) Artificial Intelligence", "b) Automated Internet", "c) Advanced Input"],
"answer": "a"
},

{
"question": "AI enables machines to?",
"options": ["a) Think and learn", "b) Only calculate", "c) Only store data"],
"answer": "a"
},

{
"question": "Machine Learning is a part of?",
"options": ["a) Artificial Intelligence", "b) Networking", "c) Hardware"],
"answer": "a"
},

{
"question": "Which language is commonly used for AI development?",
"options": ["a) Python", "b) HTML", "c) CSS"],
"answer": "a"
},

{
"question": "AI systems learn from?",
"options": ["a) Data", "b) Keyboard", "c) Monitor"],
"answer": "a"
},

{
"question": "A chatbot is an example of?",
"options": ["a) AI application", "b) Hardware device", "c) Operating system"],
"answer": "a"
},

{
"question": "Which field allows computers to understand human language?",
"options": ["a) NLP", "b) Networking", "c) Database"],
"answer": "a"
},

{
"question": "Computer vision helps machines to?",
"options": ["a) Understand images", "b) Increase storage", "c) Create hardware"],
"answer": "a"
},

{
"question": "AI stands for?",
"options": ["a) Artificial Intelligence", "b) Automatic Information", "c) Advanced Internet"],
"answer": "a"
},

{
"question": "Data is important in AI because?",
"options": ["a) Models learn from data", "b) It replaces CPU", "c) It creates hardware"],
"answer": "a"
},

{
"question": "Robot technology combined with AI is called?",
"options": ["a) Intelligent Robotics", "b) Networking", "c) Web Design"],
"answer": "a"
},

{
"question": "Deep Learning is based on?",
"options": ["a) Neural Networks", "b) Databases", "c) Browsers"],
"answer": "a"
},

{
"question": "AI models improve through?",
"options": ["a) Training", "b) Printing", "c) Formatting"],
"answer": "a"
},

{
"question": "Which is an example of AI?",
"options": ["a) Voice Assistant", "b) Keyboard", "c) Mouse"],
"answer": "a"
},

{
"question": "Google Assistant uses?",
"options": ["a) AI", "b) Printer", "c) Compiler"],
"answer": "a"
},

{
"question": "Machine Learning allows computers to?",
"options": ["a) Learn from experience", "b) Only store files", "c) Increase screen size"],
"answer": "a"
},

{
"question": "AI is used in healthcare for?",
"options": ["a) Disease prediction", "b) Making keyboards", "c) Charging batteries"],
"answer": "a"
},

{
"question": "A model in AI is trained using?",
"options": ["a) Data", "b) Wires", "c) Screens"],
"answer": "a"
},

{
"question": "NLP stands for?",
"options": ["a) Natural Language Processing", "b) Network Language Program", "c) New Learning Process"],
"answer": "a"
},

{
"question": "AI can help in?",
"options": ["a) Decision making", "b) Only typing", "c) Printing"],
"answer": "a"
},

{
"question": "Which is a supervised learning example?",
"options": ["a) Classification", "b) Formatting", "c) Searching"],
"answer": "a"
},

{
"question": "AI requires algorithms and?",
"options": ["a) Data", "b) Paint", "c) Hardware only"],
"answer": "a"
},

{
"question": "Neural networks are inspired by?",
"options": ["a) Human brain", "b) Keyboard", "c) Internet cable"],
"answer": "a"
},

{
"question": "AI applications include?",
"options": ["a) Recommendation systems", "b) Calculator only", "c) Text editor"],
"answer": "a"
},

{
"question": "Self-driving cars use?",
"options": ["a) AI and sensors", "b) Only keyboard", "c) Printer"],
"answer": "a"
}

],


"hard": [

{
"question": "Machine Learning algorithms identify patterns from?",
"options": ["a) Data", "b) Hardware", "c) Networks"],
"answer": "a"
},

{
"question": "Deep Learning uses layers of?",
"options": ["a) Neural Networks", "b) Databases", "c) Browsers"],
"answer": "a"
},

{
"question": "CNN is mainly used for?",
"options": ["a) Image processing", "b) Text writing", "c) Networking"],
"answer": "a"
},

{
"question": "RNN is useful for?",
"options": ["a) Sequential data", "b) Hardware design", "c) Storage"],
"answer": "a"
},

{
"question": "Overfitting means?",
"options": ["a) Model memorizes training data", "b) Model deletes data", "c) Model stops learning"],
"answer": "a"
},

{
"question": "Training data is used to?",
"options": ["a) Train the model", "b) Delete model", "c) Format computer"],
"answer": "a"
},

{
"question": "Testing data is used to?",
"options": ["a) Evaluate model performance", "b) Train model only", "c) Store files"],
"answer": "a"
},

{
"question": "Accuracy measures?",
"options": ["a) Correct predictions", "b) Data size", "c) Speed"],
"answer": "a"
},

{
"question": "AI bias occurs because of?",
"options": ["a) Biased data", "b) Fast internet", "c) Large storage"],
"answer": "a"
},

{
"question": "Reinforcement learning uses?",
"options": ["a) Rewards and penalties", "b) Only labels", "c) Images only"],
"answer": "a"
},

{
"question": "Computer vision focuses on?",
"options": ["a) Visual information", "b) Audio only", "c) Hardware"],
"answer": "a"
},

{
"question": "Generative AI can create?",
"options": ["a) Text and images", "b) Only folders", "c) Hardware"],
"answer": "a"
},

{
"question": "Large Language Models work with?",
"options": ["a) Text data", "b) Keyboard", "c) Printers"],
"answer": "a"
},

{
"question": "Feature selection improves?",
"options": ["a) Model performance", "b) Screen quality", "c) Internet speed"],
"answer": "a"
},

{
"question": "Classification predicts?",
"options": ["a) Categories", "b) Random files", "c) Hardware"],
"answer": "a"
},

{
"question": "Regression predicts?",
"options": ["a) Continuous values", "b) Images only", "c) Passwords"],
"answer": "a"
},

{
"question": "AI model evaluation uses?",
"options": ["a) Metrics", "b) Keyboard", "c) Browser"],
"answer": "a"
},

{
"question": "Transfer learning means?",
"options": ["a) Using knowledge from existing model", "b) Deleting data", "c) Changing hardware"],
"answer": "a"
},

{
"question": "Natural Language Processing handles?",
"options": ["a) Human language", "b) Electricity", "c) Storage"],
"answer": "a"
},

{
"question": "Epoch in deep learning means?",
"options": ["a) One complete training cycle", "b) Error message", "c) Data type"],
"answer": "a"
},

{
"question": "Optimizer is used for?",
"options": ["a) Updating model weights", "b) Creating files", "c) Saving images"],
"answer": "a"
},

{
"question": "Loss function measures?",
"options": ["a) Model error", "b) Internet speed", "c) File size"],
"answer": "a"
},

{
"question": "Artificial Neural Network contains?",
"options": ["a) Layers and neurons", "b) Browsers", "c) Printers"],
"answer": "a"
},

{
"question": "Model deployment means?",
"options": ["a) Making model available for use", "b) Deleting model", "c) Training only"],
"answer": "a"
},

{
"question": "AI ethics focuses on?",
"options": ["a) Responsible AI use", "b) Faster typing", "c) Hardware repair"],
"answer": "a"
}

]
    },
   
    "cyber": {

    "easy": [

        {
            "question": "What protects a computer network from unauthorized access?",
            "options": ["a) Firewall", "b) Browser", "c) Printer"],
            "answer": "a"
        },

        {
            "question": "What is a strong password made of?",
            "options": ["a) Only name", "b) Letters, numbers and symbols", "c) Only numbers"],
            "answer": "b"
        },

        {
            "question": "What does VPN stand for?",
            "options": ["a) Virtual Private Network", "b) Visual Program Network", "c) Virtual Public Node"],
            "answer": "a"
        },

        {
            "question": "Which is a type of cyber attack?",
            "options": ["a) Phishing", "b) Printing", "c) Formatting"],
            "answer": "a"
        },

        {
            "question": "Antivirus software protects against?",
            "options": ["a) Malware", "b) Keyboard", "c) Internet speed"],
            "answer": "a"
        },
        {
"question": "What is phishing?",
"options": ["a) Fake attempt to steal information", "b) Computer game", "c) Software update"],
"answer": "a"
},

{
"question": "What is a virus?",
"options": ["a) Malicious program", "b) Hardware device", "c) Browser"],
"answer": "a"
},

{
"question": "What does SSL provide?",
"options": ["a) Secure communication", "b) More storage", "c) Faster CPU"],
"answer": "a"
},

{
"question": "A firewall is used for?",
"options": ["a) Network protection", "b) Printing", "c) Gaming"],
"answer": "a"
},

{
"question": "What is a hacker?",
"options": ["a) Person who accesses systems", "b) Printer", "c) Browser"],
"answer": "a"
},

{
"question": "What is two-factor authentication?",
"options": ["a) Extra security verification", "b) Faster internet", "c) More memory"],
"answer": "a"
},

{
"question": "What is spyware?",
"options": ["a) Software that secretly collects information", "b) Antivirus", "c) Firewall"],
"answer": "a"
},

{
"question": "What is a secure password?",
"options": ["a) Strong and unique password", "b) Your name", "c) 12345"],
"answer": "a"
},

{
"question": "What does malware mean?",
"options": ["a) Malicious software", "b) Machine learning", "c) Hardware"],
"answer": "a"
},

{
"question": "VPN helps to?",
"options": ["a) Protect online privacy", "b) Increase screen size", "c) Print documents"],
"answer": "a"
},

{
"question": "What is a cyber crime?",
"options": ["a) Crime using computers", "b) Playing games", "c) Watching videos"],
"answer": "a"
},

{
"question": "Antivirus software detects?",
"options": ["a) Threats", "b) Photos", "c) Keyboard"],
"answer": "a"
},

{
"question": "What is a data breach?",
"options": ["a) Unauthorized data access", "b) Data backup", "c) File saving"],
"answer": "a"
},

{
"question": "What is encryption?",
"options": ["a) Converting data into secure form", "b) Deleting data", "c) Printing data"],
"answer": "a"
},

{
"question": "What is a firewall rule?",
"options": ["a) Controls network traffic", "b) Creates games", "c) Stores files"],
"answer": "a"
},

{
"question": "What is social engineering?",
"options": ["a) Manipulating people to get information", "b) Coding language", "c) Hardware repair"],
"answer": "a"
},

{
"question": "What is a Trojan horse?",
"options": ["a) Malware disguised as useful software", "b) Antivirus", "c) Firewall"],
"answer": "a"
},

{
"question": "What is authentication?",
"options": ["a) Verifying identity", "b) Deleting files", "c) Installing games"],
"answer": "a"
},

{
"question": "What is a security update?",
"options": ["a) Fixes vulnerabilities", "b) Deletes programs", "c) Slows computer"],
"answer": "a"
},

{
"question": "What is a backup?",
"options": ["a) Copy of data", "b) Virus", "c) Attack"],
"answer": "a"
},

    ],


    "hard": [

        {
            "question": "SQL Injection targets?",
            "options": ["a) Databases", "b) Monitors", "c) Printers"],
            "answer": "a"
        },

        {
            "question": "A DDoS attack attempts to?",
            "options": ["a) Overload a service", "b) Create passwords", "c) Encrypt files"],
            "answer": "a"
        },

        {
            "question": "What is cryptography used for?",
            "options": ["a) Secure communication", "b) Gaming", "c) Printing"],
            "answer": "a"
        },

        {
            "question": "CIA Triad includes?",
            "options": ["a) Confidentiality, Integrity, Availability", "b) Computer, Internet, Access", "c) Code, Input, Application"],
            "answer": "a"
        },

        {
            "question": "A zero-day vulnerability is?",
            "options": ["a) Unknown security flaw", "b) Strong password", "c) Antivirus"],
            "answer": "a"
        },

        {
            "question": "Brute force attack tries?",
            "options": ["a) Many password combinations", "b) Delete files", "c) Install software"],
            "answer": "a"
        },

        {
            "question": "IDS stands for?",
            "options": ["a) Intrusion Detection System", "b) Internet Data Service", "c) Internal Device Security"],
            "answer": "a"
        },

        {
            "question": "Ransomware does what?",
            "options": ["a) Encrypts files and demands payment", "b) Improves security", "c) Deletes browser"],
            "answer": "a"
        },

        {
            "question": "Penetration testing is used to?",
            "options": ["a) Find vulnerabilities", "b) Damage systems", "c) Create viruses"],
            "answer": "a"
        },

        {
            "question": "Incident response handles?",
            "options": ["a) Security incidents", "b) Computer games", "c) Hardware design"],
            "answer": "a"
        }

    ]

}
   
}

def quiz():

    print("\n==============================")
    print("     SMART QUIZ APPLICATION")
    print("==============================")


    name = input("Enter your name: ")

    score = 0
    wrong_answers = 0


    print("\nChoose Category")
    print("1. Python")
    print("2. AI")
    print("3. Cyber Security")
    print("4. All Categories")


    category = input("Enter choice: ")


    if category == "1":
        category_name = "Python"
        selected_questions = quiz_data["python"]

    elif category == "2":
        category_name = "AI"
        selected_questions = quiz_data["ai"]

    elif category == "3":
        category_name = "Cyber Security"
        selected_questions = quiz_data["cyber"]

    elif category == "4":

        category_name = "All Categories"

        selected_questions = {
            "easy": [],
            "hard": []
        }

        for cat in quiz_data.values():
            selected_questions["easy"].extend(cat["easy"])
            selected_questions["hard"].extend(cat["hard"])

    else:
        print("Invalid Category")
        return



    print("\nChoose Difficulty")
    print("1. Easy")
    print("2. Hard")

    difficulty = input("Enter difficulty: ")


    if difficulty == "1":
        difficulty_name = "easy"

    elif difficulty == "2":
        difficulty_name = "hard"

    else:
        print("Invalid Difficulty")
        return



    questions = selected_questions[difficulty_name]


    random_questions = random.sample(
        questions,
        len(questions)
    )



    for i, q in enumerate(random_questions, start=1):

        print("\nQuestion", i)
        print(q["question"])


        for option in q["options"]:
            print(option)


        start = time.time()

        answer = input("\nYour Answer: ").lower().strip()

        end = time.time()


        if end - start > 15:

            print("Time Over!")

            wrong_answers += 1


        elif answer == q["answer"]:

            print("Correct!")

            score += 1


        else:

            print("Wrong!")

            print("Correct Answer:", q["answer"])

            wrong_answers += 1



    percentage = (score / len(random_questions)) * 100


    print("\n==============================")
    print("          RESULT")
    print("==============================")


    print("Name:", name)
    print("Category:", category_name)
    print("Difficulty:", difficulty_name)

    print("Score:", score, "/", len(random_questions))

    print("Wrong Answers:", wrong_answers)

    print(f"Percentage: {percentage:.2f}%")



    if percentage >= 50:
        status = "PASS"
    else:
        status = "FAIL"


    print("Status:", status)



    with open("quiz_results.txt","a") as file:

        file.write(
            f"\n{name} | {category_name} | {difficulty_name} | {score}/{len(random_questions)} | {status}"
        )


    print("\nResult Saved Successfully!")



while True:

    quiz()

    again = input("\nPlay Again? yes/no: ").lower()


    if again == "no":

        print("Thank You 😊")

        break
