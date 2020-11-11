from collections import Counter
from dataclasses import dataclass


@dataclass(frozen=True)
class Order:
    time_stamp: int
    ID: int
    price: float


class OrderBook:
    """
    Class for store orders and
    """

    def __init__(self):
        self.__counter = Counter()
        self.__current_time_stamp = None
        self.__max_price = -1
        self.__functions = {'I': self.__append_order, 'E': self.__remove_order}
        self.__total_sum = 0
        self.__total_time_stamp = 0
        self.orders = dict()

    def parse_operation(self, *args) -> None:
        self.__functions.get(args[1])(*args)

    def __append_order(self, time_stamp: str, operation: str, ID: str, price: str) -> None:
        """
        Adding an order
        """
        price, time_stamp, ID = float(price), int(time_stamp), int(ID)
        if self.__current_time_stamp is None:
            self.__current_time_stamp = time_stamp
        # Increasing the number of items with the same price
        self.__counter[price] += 1
        # Check whether the price of the new order is higher than the previous ones
        if self.__max_price < price:
            self.__total_sum += self.__max_price * (time_stamp - self.__current_time_stamp)
            self.__total_time_stamp += time_stamp - self.__current_time_stamp
            self.__current_time_stamp = time_stamp
            self.__max_price = price
        # Adding an order
        self.orders[ID] = Order(price=price, time_stamp=time_stamp, ID=ID)

    def __remove_order(self, time_stamp: int, operation: str, ID: int) -> None:
        time_stamp, ID = int(time_stamp), int(ID)

        removed_order = self.orders.pop(ID, None)
        # Reducing  the number of items with the same price
        self.__counter[removed_order.price] -= 1

        if not self.__counter.get(removed_order.price):
            del self.__counter[removed_order.price]
            self.__total_sum += removed_order.price * (time_stamp - self.__current_time_stamp)
            self.__total_time_stamp += time_stamp - self.__current_time_stamp
            self.__current_time_stamp = time_stamp
            self.__max_price = self.max_price()

    def get_orders(self) -> tuple:
        return tuple(self.orders.values())

    def max_price(self) -> float:
        if self.__counter:
            return max(self.__counter.keys())
        else:
            return -1.0

    def get_total(self) -> float:
        if self.__total_time_stamp:
            return self.__total_sum / self.__total_time_stamp
        else:
            return .0
