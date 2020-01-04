import requests
import bs4
import collections

Weather_Report=collections.namedtuple('Weather_Report', 'cond, loc')

def main():
    print_header()
    code=get_zipcode()
    html=fetch_html_text(code)
    report=fetch_data(html)
    print('The condition in {} is {}'.format(report.loc, report.cond))
    #display_forecast()



def print_header():
    print('----------------------------------------------')
    print('                 WEATHER APP')
    print('----------------------------------------------')

def get_zipcode():
    zipcode =input("Please state your zipcode. eg 02139")
    return zipcode.strip()

def fetch_html_text(zipcode):
    url='https://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response=requests.get(url)
    #print (response.status_code)
    #print (response.text[0:250])
    return response.text


def fetch_data(html):
    soup=bs4.BeautifulSoup(html, 'html.parser')
    loc=soup.find(class_='region-content-header').find('h1').get_text()
    condition=soup.find(class_='condition-icon').get_text()
    #temp=soup.find(class_='wu-unit-temperature').find(class_='wu_value').get_text()
    #scale =soup.find(class_='wu-unit-temperature').find(class_='wu_label').get_text()
    loc=text_cleanup(loc)
    condition=text_cleanup(condition)
    report=Weather_Report(cond=condition, loc=loc)
    return report


def text_cleanup(text):
    if not text:
        return text
    elif text:
        return text.strip()




















if __name__=='__main__':
    main()