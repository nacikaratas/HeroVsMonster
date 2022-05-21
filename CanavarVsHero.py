import random
import time

hero_sağlık = 100
canavar_sağlık = 125

while hero_sağlık > 0 and canavar_sağlık > 0:
    hasar = random.randint(0, 50)
    hero_sağlık -= hasar
    print("Hero Canavardan:",hasar,"hasar yedi","Heronun sağlığı:",hero_sağlık)
    time.sleep(1)
    if hero_sağlık <= 0:
        print("Hero öldü")
        break
    hasar2 = random.randint(0, 50)
    canavar_sağlık -= hasar2
    print("Canavar Herodan:",hasar2,"hasar yedi","Canavarın sağlığı:",canavar_sağlık)
    time.sleep(1)
    if canavar_sağlık <= 0:
        print("Canavar öldü")
        break