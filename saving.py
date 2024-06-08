"""contains functions for saving images and gifs."""
import os
import imageio.v2 as imageio

def gif_maker(filename, cur_file_loc, seed, pixel_number, frames, filecount):
    """Creates a gif from a list of images."""
    images = []

    for i in range(len(filename)):
        if filename[i] != "":
            images.append(imageio.imread(filename[i]))

    gif_name = (
        cur_file_loc
        + "\\gifs\\movie_"
        + "seed_"
        + str(seed)
        + "pixel_"
        + str(pixel_number)
        + "frames_"
        + str(frames)
        + str(filecount)
        + ".gif"
    )
    server_gif_name = (
        "movie_"
        + "seed_"
        + str(seed)
        + "pixel_"
        + str(pixel_number)
        + "frames_"
        + str(frames)
        + str(filecount)
        + ".gif"
    )
    while os.path.isfile(gif_name):
        filecount += 1
        gif_name = (
            cur_file_loc
            + "\\gifs\\movie_"
            + "seed_"
            + str(seed)
            + "pixel_"
            + str(pixel_number)
            + "frames_"
            + str(frames)
            + str(filecount)
            + ".gif"
        )

    imageio.mimsave(gif_name, images, "GIF", disposal=2, loop=0)

    while os.path.isfile(server_gif_name):
        filecount += 1
        server_gif_name = (
            "movie_"
            + "seed_"
            + str(seed)
            + "pixel_"
            + str(pixel_number)
            + "frames_"
            + str(frames)
            + str(filecount)
            + ".gif"
        )
    return server_gif_name


def image_saver(img, file_name):
    """Saves an image to the Images folder."""
    filecount = 0
    name = ""
    server_name = ""
    cur_file_loc = os.path.dirname(os.path.realpath(__file__))
    while os.path.isfile(
        cur_file_loc + "\\Images\\" + file_name + str(filecount) + ".png"
    ):
        filecount += 1
        name = cur_file_loc + "\\Images\\" + file_name + str(filecount) + ".png"
        server_name = file_name + str(filecount) + ".png"
        print(server_name)
    img.save(cur_file_loc + "\\Images\\" + file_name + str(filecount) + ".png")

    return name, server_name