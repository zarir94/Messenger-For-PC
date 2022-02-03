from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSizeGrip, QWidget
from PyQt5.QtCore import Qt, QSize, QRect, QPropertyAnimation
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from time import sleep
import sys
import os

dirpath=os.path.dirname(os.path.abspath(__file__))
js="function check(){elem=document.getElementsByClassName('is6700om');if(elem.length!=0){return 'Found'}else{return 'Not Found'}};check()"

class Check_Notification(QObject):
	progress = pyqtSignal()

	def run(self):
		while True:
			try:
				if win.loaded:
					self.progress.emit()
			except:
				continue
			sleep(5)

class Main(QtWidgets.QWidget):
	def __init__(self):
		super(Main, self).__init__()
		# =============== Edits ==========================================
		self.titletext='Messenger - Made by ZARIR'
		self.staytop=False
		self.ispop=False
		self.setWindowFlags(Qt.FramelessWindowHint)
		QtGui.QFontDatabase.addApplicationFont(dirpath+"\\Resourse\\icons.ttf")
		# ================================================================
		self.resize(400, 500)
		self.setMinimumSize(QtCore.QSize(410, 400))
		self.setStyleSheet('QWidget{border:1px solid rgb(56, 56, 56);}')
		self.vbox = QtWidgets.QVBoxLayout(self)
		self.vbox.setContentsMargins(0, 0, 0, 0)
		self.vbox.setSpacing(0)
		self.titlebar = QtWidgets.QFrame(self)
		self.titlebar.setMinimumSize(QtCore.QSize(0, 30))
		self.titlebar.setMaximumSize(QtCore.QSize(16777215, 30))
		self.titlebar.setStyleSheet("QFrame{background-color: rgb(56, 56, 56);}QPushButton{font-family: dripicons-v2;background: transparent;color: white;font-size: 20px;}QPushButton:hover{color: yellow;}QPushButton:pressed{font-size: 17px;}")
		self.titlebar.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.titlebar.setFrameShadow(QtWidgets.QFrame.Raised)
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.titlebar)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setSpacing(0)
		self.windowicon = QtWidgets.QPushButton(self.titlebar)
		self.windowicon.setMaximumSize(QtCore.QSize(20, 20))
		self.icon1 = QtGui.QIcon()
		self.icon1.addPixmap(QtGui.QPixmap(dirpath+"\\Resourse\\msnger.png"))
		self.icon2 = QtGui.QIcon()
		self.icon2.addPixmap(QtGui.QPixmap(dirpath+"\\Resourse\\msngernotify.png"))
		self.windowicon.setIcon(self.icon1)
		self.setWindowIcon(self.icon1)
		self.windowicon.setIconSize(QtCore.QSize(20, 20))
		self.windowicon.setFlat(False)
		self.windowicon.setObjectName("windowicon")
		self.horizontalLayout.addWidget(self.windowicon)
		self.windowtitle = QtWidgets.QLabel(self.titlebar)
		self.windowtitle.setMinimumSize(QtCore.QSize(0, 30))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.windowtitle.setFont(font)
		self.windowtitle.setStyleSheet("color: rgb(255, 255, 255);padding-bottom:5px;")
		self.windowtitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.windowtitle.setWordWrap(True)
		self.windowtitle.setIndent(5)
		self.horizontalLayout.addWidget(self.windowtitle)
		self.reloadButton = QtWidgets.QPushButton(self.titlebar)
		self.reloadButton.setMinimumSize(QtCore.QSize(25, 25))
		self.reloadButton.setMaximumSize(QtCore.QSize(25, 25))
		self.reloadButton.setStyleSheet("QPushButton{font-size: 16px;}QPushButton:pressed{font-size: 13px;}")
		self.horizontalLayout.addWidget(self.reloadButton)
		self.pinbtn = QtWidgets.QPushButton(self.titlebar)
		self.pinbtn.setMinimumSize(QtCore.QSize(25, 25))
		self.pinbtn.setMaximumSize(QtCore.QSize(25, 25))
		self.pinbtn.setStyleSheet("QPushButton{font-size: 15px;}QPushButton:pressed{font-size: 12px;}")
		self.horizontalLayout.addWidget(self.pinbtn)
		self.mutebtn = QtWidgets.QPushButton(self.titlebar)
		self.mutebtn.setMinimumSize(QtCore.QSize(25, 25))
		self.mutebtn.setMaximumSize(QtCore.QSize(25, 25))
		self.mutebtn.setStyleSheet("QPushButton{font-size: 16px;}QPushButton:pressed{font-size: 13px;}")
		self.horizontalLayout.addWidget(self.mutebtn)
		self.halfminButton = QtWidgets.QPushButton(self.titlebar)
		self.halfminButton.setMinimumSize(QtCore.QSize(25, 25))
		self.halfminButton.setMaximumSize(QtCore.QSize(25, 25))
		self.halfminButton.setStyleSheet("QPushButton{font-size: 16px;}QPushButton:pressed{font-size: 13px;}")
		self.halfminButton.setObjectName("halfminButton")
		self.horizontalLayout.addWidget(self.halfminButton)
		spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem)
		self.minButton = QtWidgets.QPushButton(self.titlebar)
		self.minButton.setMinimumSize(QtCore.QSize(25, 25))
		self.minButton.setMaximumSize(QtCore.QSize(25, 25))
		font = QtGui.QFont()
		font.setFamily("dripicons-v2")
		font.setPointSize(1)
		self.minButton.setFont(font)
		self.horizontalLayout.addWidget(self.minButton)
		self.maxButton = QtWidgets.QPushButton(self.titlebar)
		self.maxButton.setMinimumSize(QtCore.QSize(25, 25))
		self.maxButton.setMaximumSize(QtCore.QSize(25, 25))
		font = QtGui.QFont()
		font.setFamily("dripicons-v2")
		font.setPointSize(1)
		self.maxButton.setFont(font)
		self.maxButton.setStyleSheet("QPushButton{font-size: 14px;}QPushButton:pressed{font-size: 11px;}")
		self.horizontalLayout.addWidget(self.maxButton)
		self.closeButton = QtWidgets.QPushButton(self.titlebar)
		self.closeButton.setMinimumSize(QtCore.QSize(30, 30))
		self.closeButton.setMaximumSize(QtCore.QSize(30, 30))
		font = QtGui.QFont()
		font.setFamily("dripicons-v2")
		font.setPointSize(1)
		self.closeButton.setFont(font)
		self.closeButton.setStyleSheet("QPushButton{padding-right:5px;}QPushButton:hover{color:red;}")
		self.closeButton.setFlat(False)
		self.horizontalLayout.addWidget(self.closeButton)
		self.vbox.addWidget(self.titlebar)
		self.body = QtWidgets.QFrame(self)
		self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.body.setFrameShadow(QtWidgets.QFrame.Raised)
		self.verticalLayout = QtWidgets.QVBoxLayout(self.body)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setSpacing(0)
		self.loaded=False
