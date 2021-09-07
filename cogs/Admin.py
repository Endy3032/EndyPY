import discord, pytz
from datetime import datetime
from discord.ext import commands as endy

class Admin(endy.Cog):
  def __init__(self, client): self.client = client

  # Clear
  @endy.command()
  @endy.has_permissions(administrator = True)
  async def c(self, ctx, amount):
    deleted = await ctx.channel.purge(limit = int(amount) + 1)
    print(f"Deleted {len(deleted) - 1} msg")
    await ctx.send(f"Deleted `{len(deleted) - 1}` messages!", delete_after=3)

  # Vembed
  @endy.command()
  @endy.has_permissions(administrator = True)
  async def vembed(self, ctx, pass_context = True):
    time = pytz.timezone("Asia/Ho_Chi_Minh")
    embed = discord.Embed(title = "Title (Markdownable) **Bold** *Italic* __Underline__ ~~Strikethrough~~ `single` :smile:", url = f"https://discord.com/", description = "Description **Bold** *Italic* __Underline__ ~~Strikethrough~~ `single` ```multiple line``` :smile: [hyperlink](https://discord.com)", colour = 0xABCDEF, timestamp = datetime.now(time))
    embed.set_footer(text = "Footer", icon_url = "https://cdn.discordapp.com/embed/avatars/0.png")
    embed.set_thumbnail(url = "https://cdn.discordapp.com/embed/avatars/1.png")
    embed.set_author(name = ctx.message.author, icon_url = ctx.message.author.avatar_url, url = "https://discord.com/")
    embed.set_image(url = "https://cdn.discordapp.com/embed/avatars/2.png")
    embed.add_field(name = ":regional_indicator_a: Field A", value = "This is a field!", inline = False)
    embed.add_field(name = ":regional_indicator_b: Field B", value = "This is another field!", inline = False)
    embed.add_field(name = ":regional_indicator_c: Field C", value = "Inline #1", inline = True)
    embed.add_field(name = ":regional_indicator_d: Field D", value = "Inline #2", inline = True)
    embed.add_field(name = ":regional_indicator_e: Field E", value = "Inline #3", inline = True)
    await ctx.send(embed = embed)

  # Embed maker
  @endy.command()
  @endy.has_permissions(administrator = True)
  async def emb(self, ctx, *, txt = None):
    await ctx.message.delete()
    time = pytz.timezone("Asia/Ho_Chi_Minh")
    if txt == None:
      P1 = discord.Embed(title = "`./emb` Tutorial", description = "Master the power of embeds!", timestamp = datetime.now(time), colour = 0xA03CFF)
      P1.add_field(name = "Embed Maker's key values", value = "​", inline = False)
      P1.add_field(name = "`title`", value = "Embed's title (top, boldest text)", inline = False)
      P1.add_field(name = "`description`", value = "The text right below the title", inline = False)
      P1.add_field(name = "`url`", value = "The URL that the title leads to", inline = False)
      P1.set_footer(text = f"{ctx.message.author} - Page 1/5", icon_url = ctx.message.author.avatar_url)

      P2 = discord.Embed(title = "`./emb` Tutorial", description = "Master the power of embeds!", timestamp = datetime.now(time), colour = 0xA03CFF)
      P2.add_field(name = "Embed Maker's key values", value = "​", inline = False)
      P2.add_field(name = "`colour/color`", value = "Embed's color #hexcol", inline = False)
      P2.add_field(name = "`image`", value = "Embed's large, bottom image (Green)", inline = False)
      P2.add_field(name = "`thumbnail`", value = "Embed's medium, right image (Gray)", inline = False)
      P2.set_thumbnail(url = "https://cdn.discordapp.com/embed/avatars/1.png")
      P2.set_image(url = "https://cdn.discordapp.com/embed/avatars/2.png")
      P2.set_footer(text = f"{ctx.message.author} - Page 2/5", icon_url = ctx.message.author.avatar_url)

      P3 = discord.Embed(title = "`./emb` Tutorial", description = "Master the power of embeds!", timestamp = datetime.now(time), colour = 0xA03CFF)
      P3.add_field(name = "Embed Maker's key values", value = "​", inline = False)
      P3.add_field(name = "`author`", value = "Embed's author at the top\nAttributes: `name`, `icon`, `url`\n`name:` Author's name\n`icon:` Author's icon\n`url:` The link that the author\ntext leads to when clicked", inline = False)
      P3.add_field(name = "`footer`", value = "Embed's footer at the bottom\n(same as author but without `url`)", inline = False)
      P3.add_field(name = "`field`", value = "Embed's field (use `./vembed` to view a full embed)\nAttributes: `name`, `value`, `inline`\n`name:` Field's title\n`value:` Field's content\n`inline:` Whether the fields are\nin a same line (3 per line max)", inline = False)
      P3.set_footer(text = f"{ctx.message.author} - Page 3/5", icon_url = ctx.message.author.avatar_url)

      P4 = discord.Embed(title = "`./emb` Tutorial", description = "Master the power of embeds!", timestamp = datetime.now(time), colour = 0xA03CFF)
      P4.add_field(name = "Command demonstration", value = "```./emb\ntitle This is a title\ndescription This is the description\ncolor 192837\nauthor Endy, https://cdn.discordapp.com/avatars/554680253876928512/25a9f3f64812ba894e7113b87b3dac4e.png?size=4096\nfooter This is the footer by Endy, https://cdn.discordapp.com/avatars/554680253876928512/25a9f3f64812ba894e7113b87b3dac4e.png?size=4096\nfield Field A\, Hi!\, False\nfield Field B\, Hello there!\, True\nfield Field C\, Oooh inline!\, True```", inline = False)
      P4.add_field(name = "Result next page!", value = "​")
      P4.set_footer(text = f"{ctx.message.author} - Page 4/5", icon_url = ctx.message.author.avatar_url)

      P5 = discord.Embed(title = "`./emb` Tutorial", description = "Master the power of embeds!", timestamp = datetime.now(time), colour = 0xA03CFF)
      P5.set_image(url = "https://repl.it/@EndyBot/EndyGeneral#Embed_result.png")
      P5.set_footer(text = f"{ctx.message.author} - Page 5/5", icon_url = ctx.message.author.avatar_url)

      pages = [P1, P2, P3, P4, P5]
      msg = await ctx.send(embed = P1, delete_after = 30)
      await msg.add_reaction("◀️")
      await msg.add_reaction("▶️")
      await msg.add_reaction("❎")

      i, emoji = 0, ""
      while True:
        if emoji == "◀️":
          if i > 0:
            i -= 1
            await msg.edit(embed = pages[i])
        
        if emoji == "▶️":
          if i < 4:
            i += 1
            await msg.edit(embed = pages[i])

        if emoji == "❎":
          await msg.delete()
          break

        res = await self.client.wait_for("reaction_add", timeout = 60)

        if str(res[1]) == str(ctx.message.author):
            emoji = str(res[0].emoji)
            await msg.remove_reaction(res[0].emoji, res[1])

      try: await msg.clear_reactions()
      except: pass

    else:
      await ctx.author.send(f"```\n---Embed Maker Input---\n{txt}```")
      fields = []
      title = description = url = thumbnail = image = chan = author = footer = id = ""
      colour = 0xA03CFF
      code = txt.split("\n")
      for i in code:
        if i.startswith("<#"):
          chan = self.client.get_channel(id = int(i[2:-1]))
        if i.startswith("author"):
          author = i.split("\, ")
          name = author[0][7:999]
          try: aicon = author[1]
          except: aicon = "https://cdn.discordapp.com/avatars/699911346367627374/53dd9572cabb9ba6872d27d552ba5448.png?size=4096"
          try: aurl = author[2]
          except: aurl = None
          author = (name, aicon, aurl)
        elif i.startswith("footer"):
          footer = i.split("\, ")
          text = footer[0][7:999]
          try: ficon = footer[1]
          except: ficon = "https://cdn.discordapp.com/avatars/699911346367627374/53dd9572cabb9ba6872d27d552ba5448.png?size=4096"
          footer = (text, ficon)
        elif i.startswith("title"): title = i[6:999]
        elif i.startswith("url"): url = i[4:999]
        elif i.startswith("color") or i.startswith("colour"): colour = int(i[7:999], 16)
        elif i.startswith("description"): description = i[12:999]
        elif i.startswith("image"): image = i[6:999]
        elif i.startswith("thumbnail"): thumbnail = i[10:999]
        elif i.startswith("edit"):
          id = i[5:999]
          msg = await ctx.fetch_message(id = id)
        elif i.startswith("field"):
          field = i.split("\, ")
          name = field[0][6:999]
          try: value = field[1]
          except: value = "​"
          try:
            if field[2].lower() == "true":
              inline = True
            else:
              inline = False
          except:
            pass
          field = (name, value, inline)
          fields.append(field)

      embed = discord.Embed(
        title = title,
        url = url,
        description = description,
        colour = colour
      )
      if len(thumbnail) != 0: embed.set_thumbnail(url = thumbnail)
      if len(image) != 0: embed.set_image(url = image)
      if len(author) != 0: embed.set_author(name = author[0], icon_url = author[1])
      if len(footer) != 0: embed.set_footer(text = footer[0], icon_url = footer[1])

      for i in range(len(fields)):
        embed.add_field(
          name = fields[i][0],
          value = fields[i][1],
          inline = bool(fields[i][2])
        )

      if len(str(chan)) != 0: await chan.send(embed = embed)
      elif len(str(id)) != 0: await msg.edit(embed = embed)
      else: await ctx.send(embed = embed)

  @endy.command(aliases = ['exe'])
  async def execute(self, ctx, *, code):
    def innerexecute(code):
      exec(f"global out; out = {code}")
      global out
      return out
    
    output = discord.Embed(
      title = "Execute Code",
      colour = 0x7289DA
    )

    output.add_field(
      name = 'Input',
      value = code,
      inline = False
    )

    try:
      code_output = innerexecute(code)
    except:
      code_output = 'Failed to execute'

    output.add_field(
      name = 'Output',
      value = code_output,
      inline = False
    )

    await ctx.send(embed = output)

  @c.error
  async def clear_error(self, ctx, error):
    if isinstance(error, endy.MissingPermissions):
      await ctx.send(f"Sorry, you are not allowed to use the `clear` command")

def setup(client):
  client.add_cog(Admin(client))

'''
Changelog v2.0
• Nothing significant here
'''