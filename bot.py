print("Loading prerequisites...")
import discord
import asyncio
from discord.ext import commands
import random
import senvrlib as snv
import chattingbot as ctb
from mutagen.mp3 import MP3
import os
print("Loading botface...")
description = '''SBML+SB3 matching'''
prefix="$"
readingchannel="all"
writingchannel=""
async def status_task():
    while True:
        await asyncio.sleep(2)
        await bot.change_presence(game=discord.Game(name="(0)"))
print('Libraries loaded. Loading bot...')
bot = commands.Bot(command_prefix=prefix, description=description)
@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    await bot.loop.create_task(status_task())
    print("------\n")
    print("Ready for action:\n")


datfilepath="TRAINING-DATA.txt"
trainingdata=open(datfilepath,"r").readlines()


@bot.event
async def on_message(msg): #processes messages in readingchannel and either replies with trained data or stores as training data
    await bot.change_presence(game=discord.Game(name="[1]")) #   "hey someone typed in a channel, lets check it out"
    stdIn=snv.strFilter(msg.content) #makes the bot not explode like a thermonuclear bomb
    if msg.content.startswith(prefix) or len(stdIn) < 2: #before digesting or replying to the message, checks if it is prefixed
        await bot.process_commands(msg) #if it did, throw all the code below into oblivion. also while i'm at it, yes i called processing "digesting"
        return False
    readingchannel=snv.readvar("readingchannel","568022407701594112")
    writingchannel=snv.readvar("writingchannel","568022407701594112")
    if msg.author.id != bot.user.id and not msg.author.bot: #safeguard so the bot doesn't reply to itself like a baby with schizophrenia
        print('-----------------------------------------------\n'+"Processing "+stdIn)
        snv.clean_file(datfilepath)
        await bot.send_typing(msg.channel) #human-like typing
        send=snv.strFilter(str(ctb.chat(stdIn)))
        if send != 'untrained': #did the bot learn how to reply?
            print("TRAINED REPLY") #if it did, do the ue
            print("Replied with: "+send)
            await bot.send_message(msg.channel,send)
            await bot.change_presence(game=discord.Game(name="{2}")) #    "yeah i got this"
            print('-----------------------------------------------')
            return
        else: #opposite of above
            print("UNTRAINED REPLY")
            f=open(datfilepath,"a")
            send=snv.random_line(datfilepath)
            trainingdata.append(stdIn+"\n")
            trainingdata.append(send+"\n")
            for line in trainingdata:
                f.write(line)
            f.close()
            await bot.send_message(msg.channel,send)
            print("Replied with: "+send)
            await bot.change_presence(game=discord.Game(name="[1]"))
            print('-----------------------------------------------')
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
    await bot.change_presence(game=discord.Game(name="[1]"))

@bot.command(pass_context=True)
async def readAll(ctx):
    readingchannel="all"
    await bot.say("Reading message to channelid "+str(readingchannel));
    snv.flashvar("readingchannel",readingchannel,"568022407701594112")
    await bot.change_presence(game=discord.Game(name="[1]"))

@bot.command(pass_context=True)
async def writeHere(ctx):
    writingchannel=str(ctx.message.channel.id)
    await bot.say("Writing messages to channelid "+str(writingchannel));
    snv.flashvar("writingchannel",writingchannel,"568022407701594112")
    await bot.change_presence(game=discord.Game(name="[1]"))

@bot.command(pass_context=True)
async def writeAll(ctx):
    writingchannel="all"
    await bot.say("Writing messages to channelid "+str(writingchannel));
    snv.flashvar("writingchannel",writingchannel,"568022407701594112")
    await bot.change_presence(game=discord.Game(name="[1]"))

@bot.command()
async def returnData():
    readingchannel=snv.readvar("readingchannel","568022407701594112")
    writingchannel=snv.readvar("writingchannel","568022407701594112")
    await bot.say("I read in: "+readingchannel+"\nI respond in :"+writingchannel)
    await bot.change_presence(game=discord.Game(name="[1]"))


#automated bot say thing
async def botSay(Title="Default Title",Description="Default Description", Text=""):
        embed = discord.Embed(title=Title, description=Description, color=0x00ff00)
        embed.add_field(name="-----------", value=Text, inline=False)
        await bot.say(embed=embed)

