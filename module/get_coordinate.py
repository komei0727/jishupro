# -*- coding: utf-8 -*-

import cv2
import csv
import numpy as np

class mouseParam:
    def __init__(self, input_img_name):
        #マウス入力用のパラメータ
        self.mouseEvent = {"x":None, "y":None, "event":None, "flags":None}
        #マウス入力の設定
        cv2.setMouseCallback(input_img_name, self.__CallBackFunc, None)

    #コールバック関数
    def __CallBackFunc(self, eventType, x, y, flags, userdata):

        self.mouseEvent["x"] = x
        self.mouseEvent["y"] = y
        self.mouseEvent["event"] = eventType
        self.mouseEvent["flags"] = flags

    #マウス入力用のパラメータを返すための関数
    def getData(self):
        return self.mouseEvent

    #マウスイベントを返す関数
    def getEvent(self):
        return self.mouseEvent["event"]

    #マウスフラグを返す関数
    def getFlags(self):
        return self.mouseEvent["flags"]

    #xの座標を返す関数
    def getX(self):
        return self.mouseEvent["x"]

    #yの座標を返す関数
    def getY(self):
        return self.mouseEvent["y"]

    #xとyの座標を返す関数
    def getPos(self):
        return (self.mouseEvent["x"], self.mouseEvent["y"])


if __name__ == "__main__":
    #入力画像
    read = cv2.imread("あ.jpg")

    #表示するWindow名
    window_name = "input window"

    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    #画像の表示
    cv2.imshow(window_name, read)

    #コールバックの設定
    mouseData = mouseParam(window_name)

    X = []
    Y = []
    while 1:
        cv2.waitKey(20)
        #左クリックがあったら表示
        if mouseData.getEvent() == cv2.EVENT_LBUTTONDOWN:
            if X == []:
                X.append(mouseData.getX())
                Y.append(mouseData.getY())
                print(mouseData.getPos())
            elif X[-1] != mouseData.getX() or Y[-1] != mouseData.getY():
                X.append(mouseData.getX())
                Y.append(mouseData.getY())
                print(mouseData.getPos())

        #右クリックがあったら終了
        elif mouseData.getEvent() == cv2.EVENT_RBUTTONDOWN:
            break;


    cv2.destroyAllWindows()
    print(X)
    print(Y)
    print("Finished")

    with open('data/あ_original_2.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(np.array([X,Y]).T)
