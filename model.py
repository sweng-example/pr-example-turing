import json

class LocalDatabaseModel:
    """Modèle utilisant une base de donnée locale en JSON"""
    def __init__(self):
        # `utf-8` pour être sûr que le fichier est lu correctement quel que soit l'OS
        with open("dsonames.json", "r+", encoding="utf-8") as f:
            self.values = json.load(f)
            sorted(self.values)

    def names(self):
       """Obtient la liste des noms, en anglais, des objets disponibles"""
       result = []
       for _, planet in self.values.items():
           result.append(planet["name"])
       return result

    def translated_names(self, language):
       """Obtient une correspondance entre noms et noms traduits dans la langue donnée."""
        return [(p["name"], p[language]) for p in self.values.values() if language in p]
