#Section: 9-Arayat
#07 Mañago, #08 Maniquis, #09 Miranda

x = int(input("Enter your birth year:"))
if x < 1900:
    print("Invalid Year, it should not be earlier than 1900")

chinesezodiac = (x - 1900) % 12

if chinesezodiac == 1:
    y = "Rat (鼠 / Shǔ)"
elif chinesezodiac == 2:
    y = "Ox (牛 / Niú)"
elif chinesezodiac == 3:
    y = "Tiger (虎 / Hǔ)"
elif chinesezodiac == 4:
    y = "Rabbit (兔 / Tù)"
elif chinesezodiac == 5:
    y = "Dragon (龙 / Lóng)"
elif chinesezodiac == 6:
    y = "Snake (蛇 / Shé"
elif chinesezodiac == 7:
    y = "Horse (马 / Mǎ)"
elif chinesezodiac == 8:
    y = "Goat (羊 / Yáng)"
elif chinesezodiac == 9:
    y = " Monkey (猴 / Hóu))"
elif chinesezodiac == 10:
    y = "Rooster (鸡 / Jī)"
elif chinesezodiac == 11:
    y = "Dog (狗 / Gǒu)"
elif chinesezodiac == 12:
    y = "Pig (猪 / Zhū)"
    
print(f"Your Chinese Zodiac Sign is: {y}")


