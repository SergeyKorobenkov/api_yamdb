import os
import django
from django.conf import settings
import csv
os.environ['DJANGO_SETTINGS_MODULE'] = 'api_yamdb.settings'
django.setup()

from api.models import *
from datetime import datetime
from django.contrib.auth import get_user_model
User = get_user_model()

def read_csv():
    with open(os.path.join(settings.BASE_DIR, 'data/titles.csv'), newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for n, row in enumerate(data):
            if n != 0:
                name = row[1]
                year = int(row[2])
                new_obj = Title.objects.create(name=name, year=year)



def rewiews():
    with open(os.path.join(settings.BASE_DIR, 'data/review.csv'), newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for n, row in enumerate(data):
            if n != 0:
                id = row[0]
                title = row[1]
                title =Title.objects.get(id=title)
                text = row[2]
                user = int(row[3])
                user = User.objects.get(id=user)
                score = int(row[4])
                voted_on = row[5].split('T')[0]
                voted_on = datetime.strptime(voted_on, '%Y-%m-%d')
                #2019-09-24T21:08:21.567Z
                new_obj = Rewiew.objects.create(id=id,title=title, text=text, user=user,score=score,voted_on=voted_on)


def users():
    with open(os.path.join(settings.BASE_DIR, 'data/users.csv'), newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for n, row in enumerate(data):
            if n != 0:
                #id,username,email,role,description,first_name,last_name
                id = row[0]
                username = row[1]
                email = row[2]
                
                new_obj = User.objects.create(id=id,username=username, email=email, password='test')
rewiews()

