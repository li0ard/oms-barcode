> [!WARNING]  
> **[Проект переписан на TypeScript](https://github.com/li0ard/oms_barcode). Данная версия является архивной и больше не поддерживается**

# oms-barcode
![](https://img.shields.io/badge/author-%40li0ard-blue.svg?maxAge=3600&style=flat-square)
![](https://img.shields.io/github/license/li0ard/oms-barcode.svg?maxAge=3600&style=flat-square)

Класс на Python для чтения данных с штрихкода полиса ОМС

### Использование

- Инициализируйте класс `OMSBarcode`
- Вызовите метод `fromString` у класса и передайте в аргумент содержимое штрихкода

Пример использования:

| **Тип 1** | **Тип 2** |
|:---------:|-----------|
| ![](https://habrastorage.org/webt/_c/9s/dm/_c9sdmop9jipq6inktpwxx_amr8.png) | ![](https://habrastorage.org/webt/oh/lu/8c/ohlu8c1ffiymxwl8byiodb9keya.png) |

```py
# 020016E959AF0F3A6C9DB3A17503BF84E869B9C3BF39C3A175AA5341C3800000000000000000000000000000000000000000000000000000000000000283EB0000015CEA680D9CDDEF0209E9F91FFEA628328CD157144B634204BAC30F573FF2E1021BDC2A28B2DD50A2761E4CF75FFCDBFBA71EAFC548AD07D38DC82A7D674BD09A
# 010016E959AF0F3A6C53E684D37771CEEF39DF38711DE4FCD27685DF35419C03000000000000000000000000000000000000000271D3000000EF4A04BDB800F618017DDE3F6B9C4B4592FB28EB75EF1E0D2274BD0F57377284F02469698A8CAC4A912FE74D773AF6FC0C8D71515CB88176EC04A414B179AD00AC548295033972DC82
oms = OMSBarcode()
oms.fromString("010016E959AF0F3A6C53E684D37771CEEF39DF38711DE4FCD27685DF35419C03000000000000000000000000000000000000000271D3000000EF4A04BDB800F618017DDE3F6B9C4B4592FB28EB75EF1E0D2274BD0F57377284F02469698A8CAC4A912FE74D773AF6FC0C8D71515CB88176EC04A414B179AD00AC548295033972DC82")

print("Фамилия: " + oms.last)
print("Имя: " + oms.first)
print("Отчество: " + oms.middle)
print("Д/р: " + oms.dob)
print("Пол: " + oms.sex)
print("Номер ОМС: " + oms.number)
print("Срок годности: " + oms.exp)
if oms.bitmap_type == "01":
	print("ОГРН: " + oms.ogrn)
	print("ОКАТО: " + oms.okato)
print("ЭЦП: " + oms.signature)
```

### Свойства и методы класса
- `bitmap_type` - Тип полиса
- `last` - Фамилия владельца
- `first` - Имя владельца
- `middle` - Отчество владельца
- `dob` - Дата рождения владельца в формате ДД.ММ.ГГГГ
- `sex` - Пол владельца (М/Ж)
- `number` - Номер полиса ОМС
- `exp` - Срок годности полиса в формате ДД.ММ.ГГГГ (00.00.0000 если без срока действия)
- `ogrn` - ОГРН страховой компании (Только тип №1)
- `okato` - ОКАТО филиала страховой компании (Только тип №1)
- `signature` - ЭЦП полиса ОМС
