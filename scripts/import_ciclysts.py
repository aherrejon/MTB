from apps.core.models import *
from datetime import datetime
import csv

filename = '/home/aherrejon/Desktop/MTB/pedalitos_full.csv'

date_obj = datetime.today()
with open(filename) as csv_infile:
  csv_reader = csv.reader(csv_infile, delimiter=',')
  for row in csv_reader:    
    name = row[1]
    lastname = row[2]
    city = row[3]
    team = row[4]
    sex = row[5]
    number = row[0]
    size = row[6]
    distance = row[7]
    package = row[8]
    paid_date = row[9]
    account = row[10]
    comments = row[11]
    logo = row[12]
    category = 'P'
    try:
      if float(distance) < 50:
        category = 'P'
      if float(distance) < 65:
        category = 'I'
      else:
        category = 'A'
    except:
      pass
    
    if size and size[0] in ('n', 'N'):
      size = 'N'

    name = name.strip()
    if name == '' or name is None:
      name = "Inexistente %s" % number

    cyclist, created = Cyclist.objects.get_or_create(firstname=name, lastname=lastname, city=city, club=team)
    cyclist.email = "%s@6tomiradores.com" % number
    cyclist.category = category
    cyclist.sex = sex
    cyclist.save()
    
    suscription, created = Suscription.objects.get_or_create(event_id=10, number=number)
    suscription.cyclist = cyclist
    suscription.size = size
    suscription.distance = distance
    suscription.package = package
    suscription.account = account
    suscription.comments = comments
    suscription.logo = 1 if logo == 'TRUE' else 0
    suscription.medal = 1
    suscription.jersey = 1 if package == '1' else 0
    suscription.status = 'A'

    new_paid_date = paid_date[:7].strip()    
    if len(new_paid_date) > 5 and '/' in new_paid_date:
      date_split = new_paid_date.split('/')
      date_split = filter(None, date_split)
      date_obj = datetime(int(date_split[2]), int(date_split[1]), int(date_split[0]))
    if new_paid_date != '""':
      date_obj = None

    suscription.paid_date = date_obj
    suscription.save()

    print "%s %s %s %s %s %s %s %s %s %s" % (number, name, lastname, team, city, size, distance, paid_date, package, comments)
