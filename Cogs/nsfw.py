from disnake.ext import commands
import random, aiohttp
from .mmbeo import api

class nsfw1(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
      
  @commands.command(name="4k")
  @commands.is_nsfw()
  async def _4k(self, ctx):
    async with aiohttp.ClientSession() as sc:
      async with sc.get(api.nekobot+"4k") as r:
        i = await r.json()
        await ctx.reply(i['message'], mention_author=False)
    
  @commands.command("69")
  @commands.is_nsfw()
  async def _69(self, ctx):
    api.tags = '69'
    await ctx.reply(str(api.dan_booru()), mention_author=False)
   

  @commands.command()
  @commands.is_nsfw()
  async def doggy(self, ctx):
    api.tags = 'doggystyle'
    await ctx.reply(str(api.dan_booru()), mention_author=False)
  
  @commands.command()
  @commands.is_nsfw()
  async def femboy(self, ctx):
    async with aiohttp.ClientSession() as sc:
      async with sc.get("https://ahni.dev/v2/nsfw/img?end=irlfemb", headers={'Authorization': 'FM73C949-H9UN-LZTG-UMJF-UPJYT5UPNQZ3'}) as r:
        i = await r.json()
        await ctx.reply(i['result'], mention_author=False)
    
  @commands.command()
  @commands.is_nsfw()
  async def pee(self, ctx):
    api.tags = 'peeing'
    await ctx.reply(str(api.dan_booru()), mention_author=False)
    
    
  @commands.command()
  @commands.is_nsfw()
  async def teacher(self, ctx):
    api.tags = 'teacher'
    await ctx.reply(str(api.dan_booru()), mention_author=False)    
    
  @commands.command()
  @commands.is_nsfw()
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def azurlane(self, ctx):
    api.tags = 'azur_lane'
    i = 0
    while i < 5:
      img = await api.dan_booru()
      await ctx.reply(str(img), mention_author=False)
      i += 1
      
  @commands.command()
  @commands.is_nsfw()
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def genshin(self, ctx):
    api.tags = 'genshin_impact'
    i = 0
    while i < 5:
      img = await api.dan_booru()
      await ctx.reply(str(img), mention_author=False)
      i += 1
      
      
  @commands.command()
  @commands.is_nsfw()
  async def cosplay(self, ctx):
    sc = aiohttp.ClientSession()
    while True:
      try:
        link = ["https://www.reddit.com/r/nsfwcosplay/random.json","https://www.reddit.com/r/cosplaynation/random.json", "https://www.reddit.com/r/cosplaybabes/random.json","https://www.reddit.com/r/cosplaybutts/random.json"]
        url = random.choice(link)
        async with sc.get(url) as r:
          res = await r.json()
        img = res[0]['data']['children'][0]['data']['url']
        if img.endswith(('.jpg', '.png', '.gif', '.jpeg', 'webm', 'tiff', 'bmp', 'mp4')):
          await ctx.reply(img, mention_author=False)
          break
        else:
          continue
      except KeyError:
        continue
    await sc.close()


  @commands.command()
  @commands.is_nsfw()
  async def kitchen(self, ctx):
    api.tags = 'kitchen'
    await ctx.reply(str(api.dan_booru()), mention_author=False)

  @commands.command()
  @commands.is_nsfw()
  async def futa(self, ctx):
    api.tags = 'futanari'
    await ctx.reply(str(api.dan_booru()), mention_author=False)
  
  @commands.command()
  @commands.is_nsfw()
  async def furry(self, ctx):
    async with aiohttp.ClientSession() as sc:
      async with sc.get("https://sheri.bot/api/yiff?format=json") as r:
        i = await r.json()
        await ctx.reply(i['url'], mention_author=False)
            
  
  @commands.command()
  @commands.is_nsfw()
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def xray(self, ctx):
    api.tags = 'x-ray'
    i = 0
    while i < 5:
      img = await api.dan_booru()
      await ctx.reply(str(img), mention_author=False)
      i += 1
      
  @commands.command()
  @commands.is_nsfw()
  async def nun(self, ctx):
    api.tags = 'nun'
    await ctx.reply(str(api.dan_booru()), mention_author=False)
  
  @commands.command()
  @commands.is_nsfw()
  async def leash(self, ctx):
    api.tags = 'leash'
    await ctx.reply(str(api.dan_booru()), mention_author=False)
  
  @commands.command()
  @commands.is_nsfw()
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def hololive(self, ctx):
    api.tags = 'hololive'
    i = 0
    while i < 5:
      img = await api.dan_booru()
      await ctx.reply(str(img), mention_author=False)
      i += 1
      
  @commands.command()
  @commands.is_nsfw()
  async def milf(self, ctx):
    api.tags = 'milf'
    await ctx.reply(str(api.dan_booru()), mention_author=False)

  @commands.command()
  @commands.is_nsfw()
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def honkai(self, ctx):
    api.tags = 'honkai_(series)'
    i = 0
    while i < 5:
      img = await api.dan_booru()
      await ctx.reply(str(img), mention_author=False)
      i += 1
      
  @commands.command()
  @commands.is_nsfw()
  async def pregnant(self, ctx):
    api.tags = 'pregnant'
    await ctx.reply(str(api.dan_booru()), mention_author=False)
  
  @commands.command()
  @commands.is_nsfw()
  async def swimsuit(self, ctx):
    api.tags = 'swimsuit'
    await ctx.reply(str(api.dan_booru()), mention_author=False)
    
  @commands.command()
  @commands.is_nsfw()
  async def succubus(self, ctx):
    api.tags = 'succubus'
    await ctx.reply(str(api.dan_booru()), mention_author=False)
    
  @commands.command()
  @commands.is_nsfw()
  async def tentacle(self, ctx):
    api.tags = 'tentacles'
    await ctx.reply(str(api.dan_booru()), mention_author=False)
  
  @commands.command()
  @commands.is_nsfw()
  async def bunny(self, ctx):
    api.tags = 'rabbit_ears'
    await ctx.reply(str(api.dan_booru()), mention_author=False)
    

  @commands.command()
  @commands.is_nsfw()
  async def mastur(self, ctx):
    api.tags = 'masturbation'
    await ctx.reply(str(api.dan_booru()), mention_author=False)

  @commands.command()
  @commands.is_nsfw()
  async def blarch(self, ctx):
    api.tags = 'blue_archive'
    await ctx.reply(str(api.dan_booru()), mention_author=False)
  
  @commands.command()
  @commands.is_nsfw()
  async def arknights(self, ctx):
    api.tags = 'arknights'
    await ctx.reply(str(api.dan_booru()), mention_author=False)

  @commands.command()
  @commands.is_nsfw()
  async def bdsm(self, ctx):
    sc = sc = aiohttp.ClientSession()
    while True:
      try:
        link = ["https://www.reddit.com/r/bdsm/random.json","https://www.reddit.com/r/bondage/random.json", "https://www.reddit.com/r/BDSMGW/random.json"]
        url = random.choice(link)
        async with sc.get(url) as r:
          res = await r.json()
        img = res[0]['data']['children'][0]['data']['url']
        if img.endswith(('.jpg', '.png', '.gif', '.jpeg', 'webm', 'tiff', 'bmp', 'mp4')):
          await ctx.reply(img, mention_author=False)
          break
        else:
          continue
      except KeyError:
        continue
    await sc.close()
  
  @commands.command()
  @commands.is_nsfw()
  async def hentai(self, ctx):
    api.tags = 'sex+video'
    await ctx.reply(str(api.dan_booru()), mention_author=False)

  @commands.command()
  @commands.is_nsfw()
  async def latex(self, ctx):
    async with aiohttp.ClientSession() as sc:
      async with sc.get("https://ahni.dev/v2/nsfw/img?end=latex", headers={'Authorization': 'FM73C949-H9UN-LZTG-UMJF-UPJYT5UPNQZ3'}) as r:
        i = await r.json()
        await ctx.reply(i['result'], mention_author=False)
    
  @commands.command()
  @commands.is_nsfw()
  async def neko(self, ctx):
    api.tags = 'cat_girl'
    await ctx.reply(str(api.dan_booru()), mention_author=False)

  @commands.command()
  @commands.is_nsfw()
  async def pov(self, ctx):
    api.tags = 'pov'
    await ctx.reply(str(api.dan_booru()), mention_author=False)

  @commands.command()
  @commands.is_nsfw()
  async def wafuku(self, ctx):
    api.tags = 'japanese_clothes'
    await ctx.reply(str(api.dan_booru()), mention_author=False)

  @commands.command()
  @commands.is_nsfw()
  async def trap(self, ctx):
    api.tags = 'trap'
    await ctx.reply(str(api.dan_booru()), mention_author=False)

  @commands.command()
  @commands.is_nsfw()
  async def yaoi(self, ctx):
    api.tags = 'yaoi'
    await ctx.reply(str(api.dan_booru()), mention_author=False)

  @commands.command()
  @commands.is_nsfw()
  async def yuri(self, ctx):
    api.tags = 'yuri'
    await ctx.reply(str(api.dan_booru()), mention_author=False)

  @commands.command()
  @commands.is_nsfw()
  async def cow(self, ctx):
    api.tags = 'cow_print'
    await ctx.reply(str(api.dan_booru()), mention_author=False)

def setup(bot):
  bot.add_cog(nsfw1(bot))
  