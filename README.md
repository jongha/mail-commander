# mail-commander

I want to control the server remotely. However, there are security problems. So, I decided to develop a program that can remote control the server safely and easily. It is using email's pop3 server located in internal network. This is still not perfect from a security. However, if you are using a well-controlled internal network it will be very useful.

## Description

This is `mail.cfg` file.

```
[Host]
POP3=POP3SERVER
SSL=1

[Account]
User=YOURACCOUNT
Password=YOURPASSWORD

[Rules]
echo=\[Daily report\] (?P<param>.*)
echo2=\[WARNING\] (?P<param>.*)
```

* Host
 * POP3
  * Server address of pop3. (ex: outlook.office365.com)
 * SSL
  * 1 is SSL, 0 is Non-SSL
* Account
 * User
  * User account for POP3
 * Password
  * User password for POP3
* Rules
 * key
  * Python module name in `modules` subdirectory.
 * value
  * A regular expression for subject selecting.
  * `?P<param>` is input parameter to module.

### Module Sample

Sample of echo.py in modules subdirectory.

```
#! /usr/bin/env python

def main(param):
    # implement your command
    print('echo module', param)

if __name__ == '__main__':
    main()
```

## Usage

You can run a `main.py` file periodically or you can use crontab.

# License

mail-commander is available under the terms of the MIT License.
