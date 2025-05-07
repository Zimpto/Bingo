from PIL import Image, ImageDraw, ImageFont
import numpy as np

#%%

def BingoSheet(bingoNumber:int = 1):
    # multiplier
    m = 10*10
    # border of the rectangles drawn
    border = 6
    # creating new Image object
    img = Image.new("RGB", (9*m+border, 3*6*m+border-87),(255,255,255))
    # create rectangle drawable image
    img1 = ImageDraw.Draw(img)
    
    size = 8*10
    font = ImageFont.truetype("Fonts/UbuntuMono-B.ttf",size)
    
    rng = np.random.default_rng()
    
    # heightBalancing
    hB = (m+border)/2
    
    blankList = np.repeat([0,0,0,1,1,1,2,2,2], 5).reshape(9,5)
    
    for i in range(5):
        rng.shuffle(blankList[:,i])

    blankList = blankList.tolist()
    
    "List with numbers 1-9, 10-19, 20-29,...,80-90"
    numberList = []
    for i in range(9):
        numberList.append(np.arange(i*10+(1 if i%10==0 else 0),
                                    10+i*10+int(i/8)))

    for i in range(9):
        # i stands for the columns across the rectangles
        rng.shuffle(numberList[i])
        # currNums originate from the numberList 
        # currNums are for one of the five rectangles
        # its important to match the first and the last special column
        if i == 0:
            currNums = np.split(numberList[i][1:],4)
            currNums.append(numberList[i][0])
            rng.shuffle(currNums)
            for ind, element in enumerate(currNums):
                if element.size == 1:
                    specialIndex = ind
        elif i == 8:
            currNums = np.split(numberList[i][3:],4)
            currNums.append(numberList[i][0:3])
            rng.shuffle(currNums)
            # align special columns
            for ind, element in enumerate(currNums):
                if (element.size == 3) and (ind != specialIndex):
                    currNums[ind], currNums[specialIndex] = currNums[
                        specialIndex], currNums[ind]
        else:
            currNums = np.split(numberList[i],5)
            rng.shuffle(currNums)
        
        for ii in range(5):
            # ii stands for one rectangle at a time
            # blank chooses a number set to skip drawing a number
            if currNums[ii].size==1:
                while blankList[0][0] == blankList[8][ii]: 
                    rng.shuffle(blankList[8])
                blank = [blankList[0].pop(0), blankList[8].pop(ii)]
                currNums[ii] = [currNums[ii]]
            elif currNums[ii].size==3:
                blank = []
            else:
                blank = [blankList[i].pop(0)]
            
            currNums[ii] = np.sort(currNums[ii]).tolist()
            for iii in range(3):
                # iii stands for the three columns in one rectangle
                # img1.rectangle draws the squares
                img1.rectangle([(m*i,m*(iii+ii*3)+ii*hB),
                                (m*i+m+border, m*(iii+ii*3)+m+border+ii*hB)], 
                               fill = (255,255,255), 
                               outline = (0,0,0), width=border)

                if iii not in blank:
                    if isinstance(currNums[ii], int):
                        currNums[ii] = [currNums[ii]]
                    number = currNums[ii].pop(0)
                    img1.text((m*i+m/2+border/2,m*(iii+ii*3)+ii*hB+m/2+size/3), 
                              str(number),
                              fill=(0,0,0), font=font, anchor = "ms")

    img.save(f"BingoSheets/BingoSheet{abs(bingoNumber)-1}.png")
    
    if abs(bingoNumber)-1:
        return BingoSheet(abs(bingoNumber)-1)

# integer argument creates integer amount of different bingo sheets, default is one
BingoSheet()

