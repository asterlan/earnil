import botogram
import os

bot = botogram.create('376118437:AAHGUTat7yo67cQEKNweuWoVHPkjiCswfbk')

TOKEN = '376118437:AAHGUTat7yo67cQEKNweuWoVHPkjiCswfbk'
PORT = int(os.environ.get('PORT', '5000'))
updater = Updater(TOKEN)
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.setWebhook("https://earnil.herokuapp.com/" + TOKEN)
updater.idle()

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
