import discord, pytz, asyncio
from datetime import datetime
from discord.ext import commands as endy

class Ping(endy.Cog):
  def __init__(self, client):
    self.client = client

  # Check status
  @endy.Cog.listener()
  async def on_ready(self):
    pass

  # Command
  @endy.command(aliases=['p', 'ping@'])
  async def ping(self, ctx, *, msg = None, pass_context = True):
    time = pytz.timezone('Asia/Ho_Chi_Minh')
    if msg == None:
      await ctx.channel.purge(limit=1)

      pingI = discord.Embed(
        title = "Ping",
        description = f"Ping...",
        timestamp = datetime.now(time),
        colour = 0x00ffff
      )
      
      msg = await ctx.send(embed = pingI)
      ping = round(self.client.latency * 1000)

      pingO = discord.Embed(
        title = "Ping",
        description = f"Pong! Latency: `{ping}ms`",
        timestamp = datetime.now(time),
        colour = 0x00ffff
      )

      await msg.edit(embed = pingO)
      print(f'Ping {int(ping)}ms')

    else:
      print(f"{ctx.message.author} pinged {msg}")
      if '<@!520162303216320522>' in msg:
        await ctx.channel.purge(limit=1)
        await ctx.send("Please don't ping him, he don't like that")

      elif '@everyone' in msg:
        await ctx.channel.purge(limit=1)
        await ctx.send("Don't ping everyone?!?")

      elif '<@!699911346367627374>' in msg or '<@&699968114271453205>' in msg: await ctx.send("Don't ping me! :stuck_out_tongue:")

      else:
        for i in range(0, int(msg[-1])):
          await ctx.send(msg[:-1])
          await asyncio.sleep(0.5)

def setup(client):
  client.add_cog(Ping(client))
