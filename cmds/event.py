import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json', 'r', encoding='utf8') as f:
    jdata = json.load(f)


class Event(Cog_Extension):

    # 和 event 一樣
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(jdata['channel_one'])
        await channel.send(f'{member} join!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(jdata['channel_two'])
        await channel.send(f'{member} leave!')

    # 輸入訊息觸發 in_message 事件，判斷條件
    @commands.Cog.listener()
    async def on_message(self, msg):
        # 存在個地方吧
        # keyword = ['kiwi','banana', 'orange','cat']
        if msg.content == '你好':
            await msg.channel.send('你好阿！')
        elif msg.content.endswith('貓'):
            await msg.channel.send('有貓！？')
        elif msg.content == 'apple' and msg.author != self.bot.user:
            await msg.channel.send('apple')
        elif msg.content in jdata['fruit'] and msg.author != self.bot.user:
            await msg.channel.send('水果！')


def setup(bot):
    bot.add_cog(Event(bot))
