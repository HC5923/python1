import telegram123

chii_token = '123456789:ABCDEDFGHIJKLMNOPQRST'
chii = telegram123.Bot(token = chii_token)
updates = chii .getUpdates()
for u in updates:
    print(u.message)
