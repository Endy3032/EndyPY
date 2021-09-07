import asyncio
from discord.ext import commands as endy

class Loading(endy.Cog):
  def __init__(self, client):
    self.client = client

  @endy.command(aliases = ['ld'])
  async def loading(self, ctx, *, text):
    process = text.split('\n')
    nprocess = []
    amount = []
    for i in process:
      i = i.strip()
      amount.append(int(i[-1]))
      nprocess.append(i[:-1].strip())

    msg = await ctx.send('**Initializing Procedure**')
    process = [':black_circle: :white_circle: :white_circle:', ':white_circle: :black_circle: :white_circle:', ':white_circle: :white_circle: :black_circle:']
    for x in nprocess:
      for y in range(1, amount[nprocess.index(x)] + 1):
        for i in process:
          await msg.edit(content = f'{i} \t{x}\t{y}/{amount[nprocess.index(x)]}')
          await asyncio.sleep(1.5)

    await msg.edit(content = '**Complete!**')

def setup(client):
  client.add_cog(Loading(client))
