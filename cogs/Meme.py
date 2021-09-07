import discord, asyncio
from random import choice
from discord.ext import commands as endy

class Meme(endy.Cog):
  def __init__(self, bot):
    self.bot = bot

  # Check status
  @endy.Cog.listener()
  async def on_ready(self):
    pass

  # Command
  @endy.command(aliases = ['m'])
  async def meme(self, ctx, type):
    v_stonks = ['buy','sell','rent'] 
    n_stonks = ['phone','company','cake','kidney','Rubiks cube','slab of gold','Mac','PC','jar of pickles']
    v_tehc = ['fix', 'speeds up', 'cool','broke']
    n_tehc = ['phone','PC',"mom's brick phone",'TV','roomba',]
    method_tehc = ['smashing it','kicking it','closing the 400+ tabs','removing the minecraft crack']
    v_shef = ['cooks','season','add']
    n_shef = ['hamburger','water','frozen pizza','salt','pepper','jalapenos','icing','muffin','rice','juice']
    if type == 'stonks':
      await ctx.channel.purge(limit=1)
      await ctx.send(f'When you {choice(v_stonks)} a {choice(n_stonks)} for a {choice(n_stonks)}:')
      stonks = discord.Embed(colour=0x0080ff)
      stonks.set_image(url = "https://i0.wp.com/lucloi.vn/wp-content/uploads/2020/01/maxresdefault-58.jpg?fit=1280%2C720&ssl=1") 
      await asyncio.sleep(1)
      await ctx.send(embed = stonks)
    
    elif type == 'tehc':
      await ctx.channel.purge(limit = 1)
      await ctx.send(f'When you {choice(v_tehc)} a {choice(n_tehc)} by {choice(method_tehc)}:')
      tehc = discord.Embed(colour = 0x6EE66E)
      tehc.set_image(url = "https://i.redd.it/61w2stl1bc941.jpg")
      await asyncio.sleep(1)
      await ctx.send(embed = tehc)
    
    elif type == 'shef':     
      shef = discord.Embed(colour = 0xfffffe)
      shef.set_image(url = 'https://en.meming.world/images/en/6/6a/Shef.jpg')
      await ctx.channel.purge(limit = 1)
      await ctx.send(f"When you {choice(v_shef)} {choice(n_shef)} to a {choice(n_shef)}:")
      await asyncio.sleep(1)
      await ctx.send(embed = shef)
    
    else:
      await ctx.send("Invalid meme. Refer to the ./help command for support\nMore memes will be added in the future :3 :grinning:")

def setup(client):
  client.add_cog(Meme(client))

'''
Changelog Meme.py v1.0
• Readded Meme.py
'''