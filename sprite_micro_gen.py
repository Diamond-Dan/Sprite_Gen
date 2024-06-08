import random
import math
import os
import sys
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw
import draw_sprite_animations as dsa
import saving as save

def main(
    start_x,
    start_y,
    frames,
    seed,
    pixel_number,
    mode,
    wiggle,
    xml,
    pixel_size,
    file_name,
    server_mode,
):
    int_x = start_x
    int_y = start_y
    filename = []
    filename_2 = []
    server_file_wiggle_name = []
    server_file_explode_name = []
    cur_file_loc = os.path.dirname(os.path.realpath(__file__))
    filecount = 0
    if mode == "1":
        guide_array_x, guide_array_y, color_array = draw_random_image_intial(
            int_x, int_y, seed, pixel_number, file_name, pixel_size
        )
    elif mode == "2":
        guide_array_x, guide_array_y, color_array = parse_xml(xml, file_name)
    elif mode == "3":
        guide_array_x, guide_array_y, color_array = draw_planet(
            int_x, int_y, seed, pixel_number, file_name, pixel_size
        )

    for i in range(frames):
        name, server_name = dsa.draw_image_guided_wiggle(
            guide_array_x, guide_array_y, color_array, i, wiggle, pixel_size, file_name
        )
        if server_name != "":
            filename.append(name)
            server_file_wiggle_name.append(server_name)
    for i in range(frames):
        name_2, server_name = dsa.draw_image_guided_explode(
            int_x,
            int_y,
            guide_array_x,
            guide_array_y,
            color_array,
            i,
            wiggle,
            pixel_size,
            file_name,
        )
        if server_name != "":
            filename_2.append(name_2)
        server_file_explode_name.append(server_name)
    gif_loc_1 = save.gif_maker(filename, cur_file_loc, seed, pixel_number, frames, filecount)
    gif_loc_2 = save.gif_maker(
        filename_2, cur_file_loc, seed, pixel_number, frames, filecount
    )
    if server_mode == True:
        return server_file_wiggle_name, server_file_explode_name, gif_loc_1, gif_loc_2



def draw_random_image_intial(x, y, seed, pixel_number, file_name, pixel_size):
    array_x = [x]
    array_y = [y]
    new_x = x
    new_y = y
    img = Image.new("RGBA", (100, 100), color=(0, 0, 0, 0))
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
    # generate colors
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
    # Find all 'partstitch' elements and print their 'x' and 'y' attributes
    for partstitch in root.iter():
        if (
            (partstitch.tag == "partstitch" or partstitch.tag == "stitch")
            and partstitch.get("x") != None
            and partstitch.get("y") != None
        ):
            # print(partstitch.get('x'), partstitch.get('y'))
            x.append(int(partstitch.get("x")))
            y.append(int(partstitch.get("y")))
            random_color_1 += random.randint(-1, 1)
            random_color_2 += random.randint(-1, 1)
            random_color_3 += random.randint(-1, 1)
            random_color_4 += random.randint(-1, 1)
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
    # print(f'x: {x}, y: {y}')
    return x, y, random_color_array


def draw_xml_image(x, y, file_name):
    img = Image.new("RGBA", (100, 100), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    for i in range(len(x)):
        draw.rectangle((x[i], y[i], x[i] + 5, y[i] + 5), fill=(255, 0, 0, 255))
    save.image_saver(img, file_name)


def draw_planet(x, y, seed, pixel_number, file_name, pixel_size):
    array_x = [x]
    array_y = [y]
    new_x = x
    new_y = y
    img = Image.new("RGBA", (100, 100), color=(0, 0, 0, 0))
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


if __name__ == "__main__":

    mode = "0"
    count = 25
    start_x = 50
    start_y = 50

    seed = 3
    pixel_number = 300
    wiggle = 1
    xml = "rockball.xml"
    pixel_size = 1
    file_name = "asteroid"
    server_mode = False
    while True:
        print(
            "Press 1 to run in random mode or 2 for xml mode,press 3 to draw a planet, 4 for drawing settings, 5 to set xml file"
        )
        print("Press e to exit")

        mode = input()
        if mode == "1":
            main(
                start_x,
                start_y,
                count,
                seed,
                pixel_number,
                mode,
                wiggle,
                xml,
                pixel_size,
                file_name,
                server_mode,
            )
        elif mode == "2":
            main(
                start_x,
                start_y,
                count,
                seed,
                pixel_number,
                mode,
                wiggle,
                xml,
                pixel_size,
                file_name,
                server_mode,
            )
        elif mode == "3":
            main(
                start_x,
                start_y,
                count,
                seed,
                pixel_number,
                mode,
                wiggle,
                xml,
                pixel_size,
                file_name,
                server_mode,
            )
        elif mode == "4":
            print("Enter the number of frames, current frames is " + str(count))
            count = int(input())
            print("Enter the seed, current seed is " + str(seed))
            seed = int(input())
            print(
                "Enter the number of pixels, current pixel number is "
                + str(pixel_number)
            )
            pixel_number = int(input())
            print("Enter the wiggle, current wiggle is " + str(wiggle))
            wiggle = int(input())
            print("Enter the pixel size, current pixel size is " + str(pixel_size))
            pixel_size = int(input())
            print("Enter the file name, current file name is " + str(file_name))
            file_name = input()
        elif mode == "5":
            print("Enter the xml file name with extension, likely .xml or .oxs")
            xml = input()
            current_file_path = os.path.dirname(os.path.realpath(__file__))
            if not os.path.isfile(current_file_path + "\\patterns\\" + xml):
                print(f"The file 'patterns/{xml}' does not exist.")

        elif mode == "e":
            sys.exit()
        else:
            print("Invalid input")