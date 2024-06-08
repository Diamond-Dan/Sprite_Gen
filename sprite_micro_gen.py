"""Basic UI and main function for the sprite micro generator."""
import os
import sys
import draw_sprite_animations as dsa
import draw_initial as init_draw
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
    """Main function for the sprite micro generator."""
    int_x = start_x
    int_y = start_y
    filename = []
    filename_2 = []
    server_file_wiggle_name = []
    server_file_explode_name = []
    cur_file_loc = os.path.dirname(os.path.realpath(__file__))
    filecount = 0
    if mode == "1":
        guide_array_x, guide_array_y, color_array = init_draw.draw_random_image_intial(
            int_x, int_y, seed, pixel_number, file_name, pixel_size
        )
    elif mode == "2":
        guide_array_x, guide_array_y, color_array = init_draw.parse_xml(xml, file_name)
    elif mode == "3":
        guide_array_x, guide_array_y, color_array = init_draw.draw_planet(
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




if __name__ == "__main__":
    """Terminal interface for the sprite micro generator."""
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