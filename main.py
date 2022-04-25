#Christina Lau
#Spring 2022 Rosen
#Final Project
from discord.ext import commands
import random
TOKEN = open("token.txt","r").readline()
bot = commands.Bot(command_prefix = '-')
@bot.command()
async def quote(ctx):
    qt = open('quotes.txt').read().splitlines()
    rp = random.choice(qt)
    random.seed(a=None)
    await ctx.send(rp)
@bot.command()
async def gif(ctx):
    g = open('gif.txt').read().splitlines()
    x = random.choice(g)
    random.seed(a=None)
    await ctx.send(x)
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f'{error}. Please try -quote or -gif.')
@bot.event
async def on_ready():
    print('You are now able to use {0.user}'.format(bot))
bot.run(TOKEN)
