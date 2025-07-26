import discord
from discord.ext import commands
from ayarlar import ayarlar
from botfunction import *
import requests
import os
import random

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='a!', intents=intents)

images_path = os.path.join(os.path.dirname(__file__), "images")
os.listdir(images_path)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yapıldı.')
    print('-------------------')

@bot.command()
async def merhaba(ctx):
    await ctx.send("Selam!")

@bot.command()
async def bye(ctx):
    await ctx.send(f"Güle güle {ctx.author.name}!")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.lower() == "sa":
        await message.channel.send(f"Aleyküm selam {message.author.name}!")
    if message.content.lower() == "bye":
        await message.channel.send(f"Güle güle {message.author.name}!")
    await bot.process_commands(message)

@bot.command()
async def ms(ctx):
    gecikme = round(bot.latency * 1000)
    await ctx.send(f'Gecikme: {gecikme} ms')

@bot.command()
async def gecikme(ctx):
    gecikme = round(bot.latency * 1000)
    await ctx.send(f'Gecikme: {gecikme} ms')

@bot.command()
async def yazitura(ctx):
    sonuc = yazi_tura()
    await ctx.send(sonuc)

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_fox_image_url():
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']

def get_dog_image_url():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command()
async def duck(ctx):
    url = get_duck_image_url()
    await ctx.send(url)

@bot.command()
async def dog(ctx):
    url = get_dog_image_url()
    await ctx.send(url)

@bot.command()
async def fox(ctx):
    url = get_fox_image_url()
    await ctx.send(url)

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir(images_path))
    with open(os.path.join(images_path, img_name), 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
    print(f'{ctx.author} tarafından MEM komutu kullanıldı.')

@bot.command()
async def yardım(ctx):
    yardim_mesaji = (
        "Kullanılabilir komutlar:\n"
        "a!merhaba\n"
        "bye\n"
        "sa\n"
        "a!ms\n"
        "a!gecikme\n"
        "a!yazitura\n"
        "a!duck\n"
        "a!mem\n"
        "a!dog\n"
        "a!fox\n"
        "a!yardım"
    )
    await ctx.send(yardim_mesaji)

bot.run(ayarlar["TOKEN"])
