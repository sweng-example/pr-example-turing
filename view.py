class ConsoleView:
    def show(self, text):
        # Affiche `text` sur la console
        print(text)

    def run(self, presenter, prompt):
        while True:
            command = input(prompt)
            presenter.onInput(command)
