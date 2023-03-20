from PIL import Image, ImageDraw, ImageFont

def generate_artt():
    print("Generating artt...")

    #initiate base image
    img_size = (480, 480)
    img_bg_color = (255, 255, 255)
    img = Image.new("RGB", (480, 480), "red")

    #draw lines
    draw = ImageDraw.Draw(img)

    for i in range(0, 480, 10):
        line_xy = (0, i, 480, i)
        line_color = (0, 0, 0)
        draw.line(line_xy, fill=line_color, width=5)

    for i in range(0, 480, 20):
        line_xy = (i, 0, i, 480)
        line_color = (255, 255, 255)
        draw.line(line_xy, fill=line_color, width=6)
    
    line_bn = (240, 0, 480, 480)
    line_color = (0, 0, 255)
    draw.line(line_bn, fill=line_color, width=15)

    line_bn = (240, 0, 0, 480)
    line_color = (0, 0, 255)
    draw.line(line_bn, fill=line_color, width=15)

    line_bn = (120, 240, 360, 240)
    line_color = (0, 0, 255)
    draw.line(line_bn, fill=line_color, width=15)

    myfont = ImageFont.truetype("arial.ttf", 60)
    draw.text((60, 360), "ANGELHACK", font=myfont, fill=(255, 255, 0))
    

    img.save("artt.png")
if __name__ == "__main__":
    generate_artt()    