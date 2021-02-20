#Discord
import discord
from discord.ext import commands

#Token
from tokens import token

# Client
client = commands.Bot(command_prefix='%')

#Functions

@client.command(name='version')
async def version(context):
    emb=discord.Embed(title="Current Version", description="Version of the bot is 1.0", color=0x00ff00)
    emb.add_field(name="Version Code:", value="v1.0.1", inline=False)
    emb.add_field(name="Date Released:", value="20/02/21", inline=False)
    emb.set_footer(text="Version")
    emb.set_author(name="Ruben Romero")
    await context.message.channel.send(embed=emb)

@client.command(name='dm')
async def dm(context):
    await context.message.author.send("Hi! Did you ask for a DM?")

    #myID=686620827717730384
    #await context.message.channel.send(context.message.author.id)
    #if(context.message.author.id==myID):
    
    #else:
    #    await context.message.author.send("U are not an Admin")

@client.event
async def on_ready():
    configChanID=812579716161994802
    configChan=client.get_channel(configChanID)
    await configChan.send('Hola zorras!')
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('Fcking around'))

@client.event
async def on_message(message):
    if message.content =='version':
        configChanID=812579716161994802
        configChan=client.get_channel(configChanID)
        emb=discord.Embed(title="Current Version", description="Version of the bot is 1.0", color=0x00ff00)
        emb.add_field(name="Version Code:", value="v1.0.1", inline=False)
        emb.add_field(name="Date Released:", value="20/02/21", inline=False)
        emb.set_footer(text="Version")
        emb.set_author(name="Ruben Romero")
        await configChan.send(embed=emb)
    if message.content == 'DM':
        await message.author.send("Hi! Did you ask for a DM?")
    await client.process_commands(message)

@client.event 
async def on_disconnect():
    configChanID=812579716161994802
    configChan=client.get_channel(configChanID)
    await configChan.send('Aios perras')


#Run client 
client.run(token)
