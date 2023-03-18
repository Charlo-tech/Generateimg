from PIL import Image, ImageDraw, ImageFont

def generate_artt():
    print("Generating artt...")

    #initiate base image
    img_size = (180, 180)
    img_bg_color = (255, 255, 255)
    img = Image.new("RGB", (100, 100), "red")

    #draw lines
    draw = ImageDraw.Draw(img)

    for i in range(0, 100, 10):
        line_xy = (0, i, 100, i)
        line_color = (0, 0, 0)
        draw.line(line_xy, fill=line_color, width=5)
    
    img.save("artt.png")
if __name__ == "__main__":
    generate_artt()    