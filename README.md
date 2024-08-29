Basic Sprite Generation and GIF Generation application for game development. Intended for easily creating prototypes for game engines that accept sprite sheets. 

Current version Alpha 0.02 8/20/24

Usage: 
Clone repository  
Run image_maker.py  
Find generated image in folder images and gifs in gifs  


Features: 
Draw an image in image_maker.py and hit enter to activate the menu options on the left side. Then click create images to draw the images and the gifs 
Commands:  
  
WHILE UNPASUSED:  
Click with the right mouse button or click and draw to draw
s key saves the xml with out generating  
g key removes the grid  
hit enter to pause the drawing  
crtl+z will undo the pixels drawn  
WHILE PAUSED:  
click the numbers on the right to change the RGB color palette  
click the size number to change the size of the paint brush  
WHILE PAUSED OR UNPAUSED  
e sets the sotware into erase mode  
b key changes the background color of the grid  

Known issues:  

If the correct folder structure is not created, it will not run.    
Likely not MAC compatible  
putting in a number that is too large for the RGB color will crash the program  

Images can be regenerated with out rerunning the program through either sprite_micro_gen.py using the text based interface  
  
OR  
  
Images can be generated through calls to the flask server in image_gen_api.py  
