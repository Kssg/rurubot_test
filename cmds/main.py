import discord
from discord.ext import commands
# 熊熊出現了
from core.classes import Cog_Extension

# 繼承喔


class Main(Cog_Extension):

    # 下面有參數，ctx:context，(使用者、ID、伺服器、頻道)
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'pong! {round(self.bot.latency*1000)} (ms)')

    @commands.command()
    async def meow(self, ctx):
        await ctx.send('Meow! Meow!')

# 想想
# setup 就長這樣，還有 Class


def setup(bot):
    bot.add_cog(Main(bot))
