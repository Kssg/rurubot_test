from dis import dis
import discord
import asyncio
client = discord.Client()


@client.event
async def on_ready():
    print('目前登入身分：', client.user)
    # 正在玩 XXX
    game = discord.Game('人類こんるる計画')
    await client.change_presence(status=discord.Status.idle, activity=game)


@client.event
async def on_message(message):

    if message.author == client.user:
        # 不做事這樣用喔
        return

    if message.content == 'ping':
        await message.channel.send('pong')

    if message.content.startswith('說'):
        tmp = message.content.split(" ", 2)

        if len(tmp) == 1:
            await message.channel.send("說啥")
        else:
            await message.channel.send(tmp[1])

    if message.content.startswith('要改狀態'):
        tmp = message.content.split(" ", 2)
        if len(tmp) == 1:
            await message.channel.send("要改成什麼？")
        else:
            game = discord.Game(tmp[1])
            await client.change_presence(status=discord.Status.idle, activity=game)

    if message.content.startswith('跟我打聲招呼吧'):
        channel = message.channel

        await channel.send('那你先跟我說你好')

        def checkmessage(m):
            return m.content == '你好' and m.channel == channel

        msg = await client.wait_for('message', check=checkmessage)
        await channel.send('嗨, {.author}!'.format(msg))

    if message.content == '我好帥喔':
        tmpmsg = await message.channel.send('你確定？')
        await asyncio.sleep(3)
        await tmpmsg.delete()
        await message.channel.send('不好意思，不要騙人啦')

    if message.content == '群組':
        guilds = await client.fetch_guilds(limit=150).flatten()
        for i in guilds:
            await message.channel.send(i.name)
client.run('ODk2MzcyMjczMjg2NjE1MDYw.YWGJuw.JxXm4nPUs6BbqWmgIXr2pPfPcAw')
