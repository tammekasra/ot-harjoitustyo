import unittest

from maksukortti import Maksukortti


class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)

    def test_alussa_oikein(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_edullisesti()

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.50 euroa")

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_maukkaasti()

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6.00 euroa")

    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(200)
        kortti.syo_edullisesti()

        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")

    def test_kortille_voi_ladata_rahaa(self):
        self.kortti.lataa_rahaa(2500)

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 35.00 euroa")
    def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
        self.kortti.lataa_rahaa(20000)

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 150.00 euroa")
    def test_kortin_saldo_maukkaasti(self):
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti() #Meilla on vain  2 euro jaljella, ja siita emme saa pienentaa sita rahaa lainkaan
        self.assertEqual((str(self.kortti)),"Kortilla on rahaa 2.00 euroa")
    def test_ei_menee_negatiiviseksi(self):
        kortti = Maksukortti(-3)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")    
    def test_Rahan_lataaminen_kasvattaa_saldoa_oikein2(self):
        self.kortti.lataa_rahaa(25100)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 250.00 euroa")
        self.kortti.syo_maukkaasti()
        self.kortti.syo_edullisesti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 240.50 euroa")