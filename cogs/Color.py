import random, discord
from discord.ext import commands as endy

class Color(endy.Cog):
  def __init__(self, client):
    self.client = client
  
  # Commands
  @endy.command(aliases = ['col'])
  async def color(self, ctx, *, value = None):
    await ctx.message.delete()
    
    try:
      if value.startswith('#') and len(value) == 7:
        RH = value[1:3]
        GH = value[3:5]
        BH = value[5:]
        RD = int(RH, 16)
        GD = int(GH, 16)
        BD = int(BH, 16)

      else:
        value = value.split(', ')
        RD = value[0]
        GD = value[1]
        BD = value[2]
        RH = hex(int(RD)).replace('0x', '').zfill(2).upper()
        GH = hex(int(GD)).replace('0x', '').zfill(2).upper()
        BH = hex(int(BD)).replace('0x', '').zfill(2).upper()

    except:
      RD = random.randint(0, 256)
      GD = random.randint(0, 256)
      BD = random.randint(0, 256)
      RH=str(hex(RD)).replace('0x','').zfill(2)
      GH=str(hex(GD)).replace('0x','').zfill(2)
      BH=str(hex(BD)).replace('0x','').zfill(2)

    embed = discord.Embed(
      title = "Color",
      description = f'Issued by {ctx.message.author}',
      colour = 0x7289DA
    )

    embed.add_field(
      name = "RGB",
      value = f'{RD}, {GD}, {BD}',
      inline = True
    )

    embed.add_field(
      name = "Hex",
      value = f'{RH}{GH}{BH}',
      inline = True
    )

    embed.set_thumbnail(url = f'https://dummyimage.com/128/{RH}{GH}{BH}/{RH}{GH}{BH}.png')
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Color(client))

'''
Changelog Color.py v2.0
• Edited display name
'''