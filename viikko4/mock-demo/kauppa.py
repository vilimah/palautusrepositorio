class Kauppa:
    def __init__(self, pankki, viitegeneraattori):
        self._pankki = pankki
        self._viitegeneraattori = viitegeneraattori
        self._yhteishinta = 0

    def aloita_ostokset(self):
        """Aloittaa uuden ostosession."""
        self._yhteishinta = 0

    def lisaa_ostos(self, hinta):
        """Lisää tuotteen ostoskoriin."""
        self._yhteishinta = self._yhteishinta + hinta

    def maksa(self, tilinumero):
        """Suorittaa ostosten maksun."""
        self._pankki.maksa(
            tilinumero,
            self._yhteishinta,
            self._viitegeneraattori.uusi()
        )
