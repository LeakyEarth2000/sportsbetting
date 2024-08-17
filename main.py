import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!",intents=intents)
bot.remove_command('help')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.playing, name="with myself"))
    print(
        "------------------------------------\n           Bot is Running: \n------------------------------------"
    )
    print("Name: {}\n".format(bot.user.name))
    print("ID: {}\n".format(bot.user.id))

@bot.command(pass_context=True)
async def coinflip(ctx):
    variable = [
        "```It's Heads```",
        "```It's Tails```",
    ]
    embed = discord.Embed(title=f"{random.choice(variable)}", color=0xe67e22)
    await ctx.send(embed=embed)

bot.run('MTI3NDI3NTM0MzczMzM2MjgxMA.GzCG6C.EJ38ebjJy2guGGi2dJ-mmT7Gu56Kaop6bQUNMs')