import random
import mysql.connector
import sys

class Cursor:
	def __init__(self):
		pass

	def execute(self, operation, params=None, multi=False):
		print(f"	Fake execution complete.... query -> {operation}")
		return True

class Connection:
	def __init__(self, host, user, password):
		pass

class Database:

	def __init__(self, host, user, password, state="Testing"):

		self.host = host
		self.user = user
		self.password = password

		self.state = state

		if state == "Testing":
			self.connection = Connection(self.host, self.user, self.password)
			self.cursor = Cursor()

		elif state == "Production":
			self.connection = mysql.connector.connect(self.host, self.user, self.password)
			self.cursor = self.connection.cursor()

		else:
			print(f"Error: unexpected connection state, not Testing or Production")
			sys.exit()

	def execute_query(self, query):
		return self.cursor.execute(query)

	def get_map_element_by_id(self, element_id: str) -> dict:

		mapElementDict = {
			"type": None,
			"image_path": None,
			"xPos": None,
			"yPos": None,
			"element_id": None
			}

		query = f"SELECT * FROM database.map WHERE ELEMENT_ID=\'{element_id}\'"

		if self.state == "Testing":

			mapElementDict["type"] = "test_type"
			mapElementDict["image_path"] = "image.jpeg"
			mapElementDict["xPos"] = "0"
			mapElementDict["yPos"] = "0"
			mapElementDict["element_id"] = str(element_id)

			self.execute_query(query)

			mapElementDict["query"] = query

		else:
			print(f"Error, calling features unimplemented for the current database state attribute....")

		return mapElementDict

	def get_appointment_by_id(self, appointment_id: str) -> dict:
		"""
		This method is called when a user searched for a specific appointment. given the appointment id the method provides
		a dictionary of the below format with the expected data fields filled in
		"""

		appointmentDict = {
			"event_name": None,
			"created_at": None,
			"event_date": None,
			"related_student": None,
			"related_staffer": None,
			"supplementary_doc_path": None,
			"event_description": None,
			"appointment_id": None
			}

		query = f"SELECT * FROM database.appointments WHERE APPOINTMENT_ID=\'{appointment_id}\'"

		if self.state == "Testing":

			appointmentDict["event_name"] = "test_appointment_name"
			appointmentDict["created_at"] = "DD-MM-YY-HH-MM"
			appointmentDict["event_date"] = "DD-MM-YY-HH-MM"
			appointmentDict["related_student"] = "test_student"
			appointmentDict["related_staffer"] = "test_staffer"
			appointmentDict["supplementary_doc_path"] = "spreadsheat.csv"
			appointmentDict["event_description"] = "test_appointment_description"
			appointmentDict["appointment_id"] = str(appointment_id)

			self.execute_query(query)

			appointmentDict["query"] = query

		else:
			print(f"Error, calling feature unimplemented for the current database state attribute....")

		return appointmentDict

	def get_job_by_id(self, job_posting_id: str) -> dict:

		jobDict = {
			"job_title": None,
			"company": None,
			"posting_type": None,
			"posting_description": None,
			"application_portal_link": None,
			"job_posting_id": None
			}

		query = f"SELECT * FROM database.jobs WHERE JOB_ID=\'{job_posting_id}\'"

		if self.state == "Testing":

			jobDict["job_title"] = "test_job_title"
			jobDict["company"] = "test_company_name"
			jobDict["posting_type"] = "test_job_type"
			jobDict["posting_description"] = "test_job_description"
			jobDict["application_portal_link"] = "www.indeed.com/jobPosting/fakeID"
			jobDict["job_posting_id"] = str(job_posting_id)

			self.execute_query(query)

			jobDict["query"] = query

		else:
			print(f"Error, calling feature unimplemented for the current database state attribute....")

		return jobDict

	def get_appointments_by_staff(self, staff_name: str) -> list: # returns a list of dictionaries

		appointments = []

		query = f"SELECT * FROM database.appointments WHERE RELATED_STAFFER=\'{staff_name}\'"

		if self.state == "Testing":
	
			for appointment in range(random.randint(5)):

				appointmentDict = self.get_appointment_by_id(appointment)
				appointmentDict["query"] = query
				appointments.append(appointmentDict)

			self.execute_query(query)			

		else:
			print(f"Error, calling features unimplemented for the current database state attribute.....")

		return appointments

	def get_appointments_by_student(self, student_name: str) -> list: # returns a list of dictionaries
		"""
		This method is called when filling a list GUI element, using this element a python list filled with dictionaries
		is returned in the below format. given a student name many appointments (or none) may be returned

		Consider methods of the type where a list is returned as a reoccuring call to its get_by_id counterpart
		the only difference being that a list of such dict objects are returned, with the exact same shape.
		"""
		
		appointments = []

		query = f"SELECT * FROM database.appointments WHERE RELATED_STUDENT=\'{student_name}\'"

		if self.state == "Testing":

			for appointment in range(random.randint(5)):

				appointment = self.get_appointment_by_id(appointment)
				appointment["query"] = query
				appointments.append(appointment)

			self.execute_query(query)

		else:
			print(f"Error, calling features unimplemented for the current database state attribute.....")

		return appointments

	def get_jobs_by_company(self, company_name: str) -> list: # returns a list of dictionaries

		jobs = []	

		query = f"SELECT * FROM database.jobs WHERE COMPANY=\'{company_name}\'"

		if self.state == "Testing":
			
			for job in range(random.randint(5)):

				jobDict = self.get_job_by_id(job)
				jobDict["query"] = query
				jobs.append(jobDict)

			self.execute_query(query)

		else:
			print(f"Error, calling feature unimplemented for the current database state attribute.....")

		return jobs

	def get_jobs_by_type(self, job_posting_type: str) -> list: # returns a list of dictionaries
		
		jobs = []

		query = f"SELECT * FROM database.jobs WHERE POSTING_TYPE=\'{job_posting_type}\'"

		if self.state == "Testing":

			for job in range(random.randint(5)):

				jobDict = self.get_job_by_id(job)
				jobDict["query"] = query
				jobs.append(jobDict)

			self.execute_query(query)

		else:
			print(f"Error, calling feature unimplemnted for the current database state attribute......")

		return jobs
