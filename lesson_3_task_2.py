from smartphone import Smartphone


catalog = []
catalog.append(Smartphone(<Honor> - <50>. <+7996-153-430-33>.))
catalog.append(Smartphone(<Huawei> - <P20>. <+7995-123-36-37>.))
catalog.append(Smartphone(<Iphone> -  <XS>. <+7965-456-65-44>.))
catalog.append(Smartphone(<Samsung> - <S20>. <+7994-567-74-46>.))
catalog.append(Smartphone(<Realme> - <c61>. <+7995-243-33-67>.))


for phone in catalog:
   print(f'{phone.brand}, {phone.model}, {phone.number}')
