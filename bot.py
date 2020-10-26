import discord
from discord.ext import commands, tasks
import random
import youtube_dl
import asyncio



TOKEN = 'NzY5OTE1OTY2NDY4MzkwOTIy.X5V-Hg.L_MVAdX6xcI78dWqek0guIxPPrg'
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
	embed = discord.Embed(title = "**KICK**", url = "https://discord.gg/EN9sv4d")
	embed.set_thumbnail(url = "https://media1.tenor.com/images/25715a5aea4f0c70057ede6e05a6472d/tenor.gif?itemid=13461094")
	embed.add_field(name = "Kicked Member", value = user.name, inline = True)
	embed.add_field(name = "Reason", value = reason, inline = True)
	embed.add_field(name = "Moderator", value = ctx.author.name, inline = True)
	await ctx.send(embed = embed)

#$ban
@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.ban(user, reason = reason)
	embed = discord.Embed(title = "**BANNED**", description = " **ENJOY :wink: **", url = "https://discord.gg/EN9sv4d")
	embed.set_thumbnail(url = "https://media1.tenor.com/images/d856e0e0055af0d726ed9e472a3e9737/tenor.gif?itemid=8540509")
	embed.add_field(name = "Ban Member", value = user.name, inline = True)
	embed.add_field(name = "Reason", value = reason, inline = True)
	embed.add_field(name = "Moderator", value = ctx.author.name, inline = True)
	await ctx.send(embed = embed)

#$unban

@bot.command()
async def unban(ctx, user, *reason):
	reason = " ".join(reason)
	userName, userId = user.split("#")
	bannedUsers = await ctx.guild.bans()
	for i in bannedUsers:
		if i.user.name == userName and i.user.discriminator == userId:
			await ctx.guild.unban(i.user, reason = reason)
			await ctx.send(f"{user} is now  unban.")
			return
	#Ici on sait que lutilisateur na pas ete trouvé
	await ctx.send(f"The user {user} is not ban")


#$warn



bot.run(TOKEN)