#======================== Web Browser ======================================================
		self.browser = QWebEngineView(self.body)
		self.verticalLayout.addWidget(self.browser)
		self.browser.setUrl(QtCore.QUrl("https://www.messenger.com/login"))
		self.browser.loadFinished.connect(self.random983857845)
		# self.browser.page().profile().cookieStore().deleteAllCookies()



#===========================================================================================
		self.vbox.addWidget(self.body)

		self.retranslateUi()
		QtCore.QMetaObject.connectSlotsByName(self)
		#========================================
		self.titlebar.mousePressEvent=self.titlemousePressEvent
		self.titlebar.mouseMoveEvent=self.titlemouseMoveEvent
		self.titlebar.mouseReleaseEvent=self.titlemouseReleaseEvent
		self.gripSize = 8
		self.grips = []
		for i in range(2):
			grip = QSizeGrip(self)
			grip.resize(self.gripSize, self.gripSize)
			grip.setStyleSheet('border:none;')
			self.grips.append(grip)

	def onLoadFinished(self):
		js="function check(){elem=document.getElementsByClassName('is6700om');if(elem.length!=0){return 'Found'}else{return 'Not Found'}};check()"
		self.browser.page().runJavaScript(js, print)

	def random983857845(self, ok):
		if ok:
			self.loaded=True
		else:
			self.loaded=False

	def muteandunmute(self):
		if self.browser.page().isAudioMuted():
			self.browser.page().setAudioMuted(False)
			self.mutebtn.setStyleSheet("QPushButton{font-size: 16px;}QPushButton:pressed{font-size: 13px;}")
		else:
			self.browser.page().setAudioMuted(True)
			self.mutebtn.setStyleSheet("QPushButton{color: yellow;font-size: 16px;}QPushButton:pressed{font-size: 13px;}")

	def resizeEvent(self, event):
		QWidget.resizeEvent(self, event)
		rect = self.rect()
		self.grips[0].move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)
		self.grips[1].move(0, rect.bottom() - self.gripSize)

	def showdot(self):
		self.windowicon.setIcon(self.icon2)
		self.setWindowIcon(self.icon2)
		pop.showdot()


	def hidedot(self):
		try:
			self.windowicon.setIcon(self.icon1)
			self.setWindowIcon(self.icon1)
			pop.hidedot()
		except RuntimeError:
			pass

	def controlstaytop(self):
		if self.staytop:
			self.setWindowFlags(Qt.FramelessWindowHint)
			self.show()
			self.staytop=False
			self.pinbtn.setStyleSheet("QPushButton{font-size: 15px;}QPushButton:pressed{font-size: 11px;}")
		else:
			self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
			self.show()
			self.staytop=True
			self.pinbtn.setStyleSheet("QPushButton{color: yellow;font-size: 15px;}QPushButton:pressed{font-size: 12px;}")
		self.hidepopup()

	def titlemousePressEvent(self, event):
		self.start = self.mapToGlobal(event.pos())
		self.pressing = True

	def titlemouseMoveEvent(self, event):
		if self.pressing:
			self.end = self.mapToGlobal(event.pos())
			self.movement = self.end-self.start
			self.setGeometry(self.mapToGlobal(self.movement).x(),self.mapToGlobal(self.movement).y(),self.width(),self.height())
			self.start = self.end

	def titlemouseReleaseEvent(self, QMouseEvent):
		self.pressing = False

	def btn_close_clicked(self):
		self.close()

	def btn_max_clicked(self):
		if self.isMaximized():
			self.setWindowState(QtCore.Qt.WindowNoState)
			self.maxButton.setStyleSheet("QPushButton{font-size: 14px;}QPushButton:pressed{font-size: 11px;}")
			self.pinbtn.show()
		else:
			self.showMaximized()
			self.pinbtn.hide()
			self.maxButton.setStyleSheet("QPushButton{font-size: 14px;color:yellow}QPushButton:pressed{font-size: 11px;}")
			self.setWindowFlags(Qt.FramelessWindowHint)
			self.show()
			self.staytop=False
			self.pinbtn.setStyleSheet("QPushButton{font-size: 15px;}QPushButton:pressed{font-size: 11px;}")


	def btn_min_clicked(self):
		self.showMinimized()
		self.hidepopup()

	def showpopup(self):
		win.hide()
		pop.onclick=self.hidepopup
		pop.show()
		self.ispop=True

	def hidepopup(self):
		pop.hide()
		win.show()
		self.ispop=False

	def update_notification(self, response):
		if response=='Found':
			self.showdot()
		else:
			self.hidedot()

	def retranslateUi(self):
		self.setWindowTitle(self.titletext)
		self.windowtitle.setText(self.titletext)
		self.mutebtn.setText("")
		self.reloadButton.setText("Z")
		self.pinbtn.setText("")
		self.minButton.setText("")
		self.maxButton.setText("")
		self.halfminButton.setText("4")
		self.closeButton.setText("9")
		#====================
		self.closeButton.clicked.connect(self.btn_close_clicked)
		self.minButton.clicked.connect(self.btn_min_clicked)
		self.maxButton.clicked.connect(self.btn_max_clicked)
		self.mutebtn.clicked.connect(self.muteandunmute)
		self.pinbtn.clicked.connect(self.controlstaytop)
		self.halfminButton.clicked.connect(self.showpopup)
		self.reloadButton.clicked.connect(self.browser.reload)
		#========= Thread =============
		self.thread = QThread()
		self.worker = Check_Notification()
		self.worker.moveToThread(self.thread)
		self.thread.started.connect(self.worker.run)
		self.worker.progress.connect(lambda: self.browser.page().runJavaScript(js, self.update_notification))
		self.thread.start()


