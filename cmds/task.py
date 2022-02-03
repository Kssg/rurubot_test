import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import asyncio
import datetime


# 初始化又繼承

class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        async def interval():
            await self.bot.wait_until_ready()
            # channel 打成字串就不行
            self.channel = self.bot.get_channel(896373179818332172)
            while not self.bot.is_closed():
                await self.channel.send('嗨嗨，運行中')
                await asyncio.sleep(5)

        # bot 去 loop 去創建 task
        self.bg_task = self.bot.loop.create_task(interval())

    @commands.command()
    async def set_channel(self, ctx, ch: int):
        # 東西在 class 裡，好呀
        self.channel = self.bot.get_channel(ch)
        # 去 tag 他
        await ctx.send(f'設置頻道 {self.channel.mention} 成功')


def setup(bot):
    bot.add_cog(Task(bot))
