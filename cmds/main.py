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
        embed=discord.Embed(title="Test", url="https://danbooru.donmai.us/", description="how to use", color=0xe31616, timestamp=dt2)
        embed.set_author(name="SHARO", url="https://danbooru.donmai.us/posts/5389251?q=gochuumon_wa_usagi_desu_ka%3F", icon_url="https://cdn.donmai.us/original/f7/4b/__kirima_syaro_gochuumon_wa_usagi_desu_ka_drawn_by_mitya__f74b5d5d9a77e595c4405fb71344fa25.png")
        embed.set_thumbnail(url="https://cdn.donmai.us/sample/db/71/__kirima_syaro_gochuumon_wa_usagi_desu_ka_drawn_by_mozukun43__sample-db710a75026e748d69a77a2b3509837f.jpg")
        embed.add_field(name="保登心愛", value="ほと ここあ", inline=True)
        embed.add_field(name="香風智乃", value="かふう ちの", inline=True)
        embed.add_field(name="天天座理世", value="てでざ りぜ", inline=True)
        embed.add_field(name="桐間紗路", value="きりま しゃろ", inline=True)
        embed.set_footer(text="甭甭= =")
        await ctx.send(embed=embed)

    #　有好幾個 arg，就是只傳給他
    @commands.command()
    async def said(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    # 原來註解是有用的，會自己轉
    @commands.command()
    async def clean(self, ctx, num: int):
        await ctx.channel.purge(limit=num+1) # 指令那則訊息也算一個

# 註冊 Cog
# 運行 bot 會呼叫 setup，傳入主文件的 bot

def setup(bot):
    bot.add_cog(Main(bot))
