import os
import yagmail


def send_mail(kindle_email_id, mobi_path,
              oauth2_file=True, subject='Book Uploaded'):
    if oauth2_file:
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        oauth2_file = os.path.join(parent_dir, 'credentials.json')
    else:
        oauth2_file = None
    yag = yagmail.SMTP(None, oauth2_file=oauth2_file)
    yag.send(to=kindle_email_id, subject=subject,
             contents='From Kindered with Love.🔥',
             attachments=mobi_path)

