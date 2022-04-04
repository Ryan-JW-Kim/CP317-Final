
from types import NoneType
import mysql.connector
import sys

class Cursor:
	def __init__(self):
		pass

	def execute(self, operation, params=None, multi=False):
		return True

class Connection:
	def __init__(self, host, user, password):
		pass

class Database:

	def __init__(self, host, user, password, state="Testing"):

		h = host
		u = user
		p = password

		if state == "Testing":
			self.connection = Connection(h, u, p)
			self.cursor = Cursor()

		elif state == "Production":
			self.connection = mysql.connector.connect(h, u, p)
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
		
		return mapElementDict

	def get_appointments_by_staff(self, staff_name: str) -> list: # returns a list of dictionaries
		pass

	def get_appointments_by_student(self, student_name: str) -> list: # returns a list of dictionaries
		"""
		This method is called when filling a list GUI element, using this element a python list filled with dictionaries
		is returned in the below format. given a student name many appointments (or none) may be returned

		Consider methods of the type where a list is returned as a reoccuring call to its get_by_id counterpart
		the only difference being that a list of such dict objects are returned, with the exact same shape.
		"""
		pass

	def get_appointment_by_id(self, appointment_id: str) -> dict:
		"""
		This method is called when a user searched for a specific appointment. given the appointment id the method provides
		a dictionary of the below format with the expected data fields filled in
		"""

		appointmentDict = {
			"event_name": None,
			"created_at": None,
			"event_date": None,
			"supplementary_doc_path": None,
			"event_description": None	
			}

		return appointmentDict

	def get_job_by_id(self, job_posting_id: str) -> dict:

		jobDict = {
			"job_title": None,
			"company": None,
			"posting_type": None,
			"posting_description": None,
			"application_portal_link": None
			}

		return jobDict

	def get_jobs_by_company(self, company_name: str) -> list: # returns a list of dictionaries
		pass

	def get_jobs_by_type(self, job_posting_type: str) -> list: # returns a list of dictionaries
		pass
