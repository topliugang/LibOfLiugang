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


def select(count):
	con = sqlite3.connect('fuck.db')
	cur = con.cursor()
	cur.execute('select ip, port from proxy limit ?', (count,))
	ip_port_list = []
	for row in cur:
		ip_port_list.append((row[0], row[1]))
		#print row[0], row[1]
	con.close()
	return ip_port_list

def select():
	con = sqlite3.connect('fuck.db')
	cur = con.cursor()
	cur.execute('select ip, port from proxy ')
	ip_port_list = []
	for row in cur:
		ip_port_list.append((row[0], row[1]))
		#print row[0], row[1]
	con.close()
	return ip_port_list


def delete_all():
	con = sqlite3.connect('fuck.db')
	sql = 'delete from proxy;'
	con.execute(sql)
	con.commit()
	con.close()
	   

if __name__ == '__main__':
	#create_table()
	pass
