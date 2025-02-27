"""draws images with guided effects"""
import random
from PIL import Image, ImageDraw
import saving as save



def draw_image_guided_wiggle(
    guide_array_x, guide_array_y, color_array, frame_num, wiggle, guide_array_size, file_name
):
    """Draws an image with a guided wiggle effect."""
    img = Image.new("RGBA", (1000, 1000), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    for i in range(len(guide_array_x)):
        new_x = guide_array_x[i] + (random.randint(-wiggle, wiggle))
        new_y = guide_array_y[i] + (random.randint(-wiggle, wiggle))
        if new_x < 10:
            new_x += 10
        if new_x > 1000:
            new_x -= 10
        if new_y < 10:
            new_y += 10
        if new_y > 1000:
            new_y -= 10
        draw.rectangle(
            (new_x, new_y, new_x + guide_array_size[i], new_y + guide_array_size[i]),
            fill=(
                color_array[i * 4],
                color_array[i * 4 + 1],
                color_array[i * 4 + 2],
                color_array[i * 4 + 3],
            ),
        )
    file_name = file_name + "_wiggle"
    name, server_name = save.image_saver(img, file_name)
    return name, server_name


def draw_image_guided_explode(
    int_x,
    int_y,
    guide_array_x,
    guide_array_y,
    color_array,
    frame_num,
    wiggle,
    guide_array_size,
    file_name,
):
    """Draws an image with a guided explode effect."""
    bottom_left = 0
    top_left = 0
    top_right = 0
    bottom_right = 0
    other = 0
    img = Image.new("RGBA", (1000, 1000), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    if frame_num > 0:
        high_wiggle = frame_num*wiggle*5
    elif frame_num > 5:
        wiggle = wiggle*5
        high_wiggle = wiggle*frame_num
    else:
        high_wiggle = wiggle
    for i in range(len(guide_array_x)):
        if guide_array_x[i] < int_x and guide_array_y[i] < int_y:  # bottom left
            bottom_left = bottom_left+1
            new_x = guide_array_x[i] - random.randint(wiggle, high_wiggle)
            new_y = guide_array_y[i] - random.randint(wiggle, high_wiggle)
        elif guide_array_x[i] < int_x and guide_array_y[i] > int_y:  # top left
            top_left = top_left+1
            new_x = guide_array_x[i] - random.randint(wiggle, high_wiggle)
            new_y = guide_array_y[i] + random.randint(wiggle, high_wiggle)
        elif guide_array_x[i] > int_x and guide_array_y[i] > int_y:  # top right
            top_right = top_right+1
            new_x = guide_array_x[i] + random.randint(wiggle, high_wiggle)
            new_y = guide_array_y[i] + random.randint(wiggle, high_wiggle)
    
        elif guide_array_x[i] > int_x and guide_array_y[i] < int_y:  # bottom right
            bottom_right = bottom_right+1
            new_x = guide_array_x[i] + random.randint(wiggle, high_wiggle)
            new_y = guide_array_y[i] - random.randint(wiggle, high_wiggle)
        else:
            other = other+1
            new_x = guide_array_x[i] + random.randint(-wiggle, wiggle)
            new_y = guide_array_y[i] + random.randint(-wiggle, wiggle)

        draw.rectangle(
            (new_x, new_y, new_x + guide_array_size[i], new_y + guide_array_size[i]),
            fill=(
                color_array[i * 4],
                color_array[i * 4 + 1],
                color_array[i * 4 + 2],
                color_array[i * 4 + 3],
            ),
        )
        
    file_name = file_name + "_explode"
    name, server_name = save.image_saver(img, file_name)
    return name, server_name
