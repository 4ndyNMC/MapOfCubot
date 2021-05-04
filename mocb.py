import discord
from discord.ext import commands
from fastai.basic_train import load_learner
from fastai.vision import open_image
from fastai.vision import *
import urllib.request
from urllib.request import Request, urlopen
import json

with open('./config.json') as f:
    config = json.load(f)

bot = commands.Bot(
    command_prefix=config['prefix'], 
    case_insensitive=True,
    activity=discord.Game('on the sands of Havana'))

@bot.event
async def on_ready():
    # path = "C:\\Users\\tmgth\\Downloads"
    # learn = load_learner(path, file="export.pkl")
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def judge(ctx):
    path = "C:\\Users\\tmgth\\Documents\\discordbots\\mapofcubot"
    learn = load_learner(path, file="export.pkl")
    url = ctx.message.attachments[0].url

    f = open('cubamap.png','wb')
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    f.write(urllib.request.urlopen(req).read())
    f.close()
    img = open_image("cubamap.png")

    pred_class,pred_idx,outputs = learn.predict(img)

    if(str(pred_class) == "maps"):await ctx.send("That\'s a nice map of Cuba, bro!")
    else: await ctx.send("That is like not even a map of Cuba, bro!")

    # await ctx.send(ctx.message.attachments[0].url)

bot.run(config['token'])