"""draws images with guided effects"""
import random
from PIL import Image, ImageDraw
import saving as save



def draw_image_guided_wiggle(
    guide_array_x, guide_array_y, color_array, frame_num, wiggle, pixel_size, file_name
):
    """Draws an image with a guided wiggle effect."""
    img = Image.new("RGBA", (100, 100), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    for i in range(len(guide_array_x)):
        new_x = guide_array_x[i] + (random.randint(-wiggle, wiggle))
        new_y = guide_array_y[i] + (random.randint(-wiggle, wiggle))
        if new_x < 10:
            new_x += 10
        if new_x > 90:
            new_x -= 10
        if new_y < 10:
            new_y += 10
        if new_y > 90:
            new_y -= 10
        draw.rectangle(
            (new_x, new_y, new_x + pixel_size, new_y + pixel_size),
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
    pixel_size,
    file_name,
):
    """Draws an image with a guided explode effect."""
    img = Image.new("RGBA", (100, 100), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rectangle(
        (
            guide_array_x[0],
            guide_array_y[0],
            guide_array_x[0] + pixel_size,
            guide_array_y[0] + pixel_size,
        ),
        fill=(color_array[0], color_array[1], color_array[2], color_array[3]),
    )
    if frame_num > 0:
        high_wiggle = frame_num + wiggle
    else:
        high_wiggle = wiggle
    for i in range(len(guide_array_x)):
        if guide_array_x[i] < int_x and guide_array_y[i] < int_y:  # bottom left
            new_x = guide_array_x[i] - random.randint(wiggle, high_wiggle)
            new_y = guide_array_y[i] - random.randint(wiggle, high_wiggle)
        elif guide_array_x[i] < int_x and guide_array_y[i] > int_y:  # top left
            new_x = guide_array_x[i] - random.randint(wiggle, high_wiggle)
            new_y = guide_array_y[i] + random.randint(wiggle, high_wiggle)
        elif guide_array_x[i] > int_x and guide_array_y[i] > int_y:  # top right
            new_x = guide_array_x[i] + random.randint(wiggle, high_wiggle)
            new_y = guide_array_y[i] + random.randint(wiggle, high_wiggle)
        elif guide_array_x[i] > int_x and guide_array_y[i] < int_y:  # bottom right
            new_x = guide_array_x[i] + random.randint(wiggle, high_wiggle)
            new_y = guide_array_y[i] - random.randint(wiggle, high_wiggle)
        else:
            new_x = guide_array_x[i]
            new_y = guide_array_y[i]
        draw.rectangle(
            (new_x, new_y, new_x + pixel_size, new_y + pixel_size),
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
