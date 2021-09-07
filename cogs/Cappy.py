from discord.ext import commands as endy

class Cappy(endy.Cog):
  def __init__(self, client):
    self.client = client

  @endy.command(aliases=['ca'], pass_context = True)
  async def cappy(self, ctx, *, txt):
    await ctx.message.delete()
    f = ''
    c = 0
    for i in txt:
      if i == ' ':
        f += ' '
      else:
        if c % 2 == 0: f += i.upper()
        else: f += i.lower()
        c += 1

    await ctx.send(f)

def setup(client):
  client.add_cog(Cappy(client))

'''
Changelog v2.0
• Fix Cappy not taking spaces into account
'''