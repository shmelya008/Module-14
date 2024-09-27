import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')


# for i in range(1, 5):
#     cursor.execute('INSERT INTO Products(title, description, price) VALUES (?, ?, ?)',
#                    (f'Название: Product {i}', f'Описание: описание {i}', f'Цена: {i * 100}'))


# cursor.execute('DELETE FROM Products')    # Очистка базы данных (database.bd)


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    products_list = []
    for product in products:
        product_dict = {
            'title': product[1],
            'description': product[2],
            'price': product[3]
        }
        products_list.append(product_dict)
    return products_list


prod_list = get_all_products()

connection.commit()
connection.close()




