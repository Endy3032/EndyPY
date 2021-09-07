from discord.ext import commands as endy

class Wavy(endy.Cog):
  def __init__(self, client):
    self.client = client

  # Check status
  @endy.Cog.listener()
  async def on_ready(self):
    pass

  # CMD
  @endy.command(aliases=['wave','w'])
  async def wavy(self, ctx, *, msg):
    await ctx.channel.purge(limit=1)
    if '<@!520162303216320522>' in msg:
      await ctx.send("Please don't spam him, he don't like that")
    elif '@everyone' in msg:
      await ctx.send("Don't wave everyone?!?")
    elif '<@!699911346367627374>' in msg or '<@&699968114271453205>' in msg:
      await ctx.send("Don't wave me! :stuck_out_tongue: I'm <@!699911346367627374> the great LOL!")
    elif "🦶" in msg:
      await ctx.send("EWWWWWW! You're so smelly!")
    else:
      print(f"{ctx.message.author} waved {msg}")
      try:
          if int(msg[-1]) <= 5 and int(msg[-1]) >= 1:
            for i in range(0, int(msg[-1])):
              text = msg[0:-1]
              wavy = (f'{text}\n'
                      f' {text}\n'
                      f'  {text}\n'
                      f'   {text}\n'
                      f'    {text}\n'
                      f'     {text}\n'
                      f'      {text}\n'
                      f'      {text}\n'
                      f'      {text}\n'
                      f'     {text}\n'
                      f'    {text}\n'
                      f'   {text}\n'
                      f'  {text}\n'
                      f' {text}\n'
                      f'{text}\n'
                      f'{text}\n')
              await ctx.send(wavy)
          else:
            await ctx.send("Please send a max of 5 and a min of 1")
      except:
        await ctx.send(msg)

def setup(client):
  client.add_cog(Wavy(client))