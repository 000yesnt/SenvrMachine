from chatterbot import ChatBot
import senvrlib as snv
import sys
chatbot = ChatBot(
    'Senvr040',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'UNTRAINED',
            'maximum_similarity_threshold': 0.50
        }
    ],
)



def chat(stdIn):
	response = chatbot.get_response(stdIn)
	if snv.word_count(stdIn) > 1:
		f=open('568022407701594112/readdata',"a+")
		f.write(stdIn+"\n") 
		f.write(str(response)+"\n") 
		f.close()
	return response
print("Testing the chatbot...")
try:
    testLine=snv.random_line('568022407701594112/readdata')
    print('>"'+testLine+'"')
    chat(testLine)
except Exception as e:
    print(">Hello")
    chat("Hello")