class PopUp(QtWidgets.QWidget):
	def __init__(self):
		super(PopUp, self).__init__()
		self.size=40
		self.hover=5
		self.duration=100
		self.maxsize=self.size + self.hover
		self.setWindowTitle(win.titletext)
		self.setMaximumSize(self.maxsize, self.maxsize)
		self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.verticalLayout = QtWidgets.QVBoxLayout(self)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setSpacing(0)
		self.btn = QtWidgets.QPushButton(self)
		self.btn.setMaximumSize(self.maxsize, self.maxsize)
		self.btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.btn.setStyleSheet("QPushButton{background: transparent;border - radius: 25px;}")
		self.icon1 = QtGui.QIcon()
		self.icon1.addPixmap(QtGui.QPixmap(dirpath+"\\Resourse\\msnger.png"))
		self.icon2 = QtGui.QIcon()
		self.icon2.addPixmap(QtGui.QPixmap(dirpath+"\\Resourse\\msngernotify.png"))
		self.btn.setIcon(self.icon1)
		self.btn.setIconSize(QSize(self.size, self.size))
		self.btn.setObjectName("btn")
		self.setWindowIcon(self.icon1)
		self.verticalLayout.addWidget(self.btn)
		self.btn.mousePressEvent=self.btnmousePressEvent
		self.btn.mouseMoveEvent=self.btnmouseMoveEvent
		self.btn.mouseReleaseEvent=self.btnmouseReleaseEvent
		self.btn.enterEvent=self.evententer
		self.btn.leaveEvent=self.eventleave
		self.moved=False
	def showdot(self):
		self.btn.setIcon(self.icon2)
		self.setWindowIcon(self.icon2)

	def hidedot(self):
		try:
			self.btn.setIcon(self.icon1)
			self.setWindowIcon(self.icon1)
		except RuntimeError:
			pass

	def evententer(self, event):
		self.anim = QPropertyAnimation(self.btn, b'iconSize')
		self.anim.setDuration(self.duration)
		self.anim.setStartValue(self.btn.iconSize())
		self.anim.setEndValue(QSize(self.maxsize, self.maxsize))
		self.anim.start()

	def eventleave(self, event):
		self.anim2 = QPropertyAnimation(self.btn, b'iconSize')
		self.anim2.setDuration(self.duration)
		self.anim2.setStartValue(self.btn.iconSize())
		self.anim2.setEndValue(QSize(self.size, self.size))
		self.anim2.start()

	def onclick(self):
		pass

	def btnmousePressEvent(self, event):
		self.start = self.mapToGlobal(event.pos())
		self.pressing = True

	def btnmouseMoveEvent(self, event):
		if self.pressing:
			self.moved=True
			self.end = self.mapToGlobal(event.pos())
			self.movement = self.end - self.start
			self.setGeometry(self.mapToGlobal(self.movement).x(),self.mapToGlobal(self.movement).y(),self.width(),self.height())
			self.start = self.end

	def btnmouseReleaseEvent(self, QMouseEvent):
		self.pressing = False
		if self.moved:
			self.moved=False
		else:
			self.onclick()




if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	win = Main()
	pop = PopUp()
	win.show()
	sys.exit(app.exec_())
