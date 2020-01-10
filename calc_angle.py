import cv2
import csv
import numpy as np
from module.get_coordinate import mouseParam
from module.calc_coordinate import calc_coordinate
from module.inverse_kinematics import inverse_kinematics

image = "image/よ.jpg"
original_data = "data/よ_original_2.csv"
data = "data/よ_2.csv"
#angle_data = "angle_data/あ_2.csv"

if __name__ == "__main__":
    # 入力画像
    read = cv2.imread(image)

    # 表示するWindow名
    window_name = "input window"

    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    # 画像の表示
    cv2.imshow(window_name, read)

    # コールバックの設定
    mouseData = mouseParam(window_name)

    X = []
    Y = []
    while 1:
        cv2.waitKey(20)
        # 左クリックがあったら表示
        if mouseData.getEvent() == cv2.EVENT_LBUTTONDOWN:
            if X == []:
                X.append(mouseData.getX())
                Y.append(mouseData.getY())
                print(mouseData.getPos())
            elif X[-1] != mouseData.getX() or Y[-1] != mouseData.getY():
                X.append(mouseData.getX())
                Y.append(mouseData.getY())
                print(mouseData.getPos())

        # 右クリックがあったら終了
        elif mouseData.getEvent() == cv2.EVENT_RBUTTONDOWN:
            break

    cv2.destroyAllWindows()
    print("Finished")

    with open(original_data, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(np.array([X, Y]).T)

    calc_coordinate(original_data, data)
    #inverse_kinematics(data, angle_data)
