import discord
import random
from discord.ext import commands
import os
import sys
import psutil
import logging
import time
import string
import subprocess
import time
import git
from git import Repo

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
token_file = open('token.txt', 'r')
token = token_file.read()

def arestart():
    import sys
    print("argv was",sys.argv)
    print("sys.executable was", sys.executable)
    print("restart now")

def restartApp():
    python = sys.executable
    os.execl(python, python, *sys.argv)

@bot.command(help='Displays Rule 11')
async def r11(ctx):
    await ctx.send('Please refrain from asking for or giving assistance with installing, using, or obtaining pirated software.')
    
@bot.command(help='Displays Rule 11')
async def rule11(ctx):
    await ctx.send('Please refrain from asking for or giving assistance with installing, using, or obtaining pirated software.')

@bot.command(help="dispways wuwe 11")
async def wuwe11(ctx):
    await ctx.send('pwease wefwain fwom asking fow ow giving assistance with instawwing, using, ow obtaining piwated softwawe')

@bot.command(help="dispways wuwe 11")
async def w11(ctx):
    await ctx.send('pwease wefwain fwom asking fow ow giving assistance with instawwing, using, ow obtaining piwated softwawe')

@bot.command(help="Bans a member.")
async def ban(ctx, member : discord.Member):
    if member.name == 'Joe Bot Testing':
        await ctx.send('ERROR: Malfunction 54.')
        time.sleep(3)
        thing = [':hammer: ', ctx, ' has been banned.']
    else:
        thing = [':hammer: ', member.mention, ' has been banned.']
        x = ''.join(thing)
        await ctx.send(x)

@bot.command(help="Warns a member.")
async def warn(ctx, member : discord.Member, *, arg2):
    reasoning = ''.join(arg2)
    if member.name == 'Joe Bot':
        await ctx.send('no')
    else:
        thing = [':warning: ', member.mention, ' was warned for: ', reasoning]
        x = ''.join(thing)
        await ctx.send(x)
        print(member.mention," got warned for ",reasoning)

@bot.command(help="Kills a member.")
async def kill(ctx, member : discord.Member):
    if member.name == 'Joe Bot':
        await ctx.send('no')
    else:
        thing = [':knife: ', member.mention, ' has been killed.']
        x = ''.join(thing)
        await ctx.send(x)

@bot.command(help="Super bans a member.")
async def superban(ctx, member : discord.Member):
    if member.name == 'Joe Bot':
        await ctx.send('no')
    else:
        thing = [member.mention, ' is now SUPER BANNED. :thumbup: https://nintendohomebrew.com/assets/img/banned.gif']
        x = ''.join(thing)
        await ctx.send(x)

@bot.command(help="Takes away help from a member.")
async def takehelp(ctx, member : discord.Member):
        thing = [member.mention, ' can no longer access the help channels.']
        x = ''.join(thing)
        await ctx.send(x)
        print("I took help from", member.mention,".")

@bot.command(help="Displays information about the bot.", )
async def about(ctx):
    embed=discord.Embed(title="Joe Bot Testing",url="https://github.com/joshuavanderbilt/joebot-testing",description="This is a JOE bot, all hail Joe! Contributers: JoshuaMV.",color=0xFF5733)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1015749450544730204/5cd7886d908ad187abec6d3defc3c5bb.webp")
    await ctx.send(embed=embed)
    print("User called the about message.")

@bot.command(help="Sends a random image from the furry folder.")
async def furryfolder(ctx):
    furryfile = random.choice(os.listdir("./FURRY"))
    furrytable = ["./FURRY/",furryfile]
    furrysend = ''.join(furrytable)
    await ctx.send(file=discord.File(furrysend))
    print("I sent", furrysend, "from the ./FURRY directory.")

@bot.command(help="Sends a chosen image from the furry folder.")
async def pickfurry(ctx, *args):
    furryfile = ''.join(args)
    furrytable = ["./FURRY/",furryfile]
    furrysend = ''.join(furrytable)
    await ctx.send(file=discord.File(furrysend))
    print("I sent", furrysend, "from the ./FURRY directory.")

@bot.command(help="Downloads an image to the furry folder.")
async def wget(ctx, *args):
    arguments=' '.join(args)
    if "$" in arguments:
        print("! User tried to download file from URL with illegal characters.")
        await ctx.send("This URL contains characters you cannot use!")
        return
    if ".." in arguments:
        print("! User tried to download file from URL with illegal characters.")
        await ctx.send("This URL contains characters you cannot use!")
        return
    print("User is downloading",arguments,"to ./FURRY.")
    await ctx.send("Downloading to the furry folder.")
    wgettable = ["wget --directory-prefix ./FURRY"," ",arguments]
    os.system(''.join(wgettable))
    print("User downloaded",arguments,"to ./FURRY.")
    await ctx.send("Finished downloading to the furry folder.")

@bot.command(help="Lists the contents of the furry folder.")
async def ls(ctx):
    print("User is requesting the contents of the furry folder.")
    await ctx.send(''.join(["Furry Directory Listing: ( ",' )( '.join(os.listdir('./FURRY'))," )"]))

@bot.command(help="Renames a file in the furry folder.")
async def rename(ctx, arg1, arg2):
    source = ''.join(arg1)
    destination = ''.join(arg2)
    if "$" in source:
        print("! User tried to rename file with illegal characters.")
        await ctx.send("This original filename contains characters you cannot use!")
        return
    if "$" in destination:
        print("! User tried to rename file to name with illegal characters.")
        await ctx.send("This destination filename contains characters you cannot use!")
        return
    if ".." in destination:
        print("! User tried to rename file to name with illegal characters.")
        await ctx.send("This destination filename contains characters you cannot use!")
        return
    if ".." in source:
        print("! User tried to rename file with illegal characters.")
        await ctx.send("This original filename contains characters you cannot use!")
        return
    print("User is renaming",source,"to", destination,".")
    await ctx.send("Renaming file.")
    renametable = ["mv ","./FURRY/",source," ","./FURRY/",destination]
    os.system(''.join(renametable))
    await ctx.send("File renamed.")

# The command below requires the string library.

@bot.command(help="Sends a random LightShot image. (Use at your own risk!)")
async def lightshot(ctx):
    lslink = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    lstable = ["https://prnt.sc/", lslink]
    lssend = ''.join(lstable)
    await ctx.send(lssend)
    print("User generated this link from LightShot:", lssend)


@bot.command(help="Make the Joe Bot say what you want it to!")
async def say(ctx, *args):
    arguments = ' '.join(args)
    await ctx.send(arguments)
    print("I said '",arguments,"'.")

@bot.command(help="Birb image.")
async def birb(ctx):
    await ctx.send('https://files.catbox.moe/s1g67r.png')

@bot.command(help='Update the bot via GIT.')
async def update(ctx):
    print("User is going to update bot.")
    os.system("rm -rf ./update")
    os.system("mkdir ./update")
    Repo.clone_from("https://www.github.com/joshuavanderbilt/joebot-testing.git", "./update")
    os.system("mv ./update/the.py ./the.py")
    await ctx.send('Updating software, please type !restart after a few seconds.')
	
@bot.command(help='Restart the bot after updating')
async def restart(ctx):
	ctx.send('Restarting...')
	restartApp()

bot.run(str(token))
