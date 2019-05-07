import discord
from discord.ext import commands
import random
import senvrlib as snv
description = '''Discord Interface for Chatterbox (RW)'''
bot = commands.Bot(command_prefix='$', description=description)
readingchannel=0



path="568022407701594112"
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command(pass_context=True)
async def readHere(ctx):
    readingchannel=ctx.message.channel.id
    await bot.say("Reading messages from channelid "+readingchannel);
    snv.flashvar("channelvar",readingchannel,"568022407701594112")

@bot.event
async def on_message(msg):
    readingchannel=snv.readvar("channelvar","568022407701594112")
    stdIn=snv.strFilter(msg.content)	
    print('------')
    print(str(readingchannel))
    print(str(snv.word_count(stdIn)))
    print(str(msg.channel.id))
    print(msg.content)
    print('------')
    if snv.word_count(stdIn) > 1 and msg.channel.id == readingchannel:
        f=open(path+"/readdata","a+")
        f.write(stdIn+"\n") 
        print("Written data!")
	f.close()
    else:
        print("Skipped this line.")
    await bot.process_commands(msg)


bot.run('NTY4MDIyNDA3NzAxNTk0MTEy.XNETWw.R0VsK_TUVuyYuMSAGrFrrUGeTYA')