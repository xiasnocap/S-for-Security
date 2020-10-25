import discord
from discord.ext import commands, tasks
import random
import youtube_dl
import asyncio



TOKEN = 'token of the bot'
bot = commands.Bot(command_prefix = "$", description = "SECURITY LVL:\n1\n2\n3\n4\n5\n6 ")
bot.remove_command('help')

@bot.event
async def on_ready():
	print("Ready !")

#status

status = ["$help"]

@bot.event
async def on_ready():
	print("Ready !")

###################################################
##########   HELP   ##############################
###################################################



#$help
@bot.command()
async def help(ctx):
	await ctx.send("I don't make it")
	
#$invite
@bot.command()
async def invite(ctx):
	await ctx.send("https://discord.com/api/oauth2/authorize?client_id=769915966468390922&permissions=8&scope=bot")

###################################################
##########   LVL 1   ###########################
###################################################

#$clear
@bot.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, nombre : int):
	messages = await ctx.channel.history(limit = nombre + 1).flatten()
	for message in messages:
		await message.delete()



#$purge
@bot.command()
@commands.has_permissions(manage_messages = True)

async def purge(ctx):
	await ctx.channel.purge()

###################################################
##########   LVL 2   ###########################
###################################################




bot.run(TOKEN)
