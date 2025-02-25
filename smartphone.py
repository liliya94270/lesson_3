from smartphone import Smartphone


catalog = []
catalog.append(Smartphone("Honor", "50","8996-153-430-33"))
catalog.append(Smartphone("Huawei", "P20", "8995-123-36-37"))
catalog.append(Smartphone("Iphone", "XS", "8965-456-65-44"))
catalog.append(Smartphone("Samsung", "S20", "8994-567-74-46"))
catalog.append(Smartphone("Realme", "c61", "8995-243-33-67"))


for phone in catalog:
   print(f'{phone.phone_brand}, {phone.phone_model}, {phone.number}')