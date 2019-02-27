from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo = False)
Base = declarative_base()

affiliation = Table(
    'Affiliation', Base.metadata,
    Column('asso_id', Integer, ForeignKey('Association.asso_id'), nullable=False),
    Column('student_id', Integer, ForeignKey('Student.number'), nullable=False)
)

class Student(Base):
    __tablename__ = 'Student'
    number = Column(Integer, primary_key=True)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    nickName = Column(String)
    country = Column(String)
    associations = relationship('Association', secondary = affiliation, back_populates = 'students')

class Association(Base):
    __tablename__ = 'Association'
    asso_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    students = relationship('Student', secondary = affiliation, back_populates = 'associations')


Base.metadata.create_all(engine)
print("Tables created!")

Session = sessionmaker(bind = engine)
session = Session()

nox = Student(number = 1, firstName = "Thomas", lastName = "Adier", nickName = "nox", country = "France")
session.add(nox)
print("Student nox added.")

rezo = Association(asso_id = 1, name = "ViaRezo", description = "Bringing Internet to the campus")
session.add(rezo)
print("Association ViaRezo added.")

enizor = Student(number=2, firstName='Remi', lastName='Garde',
                 nickName='enizor', country='France')
gossex = Student(number=3, firstName='David', lastName='Gosset',
                 nickName='gossex', country='France')
xix = Student(number=4, firstName='Julen', lastName='Dixneuf',
              nickName='xix', country='France')
session.add_all([enizor, gossex, xix])
print("enizor, gossex, xix added!")

rezo.students.append(nox)
rezo.students.append(enizor)
rezo.students.append(gossex)
rezo.students.append(xix)

session.commit()

# [asso.name for asso in enizor.associations]
# [stud.firstName + " " + stud.lastName for stud in session.query(Student)]
# [stud.nickName for stud in session.query(Student).filter(Student.lastName == 'Adier')]
# [stud.nickName for stud in session.query(Student).filter(Student.lastName == 'Adier').filter(Student.firstName.startswith('Tho'))]
# session.query(Association).one().name
# session.query(Student).get(1).lastName



#################   PARTIE 2   ################


class Association(Base):
    __tablename__ = 'Association'
    asso_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    students = relationship('Affiliation', back_populates = 'asso', cascade = "all, delete, delete-orphan")

class Address(Base):
    __tablename__ = 'Address'
    email = Column(String, primary_key=True)
    student_id = Column(Integer, ForeignKey('Student.number'))
    student = relationship('Student', back_populates = 'addresses')

class Affiliation(Base):
    __tablename__ = 'Affiliation'
    asso_id = Column(Integer, ForeignKey('Association.asso_id'), primary_key=True)
    student_id = Column(Integer, ForeignKey('Student.number'), primary_key=True)
    role = Column(String, nullable=False)
    asso = relationship('Association', back_populates='students')
    student = relationship('Student', back_populates='associations')

Base.metadata.create_all(engine)
print("Tables created!")

##########
# Session = sessionmaker(bind = engine)
# session = Session()
#
# nox = Student(number = 1, firstName = "Thomas", lastName = "Adier", nickName = "nox", country = "France")
# session.add(nox)
# print("Student nox added.")
#
# rezo = Association(asso_id = 1, name = "ViaRezo", description = "Bringing Internet to the campus")
# session.add(rezo)
# print("Association ViaRezo added.")
#
# enizor = Student(number=2, firstName='Remi', lastName='Garde',
#                  nickName='enizor', country='France')
# gossex = Student(number=3, firstName='David', lastName='Gosset',
#                  nickName='gossex', country='France')
# xix = Student(number=4, firstName='Julien', lastName='Dixneuf',
#               nickName='xix', country='France')
# session.add_all([enizor, gossex, xix])
# print("enizor, gossex, xix added!")
#
# session.add(Affiliation(asso_id = rezo.asso_id, student_id = enizor.number, role="President"))
# session.add(Address(student_id = xix.number, email = 'Julien.Dixneuf@provider.com'))
# session.commit()
#
# # [af.student.nickName for af in rezo.students]
# # [asso.name for asso in [affi.asso for affi in enizor.associations]]
# # [addr.email for addr in xix.addresses]
##########

def populates() :
    Session = sessionmaker(bind=engine)
    session = Session()

    # Load student data
    with open('../data/students.csv') as studfile :
        reader = csv.reader(studfile, delimiter=';')
        next(reader)  # skip headers
        students = {} # dictionary for storing student_id/student pairs
        for line in reader :
            newstud = Student(number=int(line[0]),
                              firstName=line[1],
                              lastName=line[2],
                              nickName=line[3],
                              country=line[4])
            students[newstud.number] = newstud
            session.add(newstud)
    # Load association data
    with open('../data/associations.csv') as assofile :
        reader = csv.reader(assofile, delimiter=';')
        next(reader)      # skip headers
        associations = {} # dictionary for storing asso_id/association pairs
        for line in reader :
            newasso = Association(asso_id=int(line[0]),
                                  name=line[1],
                                  description=line[2])
            associations[newasso.asso_id] = newasso
            session.add(newasso)
    # Load affiliation data
    with open('../data/affiliation.csv') as affifile :
        reader = csv.reader(affifile, delimiter=';')
        next(reader)  # skip headers
        for line in reader :
            session.add(Affiliation(asso_id=int(line[0]),
                                    student_id=int(line[1]),
                                    role=line[2]))
    # Load address data
    with open('../data/adresses.csv') as emailfile :
        reader = csv.reader(emailfile, delimiter=';')
        next(reader)  # skip headers
        for line in reader :
            session.add(Address(student_id=int(line[0]),
                                email=line[1]))
    # Commit data
    session.commit()

