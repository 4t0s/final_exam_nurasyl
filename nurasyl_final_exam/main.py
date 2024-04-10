import sqlite3

connection = sqlite3.connect('cinema_store.db')

cursor = connection.cursor()

class DBManager:
    def __init__(self):
        self.name = 'some'
        self.phone = '567890'
        self.place_id = 123456789
    def create_table():
        cursor.execute('CREATE TABLE IF NOT EXISTS cinema (id INTEGER PRIMARY KEY, name TEXT, address TEXT)')
        cursor.execute('CREATE TABLE IF NOT EXISTS afisha (id INTEGER PRIMARY KEY, name TEXT, genre TEXT, year INTEGER, description TEXT, rating REAL)')
        cursor.execute('CREATE TABLE IF NOT EXISTS admin_afisha (id INTEGER PRIMARY KEY, movie_id INTEGER, cinema_id INTEGER, price INTEGER, date DATE, time TIME, capacity INTEGER)')
        cursor.execute('CREATE TABLE IF NOT EXISTS place (id INTEGER PRIMARY KEY,  afisha_id INTEGER, room INTEGER, row INTEGER, seat INTEGER)')
        cursor.execute('CREATE TABLE IF NOT EXISTS ticket (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, place_id INTEGER)')      



class Order:
    def __init__(self):
        self.name = ''
        self.genre = ''
        self.film_index = 0
        self.cinema_index = 0
        self.room = 0
        self.row = 0
        self.seat = 0
        self.phone = ''
    def add_order(self):
        print('Hello you are entering the kino.kz')
        choice = int(input('To make order you just need to write 1 and if you want to exit you need to write 2: '))
        
        if(choice == 1):
            
                choice_in_order = int(input('You can select films by 1.genre or 2.name : '))
                
                if(choice_in_order == 1):
                    self.genre = int(input('You can select genres :\n1.Action\n2.Comedy\n3.Drama\n4.Horror\n5.Fantasy\n'))
                    cursor.execute(f'select * from afisha where genre = "{self.genre}";')
                    films_of_genre = cursor.fetchall()
                    print(films_of_genre)
                    
                    for film in films_of_genre:
                        print(f"{films_of_genre.index(film)+1}.Name of the film - {film[1]}\n")
                    self.film_index = int(input("Enter number to choose a film:\n"))
                    
                elif(choice_in_order == 2):
                    
                    cursor.execute(f'SELECT name FROM afisha')
                    films = cursor.fetchall()
                    
                    for film in films:
                        print(f"{films.index(film)}.{film[0]}")
                    self.film_index = int(input("Enter id of the film you would like to go to: "))
                else:
                    raise  UnicodeTranslateError("Invalid input! Please enter 1 or 2.")
                
                while True:
                        self.cinema_index = int(input('In what cinema would you like to order? \n1.Eurasia\n2.Chaplin\n3.Arman\n4.Kinopark\n5.Arsenal\n'))
                        if self.cinema_index > 1 or self.cinema_index < 5:
                            break
                        
                cursor.execute(f"select name from cinema where `id` = {self.cinema_index}")
                
                while True:
                    self.room = int(input('What room would you like to be in from 1 to 6: '))
                    self.row =  int(input('What row would you like to sit on from 1 to 16: '))
                    self.seat = int(input("Enter your seat number from 1 to 16: "))
                    if self.room  > 6 or self.row > 16 or self.seat > 16 :
                        print('Invalid input! Please enter numbers from 1-6 and 1-16 only.')
                    elif self.room < 1 or self.row < 1 or self.seat < 1:
                        print('Invalid input! Please enter numbers from 1-6 and 1-16 only.')
                    else:
                        break
                    
                while True:
                    self.phone = input('Please enter your phone number: ')
                    if len(self.phone) != 10 or not self.phone[0].isdigit():
                        print('Phone should contain exactly 10 digits.')
                    else:
                        break
                    
                cursor.execute(f'insert into place (afisha_id, room, row, seat) values({self.film_index},{self.room},{self.row},{self.seat})')
                connection.commit()
                
                cursor.execute(f'SELECT LAST_INSERT_ID() IN place WHERE afisha_id={self.film_index}')
                place_id = cursor.fetchone()
                
                self.name = input('On what name your order will be received to: ')
                
                choice_in_order == int(input('You ready to buy your ticket? \n1.YES\n2.NO\n'))
                
                if choice_in_order == 1:
                    cursor.execute(f'insert into ticket (name, phone, place_id) values(`{self.name}`,`{self.phone}`,{place_id})')
                    connection.commit()
                    
                elif choice_in_order == 2:
                    print('You will start  ordering again when you want.')
                    raise UnicodeTranslateError
                    
        elif(choice == 2):
            raise UnicodeTranslateError
        else:
            print('I think you did not understand me, so I stop the program for now')
            raise UnicodeTranslateError
    def delete_order(self):
        cursor.execute(f'delete from ticket where name = `{self.name}`')
        connection.commit()
while True:
    try:
        new_order = Order()
        new_order.add_order()
    except ValueError:
        print('\n\nThe input you have  entered was incorrect.\nTry again please.\n\n')
        continue
    except ArithmeticError:
        print("\n\nOk we'll see you again.\n\n")
        break
    # except:
    #     print('\n\n\nProgram  has encountered an error. Sorry about that.\n\n\n')