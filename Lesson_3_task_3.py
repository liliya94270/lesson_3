from address import Address
from mailing import Mailing

to_address = Address(index= "450000", city: "Уфа", street: "Цюрупа", house: "84", apartment: "6")
from_addrees =Address(index= "450001", city: "Янаул", street: "Победы", house: "101", apartment: "3")
mailing =Mailing(to_address="1247890h", from_address,  to_address track:"17" )

print(mailing)


#Распечатайте в консоль отправление в формате:
# Отправление <track>
#  из <индекс>, <город>, <улица>, <дом> -<квартира>
# в <индекс>, <город>, <улица>, <дом>-<квартира>.
# Стоимость <стоимость> рублей.
