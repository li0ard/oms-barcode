# oms-barcode
![](https://img.shields.io/badge/author-%40li0ard-blue.svg?maxAge=3600&style=flat-square)
![](https://img.shields.io/github/license/li0ard/oms-barcode.svg?maxAge=3600&style=flat-square)

Класс на Python для чтения данных с штрихкода полиса ОМС

### Использование

Декодирование штрихкода в 2 шагах:
- Инициализируйте класс `OMSBarcode`
- Вызовите метод `fromString` у класса и передайте в аргумент содержимое штрихкода

Пример использования:

![](https://habrastorage.org/webt/7t/pt/25/7tpt25vktae0q5zzsija8qo1cbg.png)

```py
from oms_barcode import OMSBarcode

oms = OMSBarcode()
oms.fromString("020016E959AF0F3A6C9DB3A17503BF84E869B9C3BF39C3A175AA5341C3800000000000000000000000000000000000000000000000000000000000000283EB0000015CEA680D9CDDEF0209E9F91FFEA628328CD157144B634204BAC30F573FF2E1021BDC2A28B2DD50A2761E4CF75FFCDBFBA71EAFC548AD07D38DC82A7D674BD09A")

print("Фамилия: " + oms.last)
print("Имя: " + oms.first)
print("Отчество: " + oms.middle)
print("Д/р: " + oms.dob)
print("Пол: " + oms.sex)
print("Номер ОМС: " + oms.number)
print("Срок годности: " + oms.exp)
print("ЭЦП: " + oms.signature)
```

### Свойства класса

- `last` - Фамилия владельца
- `first` - Имя владельца
- `middle` - Отчество владельца
- `dob` - Дата рождения владельца в формате ДД.ММ.ГГГГ
- `sex` - Пол владельца (М/Ж)
- `number` - Номер полиса ОМС
- `exp` - Срок годности полиса в формате ДД.ММ.ГГГГ (00.00.0000 если без срока действия)
- `signature` - ЭЦП полиса ОМС
