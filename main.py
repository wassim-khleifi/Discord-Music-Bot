import discord
from discord.http import handle_message_parameters
from discord.ext import commands,tasks
from discord import File , ButtonStyle
from discord.ui import Button , View
import youtube_dl
########### IMPORT CONFIGS ##############
import config
from config import *
################################
import music
from music.system import *
########### BOT INTENTS AND PREFIX ##############
bot = commands.Bot(command_prefix= prefix, intents=discord.Intents.all())
############# BOT STATUS ###############
bot.remove_command("help")
@bot.event
async def on_command_error(ctx,error):
	if isinstance(error,commands.MissingPermissions):
		await ctx.reply("You Do Not Have Permissions To Use This Command!")
@bot.event
async def on_ready():
	await bot.change_presence(status=discord.Status.online , activity=discord.Game(f'Music | {prefix}help'))
	await bot.add_cog(Music(bot))
	print("bot is ready!")
bot.run(TOKEN)