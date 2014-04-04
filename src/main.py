#! /usr/bin/env python

import asyncore
import uuid

from smtpd import SMTPServer

class MailServer(SMTPServer):
    no = 0
    def process_message(self, peer, mailfrom, rcpttos, data):
        f = open('%s.eml' % uuid.uuid4(), 'w')
        f.write(data)
        f.close

def run():
    foo = MailServer(('localhost', 25), None)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    run()