import discord
from discord.ext import commands as endy

class Speedtest(endy.Cog):
  def __init__(self, client):
    self.client = client
  
  #Is ready
  @endy.Cog.listener()
  async def on_ready(self):
    pass
  
  @endy.command(aliases = ['s', 'hunt'])
  async def speedtest(self, ctx, id):
    link = f'https://www.speedtest.net/result/{id}.png'
    st = discord.Embed(
      colour = 0x13152a 
    )
    st.set_image(url = link)
    try:
      int(id)
      await ctx.send(embed = st)
      print(type(id))
    except:
      await ctx.send('Please input a 10 digit number after the `./s` command')

def setup(client):
  client.add_cog(Speedtest(client))