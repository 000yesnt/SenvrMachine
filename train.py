from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chatbot = ChatBot("Senvr100")
import senvrlib as snv
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]
with open('568022407701594112/readdata') as my_file:
	for line in my_file:
		conversation.append(line)
		print("added "+line)

trainer = ListTrainer(chatbot)

trainer.train(conversation)
