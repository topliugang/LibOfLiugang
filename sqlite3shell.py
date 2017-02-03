import sqlite3

con = sqlite3.connect('fuck.db')
con.isolation_level = None
cur = con.cursor()

buffer = ''

print 'enter sql commands.'
print 'enter blank line to exit.'

while True:
	line = raw_input()
	if line == '':
		break
	buffer += line
	if sqlite3.complete_statement(buffer):
		try:
			buffer = buffer.strip()
			cur.execute(buffer)
			if buffer.lstrip().upper().startswith('SELECT'):
				print cur.fetchall()
		except sqlite3.Error as e:
			print 'error', e.args[0]
		buffer = ''

con.close()