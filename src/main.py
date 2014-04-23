#! /usr/bin/env python

import getpass, poplib
import ConfigParser
import re
import importlib

from email.parser import Parser
from email.header import decode_header

def main():
    config = ConfigParser.RawConfigParser()
    config.read('mail.cfg')

    host = config.get('Host', 'POP3')
    ssl = config.getint('Host', 'SSL')

    user = config.get('Account', 'User')
    password = config.get('Account', 'Password')

    rules = []
    for rule in config.options('Rules'):
        rules.append({ 'module': rule, 'rule': config.get('Rules', rule) })

    if user and password:
        if ssl:
            print('Connect to %s by SSL' % host)
            mail = poplib.POP3_SSL(host, 995)
        else:
            print('Connect to %s' % host)
            mail = poplib.POP3(host, 995)

        mail.user(user)
        mail.pass_(password)
        total = len(mail.list()[1])

        print('%d mail(s) fetched.' % total)

        for i in range(total):
            headers = Parser().parsestr('\n'.join(mail.retr(i+1)[1]))
            subject = decode_header(headers['subject'])[0][0]

            matched = False
            
            for r in rules:
                m = re.match(r['rule'], subject, re.I)
                if m: # find registered rule
                    matched = True
                    
                    module = importlib.import_module('modules.' + r['module'])
                    module.main(m.group('param'))

            if matched:
                print(matched)
                mail.dele(i+1) # delete mail

        mail.quit()

if __name__ == '__main__':
    main()

