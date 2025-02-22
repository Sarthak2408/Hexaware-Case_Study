from datetime import date

class Vehicle:
    def __init__(self, make: str, model: str, year: int, daily_rate: float, status: str, passenger_capacity: int, engine_capacity: float, vehicle_id = None):
        self.__vehicle_id = vehicle_id
        self.__make = make
        self.__model = model
        self.__year = year
        self.__daily_rate = daily_rate
        self.__status = status
        self.__passenger_capacity = passenger_capacity
        self.__engine_capacity = engine_capacity
    
    # Setters
    def set_vehicle_id(self, vehicle_id: int) -> None:
        self.__vehicle_id = vehicle_id

    def set_make(self, make: str) -> None:
        self.__make = make

    def set_model(self, model: str) -> None:
        self.__model = model

    def set_year(self, year: int) -> None:
        self.__year = year

    def set_daily_rate(self, daily_rate: float) -> None:
        self.__daily_rate = daily_rate

    def set_passenger_capacity(self, passenger_capacity: int) -> None:
        self.__passenger_capacity = passenger_capacity

    def set_engine_capacity(self, engine_capacity: float) -> None:
        self.__engine_capacity = engine_capacity

    def set_status(self, status) -> None:
        self.__status = status

    # Getters
    def get_vehicle_id(self):
        return self.__vehicle_id

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_daily_rate(self):
        return self.__daily_rate

    def get_passenger_capacity(self):
        return self.__passenger_capacity

    def get_engine_capacity(self):
        return self.__engine_capacity

    def get_status(self):
        return self.__status



class Customer:
    def __init__(self, first_name: str, last_name: str, email: str, phone_number: str, customer_id = None):
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone_number = phone_number

    # Setters
    def set_customer_id(self, customer_id: int) -> None:
        self.__customer_id = customer_id

    def set_first_name(self, first_name: str) -> None:
        self.__first_name = first_name

    def set_last_name(self, last_name: str) -> None:
        self.__last_name = last_name

    def set_email(self, email: str) -> None:
        self.__email = email

    def set_phone_number(self, phone_number: str) -> None:
        self.__phone_number = phone_number

    # Getters
    def get_customer_id(self) -> int:
        return self. __customer_id

    def get_first_name(self) -> str:
        return self.__first_name

    def get_last_name(self) -> str:
        return self.__last_name

    def get_email(self) -> str:
        return self.__email

    def get_phone_number(self) -> str:
        return self.__phone_number



class Lease:
    def __init__(self, vehicle_id: int, customer_id: int, start_date: date, end_date: date, type: str, lease_id = None):
        self.__lease_id = lease_id
        self.__vehicle_id = vehicle_id
        self.__customer_id = customer_id
        self.__start_date = start_date
        self.__end_date = end_date
        self.__type = type

    # Setters
    def set_lease_id(self, lease_id: int) -> None:
        self.__lease_id = lease_id

    def set_vehicle_id(self, vehicle_id: int) -> None:
        self.__vehicle_id = vehicle_id

    def set_customer_id(self, customer_id: int) -> None:
        self.__customer_id = customer_id

    def set_start_date(self, start_date: date) -> None:
        self.__start_date = start_date

    def set_end_date(self, end_date: date) -> None:
        self.__end_date = end_date

    def set_lease_type(self, type: str) -> None:
        self.__type = type

    # Getters
    def get_lease_id(self) -> int:
        return self.__lease_id

    def get_vehicle_id(self) -> int:
        return self.__vehicle_id

    def get_customer_id(self) -> int:
        return self.__customer_id

    def get_start_date(self) -> date:
        return self.__start_date

    def get_end_date(self) -> date:
        return self.__end_date

    def get_type(self) -> str:
        return self.__type
    

class Payment:
    def __init__(self, lease_id: int, payment_date: str, amount: float, payment_id = None):
        self.__payment_id = payment_id
        self.__lease_id = lease_id
        self.__payment_date = payment_date
        self.__amount = amount

    # Setters
    def set_payment_id(self, payment_id: int) -> None:
        self.__payment_id = payment_id

    def set_lease_id(self, lease_id: int) -> None:
        self.__lease_id = lease_id

    def set_payment_date(self, payment_date: str) -> None:
        self.__payment_date = payment_date

    def set_amount(self, amount: float) -> None:
        self.__amount = amount

    # Getters
    def get_payment_id(self) -> int:
        return self.__payment_id

    def get_lease_id(self) -> int:
        return self.__lease_id

    def get_payment_date(self) -> str:
        return self.__payment_date

    def get_amount(self) -> float:
        return self.__amount

