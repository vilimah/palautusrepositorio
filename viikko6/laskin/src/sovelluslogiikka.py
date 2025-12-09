class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._historia = []

    def miinus(self, operandi):
        self._historia.append(self._arvo)
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._historia.append(self._arvo)
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._historia.append(self._arvo)
        self._arvo = 0

    def kumoa(self):
        """Palauta edelliseen arvoon historiasta."""
        if self._historia:
            self._arvo = self._historia.pop()

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo
