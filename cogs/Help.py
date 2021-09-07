import discord, pytz
from datetime import datetime
from discord.ext import commands as endy

class Help(endy.Cog):
  def __init__(self, client):
    self.client = client

  @endy.command(aliases=['?'])
  async def help(self, ctx, mode = None):
    time = pytz.timezone('Asia/Ho_Chi_Minh')
    prefix = './'
    await ctx.message.delete()
    help = discord.Embed(
      title = "Help",
      description = "Want some help? Here ya go!",
      timestamp = datetime.now(time),
      colour = 0x7289DA
    )

    if mode == None:
      help.add_field(
        name = f":question: General",
        value = f"`{prefix}help general`",
        inline = True
      )

      help.add_field(
        name = f":tada: Fun",
        value = f"`{prefix}help fun`",
        inline = True
      )

      help.add_field(
        name = f":abc: Other",
        value = f"`{prefix}help other`",
        inline = False
      )
    
    elif mode.lower() in 'general':
      help.add_field(
        name = ":question: help <mode> (?)",
        value = f"Brings up the help dialog\nArguments: `<mode>: general/fun/text`",
        inline = False
      )
      '''
      help.add_field(
        name = ":information_source: info (bot, bot_info, bot_i, info, endy)",
        value = f"Show <@!699911346367627374>'s infos like ping (More added later, don't know what to add :P)",
        inline = False
      )
      '''

      help.add_field(
        name = 'hi <member>',
        value = 'Send a random greet to someone!\nArguments: `<member>: ping/name of a member`',
        inline = False
      )

      help.add_field(
        name = 'ping <text> <amount>/Nothing (p)',
        value = 'Ping somebody/anything or get bot\'s latency\nArguments: `<text>: Any text; <amount>: 1-5`',
        inline = False
      )
    
    elif mode.lower() in 'fun':
      help.add_field(
        name = "8ball <question> (8b)",
        value = f"~~Charlie charlie~~ <@!699911346367627374>'s 8-Ball, ya there?\nArguments: `<question>: Any text`",
        inline = False
      )

      help.add_field(
        name = 'achievement <icon/text> <icon/text> (ach)',
        value = 'Make a Minecraft achievement banner!\nArguments: `<icon/text>: the name of an icon or the text for the achievement`\n(If you already put the icon in, put the text in after and vice versa',
        inline = False
      )

      help.add_field(
        name = 'emoji <name> (e)',
        value = 'Send an emoji (kaomoji)\nArguments: `<name>: name of an emoji`',
        inline = False
      )

      help.add_field(
        name = "fact (facts, f, truth)",
        value = f"Spit some facts out!",
        inline = False
      )

      help.add_field(
        name = "meme <type> (m)",
        value = f"Make a MemeMan meme!\nArguments: `<type>: stonks/tehc/shef`",
        inline=False
      )

      help.add_field(
        name = 'random <type> <amount> (rand)',
        value = 'Send a random msg depending on your need.\nArguments: `<type>: randint, coin, dice; <amount>: 1-5',
        inline = False
      )

    elif mode.lower() in 'other':
      help.add_field(
        name = 'cappy <text>',
        value = 'cApTALiZe wOrD LiKe KrAZy\nArguments: `<text>: watever`',
        inline = False
      )

      help.add_field(
        name = 'reddit <user/sub>',
        value = 'Post the link to a subreddit/user\nArguments: `<user/sub>: r/sub or u/user`',
        inline = False
      )

      help.add_field(
        name = 'ship "<p1>", "<p2>"',
        value = 'Ship someone with another one\nArguments: `<p1> <p2>: watever`',
        inline = False
      )

      help.add_field(
        name = 'speedtest <id>',
        value = 'Get Speedtest result of somebody\nArguments: `<id>: 10 digit number`',
        inline = False
      )

      help.add_field(
        name = 'wavy <text> <amount> (w, wave)',
        value = 'Send a wavy message with style!\nArguments: `<text>: Whatever; <amount>`: 1-5',
        inline = False
      )

    await ctx.send(embed = help)

def setup(client):
  client.add_cog(Help(client))
