import discord
from random import choice
from discord.ext import commands as endy

class Facts(endy.Cog):
  def __init__(self, bot):
    self.bot = bot

  # Check status
  @endy.Cog.listener()
  async def on_ready(self):
    pass

  # Command
  @endy.command(aliases = ['truth', 'f', 'facts'])
  async def fact(self, ctx):
    await ctx.message.delete()
    facts = [
      "The chicken came first or the egg? The answer is... `the chicken`",
      "The alphabet is completely random",
      "I ran out of facts. That's a fact",
      "Found this fact? You're lucky!",
      "There are 168 prime numbers between 1 and 1000",
      "`τ` is just `π` times two!",
      "`τ` is `tau` and `π` is `pi`!",
      "The F word is the most flexible word in English!",
      "`Homosapiens` are how biologists call humans!",
      "`Endy` is a cool bot! And that's a fact!",
      "`Long` is short and `short` is long!",
      "√-1 love you!"
      "There are 13 Slavic countries in the world -- Brought to you by your gopnik friend!",
      "There are plagues in 1620, 1720, 1820, 1920 and...",
      "The phrase: `The quick brown fox jumps over the lazy dog` contains every letter in the alphabet!",
      "There are no Nobel prizes for math because Nobel lost his love to a mathematician",
      "Endy is intellegent",
      "69 is just a normal number ok?",
      "There are 24 synthetic elements from 95~118"
    ]

    embed = discord.Embed(
      title = 'Fact!',
      description = str(ctx.message.author),
      colour = 0x7289DA
    )

    embed.add_field(
      name = 'Fact of the second:',
      value = f'{choice(facts)}'
    )

    await ctx.send(embed = embed)

def setup(client):
  client.add_cog(Facts(client))

'''
Changelog Facts.py v1.0
• Readded Facts.py
'''