import discord, os, pytz, asyncio
from discord.ext import commands
from webserver import execute

# Initialization
endy = commands.Bot(command_prefix='./')
endy.remove_command('help')
event = endy.event
cmd = endy.command
time = pytz.timezone('Asia/Ho_Chi_Minh')

@event
async def on_ready():
  print("[@Endy#3636] - System Online")
  channel = endy.get_channel(id = 769497610300948480)
  await channel.send(f'[Notification] — System Online')
  await endy.change_presence(
    status = discord.Status.idle,
    activity = discord.Activity(
      type = discord.ActivityType.listening,
      name = "🌧agoraphobic🌧"
    )
  )

# Cogs Loader
EndyUUID = '554680253876928512'
Jeb = '<a:jeb_sheep:748548226889547867>'
# Changelog: Instead of ctx.msg.del() it was changed to a checkmark reaction

@cmd()
async def c(ctx, amount, pass_context = True):
  if str(ctx.message.author.id) in ['554680253876928512', '608876620417335337']:
    deleted = await ctx.channel.purge(limit = int(amount) + 1)
    print(f"Deleted {len(deleted) - 1} msg")
    await ctx.send(f"Deleted `{len(deleted) - 1}` messages!", delete_after=3)

@cmd(aliases = ['load'])
async def l(ctx, cog, pass_context = True):
  if str(ctx.message.author.id) == EndyUUID:
    msg = await ctx.fetch_message(str(ctx.message.id))
    try:
      endy.load_extension(f"cogs.{cog}")
      await msg.add_reaction('✅')
      print(f"L{cog}")

    except:
      await msg.add_reaction('❎')

    await asyncio.sleep(3)
    await msg.delete()

@cmd(aliases = ['unload'])
async def ul(ctx, cog, pass_context = True):
  if str(ctx.message.author.id) == EndyUUID:
    msg = await ctx.fetch_message(str(ctx.message.id))
    try:
      endy.unload_extension(f"cogs.{cog}")
      await msg.add_reaction('✅')
      print(f"U{cog}")

    except:
      await msg.add_reaction('❎')

    await asyncio.sleep(3)
    await msg.delete()

@cmd(aliases = ['reload'])
async def rl(ctx, cog, pass_context = True):
  if str(ctx.message.author.id) == EndyUUID:
    msg = await ctx.fetch_message(str(ctx.message.id))
    try:
      endy.unload_extension(f"cogs.{cog}")
      await asyncio.sleep(0.5)
      endy.load_extension(f"cogs.{cog}")
      await msg.add_reaction('✅')
      print(f"R{cog}")

    except:
      await msg.add_reaction('❎')

    await asyncio.sleep(3)
    await msg.delete()

for root, dirs, files in os.walk('./cogs'):
	for item in files:
		if item[-3:] == '.py': endy.load_extension(f"cogs.{item[:-3]}")

execute()
endy.run(os.environ.get("DISCORD_BOT_SECRET"))
