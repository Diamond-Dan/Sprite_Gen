from flask import Flask, jsonify, Blueprint, request, abort
import random
import os
import sprite_micro_gen
app = Flask(__name__)
# Create a blueprint for the first static folder
images_blueprint = \
    Blueprint('images', __name__, static_folder='images',
              static_url_path='/images')
app.register_blueprint(images_blueprint)

# Create a blueprint for the second static folder
gifs_blueprint = \
    Blueprint('gifs', __name__, static_folder='gifs', static_url_path='/gifs')
app.register_blueprint(gifs_blueprint)


@app.route('/generate_random_images', methods=['POST'])
def generate_random_images():
    # Call the main function
    start_x = random.randint(40, 70)
    start_y = random.randint(40, 70)
    frames = random.randint(1, 10)
    seed = random.randint(0, 100)
    pixel_number = random.randint(100, 200)
    mode = random.choice(['1', '2', '3'])
    wiggle = random.randint(1, 5)
    xml = 'tie_fighter.oxs'
    pixel_size = random.randint(1, 5)
    file_name = "random_image"
    filename, filename_2, gif_loc_1, gif_loc_2 = \
        sprite_micro_gen.main(start_x, start_y, frames, seed, pixel_number,
                              mode, wiggle, xml, pixel_size,
                              file_name, server_mode=True)
    filename.pop(0)
    filename_2.pop(0)
    # Create URLs for each image file
    image_urls = {
        'gif_loc_1': 
        'http://localhost:5000/gifs/' + gif_loc_1.replace("\\", "/"),
        'gif_loc_2': 
        'http://localhost:5000/gifs/' + gif_loc_2.replace("\\", "/")
    }
    for i, name in enumerate(filename, start=1):
        image_urls[f'wiggle_{i}'] = \
            f'http://localhost:5000/images/{name}'.replace("\\", "/")
    for i, name in enumerate(filename_2, start=1):
        image_urls[f'explode_{i}'] = \
              f'http://localhost:5000/images/{name}'.replace("\\", "/")
  
    for name, url in image_urls.items():
        print(f'{name}: {url}')
    # Return the image URLs in the API response
    return jsonify(image_urls)


@app.route('/generate_images_criteria', methods=['POST'])
def generate_images_criteria():
    # get data
    data = request.get_json()

    start_x = data.get('start_x')
    start_y = data.get('start_y')
    frames = data.get('frames')
    seed = data.get('seed')
    pixel_number = data.get('pixel_number')
    mode = data.get('mode')
    wiggle = data.get('wiggle')
    xml = data.get('xml')
    pixel_size = data.get('pixel_size')
    file_name = data.get('file_name')

    # check values
    if not data:
        print("No data provided")
        abort(400, description="No data provided")
    
    keys = ['start_x', 'start_y', 'frames', 'seed', 
            'pixel_number', 'mode', 'wiggle', 'xml', 'pixel_size', 'file_name']

    if not all(key in data for key in keys):
        print("Missing data fields")
        abort(400, description="Missing data fields")

    if any(data[key] is None for key in keys):
        print("One or more fields have None values")
        abort(400, description="One or more fields have None values")   

    if start_x < 0 or start_x > 100:
        print("start_x must be between 0 and 100")
        abort(400, description="start_x must be between 0 and 100")
    if start_y < 0 or start_y > 100:
        print("start_y must be between 0 and 100")
        abort(400, description="start_y must be between 0 and 100")
    
    if frames < 1 or frames > 30:
        print("frames must be between 1 and 30")
        abort(400, description="frames must be between 1 and 30")

    if pixel_number < 100 or pixel_number > 500:
        print("pixel_number must be between 100 and 500")
        abort(400, description="pixel_number must be between 100 and 500")
    
    if mode not in ['1', '2', '3']:
        print("mode must be 1, 2 or 3")
        abort(400, description="mode must be 1, 2 or 3")
    
    if wiggle < 1 or wiggle > 10:
        print("wiggle must be between 1 and 10")
        abort(400, description="wiggle must be between 1 and 10")

    if pixel_size < 1 or pixel_size > 5:
        print("pixel_size must be between 1 and 5")
        abort(400, description="pixel_size must be between 1 and 5")
    curfile = os.path.dirname(os.path.realpath(__file__))
    print(curfile)
    if not os.path.isfile(curfile+'\\patterns\\'+xml):
        print("xml file does not exist")
        abort(400, description="xml file does not exist")

    if not file_name:
        abort(400, description="file_name cannot be empty")

    filename = []
    filename_2 = []
    filename, filename_2, gif_loc_1, gif_loc_2 = \
        sprite_micro_gen.main(start_x, start_y, frames, seed, pixel_number,
                              mode, wiggle, xml, pixel_size,
                              file_name, server_mode=True)

    # Create URLs for each image file
    image_urls = {
        'gif_loc_1': 
        'http://localhost:5000/gifs/' + gif_loc_1.replace("\\", "/"),
        'gif_loc_2': 
        'http://localhost:5000/gifs/' + gif_loc_2.replace("\\", "/")
    }
    filename.pop(0)
    filename_2.pop(0)
    for i, name in enumerate(filename, start=0):
        if name != "":
            image_urls[f'wiggle_{i}'] = \
                f'http://localhost:5000/images/{name}' .replace("\\", "//")
    for i, name in enumerate(filename_2, start=0):
        if name != "":
            image_urls[f'explode_{i}'] = \
                f'http://localhost:5000/images/{name}'.replace("\\", "//")

    for name, url in image_urls.items():
        print(f'{name}: {url}')
    # Return the image URLs in the API response
    return jsonify(image_urls)


if __name__ == '__main__':
    app.run(port=5000, debug=True)