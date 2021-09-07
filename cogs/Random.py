import discord
from random import choice, randint
from discord.ext import commands as endy

class Random(endy.Cog):
  def __init__(self, bot):
    self.bot = bot

  # Check status
  @endy.Cog.listener()
  async def on_ready(self):
    pass

  # Command
  @endy.command(aliases=['rand'])
  async def random(self, ctx, type, t = 1, int1 = 0, int2 = 100):
    Coin = ['**Heads**', '**Tails**']
    output = [None, None, None, None, None, None]
    if t > 5:
      await ctx.send(f'Please input a number from 1-5.')

    elif type == 'dice' or type == 'die':
      for x in range(0, t):
        output[x] = randint(1, 6)
      for lap in range(0, 5):
        output[5] = lap
      result = discord.Embed(
        title = f'Rolling {t} dice...',
        description = f'{output[0]}, {output[1]}, {output[2]}, {output[3]}, {output[4]}',
        colour = 0x7289DA
      )
      result.add_field(
        name = 'Total',
        value = f'{output[5]}'
      )
      await ctx.send(embed = result)

    elif type == 'coin':
      for x in range(t):
        output[x] = choice(Coin)
      result = discord.Embed(
        title = 'Coin flipping result',
        description=f'{output[0]}, {output[1]}, {output[2]}, {output[3]}, {output[4]}',
        colour=0x7289DA
      )
      h = output.count('**Heads**')
      t = output.count('**Tails**')
      result.add_field(name = 'Total', value = f'{h} **Heads** and {t} **Tails**!')
      await ctx.send(embed = result)

    elif type == 'int':
      for x in range(0, t):
        output[x] = randint(int1, int2)
        output[5] = x
      result = discord.Embed(title = f'Random numbers from {int1} to {int2}', description=f'{output[0]}, {output[1]}, {output[2]}, {output[3]}, {output[4]}', colour=0x7289DA)
      result.add_field(name = 'Total', value = f'{output[5]}')
      await ctx.send(embed = result)

    else:
      await ctx.send(f"The mode {type} does not exist\nTry `dice`, `coin`, `int` or refer to the `help` command")

def setup(client):
  client.add_cog(Random(client))

'''
Changelog Random.py v1.0
• Readded Random.py
'''