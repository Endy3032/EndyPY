# Modules
import asyncio
from discord.ext import commands as endy

# Define Class
class Ship(endy.Cog):
  def __init__(self, client):
    self.client = client
  
  # Check status
  @endy.Cog.listener()
  async def on_ready(self):
    pass

  # Code be here
  @endy.command()
  async def ship(self, ctx, P1, P2):
    await ctx.send(f'{P1} and {P2} sitting by a tree')
    await asyncio.sleep(1)
    msg = await ctx.send('K')
    await asyncio.sleep(0.5)
    await msg.edit(content = 'K-I')
    await asyncio.sleep(0.5)
    await msg.edit(content = 'K-I-S')
    await asyncio.sleep(0.5)
    await msg.edit(content = 'K-I-S-S')
    await asyncio.sleep(0.5)
    await msg.edit(content = 'K-I-S-S-I')
    await asyncio.sleep(0.5)
    await msg.edit(content = 'K-I-S-S-I-N')
    await asyncio.sleep(0.5)
    await msg.edit(content = 'K-I-S-S-I-N-G')
    await asyncio.sleep(0.5)
    await msg.edit(content = 'Kissing!')
    print(f'Shipped {P1} with {P2}')
    
  # Error handling
  @ship.error
  async def meme_error(self, ctx, error):
    if isinstance(error, endy.MissingRequiredArgument):
      await ctx.send(content = 'Please add `2 object` to the `ship` command. Each object inside "quotes"')

# Fin
def setup(client):
  client.add_cog(Ship(client))

'''
Changelogs
v1.0:
Added ./ship cmd

v1.1:
Added error handling
Added delete recent msg
'''