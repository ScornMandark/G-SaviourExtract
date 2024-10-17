# G-SaviourExtract
Tools for extracting the graphical assets of the G-Saviour PS2 game

## What you'll need
- A copy of the G-Saviour PS2 game files, typically as an .ISO
- An unpacking tool like 7zip
- [QuickBMS by Luigi Auriemma](https://aluigi.altervista.org/quickbms.htm)
- [Noesis by Rich Whitehouse](https://richwhitehouse.com/index.php?content=inc_projects.php&showproject=91)
- These files

## Thanks
Many thanks to the helpful members at the reshax forum for helping me get the scripts developed.

Special thanks to The_oldman, who drafted all the scripts, which I then modified.

## Process
1. Place the .bms scripts in your QuickBMS directory to make it easier to use.
2. Unpack the game .iso file somewhere easy to find.
3. Start by dragging the MD2NJ.bms script onto quickbms.exe
   1. Go to your unpacked game file directory, then into the DATA folder
   2. Type *.md for the input files
   3. Stay in your unpacked game file directory DATA folder
   4. Hit enter, and let it rip.
4. This will create a subfolder for every .md file in the game - this includes stages, maps, spaceships, cutscenes, and mecha.  The created .nj files can be read by Noesis natively, and include UV mapping and bone information.
5. Then drag the GSPextractAligned.bms script onto quickbms.exe
   1. Same folder as before
   2. Type *.gsp for the input files
   3. Stay in the DATA folder
   4. Hit enter, let it rip.
5. This will create a list of .gs files in named subfolders, many of which align with the .nj files.  They are named njtex000.gs, njtex001.gs, to follow the Noesis material autonaming convention.
6. Optionally, do the same with GS2BMPBaseFolder.bms - there are some single textures in the main DATA folder, but mostly for backgrounds.
7. Finally (for now), drag the GS2BMP.bms script to quickbms.exe.
   1. Pick one of the created subfolders.  Note - There are now over 300 folders with various information in it, so pick carefully! [^1]
   2. Type *.gs for the input files.
   3. Stay in the subfolder.
   4. Hit enter, let it rip.
8. Open Noesis, go to a subfolder, and open up the .nj file.  With the proper .bmp names, it will automagically assign textures to the materials.
9. Export as desired, and enjoy!

## Future Work
It would be really nice to have noesis export the textures as assigned to the materials, but I do not know how to make it do that yet.

It would also be nice to have noesis recursively search through these folders for converting the .gs files to .bmp, instead of going folder by folder.

There are some .mt and .mtp files that are very similar to .njm animation files, and I've managed to make a couple actually animate in noesis like that, but I don't know why most of them don't work yet.  Research continues.

## Unit Decoder
[^1]: In general, the first two-three letters describe the unit in question.  The rest often indicate LOD.  Typically the highest detail version will be <Prefix>01M01, like GSG01M01 or SHC01M01.  This model will often have the effect parts from shields, thrusters, etc attached as well.

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

