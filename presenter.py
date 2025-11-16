class Presenter:
    """Presenter dans l'architecture MVP de l'app, qui gère les commandes utilisateur."""

    def __init__(self, model, view):
        """Crée un Presenter avec un modèle et une view donnés."""
        self.model = model
        self.view = view

    def _show_list(self, lst):
        """Affiche la liste donnée via la view."""
        self.view.show("\n".join(["- " + str(s) for s in lst]))

    def onInput(self, command):
        """Gère l'entrée utilisateur d'une commande donnée."""
        if command == "liste":
            self._show_list(self.model.names())
            return

        parts = command.split(' ')
        if parts[0] == "reccerche":
            # TODO: Recherche partielle (ou peut-être expressions régulières ?)
            names = self.model.names()
            self._show_list([n for n in names if parts[0] in n])
            return

        if parts[0] == "traduire":
            self._show_list(self.model.translated_names(parts[1]))
            return

        self.view.show("Commande inconnue")

    def run(self):
        """Gère l'entrée utilisateur d'une commande donnée."""
        self.view.show("Bonjour! Cette application vous donne des informations sur les groupes d'étoiles.")
        self.view.run(self, "Écrivez 'liste', 'recherche <texte>', ou 'traduire <langue>' (ou Ctrl+C): ")
