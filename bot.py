import discord
from discord.ext import commands
from ayarlar import ayarlar
from botfunction import *

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yapıldı. (ID: {bot.user.id})')
    print('-------------------')

@bot.command()
async def merhaba(ctx):
    """Merhaba komutu."""
    await ctx.send("Selam!")

@bot.command()
async def bye(ctx, message):
    """Bye komutu."""
    await ctx.send(f"Güle güle {message.author.name}!")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.lower() == "sa":
        await message.channel.send(f"Aleyküm selam {message.author.name}!")

    await bot.process_commands(message)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Üye katılım tarihini gösterir."""
    await ctx.send(f'{member.name} {discord.utils.format_dt(member.joined_at)} tarihinde sunucuya katıldı.')

@bot.command()
async def ms(ctx):
    """Botun gecikmesini gösterir."""
    gecikme = round(bot.latency * 1000)
    await ctx.send(f'Gecikme: {gecikme} ms')

@bot.command()
async def gecikme(ctx):
    """Botun gecikmesini gösterir."""
    gecikme = round(bot.latency * 1000)
    await ctx.send(f'Gecikme: {gecikme} ms')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def temizle(ctx, miktar: int):
    """Belirtilen miktarda mesajı siler."""
    if miktar < 1 or miktar > 100:
        await ctx.send("Lütfen 1 ile 100 arasında bir sayı girin.")
        return
    await ctx.channel.purge(limit=miktar + 1)
    await ctx.send(f"{miktar} mesaj silindi.", delete_after=5)

@bot.command()
async def yazi_tura(ctx):
    """Yazı tura atar."""
    sonuc = yazi_tura()
    await ctx.send(f"Sonuç: {sonuc}")

@bot.command()
async def yardım(ctx):
    """Yardım komutu."""
    yardim_mesaji = (
        "Kullanılabilir komutlar:\n"
        "!merhaba - Merhaba mesajı gönderir.\n"
        "!bye - Güle güle mesajı gönderir.\n"
        "!sa - Aleyküm selam mesajı gönderir.\n"
        "!joined <üye> - Üyenin katılım tarihini gösterir.\n"
        "!ms - Botun gecikmesini gösterir.\n"
        "!gecikme - Botun gecikmesini gösterir.\n"
        "!temizle <miktar> - Belirtilen miktarda mesajı siler (1-100).\n"
        "!yazi_tura - Yazı tura atar."
    )
    await ctx.send(yardim_mesaji)