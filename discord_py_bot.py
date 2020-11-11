import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv('./discord_py_env.env')
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix = '!')


@client.event
async def on_ready():
	print("Wilbebot is kind of working maybe. . . ")


@client.event
async def on_member_join(member):
	name = member.name.split("#")
	channel =  client.get_channel(397255918095564810)
	await channel.send(f"{name} has appeared as if from nowhere!")


@client.event
async def on_member_remove(member):
	name = member.name.split("#")
	channel = client.get_channel(397255918095564810)
	await channel.send(f"{name} has succombed to sadness, and jettisoned themself through the airlock.")


@client.command()
async def ping(ctx):
	await ctx.send(f'{round(client.latency * 1000)}ms')


@client.command()
async def whatsmyname(ctx):
	channel = client.get_channel(ctx.channel.id)
	name = ctx.message.author.name
	await channel.send(f"Your name is \"{name}\" you idiot.")


client.run(TOKEN)
