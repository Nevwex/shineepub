import disnake, aiohttp, random
from disnake.ext import commands
danbooru = "https://danbooru.donmai.us/posts.json?tags=is:nsfw&limit=10000"

class BtnNsfw(disnake.ui.View):
    message = disnake.Message
    def __init__(self, author):
      self.author = author
      super().__init__(timeout=20)
    async def on_timeout(self):
      await self.message.edit(view=None)
    
      
    @disnake.ui.button(label="Next When",style=disnake.ButtonStyle.blurple, emoji="<a:emoji_35:986833323013844992>")
    async def blurple_button(self,button:disnake.ui.Button, i:disnake.MessageInteraction):
      if i.user.id == self.author.id:
        sc = aiohttp.ClientSession()
        async with sc.get(danbooru) as r:
          while True:
            try:
              data = await r.json()
              img = random.choice(data)['file_url']
              await i.response.edit_message(content=img)
              break
            except KeyError:
              continue
        await sc.close()
      else:
        await i.response.send_message('Không Phải Bạn', ephemeral=True)
        return False
class NevNsfw(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
 
  @commands.command()
  @commands.is_nsfw()
  @commands.cooldown(1, 20, commands.BucketType.user)
  async def nsfw(self, ctx):
    sc = aiohttp.ClientSession()
    async with sc.get(danbooru) as r:
      while True:
        try:
          data = await r.json()
          img = random.choice(data)['file_url']
          view = BtnNsfw(ctx.author)
          view.message = await ctx.send(img, view=view)
          break
        except KeyError:
          continue
    await sc.close()
def setup(bot):
  bot.add_cog(NevNsfw(bot))