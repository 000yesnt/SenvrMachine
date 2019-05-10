import chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import senvrlib as snv
import sys
chatbot = ChatBot(
    'Senvr200',
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'UNTRAINED',
            'maximum_similarity_threshold': 0.50
        }
    ],
    database="database.db"
)

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)



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
trainer.train(open("TRAINING-DATA.txt","r").readlines())

#chatterbot.trainers.UbuntuCorpusTrainer(chatbot)

