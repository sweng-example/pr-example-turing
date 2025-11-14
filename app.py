from model import LocalDatabaseModel
from view import ConsoleView
from presenter import Presenter

Presenter(LocalDatabaseModel(), ConsoleView()).run()

# TODO
# teach skimming -- make it clear this PR is from a colleague, don't expect them to read the JSON
