This Python-based chatbot, named Sandra, responds to user inputs with specific replies based on recognized keywords. The bot can:

Recognize various keywords and respond with predefined messages.
Handle user queries about timetables, campus locations, course offerings, and graduation information for different campuses.
Learn new responses by asking the user for input when an unknown query is encountered.
Features:
Keyword Recognition: Uses regular expressions to detect keywords in the user's input and select an appropriate response from a dictionary of replies.
Fallback Responses: Provides generic responses for unrecognized queries.
Learning Capability: Can learn new responses to specific phrases if initiated with the "learn" command.
Exit Commands: The conversation can end when the user types "exit" or "goodbye."
Usage:
To start the chatbot, run main(). Sandra will greet you and engage in conversation based on your inputs.
