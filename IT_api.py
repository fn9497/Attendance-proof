import requests
from django.db import models


def fetch_data():
    url = 'https://studentapi.bsite.net/api/Student/GetAcademicInfo'

    response = requests.get(url)
    data = response.json()
    return data

def save_data(item):
         User=User.object.create(first_name=item['name'], email=item['email'], national_id =item['ssn'],address = item['address'], gender = item['gender'])
         Student= Student.object.create(level=item['level'],department=item['programName'])
        