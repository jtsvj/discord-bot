import discord
from discord.ext import commands
from discord.utils import get

TOKEN = "OTkyNjc5MjE2Nzg3MjQzMDg4.GBxuxx.-hJnMKGCzkuT_X_TaDOCtrt0GiG3_eSeGSaJvU"

intents = discord.Intents.all()
intents.message_content = True
intents.members = True

bot = commands.Bot(intents=intents, command_prefix = '.')

@bot.event
async def on_ready():
    print(f"Loaded successfully as {bot.user}")

@bot.command(name='all')
async def all_members(ctx):
    for member in bot.get_all_members():
        print(member)
        await ctx.send(member.mention)

@bot.command()
async def addRole(ctx, user : discord.Member, *, role : discord.Role):
    if role in user.roles:
        await ctx.send(f"{user.mention} already has the {role} role!")
    else:
        await user.add_roles(role)
        await ctx.send(f"{role} role is added to {user.mention}")

@bot.command()
async def remRole(ctx, user : discord.Member, *, role : discord.Role):
    if not role in user.roles:
        await ctx.send(f"{user.mention} does not have the {role} role!")
    else:
        await user.remove_roles(role)
        await ctx.send(f"{role} role is removed from {user.mention}")

@bot.command(name='pizda')
async def remove_all_roles(ctx):
    for member in bot.get_all_members():

        print(member)

        all_roles = member.roles[1:]
        
        try:
            for server_role in all_roles:
                await member.remove_roles(server_role)
                await ctx.send(f"{server_role} removed.")
        except discord.errors.Forbidden:
            await ctx.send(f"Don't have permission for removing '{server_role}' role from '{member}'")

bot.run(TOKEN)