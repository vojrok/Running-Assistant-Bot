from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(bot, update):
	print("Вызван /start")
	bot.sendMessage(update.message.chat_id, text = 'Физкульт привет, дорогой любитель бега!')

def info(bot, update):
	print("Вызван /info")
	bot.sendMessage(update.message.chat_id, text = 'Используй следующие команды для расчёта параметров: /heart - зоны ЧСС, /speed - скорость для преодоления интересующей дистанции.')

def heart(bot, update):
	print("Вызван /heart")
	bot.sendMessage(update.message.chat_id, text = 'Для какого возраста рассчитать зоны ЧСС?')

def speed(bot, update):
	print("Вызван /speed")
	bot.sendMessage(update.message.chat_id, text = 'Для какого расстояния рассчитать скорость?')

def talk_to_me(bot, update):
	print("Пришло сообщение: " + update.message.text)
	bot.sendMessage(update.message.chat_id, text = update.message.text)


def run_bot():
	updater = Updater("252570136:AAEpJkVi63xeP6eOC8Y1ab9UpE7NuCwFg84")

	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", start))

	dp = updater.dispatcher
	dp.add_handler(CommandHandler("info", info))

	dp = updater.dispatcher
	dp.add_handler(CommandHandler("heart", heart))

	dp = updater.dispatcher
	dp.add_handler(CommandHandler("speed", speed))

	dp.add_handler(MessageHandler([Filters.text], talk_to_me))

	updater.start_polling()
	updater.idle()

if __name__ == "__main__":
	run_bot()