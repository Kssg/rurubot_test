import discord
from discord.ext import commands
# 熊熊出現了
from core.classes import Cog_Extension
from datetime import datetime, timezone, timedelta


# 這樣繼承有三個
class Main(Cog_Extension):

    # 下面有參數，ctx:context，(使用者、ID、伺服器、頻道)
    # 這邊都成 commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'pong! {round(self.bot.latency*1000)} (ms)')

    @commands.command()
    async def meow(self, ctx):
        await ctx.send('Meow! Meow!')

    @commands.command()
    async def embed(self, ctx):

        dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
        dt2 = dt1.astimezone(timezone(timedelta(hours=8)))

        embed = discord.Embed(title="Meow", url="https://danbooru.donmai.us/",
                              description="meow meow~", color=0x2a61cf,
                              timestamp=dt2)
        embed.set_author(name="SHIRE", url="https://danbooru.donmai.us/posts/5103328",
                         icon_url="https://cdn.donmai.us/sample/67/72/__original_drawn_by_kensight328__sample-6772160be1da5827ce163388ce3ca074.jpg")
        embed.set_thumbnail(
            url="https://cdn.donmai.us/sample/35/1f/__nagae_iku_touhou_drawn_by_sei_kaien_kien__sample-351fc1aadb1a8a751333ec8ab8ce52c1.jpg")
        embed.add_field(name="1", value="11", inline=True)
        embed.add_field(name="2", value="22", inline=True)
        embed.add_field(name="3", value="33", inline=False)
        embed.add_field(name="4", value="44", inline=False)
        embed.set_footer(text="wow meow~")
        await ctx.send(embed=embed)

    #　有好幾個 arg，就是只傳給他
    @commands.command()
    async def said(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    # 原來註解是有用的，會自己轉
    @commands.command()
    async def clean(self, ctx, num: int):
        await ctx.channel.purge(limit=num+1)

# 註冊 Cog
# 運行 bot 會呼叫 setup，傳入主文件的 bot

def setup(bot):
    bot.add_cog(Main(bot))
