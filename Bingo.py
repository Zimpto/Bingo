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
    
    noNumber = np.concatenate(
        ([np.ones(5)], [np.ones(5)], [np.ones(5)]))
    noNumber = np.concatenate(
        (noNumber,[np.ones(5)+1], [np.ones(5)+1], [np.ones(5)+1]))
    noNumber = np.concatenate(
        (noNumber,[np.ones(5)-1], [np.ones(5)-1], [np.ones(5)-1])).T

    for i in noNumber:
        rng.shuffle(i)

    noNumber = noNumber.T
    
    num3 = noNumber[0][0]
    noNumber[0][0] = 3
    
    num4 = noNumber[-1][0]
    noNumber[-1][0] = 4
    
    noNumber = noNumber.astype(int).tolist()
    
    # print(noNumber)
    
    # noNumber = []
    
    for i in range(9):
        if i==0:
            numberList.append(np.arange(1,10).tolist())
            # noNumber.append([3]+
            #                 list(rng.integers(3, size =4)))
        elif i==8:
            numberList.append(np.arange(80,91).tolist())
            # noNumber.append([4]+
            #                 list(rng.integers(3, size =4)))
        else:
            numberList.append(np.arange(i*10,10+i*10).tolist())
            # noNumber.append(list(rng.integers(3, size =5)))
            
    # print(noNumber)
    noNumber = np.array(noNumber).T
    unique, counts = np.unique(noNumber[0], return_counts=True)
    noNumber =noNumber.T.tolist()
    # print(noNumber)
        # numberList.append(np.arange(1+i*10,11+i*10).tolist())
    for i in range(9):
        for ii1 in range(5):
            # noNum = noNumber[i].pop(rng.choice(len(noNumber[i])))
            noNum = noNumber[i].pop(0)
            if i==0:
                print(noNum)
            # noNum = noNumber[i].pop(0)
            if noNum==3:
                tracker2 = rng.choice(3)
            tracker = 0
            for ii in range(3):
                img1.rectangle([(m*i,m*(ii+ii1*3)+ii1*hA),
                                (m*i+m+rand, m*(ii+ii1*3)+m+rand+ii1*hA)], 
                               fill = (255,255,255), 
                               outline = (0,0,0), width=rand)
                
                if noNum==3:
                    if ii == num3:
                    # if counts[ii]<3:
                        number = numberList[i].pop(rng.choice(len(numberList[i])))
                        img1.text((m*i+m/2+rand/2,m*(ii+ii1*3)+ii1*hA+m/2+size/3), 
                                  str(number),
                                  fill=(0,0,0), font=font, anchor = "ms")
                        # counts[ii] += 1
                        # break
                    
                    tracker += 1
                
                elif noNum==4:
                    if ii == num4:
                        number = numberList[i].pop(rng.choice(len(numberList[i])))
                        img1.text((m*i+m/2+rand/2,m*(ii+ii1*3)+ii1*hA+m/2+size/3), 
                                  str(number),
                                  fill=(0,0,0), font=font, anchor = "ms")
                    
                elif ii!=noNum:
                    # print(f"ii: {ii}\nnoNum: {noNum}\nii1: {ii1}\ni: {i}")
                    number = numberList[i].pop(rng.choice(len(numberList[i])))
                    img1.text((m*i+m/2+rand/2,m*(ii+ii1*3)+ii1*hA+m/2+size/3), 
                              str(number),
                              fill=(0,0,0), font=font, anchor = "ms")
                    tracker += 1
            
    img.save(f"BingoBlaetter/BingoGanz{bingoNumber}.png")
    # img.show()

for i in range(1):
    test = ZettelGanz(10,i,3)


#%%
# rng = np.random.default_rng()

# # numberList = []

# # test = np.concatenate((np.array([[3,1,2]]).T,np.array([[4,2,0]]).T), axis = 1)


# noNumber = np.concatenate(([np.ones(5)], [np.ones(5)], [np.ones(5)]))
# noNumber = np.concatenate((noNumber,[np.ones(5)+1], [np.ones(5)+1], [np.ones(5)+1]))
# noNumber = np.concatenate((noNumber,[np.ones(5)-1], [np.ones(5)-1], [np.ones(5)-1])).T
# # noNumber[0][0] = 3

# # noNumber[-1][0] = 4
# for i in noNumber:
#     rng.shuffle(i)

# noNumber = noNumber.T



# noNumber = noNumber.astype(int).tolist()

# noNumber = np.array(noNumber).T
# unique, counts = np.unique(noNumber[0], return_counts=True)
# noNumber =noNumber.T.tolist()



# noNumber = []

# for i in range(9):
#     if i==0:
#         noNumber.append([3]+
#                         list(rng.integers(3, size =4)))
#     elif i==8:
#         noNumber.append([4]+
#                         list(rng.integers(3, size =4)))
#     else:
#         noNumber.append(list(rng.integers(3, size =5)))





















