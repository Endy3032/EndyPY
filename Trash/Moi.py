from discord.ext import commands as endy

class Moi(endy.Cog):
  def __init__(self, client):
    self.client = client

  @endy.command()
  async def moi(self, ctx, amount):
    if int(amount) <= 50: await ctx.send('moi ' * int(amount))
    else: await ctx.send('Moi moi gì mà nhìu zữ zị, năm chục thôi :)')

  @endy.command()
  async def mol(self, ctx, amount):
    if int(amount) <= 20: await ctx.send('6x10^23 ' * int(amount))
    else: await ctx.send(f'Đừng có nghiện mol nữa coi chừng ng m bay ra làm 6x10^23x{amount} mảnh giờ :)')

def setup(client):
  client.add_cog(Moi(client))