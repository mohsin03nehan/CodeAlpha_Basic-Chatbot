def chatbot_response(user_input):

    if user_input == "hello":
        return "Hi!"

    elif user_input == "how are you":
        return "I am fine, thanks!"

    elif user_input == "what is your name":
        return "I am a simple chatbot."

    elif user_input == "who made you":
        return "I was created using Python."

    elif user_input == "bye":
        return "Goodbye!"

    else:
        return "Sorry, I don't understand."


# Main program
print("================ Basic Chatbot =================")
print("Type 'bye' to exit.\n")

while True:
    user_message = input("You: ").lower()

    reply = chatbot_response(user_message)
    print("Bot:", reply)

    if user_message == "bye":
        break