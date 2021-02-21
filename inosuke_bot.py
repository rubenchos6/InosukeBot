#Discord
import discord
from discord.ext import commands
import pandas as pd
import random

#Token
from tokens import token

# Client
client = commands.Bot(command_prefix='%')

#Functions

#Commands
@client.command(name='version')
async def version(context):
    emb=discord.Embed(title="Current Version", description="Version of the bot is 1.0", color=0x00ff00)
    emb.add_field(name="Version Code:", value="v1.0.1", inline=False)
    emb.add_field(name="Date Released:", value="20/02/21", inline=False)
    emb.set_footer(text="Version")
    emb.set_author(name="Ruben Romero")
    await context.message.channel.send(embed=emb)

@client.command(name='kick', pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(context, member: discord.Member):
    await member.kick()
    await context.send('User '+member.display_name+ 'has been kicked')

@client.command(name='ban', pass_context=True)
@commands.has_permissions(kick_members=True)
async def ban(context, member: discord.Member, *, reason=None):
    await member.ban()
    await context.send('User '+member.display_name+ 'has been banned')

@client.command(name='dm')
async def dm(context):
    await context.message.author.send("Hi! Did you ask for a DM?")

    #myID=686620827717730384
    #await context.message.channel.send(context.message.author.id)
    #if(context.message.author.id==myID):
    
    #else:
    #    await context.message.author.send("U are not an Admin")
@client.command(name='img')
async def img(context):
    await context.channel.send(file=discord.File("InosukeBot/santiago.jpeg"))

#Events
@client.event
async def on_ready():
    configChanID=812579716161994802
    configChan=client.get_channel(configChanID)
    await configChan.send('Hola zorras!')
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('Fcking around'))
    
    #df = pd.DataFrame({"A":['Hello','Test']})
    #df.to_csv('C:/Users/ruben/Documents/Inosuke Bot/InosukeBot/data.csv')


@client.event
async def on_message(message):
    if message.author.id==725560073266659351:
        await message.channel.send(file=discord.File("InosukeBot/santiago.jpeg"))
    
    if message.content == 'Append':
        df = pd.read_csv('C:/Users/ruben/Documents/Inosuke Bot/InosukeBot/data.csv',index_col=0)
        df=df.append({"A": 'New message to append'}, ignore_index=True)
        df.to_csv('C:/Users/ruben/Documents/Inosuke Bot/InosukeBot/data.csv')

    await client.process_commands(message)

@client.event 
async def on_disconnect():
    configChanID=812579716161994802
    configChan=client.get_channel(configChanID)
    await configChan.send('Aios perras')


#Run client 
client.run(token)
