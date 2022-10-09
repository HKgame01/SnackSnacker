import funct
import telebot

API_KEY = ""

bot = telebot.TeleBot(API_KEY)
print("Bot is running!")
@bot.message_handler(commands=['start'])
def greet(message):
  bot.send_message(message.chat.id, "Hello, Welcome, please write /help to see the commands available.")

@bot.message_handler(commands=['help'])
def hello(message):
  bot.send_message(message.chat.id, """Available Commands :-
  /about - We made this bot so that we can enjoy food in a different way
  /moodfood - It recommends food according to your mood
  /nearme - Gives the places where you can go to have food near you
  /new - It will randomly tell something new about some food iam with a video on it
	""")


@bot.message_handler(commands=['about'])
def about(message):
  bot.send_message(message.chat.id, "We made this bot so that we can enjoy food in a different way!")

@bot.message_handler(commands=['moodfood'])
def moodfood(message):
  mood = bot.send_message(message.chat.id, "How are you feeling?")
  t = funct.mooddetect(mood)
  bot.send_message(message.chat.id, "t")

@bot.message_handler(commands=['nearme'])
def nearme(message):
  bot.send_message(message.chat.id, "https://www.google.com/maps/search/restaurants+near+me/@28.5130829,77.2323597,15z")


@bot.message_handler(commands=['new'])
def new(message):
  t = funct.random()
  bot.send_message(message.chat.id, "t")

@bot.message_handler(commands=['exit'])
def exottt(message):
  exit()

bot.polling()
