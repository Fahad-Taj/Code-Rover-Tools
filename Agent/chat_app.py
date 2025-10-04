def run_simulated_chat():
    print("Welcome to the Simulated Chat App!")
    user_name = input("Please enter your name: ")
    print(f"Hello, {user_name}! Type your messages below. Type 'quit' to exit.")

    while True:
        user_message = input(f"{user_name}: ")

        if user_message.lower() == 'quit':
            print("Exiting chat. Goodbye!")
            break
        
        print(f"{user_name}: {user_message}")
        
        # Simulate a response from another participant (e.g., a bot)
        if "hello" in user_message.lower() or "hi" in user_message.lower():
            print("Bot: Hi there!")
        elif "how are you" in user_message.lower():
            print("Bot: I'm a simulation, so I'm always great!")
        elif "name" in user_message.lower() and "your" in user_message.lower():
            print("Bot: I am Bot, your friendly chat simulator.")
        else:
            print(f"Bot: I received your message: '{user_message}'")

if __name__ == '__main__':
    run_simulated_chat()
