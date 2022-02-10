import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import asyncio
from datetime import date, datetime


# 初始化又繼承

class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = 0
        # async def interval():
        #     await self.bot.wait_until_ready()
        #     # channel 打成字串就不行
        #     self.channel = self.bot.get_channel(896373179818332172)
        #     while not self.bot.is_closed():
        #         await self.channel.send('嗨嗨，運行中')
        #         await asyncio.sleep(5)

        # # bot 去 loop 去創建 task
        # self.bg_task = self.bot.loop.create_task(interval())

        async def time_task():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(896373179818332172)
            while not self.bot.is_closed():
                now_time = datetime.now().strftime("%H:%M")
                with open('setting.json', 'r', encoding='utf8') as f:
                    jdata = json.load(f)

                if now_time == jdata['time'] and self.counter == 0:
                    self.counter = 1
                    await self.channel.send('Task Working!')
                    await asyncio.sleep(1)
                else:
                    pass
                    await asyncio.sleep(1)

        self.bg_task = self.bot.loop.create_task(time_task())

    @commands.command()
    async def set_channel(self, ctx, ch: int):
        # 東西在 class 裡，好呀
        self.channel = self.bot.get_channel(ch)
        # 去 tag 他
        await ctx.send(f'設置頻道 {self.channel.mention} 成功')

    @commands.command()
    async def set_time(self, ctx, time):
        self.counter = 0
        with open('setting.json', 'r', encoding='utf8') as f:
            jdata = json.load(f)
        jdata['time'] = time
        await ctx.send(f'Set task time: {time}.')
        with open('setting.json', 'w', encoding='utf8') as f:
            # ident 設定多少
            jdata = json.dump(jdata, f, indent=4)


def setup(bot):
    bot.add_cog(Task(bot))
