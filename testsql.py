import sqlite3

def create_table():
	sql = '''
		drop table proxy;
		create table proxy(
			ip text, 
			port text, 
			unique(ip, port));
		'''

	con = sqlite3.connect('fuck.db')
	cur = con.cursor()
	cur.executescript(sql)

	con.commit()
	con.close()

def insert(ip_port_list):
	con = sqlite3.connect('fuck.db')
	cur = con.cursor()
	cur.executemany('insert or ignore into proxy(ip, port) values(?, ?)', ip_port_list)
	con.commit()
	con.close()

	

def delete_all(conn):
	sql = 'delete from proxy;'
	conn.execute(sql)
	conn.commit()
	   

if __name__ == '__main__':
	create_table()

