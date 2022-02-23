from PIL import Image, ImageDraw
from red import Red
from green import Green
from blue import Blue


class Director():
    def main(self):
        #ask the user for an image file they would like to change the colors of
        #defin the image file into a varible and assign it double quotes
        self.image_file = ("")
        self.image_file = input("what is the chart, or image you would like to upload?")
        #print a list of different types of color filters to cutomize to
        #assign each type a number to make it easier for the user to input the type
        print()
        print("Color Filter:")
        print("1. red ")
        print("2. green ")
        print("3. blue ")
        print("4. gray ")
        
        #ask the user for the type of color filter they want to convert to and save it to varible
        self.value_scale = input("Which type of color filter would you like to convert to?")

        #assign a varible to function to open, display, get the pixels, find the width and height,
        #and create a new image for the image the user input
        self.user_image = self.open_image(self.image_file)
        self.show_image(self.user_image)
        self.user_pixels = self.get_pixels(self.user_image)
        (self.width, self.height) = self.user_image.size
        self.new_color_image = self.new_image(self.user_image)
    


        # create if statements to lanch the correct function depending on the user input

        if self.value_scale == "1":
            self.red_scale(self.user_image, self.user_pixels, self.new_color_image, self.width, self.height)
        if self.value_scale == "2":
            self.green_scale(self.user_image, self.user_pixels, self.new_color_image, self.width, self.height)
        if self.value_scale == "3":
            self.blue_scale( self.user_image, self.user_pixels, self.new_color_image, self.width, self.height)
        if self.value_scale == "4":
            self.gray_scale(self.user_image)
        else: 
            print("I'm sorry, that is not a valid option")

    #create a function that will open and read and return the file given by the user
    def open_image(self, image_file):
        self.color_image = Image.open(self.image_file)
        return self.color_image

    #display the original un edited image file to the user
    def show_image(self, user_image):
        self.user_image.show()

    #create a new image for the new color values to be added to   
    def new_image(self, user_image):
        self.output_image = Image.new("RGB", self.user_image.size)
        return self.output_image

    #get the pixels from the image file given by the user
    def get_pixels(self, user_image):

        self.pixels_image = self.user_image.load()
        return self.pixels_image
