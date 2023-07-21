import discord
from dotenv import load_dotenv, dotenv_values
import os


client = discord.Client()
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
global prefix




def change_prefix(new_prefix):
    global prefix
    prefix = new_prefix

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print('Ready!')

@client.event
async def on_message(message):
    global prefix
    if message.author == client.user:
        return
    input = message.content.casefold()
    if (input.startswith(f"{prefix}prefix")):

        await message.channel.send('hello!')


    elif (msg.startswith('$superuser')):


def load_key():
    try:
        key_file = open(".env","r")
    except FileNotFoundError:
        print ("No .env API key file given.")
        user_input = str(input("Please enter an API Key. For help or more information please refer to help.txt"))
        new_key_file = open(".env","x")
        new_key_file.write(f"API_KEY:{user_input}")
        new_key_file.close()
    finally:
        key_file.close()
        load_dotenv()

load_key()
client.run(os.getenv("API_KEY"))

