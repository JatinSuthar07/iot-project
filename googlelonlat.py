import requests
import smtplib as s
import pyowm
GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json'

params = {'address': 'Jaipur,India','sensor': 'false','region': 'india'}

# Do the request and get the response data
req = requests.get(GOOGLE_MAPS_API_URL, params=params)
res = req.json()

# Use the first result
result = res['results'][0]

geodata = dict()
geodata['lat'] = result['geometry']['location']['lat']
geodata['lng'] = result['geometry']['location']['lng']
geodata['address'] = result['formatted_address']
print('{address}. (lat, lng) = ({lat}, {lng})'.format(**geodata))
latt=geodata['lat']
lann=geodata['lng']
print(latt,lann)
owm = pyowm.OWM('5304fa933d98ccbc60cec32e958937b4')

observation = owm.weather_at_place(params['address'])
w = observation.get_weather()
temperature = w.get_temperature('celsius')
tomorrow = pyowm.timeutils.tomorrow()
wind = w.get_wind()
#print(w)
print(wind)
print(temperature)
print(tomorrow)
#c=str(wind)+str(temperature)+str(tomorrow)
c='temp is:'+str(temperature['temp'])
d=str(int(latt))+' '+str(int(lann))
e=c+d
print(e)
m=s.SMTP('smtp.gmail.com',587)
m.starttls()
id='destrothedestroyeer@gmail.com'
m.login(id,'destro_14')
m.sendmail(id,'snybhatt838@gmail.com',e)
m.sendmail(id,'snybhatt838@gmail.com',d)
print('MAIL SENT')
m.close()


