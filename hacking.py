import urllib
import webbrowser
from xml.etree.ElementTree import parse

# u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
# data = u.read()
# f = open('rt22.xml','wb')
# f.write(data)
# f.close()

doc = parse('rt22.xml')

for bus in doc.findall('bus'):
    d = bus.findtext('id')
    lat = float(bus.findtext('lat'))
    if lat > 0:
        direction = bus.findtext('d')
        if direction.startswith("North"):
            print d
#    print lat

#webbrowser.open('http://baidu.com')