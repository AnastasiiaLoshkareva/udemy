# Get Atomic Time from Internet Clock - This program will get the true atomic time from an atomic time clock on the Internet. 
# Use any one of the atomic clocks returned by a simple Google search.
# import modules for getting info from web sites and getting right html parsing
import requests
import bs4

#import regular expression module
import re

#get access to the site
response = requests.get('https://www.worldtimeserver.com/current_time_in_UTC.aspx')

#parse html from resource correctly
soup = bs4.BeautifulSoup(response.text,'lxml')

# identify a html tag with id=theTime - that shows real time
str_time = soup.select('#theTime')[0].text

#get only time as text
get_time = re.findall(r'\d+:\d{2}:\d{2}',str_time)
print('Current time is: ' + get_time[0])

if __name__ == '__main__':
    main()
