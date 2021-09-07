from discord.ext import commands as endy
from random import choice

class Hi(endy.Cog):
  def __init__(self, client):
    self.client = client

  # Check status
  @endy.Cog.listener()
  async def on_ready(self):
    pass

  # Cmd
  @endy.command()
  async def hi(self, ctx, member):
    await ctx.channel.purge(limit=1)
    responses = [
      "Hey there!", "Hi There!", "Woah, didn't see ya there!",
      "Hello?", "Ping Pong!", "What ya doin'", "What's up", "Hey"
    ]
    bad_responses = [
      "Ding dong"
    ]
    print(member)
    if member in ['<@!548080460950142976>', '<@!676844700384100352>']: await ctx.send(f"{choice(bad_responses)} {member}!")
    else: await ctx.send(f"{choice(responses)}, {member}")

def setup(client):
  client.add_cog(Hi(client))
