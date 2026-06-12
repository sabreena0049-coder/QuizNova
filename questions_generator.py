import json

questions = [

# ---------------- PYTHON ----------------

{
    "category": "Python",
    "question": "Which keyword is used to define a function in Python?",
    "options": ["func", "define", "def", "function"],
    "answer": "def"
},
{
    "category": "Python",
    "question": "What is the output type of input() in Python?",
    "options": ["int", "float", "str", "bool"],
    "answer": "str"
},
{
    "category": "Python",
    "question": "Which data type is immutable?",
    "options": ["List", "Dictionary", "Set", "Tuple"],
    "answer": "Tuple"
},
{
    "category": "Python",
    "question": "Which symbol is used for comments?",
    "options": ["//", "#", "/*", "--"],
    "answer": "#"
},
{
    "category": "Python",
    "question": "Which function returns the length of a list?",
    "options": ["count()", "size()", "length()", "len()"],
    "answer": "len()"
},

# ---------------- JAVA ----------------

{
    "category": "Java",
    "question": "Which method is the entry point of a Java application?",
    "options": ["run()", "main()", "start()", "init()"],
    "answer": "main()"
},
{
    "category": "Java",
    "question": "Java is a _____ language.",
    "options": ["Procedure-oriented", "Object-oriented", "Machine", "Assembly"],
    "answer": "Object-oriented"
},
{
    "category": "Java",
    "question": "Which keyword is used for inheritance?",
    "options": ["inherits", "extends", "implement", "super"],
    "answer": "extends"
},
{
    "category": "Java",
    "question": "Which package is imported by default?",
    "options": ["java.io", "java.util", "java.lang", "java.sql"],
    "answer": "java.lang"
},
{
    "category": "Java",
    "question": "Which operator compares object references?",
    "options": ["==", "equals()", "!=", "compare()"],
    "answer": "=="
},

# ---------------- DBMS ----------------

{
    "category": "DBMS",
    "question": "What does DBMS stand for?",
    "options": ["Database Management System", "Data Backup Management System", "Digital Base Management System", "Database Mapping System"],
    "answer": "Database Management System"
},
{
    "category": "DBMS",
    "question": "Which key uniquely identifies a record?",
    "options": ["Foreign Key", "Primary Key", "Candidate Key", "Alternate Key"],
    "answer": "Primary Key"
},
{
    "category": "DBMS",
    "question": "SQL stands for?",
    "options": ["Structured Query Language", "Simple Query Language", "System Query Language", "Sequential Query Language"],
    "answer": "Structured Query Language"
},
{
    "category": "DBMS",
    "question": "Which normal form removes partial dependency?",
    "options": ["1NF", "2NF", "3NF", "BCNF"],
    "answer": "2NF"
},
{
    "category": "DBMS",
    "question": "Which command removes all rows but keeps table structure?",
    "options": ["DELETE", "REMOVE", "TRUNCATE", "DROP"],
    "answer": "TRUNCATE"
},

# ---------------- OS ----------------

{
    "category": "OS",
    "question": "What does OS stand for?",
    "options": ["Open System", "Operating System", "Object System", "Online System"],
    "answer": "Operating System"
},
{
    "category": "OS",
    "question": "Which scheduling algorithm gives minimum average waiting time?",
    "options": ["FCFS", "Round Robin", "SJF", "Priority"],
    "answer": "SJF"
},
{
    "category": "OS",
    "question": "Which memory is volatile?",
    "options": ["ROM", "SSD", "RAM", "Hard Disk"],
    "answer": "RAM"
},
{
    "category": "OS",
    "question": "Which scheduling is preemptive?",
    "options": ["FCFS", "SJF", "Round Robin", "FIFO"],
    "answer": "Round Robin"
},
{
    "category": "OS",
    "question": "Deadlock occurs when?",
    "options": ["Processes cooperate", "Resources are shared safely", "Processes wait indefinitely", "Memory is free"],
    "answer": "Processes wait indefinitely"
},

# ---------------- APTITUDE ----------------

{
    "category": "Aptitude",
    "question": "What is 25% of 200?",
    "options": ["25", "50", "75", "100"],
    "answer": "50"
},
{
    "category": "Aptitude",
    "question": "If a train travels 60 km in 1 hour, its speed is?",
    "options": ["50 km/h", "60 km/h", "70 km/h", "80 km/h"],
    "answer": "60 km/h"
},
{
    "category": "Aptitude",
    "question": "What is the square root of 144?",
    "options": ["10", "11", "12", "13"],
    "answer": "12"
},
{
    "category": "Aptitude",
    "question": "A number increased by 20% becomes 120. Original number?",
    "options": ["100", "110", "90", "80"],
    "answer": "100"
},
{
    "category": "Aptitude",
    "question": "What is 15 × 8?",
    "options": ["100", "110", "120", "130"],
    "answer": "120"
}
]

# Repeat and slightly vary questions to build 500 entries
full_bank = []

for i in range(20):
    for q in questions:
        item = q.copy()
        item["question"] = f"{q['question']} ({i+1})"
        full_bank.append(item)

with open("questions.json", "w", encoding="utf-8") as f:
    json.dump(full_bank, f, indent=4)

print(f"{len(full_bank)} questions generated successfully!")