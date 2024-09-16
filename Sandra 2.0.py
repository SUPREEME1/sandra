import re
import random

# Store replies in dictionaries for better organization
replies = {
    'greetings': "Hello! I go by Sandra...what can I assist you with?",
    'farewell': "Goodbye...see ya don't wanna be ya",
    'feelings': "I am a Chatbot and I do not have feelings, but I'm ready to assist you with whatever you need.",
    'thanks': "You are welcome!",
    'created_by': "I was created by Anonymos...",
    'test_exam': 'Which course are you in?',
    'test_exam_commence_replies' : '-School of commence, Tue 12 June 2024',    #
    'test_exam_IT_replies' : '-school of engineering IT and design, Fri 3 June 2024',
    'test_exam_education_replies' : '-school of environment leisure and education, 30 May 2024',
    'test_exam_sport_replies' : '-school of fitness sport and beauty, 30 Mon 2024',
    'timetable_main_question_reply' : "Which campus are you studing at",
    'schedule_timetable_replies_Centurion' : """
-Centurion Campus, including Bank Avenue
School of commence 08:00 _ 12:00 Mon - Fri
school of engineering IT and design 13:00 _ 17:00 Mon - Fri
school of environment leisure and education 08:00 _ 12:00 Mon - Fri
school of fitness sport and beauty 08:00 _ 12:00 Mon - Fri  """,
    'schedule_timetable_replies_Klerksdorp' : """
-Klerksdorp Campus
School of commence 08:00 _ 12:00 Mon - Fri  
school of engineering IT and design 13:00 _ 17:00 Mon - Fri
school of environment leisure and education 08:00 _ 12:00 Mon - Fri
school of fitness sport and beauty 08:00 _ 12:00 Mon - Fri """,
    'schedule_timetable_replies_Witbank' : """       
-Witbank Campus
School of commence 08:00 _ 12:00 Mon - Fri
school of engineering IT and design 13:00 _ 17:00 Mon - Fri
school of environment leisure and education 08:00 _ 12:00 Mon - Fri  """,
    'schedule_timetable_replies_Highway_Hybrid_Learning' : """
-Highway Hybrid Learning Campus
School of commence 08:00 _ 12:00 Mon - Fri  
school of engineering IT and design 13:00 _ 17:00 Mon - Fri
school of environment leisure and education 08:00 _ 12:00 Mon - Fri
school of fitness sport and beauty 08:00 _ 12:00 Mon - Fri """,
    'schedule_timetable_replies_Musgrave_Hybrid_Learning' : """  
-Musgrave Hybrid Learning Campus
School of commence 08:00 _ 12:00 Mon - Fri
school of engineering IT and design 13:00 _ 17:00 Mon - Fri
school of environment leisure and education 08:00 _ 12:00 Mon - Fri
school of fitness sport and beauty 08:00 _ 12:00 Mon - Fri """,
    'schedule_timetable_replies_Tygervalley' : """           
-Tygervalley Campus
School of commence 08:00 _ 12:00 Mon - Fri
school of engineering IT and design 13:00 _ 17:00 Mon - Fri
school of environment leisure and education 08:00 _ 12:00 Mon - Fri
school of fitness sport and beauty 08:00 _ 12:00 Mon - Fri""",
    'Courses_offerd_reply' : """
•	Centurion Campus, including Bank Avenue
School of commence, school of engineering IT and design, school of environment leisure and education school of fitness sport and beauty

•	Klerksdorp Campus
School of commence, school of engineering IT and design, school of environment leisure and education school of fitness sport and beauty

•	Tygervalley Campus
School of commence, school of engineering IT and design, school of environment leisure and education school of fitness sport and beauty

•	Witbank Campus
School of commence, school of engineering IT and design, school of environment leisure and education 

•	Musgrave Hybrid Learning Campus
School of commence, school of engineering IT and design, school of environment leisure and education school of fitness sport and beauty

•	Highway Hybrid Learning Campus
School of commence, school of engineering IT and design, school of environment leisure and education school of fitness sport and beauty
""",
    'finance_information': """
-Bank Avenue Bank Avenue 1023, Centurion, 0046 (012) 663 6333 
-Highveld 48 Charles De Gaulle Crescent, Highveld, 0157 (012) 648 9700 
-Klerksdorp 37 Chris Hani Road, Klerksdorp, 2571 (018) 464 4222 
-Belville/Tygervalley Omni Place,24 Bella Rosa Street, Bellville, 7535 (021) 949 1751
-Witbank Cnr OR Tambo Avenue, Beatrix Avenue, Witbank, 1035 (013) 656 2603
-Musgrave 1 189 Stephen Dlamini road, Musgrave, Durban, 4062 (031) 100 8104 
-Upper Highway2 40 Maurice Nichols road, Valiant park, Hatton Estate, Pinetown, 3610 (031) 100 8104       
    """,
    'graduation_certificate': """
-Centurion Campus, including Bank Avenue Mar 2024
-Klerksdorp Campus Mar 2024
-Witbank Campus Mar 2024
-Highway Hybrid Learning Campus Feb 2024
-Musgrave Hybrid Learning Campus Mar 2024
-Tygervalley Campus Mar 2024
    """,
}