#str ot member because im sof ucking tired of this ambigious : discord.Member shit
def strToMem(ctx, memID = "", name=""):
	members=ctx.message.server.members
	#ease of access
	if memID == "" and name == "":
		return None
		#GFY if you dont provide the right data
	for member in members:
		if member.id == memID:
			return member
			#if the ID, which is more unique, matches, then return and stop here
	for member in members:
		if member.name == name:
			return member
			#otherwise, try looking for the name, which can be less unique but not terribly common...
	return None
	#If nothing was returned, then no member by the name memId or name exists here

#sudo system that calls on another sudo system because fuck you
def checkSudo(ctx, user):
#takes ctx, just to make shit easier. though if we, for some reason, want to check a different server than the asker, we'll have to fix tha
	user=strToMem(ctx,user)
	person=snv.strFilter(user.id)
	#filter the user so they cant do anything weird
	serverid=ctx.message.server.id
	#to separate each server's sudoers so a suduer from server 1234 cant fuck with 4321
	owner=ctx.message.server.owner.id
	#get the owner to see if user is the server owner, which should obviously be a sudoer
	role=snv.peek("sudorole",serverid)
	#get the set sudoer role

	#CHECK ONE: If the user owns the server
	if person == owner:
		snv.log("info",person+" PASSED a sudo check for "+str(serverid)+"/sudoers.conf")
		return True;
	#CHECK TWO: if the user has the pre-set role
	if role in [y.id.lower() for y in user.roles] and role != "":
		snv.log("info",person+" PASSED a sudo check for "+str(serverid)+"/sudoers.conf")
		return True;
		#they got the role
	else:
		snv.log("warn",serverid+" has no sudorole setup")
		#just to quickly dispatch stupid crap
	if not os.path.isdir(serverid):
		os.mkdir(serverid)
		#If the path dont exist, make it. that would also mean that, fucking, the file dont exist, but i guess i wrote this when i had the large autism moment
	sudofile=open(serverid+"/sudoers.conf","r")
	if person in snv.strFilter(sudofile.read()):
		#true as in "nothing fucked up"
		snv.log("info",person+" PASSED a sudo check for "+str(serverid)+"/sudoers.conf")
		#close file
		sudofile.close
		return True;
	else:
		snv.log("info",person+" FAILED a sudo check for "+str(serverid)+"/sudoers.conf")
		#close file
		sudofile.close
		#false as in "something fucked up"
	return False;
	#incase all fails

#Holds the "X is typing..." thing for delay seconds
#this exists because if you "send" a typing indicator, it will naturally time out after 4 or 5 seconds.
#Which is annoying sometimes.
async def holdWrite(ctx, delay=1):
	if delay < 4:
	#just some redundancy, no need to loop if it falls between the right range
		await bot.send_typing(ctx.message.channel)
		await asyncio.sleep(delay)
		return
	I=0
	delay=math.ceil(delay)
	if delay < 1:
		delay=1
	while I < delay:
		I += 1
		await bot.send_typing(ctx.message.channel)
		await asyncio.sleep(1)

#Type like a human, requires holdWwrite
#Based on the average CPM of like, 190 or something.
async def humanType(ctx, msg, speed=1):
	delay=len(msg)/random.uniform(16.0, 32.0)/speed
	await holdWrite(ctx, delay)
	await bot.say(msg)
#custom help thing
bot.remove_command('help')

###BOT COMMANDS###
#below is what i'm guessing an enhanced archive of SenvrBot
@bot.command(name="help", brief="Returns all commands available", pass_context=True)
async def help(ctx):
	commands=list(bot.commands.values())
	embed = discord.Embed(title="Help", description="All commands", color=0x00ff00)
	for command in commands:
		if str(command.brief) != "None":
			embed.add_field(name="Command: "+command.name, value="Description:\n "+str(command.brief), inline=False)
		else:
			embed.add_field(name="Command: "+command.name, value="Description:\n ...?\nThere's no usage set up for this.", inline=False)
	await bot.say(embed=embed)

