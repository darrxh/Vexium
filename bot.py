import discord
from discord.ext import commands
from discord import FFmpegPCAudio
from dotenv import load_dotenv, dotenv_values, set_key
import os
import youtube_dl
global queue
queue = []

def append_queue(url):
    global queue
    queue.append(url)

def pop_queue():
    global queue
    if (len(queue) == 0):
        return ("Nothing in Queue!")
    queue.pop()

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

        @commands.command()
        async def join(self,ctx):
            if ctx.author.voice is None:
                await ctx.send("Not connected to Voice Channel.")
            voice_channel = ctx.author.voice.channel
            if ctx.voice_client is None:
                await voice_channel.connect()
            else:
                await ctx.voice_client.move_to(voice_channel)

        @commands.command()
        async def leave(self,ctx):
            await ctx.voice_client.disconnect()

        @commands.command()
        async def play(self,ctx,url):
            if (currently_playing()):
                append_queue(url)

            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            YDL_OPTIONS = {'format': 'bestaudio'}
            vc = ctx.voice_client

            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                url2 = info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)


                vc.play(source)

        @commands.command()
            await ctx.voice_client.pause()
        async def pause(self,ctx):
            await ctx.send("Paused ")

        @commands.command()
        async def resume(self, ctx):
            await ctx.voice_client.resume()
            await ctx.send("Resuming ")

def setup(client):
    client.add_cog(Music(client))


def change_prefix(new_prefix):
    if (len(new_prefix) > 1):
        return ("Prefix must be 1 character")
    global prefix
    prefix = new_prefix
    os.environ["PREFIX"] = prefix
    set_key(".env", "PREFIX", os.environ["PREFIX"])
    return (f"Prefix changed to '{prefix}'")4 N
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
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix="+", intents=intents)


@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio("")
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


async def on_message(message):
    global prefix
    if not (message.content.startswith(prefix)):
        return
    if message.author == client.user:
        return
    input = message.content.casefold()
    if (input.startswith(f"{prefix}prefix ")):
        await message.channel.send(change_prefix(input[(input.find(" ")+1):(len(input))]))
    elif (input.startswith(f"{prefix}jump")):
        jump_to_song()
    elif (input.startswith(f"{prefix}queue")):
        print_queue()

client.run(os.getenv("API_KEY"))
