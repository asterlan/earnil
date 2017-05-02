import botogram
import requests

bot = botogram.create('376118437:AAHGUTat7yo67cQEKNweuWoVHPkjiCswfbk')
#url = "https://api.telegram.org/bot376118437:AAHGUTat7yo67cQEKNweuWoVHPkjiCswfbk/"

@bot.command("hello")
def hello_command(chat, message, args):
    """Say hello to the world!"""
    chat.send("Hello world")

@bot.command("myaf")
def myaf_command(chat, message, args):
    """Say hello to the world!"""
    chat.send("Kot kot")

if __name__ == "__main__":
    bot.run()
