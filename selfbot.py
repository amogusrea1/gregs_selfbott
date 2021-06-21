import os
import threading
import time
import sys
import subprocess

try:
    from win10toast import ToastNotifier
except:
    os.system("pip install win10toast")
    from win10toast import ToastNotifier

try:
    from colorama import init, Fore, Back, Style
except:
    os.system("pip install colorama")
    from colorama import init, Fore, Back, Style

try:
    from halo import Halo
except:
    os.system("pip install halo")
    from halo import Halo

try:
    import random
except:
    os.system("pip install random")
    import random

try:
    import discord
except:
    os.system("pip install discord")
    import discord

try:
    import nekos
except:
    os.system("pip install nekos.py")
    import nekos


import discord, json, pyfiglet, requests, aiohttp
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import io


os.system("cls")
os.system("mode 121,30")
os.system("title greg's Selfbot")
#Setup
try:
    
    os.system('cls')
    time.sleep(4)
    with open("config.txt") as setup:
        setup = setup.readlines()
        token = setup[0].replace('"',"").replace("TOKEN=","")
        prefix = setup[1].replace('"',"").replace("PREFIX=","")
        nitrosnipe = setup[2].replace('"',"").replace("NITRO-SNIPE=","")
        nitrosniping = nitrosnipe.strip().lower()
        client = commands.Bot(prefix.strip(), self_bot=True)
        guilds = len(client.guilds)
        users = len(client.users)


        


except Exception as error:
    print(f" | Did you extract me properly? Did you delete/rename config.txt? I can't access it\n | Error : {error}\n | (Tip: use apps like:winrar, 7-zip)")
    time.sleep(5)
    os._exit(0)

@client.event
async def on_ready():
       await client.wait_until_ready()
       print(
            f"""{Fore.GREEN}

░██████╗░██████╗░███████╗░██████╗░██╗░██████╗  ░██████╗███████╗██╗░░░░░███████╗██████╗░░█████╗░████████╗░░░
██╔════╝░██╔══██╗██╔════╝██╔════╝░╚█║██╔════╝  ██╔════╝██╔════╝██║░░░░░██╔════╝██╔══██╗██╔══██╗╚══██╔══╝░░░
██║░░██╗░██████╔╝█████╗░░██║░░██╗░░╚╝╚█████╗░  ╚█████╗░█████╗░░██║░░░░░█████╗░░██████╦╝██║░░██║░░░██║░░░░░░ (type !cmds)
██║░░╚██╗██╔══██╗██╔══╝░░██║░░╚██╗░░░░╚═══██╗  ░╚═══██╗██╔══╝░░██║░░░░░██╔══╝░░██╔══██╗██║░░██║░░░██║░░░░░░
╚██████╔╝██║░░██║███████╗╚██████╔╝░░░██████╔╝  ██████╔╝███████╗███████╗██║░░░░░██████╦╝╚█████╔╝░░░██║░░░██╗
░╚═════╝░╚═╝░░╚═╝╚══════╝░╚═════╝░░░░╚═════╝░  ╚═════╝░╚══════╝╚══════╝╚═╝░░░░░╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝ 
                                greg's selfbot   
if prefix ! doesnt work the open config.txt      
{Fore.GREEN}logged in as:{Fore.RESET}{client.user.name}#{client.user.discriminator}                          
{Fore.LIGHTMAGENTA_EX}premium type(nitro):{Fore.RESET}{client.user.premium_type}
{Fore.GREEN}Servers: {Fore.RESET}{guilds}
{Fore.GREEN}token uwu: {Fore.RESET}{token}
                                                                                        
"""
)

@client.command()
async def cmds(ctx, msg: str = None):
    await ctx.message.delete()
    await ctx.send(embed = discord.Embed(description = "https://panteleevgrigorij1234.gitbook.io/greg-s-selfbot/"))
    await ctx.send(embed = discord.Embed(description = "or: https://selfbot-company.gitbook.io/greg-s-selfbot/"))


@client.command()
async def flip(ctx, msg: str = None):
    await ctx.message.delete()
    await ctx.send(embed = discord.Embed(description = "(╯°□°）╯︵ ┻━┻"))

@client.command()
async def pew(ctx, msg: str = None):
    await ctx.message.delete()
    await ctx.send(embed = discord.Embed(description = "(   ' - ')>---------- pew pew"))

@client.command()
async def cookie(ctx, msg: str = None):
    await ctx.message.delete()
    await ctx.send(embed = discord.Embed(description = "(  ' - ')-🍪"))



@client.command()
async def wasted(ctx, member: discord.Member=None):
  if not member:
    member = ctx.author
          
  wastedsession = aiohttp.ClientSession()
  async with wastedsession.get(f"https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url_as(format='png')}") as img:
    if img.status != 200:
      await ctx.send("Unable to get image")
      await wastedsession.close()      
    else:
      data = io.BytesIO(await img.read())
      await ctx.send(file=discord.File(data, 'wasted.png'))
      await wastedsession.close()

