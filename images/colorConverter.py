from PIL import Image, ImageDraw



def main():
    #ask the user for an image file they would like to change the colors of
    #defin the image file into a varible and assign it double quotes
    image_file = ("")
    image_file = input("what is the chart, or image you would like to upload?")
    #print a list of different types of color filters to cutomize to
    #assign each type a number to make it easier for the user to input the type
    print()
    print("Color Filter:")
    print("1. red ")
    print("2. green ")
    print("3. blue ")
    print("4. gray ")
    
    #ask the user for the type of color filter they want to convert to and save it to varible
    value_scale = input("Which type of color filter would you like to convert to?")

    #assign a varible to function to open, display, get the pixels, find the width and height,
    #and create a new image for the image the user input
    user_image = open_image(image_file)
    show_image(user_image)
    user_pixels = get_pixels(user_image)
    (width, height) = user_image.size
    new_color_image = new_image(user_image)
   


    # create if statements to lanch the correct function depending on the user input

    if value_scale == "1":
        red_scale(user_image, user_pixels, new_color_image, width, height)
    if value_scale == "2":
        green_scale(user_image, user_pixels, new_color_image, width, height)
    if value_scale == "3":
        blue_scale(user_image, user_pixels, new_color_image, width, height)
    if value_scale == "4":
        gray_scale(user_image)
    else: 
        print("I'm sorry, that is not a valid option")

#create a function that will open and read and return the file given by the user
def open_image(image_file):
    color_image = Image.open(image_file)
    return color_image

#display the original un edited image file to the user
def show_image(user_image):
    user_image.show()

#create a new image for the new color values to be added to   
def new_image(user_image):
    output_image = Image.new("RGB", user_image.size)
    return output_image

#get the pixels from the image file given by the user
def get_pixels(user_image):

    pixels_image = user_image.load()
    return pixels_image





def red_scale(user_image, user_pixels, new_color_image, width, height):
    """changes each value to the the same value but in the color red."""
    
    


    def distance2(color1, color2):
        r1, g1, b1 = color1
        r2, g2, b2 = color2
        return (r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2

    color_to_change = (150, 150, 150)
    
    threshold = 250

    # Create output image
    
    draw = ImageDraw.Draw(new_color_image)

    # Generate image
    for x in range(width):
        for y in range(height):
            r, g, b = user_pixels[x, y]
            if distance2(color_to_change, user_pixels[x, y]) < threshold ** 2:
                r = int(r * 1.50)
                g = int(g * .50)
                b = int(b * .50)
            draw.point((x, y), (r, g, b))
    
    #display and save the new image
    new_color_image.show()
    new_color_image.save("new_image.png")


def green_scale(user_image, user_pixels, new_color_image, width, height):
    """changes each value to the the same value but in the color green."""

    def distance2(color1, color2):
        r1, g1, b1 = color1
        r2, g2, b2 = color2
        return (r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2

    color_to_change = (150, 150, 150)
    threshold = 230


    # Create output image
    
    draw = ImageDraw.Draw(new_color_image)

    # Generate image
    for x in range(width):
        for y in range(height):
            r, g, b = user_pixels[x, y]
            if distance2(color_to_change, user_pixels[x, y]) < threshold ** 2:
                r = int(r * .50)
                g = int(g * 1.00)
                b = int(b * .50)
            draw.point((x, y), (r, g, b))

    #display and save the new image
    new_color_image.show()
    new_color_image.save("new_image.png")



def blue_scale(user_image, user_pixels, new_color_image, width, height):
    """changes each value to the the same value but in the color blue."""

    def distance2(color1, color2):
        r1, g1, b1 = color1
        r2, g2, b2 = color2
        return (r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2

    color_to_change = (150, 150, 150)
    
    threshold = 230


    # Create output image
    
    draw = ImageDraw.Draw(new_color_image)

    # Generate image
    for x in range(width):
        for y in range(height):
            r, g, b = user_pixels[x, y]
            if distance2(color_to_change, user_pixels[x, y]) < threshold ** 2:
                r = int(r * .50)
                g = int(g * .50)
                b = int(b * 1.50)

            
            draw.point((x, y), (r, g, b))

    #display and save the new image
    new_color_image.show()
    new_color_image.save("new_image.png")



def gray_scale(user_image):
    """changes each value to the the same value but in the color gray."""

    new_color_image = user_image.convert("L")

    #display and save the new image
    new_color_image.show()
    new_color_image.save("new_image.png")


if __name__ == "__main__":      
    main()