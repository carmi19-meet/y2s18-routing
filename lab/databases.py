from model import Base, Student

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_student(name, year, finished_lab):
	"""
	Add a student to the database, given
	their name, year, and whether they have
	finished the lab.
	"""
	student_object = Student(
		name=name,
		year=year,
		finished_lab=finished_lab)
	session.add(student_object)
	session.commit()

def query_by_name(name):
	"""
	Find the first student in the database,
	by their name
	"""
	student = session.query(Student).filter_by(
		name=name).first()
	return student

def query_all():
	"""
	Print all the students in the database.
	"""
	students = session.query(Student).all()
	for student in students:
		print(student)
		print('\n')
	return students

def delete_student(name):
	"""
	Delete all students with a certain name
	from the database.
	"""
	session.query(Student).filter_by(
		name=name).delete()
	session.commit()
def delete_all():
	"""
	Delete all students with a certain name
	from the database.
	"""
	session.query(Student).delete()
	session.commit()

def update_lab_status(name, finished_lab):
	"""
	Update a student in the database, with 
	whether or not they have finished the lab
	"""
	student_object = session.query(Student).filter_by(
		name=name).first()
	student_object.finished_lab = finished_lab
	session.commit()

def query_by_id(student_id):
    student = session.query(Student).filter_by(
        student_id=student_id).first()
    return student
#delete_student("moses")
#add_student("jack", "Y2", True)
#add_student("jesas", "Y2", False)
#add_student("bob", "Y3", True)
#add_student("abba", "Y1", False)
#add_student("bassel", "Y1", True)
#delete_all()