@client.command()
async def jail(ctx, member: discord.Member=None):
  if not member:
    member = ctx.author
          
  jailsession = aiohttp.ClientSession()
  async with jailsession.get(f"https://some-random-api.ml/canvas/jail?avatar={member.avatar_url_as(format='png')}") as img:
    if img.status != 200:
      await ctx.send("Unable to get image")
      await jailsession.close()      
    else:
      data = io.BytesIO(await img.read())
      await ctx.send(file=discord.File(data, 'jail.png'))
      await jailsession.close()

@client.command()
async def credityt(ctx, member: discord.Member=None):
  if not member:
    member = ctx.author
          
  creditytsession = aiohttp.ClientSession()
  async with creditytsession.get(f"https://some-random-api.ml/canvas/youtube-comment?avatar={member.avatar_url_as(format='png')}&comment=Hello! This self bot is kinda cool! Made by:&username=") as img:
    if img.status != 200:
      await ctx.send("Unable to get image")
      await creditytsession.close()      
    else:
      data = io.BytesIO(await img.read())
      await ctx.send(file=discord.File(data, 'respect.png'))
      await creditytsession.close()

@client.command(aliases=['doggo', 'doggie'])
async def dog(ctx):
	"""Cute doggo pics 🐕. Example: dog"""
	await ctx.trigger_typing()

	dogimgsession = aiohttp.ClientSession()
	dogresp = await dogimgsession.get('https://some-random-api.ml/img/dog')
	dogimg = json.loads(await dogresp.text())

	embed = discord.Embed()
	embed.set_image(url=(str(dogimg['link'])))

@client.command(aliases=['shibe'])
async def shiba(ctx):

	await ctx.trigger_typing()

	dogimgsession = aiohttp.ClientSession()
	dogresp = await dogimgsession.get('http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=false')
	dogimg = json.loads(await dogresp.text())

	embed = discord.Embed()
	embed.set_image(url=(str(dogimg)))

	await dogimgsession.close()

	await ctx.reply(embed=embed)

@client.command()
async def invert(ctx, member: discord.Member=None):
  if not member:
    member = ctx.author
          
  insession = aiohttp.ClientSession()
  async with insession.get(f"https://some-random-api.ml/canvas/invert?avatar={member.avatar_url_as(format='png')}") as img:
    if img.status != 200:
      await ctx.send("Unable to get image")
      await insession.close()      
    else:
      data = io.BytesIO(await img.read())
      await ctx.send(file=discord.File(data, 'bɘtɿɘvni.png'))
      await insession.close()

@client.command()
async def pixelate(ctx, member: discord.Member=None):
  if not member:
    member = ctx.author
          
  pisession = aiohttp.ClientSession()
  async with pisession.get(f"https://some-random-api.ml/canvas/pixelate?avatar={member.avatar_url_as(format='png')}") as img:
    if img.status != 200:
      await ctx.send("Unable to get image")
      await pisession.close()      
    else:
      data = io.BytesIO(await img.read())
      await ctx.send(file=discord.File(data, 'bɘtɿɘvni.png'))
      await pisession.close()

@client.command(aliases=['channelnuke','nukechannel',])
async def nuke(ctx):

    channel_position = ctx.channel.position
    new_chan = await ctx.channel.clone()
    await ctx.channel.delete()
    await new_chan.edit(position = channel_position) 
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Channel Nuked", description=f"<#{new_chan.id}> - {new_chan.name} has been nuked", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/dKfTyqLt1jkqIfiMXj/giphy.gif")
    embed.set_footer(text="))))")
    await new_chan.send(embed=embed)

def nooooourrolesgotnukedomg(idofguild,nameofchan):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        randcolor = random.randint(0x000000, 0xFFFFFF)
        make = requests.post(f"https://discord.com/api/v8/guilds/{idofguild}/roles",headers=headers,json={"name":nameofchan,"permissions":"2251804225","color":randcolor,"mentionable":"true"})
    except:
        pass

@client.command(aliases=['spamrole', 'rolefuck',"fuckrole","fuckroles","rolesfuck","nukeroles","rolenuke"])
async def rolespam(ctx,amountofthemtomake=None,*,nameofthem=None):
    await ctx.message.delete()
    if nameofthem == None:
        nameofthem = "ngl this server fucking sucks lol"

    if amountofthemtomake == None:
        amountofthemtomake = 50
    for i in range(int(amountofthemtomake)):
        threading.Thread(target = nooooourrolesgotnukedomg, args = (ctx.guild.id,nameofthem,)).start()

@client.command(aliases=['asci','cooltext',])
async def ascii(ctx, *,paste=f"Format is {prefix.strip()}ascii [text]"):

    if paste == f"Format is {prefix.strip()}ascii [text]":
        await ctx.message.edit(content=paste)
    else:
        finaltext = paste.replace(" ", "+")
        asciiresponse = requests.get(f"http://artii.herokuapp.com/make?text={finaltext}&font=rounded") 
        await ctx.message.edit(content=f" ``` {asciiresponse.text} ``` ")

