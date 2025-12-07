##########
#####
###
#
###### SAFE ZONE, REMAINS SAME ACROSS GAMES
# homescreen video
# ctc video(s)
###### Face Guide [replace mira w Sarka or Goran]
# - miraangry
###### Pose Guide 
# - miraposeleftneutral
###### Inserts 
# - mapinsertcompone
###### Scenes [var is in brackets]
# - sceneonebg (sceneonevar)
###### Animation Guide
# - acidfade_black
###### !!! Use variables, ike the django example below, to alter the FPS on the fly

# THIS is how you block things :) 
#image scenesixteenbg:
#    block:
#        "images/anibg/scenesixteen/scenesixteen00000.webp"
#        pause 0.1
#        "images/anibg/scenesixteen/scenesixteen00001.webp"
#        pause 0.1
#        "images/anibg/scenesixteen/scenesixteen00002.webp"
#        repeat (10)
#    block:
#        pause scenesixteenvar
#        "images/anibg/scenesixteen/scenesixteen00011.webp"
#        pause scenesixteenvar
#        "images/anibg/scenesixteen/scenesixteen00012.webp"
#        repeat

# THIS is custom variables :)
#image scenetenbg:
#    "images/anibg/sceneten/sceneten00000.webp"
#    pause scenetenvar
#    "images/anibg/sceneten/sceneten00001.webp"
#   pause scenetenvar
#    "images/anibg/sceneten/sceneten00002.webp"
#    pause scenetenvar
#    repeat

##########
#####
###
#
#
# HOMESCREEN / MAIN 
#
#
##
###
#####
##########


image blackplaceholder:
    "gui/blackbackground.png" 

image homescreen: 
    "images/dynamicbgs/homescreen/homescreen_00000.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00001.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00002.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00003.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00004.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00005.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00006.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00007.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00008.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00009.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00010.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00011.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00012.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00013.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00014.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00015.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00016.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00017.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00018.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00019.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00020.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00021.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00022.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00023.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00024.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00025.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00026.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00027.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00028.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00029.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00030.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00031.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00032.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00033.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00034.webp"
    pause 0.125
    "images/dynamicbgs/homescreen/homescreen_00035.webp"
    pause 0.125
    repeat 

##########
#####
###
#
#
# CTC
#
#
##
###
#####
##########


image ctcdialogue: 
    "images/ctc/ctcdialogue/ctcdialogue_00000.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00001.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00002.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00003.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00004.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00005.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00006.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00007.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00008.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00009.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00010.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00011.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00012.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00013.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00014.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00015.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00016.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00017.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00018.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00019.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00020.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00021.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00022.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00023.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00024.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00025.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00026.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00027.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00028.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00029.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00030.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00031.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00032.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00033.webp"
    pause 0.1
    "images/ctc/ctcdialogue/ctcdialogue_00034.webp"
    pause 0.1
    repeat

image ctcnarration: 
    "images/ctc/ctcnarration/ctcnarration_00000.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00001.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00002.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00003.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00004.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00005.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00006.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00007.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00008.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00009.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00010.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00011.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00012.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00013.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00014.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00015.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00016.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00017.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00018.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00019.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00020.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00021.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00022.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00023.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00024.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00025.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00026.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00027.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00028.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00029.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00030.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00031.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00032.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00033.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00034.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00035.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00036.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00037.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00038.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00039.webp"
    pause 0.1
    "images/ctc/ctcnarration/ctcnarration_00040.webp"
    pause 0.1
    repeat

image ctcwidescreen: 
    "images/ctc/ctcwidescreen/ctcwidescreen_00000.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00001.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00002.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00003.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00004.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00005.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00006.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00007.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00008.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00009.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00010.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00011.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00012.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00013.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00014.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00015.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00016.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00017.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00018.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00019.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00020.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00021.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00022.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00023.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00024.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00025.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00026.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00027.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00028.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00029.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00030.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00031.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00032.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00033.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00034.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00035.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00036.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00037.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00038.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00039.webp"
    pause 0.1
    "images/ctc/ctcwidescreen/ctcwidescreen_00040.webp"
    pause 0.1
    repeat

image ctcfourthree: 
    "images/ctc/ctcfourthree/ctcfourthree_00000.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00001.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00002.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00003.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00004.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00005.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00006.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00007.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00008.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00009.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00010.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00011.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00012.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00013.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00014.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00015.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00016.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00017.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00018.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00019.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00020.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00021.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00022.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00023.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00024.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00025.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00026.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00027.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00028.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00029.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00030.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00031.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00032.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00033.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00034.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00035.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00036.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00037.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00038.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00039.webp"
    pause 0.1
    "images/ctc/ctcfourthree/ctcfourthree_00040.webp"
    pause 0.1
    repeat

##########
#####
###
#
#
# UNDERLAYS AND FRAMES
#
#
##
###
#####
##########


image underlay: 
    "images/framesandunders/underlay/underlay_00000.png"
    pause underlayvar
    "images/framesandunders/underlay/underlay_00001.png"
    pause underlayvar
    "images/framesandunders/underlay/underlay_00002.png"
    pause underlayvar
    "images/framesandunders/underlay/underlay_00003.png"
    pause underlayvar
    "images/framesandunders/underlay/underlay_00004.png"
    pause underlayvar
    "images/framesandunders/underlay/underlay_00005.png"
    pause underlayvar
    "images/framesandunders/underlay/underlay_00006.png"
    pause underlayvar
    "images/framesandunders/underlay/underlay_00007.png"
    pause underlayvar
    "images/framesandunders/underlayend.png"
    pause underlayvar



image underlayb: 
    "images/framesandunders/underlayb/underlayb_00000.png"
    pause underlayvar
    "images/framesandunders/underlayb/underlayb_00001.png"
    pause underlayvar
    "images/framesandunders/underlayb/underlayb_00002.png"
    pause underlayvar
    "images/framesandunders/underlayb/underlayb_00003.png"
    pause underlayvar
    "images/framesandunders/underlayb/underlayb_00004.png"
    pause underlayvar
    "images/framesandunders/underlayb/underlayb_00005.png"
    pause underlayvar
    "images/framesandunders/underlayb/underlayb_00006.png"
    pause underlayvar
    "images/framesandunders/underlayb/underlayb_00007.png"
    pause underlayvar
    "images/framesandunders/underlaybend.png"
    pause underlayvar

image underlayc: 
    "images/framesandunders/underlayc/underlayc_00000.png"
    pause underlayvar
    "images/framesandunders/underlayc/underlayc_00001.png"
    pause underlayvar
    "images/framesandunders/underlayc/underlayc_00002.png"
    pause underlayvar
    "images/framesandunders/underlayc/underlayc_00003.png"
    pause underlayvar
    "images/framesandunders/underlayc/underlayc_00004.png"
    pause underlayvar
    "images/framesandunders/underlayc/underlayc_00005.png"
    pause underlayvar
    "images/framesandunders/underlayc/underlayc_00006.png"
    pause underlayvar
    "images/framesandunders/underlayc/underlayc_00007.png"
    pause underlayvar
    "images/framesandunders/underlaycend.png"
    pause underlayvar


image underlayd: 
    "images/framesandunders/underlayd/underlayd_00000.png"
    pause underlayvar
    "images/framesandunders/underlayd/underlayd_00001.png"
    pause underlayvar
    "images/framesandunders/underlayd/underlayd_00002.png"
    pause underlayvar
    "images/framesandunders/underlayd/underlayd_00003.png"
    pause underlayvar
    "images/framesandunders/underlayd/underlayd_00004.png"
    pause underlayvar
    "images/framesandunders/underlayd/underlayd_00005.png"
    pause underlayvar
    "images/framesandunders/underlayd/underlayd_00006.png"
    pause underlayvar
    "images/framesandunders/underlayd/underlayd_00007.png"
    pause underlayvar
    "images/framesandunders/underlaydend.png"
    pause underlayvar


image widetoultra: 
    "images/framesandunders/widetoultra/widetoultra_00000.png"
    pause aspectshift
    "images/framesandunders/widetoultra/widetoultra_00001.png"
    pause aspectshift
    "images/framesandunders/widetoultra/widetoultra_00002.png"
    pause aspectshift
    "images/framesandunders/widetoultra/widetoultra_00003.png"
    pause aspectshift
    "images/framesandunders/widetoultra/widetoultra_00004.png"
    pause aspectshift
    "images/framesandunders/widetoultra/widetoultra_00005.png"
    pause aspectshift
    "images/framesandunders/widetoultra/widetoultra_00006.png"
    pause aspectshift
    "images/framesandunders/widetoultra/widetoultra_00007.png"
    pause aspectshift
    "images/framesandunders/widetoultra/widetoultra_00008.png"
    pause aspectshift
    "images/framesandunders/widetoultra/widetoultra_00009.png"
    pause aspectshift
    "images/framesandunders/widetoultra/widetoultra_00010.png"
    pause aspectshift
    "images/framesandunders/widetoultra/widetoultra_00011.png"
    pause aspectshift
    "images/framesandunders/widetoultra/widetoultra_00012.png"
    pause aspectshift
    "images/framesandunders/widetoultra/widetoultra_00013.png"
    pause aspectshift
    "images/framesandunders/widetoultra/widetoultra_00014.png"
    pause aspectshift
    "images/framesandunders/widetoultra/widetoultra_00015.png"
    pause aspectshift
    "images/framesandunders/widetoultra/widetoultra_00016.png"
    pause aspectshift
    "images/framesandunders/widetoultra/widetoultra_00017.png"
    pause aspectshift
    "images/framesandunders/widetoultra/widetoultra_00018.png"
    pause aspectshift
    "images/framesandunders/widetoultra/widetoultra_00019.png"
    pause aspectshift
    "images/framesandunders/widetoultra/widetoultra_00020.png"
    pause aspectshift
    "images/framesandunders/widetoultra/widetoultra_00021.png"
    pause aspectshift
    "images/framesandunders/widetoultra/widetoultra_00022.png"
    pause aspectshift
    "images/framesandunders/widetoultra/widetoultra_00023.png"
    pause aspectshift
    "images/framesandunders/widetoultra/widetoultra_00024.png"
    pause aspectshift
    "images/framesandunders/widetoultra/widetoultra_00025.png"
    pause aspectshift
    "images/framesandunders/widetoultra/widetoultra_00026.png"
    pause aspectshift
    "images/framesandunders/widetoultra/widetoultra_00027.png"
    pause aspectshift
    "images/framesandunders/widetoultra/widetoultra_00028.png"
    pause aspectshift


image ultratowide: 
    "images/framesandunders/ultratowide/ultratowide_00000.png"
    pause aspectshift
    "images/framesandunders/ultratowide/ultratowide_00001.png"
    pause aspectshift
    "images/framesandunders/ultratowide/ultratowide_00002.png"
    pause aspectshift
    "images/framesandunders/ultratowide/ultratowide_00003.png"
    pause aspectshift
    "images/framesandunders/ultratowide/ultratowide_00004.png"
    pause aspectshift
    "images/framesandunders/ultratowide/ultratowide_00005.png"
    pause aspectshift
    "images/framesandunders/ultratowide/ultratowide_00006.png"
    pause aspectshift
    "images/framesandunders/ultratowide/ultratowide_00007.png"
    pause aspectshift
    "images/framesandunders/ultratowide/ultratowide_00008.png"
    pause aspectshift
    "images/framesandunders/ultratowide/ultratowide_00009.png"
    pause aspectshift
    "images/framesandunders/ultratowide/ultratowide_00010.png"
    pause aspectshift
    "images/framesandunders/ultratowide/ultratowide_00011.png"
    pause aspectshift
    "images/framesandunders/ultratowide/ultratowide_00012.png"
    pause aspectshift
    "images/framesandunders/ultratowide/ultratowide_00013.png"
    pause aspectshift
    "images/framesandunders/ultratowide/ultratowide_00014.png"
    pause aspectshift
    "images/framesandunders/ultratowide/ultratowide_00015.png"
    pause aspectshift
    "images/framesandunders/ultratowide/ultratowide_00016.png"
    pause aspectshift
    "images/framesandunders/ultratowide/ultratowide_00017.png"
    pause aspectshift
    "images/framesandunders/ultratowide/ultratowide_00018.png"
    pause aspectshift
    "images/framesandunders/ultratowide/ultratowide_00019.png"
    pause aspectshift
    "images/framesandunders/ultratowide/ultratowide_00020.png"
    pause aspectshift
    "images/framesandunders/ultratowide/ultratowide_00021.png"
    pause aspectshift
    "images/framesandunders/ultratowide/ultratowide_00022.png"
    pause aspectshift
    "images/framesandunders/ultratowide/ultratowide_00023.png"
    pause aspectshift
    "images/framesandunders/ultratowide/ultratowide_00024.png"
    pause aspectshift
    "images/framesandunders/ultratowide/ultratowide_00025.png"
    pause aspectshift
    "images/framesandunders/ultratowide/ultratowide_00026.png"
    pause aspectshift
    "images/framesandunders/ultratowide/ultratowide_00027.png"
    pause aspectshift
    "images/framesandunders/ultratowide/ultratowide_00028.png"
    pause aspectshift


image standtoultra: 
    "images/framesandunders/standtoultra/standtoultra_00000.png"
    pause aspectshift
    "images/framesandunders/standtoultra/standtoultra_00001.png"
    pause aspectshift
    "images/framesandunders/standtoultra/standtoultra_00002.png"
    pause aspectshift
    "images/framesandunders/standtoultra/standtoultra_00003.png"
    pause aspectshift
    "images/framesandunders/standtoultra/standtoultra_00004.png"
    pause aspectshift
    "images/framesandunders/standtoultra/standtoultra_00005.png"
    pause aspectshift
    "images/framesandunders/standtoultra/standtoultra_00006.png"
    pause aspectshift
    "images/framesandunders/standtoultra/standtoultra_00007.png"
    pause aspectshift
    "images/framesandunders/standtoultra/standtoultra_00008.png"
    pause aspectshift
    "images/framesandunders/standtoultra/standtoultra_00009.png"
    pause aspectshift
    "images/framesandunders/standtoultra/standtoultra_00010.png"
    pause aspectshift
    "images/framesandunders/standtoultra/standtoultra_00011.png"
    pause aspectshift
    "images/framesandunders/standtoultra/standtoultra_00012.png"
    pause aspectshift
    "images/framesandunders/standtoultra/standtoultra_00013.png"
    pause aspectshift
    "images/framesandunders/standtoultra/standtoultra_00014.png"
    pause aspectshift
    "images/framesandunders/standtoultra/standtoultra_00015.png"
    pause aspectshift
    "images/framesandunders/standtoultra/standtoultra_00016.png"
    pause aspectshift
    "images/framesandunders/standtoultra/standtoultra_00017.png"
    pause aspectshift
    "images/framesandunders/standtoultra/standtoultra_00018.png"
    pause aspectshift
    "images/framesandunders/standtoultra/standtoultra_00019.png"
    pause aspectshift
    "images/framesandunders/standtoultra/standtoultra_00020.png"
    pause aspectshift
    "images/framesandunders/standtoultra/standtoultra_00021.png"
    pause aspectshift
    "images/framesandunders/standtoultra/standtoultra_00022.png"
    pause aspectshift
    "images/framesandunders/standtoultra/standtoultra_00023.png"
    pause aspectshift
    "images/framesandunders/standtoultra/standtoultra_00024.png"
    pause aspectshift
    "images/framesandunders/standtoultra/standtoultra_00025.png"
    pause aspectshift
    "images/framesandunders/standtoultra/standtoultra_00026.png"
    pause aspectshift
    "images/framesandunders/standtoultra/standtoultra_00027.png"
    pause aspectshift
    "images/framesandunders/standtoultra/standtoultra_00028.png"
    pause aspectshift

image ultratostand: 
    "images/framesandunders/ultratostand/ultratostand_00000.png"
    pause aspectshift
    "images/framesandunders/ultratostand/ultratostand_00001.png"
    pause aspectshift
    "images/framesandunders/ultratostand/ultratostand_00002.png"
    pause aspectshift
    "images/framesandunders/ultratostand/ultratostand_00003.png"
    pause aspectshift
    "images/framesandunders/ultratostand/ultratostand_00004.png"
    pause aspectshift
    "images/framesandunders/ultratostand/ultratostand_00005.png"
    pause aspectshift
    "images/framesandunders/ultratostand/ultratostand_00006.png"
    pause aspectshift
    "images/framesandunders/ultratostand/ultratostand_00007.png"
    pause aspectshift
    "images/framesandunders/ultratostand/ultratostand_00008.png"
    pause aspectshift
    "images/framesandunders/ultratostand/ultratostand_00009.png"
    pause aspectshift
    "images/framesandunders/ultratostand/ultratostand_00010.png"
    pause aspectshift
    "images/framesandunders/ultratostand/ultratostand_00011.png"
    pause aspectshift
    "images/framesandunders/ultratostand/ultratostand_00012.png"
    pause aspectshift
    "images/framesandunders/ultratostand/ultratostand_00013.png"
    pause aspectshift
    "images/framesandunders/ultratostand/ultratostand_00014.png"
    pause aspectshift
    "images/framesandunders/ultratostand/ultratostand_00015.png"
    pause aspectshift
    "images/framesandunders/ultratostand/ultratostand_00016.png"
    pause aspectshift
    "images/framesandunders/ultratostand/ultratostand_00017.png"
    pause aspectshift
    "images/framesandunders/ultratostand/ultratostand_00018.png"
    pause aspectshift
    "images/framesandunders/ultratostand/ultratostand_00019.png"
    pause aspectshift
    "images/framesandunders/ultratostand/ultratostand_00020.png"
    pause aspectshift
    "images/framesandunders/ultratostand/ultratostand_00021.png"
    pause aspectshift
    "images/framesandunders/ultratostand/ultratostand_00022.png"
    pause aspectshift
    "images/framesandunders/ultratostand/ultratostand_00023.png"
    pause aspectshift
    "images/framesandunders/ultratostand/ultratostand_00024.png"
    pause aspectshift
    "images/framesandunders/ultratostand/ultratostand_00025.png"
    pause aspectshift
    "images/framesandunders/ultratostand/ultratostand_00026.png"
    pause aspectshift
    "images/framesandunders/ultratostand/ultratostand_00027.png"
    pause aspectshift
    "images/framesandunders/ultratostand/ultratostand_00028.png"
    pause aspectshift


image widetostand: 
    "images/framesandunders/widetostand/widetostand_00000.png"
    pause aspectshift
    "images/framesandunders/widetostand/widetostand_00001.png"
    pause aspectshift
    "images/framesandunders/widetostand/widetostand_00002.png"
    pause aspectshift
    "images/framesandunders/widetostand/widetostand_00003.png"
    pause aspectshift
    "images/framesandunders/widetostand/widetostand_00004.png"
    pause aspectshift
    "images/framesandunders/widetostand/widetostand_00005.png"
    pause aspectshift
    "images/framesandunders/widetostand/widetostand_00006.png"
    pause aspectshift
    "images/framesandunders/widetostand/widetostand_00007.png"
    pause aspectshift
    "images/framesandunders/widetostand/widetostand_00008.png"
    pause aspectshift
    "images/framesandunders/widetostand/widetostand_00009.png"
    pause aspectshift
    "images/framesandunders/widetostand/widetostand_00010.png"
    pause aspectshift
    "images/framesandunders/widetostand/widetostand_00011.png"
    pause aspectshift
    "images/framesandunders/widetostand/widetostand_00012.png"
    pause aspectshift
    "images/framesandunders/widetostand/widetostand_00013.png"
    pause aspectshift
    "images/framesandunders/widetostand/widetostand_00014.png"
    pause aspectshift
    "images/framesandunders/widetostand/widetostand_00015.png"
    pause aspectshift
    "images/framesandunders/widetostand/widetostand_00016.png"
    pause aspectshift
    "images/framesandunders/widetostand/widetostand_00017.png"
    pause aspectshift
    "images/framesandunders/widetostand/widetostand_00018.png"
    pause aspectshift
    "images/framesandunders/widetostand/widetostand_00019.png"
    pause aspectshift
    "images/framesandunders/widetostand/widetostand_00020.png"
    pause aspectshift
    "images/framesandunders/widetostand/widetostand_00021.png"
    pause aspectshift
    "images/framesandunders/widetostand/widetostand_00022.png"
    pause aspectshift
    "images/framesandunders/widetostand/widetostand_00023.png"
    pause aspectshift
    "images/framesandunders/widetostand/widetostand_00024.png"
    pause aspectshift
    "images/framesandunders/widetostand/widetostand_00025.png"
    pause aspectshift
    "images/framesandunders/widetostand/widetostand_00026.png"
    pause aspectshift
    "images/framesandunders/widetostand/widetostand_00027.png"
    pause aspectshift
    "images/framesandunders/widetostand/widetostand_00028.png"
    pause aspectshift

image standtowide: 
    "images/framesandunders/standtowide/standtowide_00000.png"
    pause aspectshift
    "images/framesandunders/standtowide/standtowide_00001.png"
    pause aspectshift
    "images/framesandunders/standtowide/standtowide_00002.png"
    pause aspectshift
    "images/framesandunders/standtowide/standtowide_00003.png"
    pause aspectshift
    "images/framesandunders/standtowide/standtowide_00004.png"
    pause aspectshift
    "images/framesandunders/standtowide/standtowide_00005.png"
    pause aspectshift
    "images/framesandunders/standtowide/standtowide_00006.png"
    pause aspectshift
    "images/framesandunders/standtowide/standtowide_00007.png"
    pause aspectshift
    "images/framesandunders/standtowide/standtowide_00008.png"
    pause aspectshift
    "images/framesandunders/standtowide/standtowide_00009.png"
    pause aspectshift
    "images/framesandunders/standtowide/standtowide_00010.png"
    pause aspectshift
    "images/framesandunders/standtowide/standtowide_00011.png"
    pause aspectshift
    "images/framesandunders/standtowide/standtowide_00012.png"
    pause aspectshift
    "images/framesandunders/standtowide/standtowide_00013.png"
    pause aspectshift
    "images/framesandunders/standtowide/standtowide_00014.png"
    pause aspectshift
    "images/framesandunders/standtowide/standtowide_00015.png"
    pause aspectshift
    "images/framesandunders/standtowide/standtowide_00016.png"
    pause aspectshift
    "images/framesandunders/standtowide/standtowide_00017.png"
    pause aspectshift
    "images/framesandunders/standtowide/standtowide_00018.png"
    pause aspectshift
    "images/framesandunders/standtowide/standtowide_00019.png"
    pause aspectshift
    "images/framesandunders/standtowide/standtowide_00020.png"
    pause aspectshift
    "images/framesandunders/standtowide/standtowide_00021.png"
    pause aspectshift
    "images/framesandunders/standtowide/standtowide_00022.png"
    pause aspectshift
    "images/framesandunders/standtowide/standtowide_00023.png"
    pause aspectshift
    "images/framesandunders/standtowide/standtowide_00024.png"
    pause aspectshift
    "images/framesandunders/standtowide/standtowide_00025.png"
    pause aspectshift
    "images/framesandunders/standtowide/standtowide_00026.png"
    pause aspectshift
    "images/framesandunders/standtowide/standtowide_00027.png"
    pause aspectshift
    "images/framesandunders/standtowide/standtowide_00028.png"
    pause aspectshift

##########
#####
###
#
#
# FX / MAJOR FX 
#
#
##
###
#####
##########

image specialsicknessfx: 
    "images/fx/specialsicknessfx/specialsicknessfx_00000.webp"
    pause fxvar
    "images/fx/specialsicknessfx/specialsicknessfx_00001.webp"
    pause fxvar
    "images/fx/specialsicknessfx/specialsicknessfx_00002.webp"
    pause fxvar
    "images/fx/specialsicknessfx/specialsicknessfx_00003.webp"
    pause fxvar
    "images/fx/specialsicknessfx/specialsicknessfx_00004.webp"
    pause fxvar
    "images/fx/specialsicknessfx/specialsicknessfx_00005.webp"
    pause fxvar
    "images/fx/specialsicknessfx/specialsicknessfx_00006.webp"
    pause fxvar
    "images/fx/specialsicknessfx/specialsicknessfx_00007.webp"
    pause fxvar
    "images/fx/specialsicknessfx/specialsicknessfx_00008.webp"
    pause fxvar
    "images/fx/specialsicknessfx/specialsicknessfx_00009.webp"
    pause fxvar
    "images/fx/specialsicknessfx/specialsicknessfx_00010.webp"
    pause fxvar
    "images/fx/specialsicknessfx/specialsicknessfx_00011.webp"
    pause fxvar
    "images/fx/specialsicknessfx/specialsicknessfx_00012.webp"
    pause fxvar
    "images/fx/specialsicknessfx/specialsicknessfx_00013.webp"
    pause fxvar
    "images/fx/specialsicknessfx/specialsicknessfx_00014.webp"
    pause fxvar
    "images/fx/specialsicknessfx/specialsicknessfx_00015.webp"
    pause fxvar
    "images/fx/specialsicknessfx/specialsicknessfx_00016.webp"
    pause fxvar
    "images/fx/specialsicknessfx/specialsicknessfx_00017.webp"
    pause fxvar
    "images/fx/specialsicknessfx/specialsicknessfx_00018.webp"
    pause fxvar
    "images/fx/specialsicknessfx/specialsicknessfx_00019.webp"
    pause fxvar
    "images/fx/specialsicknessfx/specialsicknessfx_00020.webp"
    pause fxvar
    "images/fx/specialsicknessfx/specialsicknessfx_00021.webp"
    pause fxvar
    "images/fx/specialsicknessfx/specialsicknessfx_00022.webp"
    pause fxvar
    "images/fx/specialsicknessfx/specialsicknessfx_00023.webp"
    pause fxvar
    "images/fx/specialsicknessfx/specialsicknessfx_00024.webp"
    pause fxvar
    "images/fx/specialsicknessfx/specialsicknessfx_00025.webp"
    pause fxvar
    "images/fx/specialsicknessfx/specialsicknessfx_00026.webp"
    pause fxvar
    "images/fx/specialsicknessfx/specialsicknessfx_00027.webp"
    pause fxvar
    "images/fx/specialsicknessfx/specialsicknessfx_00028.webp"
    pause fxvar
    repeat


image specialintrospectfx: 
    "images/fx/specialintrospectfx/specialintrospectfx_00000.webp"
    pause fxvar
    "images/fx/specialintrospectfx/specialintrospectfx_00001.webp"
    pause fxvar
    "images/fx/specialintrospectfx/specialintrospectfx_00002.webp"
    pause fxvar
    "images/fx/specialintrospectfx/specialintrospectfx_00003.webp"
    pause fxvar
    "images/fx/specialintrospectfx/specialintrospectfx_00004.webp"
    pause fxvar
    "images/fx/specialintrospectfx/specialintrospectfx_00005.webp"
    pause fxvar
    "images/fx/specialintrospectfx/specialintrospectfx_00006.webp"
    pause fxvar
    "images/fx/specialintrospectfx/specialintrospectfx_00007.webp"
    pause fxvar
    "images/fx/specialintrospectfx/specialintrospectfx_00008.webp"
    pause fxvar
    "images/fx/specialintrospectfx/specialintrospectfx_00009.webp"
    pause fxvar
    "images/fx/specialintrospectfx/specialintrospectfx_00010.webp"
    pause fxvar
    "images/fx/specialintrospectfx/specialintrospectfx_00011.webp"
    pause fxvar
    "images/fx/specialintrospectfx/specialintrospectfx_00012.webp"
    pause fxvar
    "images/fx/specialintrospectfx/specialintrospectfx_00013.webp"
    pause fxvar
    "images/fx/specialintrospectfx/specialintrospectfx_00014.webp"
    pause fxvar
    "images/fx/specialintrospectfx/specialintrospectfx_00015.webp"
    pause fxvar
    "images/fx/specialintrospectfx/specialintrospectfx_00016.webp"
    pause fxvar
    "images/fx/specialintrospectfx/specialintrospectfx_00017.webp"
    pause fxvar
    "images/fx/specialintrospectfx/specialintrospectfx_00018.webp"
    pause fxvar
    "images/fx/specialintrospectfx/specialintrospectfx_00019.webp"
    pause fxvar
    "images/fx/specialintrospectfx/specialintrospectfx_00020.webp"
    pause fxvar
    "images/fx/specialintrospectfx/specialintrospectfx_00021.webp"
    pause fxvar
    "images/fx/specialintrospectfx/specialintrospectfx_00022.webp"
    pause fxvar
    "images/fx/specialintrospectfx/specialintrospectfx_00023.webp"
    pause fxvar
    "images/fx/specialintrospectfx/specialintrospectfx_00024.webp"
    pause fxvar
    "images/fx/specialintrospectfx/specialintrospectfx_00025.webp"
    pause fxvar
    "images/fx/specialintrospectfx/specialintrospectfx_00026.webp"
    pause fxvar
    "images/fx/specialintrospectfx/specialintrospectfx_00027.webp"
    pause fxvar
    "images/fx/specialintrospectfx/specialintrospectfx_00028.webp"
    pause fxvar
    "images/fx/specialintrospectfx/specialintrospectfx_00029.webp"
    pause fxvar
    repeat

image speciallovefx: 
    "images/fx/speciallovefx/speciallovefx_00000.webp"
    pause fxvar
    "images/fx/speciallovefx/speciallovefx_00001.webp"
    pause fxvar
    "images/fx/speciallovefx/speciallovefx_00002.webp"
    pause fxvar
    "images/fx/speciallovefx/speciallovefx_00003.webp"
    pause fxvar
    "images/fx/speciallovefx/speciallovefx_00004.webp"
    pause fxvar
    "images/fx/speciallovefx/speciallovefx_00005.webp"
    pause fxvar
    "images/fx/speciallovefx/speciallovefx_00006.webp"
    pause fxvar
    "images/fx/speciallovefx/speciallovefx_00007.webp"
    pause fxvar
    "images/fx/speciallovefx/speciallovefx_00008.webp"
    pause fxvar
    "images/fx/speciallovefx/speciallovefx_00009.webp"
    pause fxvar
    "images/fx/speciallovefx/speciallovefx_00010.webp"
    pause fxvar
    "images/fx/speciallovefx/speciallovefx_00011.webp"
    pause fxvar
    "images/fx/speciallovefx/speciallovefx_00012.webp"
    pause fxvar
    "images/fx/speciallovefx/speciallovefx_00013.webp"
    pause fxvar
    "images/fx/speciallovefx/speciallovefx_00014.webp"
    pause fxvar
    "images/fx/speciallovefx/speciallovefx_00015.webp"
    pause fxvar
    "images/fx/speciallovefx/speciallovefx_00016.webp"
    pause fxvar
    "images/fx/speciallovefx/speciallovefx_00017.webp"
    pause fxvar
    "images/fx/speciallovefx/speciallovefx_00018.webp"
    pause fxvar
    "images/fx/speciallovefx/speciallovefx_00019.webp"
    pause fxvar
    "images/fx/speciallovefx/speciallovefx_00020.webp"
    pause fxvar
    "images/fx/speciallovefx/speciallovefx_00021.webp"
    pause fxvar
    "images/fx/speciallovefx/speciallovefx_00022.webp"
    pause fxvar
    "images/fx/speciallovefx/speciallovefx_00023.webp"
    pause fxvar
    "images/fx/speciallovefx/speciallovefx_00024.webp"
    pause fxvar
    "images/fx/speciallovefx/speciallovefx_00025.webp"
    pause fxvar
    "images/fx/speciallovefx/speciallovefx_00026.webp"
    pause fxvar
    "images/fx/speciallovefx/speciallovefx_00027.webp"
    pause fxvar
    "images/fx/speciallovefx/speciallovefx_00028.webp"
    pause fxvar
    "images/fx/speciallovefx/speciallovefx_00029.webp"
    pause fxvar
    repeat


image violencefx: 
    "images/fx/violencefx/violencefx_00000.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00001.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00002.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00003.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00004.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00005.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00006.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00007.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00008.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00009.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00010.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00011.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00012.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00013.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00014.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00015.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00016.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00017.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00018.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00019.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00020.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00021.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00022.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00023.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00024.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00025.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00026.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00027.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00028.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00029.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00030.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00031.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00032.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00033.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00034.webp"
    pause fxvar
    "images/fx/violencefx/violencefx_00035.webp"
    pause fxvar
    repeat



image tensionfx: 
    "images/fx/tensionfx/tensionfx_00000.webp"
    pause fxvar
    "images/fx/tensionfx/tensionfx_00001.webp"
    pause fxvar
    "images/fx/tensionfx/tensionfx_00002.webp"
    pause fxvar
    "images/fx/tensionfx/tensionfx_00003.webp"
    pause fxvar
    "images/fx/tensionfx/tensionfx_00004.webp"
    pause fxvar
    "images/fx/tensionfx/tensionfx_00005.webp"
    pause fxvar
    "images/fx/tensionfx/tensionfx_00006.webp"
    pause fxvar
    "images/fx/tensionfx/tensionfx_00007.webp"
    pause fxvar
    "images/fx/tensionfx/tensionfx_00008.webp"
    pause fxvar
    "images/fx/tensionfx/tensionfx_00009.webp"
    pause fxvar
    "images/fx/tensionfx/tensionfx_00010.webp"
    pause fxvar
    "images/fx/tensionfx/tensionfx_00011.webp"
    pause fxvar
    "images/fx/tensionfx/tensionfx_00012.webp"
    pause fxvar
    "images/fx/tensionfx/tensionfx_00013.webp"
    pause fxvar
    "images/fx/tensionfx/tensionfx_00014.webp"
    pause fxvar
    "images/fx/tensionfx/tensionfx_00015.webp"
    pause fxvar
    "images/fx/tensionfx/tensionfx_00016.webp"
    pause fxvar
    "images/fx/tensionfx/tensionfx_00017.webp"
    pause fxvar
    "images/fx/tensionfx/tensionfx_00018.webp"
    pause fxvar
    "images/fx/tensionfx/tensionfx_00019.webp"
    pause fxvar
    "images/fx/tensionfx/tensionfx_00020.webp"
    pause fxvar
    "images/fx/tensionfx/tensionfx_00021.webp"
    pause fxvar
    "images/fx/tensionfx/tensionfx_00022.webp"
    pause fxvar
    "images/fx/tensionfx/tensionfx_00023.webp"
    pause fxvar
    "images/fx/tensionfx/tensionfx_00024.webp"
    pause fxvar
    "images/fx/tensionfx/tensionfx_00025.webp"
    pause fxvar
    "images/fx/tensionfx/tensionfx_00026.webp"
    pause fxvar
    "images/fx/tensionfx/tensionfx_00027.webp"
    pause fxvar
    "images/fx/tensionfx/tensionfx_00028.webp"
    pause fxvar
    repeat


image lovefx: 
    "images/fx/lovefx/lovefx_00000.webp"
    pause fxvar
    "images/fx/lovefx/lovefx_00001.webp"
    pause fxvar
    "images/fx/lovefx/lovefx_00002.webp"
    pause fxvar
    "images/fx/lovefx/lovefx_00003.webp"
    pause fxvar
    "images/fx/lovefx/lovefx_00004.webp"
    pause fxvar
    "images/fx/lovefx/lovefx_00005.webp"
    pause fxvar
    "images/fx/lovefx/lovefx_00006.webp"
    pause fxvar
    "images/fx/lovefx/lovefx_00007.webp"
    pause fxvar
    "images/fx/lovefx/lovefx_00008.webp"
    pause fxvar
    "images/fx/lovefx/lovefx_00009.webp"
    pause fxvar
    "images/fx/lovefx/lovefx_00010.webp"
    pause fxvar
    "images/fx/lovefx/lovefx_00011.webp"
    pause fxvar
    "images/fx/lovefx/lovefx_00012.webp"
    pause fxvar
    "images/fx/lovefx/lovefx_00013.webp"
    pause fxvar
    "images/fx/lovefx/lovefx_00014.webp"
    pause fxvar
    "images/fx/lovefx/lovefx_00015.webp"
    pause fxvar
    "images/fx/lovefx/lovefx_00016.webp"
    pause fxvar
    "images/fx/lovefx/lovefx_00017.webp"
    pause fxvar
    "images/fx/lovefx/lovefx_00018.webp"
    pause fxvar
    "images/fx/lovefx/lovefx_00019.webp"
    pause fxvar
    "images/fx/lovefx/lovefx_00020.webp"
    pause fxvar
    "images/fx/lovefx/lovefx_00021.webp"
    pause fxvar
    "images/fx/lovefx/lovefx_00022.webp"
    pause fxvar
    "images/fx/lovefx/lovefx_00023.webp"
    pause fxvar
    "images/fx/lovefx/lovefx_00024.webp"
    pause fxvar
    "images/fx/lovefx/lovefx_00025.webp"
    pause fxvar
    "images/fx/lovefx/lovefx_00026.webp"
    pause fxvar
    "images/fx/lovefx/lovefx_00027.webp"
    pause fxvar
    "images/fx/lovefx/lovefx_00028.webp"
    pause fxvar
    "images/fx/lovefx/lovefx_00029.webp"
    pause fxvar
    repeat

image chainfx: 
    "images/fx/chainfx/chainfx_00000.webp"
    pause fxvar
    "images/fx/chainfx/chainfx_00001.webp"
    pause fxvar
    "images/fx/chainfx/chainfx_00002.webp"
    pause fxvar
    "images/fx/chainfx/chainfx_00003.webp"
    pause fxvar
    "images/fx/chainfx/chainfx_00004.webp"
    pause fxvar
    "images/fx/chainfx/chainfx_00005.webp"
    pause fxvar
    "images/fx/chainfx/chainfx_00006.webp"
    pause fxvar
    "images/fx/chainfx/chainfx_00007.webp"
    pause fxvar
    "images/fx/chainfx/chainfx_00008.webp"
    pause fxvar
    "images/fx/chainfx/chainfx_00009.webp"
    pause fxvar
    "images/fx/chainfx/chainfx_00010.webp"
    pause fxvar
    "images/fx/chainfx/chainfx_00011.webp"
    pause fxvar
    "images/fx/chainfx/chainfx_00012.webp"
    pause fxvar
    "images/fx/chainfx/chainfx_00013.webp"
    pause fxvar
    "images/fx/chainfx/chainfx_00014.webp"
    pause fxvar
    "images/fx/chainfx/chainfx_00015.webp"
    pause fxvar
    "images/fx/chainfx/chainfx_00016.webp"
    pause fxvar
    "images/fx/chainfx/chainfx_00017.webp"
    pause fxvar
    "images/fx/chainfx/chainfx_00018.webp"
    pause fxvar
    "images/fx/chainfx/chainfx_00019.webp"
    pause fxvar
    "images/fx/chainfx/chainfx_00020.webp"
    pause fxvar
    "images/fx/chainfx/chainfx_00021.webp"
    pause fxvar
    "images/fx/chainfx/chainfx_00022.webp"
    pause fxvar
    "images/fx/chainfx/chainfx_00023.webp"
    pause fxvar
    "images/fx/chainfx/chainfx_00024.webp"
    pause fxvar
    "images/fx/chainfx/chainfx_00025.webp"
    pause fxvar
    "images/fx/chainfx/chainfx_00026.webp"
    pause fxvar
    "images/fx/chainfx/chainfx_00027.webp"
    pause fxvar
    "images/fx/chainfx/chainfx_00028.webp"
    pause fxvar
    repeat


image conflictfx: 
    "images/fx/conflictfx/conflictfx_00000.webp"
    pause fxvar
    "images/fx/conflictfx/conflictfx_00001.webp"
    pause fxvar
    "images/fx/conflictfx/conflictfx_00002.webp"
    pause fxvar
    "images/fx/conflictfx/conflictfx_00003.webp"
    pause fxvar
    "images/fx/conflictfx/conflictfx_00004.webp"
    pause fxvar
    "images/fx/conflictfx/conflictfx_00005.webp"
    pause fxvar
    "images/fx/conflictfx/conflictfx_00006.webp"
    pause fxvar
    "images/fx/conflictfx/conflictfx_00007.webp"
    pause fxvar
    "images/fx/conflictfx/conflictfx_00008.webp"
    pause fxvar
    "images/fx/conflictfx/conflictfx_00009.webp"
    pause fxvar
    "images/fx/conflictfx/conflictfx_00010.webp"
    pause fxvar
    "images/fx/conflictfx/conflictfx_00011.webp"
    pause fxvar
    "images/fx/conflictfx/conflictfx_00012.webp"
    pause fxvar
    "images/fx/conflictfx/conflictfx_00013.webp"
    pause fxvar
    "images/fx/conflictfx/conflictfx_00014.webp"
    pause fxvar
    "images/fx/conflictfx/conflictfx_00015.webp"
    pause fxvar
    "images/fx/conflictfx/conflictfx_00016.webp"
    pause fxvar
    "images/fx/conflictfx/conflictfx_00017.webp"
    pause fxvar
    "images/fx/conflictfx/conflictfx_00018.webp"
    pause fxvar
    "images/fx/conflictfx/conflictfx_00019.webp"
    pause fxvar
    "images/fx/conflictfx/conflictfx_00020.webp"
    pause fxvar
    "images/fx/conflictfx/conflictfx_00021.webp"
    pause fxvar
    "images/fx/conflictfx/conflictfx_00022.webp"
    pause fxvar
    "images/fx/conflictfx/conflictfx_00023.webp"
    pause fxvar
    "images/fx/conflictfx/conflictfx_00024.webp"
    pause fxvar
    "images/fx/conflictfx/conflictfx_00025.webp"
    pause fxvar
    "images/fx/conflictfx/conflictfx_00026.webp"
    pause fxvar
    "images/fx/conflictfx/conflictfx_00027.webp"
    pause fxvar
    "images/fx/conflictfx/conflictfx_00028.webp"
    pause fxvar
    repeat


image healedfx: 
    "images/fx/healedfx/healedfx_00000.webp"
    pause fxvar
    "images/fx/healedfx/healedfx_00001.webp"
    pause fxvar
    "images/fx/healedfx/healedfx_00002.webp"
    pause fxvar
    "images/fx/healedfx/healedfx_00003.webp"
    pause fxvar
    "images/fx/healedfx/healedfx_00004.webp"
    pause fxvar
    "images/fx/healedfx/healedfx_00005.webp"
    pause fxvar


image sicknessfx: 
    "images/fx/sicknessfx/sicknessfx_00000.webp"
    pause fxvar
    "images/fx/sicknessfx/sicknessfx_00001.webp"
    pause fxvar
    "images/fx/sicknessfx/sicknessfx_00002.webp"
    pause fxvar
    "images/fx/sicknessfx/sicknessfx_00003.webp"
    pause fxvar
    "images/fx/sicknessfx/sicknessfx_00004.webp"
    pause fxvar
    "images/fx/sicknessfx/sicknessfx_00005.webp"
    pause fxvar
    "images/fx/sicknessfx/sicknessfx_00006.webp"
    pause fxvar
    "images/fx/sicknessfx/sicknessfx_00007.webp"
    pause fxvar
    "images/fx/sicknessfx/sicknessfx_00008.webp"
    pause fxvar
    "images/fx/sicknessfx/sicknessfx_00009.webp"
    pause fxvar
    "images/fx/sicknessfx/sicknessfx_00010.webp"
    pause fxvar
    "images/fx/sicknessfx/sicknessfx_00011.webp"
    pause fxvar
    "images/fx/sicknessfx/sicknessfx_00012.webp"
    pause fxvar
    "images/fx/sicknessfx/sicknessfx_00013.webp"
    pause fxvar
    "images/fx/sicknessfx/sicknessfx_00014.webp"
    pause fxvar
    "images/fx/sicknessfx/sicknessfx_00015.webp"
    pause fxvar
    "images/fx/sicknessfx/sicknessfx_00016.webp"
    pause fxvar
    "images/fx/sicknessfx/sicknessfx_00017.webp"
    pause fxvar
    "images/fx/sicknessfx/sicknessfx_00018.webp"
    pause fxvar
    "images/fx/sicknessfx/sicknessfx_00019.webp"
    pause fxvar
    "images/fx/sicknessfx/sicknessfx_00020.webp"
    pause fxvar
    "images/fx/sicknessfx/sicknessfx_00021.webp"
    pause fxvar
    "images/fx/sicknessfx/sicknessfx_00022.webp"
    pause fxvar
    "images/fx/sicknessfx/sicknessfx_00023.webp"
    pause fxvar
    "images/fx/sicknessfx/sicknessfx_00024.webp"
    pause fxvar
    "images/fx/sicknessfx/sicknessfx_00025.webp"
    pause fxvar
    "images/fx/sicknessfx/sicknessfx_00026.webp"
    pause fxvar
    "images/fx/sicknessfx/sicknessfx_00027.webp"
    pause fxvar
    "images/fx/sicknessfx/sicknessfx_00028.webp"
    pause fxvar
    repeat


image noisedistortfx: 
    "images/fx/noisedistortfx/noisedistort_00000.webp"
    pause fxvar
    "images/fx/noisedistortfx/noisedistort_00001.webp"
    pause fxvar
    "images/fx/noisedistortfx/noisedistort_00002.webp"
    pause fxvar
    "images/fx/noisedistortfx/noisedistort_00003.webp"
    pause fxvar
    "images/fx/noisedistortfx/noisedistort_00004.webp"
    pause fxvar
    "images/fx/noisedistortfx/noisedistort_00005.webp"
    pause fxvar
    "images/fx/noisedistortfx/noisedistort_00006.webp"
    pause fxvar
    "images/fx/noisedistortfx/noisedistort_00007.webp"
    pause fxvar
    "images/fx/noisedistortfx/noisedistort_00008.webp"
    pause fxvar
    "images/fx/noisedistortfx/noisedistort_00009.webp"
    pause fxvar
    "images/fx/noisedistortfx/noisedistort_00010.webp"
    pause fxvar
    "images/fx/noisedistortfx/noisedistort_00011.webp"
    pause fxvar
    "images/fx/noisedistortfx/noisedistort_00012.webp"
    pause fxvar
    "images/fx/noisedistortfx/noisedistort_00013.webp"
    pause fxvar
    "images/fx/noisedistortfx/noisedistort_00014.webp"
    pause fxvar
    "images/fx/noisedistortfx/noisedistort_00015.webp"
    pause fxvar
    "images/fx/noisedistortfx/noisedistort_00016.webp"
    pause fxvar
    "images/fx/noisedistortfx/noisedistort_00017.webp"
    pause fxvar
    "images/fx/noisedistortfx/noisedistort_00018.webp"
    pause fxvar
    "images/fx/noisedistortfx/noisedistort_00019.webp"
    pause fxvar
    "images/fx/noisedistortfx/noisedistort_00020.webp"
    pause fxvar
    "images/fx/noisedistortfx/noisedistort_00021.webp"
    pause fxvar
    "images/fx/noisedistortfx/noisedistort_00022.webp"
    pause fxvar
    "images/fx/noisedistortfx/noisedistort_00023.webp"
    pause fxvar
    "images/fx/noisedistortfx/noisedistort_00024.webp"
    pause fxvar
    "images/fx/noisedistortfx/noisedistort_00025.webp"
    pause fxvar
    "images/fx/noisedistortfx/noisedistort_00026.webp"
    pause fxvar
    "images/fx/noisedistortfx/noisedistort_00027.webp"
    pause fxvar
    "images/fx/noisedistortfx/noisedistort_00028.webp"
    pause fxvar
    "images/fx/noisedistortfx/noisedistort_00029.webp"
    pause fxvar
    repeat


image rainfx: 
    "images/fx/rainfx/rainfx_00000.webp"
    pause fxvar
    "images/fx/rainfx/rainfx_00001.webp"
    pause fxvar
    "images/fx/rainfx/rainfx_00002.webp"
    pause fxvar
    "images/fx/rainfx/rainfx_00003.webp"
    pause fxvar
    "images/fx/rainfx/rainfx_00004.webp"
    pause fxvar
    "images/fx/rainfx/rainfx_00005.webp"
    pause fxvar
    "images/fx/rainfx/rainfx_00006.webp"
    pause fxvar
    "images/fx/rainfx/rainfx_00007.webp"
    pause fxvar
    "images/fx/rainfx/rainfx_00008.webp"
    pause fxvar
    "images/fx/rainfx/rainfx_00009.webp"
    pause fxvar
    "images/fx/rainfx/rainfx_00010.webp"
    pause fxvar
    "images/fx/rainfx/rainfx_00011.webp"
    pause fxvar
    "images/fx/rainfx/rainfx_00012.webp"
    pause fxvar
    "images/fx/rainfx/rainfx_00013.webp"
    pause fxvar
    "images/fx/rainfx/rainfx_00014.webp"
    pause fxvar
    "images/fx/rainfx/rainfx_00015.webp"
    pause fxvar
    "images/fx/rainfx/rainfx_00016.webp"
    pause fxvar
    "images/fx/rainfx/rainfx_00017.webp"
    pause fxvar
    "images/fx/rainfx/rainfx_00018.webp"
    pause fxvar
    "images/fx/rainfx/rainfx_00019.webp"
    pause fxvar
    "images/fx/rainfx/rainfx_00020.webp"
    pause fxvar
    "images/fx/rainfx/rainfx_00021.webp"
    pause fxvar
    "images/fx/rainfx/rainfx_00022.webp"
    pause fxvar
    "images/fx/rainfx/rainfx_00023.webp"
    pause fxvar
    "images/fx/rainfx/rainfx_00024.webp"
    pause fxvar
    "images/fx/rainfx/rainfx_00025.webp"
    pause fxvar
    "images/fx/rainfx/rainfx_00026.webp"
    pause fxvar
    "images/fx/rainfx/rainfx_00027.webp"
    pause fxvar
    "images/fx/rainfx/rainfx_00028.webp"
    pause fxvar
    "images/fx/rainfx/rainfx_00029.webp"
    pause fxvar
    repeat

image thunderfx: 
    "images/fx/thunderfx/thunderfx_00000.webp"
    pause fxvar
    "images/fx/thunderfx/thunderfx_00001.webp"
    pause fxvar
    "images/fx/thunderfx/thunderfx_00002.webp"
    pause fxvar
    "images/fx/thunderfx/thunderfx_00003.webp"
    pause fxvar
    "images/fx/thunderfx/thunderfx_00004.webp"
    pause fxvar
    "images/fx/thunderfx/thunderfx_00005.webp"
    pause fxvar
    "images/fx/thunderfx/thunderfx_00006.webp"
    pause fxvar
    "images/fx/thunderfx/thunderfx_00007.webp"
    pause fxvar
    "images/fx/thunderfx/thunderfx_00008.webp"
    pause fxvar
    "images/fx/thunderfx/thunderfx_00009.webp"
    pause fxvar
    "images/fx/thunderfx/thunderfx_00010.webp"
    pause fxvar
    "images/fx/thunderfx/thunderfx_00011.webp"
    pause fxvar
    "images/fx/thunderfx/thunderfx_00012.webp"
    pause fxvar
    "images/fx/thunderfx/thunderfx_00013.webp"
    pause fxvar
    "images/fx/thunderfx/thunderfx_00014.webp"
    pause fxvar
    "images/fx/thunderfx/thunderfx_00015.webp"
    pause fxvar
    "images/fx/thunderfx/thunderfx_00016.webp"
    pause fxvar
    "images/fx/thunderfx/thunderfx_00017.webp"
    pause fxvar
    "images/fx/thunderfx/thunderfx_00018.webp"
    pause fxvar
    "images/fx/thunderfx/thunderfx_00019.webp"
    pause fxvar
    "images/fx/thunderfx/thunderfx_00020.webp"
    pause fxvar
    "images/fx/thunderfx/thunderfx_00021.webp"
    pause fxvar
    "images/fx/thunderfx/thunderfx_00022.webp"
    pause fxvar
    "images/fx/thunderfx/thunderfx_00023.webp"
    pause fxvar
    "images/fx/thunderfx/thunderfx_00024.webp"
    pause fxvar
    "images/fx/thunderfx/thunderfx_00025.webp"
    pause fxvar
    "images/fx/thunderfx/thunderfx_00026.webp"
    pause fxvar
    "images/fx/thunderfx/thunderfx_00027.webp"
    pause fxvar
    "images/fx/thunderfx/thunderfx_00028.webp"
    pause fxvar
    "images/fx/thunderfx/thunderfx_00029.webp"
    pause fxvar


image flowersfx: 
    "images/fx/flowersfx/flowersfx_00000.webp"
    pause fxvar
    "images/fx/flowersfx/flowersfx_00001.webp"
    pause fxvar
    "images/fx/flowersfx/flowersfx_00002.webp"
    pause fxvar
    "images/fx/flowersfx/flowersfx_00003.webp"
    pause fxvar
    "images/fx/flowersfx/flowersfx_00004.webp"
    pause fxvar
    "images/fx/flowersfx/flowersfx_00005.webp"
    pause fxvar
    "images/fx/flowersfx/flowersfx_00006.webp"
    pause fxvar
    "images/fx/flowersfx/flowersfx_00007.webp"
    pause fxvar
    "images/fx/flowersfx/flowersfx_00008.webp"
    pause fxvar
    "images/fx/flowersfx/flowersfx_00009.webp"
    pause fxvar
    "images/fx/flowersfx/flowersfx_00010.webp"
    pause fxvar
    "images/fx/flowersfx/flowersfx_00011.webp"
    pause fxvar
    "images/fx/flowersfx/flowersfx_00012.webp"
    pause fxvar
    "images/fx/flowersfx/flowersfx_00013.webp"
    pause fxvar
    "images/fx/flowersfx/flowersfx_00014.webp"
    pause fxvar
    "images/fx/flowersfx/flowersfx_00015.webp"
    pause fxvar
    "images/fx/flowersfx/flowersfx_00016.webp"
    pause fxvar
    "images/fx/flowersfx/flowersfx_00017.webp"
    pause fxvar
    "images/fx/flowersfx/flowersfx_00018.webp"
    pause fxvar
    "images/fx/flowersfx/flowersfx_00019.webp"
    pause fxvar
    "images/fx/flowersfx/flowersfx_00020.webp"
    pause fxvar
    "images/fx/flowersfx/flowersfx_00021.webp"
    pause fxvar
    "images/fx/flowersfx/flowersfx_00022.webp"
    pause fxvar
    "images/fx/flowersfx/flowersfx_00023.webp"
    pause fxvar
    "images/fx/flowersfx/flowersfx_00024.webp"
    pause fxvar
    "images/fx/flowersfx/flowersfx_00025.webp"
    pause fxvar
    "images/fx/flowersfx/flowersfx_00026.webp"
    pause fxvar
    "images/fx/flowersfx/flowersfx_00027.webp"
    pause fxvar
    "images/fx/flowersfx/flowersfx_00028.webp"
    pause fxvar
    "images/fx/flowersfx/flowersfx_00029.webp"
    pause fxvar
    repeat


image burnfx: 
    "images/fx/burnfx/burnfx_00000.webp"
    pause fxvar
    "images/fx/burnfx/burnfx_00001.webp"
    pause fxvar
    "images/fx/burnfx/burnfx_00002.webp"
    pause fxvar
    "images/fx/burnfx/burnfx_00003.webp"
    pause fxvar
    "images/fx/burnfx/burnfx_00004.webp"
    pause fxvar
    "images/fx/burnfx/burnfx_00005.webp"
    pause fxvar
    "images/fx/burnfx/burnfx_00006.webp"
    pause fxvar
    "images/fx/burnfx/burnfx_00007.webp"
    pause fxvar
    "images/fx/burnfx/burnfx_00008.webp"
    pause fxvar
    "images/fx/burnfx/burnfx_00009.webp"
    pause fxvar
    "images/fx/burnfx/burnfx_00010.webp"
    pause fxvar
    "images/fx/burnfx/burnfx_00011.webp"
    pause fxvar
    "images/fx/burnfx/burnfx_00012.webp"
    pause fxvar
    "images/fx/burnfx/burnfx_00013.webp"
    pause fxvar
    "images/fx/burnfx/burnfx_00014.webp"
    pause fxvar
    "images/fx/burnfx/burnfx_00015.webp"
    pause fxvar
    "images/fx/burnfx/burnfx_00016.webp"
    pause fxvar
    "images/fx/burnfx/burnfx_00017.webp"
    pause fxvar
    "images/fx/burnfx/burnfx_00018.webp"
    pause fxvar
    "images/fx/burnfx/burnfx_00019.webp"
    pause fxvar
    "images/fx/burnfx/burnfx_00020.webp"
    pause fxvar
    "images/fx/burnfx/burnfx_00021.webp"
    pause fxvar
    "images/fx/burnfx/burnfx_00022.webp"
    pause fxvar
    "images/fx/burnfx/burnfx_00023.webp"
    pause fxvar
    "images/fx/burnfx/burnfx_00024.webp"
    pause fxvar
    "images/fx/burnfx/burnfx_00025.webp"
    pause fxvar
    "images/fx/burnfx/burnfx_00026.webp"
    pause fxvar
    "images/fx/burnfx/burnfx_00027.webp"
    pause fxvar
    "images/fx/burnfx/burnfx_00028.webp"
    pause fxvar
    "images/fx/burnfx/burnfx_00029.webp"
    pause fxvar
    repeat

image introspectfx: 
    "images/fx/introspectfx/introspectfx_00000.webp"
    pause fxvar
    "images/fx/introspectfx/introspectfx_00001.webp"
    pause fxvar
    "images/fx/introspectfx/introspectfx_00002.webp"
    pause fxvar
    "images/fx/introspectfx/introspectfx_00003.webp"
    pause fxvar
    "images/fx/introspectfx/introspectfx_00004.webp"
    pause fxvar
    "images/fx/introspectfx/introspectfx_00005.webp"
    pause fxvar
    "images/fx/introspectfx/introspectfx_00006.webp"
    pause fxvar
    "images/fx/introspectfx/introspectfx_00007.webp"
    pause fxvar
    "images/fx/introspectfx/introspectfx_00008.webp"
    pause fxvar
    "images/fx/introspectfx/introspectfx_00009.webp"
    pause fxvar
    "images/fx/introspectfx/introspectfx_00010.webp"
    pause fxvar
    "images/fx/introspectfx/introspectfx_00011.webp"
    pause fxvar
    "images/fx/introspectfx/introspectfx_00012.webp"
    pause fxvar
    "images/fx/introspectfx/introspectfx_00013.webp"
    pause fxvar
    "images/fx/introspectfx/introspectfx_00014.webp"
    pause fxvar
    "images/fx/introspectfx/introspectfx_00015.webp"
    pause fxvar
    "images/fx/introspectfx/introspectfx_00016.webp"
    pause fxvar
    "images/fx/introspectfx/introspectfx_00017.webp"
    pause fxvar
    "images/fx/introspectfx/introspectfx_00018.webp"
    pause fxvar
    "images/fx/introspectfx/introspectfx_00019.webp"
    pause fxvar
    "images/fx/introspectfx/introspectfx_00020.webp"
    pause fxvar
    "images/fx/introspectfx/introspectfx_00021.webp"
    pause fxvar
    "images/fx/introspectfx/introspectfx_00022.webp"
    pause fxvar
    "images/fx/introspectfx/introspectfx_00023.webp"
    pause fxvar
    "images/fx/introspectfx/introspectfx_00024.webp"
    pause fxvar
    "images/fx/introspectfx/introspectfx_00025.webp"
    pause fxvar
    "images/fx/introspectfx/introspectfx_00026.webp"
    pause fxvar
    "images/fx/introspectfx/introspectfx_00027.webp"
    pause fxvar
    "images/fx/introspectfx/introspectfx_00028.webp"
    pause fxvar
    "images/fx/introspectfx/introspectfx_00029.webp"
    pause fxvar
    repeat


image dizzyfx: 
    "images/fx/dizzyfx/dizzyfx_00000.webp"
    pause fxvar
    "images/fx/dizzyfx/dizzyfx_00001.webp"
    pause fxvar
    "images/fx/dizzyfx/dizzyfx_00002.webp"
    pause fxvar
    "images/fx/dizzyfx/dizzyfx_00003.webp"
    pause fxvar
    "images/fx/dizzyfx/dizzyfx_00004.webp"
    pause fxvar
    "images/fx/dizzyfx/dizzyfx_00005.webp"
    pause fxvar
    "images/fx/dizzyfx/dizzyfx_00006.webp"
    pause fxvar
    "images/fx/dizzyfx/dizzyfx_00007.webp"
    pause fxvar
    "images/fx/dizzyfx/dizzyfx_00008.webp"
    pause fxvar
    "images/fx/dizzyfx/dizzyfx_00009.webp"
    pause fxvar
    "images/fx/dizzyfx/dizzyfx_00010.webp"
    pause fxvar
    "images/fx/dizzyfx/dizzyfx_00011.webp"
    pause fxvar
    "images/fx/dizzyfx/dizzyfx_00012.webp"
    pause fxvar
    "images/fx/dizzyfx/dizzyfx_00013.webp"
    pause fxvar
    "images/fx/dizzyfx/dizzyfx_00014.webp"
    pause fxvar
    "images/fx/dizzyfx/dizzyfx_00015.webp"
    pause fxvar
    "images/fx/dizzyfx/dizzyfx_00016.webp"
    pause fxvar
    "images/fx/dizzyfx/dizzyfx_00017.webp"
    pause fxvar
    "images/fx/dizzyfx/dizzyfx_00018.webp"
    pause fxvar
    "images/fx/dizzyfx/dizzyfx_00019.webp"
    pause fxvar
    "images/fx/dizzyfx/dizzyfx_00020.webp"
    pause fxvar
    "images/fx/dizzyfx/dizzyfx_00021.webp"
    pause fxvar
    "images/fx/dizzyfx/dizzyfx_00022.webp"
    pause fxvar
    "images/fx/dizzyfx/dizzyfx_00023.webp"
    pause fxvar
    "images/fx/dizzyfx/dizzyfx_00024.webp"
    pause fxvar
    "images/fx/dizzyfx/dizzyfx_00025.webp"
    pause fxvar
    "images/fx/dizzyfx/dizzyfx_00026.webp"
    pause fxvar
    "images/fx/dizzyfx/dizzyfx_00027.webp"
    pause fxvar
    "images/fx/dizzyfx/dizzyfx_00028.webp"
    pause fxvar
    "images/fx/dizzyfx/dizzyfx_00029.webp"
    pause fxvar
    repeat


##########
#####
###
#
#
# TRANSITIONS
#
#
##
###
#####
##########


image tranone: 
    "images/transitions/tranone/tranone_00000.png"
    pause transhift
    "images/transitions/tranone/tranone_00001.png"
    pause transhift
    "images/transitions/tranone/tranone_00002.png"
    pause transhift
    "images/transitions/tranone/tranone_00003.png"
    pause transhift
    "images/transitions/tranone/tranone_00004.png"
    pause transhift
    "images/transitions/tranone/tranone_00005.png"
    pause transhift
    "images/transitions/tranone/tranone_00006.png"
    pause transhift
    "images/transitions/tranone/tranone_00007.png"
    pause transhift
    "images/transitions/tranone/tranone_00008.png"
    pause transhift
    "images/transitions/tranone/tranone_00009.png"
    pause transhift
    "images/transitions/tranone/tranone_00010.png"
    pause transhift

image tranonereverse: 
    "images/transitions/tranonereverse/tranonereverse_00000.png"
    pause transhift
    "images/transitions/tranonereverse/tranonereverse_00001.png"
    pause transhift
    "images/transitions/tranonereverse/tranonereverse_00002.png"
    pause transhift
    "images/transitions/tranonereverse/tranonereverse_00003.png"
    pause transhift
    "images/transitions/tranonereverse/tranonereverse_00004.png"
    pause transhift
    "images/transitions/tranonereverse/tranonereverse_00005.png"
    pause transhift
    "images/transitions/tranonereverse/tranonereverse_00006.png"
    pause transhift
    "images/transitions/tranonereverse/tranonereverse_00007.png"
    pause transhift
    "images/transitions/tranonereverse/tranonereverse_00008.png"
    pause transhift
    "images/transitions/tranonereverse/tranonereverse_00009.png"
    pause transhift
    "images/transitions/tranonereverse/tranonereverse_00010.png"
    pause transhift
    "images/transitions/tranonereverse/tranonereverse_00011.png"
    pause transhift
    "images/transitions/tranonereverse/tranonereverse_00012.png"
    pause transhift



##########
#####
###
#
#
# BACKDROPS
#
#
##
###
#####
##########


image sectionentrance: 
    "images/backdrops/sectionentrance/sectionentrance_00000.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00001.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00002.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00003.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00004.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00005.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00006.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00007.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00008.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00009.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00010.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00011.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00012.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00013.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00014.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00015.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00016.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00017.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00018.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00019.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00020.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00021.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00022.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00023.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00024.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00025.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00026.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00027.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00028.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00029.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00030.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00031.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00032.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00033.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00034.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00035.webp"
    pause backdropvar
    "images/backdrops/sectionentrance/sectionentrance_00036.webp"
    pause backdropvar
    repeat


image sceneonemain: 
    "images/backdrops/sceneonemain/sceneonemain_00000.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00001.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00002.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00003.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00004.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00005.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00006.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00007.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00008.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00009.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00010.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00011.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00012.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00013.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00014.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00015.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00016.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00017.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00018.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00019.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00020.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00021.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00022.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00023.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00024.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00025.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00026.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00027.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00028.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00029.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00030.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00031.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00032.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00033.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00034.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00035.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00036.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00037.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00038.webp"
    pause backdropvar
    "images/backdrops/sceneonemain/sceneonemain_00039.webp"
    pause backdropvar
    repeat


image sceneonechar: 
    "images/backdrops/sceneonechar/sceneonechar_00000.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00001.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00002.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00003.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00004.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00005.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00006.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00007.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00008.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00009.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00010.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00011.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00012.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00013.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00014.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00015.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00016.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00017.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00018.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00019.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00020.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00021.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00022.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00023.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00024.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00025.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00026.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00027.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00028.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00029.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00030.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00031.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00032.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00033.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00034.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00035.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00036.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00037.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00038.png"
    pause backdropvar
    "images/backdrops/sceneonechar/sceneonechar_00039.png"
    pause backdropvar
    repeat


image sceneonerailmain: 
    "images/backdrops/sceneonerailmain/sceneonerailmain_00000.png"
    pause backdropvar
    "images/backdrops/sceneonerailmain/sceneonerailmain_00001.png"
    pause backdropvar
    "images/backdrops/sceneonerailmain/sceneonerailmain_00002.png"
    pause backdropvar
    "images/backdrops/sceneonerailmain/sceneonerailmain_00003.png"
    pause backdropvar
    "images/backdrops/sceneonerailmain/sceneonerailmain_00004.png"
    pause backdropvar
    "images/backdrops/sceneonerailmain/sceneonerailmain_00005.png"
    pause backdropvar
    "images/backdrops/sceneonerailmain/sceneonerailmain_00006.png"
    pause backdropvar
    "images/backdrops/sceneonerailmain/sceneonerailmain_00007.png"
    pause backdropvar
    "images/backdrops/sceneonerailmain/sceneonerailmain_00008.png"
    pause backdropvar
    "images/backdrops/sceneonerailmain/sceneonerailmain_00009.png"
    pause backdropvar
    "images/backdrops/sceneonerailmain/sceneonerailmain_00010.png"
    pause backdropvar
    "images/backdrops/sceneonerailmain/sceneonerailmain_00011.png"
    pause backdropvar
    "images/backdrops/sceneonerailmain/sceneonerailmain_00012.png"
    pause backdropvar
    "images/backdrops/sceneonerailmain/sceneonerailmain_00013.png"
    pause backdropvar
    "images/backdrops/sceneonerailmain/sceneonerailmain_00014.png"
    pause backdropvar
    "images/backdrops/sceneonerailmain/sceneonerailmain_00015.png"
    pause backdropvar
    "images/backdrops/sceneonerailmain/sceneonerailmain_00016.png"
    pause backdropvar
    "images/backdrops/sceneonerailmain/sceneonerailmain_00017.png"
    pause backdropvar
    "images/backdrops/sceneonerailmain/sceneonerailmain_00018.png"
    pause backdropvar
    "images/backdrops/sceneonerailmain/sceneonerailmain_00019.png"
    pause backdropvar
    "images/backdrops/sceneonerailmain/sceneonerailmain_00020.png"
    pause backdropvar
    "images/backdrops/sceneonerailmain/sceneonerailmain_00021.png"
    pause backdropvar
    "images/backdrops/sceneonerailmain/sceneonerailmain_00022.png"
    pause backdropvar
    "images/backdrops/sceneonerailmain/sceneonerailmain_00023.png"
    pause backdropvar
    "images/backdrops/sceneonerailmain/sceneonerailmain_00024.png"
    pause backdropvar
    "images/backdrops/sceneonerailmain/sceneonerailmain_00025.png"
    pause backdropvar
    "images/backdrops/sceneonerailmain/sceneonerailmain_00026.png"
    pause backdropvar
    "images/backdrops/sceneonerailmain/sceneonerailmain_00027.png"
    pause backdropvar
    repeat


image sceneonerailchar: 
    "images/backdrops/sceneonerailchar/sceneonerailchar_00000.png"
    pause backdropvar
    "images/backdrops/sceneonerailchar/sceneonerailchar_00001.png"
    pause backdropvar
    "images/backdrops/sceneonerailchar/sceneonerailchar_00002.png"
    pause backdropvar
    "images/backdrops/sceneonerailchar/sceneonerailchar_00003.png"
    pause backdropvar
    "images/backdrops/sceneonerailchar/sceneonerailchar_00004.png"
    pause backdropvar
    "images/backdrops/sceneonerailchar/sceneonerailchar_00005.png"
    pause backdropvar
    "images/backdrops/sceneonerailchar/sceneonerailchar_00006.png"
    pause backdropvar
    "images/backdrops/sceneonerailchar/sceneonerailchar_00007.png"
    pause backdropvar
    "images/backdrops/sceneonerailchar/sceneonerailchar_00008.png"
    pause backdropvar
    "images/backdrops/sceneonerailchar/sceneonerailchar_00009.png"
    pause backdropvar
    "images/backdrops/sceneonerailchar/sceneonerailchar_00010.png"
    pause backdropvar
    "images/backdrops/sceneonerailchar/sceneonerailchar_00011.png"
    pause backdropvar
    "images/backdrops/sceneonerailchar/sceneonerailchar_00012.png"
    pause backdropvar
    "images/backdrops/sceneonerailchar/sceneonerailchar_00013.png"
    pause backdropvar
    "images/backdrops/sceneonerailchar/sceneonerailchar_00014.png"
    pause backdropvar
    "images/backdrops/sceneonerailchar/sceneonerailchar_00015.png"
    pause backdropvar
    "images/backdrops/sceneonerailchar/sceneonerailchar_00016.png"
    pause backdropvar
    "images/backdrops/sceneonerailchar/sceneonerailchar_00017.png"
    pause backdropvar
    "images/backdrops/sceneonerailchar/sceneonerailchar_00018.png"
    pause backdropvar
    "images/backdrops/sceneonerailchar/sceneonerailchar_00019.png"
    pause backdropvar
    "images/backdrops/sceneonerailchar/sceneonerailchar_00020.png"
    pause backdropvar
    "images/backdrops/sceneonerailchar/sceneonerailchar_00021.png"
    pause backdropvar
    "images/backdrops/sceneonerailchar/sceneonerailchar_00022.png"
    pause backdropvar
    "images/backdrops/sceneonerailchar/sceneonerailchar_00023.png"
    pause backdropvar
    "images/backdrops/sceneonerailchar/sceneonerailchar_00024.png"
    pause backdropvar
    "images/backdrops/sceneonerailchar/sceneonerailchar_00025.png"
    pause backdropvar
    "images/backdrops/sceneonerailchar/sceneonerailchar_00026.png"
    pause backdropvar
    "images/backdrops/sceneonerailchar/sceneonerailchar_00027.png"
    pause backdropvar
    repeat


image scenetwoundermain: 
    "images/backdrops/scenetwoundermain/scenetwoundermain_00000.png"
    pause backdropvar
    "images/backdrops/scenetwoundermain/scenetwoundermain_00001.png"
    pause backdropvar
    "images/backdrops/scenetwoundermain/scenetwoundermain_00002.png"
    pause backdropvar
    "images/backdrops/scenetwoundermain/scenetwoundermain_00003.png"
    pause backdropvar
    "images/backdrops/scenetwoundermain/scenetwoundermain_00004.png"
    pause backdropvar
    "images/backdrops/scenetwoundermain/scenetwoundermain_00005.png"
    pause backdropvar
    "images/backdrops/scenetwoundermain/scenetwoundermain_00006.png"
    pause backdropvar
    "images/backdrops/scenetwoundermain/scenetwoundermain_00007.png"
    pause backdropvar
    "images/backdrops/scenetwoundermain/scenetwoundermain_00008.png"
    pause backdropvar
    "images/backdrops/scenetwoundermain/scenetwoundermain_00009.png"
    pause backdropvar
    "images/backdrops/scenetwoundermain/scenetwoundermain_00010.png"
    pause backdropvar
    "images/backdrops/scenetwoundermain/scenetwoundermain_00011.png"
    pause backdropvar
    "images/backdrops/scenetwoundermain/scenetwoundermain_00012.png"
    pause backdropvar
    "images/backdrops/scenetwoundermain/scenetwoundermain_00013.png"
    pause backdropvar
    "images/backdrops/scenetwoundermain/scenetwoundermain_00014.png"
    pause backdropvar
    "images/backdrops/scenetwoundermain/scenetwoundermain_00015.png"
    pause backdropvar
    "images/backdrops/scenetwoundermain/scenetwoundermain_00016.png"
    pause backdropvar
    "images/backdrops/scenetwoundermain/scenetwoundermain_00017.png"
    pause backdropvar
    "images/backdrops/scenetwoundermain/scenetwoundermain_00018.png"
    pause backdropvar
    "images/backdrops/scenetwoundermain/scenetwoundermain_00019.png"
    pause backdropvar
    "images/backdrops/scenetwoundermain/scenetwoundermain_00020.png"
    pause backdropvar
    "images/backdrops/scenetwoundermain/scenetwoundermain_00021.png"
    pause backdropvar
    "images/backdrops/scenetwoundermain/scenetwoundermain_00022.png"
    pause backdropvar
    "images/backdrops/scenetwoundermain/scenetwoundermain_00023.png"
    pause backdropvar
    "images/backdrops/scenetwoundermain/scenetwoundermain_00024.png"
    pause backdropvar
    "images/backdrops/scenetwoundermain/scenetwoundermain_00025.png"
    pause backdropvar
    "images/backdrops/scenetwoundermain/scenetwoundermain_00026.png"
    pause backdropvar
    "images/backdrops/scenetwoundermain/scenetwoundermain_00027.png"
    pause backdropvar
    repeat


image scenetwounderchar: 
    "images/backdrops/scenetwounderchar/scenetwounderchar_00000.png"
    pause backdropvar
    "images/backdrops/scenetwounderchar/scenetwounderchar_00001.png"
    pause backdropvar
    "images/backdrops/scenetwounderchar/scenetwounderchar_00002.png"
    pause backdropvar
    "images/backdrops/scenetwounderchar/scenetwounderchar_00003.png"
    pause backdropvar
    "images/backdrops/scenetwounderchar/scenetwounderchar_00004.png"
    pause backdropvar
    "images/backdrops/scenetwounderchar/scenetwounderchar_00005.png"
    pause backdropvar
    "images/backdrops/scenetwounderchar/scenetwounderchar_00006.png"
    pause backdropvar
    "images/backdrops/scenetwounderchar/scenetwounderchar_00007.png"
    pause backdropvar
    "images/backdrops/scenetwounderchar/scenetwounderchar_00008.png"
    pause backdropvar
    "images/backdrops/scenetwounderchar/scenetwounderchar_00009.png"
    pause backdropvar
    "images/backdrops/scenetwounderchar/scenetwounderchar_00010.png"
    pause backdropvar
    "images/backdrops/scenetwounderchar/scenetwounderchar_00011.png"
    pause backdropvar
    "images/backdrops/scenetwounderchar/scenetwounderchar_00012.png"
    pause backdropvar
    "images/backdrops/scenetwounderchar/scenetwounderchar_00013.png"
    pause backdropvar
    "images/backdrops/scenetwounderchar/scenetwounderchar_00014.png"
    pause backdropvar
    "images/backdrops/scenetwounderchar/scenetwounderchar_00015.png"
    pause backdropvar
    "images/backdrops/scenetwounderchar/scenetwounderchar_00016.png"
    pause backdropvar
    "images/backdrops/scenetwounderchar/scenetwounderchar_00017.png"
    pause backdropvar
    "images/backdrops/scenetwounderchar/scenetwounderchar_00018.png"
    pause backdropvar
    "images/backdrops/scenetwounderchar/scenetwounderchar_00019.png"
    pause backdropvar
    "images/backdrops/scenetwounderchar/scenetwounderchar_00020.png"
    pause backdropvar
    "images/backdrops/scenetwounderchar/scenetwounderchar_00021.png"
    pause backdropvar
    "images/backdrops/scenetwounderchar/scenetwounderchar_00022.png"
    pause backdropvar
    "images/backdrops/scenetwounderchar/scenetwounderchar_00023.png"
    pause backdropvar
    "images/backdrops/scenetwounderchar/scenetwounderchar_00024.png"
    pause backdropvar
    "images/backdrops/scenetwounderchar/scenetwounderchar_00025.png"
    pause backdropvar
    "images/backdrops/scenetwounderchar/scenetwounderchar_00026.png"
    pause backdropvar
    "images/backdrops/scenetwounderchar/scenetwounderchar_00027.png"
    pause backdropvar
    repeat


image scenethreemain: 
    "images/backdrops/scenethreemain/scenethreemain_00000.png"
    pause backdropvar
    "images/backdrops/scenethreemain/scenethreemain_00001.png"
    pause backdropvar
    "images/backdrops/scenethreemain/scenethreemain_00002.png"
    pause backdropvar
    "images/backdrops/scenethreemain/scenethreemain_00003.png"
    pause backdropvar
    "images/backdrops/scenethreemain/scenethreemain_00004.png"
    pause backdropvar
    "images/backdrops/scenethreemain/scenethreemain_00005.png"
    pause backdropvar
    "images/backdrops/scenethreemain/scenethreemain_00006.png"
    pause backdropvar
    "images/backdrops/scenethreemain/scenethreemain_00007.png"
    pause backdropvar
    "images/backdrops/scenethreemain/scenethreemain_00008.png"
    pause backdropvar
    "images/backdrops/scenethreemain/scenethreemain_00009.png"
    pause backdropvar
    "images/backdrops/scenethreemain/scenethreemain_00010.png"
    pause backdropvar
    "images/backdrops/scenethreemain/scenethreemain_00011.png"
    pause backdropvar
    "images/backdrops/scenethreemain/scenethreemain_00012.png"
    pause backdropvar
    "images/backdrops/scenethreemain/scenethreemain_00013.png"
    pause backdropvar
    "images/backdrops/scenethreemain/scenethreemain_00014.png"
    pause backdropvar
    "images/backdrops/scenethreemain/scenethreemain_00015.png"
    pause backdropvar
    "images/backdrops/scenethreemain/scenethreemain_00016.png"
    pause backdropvar
    "images/backdrops/scenethreemain/scenethreemain_00017.png"
    pause backdropvar
    "images/backdrops/scenethreemain/scenethreemain_00018.png"
    pause backdropvar
    "images/backdrops/scenethreemain/scenethreemain_00019.png"
    pause backdropvar
    "images/backdrops/scenethreemain/scenethreemain_00020.png"
    pause backdropvar
    "images/backdrops/scenethreemain/scenethreemain_00021.png"
    pause backdropvar
    "images/backdrops/scenethreemain/scenethreemain_00022.png"
    pause backdropvar
    "images/backdrops/scenethreemain/scenethreemain_00023.png"
    pause backdropvar
    "images/backdrops/scenethreemain/scenethreemain_00024.png"
    pause backdropvar
    "images/backdrops/scenethreemain/scenethreemain_00025.png"
    pause backdropvar
    "images/backdrops/scenethreemain/scenethreemain_00026.png"
    pause backdropvar
    "images/backdrops/scenethreemain/scenethreemain_00027.png"
    pause backdropvar
    repeat

image scenethreechar: 
    "images/backdrops/scenethreechar/scenethreechar_00000.png"
    pause backdropvar
    "images/backdrops/scenethreechar/scenethreechar_00001.png"
    pause backdropvar
    "images/backdrops/scenethreechar/scenethreechar_00002.png"
    pause backdropvar
    "images/backdrops/scenethreechar/scenethreechar_00003.png"
    pause backdropvar
    "images/backdrops/scenethreechar/scenethreechar_00004.png"
    pause backdropvar
    "images/backdrops/scenethreechar/scenethreechar_00005.png"
    pause backdropvar
    "images/backdrops/scenethreechar/scenethreechar_00006.png"
    pause backdropvar
    "images/backdrops/scenethreechar/scenethreechar_00007.png"
    pause backdropvar
    "images/backdrops/scenethreechar/scenethreechar_00008.png"
    pause backdropvar
    "images/backdrops/scenethreechar/scenethreechar_00009.png"
    pause backdropvar
    "images/backdrops/scenethreechar/scenethreechar_00010.png"
    pause backdropvar
    "images/backdrops/scenethreechar/scenethreechar_00011.png"
    pause backdropvar
    "images/backdrops/scenethreechar/scenethreechar_00012.png"
    pause backdropvar
    "images/backdrops/scenethreechar/scenethreechar_00013.png"
    pause backdropvar
    "images/backdrops/scenethreechar/scenethreechar_00014.png"
    pause backdropvar
    "images/backdrops/scenethreechar/scenethreechar_00015.png"
    pause backdropvar
    "images/backdrops/scenethreechar/scenethreechar_00016.png"
    pause backdropvar
    "images/backdrops/scenethreechar/scenethreechar_00017.png"
    pause backdropvar
    "images/backdrops/scenethreechar/scenethreechar_00018.png"
    pause backdropvar
    "images/backdrops/scenethreechar/scenethreechar_00019.png"
    pause backdropvar
    "images/backdrops/scenethreechar/scenethreechar_00020.png"
    pause backdropvar
    "images/backdrops/scenethreechar/scenethreechar_00021.png"
    pause backdropvar
    "images/backdrops/scenethreechar/scenethreechar_00022.png"
    pause backdropvar
    "images/backdrops/scenethreechar/scenethreechar_00023.png"
    pause backdropvar
    "images/backdrops/scenethreechar/scenethreechar_00024.png"
    pause backdropvar
    "images/backdrops/scenethreechar/scenethreechar_00025.png"
    pause backdropvar
    "images/backdrops/scenethreechar/scenethreechar_00026.png"
    pause backdropvar
    "images/backdrops/scenethreechar/scenethreechar_00027.png"
    pause backdropvar
    repeat

image scenefourmain: 
    "images/backdrops/scenefourmain/scenefourmain_00000.png"
    pause backdropvar
    "images/backdrops/scenefourmain/scenefourmain_00001.png"
    pause backdropvar
    "images/backdrops/scenefourmain/scenefourmain_00002.png"
    pause backdropvar
    "images/backdrops/scenefourmain/scenefourmain_00003.png"
    pause backdropvar
    "images/backdrops/scenefourmain/scenefourmain_00004.png"
    pause backdropvar
    "images/backdrops/scenefourmain/scenefourmain_00005.png"
    pause backdropvar
    "images/backdrops/scenefourmain/scenefourmain_00006.png"
    pause backdropvar
    "images/backdrops/scenefourmain/scenefourmain_00007.png"
    pause backdropvar
    "images/backdrops/scenefourmain/scenefourmain_00008.png"
    pause backdropvar
    "images/backdrops/scenefourmain/scenefourmain_00009.png"
    pause backdropvar
    "images/backdrops/scenefourmain/scenefourmain_00010.png"
    pause backdropvar
    "images/backdrops/scenefourmain/scenefourmain_00011.png"
    pause backdropvar
    "images/backdrops/scenefourmain/scenefourmain_00012.png"
    pause backdropvar
    "images/backdrops/scenefourmain/scenefourmain_00013.png"
    pause backdropvar
    "images/backdrops/scenefourmain/scenefourmain_00014.png"
    pause backdropvar
    "images/backdrops/scenefourmain/scenefourmain_00015.png"
    pause backdropvar
    "images/backdrops/scenefourmain/scenefourmain_00016.png"
    pause backdropvar
    "images/backdrops/scenefourmain/scenefourmain_00017.png"
    pause backdropvar
    "images/backdrops/scenefourmain/scenefourmain_00018.png"
    pause backdropvar
    "images/backdrops/scenefourmain/scenefourmain_00019.png"
    pause backdropvar
    "images/backdrops/scenefourmain/scenefourmain_00020.png"
    pause backdropvar
    "images/backdrops/scenefourmain/scenefourmain_00021.png"
    pause backdropvar
    "images/backdrops/scenefourmain/scenefourmain_00022.png"
    pause backdropvar
    "images/backdrops/scenefourmain/scenefourmain_00023.png"
    pause backdropvar
    "images/backdrops/scenefourmain/scenefourmain_00024.png"
    pause backdropvar
    "images/backdrops/scenefourmain/scenefourmain_00025.png"
    pause backdropvar
    "images/backdrops/scenefourmain/scenefourmain_00026.png"
    pause backdropvar
    "images/backdrops/scenefourmain/scenefourmain_00027.png"
    pause backdropvar
    repeat

image scenefourchar: 
    "images/backdrops/scenefourchar/scenefourchar_00000.png"
    pause backdropvar
    "images/backdrops/scenefourchar/scenefourchar_00001.png"
    pause backdropvar
    "images/backdrops/scenefourchar/scenefourchar_00002.png"
    pause backdropvar
    "images/backdrops/scenefourchar/scenefourchar_00003.png"
    pause backdropvar
    "images/backdrops/scenefourchar/scenefourchar_00004.png"
    pause backdropvar
    "images/backdrops/scenefourchar/scenefourchar_00005.png"
    pause backdropvar
    "images/backdrops/scenefourchar/scenefourchar_00006.png"
    pause backdropvar
    "images/backdrops/scenefourchar/scenefourchar_00007.png"
    pause backdropvar
    "images/backdrops/scenefourchar/scenefourchar_00008.png"
    pause backdropvar
    "images/backdrops/scenefourchar/scenefourchar_00009.png"
    pause backdropvar
    "images/backdrops/scenefourchar/scenefourchar_00010.png"
    pause backdropvar
    "images/backdrops/scenefourchar/scenefourchar_00011.png"
    pause backdropvar
    "images/backdrops/scenefourchar/scenefourchar_00012.png"
    pause backdropvar
    "images/backdrops/scenefourchar/scenefourchar_00013.png"
    pause backdropvar
    "images/backdrops/scenefourchar/scenefourchar_00014.png"
    pause backdropvar
    "images/backdrops/scenefourchar/scenefourchar_00015.png"
    pause backdropvar
    "images/backdrops/scenefourchar/scenefourchar_00016.png"
    pause backdropvar
    "images/backdrops/scenefourchar/scenefourchar_00017.png"
    pause backdropvar
    "images/backdrops/scenefourchar/scenefourchar_00018.png"
    pause backdropvar
    "images/backdrops/scenefourchar/scenefourchar_00019.png"
    pause backdropvar
    "images/backdrops/scenefourchar/scenefourchar_00020.png"
    pause backdropvar
    "images/backdrops/scenefourchar/scenefourchar_00021.png"
    pause backdropvar
    "images/backdrops/scenefourchar/scenefourchar_00022.png"
    pause backdropvar
    "images/backdrops/scenefourchar/scenefourchar_00023.png"
    pause backdropvar
    "images/backdrops/scenefourchar/scenefourchar_00024.png"
    pause backdropvar
    "images/backdrops/scenefourchar/scenefourchar_00025.png"
    pause backdropvar
    "images/backdrops/scenefourchar/scenefourchar_00026.png"
    pause backdropvar
    "images/backdrops/scenefourchar/scenefourchar_00027.png"
    pause backdropvar
    repeat


image scenefivemain: 
    "images/backdrops/scenefivemain/scenefivemain_00000.png"
    pause backdropvar
    "images/backdrops/scenefivemain/scenefivemain_00001.png"
    pause backdropvar
    "images/backdrops/scenefivemain/scenefivemain_00002.png"
    pause backdropvar
    "images/backdrops/scenefivemain/scenefivemain_00003.png"
    pause backdropvar
    "images/backdrops/scenefivemain/scenefivemain_00004.png"
    pause backdropvar
    "images/backdrops/scenefivemain/scenefivemain_00005.png"
    pause backdropvar
    "images/backdrops/scenefivemain/scenefivemain_00006.png"
    pause backdropvar
    "images/backdrops/scenefivemain/scenefivemain_00007.png"
    pause backdropvar
    "images/backdrops/scenefivemain/scenefivemain_00008.png"
    pause backdropvar
    "images/backdrops/scenefivemain/scenefivemain_00009.png"
    pause backdropvar
    "images/backdrops/scenefivemain/scenefivemain_00010.png"
    pause backdropvar
    "images/backdrops/scenefivemain/scenefivemain_00011.png"
    pause backdropvar
    "images/backdrops/scenefivemain/scenefivemain_00012.png"
    pause backdropvar
    "images/backdrops/scenefivemain/scenefivemain_00013.png"
    pause backdropvar
    "images/backdrops/scenefivemain/scenefivemain_00014.png"
    pause backdropvar
    "images/backdrops/scenefivemain/scenefivemain_00015.png"
    pause backdropvar
    "images/backdrops/scenefivemain/scenefivemain_00016.png"
    pause backdropvar
    "images/backdrops/scenefivemain/scenefivemain_00017.png"
    pause backdropvar
    "images/backdrops/scenefivemain/scenefivemain_00018.png"
    pause backdropvar
    "images/backdrops/scenefivemain/scenefivemain_00019.png"
    pause backdropvar
    "images/backdrops/scenefivemain/scenefivemain_00020.png"
    pause backdropvar
    "images/backdrops/scenefivemain/scenefivemain_00021.png"
    pause backdropvar
    "images/backdrops/scenefivemain/scenefivemain_00022.png"
    pause backdropvar
    "images/backdrops/scenefivemain/scenefivemain_00023.png"
    pause backdropvar
    "images/backdrops/scenefivemain/scenefivemain_00024.png"
    pause backdropvar
    "images/backdrops/scenefivemain/scenefivemain_00025.png"
    pause backdropvar
    "images/backdrops/scenefivemain/scenefivemain_00026.png"
    pause backdropvar
    "images/backdrops/scenefivemain/scenefivemain_00027.png"
    pause backdropvar
    repeat

image scenefivechar: 
    "images/backdrops/scenefivechar/scenefivechar_00000.png"
    pause backdropvar
    "images/backdrops/scenefivechar/scenefivechar_00001.png"
    pause backdropvar
    "images/backdrops/scenefivechar/scenefivechar_00002.png"
    pause backdropvar
    "images/backdrops/scenefivechar/scenefivechar_00003.png"
    pause backdropvar
    "images/backdrops/scenefivechar/scenefivechar_00004.png"
    pause backdropvar
    "images/backdrops/scenefivechar/scenefivechar_00005.png"
    pause backdropvar
    "images/backdrops/scenefivechar/scenefivechar_00006.png"
    pause backdropvar
    "images/backdrops/scenefivechar/scenefivechar_00007.png"
    pause backdropvar
    "images/backdrops/scenefivechar/scenefivechar_00008.png"
    pause backdropvar
    "images/backdrops/scenefivechar/scenefivechar_00009.png"
    pause backdropvar
    "images/backdrops/scenefivechar/scenefivechar_00010.png"
    pause backdropvar
    "images/backdrops/scenefivechar/scenefivechar_00011.png"
    pause backdropvar
    "images/backdrops/scenefivechar/scenefivechar_00012.png"
    pause backdropvar
    "images/backdrops/scenefivechar/scenefivechar_00013.png"
    pause backdropvar
    "images/backdrops/scenefivechar/scenefivechar_00014.png"
    pause backdropvar
    "images/backdrops/scenefivechar/scenefivechar_00015.png"
    pause backdropvar
    "images/backdrops/scenefivechar/scenefivechar_00016.png"
    pause backdropvar
    "images/backdrops/scenefivechar/scenefivechar_00017.png"
    pause backdropvar
    "images/backdrops/scenefivechar/scenefivechar_00018.png"
    pause backdropvar
    "images/backdrops/scenefivechar/scenefivechar_00019.png"
    pause backdropvar
    "images/backdrops/scenefivechar/scenefivechar_00020.png"
    pause backdropvar
    "images/backdrops/scenefivechar/scenefivechar_00021.png"
    pause backdropvar
    "images/backdrops/scenefivechar/scenefivechar_00022.png"
    pause backdropvar
    "images/backdrops/scenefivechar/scenefivechar_00023.png"
    pause backdropvar
    "images/backdrops/scenefivechar/scenefivechar_00024.png"
    pause backdropvar
    "images/backdrops/scenefivechar/scenefivechar_00025.png"
    pause backdropvar
    "images/backdrops/scenefivechar/scenefivechar_00026.png"
    pause backdropvar
    "images/backdrops/scenefivechar/scenefivechar_00027.png"
    pause backdropvar
    repeat

image scenesixmain: 
    "images/backdrops/scenesixmain/scenesixmain_00000.png"
    pause backdropvar
    "images/backdrops/scenesixmain/scenesixmain_00001.png"
    pause backdropvar
    "images/backdrops/scenesixmain/scenesixmain_00002.png"
    pause backdropvar
    "images/backdrops/scenesixmain/scenesixmain_00003.png"
    pause backdropvar
    "images/backdrops/scenesixmain/scenesixmain_00004.png"
    pause backdropvar
    "images/backdrops/scenesixmain/scenesixmain_00005.png"
    pause backdropvar
    "images/backdrops/scenesixmain/scenesixmain_00006.png"
    pause backdropvar
    "images/backdrops/scenesixmain/scenesixmain_00007.png"
    pause backdropvar
    "images/backdrops/scenesixmain/scenesixmain_00008.png"
    pause backdropvar
    "images/backdrops/scenesixmain/scenesixmain_00009.png"
    pause backdropvar
    "images/backdrops/scenesixmain/scenesixmain_00010.png"
    pause backdropvar
    "images/backdrops/scenesixmain/scenesixmain_00011.png"
    pause backdropvar
    "images/backdrops/scenesixmain/scenesixmain_00012.png"
    pause backdropvar
    "images/backdrops/scenesixmain/scenesixmain_00013.png"
    pause backdropvar
    "images/backdrops/scenesixmain/scenesixmain_00014.png"
    pause backdropvar
    "images/backdrops/scenesixmain/scenesixmain_00015.png"
    pause backdropvar
    "images/backdrops/scenesixmain/scenesixmain_00016.png"
    pause backdropvar
    "images/backdrops/scenesixmain/scenesixmain_00017.png"
    pause backdropvar
    "images/backdrops/scenesixmain/scenesixmain_00018.png"
    pause backdropvar
    "images/backdrops/scenesixmain/scenesixmain_00019.png"
    pause backdropvar
    "images/backdrops/scenesixmain/scenesixmain_00020.png"
    pause backdropvar
    "images/backdrops/scenesixmain/scenesixmain_00021.png"
    pause backdropvar
    "images/backdrops/scenesixmain/scenesixmain_00022.png"
    pause backdropvar
    "images/backdrops/scenesixmain/scenesixmain_00023.png"
    pause backdropvar
    "images/backdrops/scenesixmain/scenesixmain_00024.png"
    pause backdropvar
    "images/backdrops/scenesixmain/scenesixmain_00025.png"
    pause backdropvar
    "images/backdrops/scenesixmain/scenesixmain_00026.png"
    pause backdropvar
    "images/backdrops/scenesixmain/scenesixmain_00027.png"
    pause backdropvar
    repeat

image scenesixchar: 
    "images/backdrops/scenesixchar/scenesixchar_00000.png"
    pause backdropvar
    "images/backdrops/scenesixchar/scenesixchar_00001.png"
    pause backdropvar
    "images/backdrops/scenesixchar/scenesixchar_00002.png"
    pause backdropvar
    "images/backdrops/scenesixchar/scenesixchar_00003.png"
    pause backdropvar
    "images/backdrops/scenesixchar/scenesixchar_00004.png"
    pause backdropvar
    "images/backdrops/scenesixchar/scenesixchar_00005.png"
    pause backdropvar
    "images/backdrops/scenesixchar/scenesixchar_00006.png"
    pause backdropvar
    "images/backdrops/scenesixchar/scenesixchar_00007.png"
    pause backdropvar
    "images/backdrops/scenesixchar/scenesixchar_00008.png"
    pause backdropvar
    "images/backdrops/scenesixchar/scenesixchar_00009.png"
    pause backdropvar
    "images/backdrops/scenesixchar/scenesixchar_00010.png"
    pause backdropvar
    "images/backdrops/scenesixchar/scenesixchar_00011.png"
    pause backdropvar
    "images/backdrops/scenesixchar/scenesixchar_00012.png"
    pause backdropvar
    "images/backdrops/scenesixchar/scenesixchar_00013.png"
    pause backdropvar
    "images/backdrops/scenesixchar/scenesixchar_00014.png"
    pause backdropvar
    "images/backdrops/scenesixchar/scenesixchar_00015.png"
    pause backdropvar
    "images/backdrops/scenesixchar/scenesixchar_00016.png"
    pause backdropvar
    "images/backdrops/scenesixchar/scenesixchar_00017.png"
    pause backdropvar
    "images/backdrops/scenesixchar/scenesixchar_00018.png"
    pause backdropvar
    "images/backdrops/scenesixchar/scenesixchar_00019.png"
    pause backdropvar
    "images/backdrops/scenesixchar/scenesixchar_00020.png"
    pause backdropvar
    "images/backdrops/scenesixchar/scenesixchar_00021.png"
    pause backdropvar
    "images/backdrops/scenesixchar/scenesixchar_00022.png"
    pause backdropvar
    "images/backdrops/scenesixchar/scenesixchar_00023.png"
    pause backdropvar
    "images/backdrops/scenesixchar/scenesixchar_00024.png"
    pause backdropvar
    "images/backdrops/scenesixchar/scenesixchar_00025.png"
    pause backdropvar
    "images/backdrops/scenesixchar/scenesixchar_00026.png"
    pause backdropvar
    "images/backdrops/scenesixchar/scenesixchar_00027.png"
    pause backdropvar
    repeat

image scenesevenmain: 
    "images/backdrops/scenesevenmain/scenesevenmain_00000.png"
    pause backdropvar
    "images/backdrops/scenesevenmain/scenesevenmain_00001.png"
    pause backdropvar
    "images/backdrops/scenesevenmain/scenesevenmain_00002.png"
    pause backdropvar
    "images/backdrops/scenesevenmain/scenesevenmain_00003.png"
    pause backdropvar
    "images/backdrops/scenesevenmain/scenesevenmain_00004.png"
    pause backdropvar
    "images/backdrops/scenesevenmain/scenesevenmain_00005.png"
    pause backdropvar
    "images/backdrops/scenesevenmain/scenesevenmain_00006.png"
    pause backdropvar
    "images/backdrops/scenesevenmain/scenesevenmain_00007.png"
    pause backdropvar
    "images/backdrops/scenesevenmain/scenesevenmain_00008.png"
    pause backdropvar
    "images/backdrops/scenesevenmain/scenesevenmain_00009.png"
    pause backdropvar
    "images/backdrops/scenesevenmain/scenesevenmain_00010.png"
    pause backdropvar
    "images/backdrops/scenesevenmain/scenesevenmain_00011.png"
    pause backdropvar
    "images/backdrops/scenesevenmain/scenesevenmain_00012.png"
    pause backdropvar
    "images/backdrops/scenesevenmain/scenesevenmain_00013.png"
    pause backdropvar
    "images/backdrops/scenesevenmain/scenesevenmain_00014.png"
    pause backdropvar
    "images/backdrops/scenesevenmain/scenesevenmain_00015.png"
    pause backdropvar
    "images/backdrops/scenesevenmain/scenesevenmain_00016.png"
    pause backdropvar
    "images/backdrops/scenesevenmain/scenesevenmain_00017.png"
    pause backdropvar
    "images/backdrops/scenesevenmain/scenesevenmain_00018.png"
    pause backdropvar
    "images/backdrops/scenesevenmain/scenesevenmain_00019.png"
    pause backdropvar
    "images/backdrops/scenesevenmain/scenesevenmain_00020.png"
    pause backdropvar
    "images/backdrops/scenesevenmain/scenesevenmain_00021.png"
    pause backdropvar
    "images/backdrops/scenesevenmain/scenesevenmain_00022.png"
    pause backdropvar
    "images/backdrops/scenesevenmain/scenesevenmain_00023.png"
    pause backdropvar
    "images/backdrops/scenesevenmain/scenesevenmain_00024.png"
    pause backdropvar
    "images/backdrops/scenesevenmain/scenesevenmain_00025.png"
    pause backdropvar
    "images/backdrops/scenesevenmain/scenesevenmain_00026.png"
    pause backdropvar
    "images/backdrops/scenesevenmain/scenesevenmain_00027.png"
    pause backdropvar
    repeat

image scenesevenchar: 
    "images/backdrops/scenesevenchar/scenesevenchar_00000.png"
    pause backdropvar
    "images/backdrops/scenesevenchar/scenesevenchar_00001.png"
    pause backdropvar
    "images/backdrops/scenesevenchar/scenesevenchar_00002.png"
    pause backdropvar
    "images/backdrops/scenesevenchar/scenesevenchar_00003.png"
    pause backdropvar
    "images/backdrops/scenesevenchar/scenesevenchar_00004.png"
    pause backdropvar
    "images/backdrops/scenesevenchar/scenesevenchar_00005.png"
    pause backdropvar
    "images/backdrops/scenesevenchar/scenesevenchar_00006.png"
    pause backdropvar
    "images/backdrops/scenesevenchar/scenesevenchar_00007.png"
    pause backdropvar
    "images/backdrops/scenesevenchar/scenesevenchar_00008.png"
    pause backdropvar
    "images/backdrops/scenesevenchar/scenesevenchar_00009.png"
    pause backdropvar
    "images/backdrops/scenesevenchar/scenesevenchar_00010.png"
    pause backdropvar
    "images/backdrops/scenesevenchar/scenesevenchar_00011.png"
    pause backdropvar
    "images/backdrops/scenesevenchar/scenesevenchar_00012.png"
    pause backdropvar
    "images/backdrops/scenesevenchar/scenesevenchar_00013.png"
    pause backdropvar
    "images/backdrops/scenesevenchar/scenesevenchar_00014.png"
    pause backdropvar
    "images/backdrops/scenesevenchar/scenesevenchar_00015.png"
    pause backdropvar
    "images/backdrops/scenesevenchar/scenesevenchar_00016.png"
    pause backdropvar
    "images/backdrops/scenesevenchar/scenesevenchar_00017.png"
    pause backdropvar
    "images/backdrops/scenesevenchar/scenesevenchar_00018.png"
    pause backdropvar
    "images/backdrops/scenesevenchar/scenesevenchar_00019.png"
    pause backdropvar
    "images/backdrops/scenesevenchar/scenesevenchar_00020.png"
    pause backdropvar
    "images/backdrops/scenesevenchar/scenesevenchar_00021.png"
    pause backdropvar
    "images/backdrops/scenesevenchar/scenesevenchar_00022.png"
    pause backdropvar
    "images/backdrops/scenesevenchar/scenesevenchar_00023.png"
    pause backdropvar
    "images/backdrops/scenesevenchar/scenesevenchar_00024.png"
    pause backdropvar
    "images/backdrops/scenesevenchar/scenesevenchar_00025.png"
    pause backdropvar
    "images/backdrops/scenesevenchar/scenesevenchar_00026.png"
    pause backdropvar
    "images/backdrops/scenesevenchar/scenesevenchar_00027.png"
    pause backdropvar
    repeat


image sceneeightmain: 
    "images/backdrops/sceneeightmain/sceneeightmain_00000.png"
    pause backdropvar
    "images/backdrops/sceneeightmain/sceneeightmain_00001.png"
    pause backdropvar
    "images/backdrops/sceneeightmain/sceneeightmain_00002.png"
    pause backdropvar
    "images/backdrops/sceneeightmain/sceneeightmain_00003.png"
    pause backdropvar
    "images/backdrops/sceneeightmain/sceneeightmain_00004.png"
    pause backdropvar
    "images/backdrops/sceneeightmain/sceneeightmain_00005.png"
    pause backdropvar
    "images/backdrops/sceneeightmain/sceneeightmain_00006.png"
    pause backdropvar
    "images/backdrops/sceneeightmain/sceneeightmain_00007.png"
    pause backdropvar
    "images/backdrops/sceneeightmain/sceneeightmain_00008.png"
    pause backdropvar
    "images/backdrops/sceneeightmain/sceneeightmain_00009.png"
    pause backdropvar
    "images/backdrops/sceneeightmain/sceneeightmain_00010.png"
    pause backdropvar
    "images/backdrops/sceneeightmain/sceneeightmain_00011.png"
    pause backdropvar
    "images/backdrops/sceneeightmain/sceneeightmain_00012.png"
    pause backdropvar
    "images/backdrops/sceneeightmain/sceneeightmain_00013.png"
    pause backdropvar
    "images/backdrops/sceneeightmain/sceneeightmain_00014.png"
    pause backdropvar
    "images/backdrops/sceneeightmain/sceneeightmain_00015.png"
    pause backdropvar
    "images/backdrops/sceneeightmain/sceneeightmain_00016.png"
    pause backdropvar
    "images/backdrops/sceneeightmain/sceneeightmain_00017.png"
    pause backdropvar
    "images/backdrops/sceneeightmain/sceneeightmain_00018.png"
    pause backdropvar
    "images/backdrops/sceneeightmain/sceneeightmain_00019.png"
    pause backdropvar
    "images/backdrops/sceneeightmain/sceneeightmain_00020.png"
    pause backdropvar
    "images/backdrops/sceneeightmain/sceneeightmain_00021.png"
    pause backdropvar
    "images/backdrops/sceneeightmain/sceneeightmain_00022.png"
    pause backdropvar
    "images/backdrops/sceneeightmain/sceneeightmain_00023.png"
    pause backdropvar
    "images/backdrops/sceneeightmain/sceneeightmain_00024.png"
    pause backdropvar
    "images/backdrops/sceneeightmain/sceneeightmain_00025.png"
    pause backdropvar
    "images/backdrops/sceneeightmain/sceneeightmain_00026.png"
    pause backdropvar
    "images/backdrops/sceneeightmain/sceneeightmain_00027.png"
    pause backdropvar
    repeat

image sceneeightchar: 
    "images/backdrops/sceneeightchar/sceneeightchar_00000.png"
    pause backdropvar
    "images/backdrops/sceneeightchar/sceneeightchar_00001.png"
    pause backdropvar
    "images/backdrops/sceneeightchar/sceneeightchar_00002.png"
    pause backdropvar
    "images/backdrops/sceneeightchar/sceneeightchar_00003.png"
    pause backdropvar
    "images/backdrops/sceneeightchar/sceneeightchar_00004.png"
    pause backdropvar
    "images/backdrops/sceneeightchar/sceneeightchar_00005.png"
    pause backdropvar
    "images/backdrops/sceneeightchar/sceneeightchar_00006.png"
    pause backdropvar
    "images/backdrops/sceneeightchar/sceneeightchar_00007.png"
    pause backdropvar
    "images/backdrops/sceneeightchar/sceneeightchar_00008.png"
    pause backdropvar
    "images/backdrops/sceneeightchar/sceneeightchar_00009.png"
    pause backdropvar
    "images/backdrops/sceneeightchar/sceneeightchar_00010.png"
    pause backdropvar
    "images/backdrops/sceneeightchar/sceneeightchar_00011.png"
    pause backdropvar
    "images/backdrops/sceneeightchar/sceneeightchar_00012.png"
    pause backdropvar
    "images/backdrops/sceneeightchar/sceneeightchar_00013.png"
    pause backdropvar
    "images/backdrops/sceneeightchar/sceneeightchar_00014.png"
    pause backdropvar
    "images/backdrops/sceneeightchar/sceneeightchar_00015.png"
    pause backdropvar
    "images/backdrops/sceneeightchar/sceneeightchar_00016.png"
    pause backdropvar
    "images/backdrops/sceneeightchar/sceneeightchar_00017.png"
    pause backdropvar
    "images/backdrops/sceneeightchar/sceneeightchar_00018.png"
    pause backdropvar
    "images/backdrops/sceneeightchar/sceneeightchar_00019.png"
    pause backdropvar
    "images/backdrops/sceneeightchar/sceneeightchar_00020.png"
    pause backdropvar
    "images/backdrops/sceneeightchar/sceneeightchar_00021.png"
    pause backdropvar
    "images/backdrops/sceneeightchar/sceneeightchar_00022.png"
    pause backdropvar
    "images/backdrops/sceneeightchar/sceneeightchar_00023.png"
    pause backdropvar
    "images/backdrops/sceneeightchar/sceneeightchar_00024.png"
    pause backdropvar
    "images/backdrops/sceneeightchar/sceneeightchar_00025.png"
    pause backdropvar
    "images/backdrops/sceneeightchar/sceneeightchar_00026.png"
    pause backdropvar
    "images/backdrops/sceneeightchar/sceneeightchar_00027.png"
    pause backdropvar
    repeat


image sceneninemain: 
    "images/backdrops/sceneninemain/sceneninemain_00000.png"
    pause backdropvar
    "images/backdrops/sceneninemain/sceneninemain_00001.png"
    pause backdropvar
    "images/backdrops/sceneninemain/sceneninemain_00002.png"
    pause backdropvar
    "images/backdrops/sceneninemain/sceneninemain_00003.png"
    pause backdropvar
    "images/backdrops/sceneninemain/sceneninemain_00004.png"
    pause backdropvar
    "images/backdrops/sceneninemain/sceneninemain_00005.png"
    pause backdropvar
    "images/backdrops/sceneninemain/sceneninemain_00006.png"
    pause backdropvar
    "images/backdrops/sceneninemain/sceneninemain_00007.png"
    pause backdropvar
    "images/backdrops/sceneninemain/sceneninemain_00008.png"
    pause backdropvar
    "images/backdrops/sceneninemain/sceneninemain_00009.png"
    pause backdropvar
    "images/backdrops/sceneninemain/sceneninemain_00010.png"
    pause backdropvar
    "images/backdrops/sceneninemain/sceneninemain_00011.png"
    pause backdropvar
    "images/backdrops/sceneninemain/sceneninemain_00012.png"
    pause backdropvar
    "images/backdrops/sceneninemain/sceneninemain_00013.png"
    pause backdropvar
    "images/backdrops/sceneninemain/sceneninemain_00014.png"
    pause backdropvar
    "images/backdrops/sceneninemain/sceneninemain_00015.png"
    pause backdropvar
    "images/backdrops/sceneninemain/sceneninemain_00016.png"
    pause backdropvar
    "images/backdrops/sceneninemain/sceneninemain_00017.png"
    pause backdropvar
    "images/backdrops/sceneninemain/sceneninemain_00018.png"
    pause backdropvar
    "images/backdrops/sceneninemain/sceneninemain_00019.png"
    pause backdropvar
    "images/backdrops/sceneninemain/sceneninemain_00020.png"
    pause backdropvar
    "images/backdrops/sceneninemain/sceneninemain_00021.png"
    pause backdropvar
    "images/backdrops/sceneninemain/sceneninemain_00022.png"
    pause backdropvar
    "images/backdrops/sceneninemain/sceneninemain_00023.png"
    pause backdropvar
    "images/backdrops/sceneninemain/sceneninemain_00024.png"
    pause backdropvar
    "images/backdrops/sceneninemain/sceneninemain_00025.png"
    pause backdropvar
    "images/backdrops/sceneninemain/sceneninemain_00026.png"
    pause backdropvar
    repeat


image sceneninechar: 
    "images/backdrops/sceneninechar/sceneninechar_00000.png"
    pause backdropvar
    "images/backdrops/sceneninechar/sceneninechar_00001.png"
    pause backdropvar
    "images/backdrops/sceneninechar/sceneninechar_00002.png"
    pause backdropvar
    "images/backdrops/sceneninechar/sceneninechar_00003.png"
    pause backdropvar
    "images/backdrops/sceneninechar/sceneninechar_00004.png"
    pause backdropvar
    "images/backdrops/sceneninechar/sceneninechar_00005.png"
    pause backdropvar
    "images/backdrops/sceneninechar/sceneninechar_00006.png"
    pause backdropvar
    "images/backdrops/sceneninechar/sceneninechar_00007.png"
    pause backdropvar
    "images/backdrops/sceneninechar/sceneninechar_00008.png"
    pause backdropvar
    "images/backdrops/sceneninechar/sceneninechar_00009.png"
    pause backdropvar
    "images/backdrops/sceneninechar/sceneninechar_00010.png"
    pause backdropvar
    "images/backdrops/sceneninechar/sceneninechar_00011.png"
    pause backdropvar
    "images/backdrops/sceneninechar/sceneninechar_00012.png"
    pause backdropvar
    "images/backdrops/sceneninechar/sceneninechar_00013.png"
    pause backdropvar
    "images/backdrops/sceneninechar/sceneninechar_00014.png"
    pause backdropvar
    "images/backdrops/sceneninechar/sceneninechar_00015.png"
    pause backdropvar
    "images/backdrops/sceneninechar/sceneninechar_00016.png"
    pause backdropvar
    "images/backdrops/sceneninechar/sceneninechar_00017.png"
    pause backdropvar
    "images/backdrops/sceneninechar/sceneninechar_00018.png"
    pause backdropvar
    "images/backdrops/sceneninechar/sceneninechar_00019.png"
    pause backdropvar
    "images/backdrops/sceneninechar/sceneninechar_00020.png"
    pause backdropvar
    "images/backdrops/sceneninechar/sceneninechar_00021.png"
    pause backdropvar
    "images/backdrops/sceneninechar/sceneninechar_00022.png"
    pause backdropvar
    "images/backdrops/sceneninechar/sceneninechar_00023.png"
    pause backdropvar
    "images/backdrops/sceneninechar/sceneninechar_00024.png"
    pause backdropvar
    "images/backdrops/sceneninechar/sceneninechar_00025.png"
    pause backdropvar
    "images/backdrops/sceneninechar/sceneninechar_00026.png"
    pause backdropvar
    repeat


image scenetenmain: 
    "images/backdrops/scenetenmain/scenetenmain_00000.png"
    pause backdropvar
    "images/backdrops/scenetenmain/scenetenmain_00001.png"
    pause backdropvar
    "images/backdrops/scenetenmain/scenetenmain_00002.png"
    pause backdropvar
    "images/backdrops/scenetenmain/scenetenmain_00003.png"
    pause backdropvar
    "images/backdrops/scenetenmain/scenetenmain_00004.png"
    pause backdropvar
    "images/backdrops/scenetenmain/scenetenmain_00005.png"
    pause backdropvar
    "images/backdrops/scenetenmain/scenetenmain_00006.png"
    pause backdropvar
    "images/backdrops/scenetenmain/scenetenmain_00007.png"
    pause backdropvar
    "images/backdrops/scenetenmain/scenetenmain_00008.png"
    pause backdropvar
    "images/backdrops/scenetenmain/scenetenmain_00009.png"
    pause backdropvar
    "images/backdrops/scenetenmain/scenetenmain_00010.png"
    pause backdropvar
    "images/backdrops/scenetenmain/scenetenmain_00011.png"
    pause backdropvar
    "images/backdrops/scenetenmain/scenetenmain_00012.png"
    pause backdropvar
    "images/backdrops/scenetenmain/scenetenmain_00013.png"
    pause backdropvar
    "images/backdrops/scenetenmain/scenetenmain_00014.png"
    pause backdropvar
    "images/backdrops/scenetenmain/scenetenmain_00015.png"
    pause backdropvar
    "images/backdrops/scenetenmain/scenetenmain_00016.png"
    pause backdropvar
    "images/backdrops/scenetenmain/scenetenmain_00017.png"
    pause backdropvar
    "images/backdrops/scenetenmain/scenetenmain_00018.png"
    pause backdropvar
    "images/backdrops/scenetenmain/scenetenmain_00019.png"
    pause backdropvar
    "images/backdrops/scenetenmain/scenetenmain_00020.png"
    pause backdropvar
    "images/backdrops/scenetenmain/scenetenmain_00021.png"
    pause backdropvar
    "images/backdrops/scenetenmain/scenetenmain_00022.png"
    pause backdropvar
    "images/backdrops/scenetenmain/scenetenmain_00023.png"
    pause backdropvar
    "images/backdrops/scenetenmain/scenetenmain_00024.png"
    pause backdropvar
    "images/backdrops/scenetenmain/scenetenmain_00025.png"
    pause backdropvar
    "images/backdrops/scenetenmain/scenetenmain_00026.png"
    pause backdropvar
    repeat


image scenetenchar: 
    "images/backdrops/scenetenchar/scenetenchar_00000.png"
    pause backdropvar
    "images/backdrops/scenetenchar/scenetenchar_00001.png"
    pause backdropvar
    "images/backdrops/scenetenchar/scenetenchar_00002.png"
    pause backdropvar
    "images/backdrops/scenetenchar/scenetenchar_00003.png"
    pause backdropvar
    "images/backdrops/scenetenchar/scenetenchar_00004.png"
    pause backdropvar
    "images/backdrops/scenetenchar/scenetenchar_00005.png"
    pause backdropvar
    "images/backdrops/scenetenchar/scenetenchar_00006.png"
    pause backdropvar
    "images/backdrops/scenetenchar/scenetenchar_00007.png"
    pause backdropvar
    "images/backdrops/scenetenchar/scenetenchar_00008.png"
    pause backdropvar
    "images/backdrops/scenetenchar/scenetenchar_00009.png"
    pause backdropvar
    "images/backdrops/scenetenchar/scenetenchar_00010.png"
    pause backdropvar
    "images/backdrops/scenetenchar/scenetenchar_00011.png"
    pause backdropvar
    "images/backdrops/scenetenchar/scenetenchar_00012.png"
    pause backdropvar
    "images/backdrops/scenetenchar/scenetenchar_00013.png"
    pause backdropvar
    "images/backdrops/scenetenchar/scenetenchar_00014.png"
    pause backdropvar
    "images/backdrops/scenetenchar/scenetenchar_00015.png"
    pause backdropvar
    "images/backdrops/scenetenchar/scenetenchar_00016.png"
    pause backdropvar
    "images/backdrops/scenetenchar/scenetenchar_00017.png"
    pause backdropvar
    "images/backdrops/scenetenchar/scenetenchar_00018.png"
    pause backdropvar
    "images/backdrops/scenetenchar/scenetenchar_00019.png"
    pause backdropvar
    "images/backdrops/scenetenchar/scenetenchar_00020.png"
    pause backdropvar
    "images/backdrops/scenetenchar/scenetenchar_00021.png"
    pause backdropvar
    "images/backdrops/scenetenchar/scenetenchar_00022.png"
    pause backdropvar
    "images/backdrops/scenetenchar/scenetenchar_00023.png"
    pause backdropvar
    "images/backdrops/scenetenchar/scenetenchar_00024.png"
    pause backdropvar
    "images/backdrops/scenetenchar/scenetenchar_00025.png"
    pause backdropvar
    "images/backdrops/scenetenchar/scenetenchar_00026.png"
    pause backdropvar
    repeat




##########
#####
###
#
#
# CHARACTERS - MOUTH ANIMATIONS 
#
#
##
###
#####
##########

image rexzoommouth: 
    "images/characters/rexzoommouth/rexzoommouth_00000.png"
    pause mouthvariable
    "images/characters/rexzoommouth/rexzoommouth_00001.png"
    pause mouthvariable
    "images/characters/rexzoommouth/rexzoommouth_00002.png"
    pause mouthvariable
    "images/characters/rexzoommouth/rexzoommouth_00003.png"
    pause mouthvariable
    "images/characters/rexzoommouth/rexzoommouth_00004.png"
    pause mouthvariable
    repeat


image minazoommouth: 
    "images/characters/minazoommouth/minazoommouth_00000.png"
    pause mouthvariable
    "images/characters/minazoommouth/minazoommouth_00001.png"
    pause mouthvariable
    "images/characters/minazoommouth/minazoommouth_00002.png"
    pause mouthvariable
    "images/characters/minazoommouth/minazoommouth_00003.png"
    pause mouthvariable
    "images/characters/minazoommouth/minazoommouth_00004.png"
    pause mouthvariable
    repeat

image rexstandingmouth: 
    "images/characters/rexstandingmouth/rexstandingmouth_00000.png"
    pause mouthvariable
    "images/characters/rexstandingmouth/rexstandingmouth_00001.png"
    pause mouthvariable
    "images/characters/rexstandingmouth/rexstandingmouth_00002.png"
    pause mouthvariable
    "images/characters/rexstandingmouth/rexstandingmouth_00003.png"
    pause mouthvariable
    "images/characters/rexstandingmouth/rexstandingmouth_00004.png"
    pause mouthvariable
    repeat


image minastandingmouth: 
    "images/characters/minastandingmouth/minastandingmouth_00000.png"
    pause mouthvariable
    "images/characters/minastandingmouth/minastandingmouth_00001.png"
    pause mouthvariable
    "images/characters/minastandingmouth/minastandingmouth_00002.png"
    pause mouthvariable
    "images/characters/minastandingmouth/minastandingmouth_00003.png"
    pause mouthvariable
    "images/characters/minastandingmouth/minastandingmouth_00004.png"
    pause mouthvariable
    repeat

image rexfacewidemouth: 
    "images/characters/rexfacemouth/rexfacemouth_00000.png"
    pause mouthvariable
    "images/characters/rexfacemouth/rexfacemouth_00001.png"
    pause mouthvariable
    "images/characters/rexfacemouth/rexfacemouth_00002.png"
    pause mouthvariable
    "images/characters/rexfacemouth/rexfacemouth_00003.png"
    pause mouthvariable
    "images/characters/rexfacemouth/rexfacemouth_00004.png"
    pause mouthvariable
    "images/characters/rexfacemouth/rexfacemouth_00005.png"
    pause mouthvariable
    repeat

image minafacewidemouth: 
    "images/characters/minafacemouth/minafacemouth_00000.png"
    pause mouthvariable
    "images/characters/minafacemouth/minafacemouth_00001.png"
    pause mouthvariable
    "images/characters/minafacemouth/minafacemouth_00002.png"
    pause mouthvariable
    "images/characters/minafacemouth/minafacemouth_00003.png"
    pause mouthvariable
    "images/characters/minafacemouth/minafacemouth_00004.png"
    pause mouthvariable
    "images/characters/minafacemouth/minafacemouth_00005.png"
    pause mouthvariable
    repeat

image rexfacestandardmouth: 
    "images/characters/rexfacemouth/rexfacemouth_00000.png"
    pause mouthvariable
    "images/characters/rexfacemouth/rexfacemouth_00001.png"
    pause mouthvariable
    "images/characters/rexfacemouth/rexfacemouth_00002.png"
    pause mouthvariable
    "images/characters/rexfacemouth/rexfacemouth_00003.png"
    pause mouthvariable
    "images/characters/rexfacemouth/rexfacemouth_00004.png"
    pause mouthvariable
    "images/characters/rexfacemouth/rexfacemouth_00005.png"
    pause mouthvariable
    repeat

image minafacestandardmouth: 
    "images/characters/minafacemouth/minafacemouth_00000.png"
    pause mouthvariable
    "images/characters/minafacemouth/minafacemouth_00001.png"
    pause mouthvariable
    "images/characters/minafacemouth/minafacemouth_00002.png"
    pause mouthvariable
    "images/characters/minafacemouth/minafacemouth_00003.png"
    pause mouthvariable
    "images/characters/minafacemouth/minafacemouth_00004.png"
    pause mouthvariable
    "images/characters/minafacemouth/minafacemouth_00005.png"
    pause mouthvariable
    repeat


##########
#####
###
#
#
# CHARACTERS - SHADOWS, DARKENERS, AND CHAR BACKGROUNDS 
#
#
##
###
#####
##########

image facedark: 
    "images/characters/facebackgrounddarken.png"
    alpha darkcharvar

image facebackground: 
    block:
        "images/characters/facebackgroundluma/facebackgroundluma_00000.png"
        pause lumafade
        "images/characters/facebackgroundluma/facebackgroundluma_00001.png"
        pause lumafade
        "images/characters/facebackgroundluma/facebackgroundluma_00002.png"
        pause lumafade
        "images/characters/facebackgroundluma/facebackgroundluma_00003.png"
        pause lumafade
        "images/characters/facebackgroundluma/facebackgroundluma_00004.png"
        pause lumafade
        "images/characters/facebackgroundluma/facebackgroundluma_00005.png"
        pause lumafade
        "images/characters/facebackgroundluma/facebackgroundluma_00006.png"
        pause lumafade
        "images/characters/facebackgroundluma/facebackgroundluma_00007.png"
        pause lumafade
    block:
        "images/characters/facebackground/facebackground_00000.png"
        pause facebackvariable
        "images/characters/facebackground/facebackground_00001.png"
        pause facebackvariable
        "images/characters/facebackground/facebackground_00002.png"
        pause facebackvariable
        "images/characters/facebackground/facebackground_00003.png"
        pause facebackvariable
        "images/characters/facebackground/facebackground_00004.png"
        pause facebackvariable
        "images/characters/facebackground/facebackground_00005.png"
        pause facebackvariable
        repeat

image minafacedark: 
    "images/characters/minafacedarken.png"
    alpha darkcharvar

image minastandingdark: 
    "images/characters/minastanddarken.png"
    alpha darkcharvar

image minazoomdark: 
    "images/characters/minazoomdarken.png"
    alpha darkcharvar

image minastandingshadow:
    alpha shadowcharvar 
    "images/characters/minastandingshadow/minastandingshadow_00000.png"
    pause shadowvar
    "images/characters/minastandingshadow/minastandingshadow_00001.png"
    pause shadowvar
    "images/characters/minastandingshadow/minastandingshadow_00002.png"
    pause shadowvar
    "images/characters/minastandingshadow/minastandingshadow_00003.png"
    pause shadowvar
    "images/characters/minastandingshadow/minastandingshadow_00004.png"
    pause shadowvar
    "images/characters/minastandingshadow/minastandingshadow_00005.png"
    pause shadowvar
    "images/characters/minastandingshadow/minastandingshadow_00006.png"
    pause shadowvar
    "images/characters/minastandingshadow/minastandingshadow_00007.png"
    pause shadowvar
    "images/characters/minastandingshadow/minastandingshadow_00008.png"
    pause shadowvar
    "images/characters/minastandingshadow/minastandingshadow_00009.png"
    pause shadowvar
    "images/characters/minastandingshadow/minastandingshadow_00010.png"
    pause shadowvar
    repeat

image minazoomshadow: 
    alpha shadowcharvar 
    "images/characters/minazoomshadow/minazoomshadow_00000.png"
    pause shadowvar
    "images/characters/minazoomshadow/minazoomshadow_00001.png"
    pause shadowvar
    "images/characters/minazoomshadow/minazoomshadow_00002.png"
    pause shadowvar
    "images/characters/minazoomshadow/minazoomshadow_00003.png"
    pause shadowvar
    "images/characters/minazoomshadow/minazoomshadow_00004.png"
    pause shadowvar
    "images/characters/minazoomshadow/minazoomshadow_00005.png"
    pause shadowvar
    "images/characters/minazoomshadow/minazoomshadow_00006.png"
    pause shadowvar
    "images/characters/minazoomshadow/minazoomshadow_00007.png"
    pause shadowvar
    "images/characters/minazoomshadow/minazoomshadow_00008.png"
    pause shadowvar
    "images/characters/minazoomshadow/minazoomshadow_00009.png"
    pause shadowvar
    "images/characters/minazoomshadow/minazoomshadow_00010.png"
    pause shadowvar
    repeat

image rexfacedark: 
    "images/characters/rexfacedarken.png"
    alpha darkcharvar

image rexstandingdark: 
    "images/characters/rexstandingdarken.png"
    alpha darkcharvar

image rexzoomdark: 
    "images/characters/rexzoomdarken.png"
    alpha darkcharvar


image rexstandingshadow:
    alpha shadowcharvar 
    "images/characters/rexstandingshadow/rexstandingshadow_00000.png"
    pause shadowvar
    "images/characters/rexstandingshadow/rexstandingshadow_00001.png"
    pause shadowvar
    "images/characters/rexstandingshadow/rexstandingshadow_00002.png"
    pause shadowvar
    "images/characters/rexstandingshadow/rexstandingshadow_00003.png"
    pause shadowvar
    "images/characters/rexstandingshadow/rexstandingshadow_00004.png"
    pause shadowvar
    "images/characters/rexstandingshadow/rexstandingshadow_00005.png"
    pause shadowvar
    repeat

image rexzoomshadow: 
    alpha shadowcharvar 
    "images/characters/rexzoomshadow/rexzoomshadow_00000.png"
    pause shadowvar
    "images/characters/rexzoomshadow/rexzoomshadow_00001.png"
    pause shadowvar
    "images/characters/rexzoomshadow/rexzoomshadow_00002.png"
    pause shadowvar
    "images/characters/rexzoomshadow/rexzoomshadow_00003.png"
    pause shadowvar
    "images/characters/rexzoomshadow/rexzoomshadow_00004.png"
    pause shadowvar
    "images/characters/rexzoomshadow/rexzoomshadow_00005.png"
    pause shadowvar
    repeat



##########
#####
###
#
#
# CHARACTERS - STANDING
#
#
##
###
#####
##########

image rexstandingneutral:
    block:
        "images/characters/rexstandingneutralluma/rexstandingneutralluma_00000.png"
        pause lumafade
        "images/characters/rexstandingneutralluma/rexstandingneutralluma_00001.png"
        pause lumafade
        "images/characters/rexstandingneutralluma/rexstandingneutralluma_00002.png"
        pause lumafade
        "images/characters/rexstandingneutralluma/rexstandingneutralluma_00003.png"
        pause lumafade
        "images/characters/rexstandingneutralluma/rexstandingneutralluma_00004.png"
        pause lumafade
        "images/characters/rexstandingneutralluma/rexstandingneutralluma_00005.png"
        pause lumafade
        "images/characters/rexstandingneutralluma/rexstandingneutralluma_00006.png"
        pause lumafade
        "images/characters/rexstandingneutralluma/rexstandingneutralluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexstandingneutral/rexstandingneutral_00000.png"
        pause blinkingvar
        "images/characters/rexstandingneutral/rexstandingneutral_00001.png"
        pause blinkingvar
        "images/characters/rexstandingneutral/rexstandingneutral_00002.png"
        pause 0.2
        "images/characters/rexstandingneutral/rexstandingneutral_00003.png"
        pause blinkingvar
        "images/characters/rexstandingneutral/rexstandingneutral_00004.png"
        pause blinkingvar
        "images/characters/rexstandingneutral/rexstandingneutral_00005.png"
        pause blinkingvar
        repeat


image rexstandinghappy:
    block:
        "images/characters/rexstandinghappyluma/rexstandinghappyluma_00000.png"
        pause lumafade
        "images/characters/rexstandinghappyluma/rexstandinghappyluma_00001.png"
        pause lumafade
        "images/characters/rexstandinghappyluma/rexstandinghappyluma_00002.png"
        pause lumafade
        "images/characters/rexstandinghappyluma/rexstandinghappyluma_00003.png"
        pause lumafade
        "images/characters/rexstandinghappyluma/rexstandinghappyluma_00004.png"
        pause lumafade
        "images/characters/rexstandinghappyluma/rexstandinghappyluma_00005.png"
        pause lumafade
        "images/characters/rexstandinghappyluma/rexstandinghappyluma_00006.png"
        pause lumafade
        "images/characters/rexstandinghappyluma/rexstandinghappyluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexstandinghappy/rexstandinghappy_00000.png"
        pause blinkingvar
        "images/characters/rexstandinghappy/rexstandinghappy_00001.png"
        pause blinkingvar
        "images/characters/rexstandinghappy/rexstandinghappy_00002.png"
        pause 0.2
        "images/characters/rexstandinghappy/rexstandinghappy_00003.png"
        pause blinkingvar
        "images/characters/rexstandinghappy/rexstandinghappy_00004.png"
        pause blinkingvar
        "images/characters/rexstandinghappy/rexstandinghappy_00005.png"
        pause blinkingvar
        repeat



image rexstandinglove:
    block:
        "images/characters/rexstandingloveluma/rexstandingloveluma_00000.png"
        pause lumafade
        "images/characters/rexstandingloveluma/rexstandingloveluma_00001.png"
        pause lumafade
        "images/characters/rexstandingloveluma/rexstandingloveluma_00002.png"
        pause lumafade
        "images/characters/rexstandingloveluma/rexstandingloveluma_00003.png"
        pause lumafade
        "images/characters/rexstandingloveluma/rexstandingloveluma_00004.png"
        pause lumafade
        "images/characters/rexstandingloveluma/rexstandingloveluma_00005.png"
        pause lumafade
        "images/characters/rexstandingloveluma/rexstandingloveluma_00006.png"
        pause lumafade
        "images/characters/rexstandingloveluma/rexstandingloveluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexstandinglove/rexstandinglove_00000.png"
        pause blinkingvar
        "images/characters/rexstandinglove/rexstandinglove_00001.png"
        pause blinkingvar
        "images/characters/rexstandinglove/rexstandinglove_00002.png"
        pause 0.2
        "images/characters/rexstandinglove/rexstandinglove_00003.png"
        pause blinkingvar
        "images/characters/rexstandinglove/rexstandinglove_00004.png"
        pause blinkingvar
        "images/characters/rexstandinglove/rexstandinglove_00005.png"
        pause blinkingvar
        repeat



image rexstandingangry:
    block:
        "images/characters/rexstandingangryluma/rexstandingangryluma_00000.png"
        pause lumafade
        "images/characters/rexstandingangryluma/rexstandingangryluma_00001.png"
        pause lumafade
        "images/characters/rexstandingangryluma/rexstandingangryluma_00002.png"
        pause lumafade
        "images/characters/rexstandingangryluma/rexstandingangryluma_00003.png"
        pause lumafade
        "images/characters/rexstandingangryluma/rexstandingangryluma_00004.png"
        pause lumafade
        "images/characters/rexstandingangryluma/rexstandingangryluma_00005.png"
        pause lumafade
        "images/characters/rexstandingangryluma/rexstandingangryluma_00006.png"
        pause lumafade
        "images/characters/rexstandingangryluma/rexstandingangryluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexstandingangry/rexstandingangry_00000.png"
        pause blinkingvar
        "images/characters/rexstandingangry/rexstandingangry_00001.png"
        pause blinkingvar
        "images/characters/rexstandingangry/rexstandingangry_00002.png"
        pause 0.2
        "images/characters/rexstandingangry/rexstandingangry_00003.png"
        pause blinkingvar
        "images/characters/rexstandingangry/rexstandingangry_00004.png"
        pause blinkingvar
        "images/characters/rexstandingangry/rexstandingangry_00005.png"
        pause blinkingvar
        repeat



image rexstandingpain:
    block:
        "images/characters/rexstandingpainluma/rexstandingpainluma_00000.png"
        pause lumafade
        "images/characters/rexstandingpainluma/rexstandingpainluma_00001.png"
        pause lumafade
        "images/characters/rexstandingpainluma/rexstandingpainluma_00002.png"
        pause lumafade
        "images/characters/rexstandingpainluma/rexstandingpainluma_00003.png"
        pause lumafade
        "images/characters/rexstandingpainluma/rexstandingpainluma_00004.png"
        pause lumafade
        "images/characters/rexstandingpainluma/rexstandingpainluma_00005.png"
        pause lumafade
        "images/characters/rexstandingpainluma/rexstandingpainluma_00006.png"
        pause lumafade
        "images/characters/rexstandingpainluma/rexstandingpainluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexstandingpain/rexstandingpain_00000.png"
        pause blinkingvar
        "images/characters/rexstandingpain/rexstandingpain_00001.png"
        pause blinkingvar
        "images/characters/rexstandingpain/rexstandingpain_00002.png"
        pause 0.2
        "images/characters/rexstandingpain/rexstandingpain_00003.png"
        pause blinkingvar
        "images/characters/rexstandingpain/rexstandingpain_00004.png"
        pause blinkingvar
        "images/characters/rexstandingpain/rexstandingpain_00005.png"
        pause blinkingvar
        repeat



image rexstandingregret:
    block:
        "images/characters/rexstandingregretluma/rexstandingregretluma_00000.png"
        pause lumafade
        "images/characters/rexstandingregretluma/rexstandingregretluma_00001.png"
        pause lumafade
        "images/characters/rexstandingregretluma/rexstandingregretluma_00002.png"
        pause lumafade
        "images/characters/rexstandingregretluma/rexstandingregretluma_00003.png"
        pause lumafade
        "images/characters/rexstandingregretluma/rexstandingregretluma_00004.png"
        pause lumafade
        "images/characters/rexstandingregretluma/rexstandingregretluma_00005.png"
        pause lumafade
        "images/characters/rexstandingregretluma/rexstandingregretluma_00006.png"
        pause lumafade
        "images/characters/rexstandingregretluma/rexstandingregretluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexstandingregret/rexstandingregret_00000.png"
        pause blinkingvar
        "images/characters/rexstandingregret/rexstandingregret_00001.png"
        pause blinkingvar
        "images/characters/rexstandingregret/rexstandingregret_00002.png"
        pause 0.2
        "images/characters/rexstandingregret/rexstandingregret_00003.png"
        pause blinkingvar
        "images/characters/rexstandingregret/rexstandingregret_00004.png"
        pause blinkingvar
        "images/characters/rexstandingregret/rexstandingregret_00005.png"
        pause blinkingvar
        repeat



image rexstandingsad:
    block:
        "images/characters/rexstandingsadluma/rexstandingsadluma_00000.png"
        pause lumafade
        "images/characters/rexstandingsadluma/rexstandingsadluma_00001.png"
        pause lumafade
        "images/characters/rexstandingsadluma/rexstandingsadluma_00002.png"
        pause lumafade
        "images/characters/rexstandingsadluma/rexstandingsadluma_00003.png"
        pause lumafade
        "images/characters/rexstandingsadluma/rexstandingsadluma_00004.png"
        pause lumafade
        "images/characters/rexstandingsadluma/rexstandingsadluma_00005.png"
        pause lumafade
        "images/characters/rexstandingsadluma/rexstandingsadluma_00006.png"
        pause lumafade
        "images/characters/rexstandingsadluma/rexstandingsadluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexstandingsad/rexstandingsad_00000.png"
        pause blinkingvar
        "images/characters/rexstandingsad/rexstandingsad_00001.png"
        pause blinkingvar
        "images/characters/rexstandingsad/rexstandingsad_00002.png"
        pause 0.2
        "images/characters/rexstandingsad/rexstandingsad_00003.png"
        pause blinkingvar
        "images/characters/rexstandingsad/rexstandingsad_00004.png"
        pause blinkingvar
        "images/characters/rexstandingsad/rexstandingsad_00005.png"
        pause blinkingvar
        repeat



image rexstandingserious:
    block:
        "images/characters/rexstandingseriousluma/rexstandingseriousluma_00000.png"
        pause lumafade
        "images/characters/rexstandingseriousluma/rexstandingseriousluma_00001.png"
        pause lumafade
        "images/characters/rexstandingseriousluma/rexstandingseriousluma_00002.png"
        pause lumafade
        "images/characters/rexstandingseriousluma/rexstandingseriousluma_00003.png"
        pause lumafade
        "images/characters/rexstandingseriousluma/rexstandingseriousluma_00004.png"
        pause lumafade
        "images/characters/rexstandingseriousluma/rexstandingseriousluma_00005.png"
        pause lumafade
        "images/characters/rexstandingseriousluma/rexstandingseriousluma_00006.png"
        pause lumafade
        "images/characters/rexstandingseriousluma/rexstandingseriousluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexstandingserious/rexstandingserious_00000.png"
        pause blinkingvar
        "images/characters/rexstandingserious/rexstandingserious_00001.png"
        pause blinkingvar
        "images/characters/rexstandingserious/rexstandingserious_00002.png"
        pause 0.2
        "images/characters/rexstandingserious/rexstandingserious_00003.png"
        pause blinkingvar
        "images/characters/rexstandingserious/rexstandingserious_00004.png"
        pause blinkingvar
        "images/characters/rexstandingserious/rexstandingserious_00005.png"
        pause blinkingvar
        repeat



image rexstandingshock:
    block:
        "images/characters/rexstandingshockluma/rexstandingshockluma_00000.png"
        pause lumafade
        "images/characters/rexstandingshockluma/rexstandingshockluma_00001.png"
        pause lumafade
        "images/characters/rexstandingshockluma/rexstandingshockluma_00002.png"
        pause lumafade
        "images/characters/rexstandingshockluma/rexstandingshockluma_00003.png"
        pause lumafade
        "images/characters/rexstandingshockluma/rexstandingshockluma_00004.png"
        pause lumafade
        "images/characters/rexstandingshockluma/rexstandingshockluma_00005.png"
        pause lumafade
        "images/characters/rexstandingshockluma/rexstandingshockluma_00006.png"
        pause lumafade
        "images/characters/rexstandingshockluma/rexstandingshockluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexstandingshock/rexstandingshock_00000.png"
        pause blinkingvar
        "images/characters/rexstandingshock/rexstandingshock_00001.png"
        pause blinkingvar
        "images/characters/rexstandingshock/rexstandingshock_00002.png"
        pause 0.2
        "images/characters/rexstandingshock/rexstandingshock_00003.png"
        pause blinkingvar
        "images/characters/rexstandingshock/rexstandingshock_00004.png"
        pause blinkingvar
        "images/characters/rexstandingshock/rexstandingshock_00005.png"
        pause blinkingvar
        repeat



image rexstandingsmug:
    block:
        "images/characters/rexstandingsmugluma/rexstandingsmugluma_00000.png"
        pause lumafade
        "images/characters/rexstandingsmugluma/rexstandingsmugluma_00001.png"
        pause lumafade
        "images/characters/rexstandingsmugluma/rexstandingsmugluma_00002.png"
        pause lumafade
        "images/characters/rexstandingsmugluma/rexstandingsmugluma_00003.png"
        pause lumafade
        "images/characters/rexstandingsmugluma/rexstandingsmugluma_00004.png"
        pause lumafade
        "images/characters/rexstandingsmugluma/rexstandingsmugluma_00005.png"
        pause lumafade
        "images/characters/rexstandingsmugluma/rexstandingsmugluma_00006.png"
        pause lumafade
        "images/characters/rexstandingsmugluma/rexstandingsmugluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexstandingsmug/rexstandingsmug_00000.png"
        pause blinkingvar
        "images/characters/rexstandingsmug/rexstandingsmug_00001.png"
        pause blinkingvar
        "images/characters/rexstandingsmug/rexstandingsmug_00002.png"
        pause 0.2
        "images/characters/rexstandingsmug/rexstandingsmug_00003.png"
        pause blinkingvar
        "images/characters/rexstandingsmug/rexstandingsmug_00004.png"
        pause blinkingvar
        "images/characters/rexstandingsmug/rexstandingsmug_00005.png"
        pause blinkingvar
        repeat



image rexstandingcontent:
    block:
        "images/characters/rexstandingcontentluma/rexstandingcontentluma_00000.png"
        pause lumafade
        "images/characters/rexstandingcontentluma/rexstandingcontentluma_00001.png"
        pause lumafade
        "images/characters/rexstandingcontentluma/rexstandingcontentluma_00002.png"
        pause lumafade
        "images/characters/rexstandingcontentluma/rexstandingcontentluma_00003.png"
        pause lumafade
        "images/characters/rexstandingcontentluma/rexstandingcontentluma_00004.png"
        pause lumafade
        "images/characters/rexstandingcontentluma/rexstandingcontentluma_00005.png"
        pause lumafade
        "images/characters/rexstandingcontentluma/rexstandingcontentluma_00006.png"
        pause lumafade
        "images/characters/rexstandingcontentluma/rexstandingcontentluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexstandingcontent/rexstandingcontent_00000.png"
        pause blinkingvar
        "images/characters/rexstandingcontent/rexstandingcontent_00001.png"
        pause blinkingvar
        "images/characters/rexstandingcontent/rexstandingcontent_00002.png"
        pause 0.2
        "images/characters/rexstandingcontent/rexstandingcontent_00003.png"
        pause blinkingvar
        "images/characters/rexstandingcontent/rexstandingcontent_00004.png"
        pause blinkingvar
        "images/characters/rexstandingcontent/rexstandingcontent_00005.png"
        pause blinkingvar
        repeat


# 1373,1406s/mina/mfm/g

image minastandingneutral:
    block:
        "images/characters/minaneutralluma/minaneutralluma_00000.png"
        pause lumafade
        "images/characters/minaneutralluma/minaneutralluma_00001.png"
        pause lumafade
        "images/characters/minaneutralluma/minaneutralluma_00002.png"
        pause lumafade
        "images/characters/minaneutralluma/minaneutralluma_00003.png"
        pause lumafade
        "images/characters/minaneutralluma/minaneutralluma_00004.png"
        pause lumafade
        "images/characters/minaneutralluma/minaneutralluma_00005.png"
        pause lumafade
        "images/characters/minaneutralluma/minaneutralluma_00006.png"
        pause lumafade
        "images/characters/minaneutralluma/minaneutralluma_00007.png"
        pause lumafade
    block:
        "images/characters/minastandingneutral/minastandingneutral_00000.png"
        pause blinkingvar
        "images/characters/minastandingneutral/minastandingneutral_00001.png"
        pause blinkingvar
        "images/characters/minastandingneutral/minastandingneutral_00002.png"
        pause 0.2
        "images/characters/minastandingneutral/minastandingneutral_00003.png"
        pause blinkingvar
        "images/characters/minastandingneutral/minastandingneutral_00004.png"
        pause blinkingvar
        "images/characters/minastandingneutral/minastandingneutral_00005.png"
        pause blinkingvar
        repeat

image minastandinghappy:
    block:
        "images/characters/minahappyluma/minahappyluma_00000.png"
        pause lumafade
        "images/characters/minahappyluma/minahappyluma_00001.png"
        pause lumafade
        "images/characters/minahappyluma/minahappyluma_00002.png"
        pause lumafade
        "images/characters/minahappyluma/minahappyluma_00003.png"
        pause lumafade
        "images/characters/minahappyluma/minahappyluma_00004.png"
        pause lumafade
        "images/characters/minahappyluma/minahappyluma_00005.png"
        pause lumafade
        "images/characters/minahappyluma/minahappyluma_00006.png"
        pause lumafade
        "images/characters/minahappyluma/minahappyluma_00007.png"
        pause lumafade
    block:
        "images/characters/minastandinghappy/minastandinghappy_00000.png"
        pause blinkingvar
        "images/characters/minastandinghappy/minastandinghappy_00001.png"
        pause blinkingvar
        "images/characters/minastandinghappy/minastandinghappy_00002.png"
        pause 0.2
        "images/characters/minastandinghappy/minastandinghappy_00003.png"
        pause blinkingvar
        "images/characters/minastandinghappy/minastandinghappy_00004.png"
        pause blinkingvar
        "images/characters/minastandinghappy/minastandinghappy_00005.png"
        pause blinkingvar
        repeat

image minastandingangry:
    block:
        "images/characters/minaangryluma/minaangryluma_00000.png"
        pause lumafade
        "images/characters/minaangryluma/minaangryluma_00001.png"
        pause lumafade
        "images/characters/minaangryluma/minaangryluma_00002.png"
        pause lumafade
        "images/characters/minaangryluma/minaangryluma_00003.png"
        pause lumafade
        "images/characters/minaangryluma/minaangryluma_00004.png"
        pause lumafade
        "images/characters/minaangryluma/minaangryluma_00005.png"
        pause lumafade
        "images/characters/minaangryluma/minaangryluma_00006.png"
        pause lumafade
        "images/characters/minaangryluma/minaangryluma_00007.png"
        pause lumafade
    block:
        "images/characters/minastandingangry/minastandingangry_00000.png"
        pause blinkingvar
        "images/characters/minastandingangry/minastandingangry_00001.png"
        pause blinkingvar
        "images/characters/minastandingangry/minastandingangry_00002.png"
        pause 0.2
        "images/characters/minastandingangry/minastandingangry_00003.png"
        pause blinkingvar
        "images/characters/minastandingangry/minastandingangry_00004.png"
        pause blinkingvar
        "images/characters/minastandingangry/minastandingangry_00005.png"
        pause blinkingvar
        repeat

image minastandingpain:
    block:
        "images/characters/minapainluma/minapainluma_00000.png"
        pause lumafade
        "images/characters/minapainluma/minapainluma_00001.png"
        pause lumafade
        "images/characters/minapainluma/minapainluma_00002.png"
        pause lumafade
        "images/characters/minapainluma/minapainluma_00003.png"
        pause lumafade
        "images/characters/minapainluma/minapainluma_00004.png"
        pause lumafade
        "images/characters/minapainluma/minapainluma_00005.png"
        pause lumafade
        "images/characters/minapainluma/minapainluma_00006.png"
        pause lumafade
        "images/characters/minapainluma/minapainluma_00007.png"
        pause lumafade
    block:
        "images/characters/minastandingpain/minastandingpain_00000.png"
        pause blinkingvar
        "images/characters/minastandingpain/minastandingpain_00001.png"
        pause blinkingvar
        "images/characters/minastandingpain/minastandingpain_00002.png"
        pause 0.2
        "images/characters/minastandingpain/minastandingpain_00003.png"
        pause blinkingvar
        "images/characters/minastandingpain/minastandingpain_00004.png"
        pause blinkingvar
        "images/characters/minastandingpain/minastandingpain_00005.png"
        pause blinkingvar
        repeat

image minastandingregret:
    block:
        "images/characters/minaregretluma/minaregretluma_00000.png"
        pause lumafade
        "images/characters/minaregretluma/minaregretluma_00001.png"
        pause lumafade
        "images/characters/minaregretluma/minaregretluma_00002.png"
        pause lumafade
        "images/characters/minaregretluma/minaregretluma_00003.png"
        pause lumafade
        "images/characters/minaregretluma/minaregretluma_00004.png"
        pause lumafade
        "images/characters/minaregretluma/minaregretluma_00005.png"
        pause lumafade
        "images/characters/minaregretluma/minaregretluma_00006.png"
        pause lumafade
        "images/characters/minaregretluma/minaregretluma_00007.png"
        pause lumafade
    block:
        "images/characters/minastandingregret/minastandingregret_00000.png"
        pause blinkingvar
        "images/characters/minastandingregret/minastandingregret_00001.png"
        pause blinkingvar
        "images/characters/minastandingregret/minastandingregret_00002.png"
        pause 0.2
        "images/characters/minastandingregret/minastandingregret_00003.png"
        pause blinkingvar
        "images/characters/minastandingregret/minastandingregret_00004.png"
        pause blinkingvar
        "images/characters/minastandingregret/minastandingregret_00005.png"
        pause blinkingvar
        repeat

image minastandingsad:
    block:
        "images/characters/minasadluma/minasadluma_00000.png"
        pause lumafade
        "images/characters/minasadluma/minasadluma_00001.png"
        pause lumafade
        "images/characters/minasadluma/minasadluma_00002.png"
        pause lumafade
        "images/characters/minasadluma/minasadluma_00003.png"
        pause lumafade
        "images/characters/minasadluma/minasadluma_00004.png"
        pause lumafade
        "images/characters/minasadluma/minasadluma_00005.png"
        pause lumafade
        "images/characters/minasadluma/minasadluma_00006.png"
        pause lumafade
        "images/characters/minasadluma/minasadluma_00007.png"
        pause lumafade
    block:
        "images/characters/minastandingsad/minastandingsad_00000.png"
        pause blinkingvar
        "images/characters/minastandingsad/minastandingsad_00001.png"
        pause blinkingvar
        "images/characters/minastandingsad/minastandingsad_00002.png"
        pause 0.2
        "images/characters/minastandingsad/minastandingsad_00003.png"
        pause blinkingvar
        "images/characters/minastandingsad/minastandingsad_00004.png"
        pause blinkingvar
        "images/characters/minastandingsad/minastandingsad_00005.png"
        pause blinkingvar
        repeat

image minastandingserious:
    block:
        "images/characters/minaseriousluma/minaseriousluma_00000.png"
        pause lumafade
        "images/characters/minaseriousluma/minaseriousluma_00001.png"
        pause lumafade
        "images/characters/minaseriousluma/minaseriousluma_00002.png"
        pause lumafade
        "images/characters/minaseriousluma/minaseriousluma_00003.png"
        pause lumafade
        "images/characters/minaseriousluma/minaseriousluma_00004.png"
        pause lumafade
        "images/characters/minaseriousluma/minaseriousluma_00005.png"
        pause lumafade
        "images/characters/minaseriousluma/minaseriousluma_00006.png"
        pause lumafade
        "images/characters/minaseriousluma/minaseriousluma_00007.png"
        pause lumafade
    block:
        "images/characters/minastandingserious/minastandingserious_00000.png"
        pause blinkingvar
        "images/characters/minastandingserious/minastandingserious_00001.png"
        pause blinkingvar
        "images/characters/minastandingserious/minastandingserious_00002.png"
        pause 0.2
        "images/characters/minastandingserious/minastandingserious_00003.png"
        pause blinkingvar
        "images/characters/minastandingserious/minastandingserious_00004.png"
        pause blinkingvar
        "images/characters/minastandingserious/minastandingserious_00005.png"
        pause blinkingvar
        repeat

image minastandingshock:
    block:
        "images/characters/minashockluma/minashockluma_00000.png"
        pause lumafade
        "images/characters/minashockluma/minashockluma_00001.png"
        pause lumafade
        "images/characters/minashockluma/minashockluma_00002.png"
        pause lumafade
        "images/characters/minashockluma/minashockluma_00003.png"
        pause lumafade
        "images/characters/minashockluma/minashockluma_00004.png"
        pause lumafade
        "images/characters/minashockluma/minashockluma_00005.png"
        pause lumafade
        "images/characters/minashockluma/minashockluma_00006.png"
        pause lumafade
        "images/characters/minashockluma/minashockluma_00007.png"
        pause lumafade
    block:
        "images/characters/minastandingshock/minastandingshock_00000.png"
        pause blinkingvar
        "images/characters/minastandingshock/minastandingshock_00001.png"
        pause blinkingvar
        "images/characters/minastandingshock/minastandingshock_00002.png"
        pause 0.2
        "images/characters/minastandingshock/minastandingshock_00003.png"
        pause blinkingvar
        "images/characters/minastandingshock/minastandingshock_00004.png"
        pause blinkingvar
        "images/characters/minastandingshock/minastandingshock_00005.png"
        pause blinkingvar
        repeat

image minastandingsmug:
    block:
        "images/characters/minasmugluma/minasmugluma_00000.png"
        pause lumafade
        "images/characters/minasmugluma/minasmugluma_00001.png"
        pause lumafade
        "images/characters/minasmugluma/minasmugluma_00002.png"
        pause lumafade
        "images/characters/minasmugluma/minasmugluma_00003.png"
        pause lumafade
        "images/characters/minasmugluma/minasmugluma_00004.png"
        pause lumafade
        "images/characters/minasmugluma/minasmugluma_00005.png"
        pause lumafade
        "images/characters/minasmugluma/minasmugluma_00006.png"
        pause lumafade
        "images/characters/minasmugluma/minasmugluma_00007.png"
        pause lumafade
    block:
        "images/characters/minastandingsmug/minastandingsmug_00000.png"
        pause blinkingvar
        "images/characters/minastandingsmug/minastandingsmug_00001.png"
        pause blinkingvar
        "images/characters/minastandingsmug/minastandingsmug_00002.png"
        pause 0.2
        "images/characters/minastandingsmug/minastandingsmug_00003.png"
        pause blinkingvar
        "images/characters/minastandingsmug/minastandingsmug_00004.png"
        pause blinkingvar
        "images/characters/minastandingsmug/minastandingsmug_00005.png"
        pause blinkingvar
        repeat

image minastandingcontent:
    block:
        "images/characters/minacontentluma/minacontentluma_00000.png"
        pause lumafade
        "images/characters/minacontentluma/minacontentluma_00001.png"
        pause lumafade
        "images/characters/minacontentluma/minacontentluma_00002.png"
        pause lumafade
        "images/characters/minacontentluma/minacontentluma_00003.png"
        pause lumafade
        "images/characters/minacontentluma/minacontentluma_00004.png"
        pause lumafade
        "images/characters/minacontentluma/minacontentluma_00005.png"
        pause lumafade
        "images/characters/minacontentluma/minacontentluma_00006.png"
        pause lumafade
        "images/characters/minacontentluma/minacontentluma_00007.png"
        pause lumafade
    block:
        "images/characters/minastandingcontent/minastandingcontent_00000.png"
        pause blinkingvar
        "images/characters/minastandingcontent/minastandingcontent_00001.png"
        pause blinkingvar
        "images/characters/minastandingcontent/minastandingcontent_00002.png"
        pause 0.2
        "images/characters/minastandingcontent/minastandingcontent_00003.png"
        pause blinkingvar
        "images/characters/minastandingcontent/minastandingcontent_00004.png"
        pause blinkingvar
        "images/characters/minastandingcontent/minastandingcontent_00005.png"
        pause blinkingvar
        repeat

image minastandinglove:
    block:
        "images/characters/minaloveluma/minaloveluma_00000.png"
        pause lumafade
        "images/characters/minaloveluma/minaloveluma_00001.png"
        pause lumafade
        "images/characters/minaloveluma/minaloveluma_00002.png"
        pause lumafade
        "images/characters/minaloveluma/minaloveluma_00003.png"
        pause lumafade
        "images/characters/minaloveluma/minaloveluma_00004.png"
        pause lumafade
        "images/characters/minaloveluma/minaloveluma_00005.png"
        pause lumafade
        "images/characters/minaloveluma/minaloveluma_00006.png"
        pause lumafade
        "images/characters/minaloveluma/minaloveluma_00007.png"
        pause lumafade
    block:
        "images/characters/minastandinglove/minastandinglove_00000.png"
        pause blinkingvar
        "images/characters/minastandinglove/minastandinglove_00001.png"
        pause blinkingvar
        "images/characters/minastandinglove/minastandinglove_00002.png"
        pause 0.2
        "images/characters/minastandinglove/minastandinglove_00003.png"
        pause blinkingvar
        "images/characters/minastandinglove/minastandinglove_00004.png"
        pause blinkingvar
        "images/characters/minastandinglove/minastandinglove_00005.png"
        pause blinkingvar
        repeat


##########
#####
###
#
#
# CHARACTERS - ZOOM
#
#
##
###
#####
##########

image rexzoomneutral:
    block:
        "images/characters/rexzoomneutralluma/rexzoomneutralluma_00000.png"
        pause lumafade
        "images/characters/rexzoomneutralluma/rexzoomneutralluma_00001.png"
        pause lumafade
        "images/characters/rexzoomneutralluma/rexzoomneutralluma_00002.png"
        pause lumafade
        "images/characters/rexzoomneutralluma/rexzoomneutralluma_00003.png"
        pause lumafade
        "images/characters/rexzoomneutralluma/rexzoomneutralluma_00004.png"
        pause lumafade
        "images/characters/rexzoomneutralluma/rexzoomneutralluma_00005.png"
        pause lumafade
        "images/characters/rexzoomneutralluma/rexzoomneutralluma_00006.png"
        pause lumafade
        "images/characters/rexzoomneutralluma/rexzoomneutralluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexzoomneutral/rexzoomneutral_00000.png"
        pause blinkingvar
        "images/characters/rexzoomneutral/rexzoomneutral_00001.png"
        pause blinkingvar
        "images/characters/rexzoomneutral/rexzoomneutral_00002.png"
        pause 0.2
        "images/characters/rexzoomneutral/rexzoomneutral_00003.png"
        pause blinkingvar
        "images/characters/rexzoomneutral/rexzoomneutral_00004.png"
        pause blinkingvar
        "images/characters/rexzoomneutral/rexzoomneutral_00005.png"
        pause blinkingvar
        repeat


image rexzoomhappy:
    block:
        "images/characters/rexzoomhappyluma/rexzoomhappyluma_00000.png"
        pause lumafade
        "images/characters/rexzoomhappyluma/rexzoomhappyluma_00001.png"
        pause lumafade
        "images/characters/rexzoomhappyluma/rexzoomhappyluma_00002.png"
        pause lumafade
        "images/characters/rexzoomhappyluma/rexzoomhappyluma_00003.png"
        pause lumafade
        "images/characters/rexzoomhappyluma/rexzoomhappyluma_00004.png"
        pause lumafade
        "images/characters/rexzoomhappyluma/rexzoomhappyluma_00005.png"
        pause lumafade
        "images/characters/rexzoomhappyluma/rexzoomhappyluma_00006.png"
        pause lumafade
        "images/characters/rexzoomhappyluma/rexzoomhappyluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexzoomhappy/rexzoomhappy_00000.png"
        pause blinkingvar
        "images/characters/rexzoomhappy/rexzoomhappy_00001.png"
        pause blinkingvar
        "images/characters/rexzoomhappy/rexzoomhappy_00002.png"
        pause 0.2
        "images/characters/rexzoomhappy/rexzoomhappy_00003.png"
        pause blinkingvar
        "images/characters/rexzoomhappy/rexzoomhappy_00004.png"
        pause blinkingvar
        "images/characters/rexzoomhappy/rexzoomhappy_00005.png"
        pause blinkingvar
        repeat



image rexzoomangry:
    block:
        "images/characters/rexzoomangryluma/rexzoomangryluma_00000.png"
        pause lumafade
        "images/characters/rexzoomangryluma/rexzoomangryluma_00001.png"
        pause lumafade
        "images/characters/rexzoomangryluma/rexzoomangryluma_00002.png"
        pause lumafade
        "images/characters/rexzoomangryluma/rexzoomangryluma_00003.png"
        pause lumafade
        "images/characters/rexzoomangryluma/rexzoomangryluma_00004.png"
        pause lumafade
        "images/characters/rexzoomangryluma/rexzoomangryluma_00005.png"
        pause lumafade
        "images/characters/rexzoomangryluma/rexzoomangryluma_00006.png"
        pause lumafade
        "images/characters/rexzoomangryluma/rexzoomangryluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexzoomangry/rexzoomangry_00000.png"
        pause blinkingvar
        "images/characters/rexzoomangry/rexzoomangry_00001.png"
        pause blinkingvar
        "images/characters/rexzoomangry/rexzoomangry_00002.png"
        pause 0.2
        "images/characters/rexzoomangry/rexzoomangry_00003.png"
        pause blinkingvar
        "images/characters/rexzoomangry/rexzoomangry_00004.png"
        pause blinkingvar
        "images/characters/rexzoomangry/rexzoomangry_00005.png"
        pause blinkingvar
        repeat



image rexzoompain:
    block:
        "images/characters/rexzoompainluma/rexzoompainluma_00000.png"
        pause lumafade
        "images/characters/rexzoompainluma/rexzoompainluma_00001.png"
        pause lumafade
        "images/characters/rexzoompainluma/rexzoompainluma_00002.png"
        pause lumafade
        "images/characters/rexzoompainluma/rexzoompainluma_00003.png"
        pause lumafade
        "images/characters/rexzoompainluma/rexzoompainluma_00004.png"
        pause lumafade
        "images/characters/rexzoompainluma/rexzoompainluma_00005.png"
        pause lumafade
        "images/characters/rexzoompainluma/rexzoompainluma_00006.png"
        pause lumafade
        "images/characters/rexzoompainluma/rexzoompainluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexzoompain/rexzoompain_00000.png"
        pause blinkingvar
        "images/characters/rexzoompain/rexzoompain_00001.png"
        pause blinkingvar
        "images/characters/rexzoompain/rexzoompain_00002.png"
        pause 0.2
        "images/characters/rexzoompain/rexzoompain_00003.png"
        pause blinkingvar
        "images/characters/rexzoompain/rexzoompain_00004.png"
        pause blinkingvar
        "images/characters/rexzoompain/rexzoompain_00005.png"
        pause blinkingvar
        repeat



image rexzoomregret:
    block:
        "images/characters/rexzoomregretluma/rexzoomregretluma_00000.png"
        pause lumafade
        "images/characters/rexzoomregretluma/rexzoomregretluma_00001.png"
        pause lumafade
        "images/characters/rexzoomregretluma/rexzoomregretluma_00002.png"
        pause lumafade
        "images/characters/rexzoomregretluma/rexzoomregretluma_00003.png"
        pause lumafade
        "images/characters/rexzoomregretluma/rexzoomregretluma_00004.png"
        pause lumafade
        "images/characters/rexzoomregretluma/rexzoomregretluma_00005.png"
        pause lumafade
        "images/characters/rexzoomregretluma/rexzoomregretluma_00006.png"
        pause lumafade
        "images/characters/rexzoomregretluma/rexzoomregretluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexzoomregret/rexzoomregret_00000.png"
        pause blinkingvar
        "images/characters/rexzoomregret/rexzoomregret_00001.png"
        pause blinkingvar
        "images/characters/rexzoomregret/rexzoomregret_00002.png"
        pause 0.2
        "images/characters/rexzoomregret/rexzoomregret_00003.png"
        pause blinkingvar
        "images/characters/rexzoomregret/rexzoomregret_00004.png"
        pause blinkingvar
        "images/characters/rexzoomregret/rexzoomregret_00005.png"
        pause blinkingvar
        repeat


image rexzoomsad:
    block:
        "images/characters/rexzoomsadluma/rexzoomsadluma_00000.png"
        pause lumafade
        "images/characters/rexzoomsadluma/rexzoomsadluma_00001.png"
        pause lumafade
        "images/characters/rexzoomsadluma/rexzoomsadluma_00002.png"
        pause lumafade
        "images/characters/rexzoomsadluma/rexzoomsadluma_00003.png"
        pause lumafade
        "images/characters/rexzoomsadluma/rexzoomsadluma_00004.png"
        pause lumafade
        "images/characters/rexzoomsadluma/rexzoomsadluma_00005.png"
        pause lumafade
        "images/characters/rexzoomsadluma/rexzoomsadluma_00006.png"
        pause lumafade
        "images/characters/rexzoomsadluma/rexzoomsadluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexzoomsad/rexzoomsad_00000.png"
        pause blinkingvar
        "images/characters/rexzoomsad/rexzoomsad_00001.png"
        pause blinkingvar
        "images/characters/rexzoomsad/rexzoomsad_00002.png"
        pause 0.2
        "images/characters/rexzoomsad/rexzoomsad_00003.png"
        pause blinkingvar
        "images/characters/rexzoomsad/rexzoomsad_00004.png"
        pause blinkingvar
        "images/characters/rexzoomsad/rexzoomsad_00005.png"
        pause blinkingvar
        repeat



image rexzoomserious:
    block:
        "images/characters/rexzoomseriousluma/rexzoomseriousluma_00000.png"
        pause lumafade
        "images/characters/rexzoomseriousluma/rexzoomseriousluma_00001.png"
        pause lumafade
        "images/characters/rexzoomseriousluma/rexzoomseriousluma_00002.png"
        pause lumafade
        "images/characters/rexzoomseriousluma/rexzoomseriousluma_00003.png"
        pause lumafade
        "images/characters/rexzoomseriousluma/rexzoomseriousluma_00004.png"
        pause lumafade
        "images/characters/rexzoomseriousluma/rexzoomseriousluma_00005.png"
        pause lumafade
        "images/characters/rexzoomseriousluma/rexzoomseriousluma_00006.png"
        pause lumafade
        "images/characters/rexzoomseriousluma/rexzoomseriousluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexzoomserious/rexzoomserious_00000.png"
        pause blinkingvar
        "images/characters/rexzoomserious/rexzoomserious_00001.png"
        pause blinkingvar
        "images/characters/rexzoomserious/rexzoomserious_00002.png"
        pause 0.2
        "images/characters/rexzoomserious/rexzoomserious_00003.png"
        pause blinkingvar
        "images/characters/rexzoomserious/rexzoomserious_00004.png"
        pause blinkingvar
        "images/characters/rexzoomserious/rexzoomserious_00005.png"
        pause blinkingvar
        repeat


image rexzoomshock:
    block:
        "images/characters/rexzoomshockluma/rexzoomshockluma_00000.png"
        pause lumafade
        "images/characters/rexzoomshockluma/rexzoomshockluma_00001.png"
        pause lumafade
        "images/characters/rexzoomshockluma/rexzoomshockluma_00002.png"
        pause lumafade
        "images/characters/rexzoomshockluma/rexzoomshockluma_00003.png"
        pause lumafade
        "images/characters/rexzoomshockluma/rexzoomshockluma_00004.png"
        pause lumafade
        "images/characters/rexzoomshockluma/rexzoomshockluma_00005.png"
        pause lumafade
        "images/characters/rexzoomshockluma/rexzoomshockluma_00006.png"
        pause lumafade
        "images/characters/rexzoomshockluma/rexzoomshockluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexzoomshock/rexzoomshock_00000.png"
        pause blinkingvar
        "images/characters/rexzoomshock/rexzoomshock_00001.png"
        pause blinkingvar
        "images/characters/rexzoomshock/rexzoomshock_00002.png"
        pause 0.2
        "images/characters/rexzoomshock/rexzoomshock_00003.png"
        pause blinkingvar
        "images/characters/rexzoomshock/rexzoomshock_00004.png"
        pause blinkingvar
        "images/characters/rexzoomshock/rexzoomshock_00005.png"
        pause blinkingvar
        repeat


image rexzoomsmug:
    block:
        "images/characters/rexzoomsmugluma/rexzoomsmugluma_00000.png"
        pause lumafade
        "images/characters/rexzoomsmugluma/rexzoomsmugluma_00001.png"
        pause lumafade
        "images/characters/rexzoomsmugluma/rexzoomsmugluma_00002.png"
        pause lumafade
        "images/characters/rexzoomsmugluma/rexzoomsmugluma_00003.png"
        pause lumafade
        "images/characters/rexzoomsmugluma/rexzoomsmugluma_00004.png"
        pause lumafade
        "images/characters/rexzoomsmugluma/rexzoomsmugluma_00005.png"
        pause lumafade
        "images/characters/rexzoomsmugluma/rexzoomsmugluma_00006.png"
        pause lumafade
        "images/characters/rexzoomsmugluma/rexzoomsmugluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexzoomsmug/rexzoomsmug_00000.png"
        pause blinkingvar
        "images/characters/rexzoomsmug/rexzoomsmug_00001.png"
        pause blinkingvar
        "images/characters/rexzoomsmug/rexzoomsmug_00002.png"
        pause 0.2
        "images/characters/rexzoomsmug/rexzoomsmug_00003.png"
        pause blinkingvar
        "images/characters/rexzoomsmug/rexzoomsmug_00004.png"
        pause blinkingvar
        "images/characters/rexzoomsmug/rexzoomsmug_00005.png"
        pause blinkingvar
        repeat


image rexzoomcontent:
    block:
        "images/characters/rexzoomcontentluma/rexzoomcontentluma_00000.png"
        pause lumafade
        "images/characters/rexzoomcontentluma/rexzoomcontentluma_00001.png"
        pause lumafade
        "images/characters/rexzoomcontentluma/rexzoomcontentluma_00002.png"
        pause lumafade
        "images/characters/rexzoomcontentluma/rexzoomcontentluma_00003.png"
        pause lumafade
        "images/characters/rexzoomcontentluma/rexzoomcontentluma_00004.png"
        pause lumafade
        "images/characters/rexzoomcontentluma/rexzoomcontentluma_00005.png"
        pause lumafade
        "images/characters/rexzoomcontentluma/rexzoomcontentluma_00006.png"
        pause lumafade
        "images/characters/rexzoomcontentluma/rexzoomcontentluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexzoomcontent/rexzoomcontent_00000.png"
        pause blinkingvar
        "images/characters/rexzoomcontent/rexzoomcontent_00001.png"
        pause blinkingvar
        "images/characters/rexzoomcontent/rexzoomcontent_00002.png"
        pause 0.2
        "images/characters/rexzoomcontent/rexzoomcontent_00003.png"
        pause blinkingvar
        "images/characters/rexzoomcontent/rexzoomcontent_00004.png"
        pause blinkingvar
        "images/characters/rexzoomcontent/rexzoomcontent_00005.png"
        pause blinkingvar
        repeat


image rexzoomlove:
    block:
        "images/characters/rexzoomloveluma/rexzoomloveluma_00000.png"
        pause lumafade
        "images/characters/rexzoomloveluma/rexzoomloveluma_00001.png"
        pause lumafade
        "images/characters/rexzoomloveluma/rexzoomloveluma_00002.png"
        pause lumafade
        "images/characters/rexzoomloveluma/rexzoomloveluma_00003.png"
        pause lumafade
        "images/characters/rexzoomloveluma/rexzoomloveluma_00004.png"
        pause lumafade
        "images/characters/rexzoomloveluma/rexzoomloveluma_00005.png"
        pause lumafade
        "images/characters/rexzoomloveluma/rexzoomloveluma_00006.png"
        pause lumafade
        "images/characters/rexzoomloveluma/rexzoomloveluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexzoomlove/rexzoomlove_00000.png"
        pause blinkingvar
        "images/characters/rexzoomlove/rexzoomlove_00001.png"
        pause blinkingvar
        "images/characters/rexzoomlove/rexzoomlove_00002.png"
        pause 0.2
        "images/characters/rexzoomlove/rexzoomlove_00003.png"
        pause blinkingvar
        "images/characters/rexzoomlove/rexzoomlove_00004.png"
        pause blinkingvar
        "images/characters/rexzoomlove/rexzoomlove_00005.png"
        pause blinkingvar
        repeat


image minazoomlove: 
    block:
        "images/characters/minazoomloveluma/minazoomloveluma_00000.png"
        pause lumafade
        "images/characters/minazoomloveluma/minazoomloveluma_00001.png"
        pause lumafade
        "images/characters/minazoomloveluma/minazoomloveluma_00002.png"
        pause lumafade
        "images/characters/minazoomloveluma/minazoomloveluma_00003.png"
        pause lumafade
        "images/characters/minazoomloveluma/minazoomloveluma_00004.png"
        pause lumafade
        "images/characters/minazoomloveluma/minazoomloveluma_00005.png"
        pause lumafade
        "images/characters/minazoomloveluma/minazoomloveluma_00006.png"
        pause lumafade
        "images/characters/minazoomloveluma/minazoomloveluma_00007.png"
        pause lumafade
    block:
        "images/characters/minazoomlove/minazoomlove_00000.png"
        pause blinkingvar
        "images/characters/minazoomlove/minazoomlove_00001.png"
        pause blinkingvar
        "images/characters/minazoomlove/minazoomlove_00002.png"
        pause 0.2
        "images/characters/minazoomlove/minazoomlove_00003.png"
        pause blinkingvar
        "images/characters/minazoomlove/minazoomlove_00004.png"
        pause blinkingvar
        "images/characters/minazoomlove/minazoomlove_00005.png"
        pause blinkingvar
        repeat



image minazoomhappy:
    block:
        "images/characters/minazoomhappyluma/minazoomhappyluma_00000.png"
        pause lumafade
        "images/characters/minazoomhappyluma/minazoomhappyluma_00001.png"
        pause lumafade
        "images/characters/minazoomhappyluma/minazoomhappyluma_00002.png"
        pause lumafade
        "images/characters/minazoomhappyluma/minazoomhappyluma_00003.png"
        pause lumafade
        "images/characters/minazoomhappyluma/minazoomhappyluma_00004.png"
        pause lumafade
        "images/characters/minazoomhappyluma/minazoomhappyluma_00005.png"
        pause lumafade
        "images/characters/minazoomhappyluma/minazoomhappyluma_00006.png"
        pause lumafade
        "images/characters/minazoomhappyluma/minazoomhappyluma_00007.png"
        pause lumafade
    block:
        "images/characters/minazoomhappy/minazoomhappy_00000.png"
        pause blinkingvar
        "images/characters/minazoomhappy/minazoomhappy_00001.png"
        pause blinkingvar
        "images/characters/minazoomhappy/minazoomhappy_00002.png"
        pause 0.2
        "images/characters/minazoomhappy/minazoomhappy_00003.png"
        pause blinkingvar
        "images/characters/minazoomhappy/minazoomhappy_00004.png"
        pause blinkingvar
        "images/characters/minazoomhappy/minazoomhappy_00005.png"
        pause blinkingvar
        repeat



image minazoomangry:
    block:
        "images/characters/minazoomangryluma/minazoomangryluma_00000.png"
        pause lumafade
        "images/characters/minazoomangryluma/minazoomangryluma_00001.png"
        pause lumafade
        "images/characters/minazoomangryluma/minazoomangryluma_00002.png"
        pause lumafade
        "images/characters/minazoomangryluma/minazoomangryluma_00003.png"
        pause lumafade
        "images/characters/minazoomangryluma/minazoomangryluma_00004.png"
        pause lumafade
        "images/characters/minazoomangryluma/minazoomangryluma_00005.png"
        pause lumafade
        "images/characters/minazoomangryluma/minazoomangryluma_00006.png"
        pause lumafade
        "images/characters/minazoomangryluma/minazoomangryluma_00007.png"
        pause lumafade
    block:
        "images/characters/minazoomangry/minazoomangry_00000.png"
        pause blinkingvar
        "images/characters/minazoomangry/minazoomangry_00001.png"
        pause blinkingvar
        "images/characters/minazoomangry/minazoomangry_00002.png"
        pause 0.2
        "images/characters/minazoomangry/minazoomangry_00003.png"
        pause blinkingvar
        "images/characters/minazoomangry/minazoomangry_00004.png"
        pause blinkingvar
        "images/characters/minazoomangry/minazoomangry_00005.png"
        pause blinkingvar
        repeat



image minazoompain:
    block:
        "images/characters/minazoompainluma/minazoompainluma_00000.png"
        pause lumafade
        "images/characters/minazoompainluma/minazoompainluma_00001.png"
        pause lumafade
        "images/characters/minazoompainluma/minazoompainluma_00002.png"
        pause lumafade
        "images/characters/minazoompainluma/minazoompainluma_00003.png"
        pause lumafade
        "images/characters/minazoompainluma/minazoompainluma_00004.png"
        pause lumafade
        "images/characters/minazoompainluma/minazoompainluma_00005.png"
        pause lumafade
        "images/characters/minazoompainluma/minazoompainluma_00006.png"
        pause lumafade
        "images/characters/minazoompainluma/minazoompainluma_00007.png"
        pause lumafade
    block:
        "images/characters/minazoompain/minazoompain_00000.png"
        pause blinkingvar
        "images/characters/minazoompain/minazoompain_00001.png"
        pause blinkingvar
        "images/characters/minazoompain/minazoompain_00002.png"
        pause 0.2
        "images/characters/minazoompain/minazoompain_00003.png"
        pause blinkingvar
        "images/characters/minazoompain/minazoompain_00004.png"
        pause blinkingvar
        "images/characters/minazoompain/minazoompain_00005.png"
        pause blinkingvar
        repeat

image minazoomregret:
    block:
        "images/characters/minazoomregretluma/minazoomregretluma_00000.png"
        pause lumafade
        "images/characters/minazoomregretluma/minazoomregretluma_00001.png"
        pause lumafade
        "images/characters/minazoomregretluma/minazoomregretluma_00002.png"
        pause lumafade
        "images/characters/minazoomregretluma/minazoomregretluma_00003.png"
        pause lumafade
        "images/characters/minazoomregretluma/minazoomregretluma_00004.png"
        pause lumafade
        "images/characters/minazoomregretluma/minazoomregretluma_00005.png"
        pause lumafade
        "images/characters/minazoomregretluma/minazoomregretluma_00006.png"
        pause lumafade
        "images/characters/minazoomregretluma/minazoomregretluma_00007.png"
        pause lumafade
    block:
        "images/characters/minazoomregret/minazoomregret_00000.png"
        pause blinkingvar
        "images/characters/minazoomregret/minazoomregret_00001.png"
        pause blinkingvar
        "images/characters/minazoomregret/minazoomregret_00002.png"
        pause 0.2
        "images/characters/minazoomregret/minazoomregret_00003.png"
        pause blinkingvar
        "images/characters/minazoomregret/minazoomregret_00004.png"
        pause blinkingvar
        "images/characters/minazoomregret/minazoomregret_00005.png"
        pause blinkingvar
        repeat

image minazoomsad:
    block:
        "images/characters/minazoomsadluma/minazoomsadluma_00000.png"
        pause lumafade
        "images/characters/minazoomsadluma/minazoomsadluma_00001.png"
        pause lumafade
        "images/characters/minazoomsadluma/minazoomsadluma_00002.png"
        pause lumafade
        "images/characters/minazoomsadluma/minazoomsadluma_00003.png"
        pause lumafade
        "images/characters/minazoomsadluma/minazoomsadluma_00004.png"
        pause lumafade
        "images/characters/minazoomsadluma/minazoomsadluma_00005.png"
        pause lumafade
        "images/characters/minazoomsadluma/minazoomsadluma_00006.png"
        pause lumafade
        "images/characters/minazoomsadluma/minazoomsadluma_00007.png"
        pause lumafade
    block:
        "images/characters/minazoomsad/minazoomsad_00000.png"
        pause blinkingvar
        "images/characters/minazoomsad/minazoomsad_00001.png"
        pause blinkingvar
        "images/characters/minazoomsad/minazoomsad_00002.png"
        pause 0.2
        "images/characters/minazoomsad/minazoomsad_00003.png"
        pause blinkingvar
        "images/characters/minazoomsad/minazoomsad_00004.png"
        pause blinkingvar
        "images/characters/minazoomsad/minazoomsad_00005.png"
        pause blinkingvar
        repeat

image minazoomserious:
    block:
        "images/characters/minazoomseriousluma/minazoomseriousluma_00000.png"
        pause lumafade
        "images/characters/minazoomseriousluma/minazoomseriousluma_00001.png"
        pause lumafade
        "images/characters/minazoomseriousluma/minazoomseriousluma_00002.png"
        pause lumafade
        "images/characters/minazoomseriousluma/minazoomseriousluma_00003.png"
        pause lumafade
        "images/characters/minazoomseriousluma/minazoomseriousluma_00004.png"
        pause lumafade
        "images/characters/minazoomseriousluma/minazoomseriousluma_00005.png"
        pause lumafade
        "images/characters/minazoomseriousluma/minazoomseriousluma_00006.png"
        pause lumafade
        "images/characters/minazoomseriousluma/minazoomseriousluma_00007.png"
        pause lumafade
    block:
        "images/characters/minazoomserious/minazoomserious_00000.png"
        pause blinkingvar
        "images/characters/minazoomserious/minazoomserious_00001.png"
        pause blinkingvar
        "images/characters/minazoomserious/minazoomserious_00002.png"
        pause 0.2
        "images/characters/minazoomserious/minazoomserious_00003.png"
        pause blinkingvar
        "images/characters/minazoomserious/minazoomserious_00004.png"
        pause blinkingvar
        "images/characters/minazoomserious/minazoomserious_00005.png"
        pause blinkingvar
        repeat

image minazoomshock:
    block:
        "images/characters/minazoomshockluma/minazoomshockluma_00000.png"
        pause lumafade
        "images/characters/minazoomshockluma/minazoomshockluma_00001.png"
        pause lumafade
        "images/characters/minazoomshockluma/minazoomshockluma_00002.png"
        pause lumafade
        "images/characters/minazoomshockluma/minazoomshockluma_00003.png"
        pause lumafade
        "images/characters/minazoomshockluma/minazoomshockluma_00004.png"
        pause lumafade
        "images/characters/minazoomshockluma/minazoomshockluma_00005.png"
        pause lumafade
        "images/characters/minazoomshockluma/minazoomshockluma_00006.png"
        pause lumafade
        "images/characters/minazoomshockluma/minazoomshockluma_00007.png"
        pause lumafade
    block:
        "images/characters/minazoomshock/minazoomshock_00000.png"
        pause blinkingvar
        "images/characters/minazoomshock/minazoomshock_00001.png"
        pause blinkingvar
        "images/characters/minazoomshock/minazoomshock_00002.png"
        pause 0.2
        "images/characters/minazoomshock/minazoomshock_00003.png"
        pause blinkingvar
        "images/characters/minazoomshock/minazoomshock_00004.png"
        pause blinkingvar
        "images/characters/minazoomshock/minazoomshock_00005.png"
        pause blinkingvar
        repeat

image minazoomsmug:
    block:
        "images/characters/minazoomsmugluma/minazoomsmugluma_00000.png"
        pause lumafade
        "images/characters/minazoomsmugluma/minazoomsmugluma_00001.png"
        pause lumafade
        "images/characters/minazoomsmugluma/minazoomsmugluma_00002.png"
        pause lumafade
        "images/characters/minazoomsmugluma/minazoomsmugluma_00003.png"
        pause lumafade
        "images/characters/minazoomsmugluma/minazoomsmugluma_00004.png"
        pause lumafade
        "images/characters/minazoomsmugluma/minazoomsmugluma_00005.png"
        pause lumafade
        "images/characters/minazoomsmugluma/minazoomsmugluma_00006.png"
        pause lumafade
        "images/characters/minazoomsmugluma/minazoomsmugluma_00007.png"
        pause lumafade
    block:
        "images/characters/minazoomsmug/minazoomsmug_00000.png"
        pause blinkingvar
        "images/characters/minazoomsmug/minazoomsmug_00001.png"
        pause blinkingvar
        "images/characters/minazoomsmug/minazoomsmug_00002.png"
        pause 0.2
        "images/characters/minazoomsmug/minazoomsmug_00003.png"
        pause blinkingvar
        "images/characters/minazoomsmug/minazoomsmug_00004.png"
        pause blinkingvar
        "images/characters/minazoomsmug/minazoomsmug_00005.png"
        pause blinkingvar
        repeat

image minazoomcontent:
    block:
        "images/characters/minazoomcontentluma/minazoomcontentluma_00000.png"
        pause lumafade
        "images/characters/minazoomcontentluma/minazoomcontentluma_00001.png"
        pause lumafade
        "images/characters/minazoomcontentluma/minazoomcontentluma_00002.png"
        pause lumafade
        "images/characters/minazoomcontentluma/minazoomcontentluma_00003.png"
        pause lumafade
        "images/characters/minazoomcontentluma/minazoomcontentluma_00004.png"
        pause lumafade
        "images/characters/minazoomcontentluma/minazoomcontentluma_00005.png"
        pause lumafade
        "images/characters/minazoomcontentluma/minazoomcontentluma_00006.png"
        pause lumafade
        "images/characters/minazoomcontentluma/minazoomcontentluma_00007.png"
        pause lumafade
    block:
        "images/characters/minazoomcontent/minazoomcontent_00000.png"
        pause blinkingvar
        "images/characters/minazoomcontent/minazoomcontent_00001.png"
        pause blinkingvar
        "images/characters/minazoomcontent/minazoomcontent_00002.png"
        pause 0.2
        "images/characters/minazoomcontent/minazoomcontent_00003.png"
        pause blinkingvar
        "images/characters/minazoomcontent/minazoomcontent_00004.png"
        pause blinkingvar
        "images/characters/minazoomcontent/minazoomcontent_00005.png"
        pause blinkingvar
        repeat

image minazoomneutral:
    block:
        "images/characters/minazoomneutralluma/minazoomneutralluma_00000.png"
        pause lumafade
        "images/characters/minazoomneutralluma/minazoomneutralluma_00001.png"
        pause lumafade
        "images/characters/minazoomneutralluma/minazoomneutralluma_00002.png"
        pause lumafade
        "images/characters/minazoomneutralluma/minazoomneutralluma_00003.png"
        pause lumafade
        "images/characters/minazoomneutralluma/minazoomneutralluma_00004.png"
        pause lumafade
        "images/characters/minazoomneutralluma/minazoomneutralluma_00005.png"
        pause lumafade
        "images/characters/minazoomneutralluma/minazoomneutralluma_00006.png"
        pause lumafade
        "images/characters/minazoomneutralluma/minazoomneutralluma_00007.png"
        pause lumafade
    block:
        "images/characters/minazoomneutral/minazoomneutral_00000.png"
        pause blinkingvar
        "images/characters/minazoomneutral/minazoomneutral_00001.png"
        pause blinkingvar
        "images/characters/minazoomneutral/minazoomneutral_00002.png"
        pause 0.2
        "images/characters/minazoomneutral/minazoomneutral_00003.png"
        pause blinkingvar
        "images/characters/minazoomneutral/minazoomneutral_00004.png"
        pause blinkingvar
        "images/characters/minazoomneutral/minazoomneutral_00005.png"
        pause blinkingvar
        repeat



##########
#####
###
#
#
# CHARACTERS - FACE
#
#
##
###
#####
##########

image rexfaceneutral:
    block:
        "images/characters/rexfaceneutralluma/rexfaceneutralluma_00000.png"
        pause lumafade
        "images/characters/rexfaceneutralluma/rexfaceneutralluma_00001.png"
        pause lumafade
        "images/characters/rexfaceneutralluma/rexfaceneutralluma_00002.png"
        pause lumafade
        "images/characters/rexfaceneutralluma/rexfaceneutralluma_00003.png"
        pause lumafade
        "images/characters/rexfaceneutralluma/rexfaceneutralluma_00004.png"
        pause lumafade
        "images/characters/rexfaceneutralluma/rexfaceneutralluma_00005.png"
        pause lumafade
        "images/characters/rexfaceneutralluma/rexfaceneutralluma_00006.png"
        pause lumafade
        "images/characters/rexfaceneutralluma/rexfaceneutralluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexfaceneutral/rexfaceneutral_00000.png"
        pause blinkingvar
        "images/characters/rexfaceneutral/rexfaceneutral_00001.png"
        pause blinkingvar
        "images/characters/rexfaceneutral/rexfaceneutral_00002.png"
        pause 0.2
        "images/characters/rexfaceneutral/rexfaceneutral_00003.png"
        pause blinkingvar
        "images/characters/rexfaceneutral/rexfaceneutral_00004.png"
        pause blinkingvar
        "images/characters/rexfaceneutral/rexfaceneutral_00005.png"
        pause blinkingvar
        repeat


image rexfacehappy:
    block:
        "images/characters/rexfacehappyluma/rexfacehappyluma_00000.png"
        pause lumafade
        "images/characters/rexfacehappyluma/rexfacehappyluma_00001.png"
        pause lumafade
        "images/characters/rexfacehappyluma/rexfacehappyluma_00002.png"
        pause lumafade
        "images/characters/rexfacehappyluma/rexfacehappyluma_00003.png"
        pause lumafade
        "images/characters/rexfacehappyluma/rexfacehappyluma_00004.png"
        pause lumafade
        "images/characters/rexfacehappyluma/rexfacehappyluma_00005.png"
        pause lumafade
        "images/characters/rexfacehappyluma/rexfacehappyluma_00006.png"
        pause lumafade
        "images/characters/rexfacehappyluma/rexfacehappyluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexfacehappy/rexfacehappy_00000.png"
        pause blinkingvar
        "images/characters/rexfacehappy/rexfacehappy_00001.png"
        pause blinkingvar
        "images/characters/rexfacehappy/rexfacehappy_00002.png"
        pause 0.2
        "images/characters/rexfacehappy/rexfacehappy_00003.png"
        pause blinkingvar
        "images/characters/rexfacehappy/rexfacehappy_00004.png"
        pause blinkingvar
        "images/characters/rexfacehappy/rexfacehappy_00005.png"
        pause blinkingvar
        repeat



image rexfaceangry:
    block:
        "images/characters/rexfaceangryluma/rexfaceangryluma_00000.png"
        pause lumafade
        "images/characters/rexfaceangryluma/rexfaceangryluma_00001.png"
        pause lumafade
        "images/characters/rexfaceangryluma/rexfaceangryluma_00002.png"
        pause lumafade
        "images/characters/rexfaceangryluma/rexfaceangryluma_00003.png"
        pause lumafade
        "images/characters/rexfaceangryluma/rexfaceangryluma_00004.png"
        pause lumafade
        "images/characters/rexfaceangryluma/rexfaceangryluma_00005.png"
        pause lumafade
        "images/characters/rexfaceangryluma/rexfaceangryluma_00006.png"
        pause lumafade
        "images/characters/rexfaceangryluma/rexfaceangryluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexfaceangry/rexfaceangry_00000.png"
        pause blinkingvar
        "images/characters/rexfaceangry/rexfaceangry_00001.png"
        pause blinkingvar
        "images/characters/rexfaceangry/rexfaceangry_00002.png"
        pause 0.2
        "images/characters/rexfaceangry/rexfaceangry_00003.png"
        pause blinkingvar
        "images/characters/rexfaceangry/rexfaceangry_00004.png"
        pause blinkingvar
        "images/characters/rexfaceangry/rexfaceangry_00005.png"
        pause blinkingvar
        repeat



image rexfacepain:
    block:
        "images/characters/rexfacepainluma/rexfacepainluma_00000.png"
        pause lumafade
        "images/characters/rexfacepainluma/rexfacepainluma_00001.png"
        pause lumafade
        "images/characters/rexfacepainluma/rexfacepainluma_00002.png"
        pause lumafade
        "images/characters/rexfacepainluma/rexfacepainluma_00003.png"
        pause lumafade
        "images/characters/rexfacepainluma/rexfacepainluma_00004.png"
        pause lumafade
        "images/characters/rexfacepainluma/rexfacepainluma_00005.png"
        pause lumafade
        "images/characters/rexfacepainluma/rexfacepainluma_00006.png"
        pause lumafade
        "images/characters/rexfacepainluma/rexfacepainluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexfacepain/rexfacepain_00000.png"
        pause blinkingvar
        "images/characters/rexfacepain/rexfacepain_00001.png"
        pause blinkingvar
        "images/characters/rexfacepain/rexfacepain_00002.png"
        pause 0.2
        "images/characters/rexfacepain/rexfacepain_00003.png"
        pause blinkingvar
        "images/characters/rexfacepain/rexfacepain_00004.png"
        pause blinkingvar
        "images/characters/rexfacepain/rexfacepain_00005.png"
        pause blinkingvar
        repeat



image rexfaceregret:
    block:
        "images/characters/rexfaceregretluma/rexfaceregretluma_00000.png"
        pause lumafade
        "images/characters/rexfaceregretluma/rexfaceregretluma_00001.png"
        pause lumafade
        "images/characters/rexfaceregretluma/rexfaceregretluma_00002.png"
        pause lumafade
        "images/characters/rexfaceregretluma/rexfaceregretluma_00003.png"
        pause lumafade
        "images/characters/rexfaceregretluma/rexfaceregretluma_00004.png"
        pause lumafade
        "images/characters/rexfaceregretluma/rexfaceregretluma_00005.png"
        pause lumafade
        "images/characters/rexfaceregretluma/rexfaceregretluma_00006.png"
        pause lumafade
        "images/characters/rexfaceregretluma/rexfaceregretluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexfaceregret/rexfaceregret_00000.png"
        pause blinkingvar
        "images/characters/rexfaceregret/rexfaceregret_00001.png"
        pause blinkingvar
        "images/characters/rexfaceregret/rexfaceregret_00002.png"
        pause 0.2
        "images/characters/rexfaceregret/rexfaceregret_00003.png"
        pause blinkingvar
        "images/characters/rexfaceregret/rexfaceregret_00004.png"
        pause blinkingvar
        "images/characters/rexfaceregret/rexfaceregret_00005.png"
        pause blinkingvar
        repeat



image rexfacesad:
    block:
        "images/characters/rexfacesadluma/rexfacesadluma_00000.png"
        pause lumafade
        "images/characters/rexfacesadluma/rexfacesadluma_00001.png"
        pause lumafade
        "images/characters/rexfacesadluma/rexfacesadluma_00002.png"
        pause lumafade
        "images/characters/rexfacesadluma/rexfacesadluma_00003.png"
        pause lumafade
        "images/characters/rexfacesadluma/rexfacesadluma_00004.png"
        pause lumafade
        "images/characters/rexfacesadluma/rexfacesadluma_00005.png"
        pause lumafade
        "images/characters/rexfacesadluma/rexfacesadluma_00006.png"
        pause lumafade
        "images/characters/rexfacesadluma/rexfacesadluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexfacesad/rexfacesad_00000.png"
        pause blinkingvar
        "images/characters/rexfacesad/rexfacesad_00001.png"
        pause blinkingvar
        "images/characters/rexfacesad/rexfacesad_00002.png"
        pause 0.2
        "images/characters/rexfacesad/rexfacesad_00003.png"
        pause blinkingvar
        "images/characters/rexfacesad/rexfacesad_00004.png"
        pause blinkingvar
        "images/characters/rexfacesad/rexfacesad_00005.png"
        pause blinkingvar
        repeat



image rexfaceserious:
    block:
        "images/characters/rexfaceseriousluma/rexfaceseriousluma_00000.png"
        pause lumafade
        "images/characters/rexfaceseriousluma/rexfaceseriousluma_00001.png"
        pause lumafade
        "images/characters/rexfaceseriousluma/rexfaceseriousluma_00002.png"
        pause lumafade
        "images/characters/rexfaceseriousluma/rexfaceseriousluma_00003.png"
        pause lumafade
        "images/characters/rexfaceseriousluma/rexfaceseriousluma_00004.png"
        pause lumafade
        "images/characters/rexfaceseriousluma/rexfaceseriousluma_00005.png"
        pause lumafade
        "images/characters/rexfaceseriousluma/rexfaceseriousluma_00006.png"
        pause lumafade
        "images/characters/rexfaceseriousluma/rexfaceseriousluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexfaceserious/rexfaceserious_00000.png"
        pause blinkingvar
        "images/characters/rexfaceserious/rexfaceserious_00001.png"
        pause blinkingvar
        "images/characters/rexfaceserious/rexfaceserious_00002.png"
        pause 0.2
        "images/characters/rexfaceserious/rexfaceserious_00003.png"
        pause blinkingvar
        "images/characters/rexfaceserious/rexfaceserious_00004.png"
        pause blinkingvar
        "images/characters/rexfaceserious/rexfaceserious_00005.png"
        pause blinkingvar
        repeat



image rexfaceshock:
    block:
        "images/characters/rexfaceshockluma/rexfaceshockluma_00000.png"
        pause lumafade
        "images/characters/rexfaceshockluma/rexfaceshockluma_00001.png"
        pause lumafade
        "images/characters/rexfaceshockluma/rexfaceshockluma_00002.png"
        pause lumafade
        "images/characters/rexfaceshockluma/rexfaceshockluma_00003.png"
        pause lumafade
        "images/characters/rexfaceshockluma/rexfaceshockluma_00004.png"
        pause lumafade
        "images/characters/rexfaceshockluma/rexfaceshockluma_00005.png"
        pause lumafade
        "images/characters/rexfaceshockluma/rexfaceshockluma_00006.png"
        pause lumafade
        "images/characters/rexfaceshockluma/rexfaceshockluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexfaceshock/rexfaceshock_00000.png"
        pause blinkingvar
        "images/characters/rexfaceshock/rexfaceshock_00001.png"
        pause blinkingvar
        "images/characters/rexfaceshock/rexfaceshock_00002.png"
        pause 0.2
        "images/characters/rexfaceshock/rexfaceshock_00003.png"
        pause blinkingvar
        "images/characters/rexfaceshock/rexfaceshock_00004.png"
        pause blinkingvar
        "images/characters/rexfaceshock/rexfaceshock_00005.png"
        pause blinkingvar
        repeat



image rexfacesmug:
    block:
        "images/characters/rexfacesmugluma/rexfacesmugluma_00000.png"
        pause lumafade
        "images/characters/rexfacesmugluma/rexfacesmugluma_00001.png"
        pause lumafade
        "images/characters/rexfacesmugluma/rexfacesmugluma_00002.png"
        pause lumafade
        "images/characters/rexfacesmugluma/rexfacesmugluma_00003.png"
        pause lumafade
        "images/characters/rexfacesmugluma/rexfacesmugluma_00004.png"
        pause lumafade
        "images/characters/rexfacesmugluma/rexfacesmugluma_00005.png"
        pause lumafade
        "images/characters/rexfacesmugluma/rexfacesmugluma_00006.png"
        pause lumafade
        "images/characters/rexfacesmugluma/rexfacesmugluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexfacesmug/rexfacesmug_00000.png"
        pause blinkingvar
        "images/characters/rexfacesmug/rexfacesmug_00001.png"
        pause blinkingvar
        "images/characters/rexfacesmug/rexfacesmug_00002.png"
        pause 0.2
        "images/characters/rexfacesmug/rexfacesmug_00003.png"
        pause blinkingvar
        "images/characters/rexfacesmug/rexfacesmug_00004.png"
        pause blinkingvar
        "images/characters/rexfacesmug/rexfacesmug_00005.png"
        pause blinkingvar
        repeat



image rexfacecontent:
    block:
        "images/characters/rexfacecontentluma/rexfacecontentluma_00000.png"
        pause lumafade
        "images/characters/rexfacecontentluma/rexfacecontentluma_00001.png"
        pause lumafade
        "images/characters/rexfacecontentluma/rexfacecontentluma_00002.png"
        pause lumafade
        "images/characters/rexfacecontentluma/rexfacecontentluma_00003.png"
        pause lumafade
        "images/characters/rexfacecontentluma/rexfacecontentluma_00004.png"
        pause lumafade
        "images/characters/rexfacecontentluma/rexfacecontentluma_00005.png"
        pause lumafade
        "images/characters/rexfacecontentluma/rexfacecontentluma_00006.png"
        pause lumafade
        "images/characters/rexfacecontentluma/rexfacecontentluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexfacecontent/rexfacecontent_00000.png"
        pause blinkingvar
        "images/characters/rexfacecontent/rexfacecontent_00001.png"
        pause blinkingvar
        "images/characters/rexfacecontent/rexfacecontent_00002.png"
        pause 0.2
        "images/characters/rexfacecontent/rexfacecontent_00003.png"
        pause blinkingvar
        "images/characters/rexfacecontent/rexfacecontent_00004.png"
        pause blinkingvar
        "images/characters/rexfacecontent/rexfacecontent_00005.png"
        pause blinkingvar
        repeat



image rexfacelove:
    block:
        "images/characters/rexfaceloveluma/rexfaceloveluma_00000.png"
        pause lumafade
        "images/characters/rexfaceloveluma/rexfaceloveluma_00001.png"
        pause lumafade
        "images/characters/rexfaceloveluma/rexfaceloveluma_00002.png"
        pause lumafade
        "images/characters/rexfaceloveluma/rexfaceloveluma_00003.png"
        pause lumafade
        "images/characters/rexfaceloveluma/rexfaceloveluma_00004.png"
        pause lumafade
        "images/characters/rexfaceloveluma/rexfaceloveluma_00005.png"
        pause lumafade
        "images/characters/rexfaceloveluma/rexfaceloveluma_00006.png"
        pause lumafade
        "images/characters/rexfaceloveluma/rexfaceloveluma_00007.png"
        pause lumafade
    block:
        "images/characters/rexfacelove/rexfacelove_00000.png"
        pause blinkingvar
        "images/characters/rexfacelove/rexfacelove_00001.png"
        pause blinkingvar
        "images/characters/rexfacelove/rexfacelove_00002.png"
        pause 0.2
        "images/characters/rexfacelove/rexfacelove_00003.png"
        pause blinkingvar
        "images/characters/rexfacelove/rexfacelove_00004.png"
        pause blinkingvar
        "images/characters/rexfacelove/rexfacelove_00005.png"
        pause blinkingvar
        repeat





image minafacelove:
    block:
        "images/characters/minafaceloveluma/minafaceloveluma_00000.png"
        pause lumafade
        "images/characters/minafaceloveluma/minafaceloveluma_00001.png"
        pause lumafade
        "images/characters/minafaceloveluma/minafaceloveluma_00002.png"
        pause lumafade
        "images/characters/minafaceloveluma/minafaceloveluma_00003.png"
        pause lumafade
        "images/characters/minafaceloveluma/minafaceloveluma_00004.png"
        pause lumafade
        "images/characters/minafaceloveluma/minafaceloveluma_00005.png"
        pause lumafade
        "images/characters/minafaceloveluma/minafaceloveluma_00006.png"
        pause lumafade
        "images/characters/minafaceloveluma/minafaceloveluma_00007.png"
        pause lumafade
    block:
        "images/characters/minafacelove/minafacelove_00000.png"
        pause blinkingvar
        "images/characters/minafacelove/minafacelove_00001.png"
        pause blinkingvar
        "images/characters/minafacelove/minafacelove_00002.png"
        pause 0.2
        "images/characters/minafacelove/minafacelove_00003.png"
        pause blinkingvar
        "images/characters/minafacelove/minafacelove_00004.png"
        pause blinkingvar
        "images/characters/minafacelove/minafacelove_00005.png"
        pause blinkingvar
        repeat

image minafaceneutral:
    block:
        "images/characters/minafaceneutralluma/minafaceneutralluma_00000.png"
        pause lumafade
        "images/characters/minafaceneutralluma/minafaceneutralluma_00001.png"
        pause lumafade
        "images/characters/minafaceneutralluma/minafaceneutralluma_00002.png"
        pause lumafade
        "images/characters/minafaceneutralluma/minafaceneutralluma_00003.png"
        pause lumafade
        "images/characters/minafaceneutralluma/minafaceneutralluma_00004.png"
        pause lumafade
        "images/characters/minafaceneutralluma/minafaceneutralluma_00005.png"
        pause lumafade
        "images/characters/minafaceneutralluma/minafaceneutralluma_00006.png"
        pause lumafade
        "images/characters/minafaceneutralluma/minafaceneutralluma_00007.png"
        pause lumafade
    block:
        "images/characters/minafaceneutral/minafaceneutral_00000.png"
        pause blinkingvar
        "images/characters/minafaceneutral/minafaceneutral_00001.png"
        pause blinkingvar
        "images/characters/minafaceneutral/minafaceneutral_00002.png"
        pause 0.2
        "images/characters/minafaceneutral/minafaceneutral_00003.png"
        pause blinkingvar
        "images/characters/minafaceneutral/minafaceneutral_00004.png"
        pause blinkingvar
        "images/characters/minafaceneutral/minafaceneutral_00005.png"
        pause blinkingvar
        repeat


image minafacehappy:
    block:
        "images/characters/minafacehappyluma/minafacehappyluma_00000.png"
        pause lumafade
        "images/characters/minafacehappyluma/minafacehappyluma_00001.png"
        pause lumafade
        "images/characters/minafacehappyluma/minafacehappyluma_00002.png"
        pause lumafade
        "images/characters/minafacehappyluma/minafacehappyluma_00003.png"
        pause lumafade
        "images/characters/minafacehappyluma/minafacehappyluma_00004.png"
        pause lumafade
        "images/characters/minafacehappyluma/minafacehappyluma_00005.png"
        pause lumafade
        "images/characters/minafacehappyluma/minafacehappyluma_00006.png"
        pause lumafade
        "images/characters/minafacehappyluma/minafacehappyluma_00007.png"
        pause lumafade
    block:
        "images/characters/minafacehappy/minafacehappy_00000.png"
        pause blinkingvar
        "images/characters/minafacehappy/minafacehappy_00001.png"
        pause blinkingvar
        "images/characters/minafacehappy/minafacehappy_00002.png"
        pause 0.2
        "images/characters/minafacehappy/minafacehappy_00003.png"
        pause blinkingvar
        "images/characters/minafacehappy/minafacehappy_00004.png"
        pause blinkingvar
        "images/characters/minafacehappy/minafacehappy_00005.png"
        pause blinkingvar
        repeat



image minafaceangry:
    block:
        "images/characters/minafaceangryluma/minafaceangryluma_00000.png"
        pause lumafade
        "images/characters/minafaceangryluma/minafaceangryluma_00001.png"
        pause lumafade
        "images/characters/minafaceangryluma/minafaceangryluma_00002.png"
        pause lumafade
        "images/characters/minafaceangryluma/minafaceangryluma_00003.png"
        pause lumafade
        "images/characters/minafaceangryluma/minafaceangryluma_00004.png"
        pause lumafade
        "images/characters/minafaceangryluma/minafaceangryluma_00005.png"
        pause lumafade
        "images/characters/minafaceangryluma/minafaceangryluma_00006.png"
        pause lumafade
        "images/characters/minafaceangryluma/minafaceangryluma_00007.png"
        pause lumafade
    block:
        "images/characters/minafaceangry/minafaceangry_00000.png"
        pause blinkingvar
        "images/characters/minafaceangry/minafaceangry_00001.png"
        pause blinkingvar
        "images/characters/minafaceangry/minafaceangry_00002.png"
        pause 0.2
        "images/characters/minafaceangry/minafaceangry_00003.png"
        pause blinkingvar
        "images/characters/minafaceangry/minafaceangry_00004.png"
        pause blinkingvar
        "images/characters/minafaceangry/minafaceangry_00005.png"
        pause blinkingvar
        repeat



image minafacepain:
    block:
        "images/characters/minafacepainluma/minafacepainluma_00000.png"
        pause lumafade
        "images/characters/minafacepainluma/minafacepainluma_00001.png"
        pause lumafade
        "images/characters/minafacepainluma/minafacepainluma_00002.png"
        pause lumafade
        "images/characters/minafacepainluma/minafacepainluma_00003.png"
        pause lumafade
        "images/characters/minafacepainluma/minafacepainluma_00004.png"
        pause lumafade
        "images/characters/minafacepainluma/minafacepainluma_00005.png"
        pause lumafade
        "images/characters/minafacepainluma/minafacepainluma_00006.png"
        pause lumafade
        "images/characters/minafacepainluma/minafacepainluma_00007.png"
        pause lumafade
    block:
        "images/characters/minafacepain/minafacepain_00000.png"
        pause blinkingvar
        "images/characters/minafacepain/minafacepain_00001.png"
        pause blinkingvar
        "images/characters/minafacepain/minafacepain_00002.png"
        pause 0.2
        "images/characters/minafacepain/minafacepain_00003.png"
        pause blinkingvar
        "images/characters/minafacepain/minafacepain_00004.png"
        pause blinkingvar
        "images/characters/minafacepain/minafacepain_00005.png"
        pause blinkingvar
        repeat



image minafaceregret:
    block:
        "images/characters/minafaceregretluma/minafaceregretluma_00000.png"
        pause lumafade
        "images/characters/minafaceregretluma/minafaceregretluma_00001.png"
        pause lumafade
        "images/characters/minafaceregretluma/minafaceregretluma_00002.png"
        pause lumafade
        "images/characters/minafaceregretluma/minafaceregretluma_00003.png"
        pause lumafade
        "images/characters/minafaceregretluma/minafaceregretluma_00004.png"
        pause lumafade
        "images/characters/minafaceregretluma/minafaceregretluma_00005.png"
        pause lumafade
        "images/characters/minafaceregretluma/minafaceregretluma_00006.png"
        pause lumafade
        "images/characters/minafaceregretluma/minafaceregretluma_00007.png"
        pause lumafade
    block:
        "images/characters/minafaceregret/minafaceregret_00000.png"
        pause blinkingvar
        "images/characters/minafaceregret/minafaceregret_00001.png"
        pause blinkingvar
        "images/characters/minafaceregret/minafaceregret_00002.png"
        pause 0.2
        "images/characters/minafaceregret/minafaceregret_00003.png"
        pause blinkingvar
        "images/characters/minafaceregret/minafaceregret_00004.png"
        pause blinkingvar
        "images/characters/minafaceregret/minafaceregret_00005.png"
        pause blinkingvar
        repeat



image minafacesad:
    block:
        "images/characters/minafacesadluma/minafacesadluma_00000.png"
        pause lumafade
        "images/characters/minafacesadluma/minafacesadluma_00001.png"
        pause lumafade
        "images/characters/minafacesadluma/minafacesadluma_00002.png"
        pause lumafade
        "images/characters/minafacesadluma/minafacesadluma_00003.png"
        pause lumafade
        "images/characters/minafacesadluma/minafacesadluma_00004.png"
        pause lumafade
        "images/characters/minafacesadluma/minafacesadluma_00005.png"
        pause lumafade
        "images/characters/minafacesadluma/minafacesadluma_00006.png"
        pause lumafade
        "images/characters/minafacesadluma/minafacesadluma_00007.png"
        pause lumafade
    block:
        "images/characters/minafacesad/minafacesad_00000.png"
        pause blinkingvar
        "images/characters/minafacesad/minafacesad_00001.png"
        pause blinkingvar
        "images/characters/minafacesad/minafacesad_00002.png"
        pause 0.2
        "images/characters/minafacesad/minafacesad_00003.png"
        pause blinkingvar
        "images/characters/minafacesad/minafacesad_00004.png"
        pause blinkingvar
        "images/characters/minafacesad/minafacesad_00005.png"
        pause blinkingvar
        repeat



image minafaceserious:
    block:
        "images/characters/minafaceseriousluma/minafaceseriousluma_00000.png"
        pause lumafade
        "images/characters/minafaceseriousluma/minafaceseriousluma_00001.png"
        pause lumafade
        "images/characters/minafaceseriousluma/minafaceseriousluma_00002.png"
        pause lumafade
        "images/characters/minafaceseriousluma/minafaceseriousluma_00003.png"
        pause lumafade
        "images/characters/minafaceseriousluma/minafaceseriousluma_00004.png"
        pause lumafade
        "images/characters/minafaceseriousluma/minafaceseriousluma_00005.png"
        pause lumafade
        "images/characters/minafaceseriousluma/minafaceseriousluma_00006.png"
        pause lumafade
        "images/characters/minafaceseriousluma/minafaceseriousluma_00007.png"
        pause lumafade
    block:
        "images/characters/minafaceserious/minafaceserious_00000.png"
        pause blinkingvar
        "images/characters/minafaceserious/minafaceserious_00001.png"
        pause blinkingvar
        "images/characters/minafaceserious/minafaceserious_00002.png"
        pause 0.2
        "images/characters/minafaceserious/minafaceserious_00003.png"
        pause blinkingvar
        "images/characters/minafaceserious/minafaceserious_00004.png"
        pause blinkingvar
        "images/characters/minafaceserious/minafaceserious_00005.png"
        pause blinkingvar
        repeat



image minafaceshock:
    block:
        "images/characters/minafaceshockluma/minafaceshockluma_00000.png"
        pause lumafade
        "images/characters/minafaceshockluma/minafaceshockluma_00001.png"
        pause lumafade
        "images/characters/minafaceshockluma/minafaceshockluma_00002.png"
        pause lumafade
        "images/characters/minafaceshockluma/minafaceshockluma_00003.png"
        pause lumafade
        "images/characters/minafaceshockluma/minafaceshockluma_00004.png"
        pause lumafade
        "images/characters/minafaceshockluma/minafaceshockluma_00005.png"
        pause lumafade
        "images/characters/minafaceshockluma/minafaceshockluma_00006.png"
        pause lumafade
        "images/characters/minafaceshockluma/minafaceshockluma_00007.png"
        pause lumafade
    block:
        "images/characters/minafaceshock/minafaceshock_00000.png"
        pause blinkingvar
        "images/characters/minafaceshock/minafaceshock_00001.png"
        pause blinkingvar
        "images/characters/minafaceshock/minafaceshock_00002.png"
        pause 0.2
        "images/characters/minafaceshock/minafaceshock_00003.png"
        pause blinkingvar
        "images/characters/minafaceshock/minafaceshock_00004.png"
        pause blinkingvar
        "images/characters/minafaceshock/minafaceshock_00005.png"
        pause blinkingvar
        repeat



image minafacesmug:
    block:
        "images/characters/minafacesmugluma/minafacesmugluma_00000.png"
        pause lumafade
        "images/characters/minafacesmugluma/minafacesmugluma_00001.png"
        pause lumafade
        "images/characters/minafacesmugluma/minafacesmugluma_00002.png"
        pause lumafade
        "images/characters/minafacesmugluma/minafacesmugluma_00003.png"
        pause lumafade
        "images/characters/minafacesmugluma/minafacesmugluma_00004.png"
        pause lumafade
        "images/characters/minafacesmugluma/minafacesmugluma_00005.png"
        pause lumafade
        "images/characters/minafacesmugluma/minafacesmugluma_00006.png"
        pause lumafade
        "images/characters/minafacesmugluma/minafacesmugluma_00007.png"
        pause lumafade
    block:
        "images/characters/minafacesmug/minafacesmug_00000.png"
        pause blinkingvar
        "images/characters/minafacesmug/minafacesmug_00001.png"
        pause blinkingvar
        "images/characters/minafacesmug/minafacesmug_00002.png"
        pause 0.2
        "images/characters/minafacesmug/minafacesmug_00003.png"
        pause blinkingvar
        "images/characters/minafacesmug/minafacesmug_00004.png"
        pause blinkingvar
        "images/characters/minafacesmug/minafacesmug_00005.png"
        pause blinkingvar
        repeat



image minafacecontent:
    block:
        "images/characters/minafacecontentluma/minafacecontentluma_00000.png"
        pause lumafade
        "images/characters/minafacecontentluma/minafacecontentluma_00001.png"
        pause lumafade
        "images/characters/minafacecontentluma/minafacecontentluma_00002.png"
        pause lumafade
        "images/characters/minafacecontentluma/minafacecontentluma_00003.png"
        pause lumafade
        "images/characters/minafacecontentluma/minafacecontentluma_00004.png"
        pause lumafade
        "images/characters/minafacecontentluma/minafacecontentluma_00005.png"
        pause lumafade
        "images/characters/minafacecontentluma/minafacecontentluma_00006.png"
        pause lumafade
        "images/characters/minafacecontentluma/minafacecontentluma_00007.png"
        pause lumafade
    block:
        "images/characters/minafacecontent/minafacecontent_00000.png"
        pause blinkingvar
        "images/characters/minafacecontent/minafacecontent_00001.png"
        pause blinkingvar
        "images/characters/minafacecontent/minafacecontent_00002.png"
        pause 0.2
        "images/characters/minafacecontent/minafacecontent_00003.png"
        pause blinkingvar
        "images/characters/minafacecontent/minafacecontent_00004.png"
        pause blinkingvar
        "images/characters/minafacecontent/minafacecontent_00005.png"
        pause blinkingvar
        repeat


##########
#####
###
#
#
# INSERTS - STORY INSERTS
#
#
##
###
#####
##########


image insertstoryone: 
    "images/inserts/insertstoryone/insertstoryone_00000.webp"
    pause insertvar
    "images/inserts/insertstoryone/insertstoryone_00001.webp"
    pause insertvar
    "images/inserts/insertstoryone/insertstoryone_00002.webp"
    pause insertvar
    "images/inserts/insertstoryone/insertstoryone_00003.webp"
    pause insertvar
    "images/inserts/insertstoryone/insertstoryone_00004.webp"
    pause insertvar
    "images/inserts/insertstoryone/insertstoryone_00005.webp"
    pause insertvar
    "images/inserts/insertstoryone/insertstoryone_00006.webp"
    pause insertvar
    "images/inserts/insertstoryone/insertstoryone_00007.webp"
    pause insertvar
    "images/inserts/insertstoryone/insertstoryone_00008.webp"
    pause insertvar
    "images/inserts/insertstoryone/insertstoryone_00009.webp"
    pause insertvar
    "images/inserts/insertstoryone/insertstoryone_00010.webp"
    pause insertvar
    "images/inserts/insertstoryone/insertstoryone_00011.webp"
    pause insertvar
    "images/inserts/insertstoryone/insertstoryone_00012.webp"
    pause insertvar
    "images/inserts/insertstoryone/insertstoryone_00013.webp"
    pause insertvar
    "images/inserts/insertstoryone/insertstoryone_00014.webp"
    pause insertvar
    "images/inserts/insertstoryone/insertstoryone_00015.webp"
    pause insertvar
    "images/inserts/insertstoryone/insertstoryone_00016.webp"
    pause insertvar
    "images/inserts/insertstoryone/insertstoryone_00017.webp"
    pause insertvar
    "images/inserts/insertstoryone/insertstoryone_00018.webp"
    pause insertvar
    "images/inserts/insertstoryone/insertstoryone_00019.webp"
    pause insertvar
    "images/inserts/insertstoryone/insertstoryone_00020.webp"
    pause insertvar
    "images/inserts/insertstoryone/insertstoryone_00021.webp"
    pause insertvar
    "images/inserts/insertstoryone/insertstoryone_00022.webp"
    pause insertvar
    "images/inserts/insertstoryone/insertstoryone_00023.webp"
    pause insertvar
    "images/inserts/insertstoryone/insertstoryone_00024.webp"
    pause insertvar
    "images/inserts/insertstoryone/insertstoryone_00025.webp"
    pause insertvar
    "images/inserts/insertstoryone/insertstoryone_00026.webp"
    pause insertvar
    "images/inserts/insertstoryone/insertstoryone_00027.webp"
    pause insertvar
    "images/inserts/insertstoryone/insertstoryone_00028.webp"
    pause insertvar
    "images/inserts/insertstoryone/insertstoryone_00029.webp"
    pause insertvar
    repeat

image insertstorytwo: 
    "images/inserts/insertstorytwo/insertstorytwo_00000.webp"
    pause insertvar
    "images/inserts/insertstorytwo/insertstorytwo_00001.webp"
    pause insertvar
    "images/inserts/insertstorytwo/insertstorytwo_00002.webp"
    pause insertvar
    "images/inserts/insertstorytwo/insertstorytwo_00003.webp"
    pause insertvar
    "images/inserts/insertstorytwo/insertstorytwo_00004.webp"
    pause insertvar
    "images/inserts/insertstorytwo/insertstorytwo_00005.webp"
    pause insertvar
    "images/inserts/insertstorytwo/insertstorytwo_00006.webp"
    pause insertvar
    "images/inserts/insertstorytwo/insertstorytwo_00007.webp"
    pause insertvar
    "images/inserts/insertstorytwo/insertstorytwo_00008.webp"
    pause insertvar
    "images/inserts/insertstorytwo/insertstorytwo_00009.webp"
    pause insertvar
    "images/inserts/insertstorytwo/insertstorytwo_00010.webp"
    pause insertvar
    "images/inserts/insertstorytwo/insertstorytwo_00011.webp"
    pause insertvar
    "images/inserts/insertstorytwo/insertstorytwo_00012.webp"
    pause insertvar
    "images/inserts/insertstorytwo/insertstorytwo_00013.webp"
    pause insertvar
    "images/inserts/insertstorytwo/insertstorytwo_00014.webp"
    pause insertvar
    "images/inserts/insertstorytwo/insertstorytwo_00015.webp"
    pause insertvar
    "images/inserts/insertstorytwo/insertstorytwo_00016.webp"
    pause insertvar
    "images/inserts/insertstorytwo/insertstorytwo_00017.webp"
    pause insertvar
    "images/inserts/insertstorytwo/insertstorytwo_00018.webp"
    pause insertvar
    "images/inserts/insertstorytwo/insertstorytwo_00019.webp"
    pause insertvar
    "images/inserts/insertstorytwo/insertstorytwo_00020.webp"
    pause insertvar
    "images/inserts/insertstorytwo/insertstorytwo_00021.webp"
    pause insertvar
    "images/inserts/insertstorytwo/insertstorytwo_00022.webp"
    pause insertvar
    "images/inserts/insertstorytwo/insertstorytwo_00023.webp"
    pause insertvar
    "images/inserts/insertstorytwo/insertstorytwo_00024.webp"
    pause insertvar
    "images/inserts/insertstorytwo/insertstorytwo_00025.webp"
    pause insertvar
    "images/inserts/insertstorytwo/insertstorytwo_00026.webp"
    pause insertvar
    "images/inserts/insertstorytwo/insertstorytwo_00027.webp"
    pause insertvar
    "images/inserts/insertstorytwo/insertstorytwo_00028.webp"
    pause insertvar
    "images/inserts/insertstorytwo/insertstorytwo_00029.webp"
    pause insertvar
    repeat

image insertstorythree: 
    "images/inserts/insertstorythree/insertstorythree_00000.webp"
    pause insertvar
    "images/inserts/insertstorythree/insertstorythree_00001.webp"
    pause insertvar
    "images/inserts/insertstorythree/insertstorythree_00002.webp"
    pause insertvar
    "images/inserts/insertstorythree/insertstorythree_00003.webp"
    pause insertvar
    "images/inserts/insertstorythree/insertstorythree_00004.webp"
    pause insertvar
    "images/inserts/insertstorythree/insertstorythree_00005.webp"
    pause insertvar
    "images/inserts/insertstorythree/insertstorythree_00006.webp"
    pause insertvar
    "images/inserts/insertstorythree/insertstorythree_00007.webp"
    pause insertvar
    "images/inserts/insertstorythree/insertstorythree_00008.webp"
    pause insertvar
    "images/inserts/insertstorythree/insertstorythree_00009.webp"
    pause insertvar
    "images/inserts/insertstorythree/insertstorythree_00010.webp"
    pause insertvar
    "images/inserts/insertstorythree/insertstorythree_00011.webp"
    pause insertvar
    "images/inserts/insertstorythree/insertstorythree_00012.webp"
    pause insertvar
    "images/inserts/insertstorythree/insertstorythree_00013.webp"
    pause insertvar
    "images/inserts/insertstorythree/insertstorythree_00014.webp"
    pause insertvar
    "images/inserts/insertstorythree/insertstorythree_00015.webp"
    pause insertvar
    "images/inserts/insertstorythree/insertstorythree_00016.webp"
    pause insertvar
    "images/inserts/insertstorythree/insertstorythree_00017.webp"
    pause insertvar
    "images/inserts/insertstorythree/insertstorythree_00018.webp"
    pause insertvar
    "images/inserts/insertstorythree/insertstorythree_00019.webp"
    pause insertvar
    "images/inserts/insertstorythree/insertstorythree_00020.webp"
    pause insertvar
    "images/inserts/insertstorythree/insertstorythree_00021.webp"
    pause insertvar
    "images/inserts/insertstorythree/insertstorythree_00022.webp"
    pause insertvar
    "images/inserts/insertstorythree/insertstorythree_00023.webp"
    pause insertvar
    "images/inserts/insertstorythree/insertstorythree_00024.webp"
    pause insertvar
    "images/inserts/insertstorythree/insertstorythree_00025.webp"
    pause insertvar
    "images/inserts/insertstorythree/insertstorythree_00026.webp"
    pause insertvar
    "images/inserts/insertstorythree/insertstorythree_00027.webp"
    pause insertvar
    "images/inserts/insertstorythree/insertstorythree_00028.webp"
    pause insertvar
    "images/inserts/insertstorythree/insertstorythree_00029.webp"
    pause insertvar
    repeat

image insertstoryfour: 
    "images/inserts/insertstoryfour/insertstoryfour_00000.webp"
    pause insertvar
    "images/inserts/insertstoryfour/insertstoryfour_00001.webp"
    pause insertvar
    "images/inserts/insertstoryfour/insertstoryfour_00002.webp"
    pause insertvar
    "images/inserts/insertstoryfour/insertstoryfour_00003.webp"
    pause insertvar
    "images/inserts/insertstoryfour/insertstoryfour_00004.webp"
    pause insertvar
    "images/inserts/insertstoryfour/insertstoryfour_00005.webp"
    pause insertvar
    "images/inserts/insertstoryfour/insertstoryfour_00006.webp"
    pause insertvar
    "images/inserts/insertstoryfour/insertstoryfour_00007.webp"
    pause insertvar
    "images/inserts/insertstoryfour/insertstoryfour_00008.webp"
    pause insertvar
    "images/inserts/insertstoryfour/insertstoryfour_00009.webp"
    pause insertvar
    "images/inserts/insertstoryfour/insertstoryfour_00010.webp"
    pause insertvar
    "images/inserts/insertstoryfour/insertstoryfour_00011.webp"
    pause insertvar
    "images/inserts/insertstoryfour/insertstoryfour_00012.webp"
    pause insertvar
    "images/inserts/insertstoryfour/insertstoryfour_00013.webp"
    pause insertvar
    "images/inserts/insertstoryfour/insertstoryfour_00014.webp"
    pause insertvar
    "images/inserts/insertstoryfour/insertstoryfour_00015.webp"
    pause insertvar
    "images/inserts/insertstoryfour/insertstoryfour_00016.webp"
    pause insertvar
    "images/inserts/insertstoryfour/insertstoryfour_00017.webp"
    pause insertvar
    "images/inserts/insertstoryfour/insertstoryfour_00018.webp"
    pause insertvar
    "images/inserts/insertstoryfour/insertstoryfour_00019.webp"
    pause insertvar
    "images/inserts/insertstoryfour/insertstoryfour_00020.webp"
    pause insertvar
    "images/inserts/insertstoryfour/insertstoryfour_00021.webp"
    pause insertvar
    "images/inserts/insertstoryfour/insertstoryfour_00022.webp"
    pause insertvar
    "images/inserts/insertstoryfour/insertstoryfour_00023.webp"
    pause insertvar
    "images/inserts/insertstoryfour/insertstoryfour_00024.webp"
    pause insertvar
    "images/inserts/insertstoryfour/insertstoryfour_00025.webp"
    pause insertvar
    "images/inserts/insertstoryfour/insertstoryfour_00026.webp"
    pause insertvar
    "images/inserts/insertstoryfour/insertstoryfour_00027.webp"
    pause insertvar
    "images/inserts/insertstoryfour/insertstoryfour_00028.webp"
    pause insertvar
    "images/inserts/insertstoryfour/insertstoryfour_00029.webp"
    pause insertvar
    repeat

image insertstoryfive: 
    "images/inserts/insertstoryfive/insertstoryfive_00000.webp"
    pause insertvar
    "images/inserts/insertstoryfive/insertstoryfive_00001.webp"
    pause insertvar
    "images/inserts/insertstoryfive/insertstoryfive_00002.webp"
    pause insertvar
    "images/inserts/insertstoryfive/insertstoryfive_00003.webp"
    pause insertvar
    "images/inserts/insertstoryfive/insertstoryfive_00004.webp"
    pause insertvar
    "images/inserts/insertstoryfive/insertstoryfive_00005.webp"
    pause insertvar
    "images/inserts/insertstoryfive/insertstoryfive_00006.webp"
    pause insertvar
    "images/inserts/insertstoryfive/insertstoryfive_00007.webp"
    pause insertvar
    "images/inserts/insertstoryfive/insertstoryfive_00008.webp"
    pause insertvar
    "images/inserts/insertstoryfive/insertstoryfive_00009.webp"
    pause insertvar
    "images/inserts/insertstoryfive/insertstoryfive_00010.webp"
    pause insertvar
    "images/inserts/insertstoryfive/insertstoryfive_00011.webp"
    pause insertvar
    "images/inserts/insertstoryfive/insertstoryfive_00012.webp"
    pause insertvar
    "images/inserts/insertstoryfive/insertstoryfive_00013.webp"
    pause insertvar
    "images/inserts/insertstoryfive/insertstoryfive_00014.webp"
    pause insertvar
    "images/inserts/insertstoryfive/insertstoryfive_00015.webp"
    pause insertvar
    "images/inserts/insertstoryfive/insertstoryfive_00016.webp"
    pause insertvar
    "images/inserts/insertstoryfive/insertstoryfive_00017.webp"
    pause insertvar
    "images/inserts/insertstoryfive/insertstoryfive_00018.webp"
    pause insertvar
    "images/inserts/insertstoryfive/insertstoryfive_00019.webp"
    pause insertvar
    "images/inserts/insertstoryfive/insertstoryfive_00020.webp"
    pause insertvar
    "images/inserts/insertstoryfive/insertstoryfive_00021.webp"
    pause insertvar
    "images/inserts/insertstoryfive/insertstoryfive_00022.webp"
    pause insertvar
    "images/inserts/insertstoryfive/insertstoryfive_00023.webp"
    pause insertvar
    "images/inserts/insertstoryfive/insertstoryfive_00024.webp"
    pause insertvar
    "images/inserts/insertstoryfive/insertstoryfive_00025.webp"
    pause insertvar
    "images/inserts/insertstoryfive/insertstoryfive_00026.webp"
    pause insertvar
    "images/inserts/insertstoryfive/insertstoryfive_00027.webp"
    pause insertvar
    "images/inserts/insertstoryfive/insertstoryfive_00028.webp"
    pause insertvar
    "images/inserts/insertstoryfive/insertstoryfive_00029.webp"
    pause insertvar
    repeat

image insertstorysix: 
    "images/inserts/insertstorysix/insertstorysix_00000.webp"
    pause insertvar
    "images/inserts/insertstorysix/insertstorysix_00001.webp"
    pause insertvar
    "images/inserts/insertstorysix/insertstorysix_00002.webp"
    pause insertvar
    "images/inserts/insertstorysix/insertstorysix_00003.webp"
    pause insertvar
    "images/inserts/insertstorysix/insertstorysix_00004.webp"
    pause insertvar
    "images/inserts/insertstorysix/insertstorysix_00005.webp"
    pause insertvar
    "images/inserts/insertstorysix/insertstorysix_00006.webp"
    pause insertvar
    "images/inserts/insertstorysix/insertstorysix_00007.webp"
    pause insertvar
    "images/inserts/insertstorysix/insertstorysix_00008.webp"
    pause insertvar
    "images/inserts/insertstorysix/insertstorysix_00009.webp"
    pause insertvar
    "images/inserts/insertstorysix/insertstorysix_00010.webp"
    pause insertvar
    "images/inserts/insertstorysix/insertstorysix_00011.webp"
    pause insertvar
    "images/inserts/insertstorysix/insertstorysix_00012.webp"
    pause insertvar
    "images/inserts/insertstorysix/insertstorysix_00013.webp"
    pause insertvar
    "images/inserts/insertstorysix/insertstorysix_00014.webp"
    pause insertvar
    "images/inserts/insertstorysix/insertstorysix_00015.webp"
    pause insertvar
    "images/inserts/insertstorysix/insertstorysix_00016.webp"
    pause insertvar
    "images/inserts/insertstorysix/insertstorysix_00017.webp"
    pause insertvar
    "images/inserts/insertstorysix/insertstorysix_00018.webp"
    pause insertvar
    "images/inserts/insertstorysix/insertstorysix_00019.webp"
    pause insertvar
    "images/inserts/insertstorysix/insertstorysix_00020.webp"
    pause insertvar
    "images/inserts/insertstorysix/insertstorysix_00021.webp"
    pause insertvar
    "images/inserts/insertstorysix/insertstorysix_00022.webp"
    pause insertvar
    "images/inserts/insertstorysix/insertstorysix_00023.webp"
    pause insertvar
    "images/inserts/insertstorysix/insertstorysix_00024.webp"
    pause insertvar
    "images/inserts/insertstorysix/insertstorysix_00025.webp"
    pause insertvar
    "images/inserts/insertstorysix/insertstorysix_00026.webp"
    pause insertvar
    "images/inserts/insertstorysix/insertstorysix_00027.webp"
    pause insertvar
    "images/inserts/insertstorysix/insertstorysix_00028.webp"
    pause insertvar
    "images/inserts/insertstorysix/insertstorysix_00029.webp"
    pause insertvar
    repeat



image inserttitle: 
    "images/inserts/inserttitle/inserttitle_00000.webp"
    pause insertvar
    "images/inserts/inserttitle/inserttitle_00001.webp"
    pause insertvar
    "images/inserts/inserttitle/inserttitle_00002.webp"
    pause insertvar
    "images/inserts/inserttitle/inserttitle_00003.webp"
    pause insertvar
    "images/inserts/inserttitle/inserttitle_00004.webp"
    pause insertvar
    "images/inserts/inserttitle/inserttitle_00005.webp"
    pause insertvar
    "images/inserts/inserttitle/inserttitle_00006.webp"
    pause insertvar
    "images/inserts/inserttitle/inserttitle_00007.webp"
    pause insertvar
    "images/inserts/inserttitle/inserttitle_00008.webp"
    pause insertvar
    "images/inserts/inserttitle/inserttitle_00009.webp"
    pause insertvar
    "images/inserts/inserttitle/inserttitle_00010.webp"
    pause insertvar
    "images/inserts/inserttitle/inserttitle_00011.webp"
    pause insertvar
    "images/inserts/inserttitle/inserttitle_00012.webp"
    pause insertvar
    "images/inserts/inserttitle/inserttitle_00013.webp"
    pause insertvar
    "images/inserts/inserttitle/inserttitle_00014.webp"
    pause insertvar
    "images/inserts/inserttitle/inserttitle_00015.webp"
    pause insertvar
    "images/inserts/inserttitle/inserttitle_00016.webp"
    pause insertvar
    "images/inserts/inserttitle/inserttitle_00017.webp"
    pause insertvar
    "images/inserts/inserttitle/inserttitle_00018.webp"
    pause insertvar
    "images/inserts/inserttitle/inserttitle_00019.webp"
    pause insertvar
    "images/inserts/inserttitle/inserttitle_00020.webp"
    pause insertvar
    "images/inserts/inserttitle/inserttitle_00021.webp"
    pause insertvar
    "images/inserts/inserttitle/inserttitle_00022.webp"
    pause insertvar
    "images/inserts/inserttitle/inserttitle_00023.webp"
    pause insertvar
    "images/inserts/inserttitle/inserttitle_00024.webp"
    pause insertvar
    "images/inserts/inserttitle/inserttitle_00025.webp"
    pause insertvar
    repeat


image confrontation: 
    "images/inserts/confrontation/confrontation_00000.webp"
    pause insertvar
    "images/inserts/confrontation/confrontation_00001.webp"
    pause insertvar
    "images/inserts/confrontation/confrontation_00002.webp"
    pause insertvar
    "images/inserts/confrontation/confrontation_00003.webp"
    pause insertvar
    "images/inserts/confrontation/confrontation_00004.webp"
    pause insertvar
    "images/inserts/confrontation/confrontation_00005.webp"
    pause insertvar
    "images/inserts/confrontation/confrontation_00006.webp"
    pause insertvar
    "images/inserts/confrontation/confrontation_00007.webp"
    pause insertvar
    "images/inserts/confrontation/confrontation_00008.webp"
    pause insertvar
    "images/inserts/confrontation/confrontation_00009.webp"
    pause insertvar
    "images/inserts/confrontation/confrontation_00010.webp"
    pause insertvar
    "images/inserts/confrontation/confrontation_00011.webp"
    pause insertvar
    "images/inserts/confrontation/confrontation_00012.webp"
    pause insertvar
    "images/inserts/confrontation/confrontation_00013.webp"
    pause insertvar
    "images/inserts/confrontation/confrontation_00014.webp"
    pause insertvar
    "images/inserts/confrontation/confrontation_00015.webp"
    pause insertvar
    "images/inserts/confrontation/confrontation_00016.webp"
    pause insertvar
    "images/inserts/confrontation/confrontation_00017.webp"
    pause insertvar
    "images/inserts/confrontation/confrontation_00018.webp"
    pause insertvar
    "images/inserts/confrontation/confrontation_00019.webp"
    pause insertvar
    "images/inserts/confrontation/confrontation_00020.webp"
    pause insertvar
    "images/inserts/confrontation/confrontation_00021.webp"
    pause insertvar
    "images/inserts/confrontation/confrontation_00022.webp"
    pause insertvar
    "images/inserts/confrontation/confrontation_00023.webp"
    pause insertvar
    "images/inserts/confrontation/confrontation_00024.webp"
    pause insertvar
    "images/inserts/confrontation/confrontation_00025.webp"
    pause insertvar
    repeat


image distortsketch: 
    "images/inserts/distortsketch/distortsketch_00000.webp"
    pause insertvar
    "images/inserts/distortsketch/distortsketch_00001.webp"
    pause insertvar
    "images/inserts/distortsketch/distortsketch_00002.webp"
    pause insertvar
    "images/inserts/distortsketch/distortsketch_00003.webp"
    pause insertvar
    "images/inserts/distortsketch/distortsketch_00004.webp"
    pause insertvar
    "images/inserts/distortsketch/distortsketch_00005.webp"
    pause insertvar
    "images/inserts/distortsketch/distortsketch_00006.webp"
    pause insertvar
    "images/inserts/distortsketch/distortsketch_00007.webp"
    pause insertvar
    "images/inserts/distortsketch/distortsketch_00008.webp"
    pause insertvar
    "images/inserts/distortsketch/distortsketch_00009.webp"
    pause insertvar
    "images/inserts/distortsketch/distortsketch_00010.webp"
    pause insertvar
    "images/inserts/distortsketch/distortsketch_00011.webp"
    pause insertvar
    "images/inserts/distortsketch/distortsketch_00012.webp"
    pause insertvar
    "images/inserts/distortsketch/distortsketch_00013.webp"
    pause insertvar
    "images/inserts/distortsketch/distortsketch_00014.webp"
    pause insertvar
    "images/inserts/distortsketch/distortsketch_00015.webp"
    pause insertvar
    "images/inserts/distortsketch/distortsketch_00016.webp"
    pause insertvar
    "images/inserts/distortsketch/distortsketch_00017.webp"
    pause insertvar
    "images/inserts/distortsketch/distortsketch_00018.webp"
    pause insertvar
    "images/inserts/distortsketch/distortsketch_00019.webp"
    pause insertvar
    "images/inserts/distortsketch/distortsketch_00020.webp"
    pause insertvar
    "images/inserts/distortsketch/distortsketch_00021.webp"
    pause insertvar
    "images/inserts/distortsketch/distortsketch_00022.webp"
    pause insertvar
    "images/inserts/distortsketch/distortsketch_00023.webp"
    pause insertvar
    "images/inserts/distortsketch/distortsketch_00024.webp"
    pause insertvar
    "images/inserts/distortsketch/distortsketch_00025.webp"
    pause insertvar
    repeat


image distortsketchtwo: 
    "images/inserts/distortsketchtwo/distortsketchtwo_00000.webp"
    pause insertvar
    "images/inserts/distortsketchtwo/distortsketchtwo_00001.webp"
    pause insertvar
    "images/inserts/distortsketchtwo/distortsketchtwo_00002.webp"
    pause insertvar
    "images/inserts/distortsketchtwo/distortsketchtwo_00003.webp"
    pause insertvar
    "images/inserts/distortsketchtwo/distortsketchtwo_00004.webp"
    pause insertvar
    "images/inserts/distortsketchtwo/distortsketchtwo_00005.webp"
    pause insertvar
    "images/inserts/distortsketchtwo/distortsketchtwo_00006.webp"
    pause insertvar
    "images/inserts/distortsketchtwo/distortsketchtwo_00007.webp"
    pause insertvar
    "images/inserts/distortsketchtwo/distortsketchtwo_00008.webp"
    pause insertvar
    "images/inserts/distortsketchtwo/distortsketchtwo_00009.webp"
    pause insertvar
    "images/inserts/distortsketchtwo/distortsketchtwo_00010.webp"
    pause insertvar
    "images/inserts/distortsketchtwo/distortsketchtwo_00011.webp"
    pause insertvar
    "images/inserts/distortsketchtwo/distortsketchtwo_00012.webp"
    pause insertvar
    "images/inserts/distortsketchtwo/distortsketchtwo_00013.webp"
    pause insertvar
    "images/inserts/distortsketchtwo/distortsketchtwo_00014.webp"
    pause insertvar
    "images/inserts/distortsketchtwo/distortsketchtwo_00015.webp"
    pause insertvar
    "images/inserts/distortsketchtwo/distortsketchtwo_00016.webp"
    pause insertvar
    "images/inserts/distortsketchtwo/distortsketchtwo_00017.webp"
    pause insertvar
    "images/inserts/distortsketchtwo/distortsketchtwo_00018.webp"
    pause insertvar
    "images/inserts/distortsketchtwo/distortsketchtwo_00019.webp"
    pause insertvar
    "images/inserts/distortsketchtwo/distortsketchtwo_00020.webp"
    pause insertvar
    "images/inserts/distortsketchtwo/distortsketchtwo_00021.webp"
    pause insertvar
    "images/inserts/distortsketchtwo/distortsketchtwo_00022.webp"
    pause insertvar
    "images/inserts/distortsketchtwo/distortsketchtwo_00023.webp"
    pause insertvar
    "images/inserts/distortsketchtwo/distortsketchtwo_00024.webp"
    pause insertvar
    "images/inserts/distortsketchtwo/distortsketchtwo_00025.webp"
    pause insertvar
    repeat


image momdeath: 
    "images/inserts/momdeath/momdeath_00000.webp"
    pause insertvar
    "images/inserts/momdeath/momdeath_00001.webp"
    pause insertvar
    "images/inserts/momdeath/momdeath_00002.webp"
    pause insertvar
    "images/inserts/momdeath/momdeath_00003.webp"
    pause insertvar
    "images/inserts/momdeath/momdeath_00004.webp"
    pause insertvar
    "images/inserts/momdeath/momdeath_00005.webp"
    pause insertvar
    "images/inserts/momdeath/momdeath_00006.webp"
    pause insertvar
    "images/inserts/momdeath/momdeath_00007.webp"
    pause insertvar
    "images/inserts/momdeath/momdeath_00008.webp"
    pause insertvar
    "images/inserts/momdeath/momdeath_00009.webp"
    pause insertvar
    "images/inserts/momdeath/momdeath_00010.webp"
    pause insertvar
    "images/inserts/momdeath/momdeath_00011.webp"
    pause insertvar
    "images/inserts/momdeath/momdeath_00012.webp"
    pause insertvar
    "images/inserts/momdeath/momdeath_00013.webp"
    pause insertvar
    "images/inserts/momdeath/momdeath_00014.webp"
    pause insertvar
    "images/inserts/momdeath/momdeath_00015.webp"
    pause insertvar
    "images/inserts/momdeath/momdeath_00016.webp"
    pause insertvar
    "images/inserts/momdeath/momdeath_00017.webp"
    pause insertvar
    "images/inserts/momdeath/momdeath_00018.webp"
    pause insertvar
    "images/inserts/momdeath/momdeath_00019.webp"
    pause insertvar
    "images/inserts/momdeath/momdeath_00020.webp"
    pause insertvar
    "images/inserts/momdeath/momdeath_00021.webp"
    pause insertvar
    "images/inserts/momdeath/momdeath_00022.webp"
    pause insertvar
    "images/inserts/momdeath/momdeath_00023.webp"
    pause insertvar
    "images/inserts/momdeath/momdeath_00024.webp"
    pause insertvar
    "images/inserts/momdeath/momdeath_00025.webp"
    pause insertvar
    repeat


image treeroot: 
    "images/inserts/treeroot/treeroot_00000.webp"
    pause insertvar
    "images/inserts/treeroot/treeroot_00001.webp"
    pause insertvar
    "images/inserts/treeroot/treeroot_00002.webp"
    pause insertvar
    "images/inserts/treeroot/treeroot_00003.webp"
    pause insertvar
    "images/inserts/treeroot/treeroot_00004.webp"
    pause insertvar
    "images/inserts/treeroot/treeroot_00005.webp"
    pause insertvar
    "images/inserts/treeroot/treeroot_00006.webp"
    pause insertvar
    "images/inserts/treeroot/treeroot_00007.webp"
    pause insertvar
    "images/inserts/treeroot/treeroot_00008.webp"
    pause insertvar
    "images/inserts/treeroot/treeroot_00009.webp"
    pause insertvar
    "images/inserts/treeroot/treeroot_00010.webp"
    pause insertvar
    "images/inserts/treeroot/treeroot_00011.webp"
    pause insertvar
    "images/inserts/treeroot/treeroot_00012.webp"
    pause insertvar
    "images/inserts/treeroot/treeroot_00013.webp"
    pause insertvar
    "images/inserts/treeroot/treeroot_00014.webp"
    pause insertvar
    "images/inserts/treeroot/treeroot_00015.webp"
    pause insertvar
    "images/inserts/treeroot/treeroot_00016.webp"
    pause insertvar
    "images/inserts/treeroot/treeroot_00017.webp"
    pause insertvar
    "images/inserts/treeroot/treeroot_00018.webp"
    pause insertvar
    "images/inserts/treeroot/treeroot_00019.webp"
    pause insertvar
    "images/inserts/treeroot/treeroot_00020.webp"
    pause insertvar
    "images/inserts/treeroot/treeroot_00021.webp"
    pause insertvar
    "images/inserts/treeroot/treeroot_00022.webp"
    pause insertvar
    "images/inserts/treeroot/treeroot_00023.webp"
    pause insertvar
    "images/inserts/treeroot/treeroot_00024.webp"
    pause insertvar
    "images/inserts/treeroot/treeroot_00025.webp"
    pause insertvar
    "images/inserts/treeroot/treeroot_00026.webp"
    pause insertvar
    "images/inserts/treeroot/treeroot_00027.webp"
    pause insertvar
    "images/inserts/treeroot/treeroot_00028.webp"
    pause insertvar
    "images/inserts/treeroot/treeroot_00029.webp"
    pause insertvar
    repeat


image minarash: 
    "images/inserts/minarash/minarash_00000.webp"
    pause insertvar
    "images/inserts/minarash/minarash_00001.webp"
    pause insertvar
    "images/inserts/minarash/minarash_00002.webp"
    pause insertvar
    "images/inserts/minarash/minarash_00003.webp"
    pause insertvar
    "images/inserts/minarash/minarash_00004.webp"
    pause insertvar
    "images/inserts/minarash/minarash_00005.webp"
    pause insertvar
    "images/inserts/minarash/minarash_00006.webp"
    pause insertvar
    "images/inserts/minarash/minarash_00007.webp"
    pause insertvar
    "images/inserts/minarash/minarash_00008.webp"
    pause insertvar
    "images/inserts/minarash/minarash_00009.webp"
    pause insertvar
    "images/inserts/minarash/minarash_00010.webp"
    pause insertvar
    "images/inserts/minarash/minarash_00011.webp"
    pause insertvar
    "images/inserts/minarash/minarash_00012.webp"
    pause insertvar
    "images/inserts/minarash/minarash_00013.webp"
    pause insertvar
    "images/inserts/minarash/minarash_00014.webp"
    pause insertvar
    "images/inserts/minarash/minarash_00015.webp"
    pause insertvar
    "images/inserts/minarash/minarash_00016.webp"
    pause insertvar
    "images/inserts/minarash/minarash_00017.webp"
    pause insertvar
    "images/inserts/minarash/minarash_00018.webp"
    pause insertvar
    "images/inserts/minarash/minarash_00019.webp"
    pause insertvar
    "images/inserts/minarash/minarash_00020.webp"
    pause insertvar
    "images/inserts/minarash/minarash_00021.webp"
    pause insertvar
    "images/inserts/minarash/minarash_00022.webp"
    pause insertvar
    "images/inserts/minarash/minarash_00023.webp"
    pause insertvar
    "images/inserts/minarash/minarash_00024.webp"
    pause insertvar
    "images/inserts/minarash/minarash_00025.webp"
    pause insertvar
    "images/inserts/minarash/minarash_00026.webp"
    pause insertvar
    "images/inserts/minarash/minarash_00027.webp"
    pause insertvar
    "images/inserts/minarash/minarash_00028.webp"
    pause insertvar
    "images/inserts/minarash/minarash_00029.webp"
    pause insertvar
    repeat


image rexstare: 
    "images/inserts/rexstare/rexstare_00000.webp"
    pause insertvar
    "images/inserts/rexstare/rexstare_00001.webp"
    pause insertvar
    "images/inserts/rexstare/rexstare_00002.webp"
    pause insertvar
    "images/inserts/rexstare/rexstare_00003.webp"
    pause insertvar
    "images/inserts/rexstare/rexstare_00004.webp"
    pause insertvar
    "images/inserts/rexstare/rexstare_00005.webp"
    pause insertvar
    "images/inserts/rexstare/rexstare_00006.webp"
    pause insertvar
    "images/inserts/rexstare/rexstare_00007.webp"
    pause insertvar
    "images/inserts/rexstare/rexstare_00008.webp"
    pause insertvar
    "images/inserts/rexstare/rexstare_00009.webp"
    pause insertvar
    "images/inserts/rexstare/rexstare_00010.webp"
    pause insertvar
    "images/inserts/rexstare/rexstare_00011.webp"
    pause insertvar
    "images/inserts/rexstare/rexstare_00012.webp"
    pause insertvar
    "images/inserts/rexstare/rexstare_00013.webp"
    pause insertvar
    "images/inserts/rexstare/rexstare_00014.webp"
    pause insertvar
    "images/inserts/rexstare/rexstare_00015.webp"
    pause insertvar
    "images/inserts/rexstare/rexstare_00016.webp"
    pause insertvar
    "images/inserts/rexstare/rexstare_00017.webp"
    pause insertvar
    "images/inserts/rexstare/rexstare_00018.webp"
    pause insertvar
    "images/inserts/rexstare/rexstare_00019.webp"
    pause insertvar
    "images/inserts/rexstare/rexstare_00020.webp"
    pause insertvar
    "images/inserts/rexstare/rexstare_00021.webp"
    pause insertvar
    "images/inserts/rexstare/rexstare_00022.webp"
    pause insertvar
    "images/inserts/rexstare/rexstare_00023.webp"
    pause insertvar
    "images/inserts/rexstare/rexstare_00024.webp"
    pause insertvar
    "images/inserts/rexstare/rexstare_00025.webp"
    pause insertvar
    "images/inserts/rexstare/rexstare_00026.webp"
    pause insertvar
    "images/inserts/rexstare/rexstare_00027.webp"
    pause insertvar
    "images/inserts/rexstare/rexstare_00028.webp"
    pause insertvar
    "images/inserts/rexstare/rexstare_00029.webp"
    pause insertvar
    repeat


image minarexstart: 
    "images/inserts/minarexstart/minarexstart_00000.webp"
    pause insertvar
    "images/inserts/minarexstart/minarexstart_00001.webp"
    pause insertvar
    "images/inserts/minarexstart/minarexstart_00002.webp"
    pause insertvar
    "images/inserts/minarexstart/minarexstart_00003.webp"
    pause insertvar
    "images/inserts/minarexstart/minarexstart_00004.webp"
    pause insertvar
    "images/inserts/minarexstart/minarexstart_00005.webp"
    pause insertvar
    "images/inserts/minarexstart/minarexstart_00006.webp"
    pause insertvar
    "images/inserts/minarexstart/minarexstart_00007.webp"
    pause insertvar
    "images/inserts/minarexstart/minarexstart_00008.webp"
    pause insertvar
    "images/inserts/minarexstart/minarexstart_00009.webp"
    pause insertvar
    "images/inserts/minarexstart/minarexstart_00010.webp"
    pause insertvar
    "images/inserts/minarexstart/minarexstart_00011.webp"
    pause insertvar
    "images/inserts/minarexstart/minarexstart_00012.webp"
    pause insertvar
    "images/inserts/minarexstart/minarexstart_00013.webp"
    pause insertvar
    "images/inserts/minarexstart/minarexstart_00014.webp"
    pause insertvar
    "images/inserts/minarexstart/minarexstart_00015.webp"
    pause insertvar
    "images/inserts/minarexstart/minarexstart_00016.webp"
    pause insertvar
    "images/inserts/minarexstart/minarexstart_00017.webp"
    pause insertvar
    "images/inserts/minarexstart/minarexstart_00018.webp"
    pause insertvar
    "images/inserts/minarexstart/minarexstart_00019.webp"
    pause insertvar
    "images/inserts/minarexstart/minarexstart_00020.webp"
    pause insertvar
    "images/inserts/minarexstart/minarexstart_00021.webp"
    pause insertvar
    "images/inserts/minarexstart/minarexstart_00022.webp"
    pause insertvar
    "images/inserts/minarexstart/minarexstart_00023.webp"
    pause insertvar
    "images/inserts/minarexstart/minarexstart_00024.webp"
    pause insertvar
    "images/inserts/minarexstart/minarexstart_00025.webp"
    pause insertvar
    repeat


image creamtube: 
    "images/inserts/creamtube/creamtube_00000.webp"
    pause insertvar
    "images/inserts/creamtube/creamtube_00001.webp"
    pause insertvar
    "images/inserts/creamtube/creamtube_00002.webp"
    pause insertvar
    "images/inserts/creamtube/creamtube_00003.webp"
    pause insertvar
    "images/inserts/creamtube/creamtube_00004.webp"
    pause insertvar
    "images/inserts/creamtube/creamtube_00005.webp"
    pause insertvar
    "images/inserts/creamtube/creamtube_00006.webp"
    pause insertvar
    "images/inserts/creamtube/creamtube_00007.webp"
    pause insertvar
    "images/inserts/creamtube/creamtube_00008.webp"
    pause insertvar
    "images/inserts/creamtube/creamtube_00009.webp"
    pause insertvar
    "images/inserts/creamtube/creamtube_00010.webp"
    pause insertvar
    "images/inserts/creamtube/creamtube_00011.webp"
    pause insertvar
    "images/inserts/creamtube/creamtube_00012.webp"
    pause insertvar
    "images/inserts/creamtube/creamtube_00013.webp"
    pause insertvar
    "images/inserts/creamtube/creamtube_00014.webp"
    pause insertvar
    "images/inserts/creamtube/creamtube_00015.webp"
    pause insertvar
    "images/inserts/creamtube/creamtube_00016.webp"
    pause insertvar
    "images/inserts/creamtube/creamtube_00017.webp"
    pause insertvar
    "images/inserts/creamtube/creamtube_00018.webp"
    pause insertvar
    "images/inserts/creamtube/creamtube_00019.webp"
    pause insertvar
    "images/inserts/creamtube/creamtube_00020.webp"
    pause insertvar
    "images/inserts/creamtube/creamtube_00021.webp"
    pause insertvar
    "images/inserts/creamtube/creamtube_00022.webp"
    pause insertvar
    "images/inserts/creamtube/creamtube_00023.webp"
    pause insertvar
    "images/inserts/creamtube/creamtube_00024.webp"
    pause insertvar
    "images/inserts/creamtube/creamtube_00025.webp"
    pause insertvar
    "images/inserts/creamtube/creamtube_00026.webp"
    pause insertvar
    "images/inserts/creamtube/creamtube_00027.webp"
    pause insertvar
    "images/inserts/creamtube/creamtube_00028.webp"
    pause insertvar
    "images/inserts/creamtube/creamtube_00029.webp"
    pause insertvar
    repeat


image minadadeye: 
    "images/inserts/minadadeye/minadadeye_00000.webp"
    pause insertvar
    "images/inserts/minadadeye/minadadeye_00001.webp"
    pause insertvar
    "images/inserts/minadadeye/minadadeye_00002.webp"
    pause insertvar
    "images/inserts/minadadeye/minadadeye_00003.webp"
    pause insertvar
    "images/inserts/minadadeye/minadadeye_00004.webp"
    pause insertvar
    "images/inserts/minadadeye/minadadeye_00005.webp"
    pause insertvar
    "images/inserts/minadadeye/minadadeye_00006.webp"
    pause insertvar
    "images/inserts/minadadeye/minadadeye_00007.webp"
    pause insertvar
    "images/inserts/minadadeye/minadadeye_00008.webp"
    pause insertvar
    "images/inserts/minadadeye/minadadeye_00009.webp"
    pause insertvar
    "images/inserts/minadadeye/minadadeye_00010.webp"
    pause insertvar
    "images/inserts/minadadeye/minadadeye_00011.webp"
    pause insertvar
    "images/inserts/minadadeye/minadadeye_00012.webp"
    pause insertvar
    "images/inserts/minadadeye/minadadeye_00013.webp"
    pause insertvar
    "images/inserts/minadadeye/minadadeye_00014.webp"
    pause insertvar
    "images/inserts/minadadeye/minadadeye_00015.webp"
    pause insertvar
    "images/inserts/minadadeye/minadadeye_00016.webp"
    pause insertvar
    "images/inserts/minadadeye/minadadeye_00017.webp"
    pause insertvar
    "images/inserts/minadadeye/minadadeye_00018.webp"
    pause insertvar
    "images/inserts/minadadeye/minadadeye_00019.webp"
    pause insertvar
    "images/inserts/minadadeye/minadadeye_00020.webp"
    pause insertvar
    "images/inserts/minadadeye/minadadeye_00021.webp"
    pause insertvar
    "images/inserts/minadadeye/minadadeye_00022.webp"
    pause insertvar
    "images/inserts/minadadeye/minadadeye_00023.webp"
    pause insertvar
    "images/inserts/minadadeye/minadadeye_00024.webp"
    pause insertvar
    "images/inserts/minadadeye/minadadeye_00025.webp"
    pause insertvar
    repeat


image confrontationtwo: 
    "images/inserts/confrontationtwo/confrontationtwo_00000.webp"
    pause insertvar
    "images/inserts/confrontationtwo/confrontationtwo_00001.webp"
    pause insertvar
    "images/inserts/confrontationtwo/confrontationtwo_00002.webp"
    pause insertvar
    "images/inserts/confrontationtwo/confrontationtwo_00003.webp"
    pause insertvar
    "images/inserts/confrontationtwo/confrontationtwo_00004.webp"
    pause insertvar
    "images/inserts/confrontationtwo/confrontationtwo_00005.webp"
    pause insertvar
    "images/inserts/confrontationtwo/confrontationtwo_00006.webp"
    pause insertvar
    "images/inserts/confrontationtwo/confrontationtwo_00007.webp"
    pause insertvar
    "images/inserts/confrontationtwo/confrontationtwo_00008.webp"
    pause insertvar
    "images/inserts/confrontationtwo/confrontationtwo_00009.webp"
    pause insertvar
    "images/inserts/confrontationtwo/confrontationtwo_00010.webp"
    pause insertvar
    "images/inserts/confrontationtwo/confrontationtwo_00011.webp"
    pause insertvar
    "images/inserts/confrontationtwo/confrontationtwo_00012.webp"
    pause insertvar
    "images/inserts/confrontationtwo/confrontationtwo_00013.webp"
    pause insertvar
    "images/inserts/confrontationtwo/confrontationtwo_00014.webp"
    pause insertvar
    "images/inserts/confrontationtwo/confrontationtwo_00015.webp"
    pause insertvar
    "images/inserts/confrontationtwo/confrontationtwo_00016.webp"
    pause insertvar
    "images/inserts/confrontationtwo/confrontationtwo_00017.webp"
    pause insertvar
    "images/inserts/confrontationtwo/confrontationtwo_00018.webp"
    pause insertvar
    "images/inserts/confrontationtwo/confrontationtwo_00019.webp"
    pause insertvar
    "images/inserts/confrontationtwo/confrontationtwo_00020.webp"
    pause insertvar
    "images/inserts/confrontationtwo/confrontationtwo_00021.webp"
    pause insertvar
    "images/inserts/confrontationtwo/confrontationtwo_00022.webp"
    pause insertvar
    "images/inserts/confrontationtwo/confrontationtwo_00023.webp"
    pause insertvar
    "images/inserts/confrontationtwo/confrontationtwo_00024.webp"
    pause insertvar
    "images/inserts/confrontationtwo/confrontationtwo_00025.webp"
    pause insertvar
    repeat


image rexrat: 
    "images/inserts/rexrat/rexrat_00000.webp"
    pause insertvar
    "images/inserts/rexrat/rexrat_00001.webp"
    pause insertvar
    "images/inserts/rexrat/rexrat_00002.webp"
    pause insertvar
    "images/inserts/rexrat/rexrat_00003.webp"
    pause insertvar
    "images/inserts/rexrat/rexrat_00004.webp"
    pause insertvar
    "images/inserts/rexrat/rexrat_00005.webp"
    pause insertvar
    "images/inserts/rexrat/rexrat_00006.webp"
    pause insertvar
    "images/inserts/rexrat/rexrat_00007.webp"
    pause insertvar
    "images/inserts/rexrat/rexrat_00008.webp"
    pause insertvar
    "images/inserts/rexrat/rexrat_00009.webp"
    pause insertvar
    "images/inserts/rexrat/rexrat_00010.webp"
    pause insertvar
    "images/inserts/rexrat/rexrat_00011.webp"
    pause insertvar
    "images/inserts/rexrat/rexrat_00012.webp"
    pause insertvar
    "images/inserts/rexrat/rexrat_00013.webp"
    pause insertvar
    "images/inserts/rexrat/rexrat_00014.webp"
    pause insertvar
    "images/inserts/rexrat/rexrat_00015.webp"
    pause insertvar
    "images/inserts/rexrat/rexrat_00016.webp"
    pause insertvar
    "images/inserts/rexrat/rexrat_00017.webp"
    pause insertvar
    "images/inserts/rexrat/rexrat_00018.webp"
    pause insertvar
    "images/inserts/rexrat/rexrat_00019.webp"
    pause insertvar
    "images/inserts/rexrat/rexrat_00020.webp"
    pause insertvar
    "images/inserts/rexrat/rexrat_00021.webp"
    pause insertvar
    "images/inserts/rexrat/rexrat_00022.webp"
    pause insertvar
    "images/inserts/rexrat/rexrat_00023.webp"
    pause insertvar
    "images/inserts/rexrat/rexrat_00024.webp"
    pause insertvar
    "images/inserts/rexrat/rexrat_00025.webp"
    pause insertvar
    repeat



image fathercloseup: 
    "images/inserts/fathercloseup/fathercloseup_00000.webp"
    pause insertvar
    "images/inserts/fathercloseup/fathercloseup_00001.webp"
    pause insertvar
    "images/inserts/fathercloseup/fathercloseup_00002.webp"
    pause insertvar
    "images/inserts/fathercloseup/fathercloseup_00003.webp"
    pause insertvar
    "images/inserts/fathercloseup/fathercloseup_00004.webp"
    pause insertvar
    "images/inserts/fathercloseup/fathercloseup_00005.webp"
    pause insertvar
    "images/inserts/fathercloseup/fathercloseup_00006.webp"
    pause insertvar
    "images/inserts/fathercloseup/fathercloseup_00007.webp"
    pause insertvar
    "images/inserts/fathercloseup/fathercloseup_00008.webp"
    pause insertvar
    "images/inserts/fathercloseup/fathercloseup_00009.webp"
    pause insertvar
    "images/inserts/fathercloseup/fathercloseup_00010.webp"
    pause insertvar
    "images/inserts/fathercloseup/fathercloseup_00011.webp"
    pause insertvar
    "images/inserts/fathercloseup/fathercloseup_00012.webp"
    pause insertvar
    "images/inserts/fathercloseup/fathercloseup_00013.webp"
    pause insertvar
    "images/inserts/fathercloseup/fathercloseup_00014.webp"
    pause insertvar
    "images/inserts/fathercloseup/fathercloseup_00015.webp"
    pause insertvar
    "images/inserts/fathercloseup/fathercloseup_00016.webp"
    pause insertvar
    "images/inserts/fathercloseup/fathercloseup_00017.webp"
    pause insertvar
    "images/inserts/fathercloseup/fathercloseup_00018.webp"
    pause insertvar
    "images/inserts/fathercloseup/fathercloseup_00019.webp"
    pause insertvar
    "images/inserts/fathercloseup/fathercloseup_00020.webp"
    pause insertvar
    "images/inserts/fathercloseup/fathercloseup_00021.webp"
    pause insertvar
    "images/inserts/fathercloseup/fathercloseup_00022.webp"
    pause insertvar
    "images/inserts/fathercloseup/fathercloseup_00023.webp"
    pause insertvar
    "images/inserts/fathercloseup/fathercloseup_00024.webp"
    pause insertvar
    "images/inserts/fathercloseup/fathercloseup_00025.webp"
    pause insertvar
    "images/inserts/fathercloseup/fathercloseup_00026.webp"
    pause insertvar
    "images/inserts/fathercloseup/fathercloseup_00027.webp"
    pause insertvar
    "images/inserts/fathercloseup/fathercloseup_00028.webp"
    pause insertvar
    "images/inserts/fathercloseup/fathercloseup_00029.webp"
    pause insertvar
    repeat


image heavenlymother: 
    "images/inserts/heavenlymother/heavenlymother_00000.webp"
    pause insertvar
    "images/inserts/heavenlymother/heavenlymother_00001.webp"
    pause insertvar
    "images/inserts/heavenlymother/heavenlymother_00002.webp"
    pause insertvar
    "images/inserts/heavenlymother/heavenlymother_00003.webp"
    pause insertvar
    "images/inserts/heavenlymother/heavenlymother_00004.webp"
    pause insertvar
    "images/inserts/heavenlymother/heavenlymother_00005.webp"
    pause insertvar
    "images/inserts/heavenlymother/heavenlymother_00006.webp"
    pause insertvar
    "images/inserts/heavenlymother/heavenlymother_00007.webp"
    pause insertvar
    "images/inserts/heavenlymother/heavenlymother_00008.webp"
    pause insertvar
    "images/inserts/heavenlymother/heavenlymother_00009.webp"
    pause insertvar
    "images/inserts/heavenlymother/heavenlymother_00010.webp"
    pause insertvar
    "images/inserts/heavenlymother/heavenlymother_00011.webp"
    pause insertvar
    "images/inserts/heavenlymother/heavenlymother_00012.webp"
    pause insertvar
    "images/inserts/heavenlymother/heavenlymother_00013.webp"
    pause insertvar
    "images/inserts/heavenlymother/heavenlymother_00014.webp"
    pause insertvar
    "images/inserts/heavenlymother/heavenlymother_00015.webp"
    pause insertvar
    "images/inserts/heavenlymother/heavenlymother_00016.webp"
    pause insertvar
    "images/inserts/heavenlymother/heavenlymother_00017.webp"
    pause insertvar
    "images/inserts/heavenlymother/heavenlymother_00018.webp"
    pause insertvar
    "images/inserts/heavenlymother/heavenlymother_00019.webp"
    pause insertvar
    "images/inserts/heavenlymother/heavenlymother_00020.webp"
    pause insertvar
    "images/inserts/heavenlymother/heavenlymother_00021.webp"
    pause insertvar
    "images/inserts/heavenlymother/heavenlymother_00022.webp"
    pause insertvar
    "images/inserts/heavenlymother/heavenlymother_00023.webp"
    pause insertvar
    "images/inserts/heavenlymother/heavenlymother_00024.webp"
    pause insertvar
    "images/inserts/heavenlymother/heavenlymother_00025.webp"
    pause insertvar
    "images/inserts/heavenlymother/heavenlymother_00026.webp"
    pause insertvar
    "images/inserts/heavenlymother/heavenlymother_00027.webp"
    pause insertvar
    "images/inserts/heavenlymother/heavenlymother_00028.webp"
    pause insertvar
    "images/inserts/heavenlymother/heavenlymother_00029.webp"
    pause insertvar
    repeat



image vase: 
    "images/inserts/vase/vase_00000.webp"
    pause insertvar
    "images/inserts/vase/vase_00001.webp"
    pause insertvar
    "images/inserts/vase/vase_00002.webp"
    pause insertvar
    "images/inserts/vase/vase_00003.webp"
    pause insertvar
    "images/inserts/vase/vase_00004.webp"
    pause insertvar
    "images/inserts/vase/vase_00005.webp"
    pause insertvar
    "images/inserts/vase/vase_00006.webp"
    pause insertvar
    "images/inserts/vase/vase_00007.webp"
    pause insertvar
    "images/inserts/vase/vase_00008.webp"
    pause insertvar
    "images/inserts/vase/vase_00009.webp"
    pause insertvar
    "images/inserts/vase/vase_00010.webp"
    pause insertvar
    "images/inserts/vase/vase_00011.webp"
    pause insertvar
    "images/inserts/vase/vase_00012.webp"
    pause insertvar
    "images/inserts/vase/vase_00013.webp"
    pause insertvar
    "images/inserts/vase/vase_00014.webp"
    pause insertvar
    "images/inserts/vase/vase_00015.webp"
    pause insertvar
    "images/inserts/vase/vase_00016.webp"
    pause insertvar
    "images/inserts/vase/vase_00017.webp"
    pause insertvar
    "images/inserts/vase/vase_00018.webp"
    pause insertvar
    "images/inserts/vase/vase_00019.webp"
    pause insertvar
    "images/inserts/vase/vase_00020.webp"
    pause insertvar
    "images/inserts/vase/vase_00021.webp"
    pause insertvar
    "images/inserts/vase/vase_00022.webp"
    pause insertvar
    "images/inserts/vase/vase_00023.webp"
    pause insertvar
    "images/inserts/vase/vase_00024.webp"
    pause insertvar
    "images/inserts/vase/vase_00025.webp"
    pause insertvar
    "images/inserts/vase/vase_00026.webp"
    pause insertvar
    "images/inserts/vase/vase_00027.webp"
    pause insertvar
    "images/inserts/vase/vase_00028.webp"
    pause insertvar
    "images/inserts/vase/vase_00029.webp"
    pause insertvar
    repeat

image escapeplanone: 
    "images/inserts/escapeplanone/escapeplanone_00000.webp"
    pause insertvar
    "images/inserts/escapeplanone/escapeplanone_00001.webp"
    pause insertvar
    "images/inserts/escapeplanone/escapeplanone_00002.webp"
    pause insertvar
    "images/inserts/escapeplanone/escapeplanone_00003.webp"
    pause insertvar
    "images/inserts/escapeplanone/escapeplanone_00004.webp"
    pause insertvar
    "images/inserts/escapeplanone/escapeplanone_00005.webp"
    pause insertvar
    "images/inserts/escapeplanone/escapeplanone_00006.webp"
    pause insertvar
    "images/inserts/escapeplanone/escapeplanone_00007.webp"
    pause insertvar
    "images/inserts/escapeplanone/escapeplanone_00008.webp"
    pause insertvar
    "images/inserts/escapeplanone/escapeplanone_00009.webp"
    pause insertvar
    "images/inserts/escapeplanone/escapeplanone_00010.webp"
    pause insertvar
    "images/inserts/escapeplanone/escapeplanone_00011.webp"
    pause insertvar
    "images/inserts/escapeplanone/escapeplanone_00012.webp"
    pause insertvar
    "images/inserts/escapeplanone/escapeplanone_00013.webp"
    pause insertvar
    "images/inserts/escapeplanone/escapeplanone_00014.webp"
    pause insertvar
    "images/inserts/escapeplanone/escapeplanone_00015.webp"
    pause insertvar
    "images/inserts/escapeplanone/escapeplanone_00016.webp"
    pause insertvar
    "images/inserts/escapeplanone/escapeplanone_00017.webp"
    pause insertvar
    "images/inserts/escapeplanone/escapeplanone_00018.webp"
    pause insertvar
    "images/inserts/escapeplanone/escapeplanone_00019.webp"
    pause insertvar
    "images/inserts/escapeplanone/escapeplanone_00020.webp"
    pause insertvar
    "images/inserts/escapeplanone/escapeplanone_00021.webp"
    pause insertvar
    "images/inserts/escapeplanone/escapeplanone_00022.webp"
    pause insertvar
    "images/inserts/escapeplanone/escapeplanone_00023.webp"
    pause insertvar
    "images/inserts/escapeplanone/escapeplanone_00024.webp"
    pause insertvar
    "images/inserts/escapeplanone/escapeplanone_00025.webp"
    pause insertvar
    repeat


image escapeplantwo: 
    "images/inserts/escapeplantwo/escapeplantwo_00000.webp"
    pause insertvar
    "images/inserts/escapeplantwo/escapeplantwo_00001.webp"
    pause insertvar
    "images/inserts/escapeplantwo/escapeplantwo_00002.webp"
    pause insertvar
    "images/inserts/escapeplantwo/escapeplantwo_00003.webp"
    pause insertvar
    "images/inserts/escapeplantwo/escapeplantwo_00004.webp"
    pause insertvar
    "images/inserts/escapeplantwo/escapeplantwo_00005.webp"
    pause insertvar
    "images/inserts/escapeplantwo/escapeplantwo_00006.webp"
    pause insertvar
    "images/inserts/escapeplantwo/escapeplantwo_00007.webp"
    pause insertvar
    "images/inserts/escapeplantwo/escapeplantwo_00008.webp"
    pause insertvar
    "images/inserts/escapeplantwo/escapeplantwo_00009.webp"
    pause insertvar
    "images/inserts/escapeplantwo/escapeplantwo_00010.webp"
    pause insertvar
    "images/inserts/escapeplantwo/escapeplantwo_00011.webp"
    pause insertvar
    "images/inserts/escapeplantwo/escapeplantwo_00012.webp"
    pause insertvar
    "images/inserts/escapeplantwo/escapeplantwo_00013.webp"
    pause insertvar
    "images/inserts/escapeplantwo/escapeplantwo_00014.webp"
    pause insertvar
    "images/inserts/escapeplantwo/escapeplantwo_00015.webp"
    pause insertvar
    "images/inserts/escapeplantwo/escapeplantwo_00016.webp"
    pause insertvar
    "images/inserts/escapeplantwo/escapeplantwo_00017.webp"
    pause insertvar
    "images/inserts/escapeplantwo/escapeplantwo_00018.webp"
    pause insertvar
    "images/inserts/escapeplantwo/escapeplantwo_00019.webp"
    pause insertvar
    "images/inserts/escapeplantwo/escapeplantwo_00020.webp"
    pause insertvar
    "images/inserts/escapeplantwo/escapeplantwo_00021.webp"
    pause insertvar
    "images/inserts/escapeplantwo/escapeplantwo_00022.webp"
    pause insertvar
    "images/inserts/escapeplantwo/escapeplantwo_00023.webp"
    pause insertvar
    "images/inserts/escapeplantwo/escapeplantwo_00024.webp"
    pause insertvar
    "images/inserts/escapeplantwo/escapeplantwo_00025.webp"
    pause insertvar
    repeat


image mafiameeting: 
    "images/inserts/mafiameeting/mafiameeting_00000.webp"
    pause insertvar
    "images/inserts/mafiameeting/mafiameeting_00001.webp"
    pause insertvar
    "images/inserts/mafiameeting/mafiameeting_00002.webp"
    pause insertvar
    "images/inserts/mafiameeting/mafiameeting_00003.webp"
    pause insertvar
    "images/inserts/mafiameeting/mafiameeting_00004.webp"
    pause insertvar
    "images/inserts/mafiameeting/mafiameeting_00005.webp"
    pause insertvar
    "images/inserts/mafiameeting/mafiameeting_00006.webp"
    pause insertvar
    "images/inserts/mafiameeting/mafiameeting_00007.webp"
    pause insertvar
    "images/inserts/mafiameeting/mafiameeting_00008.webp"
    pause insertvar
    "images/inserts/mafiameeting/mafiameeting_00009.webp"
    pause insertvar
    "images/inserts/mafiameeting/mafiameeting_00010.webp"
    pause insertvar
    "images/inserts/mafiameeting/mafiameeting_00011.webp"
    pause insertvar
    "images/inserts/mafiameeting/mafiameeting_00012.webp"
    pause insertvar
    "images/inserts/mafiameeting/mafiameeting_00013.webp"
    pause insertvar
    "images/inserts/mafiameeting/mafiameeting_00014.webp"
    pause insertvar
    "images/inserts/mafiameeting/mafiameeting_00015.webp"
    pause insertvar
    "images/inserts/mafiameeting/mafiameeting_00016.webp"
    pause insertvar
    "images/inserts/mafiameeting/mafiameeting_00017.webp"
    pause insertvar
    "images/inserts/mafiameeting/mafiameeting_00018.webp"
    pause insertvar
    "images/inserts/mafiameeting/mafiameeting_00019.webp"
    pause insertvar
    "images/inserts/mafiameeting/mafiameeting_00020.webp"
    pause insertvar
    "images/inserts/mafiameeting/mafiameeting_00021.webp"
    pause insertvar
    "images/inserts/mafiameeting/mafiameeting_00022.webp"
    pause insertvar
    "images/inserts/mafiameeting/mafiameeting_00023.webp"
    pause insertvar
    "images/inserts/mafiameeting/mafiameeting_00024.webp"
    pause insertvar
    "images/inserts/mafiameeting/mafiameeting_00025.webp"
    pause insertvar
    repeat


image stool: 
    "images/inserts/stool/stool_00000.webp"
    pause insertvar
    "images/inserts/stool/stool_00001.webp"
    pause insertvar
    "images/inserts/stool/stool_00002.webp"
    pause insertvar
    "images/inserts/stool/stool_00003.webp"
    pause insertvar
    "images/inserts/stool/stool_00004.webp"
    pause insertvar
    "images/inserts/stool/stool_00005.webp"
    pause insertvar
    "images/inserts/stool/stool_00006.webp"
    pause insertvar
    "images/inserts/stool/stool_00007.webp"
    pause insertvar
    "images/inserts/stool/stool_00008.webp"
    pause insertvar
    "images/inserts/stool/stool_00009.webp"
    pause insertvar
    "images/inserts/stool/stool_00010.webp"
    pause insertvar
    "images/inserts/stool/stool_00011.webp"
    pause insertvar
    "images/inserts/stool/stool_00012.webp"
    pause insertvar
    "images/inserts/stool/stool_00013.webp"
    pause insertvar
    "images/inserts/stool/stool_00014.webp"
    pause insertvar
    "images/inserts/stool/stool_00015.webp"
    pause insertvar
    "images/inserts/stool/stool_00016.webp"
    pause insertvar
    "images/inserts/stool/stool_00017.webp"
    pause insertvar
    "images/inserts/stool/stool_00018.webp"
    pause insertvar
    "images/inserts/stool/stool_00019.webp"
    pause insertvar
    "images/inserts/stool/stool_00020.webp"
    pause insertvar
    "images/inserts/stool/stool_00021.webp"
    pause insertvar
    "images/inserts/stool/stool_00022.webp"
    pause insertvar
    "images/inserts/stool/stool_00023.webp"
    pause insertvar
    "images/inserts/stool/stool_00024.webp"
    pause insertvar
    "images/inserts/stool/stool_00025.webp"
    pause insertvar
    "images/inserts/stool/stool_00026.webp"
    pause insertvar
    "images/inserts/stool/stool_00027.webp"
    pause insertvar
    "images/inserts/stool/stool_00028.webp"
    pause insertvar
    "images/inserts/stool/stool_00029.webp"
    pause insertvar
    repeat


image momdeadstool: 
    "images/inserts/momdeadstool/momdeadstool_00000.webp"
    pause insertvar
    "images/inserts/momdeadstool/momdeadstool_00001.webp"
    pause insertvar
    "images/inserts/momdeadstool/momdeadstool_00002.webp"
    pause insertvar
    "images/inserts/momdeadstool/momdeadstool_00003.webp"
    pause insertvar
    "images/inserts/momdeadstool/momdeadstool_00004.webp"
    pause insertvar
    "images/inserts/momdeadstool/momdeadstool_00005.webp"
    pause insertvar
    "images/inserts/momdeadstool/momdeadstool_00006.webp"
    pause insertvar
    "images/inserts/momdeadstool/momdeadstool_00007.webp"
    pause insertvar
    "images/inserts/momdeadstool/momdeadstool_00008.webp"
    pause insertvar
    "images/inserts/momdeadstool/momdeadstool_00009.webp"
    pause insertvar
    "images/inserts/momdeadstool/momdeadstool_00010.webp"
    pause insertvar
    "images/inserts/momdeadstool/momdeadstool_00011.webp"
    pause insertvar
    "images/inserts/momdeadstool/momdeadstool_00012.webp"
    pause insertvar
    "images/inserts/momdeadstool/momdeadstool_00013.webp"
    pause insertvar
    "images/inserts/momdeadstool/momdeadstool_00014.webp"
    pause insertvar
    "images/inserts/momdeadstool/momdeadstool_00015.webp"
    pause insertvar
    "images/inserts/momdeadstool/momdeadstool_00016.webp"
    pause insertvar
    "images/inserts/momdeadstool/momdeadstool_00017.webp"
    pause insertvar
    "images/inserts/momdeadstool/momdeadstool_00018.webp"
    pause insertvar
    "images/inserts/momdeadstool/momdeadstool_00019.webp"
    pause insertvar
    "images/inserts/momdeadstool/momdeadstool_00020.webp"
    pause insertvar
    "images/inserts/momdeadstool/momdeadstool_00021.webp"
    pause insertvar
    "images/inserts/momdeadstool/momdeadstool_00022.webp"
    pause insertvar
    "images/inserts/momdeadstool/momdeadstool_00023.webp"
    pause insertvar
    "images/inserts/momdeadstool/momdeadstool_00024.webp"
    pause insertvar
    "images/inserts/momdeadstool/momdeadstool_00025.webp"
    pause insertvar
    repeat


image minastareshock: 
    "images/inserts/minastareshock/minastareshock_00000.webp"
    pause insertvar
    "images/inserts/minastareshock/minastareshock_00001.webp"
    pause insertvar
    "images/inserts/minastareshock/minastareshock_00002.webp"
    pause insertvar
    "images/inserts/minastareshock/minastareshock_00003.webp"
    pause insertvar
    "images/inserts/minastareshock/minastareshock_00004.webp"
    pause insertvar
    "images/inserts/minastareshock/minastareshock_00005.webp"
    pause insertvar
    "images/inserts/minastareshock/minastareshock_00006.webp"
    pause insertvar
    "images/inserts/minastareshock/minastareshock_00007.webp"
    pause insertvar
    "images/inserts/minastareshock/minastareshock_00008.webp"
    pause insertvar
    "images/inserts/minastareshock/minastareshock_00009.webp"
    pause insertvar
    "images/inserts/minastareshock/minastareshock_00010.webp"
    pause insertvar
    "images/inserts/minastareshock/minastareshock_00011.webp"
    pause insertvar
    "images/inserts/minastareshock/minastareshock_00012.webp"
    pause insertvar
    "images/inserts/minastareshock/minastareshock_00013.webp"
    pause insertvar
    "images/inserts/minastareshock/minastareshock_00014.webp"
    pause insertvar
    "images/inserts/minastareshock/minastareshock_00015.webp"
    pause insertvar
    "images/inserts/minastareshock/minastareshock_00016.webp"
    pause insertvar
    "images/inserts/minastareshock/minastareshock_00017.webp"
    pause insertvar
    "images/inserts/minastareshock/minastareshock_00018.webp"
    pause insertvar
    "images/inserts/minastareshock/minastareshock_00019.webp"
    pause insertvar
    "images/inserts/minastareshock/minastareshock_00020.webp"
    pause insertvar
    "images/inserts/minastareshock/minastareshock_00021.webp"
    pause insertvar
    "images/inserts/minastareshock/minastareshock_00022.webp"
    pause insertvar
    "images/inserts/minastareshock/minastareshock_00023.webp"
    pause insertvar
    "images/inserts/minastareshock/minastareshock_00024.webp"
    pause insertvar
    "images/inserts/minastareshock/minastareshock_00025.webp"
    pause insertvar
    "images/inserts/minastareshock/minastareshock_00026.webp"
    pause insertvar
    "images/inserts/minastareshock/minastareshock_00027.webp"
    pause insertvar
    "images/inserts/minastareshock/minastareshock_00028.webp"
    pause insertvar
    "images/inserts/minastareshock/minastareshock_00029.webp"
    pause insertvar
    repeat


image rexmomhome: 
    "images/inserts/rexmomhome/rexmomhome_00000.webp"
    pause insertvar
    "images/inserts/rexmomhome/rexmomhome_00001.webp"
    pause insertvar
    "images/inserts/rexmomhome/rexmomhome_00002.webp"
    pause insertvar
    "images/inserts/rexmomhome/rexmomhome_00003.webp"
    pause insertvar
    "images/inserts/rexmomhome/rexmomhome_00004.webp"
    pause insertvar
    "images/inserts/rexmomhome/rexmomhome_00005.webp"
    pause insertvar
    "images/inserts/rexmomhome/rexmomhome_00006.webp"
    pause insertvar
    "images/inserts/rexmomhome/rexmomhome_00007.webp"
    pause insertvar
    "images/inserts/rexmomhome/rexmomhome_00008.webp"
    pause insertvar
    "images/inserts/rexmomhome/rexmomhome_00009.webp"
    pause insertvar
    "images/inserts/rexmomhome/rexmomhome_00010.webp"
    pause insertvar
    "images/inserts/rexmomhome/rexmomhome_00011.webp"
    pause insertvar
    "images/inserts/rexmomhome/rexmomhome_00012.webp"
    pause insertvar
    "images/inserts/rexmomhome/rexmomhome_00013.webp"
    pause insertvar
    "images/inserts/rexmomhome/rexmomhome_00014.webp"
    pause insertvar
    "images/inserts/rexmomhome/rexmomhome_00015.webp"
    pause insertvar
    "images/inserts/rexmomhome/rexmomhome_00016.webp"
    pause insertvar
    "images/inserts/rexmomhome/rexmomhome_00017.webp"
    pause insertvar
    "images/inserts/rexmomhome/rexmomhome_00018.webp"
    pause insertvar
    "images/inserts/rexmomhome/rexmomhome_00019.webp"
    pause insertvar
    "images/inserts/rexmomhome/rexmomhome_00020.webp"
    pause insertvar
    "images/inserts/rexmomhome/rexmomhome_00021.webp"
    pause insertvar
    "images/inserts/rexmomhome/rexmomhome_00022.webp"
    pause insertvar
    "images/inserts/rexmomhome/rexmomhome_00023.webp"
    pause insertvar
    "images/inserts/rexmomhome/rexmomhome_00024.webp"
    pause insertvar
    "images/inserts/rexmomhome/rexmomhome_00025.webp"
    pause insertvar
    repeat


image roottwo: 
    "images/inserts/roottwo/roottwo_00000.webp"
    pause insertvar
    "images/inserts/roottwo/roottwo_00001.webp"
    pause insertvar
    "images/inserts/roottwo/roottwo_00002.webp"
    pause insertvar
    "images/inserts/roottwo/roottwo_00003.webp"
    pause insertvar
    "images/inserts/roottwo/roottwo_00004.webp"
    pause insertvar
    "images/inserts/roottwo/roottwo_00005.webp"
    pause insertvar
    "images/inserts/roottwo/roottwo_00006.webp"
    pause insertvar
    "images/inserts/roottwo/roottwo_00007.webp"
    pause insertvar
    "images/inserts/roottwo/roottwo_00008.webp"
    pause insertvar
    "images/inserts/roottwo/roottwo_00009.webp"
    pause insertvar
    "images/inserts/roottwo/roottwo_00010.webp"
    pause insertvar
    "images/inserts/roottwo/roottwo_00011.webp"
    pause insertvar
    "images/inserts/roottwo/roottwo_00012.webp"
    pause insertvar
    "images/inserts/roottwo/roottwo_00013.webp"
    pause insertvar
    "images/inserts/roottwo/roottwo_00014.webp"
    pause insertvar
    "images/inserts/roottwo/roottwo_00015.webp"
    pause insertvar
    "images/inserts/roottwo/roottwo_00016.webp"
    pause insertvar
    "images/inserts/roottwo/roottwo_00017.webp"
    pause insertvar
    "images/inserts/roottwo/roottwo_00018.webp"
    pause insertvar
    "images/inserts/roottwo/roottwo_00019.webp"
    pause insertvar
    "images/inserts/roottwo/roottwo_00020.webp"
    pause insertvar
    "images/inserts/roottwo/roottwo_00021.webp"
    pause insertvar
    "images/inserts/roottwo/roottwo_00022.webp"
    pause insertvar
    "images/inserts/roottwo/roottwo_00023.webp"
    pause insertvar
    "images/inserts/roottwo/roottwo_00024.webp"
    pause insertvar
    "images/inserts/roottwo/roottwo_00025.webp"
    pause insertvar
    "images/inserts/roottwo/roottwo_00026.webp"
    pause insertvar
    "images/inserts/roottwo/roottwo_00027.webp"
    pause insertvar
    "images/inserts/roottwo/roottwo_00028.webp"
    pause insertvar
    "images/inserts/roottwo/roottwo_00029.webp"
    pause insertvar
    repeat


image redflowerclose: 
    "images/inserts/redflowerclose/redflowerclose_00000.webp"
    pause insertvar
    "images/inserts/redflowerclose/redflowerclose_00001.webp"
    pause insertvar
    "images/inserts/redflowerclose/redflowerclose_00002.webp"
    pause insertvar
    "images/inserts/redflowerclose/redflowerclose_00003.webp"
    pause insertvar
    "images/inserts/redflowerclose/redflowerclose_00004.webp"
    pause insertvar
    "images/inserts/redflowerclose/redflowerclose_00005.webp"
    pause insertvar
    "images/inserts/redflowerclose/redflowerclose_00006.webp"
    pause insertvar
    "images/inserts/redflowerclose/redflowerclose_00007.webp"
    pause insertvar
    "images/inserts/redflowerclose/redflowerclose_00008.webp"
    pause insertvar
    "images/inserts/redflowerclose/redflowerclose_00009.webp"
    pause insertvar
    "images/inserts/redflowerclose/redflowerclose_00010.webp"
    pause insertvar
    "images/inserts/redflowerclose/redflowerclose_00011.webp"
    pause insertvar
    "images/inserts/redflowerclose/redflowerclose_00012.webp"
    pause insertvar
    "images/inserts/redflowerclose/redflowerclose_00013.webp"
    pause insertvar
    "images/inserts/redflowerclose/redflowerclose_00014.webp"
    pause insertvar
    "images/inserts/redflowerclose/redflowerclose_00015.webp"
    pause insertvar
    "images/inserts/redflowerclose/redflowerclose_00016.webp"
    pause insertvar
    "images/inserts/redflowerclose/redflowerclose_00017.webp"
    pause insertvar
    "images/inserts/redflowerclose/redflowerclose_00018.webp"
    pause insertvar
    "images/inserts/redflowerclose/redflowerclose_00019.webp"
    pause insertvar
    "images/inserts/redflowerclose/redflowerclose_00020.webp"
    pause insertvar
    "images/inserts/redflowerclose/redflowerclose_00021.webp"
    pause insertvar
    "images/inserts/redflowerclose/redflowerclose_00022.webp"
    pause insertvar
    "images/inserts/redflowerclose/redflowerclose_00023.webp"
    pause insertvar
    "images/inserts/redflowerclose/redflowerclose_00024.webp"
    pause insertvar
    "images/inserts/redflowerclose/redflowerclose_00025.webp"
    pause insertvar
    "images/inserts/redflowerclose/redflowerclose_00026.webp"
    pause insertvar
    "images/inserts/redflowerclose/redflowerclose_00027.webp"
    pause insertvar
    "images/inserts/redflowerclose/redflowerclose_00028.webp"
    pause insertvar
    "images/inserts/redflowerclose/redflowerclose_00029.webp"
    pause insertvar
    repeat


image slenderbone: 
    "images/inserts/slenderbone/slenderbone_00000.webp"
    pause insertvar
    "images/inserts/slenderbone/slenderbone_00001.webp"
    pause insertvar
    "images/inserts/slenderbone/slenderbone_00002.webp"
    pause insertvar
    "images/inserts/slenderbone/slenderbone_00003.webp"
    pause insertvar
    "images/inserts/slenderbone/slenderbone_00004.webp"
    pause insertvar
    "images/inserts/slenderbone/slenderbone_00005.webp"
    pause insertvar
    "images/inserts/slenderbone/slenderbone_00006.webp"
    pause insertvar
    "images/inserts/slenderbone/slenderbone_00007.webp"
    pause insertvar
    "images/inserts/slenderbone/slenderbone_00008.webp"
    pause insertvar
    "images/inserts/slenderbone/slenderbone_00009.webp"
    pause insertvar
    "images/inserts/slenderbone/slenderbone_00010.webp"
    pause insertvar
    "images/inserts/slenderbone/slenderbone_00011.webp"
    pause insertvar
    "images/inserts/slenderbone/slenderbone_00012.webp"
    pause insertvar
    "images/inserts/slenderbone/slenderbone_00013.webp"
    pause insertvar
    "images/inserts/slenderbone/slenderbone_00014.webp"
    pause insertvar
    "images/inserts/slenderbone/slenderbone_00015.webp"
    pause insertvar
    "images/inserts/slenderbone/slenderbone_00016.webp"
    pause insertvar
    "images/inserts/slenderbone/slenderbone_00017.webp"
    pause insertvar
    "images/inserts/slenderbone/slenderbone_00018.webp"
    pause insertvar
    "images/inserts/slenderbone/slenderbone_00019.webp"
    pause insertvar
    "images/inserts/slenderbone/slenderbone_00020.webp"
    pause insertvar
    "images/inserts/slenderbone/slenderbone_00021.webp"
    pause insertvar
    "images/inserts/slenderbone/slenderbone_00022.webp"
    pause insertvar
    "images/inserts/slenderbone/slenderbone_00023.webp"
    pause insertvar
    "images/inserts/slenderbone/slenderbone_00024.webp"
    pause insertvar
    "images/inserts/slenderbone/slenderbone_00025.webp"
    pause insertvar
    "images/inserts/slenderbone/slenderbone_00026.webp"
    pause insertvar
    "images/inserts/slenderbone/slenderbone_00027.webp"
    pause insertvar
    "images/inserts/slenderbone/slenderbone_00028.webp"
    pause insertvar
    "images/inserts/slenderbone/slenderbone_00029.webp"
    pause insertvar
    repeat


image fathersus: 
    "images/inserts/fathersus/fathersus_00000.webp"
    pause insertvar
    "images/inserts/fathersus/fathersus_00001.webp"
    pause insertvar
    "images/inserts/fathersus/fathersus_00002.webp"
    pause insertvar
    "images/inserts/fathersus/fathersus_00003.webp"
    pause insertvar
    "images/inserts/fathersus/fathersus_00004.webp"
    pause insertvar
    "images/inserts/fathersus/fathersus_00005.webp"
    pause insertvar
    "images/inserts/fathersus/fathersus_00006.webp"
    pause insertvar
    "images/inserts/fathersus/fathersus_00007.webp"
    pause insertvar
    "images/inserts/fathersus/fathersus_00008.webp"
    pause insertvar
    "images/inserts/fathersus/fathersus_00009.webp"
    pause insertvar
    "images/inserts/fathersus/fathersus_00010.webp"
    pause insertvar
    "images/inserts/fathersus/fathersus_00011.webp"
    pause insertvar
    "images/inserts/fathersus/fathersus_00012.webp"
    pause insertvar
    "images/inserts/fathersus/fathersus_00013.webp"
    pause insertvar
    "images/inserts/fathersus/fathersus_00014.webp"
    pause insertvar
    "images/inserts/fathersus/fathersus_00015.webp"
    pause insertvar
    "images/inserts/fathersus/fathersus_00016.webp"
    pause insertvar
    "images/inserts/fathersus/fathersus_00017.webp"
    pause insertvar
    "images/inserts/fathersus/fathersus_00018.webp"
    pause insertvar
    "images/inserts/fathersus/fathersus_00019.webp"
    pause insertvar
    "images/inserts/fathersus/fathersus_00020.webp"
    pause insertvar
    "images/inserts/fathersus/fathersus_00021.webp"
    pause insertvar
    "images/inserts/fathersus/fathersus_00022.webp"
    pause insertvar
    "images/inserts/fathersus/fathersus_00023.webp"
    pause insertvar
    "images/inserts/fathersus/fathersus_00024.webp"
    pause insertvar
    "images/inserts/fathersus/fathersus_00025.webp"
    pause insertvar
    repeat


image rexfatherdanger: 
    "images/inserts/rexfatherdanger/rexfatherdanger_00000.webp"
    pause insertvar
    "images/inserts/rexfatherdanger/rexfatherdanger_00001.webp"
    pause insertvar
    "images/inserts/rexfatherdanger/rexfatherdanger_00002.webp"
    pause insertvar
    "images/inserts/rexfatherdanger/rexfatherdanger_00003.webp"
    pause insertvar
    "images/inserts/rexfatherdanger/rexfatherdanger_00004.webp"
    pause insertvar
    "images/inserts/rexfatherdanger/rexfatherdanger_00005.webp"
    pause insertvar
    "images/inserts/rexfatherdanger/rexfatherdanger_00006.webp"
    pause insertvar
    "images/inserts/rexfatherdanger/rexfatherdanger_00007.webp"
    pause insertvar
    "images/inserts/rexfatherdanger/rexfatherdanger_00008.webp"
    pause insertvar
    "images/inserts/rexfatherdanger/rexfatherdanger_00009.webp"
    pause insertvar
    "images/inserts/rexfatherdanger/rexfatherdanger_00010.webp"
    pause insertvar
    "images/inserts/rexfatherdanger/rexfatherdanger_00011.webp"
    pause insertvar
    "images/inserts/rexfatherdanger/rexfatherdanger_00012.webp"
    pause insertvar
    "images/inserts/rexfatherdanger/rexfatherdanger_00013.webp"
    pause insertvar
    "images/inserts/rexfatherdanger/rexfatherdanger_00014.webp"
    pause insertvar
    "images/inserts/rexfatherdanger/rexfatherdanger_00015.webp"
    pause insertvar
    "images/inserts/rexfatherdanger/rexfatherdanger_00016.webp"
    pause insertvar
    "images/inserts/rexfatherdanger/rexfatherdanger_00017.webp"
    pause insertvar
    "images/inserts/rexfatherdanger/rexfatherdanger_00018.webp"
    pause insertvar
    "images/inserts/rexfatherdanger/rexfatherdanger_00019.webp"
    pause insertvar
    "images/inserts/rexfatherdanger/rexfatherdanger_00020.webp"
    pause insertvar
    "images/inserts/rexfatherdanger/rexfatherdanger_00021.webp"
    pause insertvar
    "images/inserts/rexfatherdanger/rexfatherdanger_00022.webp"
    pause insertvar
    "images/inserts/rexfatherdanger/rexfatherdanger_00023.webp"
    pause insertvar
    "images/inserts/rexfatherdanger/rexfatherdanger_00024.webp"
    pause insertvar
    "images/inserts/rexfatherdanger/rexfatherdanger_00025.webp"
    pause insertvar
    repeat


image wovenbag: 
    "images/inserts/wovenbag/wovenbag_00000.webp"
    pause insertvar
    "images/inserts/wovenbag/wovenbag_00001.webp"
    pause insertvar
    "images/inserts/wovenbag/wovenbag_00002.webp"
    pause insertvar
    "images/inserts/wovenbag/wovenbag_00003.webp"
    pause insertvar
    "images/inserts/wovenbag/wovenbag_00004.webp"
    pause insertvar
    "images/inserts/wovenbag/wovenbag_00005.webp"
    pause insertvar
    "images/inserts/wovenbag/wovenbag_00006.webp"
    pause insertvar
    "images/inserts/wovenbag/wovenbag_00007.webp"
    pause insertvar
    "images/inserts/wovenbag/wovenbag_00008.webp"
    pause insertvar
    "images/inserts/wovenbag/wovenbag_00009.webp"
    pause insertvar
    "images/inserts/wovenbag/wovenbag_00010.webp"
    pause insertvar
    "images/inserts/wovenbag/wovenbag_00011.webp"
    pause insertvar
    "images/inserts/wovenbag/wovenbag_00012.webp"
    pause insertvar
    "images/inserts/wovenbag/wovenbag_00013.webp"
    pause insertvar
    "images/inserts/wovenbag/wovenbag_00014.webp"
    pause insertvar
    "images/inserts/wovenbag/wovenbag_00015.webp"
    pause insertvar
    "images/inserts/wovenbag/wovenbag_00016.webp"
    pause insertvar
    "images/inserts/wovenbag/wovenbag_00017.webp"
    pause insertvar
    "images/inserts/wovenbag/wovenbag_00018.webp"
    pause insertvar
    "images/inserts/wovenbag/wovenbag_00019.webp"
    pause insertvar
    "images/inserts/wovenbag/wovenbag_00020.webp"
    pause insertvar
    "images/inserts/wovenbag/wovenbag_00021.webp"
    pause insertvar
    "images/inserts/wovenbag/wovenbag_00022.webp"
    pause insertvar
    "images/inserts/wovenbag/wovenbag_00023.webp"
    pause insertvar
    "images/inserts/wovenbag/wovenbag_00024.webp"
    pause insertvar
    "images/inserts/wovenbag/wovenbag_00025.webp"
    pause insertvar
    "images/inserts/wovenbag/wovenbag_00026.webp"
    pause insertvar
    "images/inserts/wovenbag/wovenbag_00027.webp"
    pause insertvar
    "images/inserts/wovenbag/wovenbag_00028.webp"
    pause insertvar
    "images/inserts/wovenbag/wovenbag_00029.webp"
    pause insertvar
    repeat


image minastareangry: 
    "images/inserts/minastareangry/minastareangry_00000.webp"
    pause insertvar
    "images/inserts/minastareangry/minastareangry_00001.webp"
    pause insertvar
    "images/inserts/minastareangry/minastareangry_00002.webp"
    pause insertvar
    "images/inserts/minastareangry/minastareangry_00003.webp"
    pause insertvar
    "images/inserts/minastareangry/minastareangry_00004.webp"
    pause insertvar
    "images/inserts/minastareangry/minastareangry_00005.webp"
    pause insertvar
    "images/inserts/minastareangry/minastareangry_00006.webp"
    pause insertvar
    "images/inserts/minastareangry/minastareangry_00007.webp"
    pause insertvar
    "images/inserts/minastareangry/minastareangry_00008.webp"
    pause insertvar
    "images/inserts/minastareangry/minastareangry_00009.webp"
    pause insertvar
    "images/inserts/minastareangry/minastareangry_00010.webp"
    pause insertvar
    "images/inserts/minastareangry/minastareangry_00011.webp"
    pause insertvar
    "images/inserts/minastareangry/minastareangry_00012.webp"
    pause insertvar
    "images/inserts/minastareangry/minastareangry_00013.webp"
    pause insertvar
    "images/inserts/minastareangry/minastareangry_00014.webp"
    pause insertvar
    "images/inserts/minastareangry/minastareangry_00015.webp"
    pause insertvar
    "images/inserts/minastareangry/minastareangry_00016.webp"
    pause insertvar
    "images/inserts/minastareangry/minastareangry_00017.webp"
    pause insertvar
    "images/inserts/minastareangry/minastareangry_00018.webp"
    pause insertvar
    "images/inserts/minastareangry/minastareangry_00019.webp"
    pause insertvar
    "images/inserts/minastareangry/minastareangry_00020.webp"
    pause insertvar
    "images/inserts/minastareangry/minastareangry_00021.webp"
    pause insertvar
    "images/inserts/minastareangry/minastareangry_00022.webp"
    pause insertvar
    "images/inserts/minastareangry/minastareangry_00023.webp"
    pause insertvar
    "images/inserts/minastareangry/minastareangry_00024.webp"
    pause insertvar
    "images/inserts/minastareangry/minastareangry_00025.webp"
    pause insertvar
    "images/inserts/minastareangry/minastareangry_00026.webp"
    pause insertvar
    "images/inserts/minastareangry/minastareangry_00027.webp"
    pause insertvar
    "images/inserts/minastareangry/minastareangry_00028.webp"
    pause insertvar
    "images/inserts/minastareangry/minastareangry_00029.webp"
    pause insertvar
    repeat


image rexstreetmina: 
    "images/inserts/rexstreetmina/rexstreetmina_00000.webp"
    pause insertvar
    "images/inserts/rexstreetmina/rexstreetmina_00001.webp"
    pause insertvar
    "images/inserts/rexstreetmina/rexstreetmina_00002.webp"
    pause insertvar
    "images/inserts/rexstreetmina/rexstreetmina_00003.webp"
    pause insertvar
    "images/inserts/rexstreetmina/rexstreetmina_00004.webp"
    pause insertvar
    "images/inserts/rexstreetmina/rexstreetmina_00005.webp"
    pause insertvar
    "images/inserts/rexstreetmina/rexstreetmina_00006.webp"
    pause insertvar
    "images/inserts/rexstreetmina/rexstreetmina_00007.webp"
    pause insertvar
    "images/inserts/rexstreetmina/rexstreetmina_00008.webp"
    pause insertvar
    "images/inserts/rexstreetmina/rexstreetmina_00009.webp"
    pause insertvar
    "images/inserts/rexstreetmina/rexstreetmina_00010.webp"
    pause insertvar
    "images/inserts/rexstreetmina/rexstreetmina_00011.webp"
    pause insertvar
    "images/inserts/rexstreetmina/rexstreetmina_00012.webp"
    pause insertvar
    "images/inserts/rexstreetmina/rexstreetmina_00013.webp"
    pause insertvar
    "images/inserts/rexstreetmina/rexstreetmina_00014.webp"
    pause insertvar
    "images/inserts/rexstreetmina/rexstreetmina_00015.webp"
    pause insertvar
    "images/inserts/rexstreetmina/rexstreetmina_00016.webp"
    pause insertvar
    "images/inserts/rexstreetmina/rexstreetmina_00017.webp"
    pause insertvar
    "images/inserts/rexstreetmina/rexstreetmina_00018.webp"
    pause insertvar
    "images/inserts/rexstreetmina/rexstreetmina_00019.webp"
    pause insertvar
    "images/inserts/rexstreetmina/rexstreetmina_00020.webp"
    pause insertvar
    "images/inserts/rexstreetmina/rexstreetmina_00021.webp"
    pause insertvar
    "images/inserts/rexstreetmina/rexstreetmina_00022.webp"
    pause insertvar
    "images/inserts/rexstreetmina/rexstreetmina_00023.webp"
    pause insertvar
    "images/inserts/rexstreetmina/rexstreetmina_00024.webp"
    pause insertvar
    "images/inserts/rexstreetmina/rexstreetmina_00025.webp"
    pause insertvar
    repeat


image minastreetrex: 
    "images/inserts/minastreetrex/minastreetrex_00000.webp"
    pause insertvar
    "images/inserts/minastreetrex/minastreetrex_00001.webp"
    pause insertvar
    "images/inserts/minastreetrex/minastreetrex_00002.webp"
    pause insertvar
    "images/inserts/minastreetrex/minastreetrex_00003.webp"
    pause insertvar
    "images/inserts/minastreetrex/minastreetrex_00004.webp"
    pause insertvar
    "images/inserts/minastreetrex/minastreetrex_00005.webp"
    pause insertvar
    "images/inserts/minastreetrex/minastreetrex_00006.webp"
    pause insertvar
    "images/inserts/minastreetrex/minastreetrex_00007.webp"
    pause insertvar
    "images/inserts/minastreetrex/minastreetrex_00008.webp"
    pause insertvar
    "images/inserts/minastreetrex/minastreetrex_00009.webp"
    pause insertvar
    "images/inserts/minastreetrex/minastreetrex_00010.webp"
    pause insertvar
    "images/inserts/minastreetrex/minastreetrex_00011.webp"
    pause insertvar
    "images/inserts/minastreetrex/minastreetrex_00012.webp"
    pause insertvar
    "images/inserts/minastreetrex/minastreetrex_00013.webp"
    pause insertvar
    "images/inserts/minastreetrex/minastreetrex_00014.webp"
    pause insertvar
    "images/inserts/minastreetrex/minastreetrex_00015.webp"
    pause insertvar
    "images/inserts/minastreetrex/minastreetrex_00016.webp"
    pause insertvar
    "images/inserts/minastreetrex/minastreetrex_00017.webp"
    pause insertvar
    "images/inserts/minastreetrex/minastreetrex_00018.webp"
    pause insertvar
    "images/inserts/minastreetrex/minastreetrex_00019.webp"
    pause insertvar
    "images/inserts/minastreetrex/minastreetrex_00020.webp"
    pause insertvar
    "images/inserts/minastreetrex/minastreetrex_00021.webp"
    pause insertvar
    "images/inserts/minastreetrex/minastreetrex_00022.webp"
    pause insertvar
    "images/inserts/minastreetrex/minastreetrex_00023.webp"
    pause insertvar
    "images/inserts/minastreetrex/minastreetrex_00024.webp"
    pause insertvar
    "images/inserts/minastreetrex/minastreetrex_00025.webp"
    pause insertvar
    repeat


image rexstareangry: 
    "images/inserts/rexstareangry/rexstareangry_00000.webp"
    pause insertvar
    "images/inserts/rexstareangry/rexstareangry_00001.webp"
    pause insertvar
    "images/inserts/rexstareangry/rexstareangry_00002.webp"
    pause insertvar
    "images/inserts/rexstareangry/rexstareangry_00003.webp"
    pause insertvar
    "images/inserts/rexstareangry/rexstareangry_00004.webp"
    pause insertvar
    "images/inserts/rexstareangry/rexstareangry_00005.webp"
    pause insertvar
    "images/inserts/rexstareangry/rexstareangry_00006.webp"
    pause insertvar
    "images/inserts/rexstareangry/rexstareangry_00007.webp"
    pause insertvar
    "images/inserts/rexstareangry/rexstareangry_00008.webp"
    pause insertvar
    "images/inserts/rexstareangry/rexstareangry_00009.webp"
    pause insertvar
    "images/inserts/rexstareangry/rexstareangry_00010.webp"
    pause insertvar
    "images/inserts/rexstareangry/rexstareangry_00011.webp"
    pause insertvar
    "images/inserts/rexstareangry/rexstareangry_00012.webp"
    pause insertvar
    "images/inserts/rexstareangry/rexstareangry_00013.webp"
    pause insertvar
    "images/inserts/rexstareangry/rexstareangry_00014.webp"
    pause insertvar
    "images/inserts/rexstareangry/rexstareangry_00015.webp"
    pause insertvar
    "images/inserts/rexstareangry/rexstareangry_00016.webp"
    pause insertvar
    "images/inserts/rexstareangry/rexstareangry_00017.webp"
    pause insertvar
    "images/inserts/rexstareangry/rexstareangry_00018.webp"
    pause insertvar
    "images/inserts/rexstareangry/rexstareangry_00019.webp"
    pause insertvar
    "images/inserts/rexstareangry/rexstareangry_00020.webp"
    pause insertvar
    "images/inserts/rexstareangry/rexstareangry_00021.webp"
    pause insertvar
    "images/inserts/rexstareangry/rexstareangry_00022.webp"
    pause insertvar
    "images/inserts/rexstareangry/rexstareangry_00023.webp"
    pause insertvar
    "images/inserts/rexstareangry/rexstareangry_00024.webp"
    pause insertvar
    "images/inserts/rexstareangry/rexstareangry_00025.webp"
    pause insertvar
    "images/inserts/rexstareangry/rexstareangry_00026.webp"
    pause insertvar
    "images/inserts/rexstareangry/rexstareangry_00027.webp"
    pause insertvar
    "images/inserts/rexstareangry/rexstareangry_00028.webp"
    pause insertvar
    "images/inserts/rexstareangry/rexstareangry_00029.webp"
    pause insertvar
    repeat




image bloodpools: 
    "images/inserts/bloodpools/bloodpools_00000.webp"
    pause insertvar
    "images/inserts/bloodpools/bloodpools_00001.webp"
    pause insertvar
    "images/inserts/bloodpools/bloodpools_00002.webp"
    pause insertvar
    "images/inserts/bloodpools/bloodpools_00003.webp"
    pause insertvar
    "images/inserts/bloodpools/bloodpools_00004.webp"
    pause insertvar
    "images/inserts/bloodpools/bloodpools_00005.webp"
    pause insertvar
    "images/inserts/bloodpools/bloodpools_00006.webp"
    pause insertvar
    "images/inserts/bloodpools/bloodpools_00007.webp"
    pause insertvar
    "images/inserts/bloodpools/bloodpools_00008.webp"
    pause insertvar
    "images/inserts/bloodpools/bloodpools_00009.webp"
    pause insertvar
    "images/inserts/bloodpools/bloodpools_00010.webp"
    pause insertvar
    "images/inserts/bloodpools/bloodpools_00011.webp"
    pause insertvar
    "images/inserts/bloodpools/bloodpools_00012.webp"
    pause insertvar
    "images/inserts/bloodpools/bloodpools_00013.webp"
    pause insertvar
    "images/inserts/bloodpools/bloodpools_00014.webp"
    pause insertvar
    "images/inserts/bloodpools/bloodpools_00015.webp"
    pause insertvar
    "images/inserts/bloodpools/bloodpools_00016.webp"
    pause insertvar
    "images/inserts/bloodpools/bloodpools_00017.webp"
    pause insertvar
    "images/inserts/bloodpools/bloodpools_00018.webp"
    pause insertvar
    "images/inserts/bloodpools/bloodpools_00019.webp"
    pause insertvar
    "images/inserts/bloodpools/bloodpools_00020.webp"
    pause insertvar
    "images/inserts/bloodpools/bloodpools_00021.webp"
    pause insertvar
    "images/inserts/bloodpools/bloodpools_00022.webp"
    pause insertvar
    "images/inserts/bloodpools/bloodpools_00023.webp"
    pause insertvar
    "images/inserts/bloodpools/bloodpools_00024.webp"
    pause insertvar
    "images/inserts/bloodpools/bloodpools_00025.webp"
    pause insertvar
    "images/inserts/bloodpools/bloodpools_00026.webp"
    pause insertvar
    "images/inserts/bloodpools/bloodpools_00027.webp"
    pause insertvar
    "images/inserts/bloodpools/bloodpools_00028.webp"
    pause insertvar
    "images/inserts/bloodpools/bloodpools_00029.webp"
    pause insertvar
    repeat


image bloodpoolfresh: 
    "images/inserts/bloodpoolfresh/bloodpoolfresh_00000.webp"
    pause insertvar
    "images/inserts/bloodpoolfresh/bloodpoolfresh_00001.webp"
    pause insertvar
    "images/inserts/bloodpoolfresh/bloodpoolfresh_00002.webp"
    pause insertvar
    "images/inserts/bloodpoolfresh/bloodpoolfresh_00003.webp"
    pause insertvar
    "images/inserts/bloodpoolfresh/bloodpoolfresh_00004.webp"
    pause insertvar
    "images/inserts/bloodpoolfresh/bloodpoolfresh_00005.webp"
    pause insertvar
    "images/inserts/bloodpoolfresh/bloodpoolfresh_00006.webp"
    pause insertvar
    "images/inserts/bloodpoolfresh/bloodpoolfresh_00007.webp"
    pause insertvar
    "images/inserts/bloodpoolfresh/bloodpoolfresh_00008.webp"
    pause insertvar
    "images/inserts/bloodpoolfresh/bloodpoolfresh_00009.webp"
    pause insertvar
    "images/inserts/bloodpoolfresh/bloodpoolfresh_00010.webp"
    pause insertvar
    "images/inserts/bloodpoolfresh/bloodpoolfresh_00011.webp"
    pause insertvar
    "images/inserts/bloodpoolfresh/bloodpoolfresh_00012.webp"
    pause insertvar
    "images/inserts/bloodpoolfresh/bloodpoolfresh_00013.webp"
    pause insertvar
    "images/inserts/bloodpoolfresh/bloodpoolfresh_00014.webp"
    pause insertvar
    "images/inserts/bloodpoolfresh/bloodpoolfresh_00015.webp"
    pause insertvar
    "images/inserts/bloodpoolfresh/bloodpoolfresh_00016.webp"
    pause insertvar
    "images/inserts/bloodpoolfresh/bloodpoolfresh_00017.webp"
    pause insertvar
    "images/inserts/bloodpoolfresh/bloodpoolfresh_00018.webp"
    pause insertvar
    "images/inserts/bloodpoolfresh/bloodpoolfresh_00019.webp"
    pause insertvar
    "images/inserts/bloodpoolfresh/bloodpoolfresh_00020.webp"
    pause insertvar
    "images/inserts/bloodpoolfresh/bloodpoolfresh_00021.webp"
    pause insertvar
    "images/inserts/bloodpoolfresh/bloodpoolfresh_00022.webp"
    pause insertvar
    "images/inserts/bloodpoolfresh/bloodpoolfresh_00023.webp"
    pause insertvar
    "images/inserts/bloodpoolfresh/bloodpoolfresh_00024.webp"
    pause insertvar
    "images/inserts/bloodpoolfresh/bloodpoolfresh_00025.webp"
    pause insertvar
    "images/inserts/bloodpoolfresh/bloodpoolfresh_00026.webp"
    pause insertvar
    "images/inserts/bloodpoolfresh/bloodpoolfresh_00027.webp"
    pause insertvar
    "images/inserts/bloodpoolfresh/bloodpoolfresh_00028.webp"
    pause insertvar
    "images/inserts/bloodpoolfresh/bloodpoolfresh_00029.webp"
    pause insertvar
    repeat


image palmblood: 
    "images/inserts/palmblood/palmblood_00000.webp"
    pause insertvar
    "images/inserts/palmblood/palmblood_00001.webp"
    pause insertvar
    "images/inserts/palmblood/palmblood_00002.webp"
    pause insertvar
    "images/inserts/palmblood/palmblood_00003.webp"
    pause insertvar
    "images/inserts/palmblood/palmblood_00004.webp"
    pause insertvar
    "images/inserts/palmblood/palmblood_00005.webp"
    pause insertvar
    "images/inserts/palmblood/palmblood_00006.webp"
    pause insertvar
    "images/inserts/palmblood/palmblood_00007.webp"
    pause insertvar
    "images/inserts/palmblood/palmblood_00008.webp"
    pause insertvar
    "images/inserts/palmblood/palmblood_00009.webp"
    pause insertvar
    "images/inserts/palmblood/palmblood_00010.webp"
    pause insertvar
    "images/inserts/palmblood/palmblood_00011.webp"
    pause insertvar
    "images/inserts/palmblood/palmblood_00012.webp"
    pause insertvar
    "images/inserts/palmblood/palmblood_00013.webp"
    pause insertvar
    "images/inserts/palmblood/palmblood_00014.webp"
    pause insertvar
    "images/inserts/palmblood/palmblood_00015.webp"
    pause insertvar
    "images/inserts/palmblood/palmblood_00016.webp"
    pause insertvar
    "images/inserts/palmblood/palmblood_00017.webp"
    pause insertvar
    "images/inserts/palmblood/palmblood_00018.webp"
    pause insertvar
    "images/inserts/palmblood/palmblood_00019.webp"
    pause insertvar
    "images/inserts/palmblood/palmblood_00020.webp"
    pause insertvar
    "images/inserts/palmblood/palmblood_00021.webp"
    pause insertvar
    "images/inserts/palmblood/palmblood_00022.webp"
    pause insertvar
    "images/inserts/palmblood/palmblood_00023.webp"
    pause insertvar
    "images/inserts/palmblood/palmblood_00024.webp"
    pause insertvar
    "images/inserts/palmblood/palmblood_00025.webp"
    pause insertvar
    "images/inserts/palmblood/palmblood_00026.webp"
    pause insertvar
    "images/inserts/palmblood/palmblood_00027.webp"
    pause insertvar
    "images/inserts/palmblood/palmblood_00028.webp"
    pause insertvar
    "images/inserts/palmblood/palmblood_00029.webp"
    pause insertvar
    repeat




image motherstoryone: 
    "images/inserts/motherstoryone/motherstoryone_00000.webp"
    pause insertvar
    "images/inserts/motherstoryone/motherstoryone_00001.webp"
    pause insertvar
    "images/inserts/motherstoryone/motherstoryone_00002.webp"
    pause insertvar
    "images/inserts/motherstoryone/motherstoryone_00003.webp"
    pause insertvar
    "images/inserts/motherstoryone/motherstoryone_00004.webp"
    pause insertvar
    "images/inserts/motherstoryone/motherstoryone_00005.webp"
    pause insertvar
    "images/inserts/motherstoryone/motherstoryone_00006.webp"
    pause insertvar
    "images/inserts/motherstoryone/motherstoryone_00007.webp"
    pause insertvar
    "images/inserts/motherstoryone/motherstoryone_00008.webp"
    pause insertvar
    "images/inserts/motherstoryone/motherstoryone_00009.webp"
    pause insertvar
    "images/inserts/motherstoryone/motherstoryone_00010.webp"
    pause insertvar
    "images/inserts/motherstoryone/motherstoryone_00011.webp"
    pause insertvar
    "images/inserts/motherstoryone/motherstoryone_00012.webp"
    pause insertvar
    "images/inserts/motherstoryone/motherstoryone_00013.webp"
    pause insertvar
    "images/inserts/motherstoryone/motherstoryone_00014.webp"
    pause insertvar
    "images/inserts/motherstoryone/motherstoryone_00015.webp"
    pause insertvar
    "images/inserts/motherstoryone/motherstoryone_00016.webp"
    pause insertvar
    "images/inserts/motherstoryone/motherstoryone_00017.webp"
    pause insertvar
    "images/inserts/motherstoryone/motherstoryone_00018.webp"
    pause insertvar
    "images/inserts/motherstoryone/motherstoryone_00019.webp"
    pause insertvar
    "images/inserts/motherstoryone/motherstoryone_00020.webp"
    pause insertvar
    "images/inserts/motherstoryone/motherstoryone_00021.webp"
    pause insertvar
    "images/inserts/motherstoryone/motherstoryone_00022.webp"
    pause insertvar
    "images/inserts/motherstoryone/motherstoryone_00023.webp"
    pause insertvar
    "images/inserts/motherstoryone/motherstoryone_00024.webp"
    pause insertvar
    "images/inserts/motherstoryone/motherstoryone_00025.webp"
    pause insertvar
    repeat


image motherstorytwo: 
    "images/inserts/motherstorytwo/motherstorytwo_00000.webp"
    pause insertvar
    "images/inserts/motherstorytwo/motherstorytwo_00001.webp"
    pause insertvar
    "images/inserts/motherstorytwo/motherstorytwo_00002.webp"
    pause insertvar
    "images/inserts/motherstorytwo/motherstorytwo_00003.webp"
    pause insertvar
    "images/inserts/motherstorytwo/motherstorytwo_00004.webp"
    pause insertvar
    "images/inserts/motherstorytwo/motherstorytwo_00005.webp"
    pause insertvar
    "images/inserts/motherstorytwo/motherstorytwo_00006.webp"
    pause insertvar
    "images/inserts/motherstorytwo/motherstorytwo_00007.webp"
    pause insertvar
    "images/inserts/motherstorytwo/motherstorytwo_00008.webp"
    pause insertvar
    "images/inserts/motherstorytwo/motherstorytwo_00009.webp"
    pause insertvar
    "images/inserts/motherstorytwo/motherstorytwo_00010.webp"
    pause insertvar
    "images/inserts/motherstorytwo/motherstorytwo_00011.webp"
    pause insertvar
    "images/inserts/motherstorytwo/motherstorytwo_00012.webp"
    pause insertvar
    "images/inserts/motherstorytwo/motherstorytwo_00013.webp"
    pause insertvar
    "images/inserts/motherstorytwo/motherstorytwo_00014.webp"
    pause insertvar
    "images/inserts/motherstorytwo/motherstorytwo_00015.webp"
    pause insertvar
    "images/inserts/motherstorytwo/motherstorytwo_00016.webp"
    pause insertvar
    "images/inserts/motherstorytwo/motherstorytwo_00017.webp"
    pause insertvar
    "images/inserts/motherstorytwo/motherstorytwo_00018.webp"
    pause insertvar
    "images/inserts/motherstorytwo/motherstorytwo_00019.webp"
    pause insertvar
    "images/inserts/motherstorytwo/motherstorytwo_00020.webp"
    pause insertvar
    "images/inserts/motherstorytwo/motherstorytwo_00021.webp"
    pause insertvar
    "images/inserts/motherstorytwo/motherstorytwo_00022.webp"
    pause insertvar
    "images/inserts/motherstorytwo/motherstorytwo_00023.webp"
    pause insertvar
    "images/inserts/motherstorytwo/motherstorytwo_00024.webp"
    pause insertvar
    "images/inserts/motherstorytwo/motherstorytwo_00025.webp"
    pause insertvar
    repeat


image deviseplaneone: 
    "images/inserts/deviseplaneone/deviseplaneone_00000.webp"
    pause insertvar
    "images/inserts/deviseplaneone/deviseplaneone_00001.webp"
    pause insertvar
    "images/inserts/deviseplaneone/deviseplaneone_00002.webp"
    pause insertvar
    "images/inserts/deviseplaneone/deviseplaneone_00003.webp"
    pause insertvar
    "images/inserts/deviseplaneone/deviseplaneone_00004.webp"
    pause insertvar
    "images/inserts/deviseplaneone/deviseplaneone_00005.webp"
    pause insertvar
    "images/inserts/deviseplaneone/deviseplaneone_00006.webp"
    pause insertvar
    "images/inserts/deviseplaneone/deviseplaneone_00007.webp"
    pause insertvar
    "images/inserts/deviseplaneone/deviseplaneone_00008.webp"
    pause insertvar
    "images/inserts/deviseplaneone/deviseplaneone_00009.webp"
    pause insertvar
    "images/inserts/deviseplaneone/deviseplaneone_00010.webp"
    pause insertvar
    "images/inserts/deviseplaneone/deviseplaneone_00011.webp"
    pause insertvar
    "images/inserts/deviseplaneone/deviseplaneone_00012.webp"
    pause insertvar
    "images/inserts/deviseplaneone/deviseplaneone_00013.webp"
    pause insertvar
    "images/inserts/deviseplaneone/deviseplaneone_00014.webp"
    pause insertvar
    "images/inserts/deviseplaneone/deviseplaneone_00015.webp"
    pause insertvar
    "images/inserts/deviseplaneone/deviseplaneone_00016.webp"
    pause insertvar
    "images/inserts/deviseplaneone/deviseplaneone_00017.webp"
    pause insertvar
    "images/inserts/deviseplaneone/deviseplaneone_00018.webp"
    pause insertvar
    "images/inserts/deviseplaneone/deviseplaneone_00019.webp"
    pause insertvar
    "images/inserts/deviseplaneone/deviseplaneone_00020.webp"
    pause insertvar
    "images/inserts/deviseplaneone/deviseplaneone_00021.webp"
    pause insertvar
    "images/inserts/deviseplaneone/deviseplaneone_00022.webp"
    pause insertvar
    "images/inserts/deviseplaneone/deviseplaneone_00023.webp"
    pause insertvar
    "images/inserts/deviseplaneone/deviseplaneone_00024.webp"
    pause insertvar
    "images/inserts/deviseplaneone/deviseplaneone_00025.webp"
    pause insertvar
    repeat


image deviseplantwo: 
    "images/inserts/deviseplantwo/deviseplantwo_00000.webp"
    pause insertvar
    "images/inserts/deviseplantwo/deviseplantwo_00001.webp"
    pause insertvar
    "images/inserts/deviseplantwo/deviseplantwo_00002.webp"
    pause insertvar
    "images/inserts/deviseplantwo/deviseplantwo_00003.webp"
    pause insertvar
    "images/inserts/deviseplantwo/deviseplantwo_00004.webp"
    pause insertvar
    "images/inserts/deviseplantwo/deviseplantwo_00005.webp"
    pause insertvar
    "images/inserts/deviseplantwo/deviseplantwo_00006.webp"
    pause insertvar
    "images/inserts/deviseplantwo/deviseplantwo_00007.webp"
    pause insertvar
    "images/inserts/deviseplantwo/deviseplantwo_00008.webp"
    pause insertvar
    "images/inserts/deviseplantwo/deviseplantwo_00009.webp"
    pause insertvar
    "images/inserts/deviseplantwo/deviseplantwo_00010.webp"
    pause insertvar
    "images/inserts/deviseplantwo/deviseplantwo_00011.webp"
    pause insertvar
    "images/inserts/deviseplantwo/deviseplantwo_00012.webp"
    pause insertvar
    "images/inserts/deviseplantwo/deviseplantwo_00013.webp"
    pause insertvar
    "images/inserts/deviseplantwo/deviseplantwo_00014.webp"
    pause insertvar
    "images/inserts/deviseplantwo/deviseplantwo_00015.webp"
    pause insertvar
    "images/inserts/deviseplantwo/deviseplantwo_00016.webp"
    pause insertvar
    "images/inserts/deviseplantwo/deviseplantwo_00017.webp"
    pause insertvar
    "images/inserts/deviseplantwo/deviseplantwo_00018.webp"
    pause insertvar
    "images/inserts/deviseplantwo/deviseplantwo_00019.webp"
    pause insertvar
    "images/inserts/deviseplantwo/deviseplantwo_00020.webp"
    pause insertvar
    "images/inserts/deviseplantwo/deviseplantwo_00021.webp"
    pause insertvar
    "images/inserts/deviseplantwo/deviseplantwo_00022.webp"
    pause insertvar
    "images/inserts/deviseplantwo/deviseplantwo_00023.webp"
    pause insertvar
    "images/inserts/deviseplantwo/deviseplantwo_00024.webp"
    pause insertvar
    "images/inserts/deviseplantwo/deviseplantwo_00025.webp"
    pause insertvar
    repeat


image fatherstoryone: 
    "images/inserts/fatherstoryone/fatherstoryone_00000.webp"
    pause insertvar
    "images/inserts/fatherstoryone/fatherstoryone_00001.webp"
    pause insertvar
    "images/inserts/fatherstoryone/fatherstoryone_00002.webp"
    pause insertvar
    "images/inserts/fatherstoryone/fatherstoryone_00003.webp"
    pause insertvar
    "images/inserts/fatherstoryone/fatherstoryone_00004.webp"
    pause insertvar
    "images/inserts/fatherstoryone/fatherstoryone_00005.webp"
    pause insertvar
    "images/inserts/fatherstoryone/fatherstoryone_00006.webp"
    pause insertvar
    "images/inserts/fatherstoryone/fatherstoryone_00007.webp"
    pause insertvar
    "images/inserts/fatherstoryone/fatherstoryone_00008.webp"
    pause insertvar
    "images/inserts/fatherstoryone/fatherstoryone_00009.webp"
    pause insertvar
    "images/inserts/fatherstoryone/fatherstoryone_00010.webp"
    pause insertvar
    "images/inserts/fatherstoryone/fatherstoryone_00011.webp"
    pause insertvar
    "images/inserts/fatherstoryone/fatherstoryone_00012.webp"
    pause insertvar
    "images/inserts/fatherstoryone/fatherstoryone_00013.webp"
    pause insertvar
    "images/inserts/fatherstoryone/fatherstoryone_00014.webp"
    pause insertvar
    "images/inserts/fatherstoryone/fatherstoryone_00015.webp"
    pause insertvar
    "images/inserts/fatherstoryone/fatherstoryone_00016.webp"
    pause insertvar
    "images/inserts/fatherstoryone/fatherstoryone_00017.webp"
    pause insertvar
    "images/inserts/fatherstoryone/fatherstoryone_00018.webp"
    pause insertvar
    "images/inserts/fatherstoryone/fatherstoryone_00019.webp"
    pause insertvar
    "images/inserts/fatherstoryone/fatherstoryone_00020.webp"
    pause insertvar
    "images/inserts/fatherstoryone/fatherstoryone_00021.webp"
    pause insertvar
    "images/inserts/fatherstoryone/fatherstoryone_00022.webp"
    pause insertvar
    "images/inserts/fatherstoryone/fatherstoryone_00023.webp"
    pause insertvar
    "images/inserts/fatherstoryone/fatherstoryone_00024.webp"
    pause insertvar
    "images/inserts/fatherstoryone/fatherstoryone_00025.webp"
    pause insertvar
    repeat


image fatherstorytwo: 
    "images/inserts/fatherstorytwo/fatherstorytwo_00000.webp"
    pause insertvar
    "images/inserts/fatherstorytwo/fatherstorytwo_00001.webp"
    pause insertvar
    "images/inserts/fatherstorytwo/fatherstorytwo_00002.webp"
    pause insertvar
    "images/inserts/fatherstorytwo/fatherstorytwo_00003.webp"
    pause insertvar
    "images/inserts/fatherstorytwo/fatherstorytwo_00004.webp"
    pause insertvar
    "images/inserts/fatherstorytwo/fatherstorytwo_00005.webp"
    pause insertvar
    "images/inserts/fatherstorytwo/fatherstorytwo_00006.webp"
    pause insertvar
    "images/inserts/fatherstorytwo/fatherstorytwo_00007.webp"
    pause insertvar
    "images/inserts/fatherstorytwo/fatherstorytwo_00008.webp"
    pause insertvar
    "images/inserts/fatherstorytwo/fatherstorytwo_00009.webp"
    pause insertvar
    "images/inserts/fatherstorytwo/fatherstorytwo_00010.webp"
    pause insertvar
    "images/inserts/fatherstorytwo/fatherstorytwo_00011.webp"
    pause insertvar
    "images/inserts/fatherstorytwo/fatherstorytwo_00012.webp"
    pause insertvar
    "images/inserts/fatherstorytwo/fatherstorytwo_00013.webp"
    pause insertvar
    "images/inserts/fatherstorytwo/fatherstorytwo_00014.webp"
    pause insertvar
    "images/inserts/fatherstorytwo/fatherstorytwo_00015.webp"
    pause insertvar
    "images/inserts/fatherstorytwo/fatherstorytwo_00016.webp"
    pause insertvar
    "images/inserts/fatherstorytwo/fatherstorytwo_00017.webp"
    pause insertvar
    "images/inserts/fatherstorytwo/fatherstorytwo_00018.webp"
    pause insertvar
    "images/inserts/fatherstorytwo/fatherstorytwo_00019.webp"
    pause insertvar
    "images/inserts/fatherstorytwo/fatherstorytwo_00020.webp"
    pause insertvar
    "images/inserts/fatherstorytwo/fatherstorytwo_00021.webp"
    pause insertvar
    "images/inserts/fatherstorytwo/fatherstorytwo_00022.webp"
    pause insertvar
    "images/inserts/fatherstorytwo/fatherstorytwo_00023.webp"
    pause insertvar
    "images/inserts/fatherstorytwo/fatherstorytwo_00024.webp"
    pause insertvar
    "images/inserts/fatherstorytwo/fatherstorytwo_00025.webp"
    pause insertvar
    repeat


image fatherstorythree: 
    "images/inserts/fatherstorythree/fatherstorythree_00000.webp"
    pause insertvar
    "images/inserts/fatherstorythree/fatherstorythree_00001.webp"
    pause insertvar
    "images/inserts/fatherstorythree/fatherstorythree_00002.webp"
    pause insertvar
    "images/inserts/fatherstorythree/fatherstorythree_00003.webp"
    pause insertvar
    "images/inserts/fatherstorythree/fatherstorythree_00004.webp"
    pause insertvar
    "images/inserts/fatherstorythree/fatherstorythree_00005.webp"
    pause insertvar
    "images/inserts/fatherstorythree/fatherstorythree_00006.webp"
    pause insertvar
    "images/inserts/fatherstorythree/fatherstorythree_00007.webp"
    pause insertvar
    "images/inserts/fatherstorythree/fatherstorythree_00008.webp"
    pause insertvar
    "images/inserts/fatherstorythree/fatherstorythree_00009.webp"
    pause insertvar
    "images/inserts/fatherstorythree/fatherstorythree_00010.webp"
    pause insertvar
    "images/inserts/fatherstorythree/fatherstorythree_00011.webp"
    pause insertvar
    "images/inserts/fatherstorythree/fatherstorythree_00012.webp"
    pause insertvar
    "images/inserts/fatherstorythree/fatherstorythree_00013.webp"
    pause insertvar
    "images/inserts/fatherstorythree/fatherstorythree_00014.webp"
    pause insertvar
    "images/inserts/fatherstorythree/fatherstorythree_00015.webp"
    pause insertvar
    "images/inserts/fatherstorythree/fatherstorythree_00016.webp"
    pause insertvar
    "images/inserts/fatherstorythree/fatherstorythree_00017.webp"
    pause insertvar
    "images/inserts/fatherstorythree/fatherstorythree_00018.webp"
    pause insertvar
    "images/inserts/fatherstorythree/fatherstorythree_00019.webp"
    pause insertvar
    "images/inserts/fatherstorythree/fatherstorythree_00020.webp"
    pause insertvar
    "images/inserts/fatherstorythree/fatherstorythree_00021.webp"
    pause insertvar
    "images/inserts/fatherstorythree/fatherstorythree_00022.webp"
    pause insertvar
    "images/inserts/fatherstorythree/fatherstorythree_00023.webp"
    pause insertvar
    "images/inserts/fatherstorythree/fatherstorythree_00024.webp"
    pause insertvar
    "images/inserts/fatherstorythree/fatherstorythree_00025.webp"
    pause insertvar
    repeat


image documents: 
    "images/inserts/documents/documents_00000.webp"
    pause insertvar
    "images/inserts/documents/documents_00001.webp"
    pause insertvar
    "images/inserts/documents/documents_00002.webp"
    pause insertvar
    "images/inserts/documents/documents_00003.webp"
    pause insertvar
    "images/inserts/documents/documents_00004.webp"
    pause insertvar
    "images/inserts/documents/documents_00005.webp"
    pause insertvar
    "images/inserts/documents/documents_00006.webp"
    pause insertvar
    "images/inserts/documents/documents_00007.webp"
    pause insertvar
    "images/inserts/documents/documents_00008.webp"
    pause insertvar
    "images/inserts/documents/documents_00009.webp"
    pause insertvar
    "images/inserts/documents/documents_00010.webp"
    pause insertvar
    "images/inserts/documents/documents_00011.webp"
    pause insertvar
    "images/inserts/documents/documents_00012.webp"
    pause insertvar
    "images/inserts/documents/documents_00013.webp"
    pause insertvar
    "images/inserts/documents/documents_00014.webp"
    pause insertvar
    "images/inserts/documents/documents_00015.webp"
    pause insertvar
    "images/inserts/documents/documents_00016.webp"
    pause insertvar
    "images/inserts/documents/documents_00017.webp"
    pause insertvar
    "images/inserts/documents/documents_00018.webp"
    pause insertvar
    "images/inserts/documents/documents_00019.webp"
    pause insertvar
    "images/inserts/documents/documents_00020.webp"
    pause insertvar
    "images/inserts/documents/documents_00021.webp"
    pause insertvar
    "images/inserts/documents/documents_00022.webp"
    pause insertvar
    "images/inserts/documents/documents_00023.webp"
    pause insertvar
    "images/inserts/documents/documents_00024.webp"
    pause insertvar
    "images/inserts/documents/documents_00025.webp"
    pause insertvar
    "images/inserts/documents/documents_00026.webp"
    pause insertvar
    "images/inserts/documents/documents_00027.webp"
    pause insertvar
    "images/inserts/documents/documents_00028.webp"
    pause insertvar
    "images/inserts/documents/documents_00029.webp"
    pause insertvar
    repeat


image office: 
    "images/inserts/office/office_00000.webp"
    pause insertvar
    "images/inserts/office/office_00001.webp"
    pause insertvar
    "images/inserts/office/office_00002.webp"
    pause insertvar
    "images/inserts/office/office_00003.webp"
    pause insertvar
    "images/inserts/office/office_00004.webp"
    pause insertvar
    "images/inserts/office/office_00005.webp"
    pause insertvar
    "images/inserts/office/office_00006.webp"
    pause insertvar
    "images/inserts/office/office_00007.webp"
    pause insertvar
    "images/inserts/office/office_00008.webp"
    pause insertvar
    "images/inserts/office/office_00009.webp"
    pause insertvar
    "images/inserts/office/office_00010.webp"
    pause insertvar
    "images/inserts/office/office_00011.webp"
    pause insertvar
    "images/inserts/office/office_00012.webp"
    pause insertvar
    "images/inserts/office/office_00013.webp"
    pause insertvar
    "images/inserts/office/office_00014.webp"
    pause insertvar
    "images/inserts/office/office_00015.webp"
    pause insertvar
    "images/inserts/office/office_00016.webp"
    pause insertvar
    "images/inserts/office/office_00017.webp"
    pause insertvar
    "images/inserts/office/office_00018.webp"
    pause insertvar
    "images/inserts/office/office_00019.webp"
    pause insertvar
    "images/inserts/office/office_00020.webp"
    pause insertvar
    "images/inserts/office/office_00021.webp"
    pause insertvar
    "images/inserts/office/office_00022.webp"
    pause insertvar
    "images/inserts/office/office_00023.webp"
    pause insertvar
    "images/inserts/office/office_00024.webp"
    pause insertvar
    "images/inserts/office/office_00025.webp"
    pause insertvar
    "images/inserts/office/office_00026.webp"
    pause insertvar
    "images/inserts/office/office_00027.webp"
    pause insertvar
    "images/inserts/office/office_00028.webp"
    pause insertvar
    "images/inserts/office/office_00029.webp"
    pause insertvar
    repeat


image fatherroom: 
    "images/inserts/fatherroom/fatherroom_00000.webp"
    pause insertvar
    "images/inserts/fatherroom/fatherroom_00001.webp"
    pause insertvar
    "images/inserts/fatherroom/fatherroom_00002.webp"
    pause insertvar
    "images/inserts/fatherroom/fatherroom_00003.webp"
    pause insertvar
    "images/inserts/fatherroom/fatherroom_00004.webp"
    pause insertvar
    "images/inserts/fatherroom/fatherroom_00005.webp"
    pause insertvar
    "images/inserts/fatherroom/fatherroom_00006.webp"
    pause insertvar
    "images/inserts/fatherroom/fatherroom_00007.webp"
    pause insertvar
    "images/inserts/fatherroom/fatherroom_00008.webp"
    pause insertvar
    "images/inserts/fatherroom/fatherroom_00009.webp"
    pause insertvar
    "images/inserts/fatherroom/fatherroom_00010.webp"
    pause insertvar
    "images/inserts/fatherroom/fatherroom_00011.webp"
    pause insertvar
    "images/inserts/fatherroom/fatherroom_00012.webp"
    pause insertvar
    "images/inserts/fatherroom/fatherroom_00013.webp"
    pause insertvar
    "images/inserts/fatherroom/fatherroom_00014.webp"
    pause insertvar
    "images/inserts/fatherroom/fatherroom_00015.webp"
    pause insertvar
    "images/inserts/fatherroom/fatherroom_00016.webp"
    pause insertvar
    "images/inserts/fatherroom/fatherroom_00017.webp"
    pause insertvar
    "images/inserts/fatherroom/fatherroom_00018.webp"
    pause insertvar
    "images/inserts/fatherroom/fatherroom_00019.webp"
    pause insertvar
    "images/inserts/fatherroom/fatherroom_00020.webp"
    pause insertvar
    "images/inserts/fatherroom/fatherroom_00021.webp"
    pause insertvar
    "images/inserts/fatherroom/fatherroom_00022.webp"
    pause insertvar
    "images/inserts/fatherroom/fatherroom_00023.webp"
    pause insertvar
    "images/inserts/fatherroom/fatherroom_00024.webp"
    pause insertvar
    "images/inserts/fatherroom/fatherroom_00025.webp"
    pause insertvar
    repeat



image deadbody: 
    "images/inserts/deadbody/deadbody_00000.webp"
    pause insertvar
    "images/inserts/deadbody/deadbody_00001.webp"
    pause insertvar
    "images/inserts/deadbody/deadbody_00002.webp"
    pause insertvar
    "images/inserts/deadbody/deadbody_00003.webp"
    pause insertvar
    "images/inserts/deadbody/deadbody_00004.webp"
    pause insertvar
    "images/inserts/deadbody/deadbody_00005.webp"
    pause insertvar
    "images/inserts/deadbody/deadbody_00006.webp"
    pause insertvar
    "images/inserts/deadbody/deadbody_00007.webp"
    pause insertvar
    "images/inserts/deadbody/deadbody_00008.webp"
    pause insertvar
    "images/inserts/deadbody/deadbody_00009.webp"
    pause insertvar
    "images/inserts/deadbody/deadbody_00010.webp"
    pause insertvar
    "images/inserts/deadbody/deadbody_00011.webp"
    pause insertvar
    "images/inserts/deadbody/deadbody_00012.webp"
    pause insertvar
    "images/inserts/deadbody/deadbody_00013.webp"
    pause insertvar
    "images/inserts/deadbody/deadbody_00014.webp"
    pause insertvar
    "images/inserts/deadbody/deadbody_00015.webp"
    pause insertvar
    "images/inserts/deadbody/deadbody_00016.webp"
    pause insertvar
    "images/inserts/deadbody/deadbody_00017.webp"
    pause insertvar
    "images/inserts/deadbody/deadbody_00018.webp"
    pause insertvar
    "images/inserts/deadbody/deadbody_00019.webp"
    pause insertvar
    "images/inserts/deadbody/deadbody_00020.webp"
    pause insertvar
    "images/inserts/deadbody/deadbody_00021.webp"
    pause insertvar
    "images/inserts/deadbody/deadbody_00022.webp"
    pause insertvar
    "images/inserts/deadbody/deadbody_00023.webp"
    pause insertvar
    "images/inserts/deadbody/deadbody_00024.webp"
    pause insertvar
    "images/inserts/deadbody/deadbody_00025.webp"
    pause insertvar
    "images/inserts/deadbody/deadbody_00026.webp"
    pause insertvar
    "images/inserts/deadbody/deadbody_00027.webp"
    pause insertvar
    "images/inserts/deadbody/deadbody_00028.webp"
    pause insertvar
    "images/inserts/deadbody/deadbody_00029.webp"
    pause insertvar
    repeat


image skull: 
    "images/inserts/skull/skull_00000.webp"
    pause insertvar
    "images/inserts/skull/skull_00001.webp"
    pause insertvar
    "images/inserts/skull/skull_00002.webp"
    pause insertvar
    "images/inserts/skull/skull_00003.webp"
    pause insertvar
    "images/inserts/skull/skull_00004.webp"
    pause insertvar
    "images/inserts/skull/skull_00005.webp"
    pause insertvar
    "images/inserts/skull/skull_00006.webp"
    pause insertvar
    "images/inserts/skull/skull_00007.webp"
    pause insertvar
    "images/inserts/skull/skull_00008.webp"
    pause insertvar
    "images/inserts/skull/skull_00009.webp"
    pause insertvar
    "images/inserts/skull/skull_00010.webp"
    pause insertvar
    "images/inserts/skull/skull_00011.webp"
    pause insertvar
    "images/inserts/skull/skull_00012.webp"
    pause insertvar
    "images/inserts/skull/skull_00013.webp"
    pause insertvar
    "images/inserts/skull/skull_00014.webp"
    pause insertvar
    "images/inserts/skull/skull_00015.webp"
    pause insertvar
    "images/inserts/skull/skull_00016.webp"
    pause insertvar
    "images/inserts/skull/skull_00017.webp"
    pause insertvar
    "images/inserts/skull/skull_00018.webp"
    pause insertvar
    "images/inserts/skull/skull_00019.webp"
    pause insertvar
    "images/inserts/skull/skull_00020.webp"
    pause insertvar
    "images/inserts/skull/skull_00021.webp"
    pause insertvar
    "images/inserts/skull/skull_00022.webp"
    pause insertvar
    "images/inserts/skull/skull_00023.webp"
    pause insertvar
    "images/inserts/skull/skull_00024.webp"
    pause insertvar
    "images/inserts/skull/skull_00025.webp"
    pause insertvar
    repeat


image crown: 
    "images/inserts/crown/crown_00000.webp"
    pause insertvar
    "images/inserts/crown/crown_00001.webp"
    pause insertvar
    "images/inserts/crown/crown_00002.webp"
    pause insertvar
    "images/inserts/crown/crown_00003.webp"
    pause insertvar
    "images/inserts/crown/crown_00004.webp"
    pause insertvar
    "images/inserts/crown/crown_00005.webp"
    pause insertvar
    "images/inserts/crown/crown_00006.webp"
    pause insertvar
    "images/inserts/crown/crown_00007.webp"
    pause insertvar
    "images/inserts/crown/crown_00008.webp"
    pause insertvar
    "images/inserts/crown/crown_00009.webp"
    pause insertvar
    "images/inserts/crown/crown_00010.webp"
    pause insertvar
    "images/inserts/crown/crown_00011.webp"
    pause insertvar
    "images/inserts/crown/crown_00012.webp"
    pause insertvar
    "images/inserts/crown/crown_00013.webp"
    pause insertvar
    "images/inserts/crown/crown_00014.webp"
    pause insertvar
    "images/inserts/crown/crown_00015.webp"
    pause insertvar
    "images/inserts/crown/crown_00016.webp"
    pause insertvar
    "images/inserts/crown/crown_00017.webp"
    pause insertvar
    "images/inserts/crown/crown_00018.webp"
    pause insertvar
    "images/inserts/crown/crown_00019.webp"
    pause insertvar
    "images/inserts/crown/crown_00020.webp"
    pause insertvar
    "images/inserts/crown/crown_00021.webp"
    pause insertvar
    "images/inserts/crown/crown_00022.webp"
    pause insertvar
    "images/inserts/crown/crown_00023.webp"
    pause insertvar
    "images/inserts/crown/crown_00024.webp"
    pause insertvar
    "images/inserts/crown/crown_00025.webp"
    pause insertvar
    repeat


image pathway: 
    "images/inserts/pathway/pathway_00000.webp"
    pause insertvar
    "images/inserts/pathway/pathway_00001.webp"
    pause insertvar
    "images/inserts/pathway/pathway_00002.webp"
    pause insertvar
    "images/inserts/pathway/pathway_00003.webp"
    pause insertvar
    "images/inserts/pathway/pathway_00004.webp"
    pause insertvar
    "images/inserts/pathway/pathway_00005.webp"
    pause insertvar
    "images/inserts/pathway/pathway_00006.webp"
    pause insertvar
    "images/inserts/pathway/pathway_00007.webp"
    pause insertvar
    "images/inserts/pathway/pathway_00008.webp"
    pause insertvar
    "images/inserts/pathway/pathway_00009.webp"
    pause insertvar
    "images/inserts/pathway/pathway_00010.webp"
    pause insertvar
    "images/inserts/pathway/pathway_00011.webp"
    pause insertvar
    "images/inserts/pathway/pathway_00012.webp"
    pause insertvar
    "images/inserts/pathway/pathway_00013.webp"
    pause insertvar
    "images/inserts/pathway/pathway_00014.webp"
    pause insertvar
    "images/inserts/pathway/pathway_00015.webp"
    pause insertvar
    "images/inserts/pathway/pathway_00016.webp"
    pause insertvar
    "images/inserts/pathway/pathway_00017.webp"
    pause insertvar
    "images/inserts/pathway/pathway_00018.webp"
    pause insertvar
    "images/inserts/pathway/pathway_00019.webp"
    pause insertvar
    "images/inserts/pathway/pathway_00020.webp"
    pause insertvar
    "images/inserts/pathway/pathway_00021.webp"
    pause insertvar
    "images/inserts/pathway/pathway_00022.webp"
    pause insertvar
    "images/inserts/pathway/pathway_00023.webp"
    pause insertvar
    "images/inserts/pathway/pathway_00024.webp"
    pause insertvar
    "images/inserts/pathway/pathway_00025.webp"
    pause insertvar
    repeat


image minacatseye: 
    "images/inserts/minacatseye/minacatseye_00000.webp"
    pause insertvar
    "images/inserts/minacatseye/minacatseye_00001.webp"
    pause insertvar
    "images/inserts/minacatseye/minacatseye_00002.webp"
    pause insertvar
    "images/inserts/minacatseye/minacatseye_00003.webp"
    pause insertvar
    "images/inserts/minacatseye/minacatseye_00004.webp"
    pause insertvar
    "images/inserts/minacatseye/minacatseye_00005.webp"
    pause insertvar
    "images/inserts/minacatseye/minacatseye_00006.webp"
    pause insertvar
    "images/inserts/minacatseye/minacatseye_00007.webp"
    pause insertvar
    "images/inserts/minacatseye/minacatseye_00008.webp"
    pause insertvar
    "images/inserts/minacatseye/minacatseye_00009.webp"
    pause insertvar
    "images/inserts/minacatseye/minacatseye_00010.webp"
    pause insertvar
    "images/inserts/minacatseye/minacatseye_00011.webp"
    pause insertvar
    "images/inserts/minacatseye/minacatseye_00012.webp"
    pause insertvar
    "images/inserts/minacatseye/minacatseye_00013.webp"
    pause insertvar
    "images/inserts/minacatseye/minacatseye_00014.webp"
    pause insertvar
    "images/inserts/minacatseye/minacatseye_00015.webp"
    pause insertvar
    "images/inserts/minacatseye/minacatseye_00016.webp"
    pause insertvar
    "images/inserts/minacatseye/minacatseye_00017.webp"
    pause insertvar
    "images/inserts/minacatseye/minacatseye_00018.webp"
    pause insertvar
    "images/inserts/minacatseye/minacatseye_00019.webp"
    pause insertvar
    "images/inserts/minacatseye/minacatseye_00020.webp"
    pause insertvar
    "images/inserts/minacatseye/minacatseye_00021.webp"
    pause insertvar
    "images/inserts/minacatseye/minacatseye_00022.webp"
    pause insertvar
    "images/inserts/minacatseye/minacatseye_00023.webp"
    pause insertvar
    "images/inserts/minacatseye/minacatseye_00024.webp"
    pause insertvar
    "images/inserts/minacatseye/minacatseye_00025.webp"
    pause insertvar
    repeat


image minadeathstare: 
    "images/inserts/minadeathstare/minadeathstare_00000.webp"
    pause insertvar
    "images/inserts/minadeathstare/minadeathstare_00001.webp"
    pause insertvar
    "images/inserts/minadeathstare/minadeathstare_00002.webp"
    pause insertvar
    "images/inserts/minadeathstare/minadeathstare_00003.webp"
    pause insertvar
    "images/inserts/minadeathstare/minadeathstare_00004.webp"
    pause insertvar
    "images/inserts/minadeathstare/minadeathstare_00005.webp"
    pause insertvar
    "images/inserts/minadeathstare/minadeathstare_00006.webp"
    pause insertvar
    "images/inserts/minadeathstare/minadeathstare_00007.webp"
    pause insertvar
    "images/inserts/minadeathstare/minadeathstare_00008.webp"
    pause insertvar
    "images/inserts/minadeathstare/minadeathstare_00009.webp"
    pause insertvar
    "images/inserts/minadeathstare/minadeathstare_00010.webp"
    pause insertvar
    "images/inserts/minadeathstare/minadeathstare_00011.webp"
    pause insertvar
    "images/inserts/minadeathstare/minadeathstare_00012.webp"
    pause insertvar
    "images/inserts/minadeathstare/minadeathstare_00013.webp"
    pause insertvar
    "images/inserts/minadeathstare/minadeathstare_00014.webp"
    pause insertvar
    "images/inserts/minadeathstare/minadeathstare_00015.webp"
    pause insertvar
    "images/inserts/minadeathstare/minadeathstare_00016.webp"
    pause insertvar
    "images/inserts/minadeathstare/minadeathstare_00017.webp"
    pause insertvar
    "images/inserts/minadeathstare/minadeathstare_00018.webp"
    pause insertvar
    "images/inserts/minadeathstare/minadeathstare_00019.webp"
    pause insertvar
    "images/inserts/minadeathstare/minadeathstare_00020.webp"
    pause insertvar
    "images/inserts/minadeathstare/minadeathstare_00021.webp"
    pause insertvar
    "images/inserts/minadeathstare/minadeathstare_00022.webp"
    pause insertvar
    "images/inserts/minadeathstare/minadeathstare_00023.webp"
    pause insertvar
    "images/inserts/minadeathstare/minadeathstare_00024.webp"
    pause insertvar
    "images/inserts/minadeathstare/minadeathstare_00025.webp"
    pause insertvar
    repeat


image minahyperventilate: 
    "images/inserts/minahyperventilate/minahyperventilate_00000.webp"
    pause insertvar
    "images/inserts/minahyperventilate/minahyperventilate_00001.webp"
    pause insertvar
    "images/inserts/minahyperventilate/minahyperventilate_00002.webp"
    pause insertvar
    "images/inserts/minahyperventilate/minahyperventilate_00003.webp"
    pause insertvar
    "images/inserts/minahyperventilate/minahyperventilate_00004.webp"
    pause insertvar
    "images/inserts/minahyperventilate/minahyperventilate_00005.webp"
    pause insertvar
    "images/inserts/minahyperventilate/minahyperventilate_00006.webp"
    pause insertvar
    "images/inserts/minahyperventilate/minahyperventilate_00007.webp"
    pause insertvar
    "images/inserts/minahyperventilate/minahyperventilate_00008.webp"
    pause insertvar
    "images/inserts/minahyperventilate/minahyperventilate_00009.webp"
    pause insertvar
    "images/inserts/minahyperventilate/minahyperventilate_00010.webp"
    pause insertvar
    "images/inserts/minahyperventilate/minahyperventilate_00011.webp"
    pause insertvar
    "images/inserts/minahyperventilate/minahyperventilate_00012.webp"
    pause insertvar
    "images/inserts/minahyperventilate/minahyperventilate_00013.webp"
    pause insertvar
    "images/inserts/minahyperventilate/minahyperventilate_00014.webp"
    pause insertvar
    "images/inserts/minahyperventilate/minahyperventilate_00015.webp"
    pause insertvar
    "images/inserts/minahyperventilate/minahyperventilate_00016.webp"
    pause insertvar
    "images/inserts/minahyperventilate/minahyperventilate_00017.webp"
    pause insertvar
    "images/inserts/minahyperventilate/minahyperventilate_00018.webp"
    pause insertvar
    "images/inserts/minahyperventilate/minahyperventilate_00019.webp"
    pause insertvar
    "images/inserts/minahyperventilate/minahyperventilate_00020.webp"
    pause insertvar
    "images/inserts/minahyperventilate/minahyperventilate_00021.webp"
    pause insertvar
    "images/inserts/minahyperventilate/minahyperventilate_00022.webp"
    pause insertvar
    "images/inserts/minahyperventilate/minahyperventilate_00023.webp"
    pause insertvar
    "images/inserts/minahyperventilate/minahyperventilate_00024.webp"
    pause insertvar
    "images/inserts/minahyperventilate/minahyperventilate_00025.webp"
    pause insertvar
    repeat


image minaragestare: 
    "images/inserts/minaragestare/minaragestare_00000.webp"
    pause insertvar
    "images/inserts/minaragestare/minaragestare_00001.webp"
    pause insertvar
    "images/inserts/minaragestare/minaragestare_00002.webp"
    pause insertvar
    "images/inserts/minaragestare/minaragestare_00003.webp"
    pause insertvar
    "images/inserts/minaragestare/minaragestare_00004.webp"
    pause insertvar
    "images/inserts/minaragestare/minaragestare_00005.webp"
    pause insertvar
    "images/inserts/minaragestare/minaragestare_00006.webp"
    pause insertvar
    "images/inserts/minaragestare/minaragestare_00007.webp"
    pause insertvar
    "images/inserts/minaragestare/minaragestare_00008.webp"
    pause insertvar
    "images/inserts/minaragestare/minaragestare_00009.webp"
    pause insertvar
    "images/inserts/minaragestare/minaragestare_00010.webp"
    pause insertvar
    "images/inserts/minaragestare/minaragestare_00011.webp"
    pause insertvar
    "images/inserts/minaragestare/minaragestare_00012.webp"
    pause insertvar
    "images/inserts/minaragestare/minaragestare_00013.webp"
    pause insertvar
    "images/inserts/minaragestare/minaragestare_00014.webp"
    pause insertvar
    "images/inserts/minaragestare/minaragestare_00015.webp"
    pause insertvar
    "images/inserts/minaragestare/minaragestare_00016.webp"
    pause insertvar
    "images/inserts/minaragestare/minaragestare_00017.webp"
    pause insertvar
    "images/inserts/minaragestare/minaragestare_00018.webp"
    pause insertvar
    "images/inserts/minaragestare/minaragestare_00019.webp"
    pause insertvar
    "images/inserts/minaragestare/minaragestare_00020.webp"
    pause insertvar
    "images/inserts/minaragestare/minaragestare_00021.webp"
    pause insertvar
    "images/inserts/minaragestare/minaragestare_00022.webp"
    pause insertvar
    "images/inserts/minaragestare/minaragestare_00023.webp"
    pause insertvar
    "images/inserts/minaragestare/minaragestare_00024.webp"
    pause insertvar
    "images/inserts/minaragestare/minaragestare_00025.webp"
    pause insertvar
    repeat


image minarunaway: 
    "images/inserts/minarunaway/minarunaway_00000.webp"
    pause insertvar
    "images/inserts/minarunaway/minarunaway_00001.webp"
    pause insertvar
    "images/inserts/minarunaway/minarunaway_00002.webp"
    pause insertvar
    "images/inserts/minarunaway/minarunaway_00003.webp"
    pause insertvar
    "images/inserts/minarunaway/minarunaway_00004.webp"
    pause insertvar
    "images/inserts/minarunaway/minarunaway_00005.webp"
    pause insertvar
    "images/inserts/minarunaway/minarunaway_00006.webp"
    pause insertvar
    "images/inserts/minarunaway/minarunaway_00007.webp"
    pause insertvar
    "images/inserts/minarunaway/minarunaway_00008.webp"
    pause insertvar
    "images/inserts/minarunaway/minarunaway_00009.webp"
    pause insertvar
    "images/inserts/minarunaway/minarunaway_00010.webp"
    pause insertvar
    "images/inserts/minarunaway/minarunaway_00011.webp"
    pause insertvar
    "images/inserts/minarunaway/minarunaway_00012.webp"
    pause insertvar
    "images/inserts/minarunaway/minarunaway_00013.webp"
    pause insertvar
    "images/inserts/minarunaway/minarunaway_00014.webp"
    pause insertvar
    "images/inserts/minarunaway/minarunaway_00015.webp"
    pause insertvar
    "images/inserts/minarunaway/minarunaway_00016.webp"
    pause insertvar
    "images/inserts/minarunaway/minarunaway_00017.webp"
    pause insertvar
    "images/inserts/minarunaway/minarunaway_00018.webp"
    pause insertvar
    "images/inserts/minarunaway/minarunaway_00019.webp"
    pause insertvar
    "images/inserts/minarunaway/minarunaway_00020.webp"
    pause insertvar
    "images/inserts/minarunaway/minarunaway_00021.webp"
    pause insertvar
    "images/inserts/minarunaway/minarunaway_00022.webp"
    pause insertvar
    "images/inserts/minarunaway/minarunaway_00023.webp"
    pause insertvar
    "images/inserts/minarunaway/minarunaway_00024.webp"
    pause insertvar
    "images/inserts/minarunaway/minarunaway_00025.webp"
    pause insertvar
    repeat


image rexchase: 
    "images/inserts/rexchase/rexchase_00000.webp"
    pause insertvar
    "images/inserts/rexchase/rexchase_00001.webp"
    pause insertvar
    "images/inserts/rexchase/rexchase_00002.webp"
    pause insertvar
    "images/inserts/rexchase/rexchase_00003.webp"
    pause insertvar
    "images/inserts/rexchase/rexchase_00004.webp"
    pause insertvar
    "images/inserts/rexchase/rexchase_00005.webp"
    pause insertvar
    "images/inserts/rexchase/rexchase_00006.webp"
    pause insertvar
    "images/inserts/rexchase/rexchase_00007.webp"
    pause insertvar
    "images/inserts/rexchase/rexchase_00008.webp"
    pause insertvar
    "images/inserts/rexchase/rexchase_00009.webp"
    pause insertvar
    "images/inserts/rexchase/rexchase_00010.webp"
    pause insertvar
    "images/inserts/rexchase/rexchase_00011.webp"
    pause insertvar
    "images/inserts/rexchase/rexchase_00012.webp"
    pause insertvar
    "images/inserts/rexchase/rexchase_00013.webp"
    pause insertvar
    "images/inserts/rexchase/rexchase_00014.webp"
    pause insertvar
    "images/inserts/rexchase/rexchase_00015.webp"
    pause insertvar
    "images/inserts/rexchase/rexchase_00016.webp"
    pause insertvar
    "images/inserts/rexchase/rexchase_00017.webp"
    pause insertvar
    "images/inserts/rexchase/rexchase_00018.webp"
    pause insertvar
    "images/inserts/rexchase/rexchase_00019.webp"
    pause insertvar
    "images/inserts/rexchase/rexchase_00020.webp"
    pause insertvar
    "images/inserts/rexchase/rexchase_00021.webp"
    pause insertvar
    "images/inserts/rexchase/rexchase_00022.webp"
    pause insertvar
    "images/inserts/rexchase/rexchase_00023.webp"
    pause insertvar
    "images/inserts/rexchase/rexchase_00024.webp"
    pause insertvar
    "images/inserts/rexchase/rexchase_00025.webp"
    pause insertvar
    repeat


image minarexdying: 
    "images/inserts/minarexdying/minarexdying_00000.webp"
    pause insertvar
    "images/inserts/minarexdying/minarexdying_00001.webp"
    pause insertvar
    "images/inserts/minarexdying/minarexdying_00002.webp"
    pause insertvar
    "images/inserts/minarexdying/minarexdying_00003.webp"
    pause insertvar
    "images/inserts/minarexdying/minarexdying_00004.webp"
    pause insertvar
    "images/inserts/minarexdying/minarexdying_00005.webp"
    pause insertvar
    "images/inserts/minarexdying/minarexdying_00006.webp"
    pause insertvar
    "images/inserts/minarexdying/minarexdying_00007.webp"
    pause insertvar
    "images/inserts/minarexdying/minarexdying_00008.webp"
    pause insertvar
    "images/inserts/minarexdying/minarexdying_00009.webp"
    pause insertvar
    "images/inserts/minarexdying/minarexdying_00010.webp"
    pause insertvar
    "images/inserts/minarexdying/minarexdying_00011.webp"
    pause insertvar
    "images/inserts/minarexdying/minarexdying_00012.webp"
    pause insertvar
    "images/inserts/minarexdying/minarexdying_00013.webp"
    pause insertvar
    "images/inserts/minarexdying/minarexdying_00014.webp"
    pause insertvar
    "images/inserts/minarexdying/minarexdying_00015.webp"
    pause insertvar
    "images/inserts/minarexdying/minarexdying_00016.webp"
    pause insertvar
    "images/inserts/minarexdying/minarexdying_00017.webp"
    pause insertvar
    "images/inserts/minarexdying/minarexdying_00018.webp"
    pause insertvar
    "images/inserts/minarexdying/minarexdying_00019.webp"
    pause insertvar
    "images/inserts/minarexdying/minarexdying_00020.webp"
    pause insertvar
    "images/inserts/minarexdying/minarexdying_00021.webp"
    pause insertvar
    "images/inserts/minarexdying/minarexdying_00022.webp"
    pause insertvar
    "images/inserts/minarexdying/minarexdying_00023.webp"
    pause insertvar
    "images/inserts/minarexdying/minarexdying_00024.webp"
    pause insertvar
    "images/inserts/minarexdying/minarexdying_00025.webp"
    pause insertvar
    repeat


image minarexdead: 
    "images/inserts/minarexdead/minarexdead_00000.webp"
    pause insertvar
    "images/inserts/minarexdead/minarexdead_00001.webp"
    pause insertvar
    "images/inserts/minarexdead/minarexdead_00002.webp"
    pause insertvar
    "images/inserts/minarexdead/minarexdead_00003.webp"
    pause insertvar
    "images/inserts/minarexdead/minarexdead_00004.webp"
    pause insertvar
    "images/inserts/minarexdead/minarexdead_00005.webp"
    pause insertvar
    "images/inserts/minarexdead/minarexdead_00006.webp"
    pause insertvar
    "images/inserts/minarexdead/minarexdead_00007.webp"
    pause insertvar
    "images/inserts/minarexdead/minarexdead_00008.webp"
    pause insertvar
    "images/inserts/minarexdead/minarexdead_00009.webp"
    pause insertvar
    "images/inserts/minarexdead/minarexdead_00010.webp"
    pause insertvar
    "images/inserts/minarexdead/minarexdead_00011.webp"
    pause insertvar
    "images/inserts/minarexdead/minarexdead_00012.webp"
    pause insertvar
    "images/inserts/minarexdead/minarexdead_00013.webp"
    pause insertvar
    "images/inserts/minarexdead/minarexdead_00014.webp"
    pause insertvar
    "images/inserts/minarexdead/minarexdead_00015.webp"
    pause insertvar
    "images/inserts/minarexdead/minarexdead_00016.webp"
    pause insertvar
    "images/inserts/minarexdead/minarexdead_00017.webp"
    pause insertvar
    "images/inserts/minarexdead/minarexdead_00018.webp"
    pause insertvar
    "images/inserts/minarexdead/minarexdead_00019.webp"
    pause insertvar
    "images/inserts/minarexdead/minarexdead_00020.webp"
    pause insertvar
    "images/inserts/minarexdead/minarexdead_00021.webp"
    pause insertvar
    "images/inserts/minarexdead/minarexdead_00022.webp"
    pause insertvar
    "images/inserts/minarexdead/minarexdead_00023.webp"
    pause insertvar
    "images/inserts/minarexdead/minarexdead_00024.webp"
    pause insertvar
    "images/inserts/minarexdead/minarexdead_00025.webp"
    pause insertvar
    repeat


image minadoom: 
    "images/inserts/minadoom/minadoom_00000.webp"
    pause insertvar
    "images/inserts/minadoom/minadoom_00001.webp"
    pause insertvar
    "images/inserts/minadoom/minadoom_00002.webp"
    pause insertvar
    "images/inserts/minadoom/minadoom_00003.webp"
    pause insertvar
    "images/inserts/minadoom/minadoom_00004.webp"
    pause insertvar
    "images/inserts/minadoom/minadoom_00005.webp"
    pause insertvar
    "images/inserts/minadoom/minadoom_00006.webp"
    pause insertvar
    "images/inserts/minadoom/minadoom_00007.webp"
    pause insertvar
    "images/inserts/minadoom/minadoom_00008.webp"
    pause insertvar
    "images/inserts/minadoom/minadoom_00009.webp"
    pause insertvar
    "images/inserts/minadoom/minadoom_00010.webp"
    pause insertvar
    "images/inserts/minadoom/minadoom_00011.webp"
    pause insertvar
    "images/inserts/minadoom/minadoom_00012.webp"
    pause insertvar
    "images/inserts/minadoom/minadoom_00013.webp"
    pause insertvar
    "images/inserts/minadoom/minadoom_00014.webp"
    pause insertvar
    "images/inserts/minadoom/minadoom_00015.webp"
    pause insertvar
    "images/inserts/minadoom/minadoom_00016.webp"
    pause insertvar
    "images/inserts/minadoom/minadoom_00017.webp"
    pause insertvar
    "images/inserts/minadoom/minadoom_00018.webp"
    pause insertvar
    "images/inserts/minadoom/minadoom_00019.webp"
    pause insertvar
    "images/inserts/minadoom/minadoom_00020.webp"
    pause insertvar
    "images/inserts/minadoom/minadoom_00021.webp"
    pause insertvar
    "images/inserts/minadoom/minadoom_00022.webp"
    pause insertvar
    "images/inserts/minadoom/minadoom_00023.webp"
    pause insertvar
    "images/inserts/minadoom/minadoom_00024.webp"
    pause insertvar
    "images/inserts/minadoom/minadoom_00025.webp"
    pause insertvar
    repeat


image sanctumdoor: 
    "images/inserts/sanctumdoor/sanctumdoor_00000.webp"
    pause insertvar
    "images/inserts/sanctumdoor/sanctumdoor_00001.webp"
    pause insertvar
    "images/inserts/sanctumdoor/sanctumdoor_00002.webp"
    pause insertvar
    "images/inserts/sanctumdoor/sanctumdoor_00003.webp"
    pause insertvar
    "images/inserts/sanctumdoor/sanctumdoor_00004.webp"
    pause insertvar
    "images/inserts/sanctumdoor/sanctumdoor_00005.webp"
    pause insertvar
    "images/inserts/sanctumdoor/sanctumdoor_00006.webp"
    pause insertvar
    "images/inserts/sanctumdoor/sanctumdoor_00007.webp"
    pause insertvar
    "images/inserts/sanctumdoor/sanctumdoor_00008.webp"
    pause insertvar
    "images/inserts/sanctumdoor/sanctumdoor_00009.webp"
    pause insertvar
    "images/inserts/sanctumdoor/sanctumdoor_00010.webp"
    pause insertvar
    "images/inserts/sanctumdoor/sanctumdoor_00011.webp"
    pause insertvar
    "images/inserts/sanctumdoor/sanctumdoor_00012.webp"
    pause insertvar
    "images/inserts/sanctumdoor/sanctumdoor_00013.webp"
    pause insertvar
    "images/inserts/sanctumdoor/sanctumdoor_00014.webp"
    pause insertvar
    "images/inserts/sanctumdoor/sanctumdoor_00015.webp"
    pause insertvar
    "images/inserts/sanctumdoor/sanctumdoor_00016.webp"
    pause insertvar
    "images/inserts/sanctumdoor/sanctumdoor_00017.webp"
    pause insertvar
    "images/inserts/sanctumdoor/sanctumdoor_00018.webp"
    pause insertvar
    "images/inserts/sanctumdoor/sanctumdoor_00019.webp"
    pause insertvar
    "images/inserts/sanctumdoor/sanctumdoor_00020.webp"
    pause insertvar
    "images/inserts/sanctumdoor/sanctumdoor_00021.webp"
    pause insertvar
    "images/inserts/sanctumdoor/sanctumdoor_00022.webp"
    pause insertvar
    "images/inserts/sanctumdoor/sanctumdoor_00023.webp"
    pause insertvar
    "images/inserts/sanctumdoor/sanctumdoor_00024.webp"
    pause insertvar
    "images/inserts/sanctumdoor/sanctumdoor_00025.webp"
    pause insertvar
    repeat


image bluelight: 
    block:
        "images/inserts/bluelight/bluelight_00000.webp"
        pause insertvar
        "images/inserts/bluelight/bluelight_00001.webp"
        pause insertvar
        "images/inserts/bluelight/bluelight_00002.webp"
        pause insertvar
        "images/inserts/bluelight/bluelight_00003.webp"
        pause insertvar
        "images/inserts/bluelight/bluelight_00004.webp"
        pause insertvar
        "images/inserts/bluelight/bluelight_00005.webp"
        pause insertvar
    block:
        "images/inserts/bluelight/bluelight_00006.webp"
        pause insertvar
        "images/inserts/bluelight/bluelight_00007.webp"
        pause insertvar
        "images/inserts/bluelight/bluelight_00008.webp"
        pause insertvar
        "images/inserts/bluelight/bluelight_00009.webp"
        pause insertvar
        "images/inserts/bluelight/bluelight_00010.webp"
        pause insertvar
        "images/inserts/bluelight/bluelight_00011.webp"
        pause insertvar
        "images/inserts/bluelight/bluelight_00012.webp"
        pause insertvar
        "images/inserts/bluelight/bluelight_00013.webp"
        pause insertvar
        "images/inserts/bluelight/bluelight_00014.webp"
        pause insertvar
        "images/inserts/bluelight/bluelight_00015.webp"
        pause insertvar
        "images/inserts/bluelight/bluelight_00016.webp"
        pause insertvar
        "images/inserts/bluelight/bluelight_00017.webp"
        pause insertvar
        "images/inserts/bluelight/bluelight_00018.webp"
        pause insertvar
        "images/inserts/bluelight/bluelight_00019.webp"
        pause insertvar
        "images/inserts/bluelight/bluelight_00020.webp"
        pause insertvar
        "images/inserts/bluelight/bluelight_00021.webp"
        pause insertvar
        "images/inserts/bluelight/bluelight_00022.webp"
        pause insertvar
        "images/inserts/bluelight/bluelight_00023.webp"
        pause insertvar
        "images/inserts/bluelight/bluelight_00024.webp"
        pause insertvar
        "images/inserts/bluelight/bluelight_00025.webp"
        pause insertvar
        repeat


image rexdoomstare: 
    "images/inserts/rexdoomstare/rexdoomstare_00000.webp"
    pause insertvar
    "images/inserts/rexdoomstare/rexdoomstare_00001.webp"
    pause insertvar
    "images/inserts/rexdoomstare/rexdoomstare_00002.webp"
    pause insertvar
    "images/inserts/rexdoomstare/rexdoomstare_00003.webp"
    pause insertvar
    "images/inserts/rexdoomstare/rexdoomstare_00004.webp"
    pause insertvar
    "images/inserts/rexdoomstare/rexdoomstare_00005.webp"
    pause insertvar
    "images/inserts/rexdoomstare/rexdoomstare_00006.webp"
    pause insertvar
    "images/inserts/rexdoomstare/rexdoomstare_00007.webp"
    pause insertvar
    "images/inserts/rexdoomstare/rexdoomstare_00008.webp"
    pause insertvar
    "images/inserts/rexdoomstare/rexdoomstare_00009.webp"
    pause insertvar
    "images/inserts/rexdoomstare/rexdoomstare_00010.webp"
    pause insertvar
    "images/inserts/rexdoomstare/rexdoomstare_00011.webp"
    pause insertvar
    "images/inserts/rexdoomstare/rexdoomstare_00012.webp"
    pause insertvar
    "images/inserts/rexdoomstare/rexdoomstare_00013.webp"
    pause insertvar
    "images/inserts/rexdoomstare/rexdoomstare_00014.webp"
    pause insertvar
    "images/inserts/rexdoomstare/rexdoomstare_00015.webp"
    pause insertvar
    "images/inserts/rexdoomstare/rexdoomstare_00016.webp"
    pause insertvar
    "images/inserts/rexdoomstare/rexdoomstare_00017.webp"
    pause insertvar
    "images/inserts/rexdoomstare/rexdoomstare_00018.webp"
    pause insertvar
    "images/inserts/rexdoomstare/rexdoomstare_00019.webp"
    pause insertvar
    "images/inserts/rexdoomstare/rexdoomstare_00020.webp"
    pause insertvar
    "images/inserts/rexdoomstare/rexdoomstare_00021.webp"
    pause insertvar
    "images/inserts/rexdoomstare/rexdoomstare_00022.webp"
    pause insertvar
    "images/inserts/rexdoomstare/rexdoomstare_00023.webp"
    pause insertvar
    "images/inserts/rexdoomstare/rexdoomstare_00024.webp"
    pause insertvar
    "images/inserts/rexdoomstare/rexdoomstare_00025.webp"
    pause insertvar
    repeat


image minabackstare: 
    "images/inserts/minabackstare/minabackstare_00000.webp"
    pause insertvar
    "images/inserts/minabackstare/minabackstare_00001.webp"
    pause insertvar
    "images/inserts/minabackstare/minabackstare_00002.webp"
    pause insertvar
    "images/inserts/minabackstare/minabackstare_00003.webp"
    pause insertvar
    "images/inserts/minabackstare/minabackstare_00004.webp"
    pause insertvar
    "images/inserts/minabackstare/minabackstare_00005.webp"
    pause insertvar
    "images/inserts/minabackstare/minabackstare_00006.webp"
    pause insertvar
    "images/inserts/minabackstare/minabackstare_00007.webp"
    pause insertvar
    "images/inserts/minabackstare/minabackstare_00008.webp"
    pause insertvar
    "images/inserts/minabackstare/minabackstare_00009.webp"
    pause insertvar
    "images/inserts/minabackstare/minabackstare_00010.webp"
    pause insertvar
    "images/inserts/minabackstare/minabackstare_00011.webp"
    pause insertvar
    "images/inserts/minabackstare/minabackstare_00012.webp"
    pause insertvar
    "images/inserts/minabackstare/minabackstare_00013.webp"
    pause insertvar
    "images/inserts/minabackstare/minabackstare_00014.webp"
    pause insertvar
    "images/inserts/minabackstare/minabackstare_00015.webp"
    pause insertvar
    "images/inserts/minabackstare/minabackstare_00016.webp"
    pause insertvar
    "images/inserts/minabackstare/minabackstare_00017.webp"
    pause insertvar
    "images/inserts/minabackstare/minabackstare_00018.webp"
    pause insertvar
    "images/inserts/minabackstare/minabackstare_00019.webp"
    pause insertvar
    "images/inserts/minabackstare/minabackstare_00020.webp"
    pause insertvar
    "images/inserts/minabackstare/minabackstare_00021.webp"
    pause insertvar
    "images/inserts/minabackstare/minabackstare_00022.webp"
    pause insertvar
    "images/inserts/minabackstare/minabackstare_00023.webp"
    pause insertvar
    "images/inserts/minabackstare/minabackstare_00024.webp"
    pause insertvar
    "images/inserts/minabackstare/minabackstare_00025.webp"
    pause insertvar
    repeat


image minarexdyingspecial: 
    "images/inserts/minarexdyingspecial/minarexdyingspecial_00000.webp"
    pause insertvar
    "images/inserts/minarexdyingspecial/minarexdyingspecial_00001.webp"
    pause insertvar
    "images/inserts/minarexdyingspecial/minarexdyingspecial_00002.webp"
    pause insertvar
    "images/inserts/minarexdyingspecial/minarexdyingspecial_00003.webp"
    pause insertvar
    "images/inserts/minarexdyingspecial/minarexdyingspecial_00004.webp"
    pause insertvar
    "images/inserts/minarexdyingspecial/minarexdyingspecial_00005.webp"
    pause insertvar
    "images/inserts/minarexdyingspecial/minarexdyingspecial_00006.webp"
    pause insertvar
    "images/inserts/minarexdyingspecial/minarexdyingspecial_00007.webp"
    pause insertvar
    "images/inserts/minarexdyingspecial/minarexdyingspecial_00008.webp"
    pause insertvar
    "images/inserts/minarexdyingspecial/minarexdyingspecial_00009.webp"
    pause insertvar
    "images/inserts/minarexdyingspecial/minarexdyingspecial_00010.webp"
    pause insertvar
    "images/inserts/minarexdyingspecial/minarexdyingspecial_00011.webp"
    pause insertvar
    "images/inserts/minarexdyingspecial/minarexdyingspecial_00012.webp"
    pause insertvar
    "images/inserts/minarexdyingspecial/minarexdyingspecial_00013.webp"
    pause insertvar
    "images/inserts/minarexdyingspecial/minarexdyingspecial_00014.webp"
    pause insertvar
    "images/inserts/minarexdyingspecial/minarexdyingspecial_00015.webp"
    pause insertvar
    "images/inserts/minarexdyingspecial/minarexdyingspecial_00016.webp"
    pause insertvar
    "images/inserts/minarexdyingspecial/minarexdyingspecial_00017.webp"
    pause insertvar
    "images/inserts/minarexdyingspecial/minarexdyingspecial_00018.webp"
    pause insertvar
    "images/inserts/minarexdyingspecial/minarexdyingspecial_00019.webp"
    pause insertvar
    "images/inserts/minarexdyingspecial/minarexdyingspecial_00020.webp"
    pause insertvar
    "images/inserts/minarexdyingspecial/minarexdyingspecial_00021.webp"
    pause insertvar
    "images/inserts/minarexdyingspecial/minarexdyingspecial_00022.webp"
    pause insertvar
    "images/inserts/minarexdyingspecial/minarexdyingspecial_00023.webp"
    pause insertvar
    "images/inserts/minarexdyingspecial/minarexdyingspecial_00024.webp"
    pause insertvar
    "images/inserts/minarexdyingspecial/minarexdyingspecial_00025.webp"
    pause insertvar
    repeat


image coverart: 
    "images/inserts/coverart/coverart_00000.webp"
    pause insertvar
    "images/inserts/coverart/coverart_00001.webp"
    pause insertvar
    "images/inserts/coverart/coverart_00002.webp"
    pause insertvar
    "images/inserts/coverart/coverart_00003.webp"
    pause insertvar
    "images/inserts/coverart/coverart_00004.webp"
    pause insertvar
    "images/inserts/coverart/coverart_00005.webp"
    pause insertvar
    "images/inserts/coverart/coverart_00006.webp"
    pause insertvar
    "images/inserts/coverart/coverart_00007.webp"
    pause insertvar
    "images/inserts/coverart/coverart_00008.webp"
    pause insertvar
    "images/inserts/coverart/coverart_00009.webp"
    pause insertvar
    "images/inserts/coverart/coverart_00010.webp"
    pause insertvar
    "images/inserts/coverart/coverart_00011.webp"
    pause insertvar
    "images/inserts/coverart/coverart_00012.webp"
    pause insertvar
    "images/inserts/coverart/coverart_00013.webp"
    pause insertvar
    "images/inserts/coverart/coverart_00014.webp"
    pause insertvar
    "images/inserts/coverart/coverart_00015.webp"
    pause insertvar
    "images/inserts/coverart/coverart_00016.webp"
    pause insertvar
    "images/inserts/coverart/coverart_00017.webp"
    pause insertvar
    "images/inserts/coverart/coverart_00018.webp"
    pause insertvar
    "images/inserts/coverart/coverart_00019.webp"
    pause insertvar
    "images/inserts/coverart/coverart_00020.webp"
    pause insertvar
    "images/inserts/coverart/coverart_00021.webp"
    pause insertvar
    "images/inserts/coverart/coverart_00022.webp"
    pause insertvar
    "images/inserts/coverart/coverart_00023.webp"
    pause insertvar
    "images/inserts/coverart/coverart_00024.webp"
    pause insertvar
    "images/inserts/coverart/coverart_00025.webp"
    pause insertvar
    repeat


image rexdoomed: 
    "images/inserts/rexdoomed/rexdoomed_00000.webp"
    pause insertvar
    "images/inserts/rexdoomed/rexdoomed_00001.webp"
    pause insertvar
    "images/inserts/rexdoomed/rexdoomed_00002.webp"
    pause insertvar
    "images/inserts/rexdoomed/rexdoomed_00003.webp"
    pause insertvar
    "images/inserts/rexdoomed/rexdoomed_00004.webp"
    pause insertvar
    "images/inserts/rexdoomed/rexdoomed_00005.webp"
    pause insertvar
    "images/inserts/rexdoomed/rexdoomed_00006.webp"
    pause insertvar
    "images/inserts/rexdoomed/rexdoomed_00007.webp"
    pause insertvar
    "images/inserts/rexdoomed/rexdoomed_00008.webp"
    pause insertvar
    "images/inserts/rexdoomed/rexdoomed_00009.webp"
    pause insertvar
    "images/inserts/rexdoomed/rexdoomed_00010.webp"
    pause insertvar
    "images/inserts/rexdoomed/rexdoomed_00011.webp"
    pause insertvar
    "images/inserts/rexdoomed/rexdoomed_00012.webp"
    pause insertvar
    "images/inserts/rexdoomed/rexdoomed_00013.webp"
    pause insertvar
    "images/inserts/rexdoomed/rexdoomed_00014.webp"
    pause insertvar
    "images/inserts/rexdoomed/rexdoomed_00015.webp"
    pause insertvar
    "images/inserts/rexdoomed/rexdoomed_00016.webp"
    pause insertvar
    "images/inserts/rexdoomed/rexdoomed_00017.webp"
    pause insertvar
    "images/inserts/rexdoomed/rexdoomed_00018.webp"
    pause insertvar
    "images/inserts/rexdoomed/rexdoomed_00019.webp"
    pause insertvar
    "images/inserts/rexdoomed/rexdoomed_00020.webp"
    pause insertvar
    "images/inserts/rexdoomed/rexdoomed_00021.webp"
    pause insertvar
    "images/inserts/rexdoomed/rexdoomed_00022.webp"
    pause insertvar
    "images/inserts/rexdoomed/rexdoomed_00023.webp"
    pause insertvar
    "images/inserts/rexdoomed/rexdoomed_00024.webp"
    pause insertvar
    "images/inserts/rexdoomed/rexdoomed_00025.webp"
    pause insertvar
    repeat


image minahome: 
    "images/inserts/minahome/minahome_00000.webp"
    pause insertvar
    "images/inserts/minahome/minahome_00001.webp"
    pause insertvar
    "images/inserts/minahome/minahome_00002.webp"
    pause insertvar
    "images/inserts/minahome/minahome_00003.webp"
    pause insertvar
    "images/inserts/minahome/minahome_00004.webp"
    pause insertvar
    "images/inserts/minahome/minahome_00005.webp"
    pause insertvar
    "images/inserts/minahome/minahome_00006.webp"
    pause insertvar
    "images/inserts/minahome/minahome_00007.webp"
    pause insertvar
    "images/inserts/minahome/minahome_00008.webp"
    pause insertvar
    "images/inserts/minahome/minahome_00009.webp"
    pause insertvar
    "images/inserts/minahome/minahome_00010.webp"
    pause insertvar
    "images/inserts/minahome/minahome_00011.webp"
    pause insertvar
    "images/inserts/minahome/minahome_00012.webp"
    pause insertvar
    "images/inserts/minahome/minahome_00013.webp"
    pause insertvar
    "images/inserts/minahome/minahome_00014.webp"
    pause insertvar
    "images/inserts/minahome/minahome_00015.webp"
    pause insertvar
    "images/inserts/minahome/minahome_00016.webp"
    pause insertvar
    "images/inserts/minahome/minahome_00017.webp"
    pause insertvar
    "images/inserts/minahome/minahome_00018.webp"
    pause insertvar
    "images/inserts/minahome/minahome_00019.webp"
    pause insertvar
    "images/inserts/minahome/minahome_00020.webp"
    pause insertvar
    "images/inserts/minahome/minahome_00021.webp"
    pause insertvar
    "images/inserts/minahome/minahome_00022.webp"
    pause insertvar
    "images/inserts/minahome/minahome_00023.webp"
    pause insertvar
    "images/inserts/minahome/minahome_00024.webp"
    pause insertvar
    "images/inserts/minahome/minahome_00025.webp"
    pause insertvar
    repeat


image minashell: 
    "images/inserts/minashell/minashell_00000.webp"
    pause insertvar
    "images/inserts/minashell/minashell_00001.webp"
    pause insertvar
    "images/inserts/minashell/minashell_00002.webp"
    pause insertvar
    "images/inserts/minashell/minashell_00003.webp"
    pause insertvar
    "images/inserts/minashell/minashell_00004.webp"
    pause insertvar
    "images/inserts/minashell/minashell_00005.webp"
    pause insertvar
    "images/inserts/minashell/minashell_00006.webp"
    pause insertvar
    "images/inserts/minashell/minashell_00007.webp"
    pause insertvar
    "images/inserts/minashell/minashell_00008.webp"
    pause insertvar
    "images/inserts/minashell/minashell_00009.webp"
    pause insertvar
    "images/inserts/minashell/minashell_00010.webp"
    pause insertvar
    "images/inserts/minashell/minashell_00011.webp"
    pause insertvar
    "images/inserts/minashell/minashell_00012.webp"
    pause insertvar
    "images/inserts/minashell/minashell_00013.webp"
    pause insertvar
    "images/inserts/minashell/minashell_00014.webp"
    pause insertvar
    "images/inserts/minashell/minashell_00015.webp"
    pause insertvar
    "images/inserts/minashell/minashell_00016.webp"
    pause insertvar
    "images/inserts/minashell/minashell_00017.webp"
    pause insertvar
    "images/inserts/minashell/minashell_00018.webp"
    pause insertvar
    "images/inserts/minashell/minashell_00019.webp"
    pause insertvar
    "images/inserts/minashell/minashell_00020.webp"
    pause insertvar
    "images/inserts/minashell/minashell_00021.webp"
    pause insertvar
    "images/inserts/minashell/minashell_00022.webp"
    pause insertvar
    "images/inserts/minashell/minashell_00023.webp"
    pause insertvar
    "images/inserts/minashell/minashell_00024.webp"
    pause insertvar
    "images/inserts/minashell/minashell_00025.webp"
    pause insertvar
    repeat


image rexdeadbody: 
    "images/inserts/rexdeadbody/rexdeadbody_00000.webp"
    pause insertvar
    "images/inserts/rexdeadbody/rexdeadbody_00001.webp"
    pause insertvar
    "images/inserts/rexdeadbody/rexdeadbody_00002.webp"
    pause insertvar
    "images/inserts/rexdeadbody/rexdeadbody_00003.webp"
    pause insertvar
    "images/inserts/rexdeadbody/rexdeadbody_00004.webp"
    pause insertvar
    "images/inserts/rexdeadbody/rexdeadbody_00005.webp"
    pause insertvar
    "images/inserts/rexdeadbody/rexdeadbody_00006.webp"
    pause insertvar
    "images/inserts/rexdeadbody/rexdeadbody_00007.webp"
    pause insertvar
    "images/inserts/rexdeadbody/rexdeadbody_00008.webp"
    pause insertvar
    "images/inserts/rexdeadbody/rexdeadbody_00009.webp"
    pause insertvar
    "images/inserts/rexdeadbody/rexdeadbody_00010.webp"
    pause insertvar
    "images/inserts/rexdeadbody/rexdeadbody_00011.webp"
    pause insertvar
    "images/inserts/rexdeadbody/rexdeadbody_00012.webp"
    pause insertvar
    "images/inserts/rexdeadbody/rexdeadbody_00013.webp"
    pause insertvar
    "images/inserts/rexdeadbody/rexdeadbody_00014.webp"
    pause insertvar
    "images/inserts/rexdeadbody/rexdeadbody_00015.webp"
    pause insertvar
    "images/inserts/rexdeadbody/rexdeadbody_00016.webp"
    pause insertvar
    "images/inserts/rexdeadbody/rexdeadbody_00017.webp"
    pause insertvar
    "images/inserts/rexdeadbody/rexdeadbody_00018.webp"
    pause insertvar
    "images/inserts/rexdeadbody/rexdeadbody_00019.webp"
    pause insertvar
    "images/inserts/rexdeadbody/rexdeadbody_00020.webp"
    pause insertvar
    "images/inserts/rexdeadbody/rexdeadbody_00021.webp"
    pause insertvar
    "images/inserts/rexdeadbody/rexdeadbody_00022.webp"
    pause insertvar
    "images/inserts/rexdeadbody/rexdeadbody_00023.webp"
    pause insertvar
    "images/inserts/rexdeadbody/rexdeadbody_00024.webp"
    pause insertvar
    "images/inserts/rexdeadbody/rexdeadbody_00025.webp"
    pause insertvar
    repeat


image minasickly: 
    "images/inserts/minasickly/minasickly_00000.webp"
    pause insertvar
    "images/inserts/minasickly/minasickly_00001.webp"
    pause insertvar
    "images/inserts/minasickly/minasickly_00002.webp"
    pause insertvar
    "images/inserts/minasickly/minasickly_00003.webp"
    pause insertvar
    "images/inserts/minasickly/minasickly_00004.webp"
    pause insertvar
    "images/inserts/minasickly/minasickly_00005.webp"
    pause insertvar
    "images/inserts/minasickly/minasickly_00006.webp"
    pause insertvar
    "images/inserts/minasickly/minasickly_00007.webp"
    pause insertvar
    "images/inserts/minasickly/minasickly_00008.webp"
    pause insertvar
    "images/inserts/minasickly/minasickly_00009.webp"
    pause insertvar
    "images/inserts/minasickly/minasickly_00010.webp"
    pause insertvar
    "images/inserts/minasickly/minasickly_00011.webp"
    pause insertvar
    "images/inserts/minasickly/minasickly_00012.webp"
    pause insertvar
    "images/inserts/minasickly/minasickly_00013.webp"
    pause insertvar
    "images/inserts/minasickly/minasickly_00014.webp"
    pause insertvar
    "images/inserts/minasickly/minasickly_00015.webp"
    pause insertvar
    "images/inserts/minasickly/minasickly_00016.webp"
    pause insertvar
    "images/inserts/minasickly/minasickly_00017.webp"
    pause insertvar
    "images/inserts/minasickly/minasickly_00018.webp"
    pause insertvar
    "images/inserts/minasickly/minasickly_00019.webp"
    pause insertvar
    "images/inserts/minasickly/minasickly_00020.webp"
    pause insertvar
    "images/inserts/minasickly/minasickly_00021.webp"
    pause insertvar
    "images/inserts/minasickly/minasickly_00022.webp"
    pause insertvar
    "images/inserts/minasickly/minasickly_00023.webp"
    pause insertvar
    "images/inserts/minasickly/minasickly_00024.webp"
    pause insertvar
    "images/inserts/minasickly/minasickly_00025.webp"
    pause insertvar
    repeat






