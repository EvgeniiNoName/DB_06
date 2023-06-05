import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Shop, Book, Stock, Sale

def create_engine():
    info =list()

    with open("info.txt") as f:
        for line in f:
            info.append(line.rstrip('\n'))

    login = info[0]
    password = info[1]
    name_database = info[2]

    DSN = (f'postgresql://{login}:{password}@localhost:5432/{name_database}')
    engine = sqlalchemy.create_engine(DSN)

    return engine

def adding_data():
    with open('fixtures/tests_data.json', 'r') as fd:
        data = json.load(fd)

    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]
        session.add(model(id=record.get('pk'), **record.get('fields')))
        session.commit()

def get_info(id_name):
    q = session.query(Book, Publisher, Shop, Stock, Sale
    ).select_from(Shop
    ).join(Stock
    ).join(Book
    ).join(Publisher
    ).join(Sale
    )
    if id_name.isdigit():
        subq = q.filter(Publisher.id == id_name).all()
    else:
        subq = q.filter(Publisher.name == id_name).all()
    for book, publisher, shop, stock, sale  in subq:
        print(f' {book.title: <40} | {shop.name: <10} | {sale.price: <5} | {sale.date_sale.strftime("%d-%m-%Y")} ')

if __name__ == '__main__':

    engine = create_engine()
    create_tables(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    adding_data()
    id_name = input("Введите Фамилию или ID автора: ")
    get_info(id_name)
    session.close()


