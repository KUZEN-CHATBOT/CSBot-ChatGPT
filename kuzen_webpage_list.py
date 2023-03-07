import requests
import time
urls = [
#'https://corp.kuzen.io/',
#'https://www.kuzen.io/',
#'https://www.kuzen.io/support.html',
#'https://www.kuzen.io/appraisal.html',
#'https://www.kuzen.io/kuzen-recruitment.html',
#'https://www.kuzen.io/education.html',
#'https://www.kuzen.io/hr.html',
#'https://www.kuzen.io/jiti-dx.html',
#'https://www.kuzen.io/cases.html',
#'https://www.kuzen.io/seminar.html',
'https://www.kuzen.io/partner_program.html',
#'https://www.kuzen.io/cases/bizmates.html',
#'https://www.kuzen.io/cases/17live.html',
'https://corp.kuzen.io/news.html',
'https://www.kuzen.io/kuzen-nurture.html',
'https://www.kuzen.io/kuzen-efo.html',
'https://www.kuzen.io/kuzen-stopper.html',
'https://www.kuzen.io/assistant.html',
'https://www.kuzen.io/support.html',
'https://www.kuzen.io/terms.html',
'https://www.kuzen.io/privacy.html'
]
for url in urls:
    response = requests.post('https://stg-chat.kuzen.io/index', data={'url': url, 'original_service_id': '9385'})
    print(response.status_code)
    print(f"{response.text}: {url}")
    time.sleep(6)
