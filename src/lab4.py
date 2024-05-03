class Gem:
    def __init__(self, carats_number, cost, name):
        self.__carats_number = carats_number
        self.__cost = cost
        self.__name = name
        self.public_field_numeric = 0
        self.public_field_string = ""




    def __str__(self):
        return f"Gem: кількість каратів: {self.__carats_number}, ціна: {self.__cost}, назва каменю: {self.__name}"

    def __repr__(self):
        return f"Gem('{self.__carats_number}', {self.__cost}, '{self.__name}')"

    def get_carats_number(self):
        return self.__carats_number

    def get_cost(self):
        return self.__cost

    def get_name(self):
        return self.__name



    def __del__(self):
        print(f"Gem '{self.__name}' видалено")

def main():
    gem1 =Gem("1", 500, "diamond")
    gem2 = Gem("5", 100000, "emerald")
    gem3 = Gem("2", 500, "gemstone")

    print(gem1)
    print(gem2)
    print(gem3)


if __name__ == "__main__":
    main()


