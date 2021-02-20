#Import Discord package
import discord

#Token
from tokens import token

# Client
client = discord.Client()

#Functions

@client.event
async def on_ready():
    configChanID=812579716161994802
    configChan=client.get_channel(configChanID)
    await configChan.send('Hola zorras!')

@client.event
async def on_message(message):
    if message.content =='version':
        configChanID=812579716161994802
        configChan=client.get_channel(configChanID)
        emb=discord.Embed(title="Current Version", description="Version of the bot is 1.0", color=0x00ff00)
        emb.add_field(name="Version Code:", value="v1.0.0", inline=False)
        emb.add_field(name="Date Released:", value="20/02/21", inline=False)
        emb.set_footer(text="Version")
        emb.set_author(name="Ruben Romero")
        await configChan.send(embed=emb)
    
@client.event 
async def on_disconnect():
    configChanID=812579716161994802
    configChan=client.get_channel(configChanID)
    await configChan.send('Aios perras')


#Run client 
client.run(token)
