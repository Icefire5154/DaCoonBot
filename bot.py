import discord
import random
import time
import asyncio
import shitposts

TOKEN = "OTc0Mzk2NDA5MzA4NjYzODY4.G4C8H8.cefBpn4Enj8yTYUJKp8VBmjISfjTKizJkUOuwE"

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("&help"):
        await message.channel.send("Have you tried sucking?")

    if message.content.startswith("&Wyatt"):
        wyattNuts = 0
        wyattNuts = wyattNuts + 1
        wyattDeezNuts = ("We have reached ", wyattNuts, " Deez Nuts jokes")
        await message.channel.send(wyattDeezNuts)
        await message.delete()      #will delete the "&Wyatt"

    if message.content.startswith("&say"):
        mes = message.content.split()
        output = ""
        for word in mes[1:]:
            output += word
            output += " "
        await message.channel.send(output)
        await message.delete()

    if message.content.startswith("&shitpost"):
        await message.channel.send(random.choice(shitposts.photos))

    if message.content.startswith("&addshitpost"):
        channel = message.channel
        await channel.send("Link your shitpost")

        msg = await client.wait_for('message', check=None)
        shitposts.photos.append(msg)
        
        # new code - adding 5/26 - designed to test out working with a text file - work with the console then figure out how to transfer to discord
        
        channel = message.channel
        await channel.send("Link your shitpost"):
            msg = await client.wait_for('message', check=None)
            file = open('photos.txt', 'w')
            file.write(msg)
            file.close()
         
        channel = message.channel
        await channel.send(msg, " added to shitposts")
        
        #I think this will work - will have to change the regular shitpost command to take from the photos.txt instead of 'shitposts.photos'
        #file = open('helloworld.txt','r') for file.read
        #f = open('helloworld.txt','a') for file.append


@client.event
async def on_ready():
    print("We online bois")

client.run(TOKEN)
