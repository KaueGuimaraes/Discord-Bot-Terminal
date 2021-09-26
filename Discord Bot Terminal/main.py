import discord
from discord.ext import commands


def connect_bot(token):
    client = commands.Bot(command_prefix = '!')

    @client.event
    async def on_ready():
        print(f'Conectado como {client.user}')
    
    @client.command(name = 'eai?')
    async def working(ctx):
        await ctx.send('Working.')

    @tasks.loop(seconds = 10)
    async def current_time():
        channel = client.get_channel(818276644439326793)
        await channel.send('Olá.')

    current_time.start()
    client.run(token)
    

#token = str(input('Bot Token: '))
token = 'token'

try:
    print('entrar')
    connect_bot(token)
except:
    print(f'Não consegui conectar ao bot de token {token}')