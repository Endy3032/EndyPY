from discord.ext import commands as endy
from random import choice
class Emoji(endy.Cog):
  def __init__(self, client):
    self.client = client

  @endy.command(aliases = ['kaomoji', 'e'])
  async def emoji(self, ctx, *, text = None):
    type = ['sad', 'shrug', 'tableflip', 'unflip']
    if text == None:
      text = choice(type)
    emoji = ['(๑◕︵◕๑)', '¯\_(ツ)_/¯', '(╯°□°）╯︵ ┻━┻', '┬─┬ ノ( ゜-゜ノ)']
    index = int(type.index(text))
    await ctx.send(emoji[index])

def setup(client):
  client.add_cog(Emoji(client))
