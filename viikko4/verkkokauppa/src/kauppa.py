from ostoskori import Ostoskori

class Kauppa:
    """Luokka, joka vastaa verkkokaupan toiminnasta."""
    def __init__(self, varasto, pankki,viitegeneraattori):
        self._varasto = varasto
        self._pankki = pankki
        self._viitegeneraattori = viitegeneraattori
        self._kaupan_tili = "33333-44455"


    def aloita_asiointi(self):
        """Aloittaa uuden asiakastapahtuman."""
        self._ostoskori = Ostoskori()

    def poista_korista(self, id):
        """Poistaa tuotteen ostoskorista."""
        tuote = self._varasto.hae_tuote(id)
        self._ostoskori.poista(tuote)
        self._varasto.palauta_varastoon(tuote)

    def lisaa_koriin(self, id):
        """Lisää tuotteen ostoskoriin."""
        if self._varasto.saldo(id) > 0:
            tuote = self._varasto.hae_tuote(id)
            self._ostoskori.lisaa(tuote)
            self._varasto.ota_varastosta(tuote)

    def tilimaksu(self, nimi, tili_numero):
        """Suorittaa tilisiirron ostosten maksamiseksi."""
        viite = self._viitegeneraattori.uusi()
        summa = self._ostoskori.hinta()

        return self._pankki.tilisiirto(nimi, viite, tili_numero, self._kaupan_tili, summa)