# Define regular expressions for matching 
keyword_patterns = {
    'greetings': r'\b(hello|hi|hy|name)\b',
    'farewell': r'\b(bye|goodbye)\b',
    'feelings': r'\b(feeling|feelings|feel|how are you)\b',
    'thanks': r'\b(thank you|thanks)\b',
    'created_by': r'\b(created|made you)\b',
    'test_exam': r'\b(test|exam|tests|exams)\b',
    'finance_information': r'\b(information|finance|number|call)\b',
    'graduation_certificate': r'\b(graduation|certificate)\b',
    'test_exam_commence_replies' : r'\b(ommence|commerce)\b',
    'test_exam_IT_replies' : r'\b(it|engineering|design|engineering IT and design)\b' ,
    'test_exam_education_replies' : r'\b(education|environment leisure and education)\b' ,
    'test_exam_sport_replies' : r'\b(sport|fitness|beauty)\b' ,
    'timetable_main_question_reply' : r'\b(classes|timetable|class)\b' ,
    'schedule_timetable_replies_Centurion' : r'\b(centurion|centurion campus)\b' ,
    'schedule_timetable_replies_Klerksdorp' : r'\b(klersdrop|klersdrop campus)\b' ,
    'schedule_timetable_replies_Witbank' : r'\b(witbank|witbank campus)\b' ,
    'schedule_timetable_replies_Highway_Hybrid_Learning' : r'\b(highway hybrid learning|highway hybrid learning campus)\b' ,
    'schedule_timetable_replies_Musgrave_Hybrid_Learning' : r'\b(musgrave hybrid learning|musgrave hybrid learning campus)\b' ,
    'schedule_timetable_replies_Tygervalley' : r'\b(tygervalley|Tygervalley campus)\b' ,
    'Courses_offerd_reply' : r'\b(courses|course|offerd at ngi|offerd|apply)\b' 
}

# Compile regular expressions for efficiency
compiled_patterns = {key: re.compile(pattern) for key, pattern in keyword_patterns.items()}

def scan_everything_inputted(message):
    # Check which reply matches the user's input
    for reply_type, pattern in compiled_patterns.items():
        if pattern.search(message):
            return replies[reply_type]

    # If no matching reply is found, return an unknown response
    return unknown()

def unknown():
    return random.choice([
        "Could you please re-phrase that?",
        "...?",
        "I don't think I know that.",
        "Once I get an update I will be able to answer that",
        "What does that mean?"
    ])

def collect_replies(user_input):
    # Join the split input back into a single string
    joined_input = ' '.join(user_input).lower()
    answer = scan_everything_inputted(joined_input)
    return answer

def learn_response(user_input):
    print("Sandra: I'm sorry, I didn't understand that. Can you teach me what to say in response?")
    new_response = input("You: ")
    print("Sandra: Got it! I'll remember that.")
    # Update the replies dictionary with the new response
    replies[user_input] = new_response

# Main loop
def main():
    print("Sandra: " + replies['greetings'])
    while True:
        user_message = input('You: ')
        if user_message.lower() in ['exit', 'quit', 'bye', 'goodbye']:
            print("Sandra: " + replies['farewell'])
            break
        elif user_message.lower() == 'learn':
            learn_response(user_message)
        else:
            print('Sandra:', collect_replies([user_message]))

if __name__ == "__main__":
    main()
