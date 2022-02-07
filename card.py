from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton,QLabel,QGridLayout
from PyQt5 import uic
import sys
import random





class Ui(QMainWindow):


	def __init__(self):
		super(Ui, self).__init__()

		#load the file
		uic.loadUi("card.ui",self)
		self.setWindowTitle("Deal Cards")

		#define our widegts
		self.dealerLabel = self.findChild(QLabel,"dealer_card")
		self.playerLabel = self.findChild(QLabel,"player_card")
		self.dealerHeadLabel = self.findChild(QLabel,"label_3")
		self.playerHeadLabel = self.findChild(QLabel,"player")
		self.shuffleBtn = self.findChild(QPushButton,"pushButton")
		self.dealBtn= self.findChild(QPushButton,"pushButton_2")


		self.shuffle()


		#connect the widgets

		self.shuffleBtn.clicked.connect(self.shuffle)
		self.dealBtn.clicked.connect(self.deal)


		#show the app
		self.show()

	def shuffle(self):
		#define the deck
		suits =["D","C","S","H"]
		values = range(2,15)
		#11= jack,12= queen...

		#create deck
		global deck
		self.deck =[]

		for suit in suits:
			for value in values:
				self.deck.append(f"{value}{suit}")

		#create our players
		#global player,dealer
		self.dealer=[]
		self.player=[]

		#grab a random card from dealer
		card1 = random.choice(self.deck)

		#remove that above card
		self.deck.remove(card1)
		#add that card to dealer list
		self.dealer.append(card1)

		#output to screen
		pixmap = QPixmap(f'C:/Users/Lovely/Desktop/cards/cc/{card1}.jpg')
		self.dealerLabel.setPixmap(pixmap)


		
		#grab a random card from dealer
		card1 = random.choice(self.deck)

		#remove that above card
		self.deck.remove(card1)
		#add that card to dealer list
		self.player.append(card1)

		#output to screen
		pixmap = QPixmap(f'C:/Users/Lovely/Desktop/cards/cc/{card1}.jpg')
		self.playerLabel.setPixmap(pixmap)

		self.setWindowTitle(f"{len(self.deck)} left ")




		



	def deal(self):
		#self.setWindowTitle("deals")
		#define the deck

		try:
			suits =["D","C","S","H"]
			values = range(2,15)
			#11= jack,12= queen...
			#create deck
			global deck
			self.deck =[]

			for suit in suits:
				for value in values:
					self.deck.append(f"{value}{suit}")

			#create our players
			#global player,dealer
			self.dealer=[]
			self.player=[]

			#grab a random card from dealer
			card1 = random.choice(self.deck)
	         # Remove That Card From The Deck
			self.deck.remove(card1)
			# Add That Card To Dealers List
			self.player.append(card1)

			#output to screen
			pixmap = QPixmap(f'C:/Users/Lovely/Desktop/cards/cc/{card1}.jpg')
			self.dealerLabel.setPixmap(pixmap)
				#grab a random card from dealer
			card1 = random.choice(deck)

				# Remove That Card From The Deck
			self.deck.remove(card1)
			# Add That Card To Dealers List
			self.player.append(card1)

			#output to screen
			pixmap = QPixmap(f'C:/Users/Lovely/Desktop/cards/cc/{card1}.jpg')
			self.playerLabel.setPixmap(pixmap)
			print(len(deck))
			self.setWindowTitle(f"{len(self.deck)} left ")
			

		except:
			self.setWindowTitle("GameOver")




		

		pass











#initialize the app
app= QApplication(sys.argv)
UIWindow = Ui()
app.exec_()
