import discord
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print('Ready!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content.lower()
    if (msg.startswith('$hello')):
        await message.channel.send('Hello!')

    elif (msg.startswith('$superuser')):

client.run(token)