print("Loading libraries...")
import discord
from discord.ext import commands
import random
import senvrlib as snv
import chattingbot as ctb



description = '''Discord Interface for Chatterbox (RW)'''
prefix="$"
readingchannel="all"
writingchannel=""
async def status_task():
    while True:
        await asyncio.sleep(10)
        VER=open("VERSION","r")
        await bot.change_presence(game=discord.Game(name="[AwR]Waiting..."))
        VER.close
print('Libraries loaded. Loading bot...')
bot = commands.Bot(command_prefix=prefix, description=description)
@bot.event
async def on_ready():
    print("We're all ready!\n\n")
    await bot.change_presence(game=discord.Game(name="[AwR]Initialized..."))


datfilepath="TRAINING-DATA.txt"
trainingdata=open(datfilepath,"r").readlines()


@bot.event
async def on_message(msg):
    await bot.change_presence(game=discord.Game(name="[AwR]Waiting..."))
    if msg.content.startswith(prefix):
        await bot.process_commands(msg)
        return False
    readingchannel=snv.readvar("readingchannel","568022407701594112")
    writingchannel=snv.readvar("writingchannel","568022407701594112")
    stdIn=snv.strFilter(msg.content)	
    if msg.author.id != bot.user.id:
        print("Processing "+stdIn)
        snv.clean_file(datfilepath)
        await bot.send_typing(msg.channel)
        send=snv.strFilter(str(ctb.chat(stdIn)))
        if send != 'untrained':
            await bot.send_message(msg.channel,send)
            await bot.change_presence(game=discord.Game(name="(R)Replied."))
            return
        else: 
            print("Caught untrainederror on "+stdIn)
            f=open(datfilepath,"a")
            send=snv.random_line(datfilepath)
            trainingdata.append(stdIn+"\n")
            trainingdata.append(send+"\n")             
            for line in trainingdata:
                f.write(line)
            f.close()
            await bot.send_message(msg.channel,send)
            await bot.change_presence(game=discord.Game(name="(AwR)Awaiting..."))
            return
#    if msg.channel.id == readingchannel or readingchannel == "all" :
#            print('------')
#            print(str(readingchannel))
#            print(str(snv.word_count(stdIn)))
#            print(str(msg.channel.id))
#            print(msg.content)
#            print('------\nResponse:')
#            if snv.word_count(stdIn) > 0:
#                f=open(datfilepath,"a+")
#                f.write(stdIn+"\n") 
#                print("Assimilated")
#                await bot.change_presence(game=discord.Game(name="(W)Learned something."))
#                f.close()
#            else:
#                print("Ignored")
#                await bot.change_presence(game=discord.Game(name="(AwR)Waiting..."))

	
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
@bot.command(pass_context=True)
async def writeAll(ctx):
    writingchannel="all"
    await bot.say("Writing messages to channelid "+str(writingchannel));
    snv.flashvar("writingchannel",writingchannel,"568022407701594112")
@bot.command()
async def returnData():
    readingchannel=snv.readvar("readingchannel","568022407701594112")
    writingchannel=snv.readvar("writingchannel","568022407701594112")
    await bot.say("I read in: "+readingchannel+"\nI respond in :"+writingchannel)
	    
    


bot.run('NTY4MDIyNDA3NzAxNTk0MTEy.XNETWw.R0VsK_TUVuyYuMSAGrFrrUGeTYA')
#print("We're all ready!\n\n")