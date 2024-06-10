from revChatGPT.V1 import Chatbot

def chat_gpt():
    accesstoken = ""
    chatbot = Chatbot(config={"access_token":accesstoken}) 

    message = input("Вы:")
    output = chatbot.ask(message) #даем запрос ChatGPT с набранным текстом

    return output
