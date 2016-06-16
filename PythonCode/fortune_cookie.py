## Fortune Cookie
## Program by Your Name
## 20 May 2016


import random

select = random.randint(1,3)
cookie_select = "cookie"+str(select)

fortune_cookie = {'cookie1': 'No wind, no waves', \
                  'cookie2': 'How do you know what you don\'t know?', \
                  'cookie3': 'next message', \
                  'cookie4': 'mmmmm' }

print(select)
print(cookie_select)
print(fortune_cookie[cookie_select])
