import asyncio
from random import choice
from discord.ext import commands as endy

class Ball(endy.Cog):
  def __init__(self, client):
    self.client = client

  @endy.command(aliases=['8ball', '8b'], pass_context = True)
  async def ball(self, ctx, *, question):
    await ctx.message.delete()
    responses = [
      "It's certain.",
      "It's decidedly so.",
      "Without a doubt.",
      "Yes - definitely.",
      "You may rely on it.",
      "As i see it, yes!",
      "Very likely",
      "Outlook good!",
      "Yes",
      "The signs point to YES!",
      "Reply hazy, try again?",
      "Ask again late",
      "Better tomorrow than today",
      "Can't predict now",
      "Concentrate and ask again",
      "My reply is... no",
      "Enderhoang said... no, definitely",
      "Endy said... maybe",
      "Very doubtful"
    ]

    gura = [
      'No, definitely',
      'Why would I say yes?',
      'Well no',
      'Everything will freeze i mean say no'
    ]

    if 'gura' in question.lower():
      msg = await ctx.send(f"{ctx.message.author}\n:question:: {question}\n:8ball::")
      await asyncio.sleep(1)
      await msg.edit(content = f"{ctx.message.author}\n:question:: {question}\n:8ball:: `{choice(gura)}`")

    else:
      msg = await ctx.send(f"{ctx.message.author}\n:question:: {question}\n:8ball::")
      await asyncio.sleep(1)
      await msg.edit(content = f"{ctx.message.author}\n:question:: {question}\n:8ball:: `{choice(responses)}`")

def setup(client):
  client.add_cog(Ball(client))

'''
Changelog v2.0
• Shortened code
• Redesigned interaction
'''