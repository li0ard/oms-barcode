import datetime

class OMSBarcode:
	bitmap_type = ""
	last = ""
	first = ""
	middle = ""
	dob = ""
	sex = ""

	#Только тип №1
	ogrn = ""
	okato = ""
	
	number = ""
	exp = ""
	signature = ""

	charTable = [
		[' ', '.', '-', '‘', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'А', 'Б'],
		['В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р'],
		['С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ъ', 'Ы', 'Э', 'Ю', 'Я', '*'],
		['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '|']
	]

	def FindSNPEnd(self, start, sbuffer):
		i = start
		while i < (len(sbuffer) - 2):
			if sbuffer[i] + sbuffer[i + 1] == 0 and sbuffer[i + 2] < 3 and sbuffer[i + 2] > 0:
				return i+1
			i = i + 1

	def hextobin(self, hexval):
		thelen = len(hexval)*4
		binval = bin(int(hexval, 16))[2:]
		while ((len(binval)) < thelen):
			binval = '0' + binval
		return binval

	def fromString(self, string):
		self.bitmap_type = string[0:2]
		if string[0:2] == "01":
			self.number = str(int(string[2:18], 16)).zfill(16)

			snpBuffer = bytearray.fromhex(string)[9:42]
			snpBuffer.reverse()
			snpBuffer = ''.join('{:02x}'.format(x) for x in snpBuffer)
			snpChar = []
			s = self.hextobin(snpBuffer)
			s = [s[i:i+6] for i in range(0,len(s),6)]
			for i in s:
				snpChar.append(self.charTable[int(int(i, 2)/16)][int(int(i, 2)%16)])
			snpChar = "".join(snpChar).strip().split("|")
			self.last = snpChar[1][::-1]
			self.first = snpChar[2][::-1]
			self.middle = snpChar[0][::-1]

			if str(string[51*2:51*2+2]) == "01":
				self.sex = "М"
			else:
				self.sex = "Ж"
			
			self.dob = int(string[52*2:52*2+4], 16)
			self.dob = (datetime.datetime.strptime('1900-01-01', "%Y-%m-%d") + datetime.timedelta(days=self.dob)).strftime('%d.%m.%Y')

			self.exp = int(string[54*2:54*2+4],16)
			if self.exp > 0:
				self.exp = (datetime.datetime.strptime('1900-01-01', "%Y-%m-%d") + datetime.timedelta(days=self.exp)).strftime('%d.%m.%Y')
			else:
				self.exp = "00.00.0000"

			self.ogrn = str(int(string[56*2:56*2+12], 16))
			self.okato = str(int(string[62*2:62*2+6], 16))
			self.signature = string[65*2:]
		else:
			self.number = str(int(string[2:18], 16)).zfill(16)
			snpEnd = self.FindSNPEnd(9, bytearray.fromhex(string))
			if str(string[(snpEnd+1)*2:(snpEnd+1)*2+2]) == "01":
				self.sex = "М"
			else:
				self.sex = "Ж"
			self.dob = int(string[(snpEnd+2)*2:(snpEnd+2)*2+4],16)
			self.dob = (datetime.datetime.strptime('1900-01-01', "%Y-%m-%d") + datetime.timedelta(days=self.dob)).strftime('%d.%m.%Y')
			self.exp = int(string[(snpEnd+4)*2:(snpEnd+4)*2+4],16)
			if self.exp > 0:
				self.exp = (datetime.datetime.strptime('1900-01-01', "%Y-%m-%d") + datetime.timedelta(days=self.exp)).strftime('%d.%m.%Y')
			else:
				self.exp = "00.00.0000"
			self.signature = string[65*2:]

			snpBuffer = bytearray.fromhex(string)[9:snpEnd-8]
			snpBuffer = ''.join('{:02x}'.format(x) for x in snpBuffer)
			snpChar = []
			s = self.hextobin(snpBuffer)
			s = [s[i:i+6] for i in range(0,len(s),6)]
			for i in s:
				snpChar.append(self.charTable[int(int(i, 2)/16)][int(int(i, 2)%16)])
			snpChar = "".join(snpChar).strip().split("|")
			self.last = snpChar[0]
			self.first = snpChar[1]
			self.middle = snpChar[2]