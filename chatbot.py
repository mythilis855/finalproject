from openai import OpenAI

class Chatbot:
    def __init__(self, api_key):
        self.api_key = api_key
        self.openai_client = OpenAI(api_key=self.api_key)

    def get_response(self, user_input):
        response = self.openai_client.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=150
        )
        return response.choices[0].text.strip()

def main():
    chatbot = Chatbot(api_key="YOUR_OPENAI_API_KEY")
    
    user_input = input("You: ")
    while user_input.lower() != "exit":
        response = chatbot.get_response(user_input)
        print(f"AI: {response}")
        user_input = input("You: ")

if __name__ == "__main__":
    main()