import scratchattach as scratch3
import requests
from PIL import Image
from io import BytesIO
from math import floor
from time import sleep

# Does not work on replit
session = scratch3.login("Your username", "Your password")

#                             ⬇ Make this your project Id
conn = session.connect_cloud("827525110")

#The id of the project that it grabs the thumbnail of.
projectId = 817510750

while True:
    print("Current Project: %i" % projectId)
    projectId += 1
    # You can change this to any image url
    url = "https://uploads.scratch.mit.edu/get_image/project/"+str(projectId)+"_56x42.png"
    
    response = requests.get(url)
    im = Image.open(BytesIO(response.content)) #loads image
    pix = im.load()

    line = ''
    conn.set_var("thumb", "0")
    sleep(.01)
    width, height = im.size
    # 42 is the max number of pixels you can fit in one variable
    jump = height/42
    # You change 56 to up the horizontal quality
    xJump = width/56

    for y in range(56):
        line = ''
        for x in range(42):
            for i in range(3):
                try:
                    pixel = str(round(pix[floor(xJump*y),floor(jump*x)][i]/10)) # Puts a pixel into rgb value divided by 10 to fit more pixels in a single cloud variable.
                    
                except TypeError:
                    pixel = "25"
                
                if len(pixel) == 1: #makes sure all values are two characters long
                    pixel = '0' + pixel
                    
                line += pixel
           
        conn.set_var("thumb", line)
        
    sleep(5)
    

