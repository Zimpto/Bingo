from PIL import Image, ImageDraw, ImageFont
import numpy as np

#%%

def ZettelGanz(mult:int, bingoNumber:int, rand:int = 1):
    m = 10*mult
    rand *=2
    # creating new Image object
    img = Image.new("RGB", (9*m+rand, 3*6*m+rand),(255,255,255))
    # create rectangle drawable image
    img1 = ImageDraw.Draw(img)
    
    size = 8*mult
    fontpath = "B:/PyProjekt/Bingo/"
    # font = ImageFont.truetype(fontpath+"SourceCodePro-Black.otf",size)
    font = ImageFont.truetype(fontpath+"Fonts/UbuntuMono-B.ttf",size)
    
    rng = np.random.default_rng()
    
    # höhenAusgleich
    hA = (m+rand)/2
    
    numberList = []
    
    "List with numbers 1-9, 10-19, 20-29,...,80-90"
    for i in range(9):
        numberList.append(np.arange(i*10+(1 if i%10==0 else 0),
                                    10+i*10+int(i/8)))

    for i in range(9):
        rng.shuffle(numberList[i])
        if i == 0:
            currNums = np.split(numberList[i][1:],4)
            currNums.append(np.array(numberList[i][0]))
        elif i == 8:
            currNums = np.split(numberList[i][3:],4)
            currNums.append(np.array(numberList[i][0:3]))
        else:
            currNums = np.split(numberList[i],5)
        print(f"i: {i}, currNums: {currNums}")
        for ii in range(5):
            # blank = rng.integers(3, size = 3-currNums[ii].size, replace=False)
            blank = rng.choice(3, 3-currNums[ii].size, False)
            counter = 0
            for iii in range(3):
                img1.rectangle([(m*i,m*(iii+ii*3)+ii*hA),
                                (m*i+m+rand, m*(iii+ii*3)+m+rand+ii*hA)], 
                               fill = (255,255,255), 
                               outline = (0,0,0), width=rand)
                if iii not in blank:
                    # print(f"currNums: {currNums}\nblank: {blank}")
                    if currNums[ii].size > 1:
                        number = currNums[ii][counter]
                    else: number = currNums[ii]
                    img1.text((m*i+m/2+rand/2,m*(iii+ii*3)+ii*hA+m/2+size/3), 
                              str(number),
                              fill=(0,0,0), font=font, anchor = "ms")
                    counter += 1
            
    img.save(f"BingoBlaetter/BingoGanz{bingoNumber}.png")
    # img.show()

for i in range(1):
    test = ZettelGanz(10,i,3)


#%%
numberList = []

for i in range(9):
    # if i == 0
    if not i:
        numberList.append(np.arange(1,10))
    elif i==8:
        numberList.append(np.arange(80,91))
    else:
        numberList.append(np.arange(i*10,10+i*10))

#%%
rng = np.random.default_rng()

numberList = []

"List with numbers 1-9, 10-19, 20-29,...,80-90"
for i in range(9):
    numberList.append(np.arange(i*10+(1 if i%10==0 else 0),
                                10+i*10+int(i/8)))

rng.shuffle(numberList[0])
currNums = np.split(numberList[0][1:],4)
currNums.append(np.array(numberList[0][0]))


#%%









