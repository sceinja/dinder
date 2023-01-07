import nextcord
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("qirsh_token")

client = nextcord.Client(intents=nextcord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user} is ready')


client.run(token)