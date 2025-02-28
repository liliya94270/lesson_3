class Mailing:
    def __init__(self, to_adress, from_adress, cost, track):
        self.Adress = to_adress
        self.Adress = from_adress
        self.Num =cost
        self.Str = track

        def __str__(self):
            return F"{self.Str} из {self.Adress} в {self.Adress}. Стоимость {self.Num} рублей"
        

        #В классе должно быть четыре поля:
        # to_adress (тип данных Adress);
        # from_adress (тип данных Adress);
        # cost (тип данных число);
        # track (тип данных строка).

    
