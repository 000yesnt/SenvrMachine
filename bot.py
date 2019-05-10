print("Loading libraries...\n")
import discord
from discord.ext import commands
import random
import senvrlib as snv
import chattingbot as ctb



description = '''Discord Interface for Chatterbox (RW)'''
prefix="$"
readingchannel="all"
writingchannel=""

print('Libraries loaded. Loading bot...\n\n')
bot = commands.Bot(command_prefix=prefix, description=description)
@bot.event
async def on_ready():
    print("We're all ready!\n\n")
    await bot.change_presence(game=discord.Game(name="Awaiting..."))

@bot.event
async def on_message(msg):
    if msg.content.startswith(prefix):
        await bot.process_commands(msg)
        return False
    readingchannel=snv.readvar("readingchannel","568022407701594112")
    writingchannel=snv.readvar("writingchannel","568022407701594112")
    stdIn=snv.strFilter(msg.content)	
    if msg.channel.id==writingchannel and msg.author.id != bot.user.id:
        print("Processing "+stdIn)
        snv.clean_file("568022407701594112/readdata")
        await bot.send_typing(msg.channel)
        send=snv.strFilter(str(ctb.chat(stdIn)))
        await bot.send_message(msg.channel,send)
        print("UNTRAINED ON "+stdIn)

    if msg.channel.id == readingchannel or readingchannel == "all" :
            print('------')
            print(str(readingchannel))
            print(str(snv.word_count(stdIn)))
            print(str(msg.channel.id))
            print(msg.content)
            print('------\nResponse:')
            if snv.word_count(stdIn) > 0 and msg.author.id != bot.user.id and msg.channel.id != writingchannel:
                f=open("568022407701594112/readdata","a+")
                f.write(stdIn+"\n") 
                print("Assimilated")
                await bot.change_presence(game=discord.Game(name="Taught a line!"))
                f.close()
            else:
                print("Ignored")
                await bot.change_presence(game=discord.Game(name="Awaiting..."))

	
@bot.command(pass_context=True)
async def readHere(ctx):
    readingchannel=str(ctx.message.channel.id)
    await bot.say("Reading messages from channelid "+str(readingchannel));
    snv.flashvar("readingchannel",readingchannel,"568022407701594112")

@bot.command(pass_context=True)
async def readAll(ctx):
    readingchannel="all"
    await bot.say("Reading message to channelid "+str(readingchannel));
    snv.flashvar("readingchannel",readingchannel,"568022407701594112")

@bot.command(pass_context=True)
async def writeHere(ctx):
    writingchannel=str(ctx.message.channel.id)
    await bot.say("Writing messages to channelid "+str(writingchannel));
    snv.flashvar("writingchannel",writingchannel,"568022407701594112")
@bot.command()
async def returnData():
    readingchannel=snv.readvar("readingchannel","568022407701594112")
    writingchannel=snv.readvar("writingchannel","568022407701594112")
    await bot.say("I read in: "+readingchannel+"\nI respond in :"+writingchannel)
	    
    


bot.run('NTY4MDIyNDA3NzAxNTk0MTEy.XNETWw.R0VsK_TUVuyYuMSAGrFrrUGeTYA')
#print("We're all ready!\n\n")