@client.command(aliases=['haste','paste'])
async def hastebin(ctx, *,paste=f"Format is {prefix.strip()}hastebin [text]"):
    try:
        data = requests.post(f"https://hastebin.com/documents",timeout=3,data=paste).text
        textlink = "https://hastebin.com/"      
    except:  #hastebin is often used so much, using the except i can use a similar reliable service
        await ctx.message.edit(content=f"_https://hastebin.com/documents is having problems - switching to https://paste.pythondiscord.com/documents_")
        await asyncio.sleep(1)
        data = requests.post(f"https://paste.pythondiscord.com/documents",data=paste).text
        textlink = "https://paste.pythondiscord.com/"

    j = json.loads(data)
    endoflink = j['key']

    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="greg's Selfbot - Hastebin", description=f"Here's your paste!\n{textlink}{endoflink}", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/dKfTyqLt1jkqIfiMXj/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)

def nooooourchannelsgotnukedomg(idofguild,nameofchan):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        req = requests.post(f"https://canary.discord.com/api/v8/guilds/{idofguild}/channels",headers=headers,json={"type":"0","name":nameofchan})
    except:
        pass

@client.command(aliases=['textchannelcreation', 'textchannelnuke',"channelspam","nuketextchannels","channelsspam"])
async def nuketextchannel(ctx,amountofthemtomake=None,*,nameofthem=None):
    await ctx.message.delete()
    if nameofthem == None:
        nameofthem = "github.com/spaghettilord945/Gregs_selfbot"
    else:
        nameofthem = nameofthem.replace(" ","-")

    if amountofthemtomake == None:
        amountofthemtomake = 200
    for i in range(int(amountofthemtomake)):
        threading.Thread(target = nooooourchannelsgotnukedomg, args = (ctx.guild.id,nameofthem,)).start()

@client.command(aliases=["serverinformation","infoserver"])
async def serverinfo(ctx):
    await ctx.message.delete()

    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title=f"gregs selfbot - Getting info on {ctx.guild.name}", description="...", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/spaghettilord945/Gregs_selfbot")
    message = await ctx.send(embed=embed)
    await asyncio.sleep(1)
    try:
        boostlevel = ctx.guild.premium_tier
    except:
        boostlevel = "Error"
    try:
        boostcount = ctx.guild.premium_subscription_count
    except:
        boostcount = "Error"
    try:

        roles = len(ctx.guild.roles)
    except:
        roles = "Error"
    
    try:
        cate = len(ctx.guild.categories)
    except:
        cate = "Error"
    
    try:
        chanel = len(ctx.guild.channels)
    except:
        chanel = "Error"
    try:

        textchans = len(ctx.guild.text_channels)
    except:
        textchans = "Error"

    try:
        vcchans = len(ctx.guild.voice_channels)
    except:
        vcchans = "Error"
    try:

        users = ctx.guild.member_count
    except:
        users = "Error"

    try:
        onlineusers = sum(member.status==discord.Status.online and not member.bot for member in ctx.guild.members)
    except:
        onlineusers = "Error"
    try:
        offlineusers = sum(member.status==discord.Status.offline and not member.bot for member in ctx.guild.members)
    except:
        offlineusers = "Error"
    try:
   
        humans = sum(not member.bot for member in ctx.guild.members)
    except:
        humans = "Error"

    try:
  
        bots = sum(member.bot for member in ctx.guild.members)
    except:
        bots = "Error"
    
    info = f"""
`Boost Count` ```{boostcount}```
`Server Boost Level` ```{boostlevel}```
`Role Count` ```{roles}```
`Category Count` ```{cate}```
`Total Channel Count` ```{chanel}```
`Text Channel Count` ```{textchans}```
`Voice Channel Count` ```{vcchans}```
`Total Member Count` ```{users}```
"""

    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title=f"gregs Selfbot - {ctx.guild.name}", description=info, color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/spaghettilord945/Gregs_selfbot")
    await message.edit(embed=embed)

@client.command(aliases=['nitrosniper', 'snipenitro'])
async def nitrosnipe(ctx,snipestatus=None):
    global nitrosniping 
    if snipestatus == None:
        if nitrosniping == "off":
            nitrosniping = "on"
        elif nitrosniping == "on":
            nitrosniping = "off"
    else:
        if snipestatus.lower() == "off":
            nitrosniping = "off"
        if snipestatus.lower() == "on":
            nitrosniping = "on"

        if snipestatus.lower() == "true":
            nitrosniping = "on"
        if snipestatus.lower() == "false":
            nitrosniping = "off"

    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Nitro Sniper", description=f"Nitro sniper is now : `{nitrosniping}`", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)

@client.command(aliases=['fuck'])
async def hentai(ctx, user: discord.User = None):
        await ctx.message.delete()
        api = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
        json = api.json()
        msg = discord.Embed(description=user.mention + " This could be you and me ")
        msg.set_image(url=json['url'])
        
        await ctx.send(embed=msg)


client.run(token.strip(), bot=False)