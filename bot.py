import discord
from discord.ext import commands, tasks
import random
import youtube_dl
import asyncio



TOKEN = 'token'
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

##################################################
##########   HELP   ##############################
##################################################



#$help
@bot.command()
async def help(ctx):
	await ctx.send("I don't make it")
	
#$invite
@bot.command()
async def invite(ctx):
	await ctx.send("https://discord.com/api/oauth2/authorize?client_id=769915966468390922&permissions=8&scope=bot")

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


#$mute
@bot.command()
@commands.has_permissions(manage_messages = True)
async def mute(ctx, member: discord.Member):
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await bot.say(embed=embed)

#$kick
@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.kick(user, reason = reason)
	embed=discord.Embed(title="KICK", description="user as been kicked succesfully")
	embed.set_thumbnail(url="https://media.tenor.com/images/27f16871c55a3376fa4bfdd76ac2ab5c/tenor.gif")
	await ctx.send(embed=embed)

#$ban
@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.ban(user, reason = reason)
	embed=discord.Embed(title="BAN", description="user as been banned succesfully")
	embed.set_thumbnail(url="https://i.imgur.com/azCR8D1.gif")
	await ctx.send(embed=embed)

#$unban

#$warn



bot.run(TOKEN)
