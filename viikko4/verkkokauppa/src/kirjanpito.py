class Kirjanpito:
    """Luokka kirjanpidon tapahtumien tallentamiseen."""
    def __init__(self):
        self.tapahtumat = []

    def lisaa_tapahtuma(self, tapahtuma):
        self.tapahtumat.append(tapahtuma)


kirjanpito = Kirjanpito()
