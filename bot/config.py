#    Copyright (c) 2021 Danish_00
#    Improved By @Zylern

from decouple import config

try:
    APP_ID = config("14082290", cast=int)
    API_HASH = config("ef7c8ee7f5a019ccca3f28d441d3bc49")
    BOT_TOKEN = config("5777606472:AAHrGefe6WVNjxNSC13wW0AfNLisusztUMw")
    DEV = 1664850827
    OWNER = config("1851497983")
    ffmpegcode = ["-preset faster -c:v libx265 -s 854x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By TGVid-Comp (https://github.com/Zylern/TGVid-Comp)' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1"]
    THUMBNAIL = config("https://te.legra.ph/file/482f15b1b331e15ff15c3.jpg", default="https://telegra.ph/file/f9e5d783542906418412d.jpg")
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
