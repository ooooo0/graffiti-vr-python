from BotDraw import *

bot = Bot()

bot.saveLocation("start")




#======================================================================

bot.moveToLocation("start")
bot.color = "red"
for x in range(0,10):
	bot.drawBox(1,1,1)
	bot.moveUp(1)
	bot.forward(1)


#======================================================================

bot.moveToLocation("start")
bot.moveRight(-10)
bot.color = "blue"
for k in range(0,10):
	bot.drawBox(1,1,1)
	bot.moveUp(1)
	bot.moveLeft(1)

#======================================================================

bot.moveToLocation("start")
bot.moveRight(10)
bot.color = "green"
for k in range(0,10):
	bot.drawBox(1,1,1)
	bot.moveUp(1)
	bot.moveRight(1)

#======================================================================

bot.moveToLocation("start")
bot.moveRight(20)
bot.color = "purple"
for k in range(0,10):
	bot.drawBox(1,1,1)
	bot.moveUp(1)
	bot.forward(-1)


sceneMaker = SceneMaker()
sceneMaker.Save(bot.getElements(),"index.html")
print("Scene created.")

