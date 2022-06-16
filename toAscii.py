from PIL import Image
from flask import Flask, redirect, url_for, render_template

# app = Flask(__name__)

# @app.route("/<name>")
# def home(name):
# #    return render_template("index.html", content=name,s=2)
#     return render_template("index.html", content=["sedra","layla","alaa"])





# # @app.route("/<name>")
# # def result(name):
# #     return f"Here is your {name}!"

# # @app.route("/admin/")
# # def admin():
# #     return redirect(url_for("ASCII",name="Admin!"))
# if __name__ == "__main__":
#     app.run()


# ascii characters used to build the output text
#customizable settings: chars, resolution, animation frames
# style= int(input("choose style: \n 1- \n 2- \n 3-\n"))
# add switch here for ascii style
ASCII_CHARS = ["G", "F", "8", "*", ":", ",", " ", " ", " ", " ", " "]


#adjust/set resolution
resolution= int(input("Enter resolution \n * 0 to 100 is low, 101 to 200 is medium, 201 and above is high \n "))

x= resolution/resolution*2.25
# resize image according to a new width
def resize_image(image, new_width=resolution):
    width, height = image.size
    ratio = height/width/x
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)
    
# convert pixels to a string of ascii characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)    

def main(new_width=resolution):
    # attempt to open image from user-input
    path = input("Enter a valid pathname to an image:\n")
    try:
        image = Image.open(path)
    except:
        print(path, " is not a valid pathname to an image.")
        return
  
    # convert image to ascii    
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))
    
    # format
    pixel_count = len(new_image_data)  
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
    
    # print result
    print(ascii_image)
    150
    # save result to "ascii_image.txt"
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)
 
# run program
main()