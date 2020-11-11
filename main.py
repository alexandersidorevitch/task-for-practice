from OrderBook import OrderBook
from Reader import Reader


def main():
    reader = Reader('1.txt')
    order_book = OrderBook()
    for el in reader.get_from_file():
        order_book.parse_operation(*el)
    print(order_book.get_total())


if __name__ == '__main__':
    main()
