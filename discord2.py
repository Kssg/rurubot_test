from ast import AsyncFunctionDef
import discord
from discord.ext import commands
import json

with open('setting.json', 'r', encoding='utf8') as f:
    jdata = json.load(f)

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(">> Bot is online. <<")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel('938012080760565770')
    await channel.send(f'{member} join!')


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel('938012126470086666')
    await channel.send(f'{member} leave!')

# 下面有參數，ctx:context，(使用者、ID、伺服器、頻道)


@bot.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(bot.latency*1000)} (ms)')

bot.run(jdata['TOKEN'])
