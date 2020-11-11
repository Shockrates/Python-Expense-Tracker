import sys

from main_window import MainWindow
from PySide2.QtWidgets import QApplication, QHeaderView
from controllers.main_controller import MainController


# Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    app = QApplication(sys.argv)

    #iNITIALLIZE VIEWS AND CONTROLLERS
    view =  MainWindow()
    main_controller=MainController(view=view)

    # Show the application's GUI
    view.show()

    # Execute the application's main loop
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()