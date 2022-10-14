import requests, disnake, aiohttp
tags = None
async def dan_booru():
    while True:
      try:
        async with aiohttp.ClientSession() as sc:
          async with sc.get(f"https://danbooru.donmai.us/posts/random.json?tags=is:nsfw+{tags}&api_key=Z56sewvSbtL6eVXYn6J4uZ7P&login=DoonG") as data:
            i = await data.json()
            return i['file_url']
      except KeyError:
        continue 
  
nekobot = "https://nekobot.xyz/api/image?type="
danbooru = "https://danbooru.donmai.us/posts/random.json?tags=is:nsfw+"
dankey = ""