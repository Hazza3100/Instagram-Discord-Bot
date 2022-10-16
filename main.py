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

    def get_post(self, post_id):
        try:
            headers = {'authority': 'www.instagram.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'en-GB,en;q=0.9','cache-control': 'max-age=0','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',}
            response = self.session.get(f'https://www.instagram.com/p/{post_id}/', headers=headers).text
            return response.split('postPage_')[1].split('"')[0]
        except:
            print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} Post does not exist")

    def follow(self, user_id):
        try:
            cookie = random.choice(open('cookies.txt', 'r').read().splitlines())
            headers = {'authority': 'www.instagram.com','accept': '*/*','accept-language': 'en-GB,en-US;q=0.9,en;q=0.8','content-type': 'application/x-www-form-urlencoded','cookie': f'sessionid={cookie}','origin': 'https://www.instagram.com','sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36','x-csrftoken': '2SAvFYoHgS8GwleiP7j5vTLPqRJX4IFL','x-requested-with': 'XMLHttpRequest',}

            r = self.session.post(f'https://www.instagram.com/web/friendships/{user_id}/follow/', headers=headers)
        except:
            print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} Error")

    def unfollow(self, user_id):
        try:
            cookie = random.choice(open('cookies.txt', 'r').read().splitlines())
            headers = {'authority': 'www.instagram.com','accept': '*/*','accept-language': 'en-GB,en-US;q=0.9,en;q=0.8','content-type': 'application/x-www-form-urlencoded','cookie': f'sessionid={cookie}','origin': 'https://www.instagram.com','sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36','x-csrftoken': '2SAvFYoHgS8GwleiP7j5vTLPqRJX4IFL','x-requested-with': 'XMLHttpRequest',}

            r = self.session.post(f'https://www.instagram.com/web/friendships/{user_id}/unfollow/', headers=headers)
        except:
            print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} Error")

    def like(self, postID):
        try:
            cookie = random.choice(open('cookies.txt', 'r').read().splitlines())
            headers = {'authority': 'www.instagram.com','accept': '*/*','accept-language': 'en-GB,en;q=0.9','content-type': 'application/x-www-form-urlencoded','cookie': f'sessionid={cookie}','origin': 'https://www.instagram.com','referer': f'https://www.instagram.com/p/{postID}/','sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36','x-csrftoken': 'eB8F8DBi9fUrycehIas063lomgcrfwLS','x-requested-with': 'XMLHttpRequest',}
            
            r = self.session.post(f'https://www.instagram.com/web/likes/{postID}/like/', headers=headers)
        except:
            print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} Error")

    def comment(self, postID, message):
        try:
            cookie = random.choice(open('cookies.txt', 'r').read().splitlines())
            headers = {'authority': 'www.instagram.com','accept': '*/*','accept-language': 'en-GB,en;q=0.9','cookie': f'sessionid={cookie}','origin': 'https://www.instagram.com','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36','viewport-width': '1083','x-asbd-id': '198387','x-csrftoken': 'kebImKHMQVjftn79AU80A0pqW4ugYOfA','x-requested-with': 'XMLHttpRequest',}
            data = {'comment_text': message, 'replied_to_comment_id': '',}

            r = requests.post(f'https://www.instagram.com/web/comments/{postID}/add/', headers=headers, data=data)
        except:
            print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} Error")



@bot.command()
async def igfollow(ctx, username):
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
async def igunfollow(ctx, username):
    if ctx.channel.id == channel_1 or ctx.channel.id == channel_2:
        config = open('config.json', 'r').read()
        role_config = json.loads(config)['Roles']
        for role_name in role_config:
            threads = cfg['Roles'][role_name]
            role_id = discord.utils.get(ctx.guild.roles, name=role_name)
            if role_id in ctx.author.roles:
                
                embed = discord.Embed(title="Instagram Unfollowers", description=f"Removing `{threads}` followers from `{username}`", color=color)
                await ctx.send(embed=embed)
                x = backend()
                user_id = x.get_id(username)
                for _ in range(threads):
                    threading.Thread(target=x.unfollow, args=(user_id,)).start()


@bot.command()
async def iglike(ctx, postID):
    if ctx.channel.id == channel_1 or ctx.channel.id == channel_2:
        config = open('config.json', 'r').read()
        role_config = json.loads(config)['Roles']
        for role_name in role_config:
            threads = cfg['Roles'][role_name]
            role_id = discord.utils.get(ctx.guild.roles, name=role_name)
            if role_id in ctx.author.roles:
                
                embed = discord.Embed(title="Instagram Likes", description=f"Sending `{threads}` likes to `{postID}`", color=color)
                await ctx.send(embed=embed)
                x = backend()
                post_ID = x.get_post(postID)
                for _ in range(threads):
                    threading.Thread(target=x.like, args=(post_ID,)).start()

                    

@bot.command()
async def igcomment(ctx, postID):
    if ctx.channel.id == channel_1 or ctx.channel.id == channel_2:
        config = open('config.json', 'r').read()
        role_config = json.loads(config)['Roles']
        for role_name in role_config:
            threads = cfg['Roles'][role_name]
            role_id = discord.utils.get(ctx.guild.roles, name=role_name)
            if role_id in ctx.author.roles:
                
                embed = discord.Embed(title="Instagram Comments", description=f"Sending `{threads}` Comments to `{postID}`", color=color)
                await ctx.send(embed=embed)
                x = backend()
                post_ID = x.get_post(postID)
                for _ in range(threads):
                    threading.Thread(target=x.comment, args=(post_ID,)).start()


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Instagram Discord", description="github.com/hazza3100", color=color)
    embed.add_field(name="Help Embed", value=f"```{prefix}help```", )
    embed.add_field(name="Instagram Follow", value=f"```{prefix}igfollow <username>```", inline=False)
    embed.add_field(name="Instagram Unfollow", value=f"```{prefix}igunfollow <username>```", inline=False)
    embed.add_field(name="Instagram Like", value=f"```{prefix}iglike <postID>```", inline=False)
    embed.add_field(name="Instagram Comment", value=f"```{prefix}igcomment <postID>```", inline=False)
    await ctx.send(embed=embed)
                    
                    
                    
                    
                    
                    
bot.run(token)