#manual, like how you would on linux
@bot.command(pass_context=True, brief="Detailed descriptions of commands.")
async def man(ctx, name):
	commands=list(bot.commands.values())
	comand=""
	for tempCommand in commands:
		if tempCommand.name == name:
			command=tempCommand
			break
	if command.name == "":
		await bot.say("Command not found.")
		return
	if command.description != "":
		await botSay("Manual for Command: "+command.name,"In-depth descriptions on a command-by-command basis.",command.description)
	elif str(command.brief) != None:
		await botSay("Manual for Command: "+command.name,"In-depth descriptions on a command-by-command basis.",command.brief)
	else:
		await bot.say("There's no documentation for this command at all.")

#generic testing placeholder
@bot.command(pass_context=True)
async def placeholder(ctx, speed=1):
	await bot.say("speed: "+str(speed))
	await humanType(ctx,"mogatown11teen",speed)
	await humanType(ctx,"mogatown11teenAAAA",speed)
	await humanType(ctx,"mogatown11teenBBBBBBBB",speed)
	await humanType(ctx,"According to all known laws of aviation, there is no way that a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway. Because bees don’t care what humans think is impossible.” ",speed)

#adduser to sudoers file
@bot.command(pass_context=True, brief="SUDO: Adds a user to the sudoers group",description=prefix+"adduser user \nAdds a user to the sudoers file for this server")
async def adduser(ctx, user : discord.Member):
	userid=user.id
	serverid=ctx.message.server.id
	randchance=random.randrange(1,100)
	if checkSudo(ctx, ctx.message.author.id):
		if checkSudo(ctx, userid):
			if snv.makesudoer(userid,serverid):
				await bot.say("Executed")
			else:
				await bot.say("Problem in execution")
		else:
			await bot.say("Executed")
	else:
		if randchance < 25:
			await bot.say("You are not a sudoer")
		else:
			await bot.say("You are not a suetor.")

#ping commands
@bot.command(pass_context=True,brief="Simple ping command.",description="THANKS SAIKO! Checks the latency between the bot (if locally hosted, the pc) and discord.")
async def ping(ctx):
	t = await bot.say('Pong!')
	ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
	await bot.edit_message(t, new_content='Pong! Took: {}ms'.format(int(ms)))

#return what is said by speaker
@bot.command(pass_context=True,brief="Returns what you say.")
async def echo(ctx):
    await bot.send_message(ctx.message.channel,snv.strFilter(ctx.message.content))

#"ask" command, 1/3 chance for every answer and is intentionally simple (if you see other "ask" commands in other bots it seems like it hangs on "ask again" or "unsure" all the time)
@bot.command(pass_context=True,brief="Answers a question.",description="Answers a given question with 3 possible answers.")
async def ask(ctx):
	if len(ctx.message.content) < 2:
		await bot.send_message(ctx.message.channel, "You need to ask a question.")
		return;
	else:
		replies=["yes","no","maybe"]
		await bot.say(random.choice(replies))

#play a random mp3 in a VC, usually earrape or stupid memes - Modified from snv1
@bot.command(pass_context=True,brief="Plays a normal audio clip.",description="Plays an MP3 file from the `audio/` directory. You can select ")
async def play(ctx,id=-1):

    if id > 0:
        audio="audio/"+os.listdir("audio/")[id]
    else:
        audio = "audio/" + random.choice(os.listdir("audio/"))
    duration=MP3(audio).info.length
    message=await bot.say("Playing file "+audio+" which last "+str(duration)+" seconds.")
    voice = await bot.join_voice_channel(ctx.message.author.voice_channel)
    player = voice.create_ffmpeg_player(audio)
    player.start()
    await asyncio.sleep(duration+1)
    await voice.disconnect()
    if 1-duration > 1:
        await asyncio.sleep(1-duration)
    else:
        await asyncio.sleep(1)
    await bot.delete_message(message)

#you know what would be cool
#if the assf.art API command came back
@bot.command(pass_context=True,brief="Returns assf.art text",description="Gets random text from assf.art API and returns it to chat")
async def assf(ctx):
	assft = snv.assfart()
	await bot.send_message(ctx.message.channel, assft)

##END BOT COMMANDS
#handle errors
@bot.event
async def on_command_error(error, ctx):
    await bot.send_message(ctx.message.channel, "uh-oh spaghetti-code:\n`"+str(error)+"`")
    snv.log("error",str(error))
    print(error)
	    
    

tokn = open("tkn", "r").read()
bot.run(str(tokn))
#print("We're all ready!\n\n")
