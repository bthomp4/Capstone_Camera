# Capstone_Camera

## Project Goal
The goal of this project is to develop code that will operate the camera on the raspberry pi

## Project Tasks
1. Get the raspberry pi to record input through programming
   - C is the language of choice, however for the capstone demo Python should be acceptable
   - This can be done by having user input or just taking a single picture and exiting
   - The image can be saved to a file to be opened later
2. Get the raspberry pi to record input and display on the screen without saving the file
   - I'm guessing that a gui window will need to be created to display the image
   - Again c might be better in the long run but if python gets it working now that is fine too
3. Have the camera update the image approximatly once every second
   - Again no saving the file just display the image

## Additional Info
I was able to take pictues on the Raspberry Pi using the following command on terminal
```
raspistill -o <filename>
```
There are additional flags for the `raspistill` command and I do not believe that command will work in any programming language

There should be a library for using the camera in C or Python

