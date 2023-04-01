import unittest
from oms_barcode import OMSBarcode

class TestOMS(unittest.TestCase):
	def setUp(self):
		self.v1 = OMSBarcode()
		self.v1.fromString("010016E959AF0F3A6C53E684D37771CEEF39DF38711DE4FCD27685DF35419C03000000000000000000000000000000000000000271D3000000EF4A04BDB800F618017DDE3F6B9C4B4592FB28EB75EF1E0D2274BD0F57377284F02469698A8CAC4A912FE74D773AF6FC0C8D71515CB88176EC04A414B179AD00AC548295033972DC82")
		self.v2 = OMSBarcode()
		self.v2.fromString("0200000000363D804E9DB3A17503BF84E869B9C3BF39C3A175AA5341C3800000000000000000000000000000000000000000000000000000000000000283EB0000015CEA680D9CDDEF0209E9F91FFEA628328CD157144B634204BAC30F573FF2E1021BDC2A28B2DD50A2761E4CF75FFCDBFBA71EAFC548AD07D38DC82A7D674BD09A")
	def test_V1(self):
		self.assertEqual(self.v1.last, "ПАРФЕНОВА")
		self.assertEqual(self.v1.first, "ЕКАТЕРИНА")
		self.assertEqual(self.v1.middle, "ДМИТРИЕВНА")
		self.assertEqual(self.v1.dob, "13.10.1979")
		self.assertEqual(self.v1.number, "6449020886006380")
		self.assertEqual(self.v1.okato, "63000")
		self.assertEqual(self.v1.ogrn, "1027739008440")
		self.assertEqual(self.v1.sex, "Ж")
		self.assertEqual(self.v1.exp, "00.00.0000")
		self.assertEqual(self.v1.signature, "017DDE3F6B9C4B4592FB28EB75EF1E0D2274BD0F57377284F02469698A8CAC4A912FE74D773AF6FC0C8D71515CB88176EC04A414B179AD00AC548295033972DC82")

	def test_V2(self):
		self.assertEqual(self.v2.last, "ШМАТОВА")
		self.assertEqual(self.v2.first, "ТАТЬЯНА")
		self.assertEqual(self.v2.middle, "АНАТОЛЬЕВНА")
		self.assertEqual(self.v2.dob, "18.06.1992")
		self.assertEqual(self.v2.number, "0000000910000206")
		self.assertEqual(self.v2.sex, "Ж")
		self.assertEqual(self.v2.exp, "00.00.0000")
		self.assertEqual(self.v2.signature, "015CEA680D9CDDEF0209E9F91FFEA628328CD157144B634204BAC30F573FF2E1021BDC2A28B2DD50A2761E4CF75FFCDBFBA71EAFC548AD07D38DC82A7D674BD09A")

if __name__ == "__main__":
	unittest.main()