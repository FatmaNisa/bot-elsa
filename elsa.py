import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def topla(ctx, s1:int,s2:int):
    await ctx.send(f"toplam: {s1+s2}")
@bot.command()
async def çarpı(ctx, s1:int,s2:int):
    await ctx.send(f"çarpım: {s1*s2}")

    





bot.run("")