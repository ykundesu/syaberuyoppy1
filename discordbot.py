import discord
from gtts import gTTS
from discord.ext import commands,tasks
import time
#from urllib.parse import 
Intents = discord.Intents.default()
Intents.members = True
client = discord.Client(intents=Intents)
@tasks.loop(seconds=60)
async def change_activity():
    # 「○○をプレイ中」の内容を変更します
    await client.change_presence(
        activity=discord.Game(name=f'sy!helpで使い方/作成:よっキング#8329|{len(client.guilds)}サーバーで導入されています'))
@change_activity.before_loop
async def before_change_activity():
    # botがログインするまで(on_readyが発火するまで）待機します
    await client.wait_until_ready()
# tasks.loop を開始します
change_activity.start()
@client.event
async def on_message(message):
 if message.content == "sy!join":
    if message.author.voice is None:
        await message.channel.send("あなたはボイスチャンネルに接続していません。")
        return
    # ボイスチャンネルに接続する
    await message.author.voice.channel.connect()
    await message.channel.send("""```
やっほー!喋るよっぴーだよー!どんどん喋るで!
ヘルプはsy!helpから!```
""")
    output = gTTS(text="やっほー！。。喋るよっぴーだよ!よろしくねー!",lang="ja", slow=False)
    output.save("しゃべるよっぴー.mp3")
    message.guild.voice_client.play(discord.FFmpegPCMAudio("しゃべるよっぴー.mp3"))
 elif message.content == "sy!kick":
        if message.guild.voice_client is None:
            await message.channel.send("接続していません。")
            return

        # 切断する
        await message.guild.voice_client.disconnect()

        await message.channel.send("切断しました。")
 elif message.content == "sy!help":
        embed = discord.Embed(title="使い方・ヘルプ", description="作成:よっキング#8329")
        embed.add_field(name="sy!help",value="へるぷ!")
        embed.add_field(name="sy!join",value="あなたが入ってるボイスチャンネルに入ります")
        embed.add_field(name="sy!kick", value="ボイスチャンネルからでます")
        #embed.add_field(name="!clch", value="チャンネルを削除")
        embed.add_field(name="詳しくはこちら!",value="https://qiita.com/yokingkun/items/8817905de232f8081fea")
 else:
     if message.author.bot:
        return
     if "https://" in message.content:
         msgtext="ゆーあーるえる"
     elif "http://" in message.content:
         msgtext="ゆーあーるえる"
     else:
      msgtext=message.content
      henkanlist={"w":"わら","(":"かっこ",")":"かっこ","?":"はてな","（":"かっこ","）":"かっこ","\\n":"。。","「":"かぎかっこ","」":""}
      for henkan in henkanlist:
       msgtext=msgtext.replace(str(henkan),str(henkanlist[henkan]))
     myText = message.author.display_name+"。。。。。"+msgtext
     language ='ja'
     output = gTTS(text=myText, lang=language, slow=False)
     output.save(msgtext.replace("/","")+".mp3")
     try:
      message.guild.voice_client.play(discord.FFmpegPCMAudio(msgtext.replace("/","")+".mp3"))
     except:
      time.sleep(6)
      message.guild.voice_client.play(discord.FFmpegPCMAudio(msgtext.replace("/","")+".mp3"))
     message.guild.pause()
token="ODA5MzMzNjczMzA3Nzk5NTYz.YCTkuA.SRdyopYG6BMtikRoH2jev-rdFr"+"w"
client.run(token)
