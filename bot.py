import discord
from discord.ext import commands

TOKEN = ''
client = commands.Bot(command_prefix = '!')
client.remove_command('help')

@client.event
async def on_ready():
	print('Bot is ready!')

#@commands.is_owner() # Only you can nuke.
@commands.has_permissions(administrator=True) # Admins (including you) can nuke.
@client.command(pass_context=True)
async def nuke(ctx):
	channel = await ctx.channel.clone()
	await ctx.channel.delete()
	await channel.send(':ok_hand:  Nuked this channel.\nhttps://imgur.com/LIyGeCR')

client.run(TOKEN)
