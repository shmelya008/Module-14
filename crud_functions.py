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

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')


# for i in range(1, 5):
#     cursor.execute('INSERT INTO Products(title, description, price) VALUES (?, ?, ?)',
#                    (f'Название: Product {i}', f'Описание: описание {i}', f'Цена: {i * 100}'))


def is_included(username):
    exist_user = cursor.execute('SELECT * FROM Users WHERE username=?', (username,)).fetchone()
    if exist_user is None:
        return True
    connection.commit()


def add_user(username, email, age):
    cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'{username}', f'{email}', f'{age}', f'1000'))
    connection.commit()


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


connection.commit()
prod_list = get_all_products()

# cursor.execute('DELETE FROM Users')
# initiate_db()

# connection.close()
