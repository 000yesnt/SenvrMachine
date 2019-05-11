import chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import senvrlib as snv

import sys
print("Training the bot")
chatbot = ChatBot(
    'Senvr040',
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
    "chatterbot.corpus.english.ai",
)





conversation = [
    "sorry",
    "its ok",
    "senvr is gay",
    "no",
    "no",
    "yed",
    "shut up",
    "retrain",
    "NO NOT AGAN",
    "ree"
]

#with open('568022407701594112/readdata') as my_file:
#        for line in my_file:
#                conversation.append(line)
#                print("added "+line)

trainer = ListTrainer(chatbot)
trainer.train(conversation)
snv.clean_file("TRAINING-DATA.txt")
trainer.train(open("TRAINING-DATA.txt","r").readlines())
trauner=chatterbot.trainers.UbuntuCorpusTrainer(ChatBot)
trainer.train("/usr/local/lib/python3.6/site-packages/chatterbot_corpus/data/ubuntu_dialogs/")
trainer.train("chatterbot.corpus.ubuntu_dialogs")
#chatterbot.trainers.UbuntuCorpusTrainer(chatbot)

