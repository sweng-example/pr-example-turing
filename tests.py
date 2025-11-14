from unittest import TestCase

from model import LocalDatabaseModel
from presenter import Presenter

# Vérifions que les données soient bien chargées
class LocalDatabaseModelTests(TestCase):
    def test_names(self):
        m = LocalDatabaseModel()
        self.assertIn("Sextans Dwarf Spheroidal Galaxy", m.names())

    def test_translate(self):
        m = LocalDatabaseModel()
        self.assertIn(("Sextans Dwarf Spheroidal Galaxy", "Galaxie naine sphéroïdale du Sextant"), m.translated_names("fr"))


class FakeModel:
    def names(self):
        return ["X", "Y", "Z"]

    def translated_names(self, language):
        return [("X", "A"), ("Y", language), ("Z", "C")]

class FakeView:
    def __init__(self, inputs):
        self._inputs = inputs
        self.outputs = []

    def show(self, text):
        self.outputs.append(text)

    def run(self, presenter, prompt):
        if len(self._inputs) > 0:
            presenter.onInput(self._inputs[0])
            self._inputs = self._inputs[1:]

class PresenterTests(TestCase):
    def test_liste(self):
        v = FakeView(["liste"])
        p = Presenter(FakeModel(), v)
        self.assertEqual([], v.outputs)
        p.run()
        self.assertEqual(["Bonjour! Cette application vous donne des informations sur les groupes d'étoiles.", "- X\n- Y\n- Z"], v.outputs)

    def test_traduire(self):
        v = FakeView(["traduire fr"])
        p = Presenter(FakeModel(), v)
        self.assertEqual([], v.outputs)
        p.run()
        self.assertEqual(["Bonjour! Cette application vous donne des informations sur les groupes d'étoiles.", "- ('X', 'A')\n- ('Y', 'fr')\n- ('Z', 'C')"], v.outputs)
