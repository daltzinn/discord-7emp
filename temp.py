import discord
from discord.ext import commands, tasks
import asyncio
import time

intents = discord.Intents.all()
intents.messages = True

bot = commands.Bot(command_prefix='<', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is up!')

@bot.command()
async def clear(ctx):
    await ctx.channel.purge(limit=10000)  
@tasks.loop(minutes=1440) # Here you can change the time
async def clear_messages(ctx):
    await asyncio.sleep(10)
    await ctx.channel.purge(limit=10000) 

@bot.command()
async def start_clear(ctx):
    await ctx.send("Temporary messages enabled, messages will be deleted every 24 hours.")
    clear_messages.start(ctx)

@bot.command()
async def stop_clear(ctx):
    clear_messages.stop()
    await ctx.send("Temporary messages disabled.")


bot.run('Bot token goes here')

