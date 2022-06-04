import discord
from discord.ext import commands

# 因為不想每個檔案開頭都重新定義這些
# 繼承，傳入 bot
class Cog_Extension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
