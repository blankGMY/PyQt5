import sys
import MainWinVHLayout
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()     #创建主窗口
    ui = MainWinVHLayout.Ui_MainWindow()  #调用转换代码的Ui_MainWindow方法
    #向主窗口添加控件
    ui.setupUi(mainWindow)      #setupUi是Ui_MainWindow方法里的函数
    mainWindow.show()
    sys.exit(app.exec_())