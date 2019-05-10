from chatterbot import ChatBot
import senvrlib as snv
import sys
chatbot = ChatBot(
    'Senvr200',
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
	print(response)
	if snv.word_count(stdIn) > 1:
		f=open('568022407701594112/readdata',"a+")
		f.write(stdIn+"\n") 
		print("Written data!")
		f.close()
	else:
		print("Skipped this line.")
	return response
print("Testing the chatbot...")
testLine=snv.random_line('568022407701594112/readdata')
print('Using line "'+testLine+'"')
chat(testLine)