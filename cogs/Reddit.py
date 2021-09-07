import discord, praw
from discord.ext import commands as endy

class Reddit(endy.Cog):
  def __init__(self, client):
    self.client = client
  
  #Is ready
  @endy.Cog.listener()
  async def on_ready(self):
    pass

  @endy.command(aliases = ['red', 'r'])
  async def reddit(self, ctx, text):
    redditvar = praw.Reddit(
      client_id = "Jsc0erJJTxRzMg",
      client_secret = "mx1Ef-2Ilf268Vqf4U7mW0TSHf0",
      password = "Hoang06032007",
      user_agent = "Reddit Plugin for Endy bot",
      username = "Enderhoang"
    )
    link = f"https://reddit.com/{text}"
    reddit = discord.Embed(title = 'Reddit', colour = 0xFF4500)
    if text[0] == 'r':
      reddit.add_field(name = 'Subreddit', value = f'Go to {link}', inline=False)
    elif text[0] == 'u':
      reddit.add_field(name = 'Reddit user', value = f'Go to {link}', inline=False)
    await ctx.send(embed=reddit)

def setup(client):
  client.add_cog(Reddit(client))
