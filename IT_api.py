import requests
from django.db import models

#to get the academic info from IT endpoints
def fetch_data():
    url = 'https://studentapi.bsite.net/api/Student/GetAcademicInfo'
    headers = {
        'Authorization': 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJHdWlkIjoiOTRBNTUyQ0YtQUY4RC00MDJBLUFCOUQtRjM3RDExMjIwRTk3IiwibmJmIjoxNjg2MjkxMzI0LCJleHAiOjE2ODYzMjM3MjQsImlhdCI6MTY4NjI5MTMyNCwiaXNzIjoiaGZkdWV3aHJwN3luNTQ0M3U5cGlyZnR0NXl1aGdmY3hkZmVyNTY0dzhteW4zOXdvcDkzbXo0dTJuN256MzI0NnRiajZ0ejU2MzJjcjUiLCJhdWQiOiIydnQzN2JubXpodm5mc2pid3RubXl1am1hd2VzcnRmZ3lodWppa21uY3hkZXM0NTZ5N3VpamhidmNkeHNlNDU2NzhpOW9rbG1uYiJ9.nh4VVhFbHQcKrXVKXmAS2AqVzPcvy6N6E2Ec6yDGSXCRMIw8Oo-rCALJT0qUSl2B70S-MwJ1JkzNupg66kltew'
    }

    response = requests.get(url)
    data = response.json()
    return data

def save_data(item):
         User=User.object.create(first_name=item['name'], email=item['email'], national_id =item['ssn'],address = item['address'], gender = item['gender'])
         Department =Department.object.create(name=item['programName'])
         Teacher=Teacher.object.create(level=item['level'],department=Department)
        
        