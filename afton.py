import os
import discord



TOKEN = os.getenv('TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'afton':
        await message.channel.send('https://i.redd.it/j3fv1j5csmm11.gif')
    if message.content == 'its been so long' or 'dance' or 'man behind the slaughter':
        await message.channel.send('https://th.bing.com/th/id/R.1e24a57314d65203bb344b5091c58a61?rik=Q4igy%2fgzBoV2TQ&pid=ImgRaw&r=0')
    if message.content == 'hi' or 'hello':
        await message.channel.send('are you a kid? just wondering')

client.run('OTU3MjkwMTk5Njk4NzY3ODgz.Yj8n-Q.YrxRyswZTQRi6am6mC8J773lJl0')
