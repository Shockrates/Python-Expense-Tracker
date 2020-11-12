import sys

from main_window import MainWindow
from expenseform_window import ExpenseForm
from PySide2.QtWidgets import QApplication, QHeaderView
from controllers.main_controller import MainController


# Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    app = QApplication(sys.argv)

    #iNITIALLIZE VIEWS AND CONTROLLERS
    # view =  [MainWindow(), ExpenseForm()]
    #main_controller=MainController(view=view)
    main_controller=MainController()

    # Show the application's GUI
    # view[0].show()
    # main_controller.showMainWindow()

    # Execute the application's main loop
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()