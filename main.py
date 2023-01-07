import nextcord
import os 
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("token")
client = nextcord.Client(intents=nextcord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user} is on!')

client.command_prefix = '!'

@client.slash_command(
    name="invite",
    description="Retrieve an Invite to Dinder's Official Server!",
    guild_ids=[],
)
async def invite(inter: nextcord.Interaction) -> None:
    await inter.response.send_message("Join our official Discord! \nhttps://discord.gg/HCjNSd3ZYK")

client.run(token)
