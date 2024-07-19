

    




import discord
import random
import os
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)




@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def görüşürüz(ctx):
    await ctx.send(f'gülegüle {bot.user}, sana iyi günler diler')

@bot.command()
async def nasılsın(ctx):
    await ctx.send(f'iyiyim sen nasılsın')

@bot.command()
async def iyiyim(ctx):
    await ctx.send(f'harika')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def topla(ctx, s1:int,s2:int):
    await ctx.send(f"toplam: {s1+s2}")
@bot.command()
async def çarpı(ctx, s1:int,s2:int):
    await ctx.send(f"çarpım: {s1*s2}")

@bot.command()
async def eksi(ctx, s1:int,s2:int):
    await ctx.send(f"eksilim: {s1-s2}")

@bot.command()
async def bölüm(ctx, s1:int,s2:int):
    await ctx.send(f"bölüm: {s1/s2}")
  
@bot.command()
async def resim(ctx):
    a=random.choice(os.listdir("resimler"))
    with open(f"resimler/{a}","rb")as r:
        fatma=discord.File(r)
    await ctx.send(file=fatma)

@bot.command()
async def resim1(ctx):
    with open(f"resimler/resim1.png","rb")as r:
        fatma=discord.File(r)
    await ctx.send(file=fatma)


@bot.command()
async def resim2(ctx):
    with open(f"resimler/resim2.png","rb")as r:
        fatma=discord.File(r)
    await ctx.send(file=fatma)

@bot.command()
async def resim3(ctx):
    with open(f"resimler/resim3.png","rb")as r:
        fatma=discord.File(r)
    await ctx.send(file=fatma)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("")
