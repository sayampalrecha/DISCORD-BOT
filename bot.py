# OTc4OTY2MDA1MjM5OTE4NjMy.G_f3_U.pbikmZX6GLW--Gfy5Va_geO4CTTq6XZad3HAfI

# bot for discord

# from http import client

import discord 
import os
client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as as {0.user}".format(client))
    
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startwith('$hello'):
        await message.channel.send('Hello!')
        
client.run(os.getenv('TOKEN'))
    
    
    
