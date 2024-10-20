# G-SaviourExtract
Tools for extracting the graphical assets of the G-Saviour PS2 game

![GSS_HI Cleaned up and blinged out in blender](https://reshax.com/uploads/monthly_2024_10/image.png.a2e20aeffaab69c24345e6e6d13c7bd0.png "GSS_HI, blender")

![JS01M01 up and blinged out a bit in blender](https://reshax.com/uploads/monthly_2024_10/image.png.29fe96589b20ef4d86b63c50b983f122.png "JS01M01, blender")

![SH01M01 viewed in Noesis](https://reshax.com/uploads/monthly_2024_10/image.png.fe9bfa98e9b64860abb07a949961dcef.png "SH01M01, noesis")


## What you'll need
- A copy of the G-Saviour PS2 game files, typically as an .ISO
- An unpacking tool like 7zip
- [QuickBMS by Luigi Auriemma](https://aluigi.altervista.org/quickbms.htm)
- [Noesis by Rich Whitehouse](https://richwhitehouse.com/index.php?content=inc_projects.php&showproject=91)
- These files

## Thanks
[Many thanks to the helpful members at the reshax forum for helping me get the scripts developed.](https://reshax.com/topic/1131-ps2-gundam-g-saviour-model-file-help/)

Special thanks to The_oldman, who drafted all the scripts, which I then modified.

## Process
1. Place the .bms scripts in your QuickBMS directory to make it easier to use.
2. Save the .py somewhere you will remember it.
3. Unpack the game .iso file somewhere easy to find.
4. Start by dragging the MD2NJ.bms script onto quickbms.exe
   1. Go to your unpacked game file directory, then into the DATA folder
   2. Type *.md for the input files
   3. Stay in your unpacked game file directory DATA folder
   4. Hit enter, and let it rip.
5. This will create a subfolder for every .md file in the game - this includes stages, maps, spaceships, cutscenes, and mecha.  The created .nj files can be read by Noesis natively, and include UV mapping and bone information.
6. Then drag the GSPextractAligned.bms script onto quickbms.exe
   1. Same folder as before
   2. Type *.gsp for the input files
   3. Stay in the DATA folder
   4. Hit enter, let it rip.
5. This will create a list of .gs files in named subfolders, many of which align with the .nj files.  They are named njtex000.gs, njtex001.gs, to follow the Noesis material autonaming convention.
6. Optionally, do the same with GS2BMPBaseFolder.bms - there are some single textures in the main DATA folder, but mostly for backgrounds.
7. Next, drag the GS2BMP.bms script to quickbms.exe.
   1. Pick one of the created subfolders.  Note - There are now over 300 folders with various information in it, so pick carefully! See Unit Decoder list below.
   2. Type *.gs for the input files.
   3. Stay in the subfolder.
   4. Hit enter, let it rip.
8. Open Noesis, go to a subfolder, and open up the .nj file.  With the proper .bmp names, it will automagically preview textures for the materials.
9. Export to .fbx to maintain the bone structure from the file.
   - Once I figure out animation conversion, .fbx will contain bones and animations.
11. Open Blender, clear out the scene, and import the .fbx model of your choice.
    - To ensure proper bone alignment, make sure Armature -> Automatic Bone Orientation is selected.
12. Save the Blender file in the same folder as your extracted .bmp files.
    - I typically name the blender file after the .md file, but you do you.
13. Go to the Scripting window and open the .py file.
14. Select all the objects with A, then run the script. Switch back to the Layout window.
15. Make sure you are in Material Preview mode to verify the material assignments, then save again.
16. Enjoy!

## Future Work

It would be nice to have QuickBMS recursively search through these folders for converting the .gs files to .bmp, instead of going folder by folder.

There are some .mt and .mtp files that are very similar to .njm animation files, and I've managed to make a couple actually animate in noesis like that, but I don't know why most of them don't work yet.  Research continues.

## Unit Decoder List
In general, the first two-three letters describe the unit in question; the rest typically indicate LOD.  

Typically the highest detail version will be <Prefix>01M01, like GSG01M01 or SHC01M01.  This model will often have the effect parts from shields, thrusters, etc attached as well.

Here's a list of ones I've sorted out so far:
- BG : Bugu
- BR : Briefing (mission briefings)
- BT : Bugu II
- EF : Effects
- EV : Game asset animated cutscenes (includes the main capital ship and end of level animations)
- FC : Face (talking heads)
- G2 : G3-Saviour
- G2B : G3-Saviour Ground Attack Mode
- G2I : G3-Saviour Intensive Attack Mode
- GS : G-Saviour Space
- GSG : G-Saviour Ground
- GSS_HI : G-Saviour Space High Detail (start screen)
- H* : specific effects for different units
   - HBG : Bugu
   - HG2 : G3-Saviour
   - etc
- JS : J-Saviour
- MP : Map elements
- MSSEL : the swirly rings around the MS Selection Screen
- RD : MS/MW Raid
- RV : Raven
- SH : Spear Head
- SHB : Spear Head Ballistic
- SHC : Spear Head Cannon
- SHN : Spear Head Normal
- TEST : some equipment base?
- TR : Turret

