import sqlite3


connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

# for i in range(1, 11):
#     cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
#                    (f'User{i}', f'example{i}@gmail.com', f'{i*10}', f'{1000}'))

# for i in range(1, 11):
#     if i % 2 != 0:
#         cursor.execute('UPDATE Users SET balance = ? WHERE username = ?', (500, f'User{i}'))

# x = [x for x in range(1, 11)]
# del_id = x[::3]
# for i in del_id:
#     cursor.execute('DELETE FROM Users WHERE id = ?', (f'{i}', ))

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60, ))
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

# Очистка базы данных (not_telegram.bd)
# for i in range(0, 11):
#     cursor.execute('DELETE FROM Users WHERE id = ?', (f'{i}', ))

connection.commit()
connection.close()
