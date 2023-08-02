import discord
from discord.ext import commands
from dotenv import load_dotenv, dotenv_values, set_key
import os


def change_prefix(new_prefix):
    if (len(new_prefix) > 1):
        return ("Prefix must be 1 character")
    global prefix
    prefix = new_prefix
    os.environ["PREFIX"] = prefix
    set_key(".env", "PREFIX", os.environ["PREFIX"])
    return (f"Prefix changed to '{prefix}'")

def load_key():
    try:
        key_file = open(".env","r")
    except FileNotFoundError:
        print ("No .env API key file given.")
        user_input = str(input("Please enter an API Key. For help or more information please refer to Documentation."))
        new_key_file = open(".env","x")
        new_key_file.write(f"API_KEY={user_input}\nPREFIX=+")
        new_key_file.close()
    finally:
        key_file.close()
        load_dotenv()

def set_prefix():
    global prefix
    prefix = os.getenv("PREFIX")
    if (len(prefix) > 1):
        print ("Prefix must be 1 character. Check .env file before starting.")
        return False
    return True


global prefix
global playlist
load_key()
set_prefix()
client = commands.Bot(command_prefix=prefix, intents=discord.Intents.default())

@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You must be in a voice channel to run this command!")

@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("I can't leave a voice channel if I'm not in one!")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print('Ready!')

@client.command()
async def prefix(ctx):
    await message.channel.send(change_prefix(input[(input.find(" ") + 1):(len(input))]))


"""
async def on_message(message):
    global prefix
    if not (message.content.startswith(prefix)):
        return
    if message.author == client.user:
        return
    input = message.content.casefold()
    if (input.startswith(f"{prefix}prefix ")):
        await message.channel.send(change_prefix(input[(input.find(" ")+1):(len(input))]))
    elif (input.startswith(f"{prefix}play")):
        play_song()
    elif (input.startswith(f"{prefix}stop")):
        stop_song()
    elif (input.startswith(f"{prefix}join")):
        channel = message.author.voice.channel
        await connect(channel)
    elif (input.startswith(f"{prefix}leave")):
        if not discord.VoiceClient.is_connected():
            await message.channel.send("Not connected to Voice Channel.")
            return
        await discord.VoiceClient.disconnect()
    elif (input.startswith(f"{prefix}skip")):
        skip_song()
    elif (input.startswith(f"{prefix}jump")):
        jump_to_song()
    elif (input.startswith(f"{prefix}queue")):
        print_queue()
"""
client.run(os.getenv("API_KEY"))
