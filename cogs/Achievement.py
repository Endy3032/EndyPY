import random, discord
from urllib.parse import quote_plus as enc
from discord.ext import commands as endy

class Achievement(endy.Cog):
  def __init__(self, client):
    self.client = client

  # Commands
  @endy.command(aliases = ['ach'])
  async def achievement(self, ctx, *, text):
    name = ['stone', 'grass_block', 'planks', 'crafting_table', 'furnace', 'chest', 'bed', 'coal_block', 'iron_ingot', 'gold_ingot', 'diamond', 'sign', 'book', 'oak_door', 'iron_door', 'redstone', 'rail', 'bow', 'arrow', 'iron_sword', 'diamond_sword', 'iron_armor', 'diamond_armor', 'tnt', 'flint_and_steel', 'fire', 'bucket', 'water', 'lava', 'cookie', 'cake', 'milk', 'creeper', 'pig', 'spawn_egg', 'heart', 'cobweb', 'potion', 'splash']
    id = ['20', '1', '21', '13', '18', '17', '9', '31', '22', '23', '2', '11', '19', '24', '25', '14', '12', '33', '34', '32', '3', '35', '26', '6', '27', '15', '36', '37', '38', '7', '10', '39', '4', '5', '30', '8', '16', '28', '29']
    text = text.split(' ')

    if text[-1] not in name:
      icon = name.index(random.choice(name))
      ach = " ".join(text).strip()
    else:
      icon = name.index(text[-1])
      ach = " ".join(text[:-1]).strip()

    title = enc(random.choice(['Achievement Get!', 'Advancement Made!', 'Goal Reached!', 'Challenge Complete!']))
    url = f"https://minecraftskinstealer.com/achievement/{id[icon]}/{title}/{enc(ach)}"
    achievement = discord.Embed(colour = 0x2f3136)
    achievement.set_image(url = url)
    await ctx.message.delete()
    await ctx.send(embed = achievement)

def setup(client):
  client.add_cog(Achievement(client))

'''
Changelog Achievement.py v2.0
• More efficient code
'''