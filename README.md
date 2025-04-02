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


Lets look at some example usage   
![spritegen](https://github.com/user-attachments/assets/e11c5aad-6fdc-4e62-a567-c268044f0918)

The orginal generation from the painting canvas looks like this using the "exploding" animation  

![spaceship1 xmlexplodeseed_3pixel_1300frames_250](https://github.com/user-attachments/assets/b5363f69-f589-49b3-a927-e7938324b343)  


But we can regenerate that file a variety of ways, by changing where we start our explosion we can change where the pixels move, moving the start generation to x:1 y:1 results in:  


![splocexplodeseed_3pixel_1300frames_250](https://github.com/user-attachments/assets/2c5d4ca4-9b54-4b43-b328-44ee65a1b463)

We can also extend out the length of time the animation takes by adding many extra frames moving from 250 frames to 1000 frames this.  
This takes some time even on fast computer and likely shouldn't be done till improvements are implemented inthe way images are generated.  
I can't even upload the file due to the being over the github size limit.  

![image](https://github.com/user-attachments/assets/baaa6d2d-d344-4bd6-9c5a-8da95f01e552)





