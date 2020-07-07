from datetime import datetime, timedelta
from faker import Faker
import re


class UserData(object):

    def __init__(self, first_name="Stepan", last_name="Zagrushiv", martial_status=1,
                 nationality="185", birth_date="1996-04-17"):
        self.first_name = first_name
        self.last_name = last_name
        self.martial_status = martial_status
        self.nationality = nationality
        self.birth_date = birth_date


class LocationData(object):
    fake = Faker()

    def __init__(self, name=fake.name(), country_code=fake.country_code(), state=fake.state(),
                 city=fake.city(), address=fake.street_address(), zipcode=fake.postcode(),
                 phone=re.sub('[^0-9]', '', fake.phone_number()), fax=fake.msisdn(), notes=fake.catch_phrase()):
        self.name = name
        self.country_code = country_code
        self.state = state
        self.city = city
        self.address = address
        self.zipcode = zipcode
        self.phone = phone
        self.fax = fax
        self.notes = notes


class PunchData(object):
    fake = Faker()

    def __init__(self):
        self.punch_in_msg = self.fake.catch_phrase()
        self.punch_out_msg = self.fake.catch_phrase()
        self.today_date = datetime.today().strftime("%Y-%m-%d")
        self.future_date = (datetime.today() + timedelta(weeks=1)).strftime("%Y-%m-%d")

