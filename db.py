import datetime 
import sqlite3

#Function to write the user to the database

a_time = datetime.datetime.now()

conn = sqlite3.connect('database.db', check_same_thread=False)
cursor = conn.cursor()



def db_table_val(us: int, name: str, fam: str, nik: str):#<--Function to check the user in the database. If it doesn't exist, she writes it down.
	cursor.execute(f"SELECT user_id FROM user WHERE user_id = {us}")
	result = cursor.fetchone()
	if result == None:
		cursor.execute("INSERT INTO user (user_id, name_user, famyly_user, nikname_user, time_in) VALUES (?, ?, ?, ?, ?)", (us, name, fam, nik, a_time))
		conn.commit()


def db_comment_save(user_id: int, text: str):#<--The function of writing a comment to the database.
	cursor.execute("INSERT INTO user_comment (user_id, text_comment, time_comment) VALUES (?, ?, ?)", (user_id, text, a_time))
	conn.commit()