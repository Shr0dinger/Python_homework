class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def get_data(obj):
        if obj.day >= 1 and obj.day <= 31:
            if obj.month >= 1 and obj.month <= 12:
                if obj.year >= 1 and obj.year <= 9999:
                    return f"Данные введены верно: день - {obj.day}, месяц -  {obj.month}, год -  {obj.year}"
                else:
                    print("Неверный формат года")
                    exit()
            else:
                print("Неверный формат месяца")
                exit()
        else:
            print("Неверный формат дня месяца")
            exit()

    @classmethod
    def set_data(cls, data):
        n = data.split("-")
        n = [int(i) for i in n]
        return cls(n[0], n[1], n[2])


lst_1 = "13-05-1977"
one = Data.set_data(lst_1)
print(Data.get_data(one))
