"""
Bithumb Auto Trading Program
with GUI
Byunghyun Ban
https://github.com/needleworm
"""

import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets as Q
from PyQt5.QtCore import *
import time
from pybithumb import Bithumb as B


doing_job = False

from ui import Ui_Dialog
ui_class = Ui_Dialog

coin_list = ["-"] + B.get_tickers()


class autoTrader(QThread):
    text_out = pyqtSignal(str)

    def __init__(self, access_token, secret_key, coin, buyPrice, sellPrice):
        super().__init__()
        self.access_token = access_token
        self.secret_key = secret_key
        self.coin = coin
        self.buyPrice = buyPrice
        self.sellPrice = sellPrice

    def sell_all(self, trader):
        qty = trader.get_balance(self.coin)
        price = B.get_current_price(self.coin)
        if price < self.sellPrice:
            return None, None
        if qty <= 0:
            return None, None

        trader.sell_limit_order(self.coin, price, qty)
        QtGui.QGuiApplication.processEvents()
        splt = str(qty).split(".")
        qtyStr = splt[0] + "." + splt[-1][:6]
        return "TRY> Coin Limit sell\t" + str(time.ctime()) + "\nPrice: " + str(price) + "\tQuantity: " + qtyStr + "\n", price * qty

    def buy_all(self, trader):
        krw = trader.get_balance("KRW")
        price = B.get_current_price(self.coin)
        if price > self.buyPrice:
            return None, None
        qty = krw / price
        qty -= qty % 0.0001
        if qty <= 0:
            return None, None

        trader.buy_limit_order(self.coin, price, qty)
        QtGui.QGuiApplication.processEvents()
        splt = str(qty).split(".")
        qtyStr = splt[0] + "." + splt[-1][:6]
        return "TRY> Coin Limit Buy\t" + str(time.ctime()) + "\nPrice: " + str(price) + "\tQuantity: " + qtyStr + "\n", price * qty

    def run(self):
        global doing_job, latest_message
        if doing_job:
            self.text_out.emit("Auto Trading Bot Initiated.")

            self.text_out.emit("Target Coin : " + self.coin + "\n")
            latest_message = ""
            bithumb = B(self.access_token, self.secret_key)
        else:
            self.text_out.emit("Stop Auto Trading.\n\n")
        while doing_job:
            QtGui.QGuiApplication.processEvents()
            lastBuyWon = None
            lastSellWon = None

            coinPrice = B.get_current_price(self.coin)
            if coinPrice < self.buyPrice:
                message, lastBuyWon = self.buy_all(bithumb)
                if not message:
                    continue
                elif message[:20] == latest_message:
                    continue
                elif message:
                    self.text_out.emit(message)
                    latest_message = message[:20]
                    QtGui.QGuiApplication.processEvents()
            elif coinPrice > self.sellPrice:
                message, lastSellWon = self.sell_all(bithumb)
                if not message:
                    continue
                elif message[:20] == latest_message:
                    continue
                elif message:
                    self.text_out.emit(message)
                    QtGui.QGuiApplication.processEvents()
                    latest_message = message[:20]
                    if lastSellWon and lastBuyWon:
                        self.text_out.emit("Income : " + str(lastSellWon - lastBuyWon) + "￦\n\n")
                        QtGui.QGuiApplication.processEvents()
            time.sleep(0.5)


class SetCoin(QThread):
    text_out = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def change(self, price):
        self.text_out.emit(price)
        QtGui.QGuiApplication.processEvents()


class WindowClass(Q.QMainWindow, ui_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.doing_job = False

        self.coin = ""
        self.access_token = ""
        self.secret_key = ""
        self.buyPrice = 0
        self.sellPrice = 0

        # 코인명 콤보박스에 업로드
        self.comboBox.addItems(coin_list)

        # 코인명이 바뀔 경우 코인명을 업데이트함
        self.comboBox.currentIndexChanged.connect(self.set_coin)

        # 버튼이 눌릴 경우 작업을 시작합니다.
        self.pushButton.clicked.connect(self.button_pushed)

    def button_pushed(self):
        if self.coin == "-":
            return

        # 정보 불러오기
        self.access_token = self.lineEdit.text().strip()
        self.secret_key = self.lineEdit_2.text().strip()
        self.buyPrice = int(self.lineEdit_3.text())
        self.sellPrice = int(self.lineEdit_4.text())
        self.checked = self.checkBox.isChecked()

        if not (self.access_token and self.secret_key and self.buyPrice and self.sellPrice and self.coin and self.checked):
            return

        global doing_job
        doing_job = not doing_job
        if doing_job:
            self.pushButton.setText("Stop Auto Trading")
        else:
            self.pushButton.setText("Start Auto Trading")
        # 멀티스레드로 오토트레이딩
        self.Bot = autoTrader(self.access_token, self.secret_key, self.coin, self.buyPrice, self.sellPrice)
        self.Bot.text_out.connect(self.textBrowser.append)
        QtGui.QGuiApplication.processEvents()
        self.Bot.run()

    def set_coin(self):
        self.coin = self.comboBox.currentText()
        if self.coin != "-":
            currentPrice = B.get_current_price(self.coin)
        else:
            currentPrice = 0

        self.coinsetter1 = SetCoin()
        self.coinsetter1.text_out.connect(self.lineEdit_3.setText)
        self.coinsetter1.change(str(int(currentPrice * 0.996)))

        self.coinsetter2 = SetCoin()
        self.coinsetter2.text_out.connect(self.lineEdit_4.setText)
        self.coinsetter2.change(str(int(currentPrice * 1.004)))


if __name__ == "__main__":
    app = Q.QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    sys.exit(app.exec_)
