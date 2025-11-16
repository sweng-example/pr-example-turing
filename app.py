from model import LocalDatabaseModel
from view import ConsoleView
from presenter import Presenter

Presenter(LocalDatabaseModel(), ConsoleView()).run()
