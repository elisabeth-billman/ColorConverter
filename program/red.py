from PIL import Image, ImageDraw


class Red():

    def distance2(self, color1, color2):
        r1, g1, b1 = color1
        r2, g2, b2 = color2
        return (r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2

    def red_scale(self, user_image, user_pixels, new_color_image, width, height):
        """changes each value to the the same value but in the color red."""
        
        



        self.color_to_change = (150, 150, 150)
        
        self.threshold = 250

        # Create output image
        
        self.draw = ImageDraw.Draw(new_color_image)

        # Generate image
        for x in range(width):
            for y in range(height):
                r, g, b = user_pixels[x, y]
                if self.distance2(self.color_to_change, user_pixels[x, y]) < self.threshold ** 2:
                    r = int(r * 1.50)
                    g = int(g * .50)
                    b = int(b * .50)
                self.draw.point((x, y), (r, g, b))
        
        #display and save the new image
        new_color_image.show()
        new_color_image.save("new_image.png")
