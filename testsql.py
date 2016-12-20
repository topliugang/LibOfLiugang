import sqlite3



def select(conn):
	sql = 'select * from proxy;'
	cursor = conn.execute(sql)

	count = 0
	for row in cursor:
	   print row[0]+':'+row[1]
	   count = count+1

	print count
	

def delete_all(conn):
	sql = 'delete from proxy;'
	conn.execute(sql)
	conn.commit()
	   

if __name__ == '__main__':
	#ip_port_dict = fuck_xicidaili()

	

	conn = sqlite3.connect('fuck.db')

	c = conn.cursor()

	for sb in c.execute('select * from proxy'):
		print sb

	conn.close()