# Session = sessionmaker(bind=engine)
# session = Session()

## Students from Brazil
# session.query(Student).filter(Student.country=='Brazil').count()
# [stud.firstName + " " + stud.lastName for stud in session.query(Student).filter(Student.country=='Brazil')]

## Students in association ViaRezo
## X.any(P) tels if any item in collection X has property P
## X.has(P) tels if item X has property P
# session.query(Student).filter(Student.associations.any(Affiliation.asso.has(Association.name=='ViaRezo'))).count()
# [stud.firstName + " " + stud.lastName for stud in session.query(Student).filter(Student.associations.any(Affiliation.asso.has(Association.name=='ViaRezo')))]

## Students in ViaRezo by country
# [s for s in session.query(func.count(Student.number), Student.country).filter(Student.associations.any(Affiliation.asso.has(Association.name=='ViaRezo'))).group_by(Student.country)]

## Presidents of associations
# [s.firstName + " " + s.lastName for s in session.query(Student).filter(Student.associations.any(Affiliation.role == 'president'))]

## Delete association BDI
# bdi = session.query(Association).filter(Association.name=='BDI').one()
# session.delete(bdi)
# session.commit()

## Add an email to Julie Rose (sudent number 8)
# julie = session.query(Student).filter(Student.number == 8).one()
# julie.addresses.append(Address(email="julier@gmail.com"))
# session.commit()



####################     PARTIE 3    ##############

# 7878656358ddfb28fb9b904b2242fd2a
import requests
import json

WeatherAPIKey = "7878656358ddfb28fb9b904b2242fd2a"

req = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Paris,France&APPID=" + WeatherAPIKey)
rawData = req.content.decode('utf-8')

data = json.loads(rawData)

# Ex 14
print(data["weather"][0]["description"])

# Ex 15
print(data["main"]["temp"]-273.15)

# Ex 16
req = requests.get("http://api.openweathermap.org/data/2.5/find?lat=48.86&lon=2.35&cnt=50&units=metric&APPID=" + WeatherAPIKey)
rawData = req.content.decode('utf-8')

places = json.loads(rawData)
print([(p['name'], p['main']['temp']) for p in places['list']])

request = requests.get("http://api.openweathermap.org/data/2.5/forecast?q=Paris,France&units=metric&APPID=" + WeatherAPIKey)
rawData = request.content.decode('utf-8')
forecast = json.loads(rawData)['list']
print(forecast)

import time
print(["day={}, weather={}, temp={}°C".format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(f['dt'])),
                                              f['weather'][0]['description'],
                                              f['main']['temp'])
       for f in forecast
      ])


def avg_temperature(lon_left, lat_bot, lon_right, lat_top, nb_loc) :
    req = requests.get(
        'http://api.openweathermap.org/data/2.5/box/city?bbox={},{},{},{},{}&unit=metric&APPID={}'.format(
            lon_left, lat_bot, lon_right, lat_top, nb_loc, WeatherAPIKey
        )
    )
    rawData = req.content.decode('utf-8')
    data = json.loads(rawData)
    locations = data['list']
    nbLoc = data['cnt']
    average_temp = 0
    for loc in locations :
        average_temp += loc['main']['temp']
    return average_temp / nbLoc

print(avg_temperature(-4.9,42.34,8.43,51.09, 9))

def get_country(loc_id) :
    req = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?id={}&unit=metric&APPID={}'.format(
            loc_id, WeatherAPIKey
        )
    )
    rawData = req.content.decode('utf-8')
    data = json.loads(rawData)
    return data['sys']['country']

import time
def avg_temperature2(lon_left, lat_bot, lon_right, lat_top, nb_loc, country) :
    req = requests.get(
        'http://api.openweathermap.org/data/2.5/box/city?bbox={},{},{},{},{}&unit=metric&APPID={}'.format(
            lon_left, lat_bot, lon_right, lat_top, nb_loc, WeatherAPIKey
        )
    )
    rawData = req.content.decode('utf-8')
    data = json.loads(rawData)
    locations = data['list']
    nbLoc = 0
    average_temp = 0
    for loc in locations :
        print("Checking " + loc['name'] + "...")
        if country == get_country(loc['id']) :
            average_temp += loc['main']['temp']
            nbLoc += 1
        time.sleep(1)  # Wait 1s to avoid hitting the 60 requests per minute limit
    if nbLoc > 0
        return average_temp / nbLoc
    else:
        print("Error: no location in country, check your bounding box and country code.")
        return 0

print(avg_temperature2(-4.9,42.34,8.43,51.09, 9, 'FR'))
