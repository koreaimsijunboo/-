from time import sleep
from random import choice
import gtts
import os


text = "밥 다 됬어?"
text2 = "아니"
text3 = "응"

lang = "ko"

gt = gtts.gTTS(text=text,lang=lang,slow=False)
gt1 = gtts.gTTS(text=text2,lang=lang,slow=False)
gt2 = gtts.gTTS(text=text3,lang=lang,slow=False)

gt.save("밥_질문.mp3")
gt1.save("밥_대답.mp3")
gt2.save("밥_배답1.mp3")


hi = [1,2,3,4,5,6,7,8,9]
var1 = 0
he = choice(hi)

while var1 != he:
    os.system("밥_질문.mp3")
    sleep(5)
    os.system("밥_대답.mp3")
    sleep(5)
    var1 += 1

os.system("밥_질문.mp3")
sleep(5)
os.system("밥_배답1.mp3")
