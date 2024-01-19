from db.getConnection import getConnection
from entity.Person import Person
from fastapi import APIRouter, HTTPException

router = APIRouter(
	tags = ['Person'],
	prefix = '/api/person'
)

@router.get('/')
async def getPeople():
	people = []
	con = getConnection()
	cur = con.cursor()
	cur.execute('''
	SELECT id, firstname, lastname, age
	FROM People;
	'''.strip())
	rs = cur.fetchall()
	cur.close()
	con.close()
	for p in rs:
		people.append(
	  		Person(
				id = int(p[0]),
				firstname = p[1],
				lastname = p[2],
				age = int(p[3])
			)
		)
	return people

@router.get('/{id}')
async def getPerson(id: int):
	con = getConnection()
	cur = con.cursor()
	cur.execute(f'''
	SELECT id, firstname, lastname, age
	FROM People
	WHERE id = {id};
	'''.strip())
	rs = cur.fetchall()
	cur.close()
	con.close()
	if len(rs) > 0:
		return Person(
			id = int(rs[0][0]),
			firstname = rs[0][1],
			lastname = rs[0][2],
			age = int(rs[0][3])
		)
	return None

@router.delete('/{id}')
async def removePerson(id:int):
	con = getConnection()
	if con:
		try:
			cur = con.cursor()
			cur.execute('DELETE FROM People WHERE id={};'.format(id))
			con.commit()
			if cur.rowcount > 0:
				raise HTTPException(status_code=200, detail="cancellata correttamente")
			else:
				raise HTTPException(status_code=404, detail="Non riesco a cancellare la persona")
		finally:
			cur.close()
			con.close()
	else:
		raise HTTPException(status_code=404, detail="Non riesco a connettermi figuriamoci a cancellare la persona")

@router.post('/')
async def addPerson(p:Person):
	con = getConnection()
	if con:
		try:
			cur = con.cursor()
			cur.execute(
				'INSERT INTO People (firstname, lastname, age) VALUES ("{}", "{}", {});'.format(
					p.firstname,
					p.lastname,
					p.age
				)
			)
			con.commit()
			if cur.rowcount > 0:
				raise HTTPException(status_code=200, detail="persona inserita correttamente")
			else:
				raise HTTPException(status_code=404, detail="NON Riesco ad inserirla")
		finally:
			cur.close()
			con.close()
	else:
		raise HTTPException(status_code=404, detail="NON Riesco ad connettermi, COLPA DELLA CAFIERO")

@router.put('/{id}')
async def modifyPerson(id:int, p:Person):
	con = getConnection()
	if con:
		try:
			cur = con.cursor()
			cur.execute(
				'UPDATE People SET firstname="{}", lastname="{}", age={} WHERE id={};'.format(
					p.firstname,
					p.lastname,
					p.age,
					id
				)
			)
			con.commit()
			if cur.rowcount > 0:
				raise HTTPException(status_code=200, detail="persona modificata correttamente")
			else:
				raise HTTPException(status_code=404, detail="NON Riesco a modificarla")
		finally:
			cur.close()
			con.close()
	else:
		raise HTTPException(status_code=404, detail="NON RIESCO A CONNETTERMI NE MODIFICARE, IL FANTASMA DELLA CAFIERO E' TRA DI NOI!!!!")