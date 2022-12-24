import ui_view

if __name__ == "__main__":
    import sys
    app = ui_view.QtWidgets.QApplication(sys.argv)
    MainWindow = ui_view.QtWidgets.QMainWindow()
    ui = ui_view.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())