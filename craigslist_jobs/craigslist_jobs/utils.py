from craigslist_jobs import settings
import smtplib

class Email(object):
  
  def __init__(self):
    """
    Set the smpt credientials from the settings.py values
    """
    self.email_user = settings.EMAIL_USER
    self.email_password = settings.EMAIL_PASSWORD 
    self.smtp_server = settings.SMTP_SERVER
    self.smpt_port = settings.SMTP_PORT


  def build_message_from_gigs(self, gigs_list):
    """
    Takes a list of scrapy Gig(Items) and builds a message string to 
    send as email body
    return string
    """
    message = ''
    for gig in gigs_list:
      message += '%s - %s - %s\n' % (gig['name'], gig['url'], ','.join(gig['skills']))
    return message
   

  def send(self, recipient_address, message):
    """
    Send an email message to a recipient
    """
    smtpserver = smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.login(self.email_user, self.email_password)
    header = 'To:' + recipient_address + '\n' + 'From: ' + self.email_user + '\n' + 'Craigslist:Jobs' + '\n'
    msg = header + '\n' + message + '\n\n'
    smtpserver.sendmail(self.email_user, recipient_address, msg)
    smtpserver.close()

