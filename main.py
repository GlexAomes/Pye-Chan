import discord
from discord.ext import commands
from random import randint
import asyncio

## ----------- SETUP ----------- ##

client = discord.Client(status = "say !help")
bot = commands.Bot(command_prefix = '!')
bot.remove_command("help") #disabling, may want to override later
print("API Version {0}".format(discord.__version__))

## ----------- EVENTS ----------- ##

@bot.event
async def on_ready():
    print("Online.")

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(error)

## ----------- COMMANDS ----------- ##

@bot.command()
async def help(ctx):
    e = discord.Embed(
        title = "Here is what you can do with Rye-Chan",
        description = "Note: this is a Python rewrite.",
        color = 0XFFDF00
    )
    e.add_field(
        name = "!ping",
        value = "Returns the latency of the bot's response.",
        inline = False
    )
    e.add_field(
        name = "!avatar \{Username\}",
        value = "Gives you the URL of someone's avatar.",
        inline = False
    )
    e.add_field(
        name = "!8ball",
        value = "Acts like a Magic 8-Ball so ask it yes or no questions.",
        inline = False
    )
    await ctx.send(embed = e)

@bot.command()
async def ping(ctx): 
    await ctx.send("{0} Pong! {1} ms :ping_pong:".format(ctx.message.author.mention, round(bot.latency * 1000)))

@bot.command()
async def avatar(ctx, *, member: discord.User):
    e = discord.Embed(
        title = member.name + "#" + member.discriminator,
        color = 0xFF0000
    )
    e.set_image(url = member.avatar_url)
    await ctx.send(embed = e)

@bot.command(name = "8ball")
async def eightball(ctx, *, question):
    response = []
    ## GOOD RESPONSE ##
    response.append(":green_book:|It is certain.|:green_book:")
    response.append(":green_book:|It is decidedly so.|:green_book:")
    response.append(":green_book:|Without a doubt.|:green_book:")
    response.append(":green_book:|Yes, definitely.|:green_book:")
    response.append(":green_book:|You may rely on it.|:green_book:")
    response.append(":green_book:|As I see it, yes.|:green_book:")
    response.append(":green_book:|Most likely.|:green_book:")
    response.append(":green_book:|Outlook good.|:green_book:")
    response.append(":green_book:|Yes.|:green_book:")
    response.append(":green_book:|Signs point to yes.|:green_book:")
    ## UNCERTAIN RESPONSE ##
    response.append(":ledger:|Reply hazy, try again.|:ledger:")
    response.append(":ledger:|Ask again later.|:ledger:")
    response.append(":ledger:|Better not tell you now.|:ledger:")
    response.append(":ledger:|Cannot predict now.|:ledger:")
    response.append(":ledger:|Concentrate and ask again.|:ledger:")
    ## BAD RESPONSE ##
    response.append(":closed_book:|Don't count on it.|:closed_book:")
    response.append(":closed_book:|My reply is no.|:closed_book:")
    response.append(":closed_book:|My sources say no.|:closed_book:")
    response.append(":closed_book:|Outlook not so good.|:closed_book:")
    response.append(":closed_book:|Very doubtful.|:closed_book:")
    await ctx.send(":8ball: {0} :8ball:\n\n{1}".format(question, response[randint(0, len(response)-1)]))

## ----------- RUN ----------- ##

def read_token():
    with open("token.key", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

bot.run(read_token())