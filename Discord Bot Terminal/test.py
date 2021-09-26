import discord
from discord.ext import commands, tasks

bot = commands.Bot('!')

@bot.event
async def on_ready():
    print(f'Estou conectada como {bot.user}!')
    send_message.start()

@bot.event
async def on_message(message):
    name = message.author.name
    server = message.guild
    content = message.content
    print(f'''\n\033[31mName: {name}\nServer: {server}\nMessage: {content}\033[m\n''')

@tasks.loop(seconds = 3)
async def send_message():
    choice = str(input('Server or User? ')).lower()

    if choice == 'server':
        try:
            channel_id = int(input('Channel ID: '))
        except:
            print('Por favor informe um número inteiro.')
        
        try:
            channel = bot.get_channel(channel_id)
            print('Conectado com sucesso.')
        except:
            channel = None
            print('O canal não foi encontrado.')
        
        if channel != None:
            message = str(input('Message: '))
            await channel.send(message)
    elif choice == 'user':
        print('user')


bot.run('token')