"""
Yapımcı: Webhook spammer made by lyxsca
Discord: lyxscasemenov
Github: lyxscaxd
"""
print("""

  _                          
 | |_   ___  _____  ___ __ _ 
 | | | | \ \/ / __|/ __/ _` |
 | | |_| |>  <\__ \ (_| (_| |
 |_|\__, /_/\_\___/\___\__,_|
    |___/                    
                           

                                Made by lyxscasemenov
                                   Github: lyxscaxd
""")


from dhooks import Webhook
import time


message = input("Ne spamlamak istiyorsun?: ")
webhookurl = Webhook(input("webhook gir: "))
delay = int(input("delay yaz: "))


while True:
    time.sleep(delay)
    webhookurl.send(message)
    print("illegalsemenov")