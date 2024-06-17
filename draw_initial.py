"""Creates initial images"""
import random
import math
import os
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw
import saving as save


def draw_random_image_intial(x, y, seed, pixel_number, file_name, pixel_size):
    array_x = [x]
    array_y = [y]
    new_x = x
    new_y = y
    img = Image.new("RGBA", (1000, 1000), color=(0, 0, 0, 0))
    random.seed(seed)
    draw = ImageDraw.Draw(img)
    lastrand = 0
    draw.rectangle((x, y, x + pixel_size, y + pixel_size), fill=(255, 0, 0, 255))
    i = 0
    random_color_1 = random.randint(0, 255)
    random_color_2 = random.randint(0, 255)
    random_color_3 = random.randint(0, 255)
    random_color_4 = random.randint(200, 255)
    random_color_array = [
        random_color_1,
        random_color_2,
        random_color_3,
        random_color_4,
    ]
    while i < pixel_number:
        random_number = random.randint(1, 4)
        random_color_1 += random.randint(-10, 10)
        random_color_2 += random.randint(-10, 10)
        random_color_3 += random.randint(-10, 10)
        random_color_4 += random.randint(-10, 10)
        random_color_array.append(random_color_1)
        random_color_array.append(random_color_2)
        random_color_array.append(random_color_3)
        random_color_array.append(random_color_4)
        if random_color_1 <= 0 or random_color_1 >= 255:
            random_color_1 = 255
        if random_color_2 <= 0 or random_color_2 >= 255:
            random_color_2 = 0
        if random_color_3 <= 0 or random_color_3 >= 255:
            random_color_3 = 0
        if random_color_4 <= 0 or random_color_4 >= 255:
            random_color_4 = 255

        if lastrand == 1 or lastrand == 2:
            random_number = random.randint(3, 4)
        elif lastrand == 3 or lastrand == 4:
            random_number = random.randint(1, 2)
        if random_number == 1:
            new_x += 5
        elif random_number == 2:
            new_x -= 5
        elif random_number == 3:
            new_y += 5
        elif random_number == 4:
            new_y -= 5
        lastrand = random_number

        array_x.append(new_x)
        array_y.append(new_y)

        if new_x < 10 or new_x > 90 or new_y < 10 or new_y > 90:
            new_x = x
            new_y = y

        draw.rectangle(
            (new_x, new_y, new_x + pixel_size, new_y + pixel_size),
            fill=(random_color_1, random_color_2, random_color_3, random_color_4),
        )
        i += 1

    save.image_saver(img, file_name)
    return array_x, array_y, random_color_array


def parse_xml(xml_file_name, file_name):
    # Parse the XML file
    x = []
    y = []
    current_file_path = os.path.dirname(os.path.realpath(__file__))

    file_name_loc = current_file_path + "\\patterns\\" + xml_file_name
    tree = ET.parse(file_name_loc)

    # Get the root element
    root = tree.getroot()
   
    color_array = []    # Find all 'partstitch' elements and print their 'x' and 'y' attributes
    for partstitch in root.iter():
        if (
            (partstitch.tag == "partstitch" or partstitch.tag == "stitch")
            and partstitch.get("x") != None
            and partstitch.get("y") != None
        ):
          
            x.append(int(partstitch.get("x")))
            y.append(int(partstitch.get("y")))
           
            color_array.append(int(partstitch.get("color_1")))
            color_array.append(int(partstitch.get("color_2")))
            color_array.append(int(partstitch.get("color_3")))
            color_array.append(255)
       
    return x, y, color_array


def draw_xml_image(x, y, file_name):
    img = Image.new("RGBA", (1000, 1000), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    for i in range(len(x)):
        draw.rectangle((x[i], y[i], x[i] + 5, y[i] + 5), fill=(255, 0, 0, 255))
    save.image_saver(img, file_name)


def draw_planet(x, y, seed, pixel_number, file_name, pixel_size):
    array_x = [x]
    array_y = [y]
    new_x = x
    new_y = y
    img = Image.new("RGBA", (1000, 1000), color=(0, 0, 0, 0))
    random.seed(seed)
    draw = ImageDraw.Draw(img)
    draw.rectangle((x, y, x + pixel_size, y + pixel_size), fill=(255, 0, 0, 255))
    random_color_array = []
    pixel_size = 1
    h = x
    k = x
    r = math.sqrt(100)

    # Generate points on the circle
    points = [
        (h + r * math.cos(t), k + r * math.sin(t))
        for t in [i * 0.01 for i in range(int(2 * math.pi / 0.01))]
    ]

    # Split into two lists
    array_x = [x for x, y in points]
    array_y = [y for x, y in points]
    for x in points:
        random_color_array.append(255)
        random_color_array.append(0)
        random_color_array.append(0)
        random_color_array.append(255)

    for i in range(len(array_x)):
        draw.rectangle(
            (array_x[i], array_y[i], array_x[i] + pixel_size, array_y[i] + pixel_size),
            fill=(255, 0, 0, 255),
        )
    # print(array_x,array_y)

    save.image_saver(img, file_name)
    return array_x, array_y, random_color_array