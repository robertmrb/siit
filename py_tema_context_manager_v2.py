import contextlib


# Class with KeyError (Dictionary)

class KeyErrorClass:
    def __init__(self):
        self.auto_price = {
            'Opel': 12300,
            'Dacia': 10500,
            'Volvo': 21000,
            'Fiat': 15300
        }

    def __enter__(self):
        return self.auto_price

    def __exit__(self, exc_type, exc_value, traceback):
        car_brand = input('Input car brand: ')

        try:
            print(f'The price for {car_brand} is {self.auto_price[car_brand]} euro.')
        except KeyError as keyerr:
            print(f"{keyerr} it's not in our offert.")


with KeyErrorClass() as dict_key_class:
    print('-' * 50)
    print(dict_key_class)


# Generator with KeyError (Dictionary)

@contextlib.contextmanager
def key_error_generator():
    auto_price_key_g = {
        'Opel': 12300,
        'Dacia': 10500,
        'Volvo': 21000,
        'Fiat': 15300
    }
    car_brand_key = input('Input car brand: ')

    try:
        yield auto_price_key_g
        print(f'The price for {car_brand_key} is {auto_price_key_g[car_brand_key]} euro.')
    except KeyError as keyerrc:
        print(f"{keyerrc} its not in our offert.")
    finally:
        return


with key_error_generator() as dict_key_gen:
    print('-' * 50)
    print(dict_key_gen)


# Class with IndexError (List)

class IndexErrorClass:
    def __init__(self):
        self.auto_list = ['Opel', 'Dacia', 'Volvo', 'Fiat']

    def __enter__(self):
        return self.auto_list

    def __exit__(self, exc_type, exc_value, traceback):
        number = input("Enter a number to view what car is: ")

        try:
            print(f"The car is:  {self.auto_list[int(number)]}")
        except IndexError:
            print(f'This is not in list')
        finally:
            return


with IndexErrorClass() as list_index_class:
    print('-' * 50)
    print(list_index_class)


# Generator with IndexError (List)

@contextlib.contextmanager
def index_error_generator():
    list_auto = ['Opel', 'Dacia', 'Volvo', 'Fiat']
    print(list_auto)
    number = input("Enter a number to view what car is: ")

    try:
        yield list_auto
        print(f"The car is: {list_auto[int(number)]}")
    except IndexError:
        print(f'This is not in list')
    finally:
        return


with index_error_generator() as list_index_gen:
    print('-' * 50)
    print(list_index_gen)
