# english_tutor_cli.py

def simple_ai_logic(user_input_text):
    """
    一个非常简单的基于规则的AI逻辑。
    接收用户输入的文本，返回AI的文本回答。
    """
    user_input_lower = user_input_text.lower().strip()
    ai_response = "Sorry, I didn't understand that. Can you rephrase?" # 默认回答

    if "hello" in user_input_lower or "hi" in user_input_lower:
        ai_response = "Hello there! How can I help you practice your English today?"
    elif "how are you" in user_input_lower:
        ai_response = "I'm an AI, so I don't have feelings, but I'm functioning optimally! Thanks for asking. How about you?"
    elif "what's your name" in user_input_lower or "who are you" in user_input_lower:
        ai_response = "I am your friendly English Practice AI. You can call me TutorBot."
    elif "weather" in user_input_lower:
        ai_response = "I don't have access to real-time weather information. Let's talk about something else! For example, you can ask me about 'apples' or 'books'."
    elif "apple" in user_input_lower:
        ai_response = "An apple is a round fruit with firm, white flesh and a green or red skin. Do you like apples?"
    elif "book" in user_input_lower:
        ai_response = "A book is a set of written, printed, or blank sheets, fastened along one side and encased in a protective cover. What's your favorite book?"
    elif "thank you" in user_input_lower or "thanks" in user_input_lower:
        ai_response = "You're welcome! Is there anything else I can help you with?"
    elif "bye" in user_input_lower or "goodbye" in user_input_lower or "exit" in user_input_lower or "quit" in user_input_lower:
        ai_response = "Goodbye! Keep practicing your English. See you next time!"
    # 你可以在这里添加更多的规则
    # elif "关键词" in user_input_lower:
    #     ai_response = "相关的回答"

    return ai_response

def main():
    """
    主程序运行逻辑
    """
    print("English Tutor AI (Text Version)")
    print("Type your questions or statements in English.")
    print("Type 'quit', 'exit', or 'bye' to end the session.")
    print("-" * 30)

    while True:
        try:
            # 模拟用户语音输入 (实际是文本输入)
            user_input = input("You: ")

            if user_input.lower().strip() in ["quit", "exit", "bye"]:
                ai_final_response = simple_ai_logic(user_input)
                print(f"AI:  {ai_final_response}")
                break

            # 获取AI的回答
            ai_output = simple_ai_logic(user_input)

            # 模拟AI语音输出 (实际是文本输出)
            print(f"AI:  {ai_output}")

        except KeyboardInterrupt: # 处理 Ctrl+C 退出
            print("\nAI:  Goodbye! Hope to see you soon.")
            break
        except Exception as e:
            print(f"AI:  An error occurred: {e}")
            print("AI:  Let's try again.")

if __name__ == "__main__":
    main()
