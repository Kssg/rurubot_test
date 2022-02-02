import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json', 'r', encoding='utf8') as f:
    jdata = json.load(f)


class React(Cog_Extension):

    @commands.command()
    async def img(ctx):
        pic = discord.File(jdata['pic'][0])
        await ctx.send(file=pic)

    @commands.command()
    async def ranimg(ctx):
        ranimg = random.choice(jdata['pic'])
        pic = discord.File(ranimg)
        await ctx.send(file=pic)

    @commands.command()
    async def urlimg(ctx):
        ranimg = random.choice(jdata['url_pic'])
        # 網址可直接傳送
        await ctx.send(ranimg)


def setup(bot):
    bot.add_cog(React(bot))
