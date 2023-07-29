import discord
from dotenv import load_dotenv, dotenv_values
import os

def change_prefix(new_prefix):
    if (len(new_prefix) > 1):
        return ("Prefix must be 1 character")
    global prefix
    prefix = new_prefix
    try:
        env_file = open(".env", "w")
    except FileNotFoundError:


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print('Ready!')

@client.event
async def on_message(message):
    global prefix
    if not (message.content.startswith(prefix)):
        return
    if message.author == client.user:
        return
    input = message.content.casefold()
    if (input.startswith(f"{prefix}prefix ")):
        await message.channel.send(change_prefix(input[8:(len(input))]))
    elif (input.startswith(f"{prefix}jump")):
        jump_to_song()
    elif (input.startswith(f"{prefix}skip")):
        skip_song()
    elif (input.startswith(f"{prefix}play")):
        play_song()
    elif (input.startswith(f"{prefix}stop")):
        stop_song()
    elif (input.startswith(f"{prefix}leave")):
        leave_channel()
    elif (input.startswith(f"{prefix}queue")):
        print_queue()



def load_key():
    try:
        key_file = open(".env","r")
    except FileNotFoundError:
        print ("No .env API key file given.")
        user_input = str(input("Please enter an API Key. For help or more information please refer to help.txt"))
        new_key_file = open(".env","x")
        new_key_file.write(f"API_KEY={user_input}\nPREFIX=+")
        new_key_file.close()
    finally:
        key_file.close()
        load_dotenv()

def init():
    global prefix
    global playlist
    prefix = os.getenv("PREFIX")
    playlist = []

def main():
    intents = discord.Intents.default()
    intents.message_content = True
    global prefix
    global playlist
    client = discord.Client(intents=intents)
    load_key()
    client.run(os.getenv("API_KEY"))

def test():


if __name__ == '__main__':
    test()