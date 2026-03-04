import subprocess
from google import genai
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def getDiff():
    diff = subprocess.check_output(["git", "show"], text=True)
    return diff


client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def send_email(html_content):

    sender_email = os.getenv("SENDER_EMAIL")
    receiver_email = os.getenv("RECEIVER_EMAIL")
    password = os.getenv("EMAIL_PASSWORD")

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "AI Code Review Feedback"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    part = MIMEText(html_content, "html")
    msg.attach(part)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())


def main():

    diff = getDiff()

    prompt = f"""
    Review the following code changes and give feedback.

    Mandatory:
    Provide output in clean HTML format suitable for email.

    Code Changes:
    {diff}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    review_html = response.text

    send_email(review_html)


main()