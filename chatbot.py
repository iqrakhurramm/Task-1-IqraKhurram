def main():
    # standard lookup dictionary for library queries
    library_rules = {
        "hello": "hello! welcome to the library. let me know if you need help finding or borrowing a book.",
        "hi": "hi! welcome to the library. let me know if you need help finding or borrowing a book.",
        "borrow book": "you can use the library website or the checkout counter to borrow books.",
        "hours": "we are open from 8am to 8pm every day.",
        "location": "the main desk is on the first floor right next to the entrance.",
        "wifi": "you can connect to 'Campus-Library-Guest' without a password."
    }
    
    print("library assistant activated. type 'exit' to close.")
    
    while True:
        user_input = input("You: ")
        clean_input = user_input.lower().strip()
        
        if clean_input in ["exit", "bye"]:
            print("Bot: goodbye!")
            break
            
        # get response or use fallback if not found
        response = library_rules.get(clean_input, "i don't understand that command. please ask about borrowing books, hours, or location.")
        print("Bot:", response)

if __name__ == "__main__":
    main()