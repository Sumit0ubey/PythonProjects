from bs4 import BeautifulSoup
from requests import request

from os import getenv
from datetime import datetime
from dotenv import load_dotenv
from smtplib import SMTP, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()
SERVER = 'smtp.gmail.com'
PORT = 587
FROM = getenv('FROMEMAIL')
TO = getenv('TOEMAIL').split(",")
PASS = getenv('PASSWORD')

def extractNews(url: str) -> str:
    response = request(url=url, method="GET")
    data = response.content
    soup = BeautifulSoup(data, "html.parser")

    content = """
    <html>
    <body style="margin:0; padding:0; font-family:Arial, sans-serif; background-color:#28282B;">
        <table width="100%" cellpadding="0" cellspacing="0" style="max-width:600px; margin:auto; background-color:#ffffff; padding:20px; border-radius:8px; box-shadow:0px 4px 10px rgba(0,0,0,0.1);">
        <tr>
            <td align="center">
            <h1 style="color:#333;">🚀 Daily IT & Tech News</h1>
            <p style="font-size:14px; color:#777;">Bringing you the latest tech updates every day.</p>
            <hr style="border:1px solid #ddd; width:90%;">
            </td>
        </tr>
    """

    for i, title in enumerate(soup.find_all("h3", class_="loop-card__title")):
        url = title.find("a")
        content += f"""
        <tr>
            <td style="padding:15px; border-bottom:1px solid #ddd; display:flex; align-items:center;">
            <div>
                <p style="margin:0;">
                <a style="text-decoration: none; color: black;" href="{url['href']}" style="color:#007BFF; text-decoration:none;">
                    📌 {title.text}
                </a>
                </p>
            </div>
            </td>
        </tr>
        """

    content += """
                <tr>
                    <td align="center" style="padding-top:30px;">
                    <p style="font-size:12px; color:#999;">You are receiving this email because you subscribed to our daily tech news.</p>
                    <p style="font-size:12px; color:#999;">Powered by <strong>Sumit Dubey</strong></p>
                    <a href="https://github.com/Sumit0ubey/" 
                        style="font-size:12px; color:#FF0000; text-decoration:none;">Unsubscribe</a>
                    </td>
                </tr> 
            </table>
        </body>
    </html>"""

    return content


def setServer():
    try:
        server = SMTP(SERVER, PORT)
        server.starttls()
        server.ehlo()
        server.login(FROM, PASS)
        return server
    except SMTPException as e:
        print(f"An Error Occur while connecting to the server: {e}")
        raise

def createMail(data: str, server):
    date = datetime.now()
    
    for user in TO:
        message = MIMEMultipart()
        message["From"] = FROM
        message["Subject"] = f"IT News - Automation Email | {str(date.day)}:{str(date.month)}:{str(date.year)}"
        message.attach(MIMEText(data, "html"))
        message["To"] = user
        try:
            server.sendmail(FROM, user, message.as_string())
        except SMTPException as e:
            print(f"Error sending email: {str(e)}")
        print(f"Email send to {user}")

def main():
    print("Extracting News Stories.......")
    data = extractNews('https://techcrunch.com/latest/')
    print("Initiating Server......")
    server = setServer()
    print("Composing Email......")
    createMail(data=data, server=server)
    server.quit()
    print("Email Send")

if __name__ == '__main__':
    main()
