import requests # type: ignore
import smtplib
from bs4 import BeautifulSoup # type: ignore
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime as dt


SERVER = 'smtp.gmail.com'
PORT = 587
FROM = 'automatic634suriko@gmail.com'
TO = 'dubeysumit378@gmail.com'
PASS ='utfambvyhhxiuvuy'

def extract_news(url: str) -> str:
    Emailcontent = ''
    Emailcontent += '<b> HN Top Stories: </b>\n' + '<br>' + '-'*50 + '<br>'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.content
        Beautiful = BeautifulSoup(data, 'html.parser')
        
        for i, topic in enumerate(Beautiful.find_all('td', attrs={'class': 'title', 'valign': ''})):
            if topic.text.lower() != 'more':
                Emailcontent += f'{str(i + 1)}: {topic.text.strip()}<br>'
        
    except requests.exceptions.RequestException as e:
        Emailcontent += f'Error fetching news: {str(e)}'
    return Emailcontent

def setServer():
    try:
        server = smtplib.SMTP(SERVER, PORT)
        server.set_debuglevel(1)
        server.ehlo()
        server.starttls()
        server.login(FROM, PASS)
        return server
    except smtplib.SMTPException as e:
        print(f"Error setting up the email server: {str(e)}")
        raise

def CreateMail(data: str, server):
    now = dt.datetime.now()
    content = f'{data}<br>-------------<br><br>End of Message'

    Message = MIMEMultipart()
    Message['Subject'] = f"Top News Stories HN - {str(now.day)} {str(now.year)}"
    Message['From'] = FROM
    Message['To'] = TO

    Message.attach(MIMEText(content, 'html'))
    try:
        server.sendmail(FROM, TO, Message.as_string())
        print("Email Sent")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {str(e)}")


def main():
    print("Extracting News Stories.......")
    data = extract_news('https://news.ycombinator.com/')
    print("Initiating Server......")
    server = setServer()
    print("Composing Email......")
    CreateMail(data=data, server=server)
    server.quit()

if __name__ == '__main__':
    main()
