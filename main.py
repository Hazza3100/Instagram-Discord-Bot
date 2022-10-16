import json
import random
import discord
import requests
import threading

from colorama import Fore
from discord.ext import commands

with open('config.json') as f:
    cfg = json.load(f)

token     = cfg['Config']['token']
prefix    = cfg['Config']['prefix']
color     = cfg['Config']['color']
channel_1 = cfg['Config']['channel_1']
channel_2 = cfg['Config']['channel_2']

bot = commands.Bot(command_prefix=prefix, help_command=None, intents=discord.Intents.all())



class backend:
    def __init__(self) -> None:
        self.session = requests.Session()
        
    def get_id(self, username):
        try:
            headers = {'authority': 'i.instagram.com','accept': '*/*','accept-language': 'en-GB,en-US;q=0.9,en;q=0.8','origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36','x-csrftoken': '2SAvFYoHgS8GwleiP7j5vTLPqRJX4IFL','x-ig-app-id': '936619743392459',}
            params = {'username': username,}
            r = self.session.get('https://i.instagram.com/api/v1/users/web_profile_info/', params=params, headers=headers)
            return r.text.split('"id":"')[2].split('"')[0]
        except:
            print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} User does not exist")


    def follow(self, user_id):
        try:
            cookie = random.choice(open('cookies.txt', 'r').read().splitlines())
            headers = {'authority': 'www.instagram.com','accept': '*/*','accept-language': 'en-GB,en-US;q=0.9,en;q=0.8','content-type': 'application/x-www-form-urlencoded','cookie': f'sessionid={cookie}','origin': 'https://www.instagram.com','sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36','x-csrftoken': '2SAvFYoHgS8GwleiP7j5vTLPqRJX4IFL','x-requested-with': 'XMLHttpRequest',}

            r = self.session.post(f'https://www.instagram.com/web/friendships/{user_id}/follow/', headers=headers)
        except:
            print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} Error")




@bot.command()
async def ig(ctx, username):
    if ctx.channel.id == channel_1 or ctx.channel.id == channel_2:
        config = open('config.json', 'r').read()
        role_config = json.loads(config)['Roles']
        for role_name in role_config:
            threads = cfg['Roles'][role_name]
            role_id = discord.utils.get(ctx.guild.roles, name=role_name)
            if role_id in ctx.author.roles:
                
                embed = discord.Embed(title="Instagram Followers", description=f"Sending `{threads}` followers to `{username}`", color=color)
                await ctx.send(embed=embed)
                x = backend()
                user_id = x.get_id(username)
                for _ in range(threads):
                    threading.Thread(target=x.follow, args=(user_id,)).start()



@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Instagram Discord", description="github.com/hazza3100", color=color)
    embed.add_field(name="Help Embed", value=f"```{prefix}help```", )
    embed.add_field(name="Instagram Followers", value=f"```{prefix}ig username```", inline=False)
    await ctx.send(embed=embed)
                    
                    
                    
                    
                    
                    
bot.run(token)
