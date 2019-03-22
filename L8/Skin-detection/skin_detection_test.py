from PIL import Image
import pandas as pd
import os

def open_image(src): 
    return Image.open(src,'r')

                   
def test(probability, path):
    
    im = open_image(path)
    temp = im.copy()
    create_image(temp, probability,path)


def create_image(im,probability,path): 
    
    width, height = im.size

    pix = im.load()
  
    for i in range(width):
        for j in range(height):
            r,g,b = im.getpixel((i,j))
            row_num = (r*256*256) + (g*256) + b #calculating the serial row number 
            if(probability['Probability'][row_num] <0.555555):
                pix[i,j] = (0,0,0)
            else:
                pix[i,j] = (255,255,255)
                
    saveImage(im,path)
    
def saveImage(image,path): ## saving image
    image.save(path.replace(".jpg","_result.jpg"))

def main():

    print("Reading CSV...")
    probability = pd.read_csv('train.csv') # getting the rows from csv    
    print('Data collection completed') 
    
    imgs = os.listdir("test/")
    for i in imgs:

        if "_result" in i or ".DS_Store" in i:
            continue
        path = 'test/%s' % i
        print(path)
        test(probability, path) # this tests the data
        print("Image created")


if __name__ == "__main__":
    main()

