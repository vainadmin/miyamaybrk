################################################################################
## Initialization
################################################################################

# Without this, beepy_voice won't be registered in time for the Characters
init offset = -1

###############
###
### 
### CORE IMAGES / FOUNDATIONS
###
###
###############

image blackbackground = "gui/blackbackground.png"
image blackout = "gui/blackbackground.png"
image wideframe = "gui/widescreenframe.png"

###############
###
### 
### LAYERING SYSTEM
###
###
###############

init python:
    def CharSpriteMask(d):
        return AlphaMask(d, "images/charcompmask.png")

init python:
    def ClearChar():
        renpy.scene(layer='under')
        renpy.scene(layer='chardrop00')
        renpy.scene(layer='chardrop0')
        renpy.scene(layer='chardrop1')
        renpy.scene(layer='chardrop2')
        renpy.scene(layer='chardrop3')

init python:
    def ClearOverframe():
        renpy.scene(layer='under')
        renpy.scene(layer='imagedrop5')
        renpy.scene(layer='imagedrop6')
        renpy.scene(layer='imagedrop7')
        renpy.scene(layer='imagedrop8')
        renpy.scene(layer='imagedrop9')



init python:
    def ClearLayers():
        global underlaylast, emotionlast

        underlaylast = "nulll"
        emotionlast = "nulll"

        renpy.scene(layer='chardrop1')
        # renpy.with_statement(Dissolve(1.0))
        renpy.scene(layer='backdrop1')
        renpy.scene(layer='backdrop2')
        renpy.scene(layer='backdrop3')
        renpy.scene(layer='backdrop4')
        renpy.scene(layer='backdrop5')
        renpy.scene(layer='backdrop6')
        renpy.scene(layer='imagedrop1')
        renpy.scene(layer='imagedrop2')
        renpy.scene(layer='imagedrop3')
        renpy.scene(layer='under')
        renpy.scene(layer='imagedrop4')
        renpy.scene(layer='imagedrop5')
        renpy.scene(layer='imagedrop6')
        renpy.scene(layer='imagedrop7')
        renpy.scene(layer='imagedrop8')
        renpy.scene(layer='imagedrop9')
        renpy.scene(layer='chardrop00')
        renpy.scene(layer='chardrop0')
        renpy.scene(layer='chardrop1')
        renpy.scene(layer='chardrop2')
        renpy.scene(layer='chardrop3')
        renpy.scene(layer='chardrop4')
        renpy.scene(layer='chardrop5')
        renpy.scene(layer='effects')
        renpy.scene(layer='effects2')

init python:
    def ClearHalf():
        global underlaylast, emotionlast

        underlaylast = "nulll"
        emotionlast = "nulll"

        renpy.scene(layer='backdrop4')
        renpy.scene(layer='backdrop5')
        renpy.scene(layer='backdrop6')
        renpy.scene(layer='imagedrop1')
        renpy.scene(layer='imagedrop2')
        renpy.scene(layer='imagedrop3')
        renpy.scene(layer='imagedrop4')
        renpy.scene(layer='imagedrop5')
        renpy.scene(layer='imagedrop6')
        renpy.scene(layer='under')
        renpy.scene(layer='chardrop00')
        renpy.scene(layer='chardrop0')
        renpy.scene(layer='chardrop1')
        renpy.scene(layer='chardrop2')
        renpy.scene(layer='chardrop3')
        renpy.scene(layer='chardrop4')
        renpy.scene(layer='chardrop5')

init python:
    def SoundOff(fadevalue):
        renpy.music.stop(channel='music1', fadeout=fadevalue)
        renpy.music.stop(channel='music2', fadeout=fadevalue)
        renpy.music.stop(channel='music3', fadeout=fadevalue)
        renpy.music.stop(channel='music4', fadeout=fadevalue)
        renpy.music.stop(channel='fx1', fadeout=fadevalue)
        renpy.music.stop(channel='fx2', fadeout=fadevalue)
        renpy.music.stop(channel='fx3', fadeout=fadevalue)
        renpy.music.set_volume(1.0, delay=3, channel='music1')
        renpy.music.set_volume(1.0, delay=3, channel='music2')
        renpy.music.set_volume(1.0, delay=3, channel='music3')
        renpy.music.set_volume(1.0, delay=3, channel='music4')
        renpy.music.set_volume(1.0, delay=3, channel='fx1')
        renpy.music.set_volume(1.0, delay=3, channel='fx2')
        renpy.music.set_volume(1.0, delay=3, channel='fx3')




# Create the extra layers 
init python:

    # layer master is the bottom-most layer

    ###
    ### BACKDROP LAYERS
    ###

    renpy.add_layer("backdrop1", 
                    above="master", 
                    below=None, 
                    menu_clear=True, 
                    sticky=None)

    renpy.add_layer("backdrop2", 
                    above="backdrop1", 
                    below=None, 
                    menu_clear=True, 
                    sticky=None)
    
    renpy.add_layer("backdrop3", 
                    above="backdrop2", 
                    below=None, 
                    menu_clear=True, 
                    sticky=None)

    renpy.add_layer("backdrop4", 
                    above="backdrop3", 
                    below=None, 
                    menu_clear=True, 
                    sticky=None)

    renpy.add_layer("backdrop5", 
                    above="backdrop4", 
                    below=None, 
                    menu_clear=True, 
                    sticky=None)

    renpy.add_layer("backdrop6", 
                    above="backdrop5", 
                    below=None, 
                    menu_clear=True, 
                    sticky=None)


    ###
    ### IMAGE LAYERS
    ###

    renpy.add_layer("imagedrop1", 
                    above="backdrop6", 
                    below=None, 
                    menu_clear=True, 
                    sticky=None)

    renpy.add_layer("imagedrop2", 
                    above="imagedrop1", 
                    below=None, 
                    menu_clear=True, 
                    sticky=None)

    renpy.add_layer("imagedrop3", 
                    above="imagedrop2", 
                    below=None, 
                    menu_clear=True, 
                    sticky=None)

    renpy.add_layer("imagedrop4", 
                    above="imagedrop3", 
                    below=None, 
                    menu_clear=True, 
                    sticky=None)

    renpy.add_layer("imagedrop5", 
                    above="imagedrop4", 
                    below=None, 
                    menu_clear=True, 
                    sticky=None)

    renpy.add_layer("imagedrop6", 
                    above="imagedrop5", 
                    below=None, 
                    menu_clear=True, 
                    sticky=None)

    renpy.add_layer("imagedrop7", 
                    above="imagedrop6", 
                    below=None, 
                    menu_clear=True, 
                    sticky=None)

    renpy.add_layer("imagedrop8", 
                    above="imagedrop7", 
                    below=None, 
                    menu_clear=True, 
                    sticky=None)

    renpy.add_layer("imagedrop9", 
                    above="imagedrop8", 
                    below=None, 
                    menu_clear=True, 
                    sticky=None)


    ###
    ### CHARACTER LAYERS
    ###

    renpy.add_layer("chardrop00", 
                    above="imagedrop9", 
                    below=None, 
                    menu_clear=True, 
                    sticky=None)

    renpy.add_layer("chardrop0", 
                        above="chardrop00", 
                        below=None, 
                        menu_clear=True, 
                        sticky=None)

    renpy.add_layer("chardrop1", 
                    above="chardrop0", 
                    below=None, 
                    menu_clear=True, 
                    sticky=None)

    renpy.add_layer("chardrop2", 
                    above="chardrop1", 
                    below=None, 
                    menu_clear=True, 
                    sticky=None)

    renpy.add_layer("chardrop3", 
                    above="chardrop2", 
                    below=None, 
                    menu_clear=True, 
                    sticky=None)

    renpy.add_layer("chardrop4", 
                    above="chardrop3", 
                    below=None, 
                    menu_clear=True, 
                    sticky=None)

    renpy.add_layer("chardrop5", 
                    above="chardrop4", 
                    below=None, 
                    menu_clear=True, 
                    sticky=None)

    renpy.add_layer("chardrop6", 
                    above="chardrop5", 
                    below=None, 
                    menu_clear=True, 
                    sticky=None)

    renpy.add_layer("under", 
                    above="chardrop6", 
                    below=None, 
                    menu_clear=True, 
                    sticky=None)


    ###
    ### FX / ABOVE UI LAYERS 
    ###    

    # effects layer, Layer above UI, so above the dialogue box [screens] 
    renpy.add_layer("effects", 
                    above="screens", 
                    below=None, 
                    menu_clear=True, 
                    sticky=None)
    
    renpy.add_layer("effects2", 
                    above="effects", 
                    below=None, 
                    menu_clear=True, 
                    sticky=None)

    # heaven layer, Layer above UI, so above the dialogue box [screens] 
    renpy.add_layer("heaven", 
                    above="overlay", 
                    below=None, 
                    menu_clear=True, 
                    sticky=None)

###############
###
### 
### UI FX
###
###
###############

# EXAMPLE transform for all possibilities
# transform custom_transform:
    # xpos 150         # 150 pixels from the left edge
    # ypos 300         # 300 pixels from the top edge
    # xanchor 0.5      # Anchor at the center of the image.
    # yanchor 0.5
    # xzoom 0.5        # Scale width to 50%
    # yzoom 0.5        # Scale height to 50%
    # rotate 45        # Rotate 45 degrees
    # alpha 0.8        # 80% opacity
    # subpixel True    # Enable subpixel rendering for smoother animation
    # xoffset 10       # Additional 10 pixels offset on x-axis
    # yoffset 10       # Additional 10 pixels offset on y-axis

transform face_wide:
    zoom 0.16
    xpos 180
    ypos 705

transform face_ultrawide:
    zoom 0.16
    xpos 180
    ypos 705


transform face_standard:
    zoom 0.16
    xpos 262
    ypos 698

transform face_hover:
    on hover:
        linear 0.1 zoom 0.5
        xpos 180
        ypos 705
    on idle:
        linear 0.1 zoom 0.4
        xpos 180
        ypos 705

    


transform left_standing:
    xzoom 0.8
    yzoom 0.8
    xpos -180
    ypos 180

transform right_standing:
    xzoom 0.8
    yzoom 0.8
    xpos 750
    ypos 180



transform ultrawide:
    ypos -60


transform linear_scale(timeo=3, zoomo=1.5):
    linear timeo zoom zoomo

transform linear_move(timeo=3, xpoo=0, ypoo=0):
    linear timeo xpos xpoo, ypos ypoo

transform linear_fade(timeo=3, starto=0.00, endo=1.00):
    alpha starto
    linear timeo alpha endo

transform shake_effect(delayo=0.0458, offseto=10, repeato=0):
    # linear is the time between each beat 
    yoffset 0.0
    linear delayo yoffset offseto
    linear delayo yoffset -offseto
    linear delayo yoffset offseto
    linear delayo yoffset -offseto
    linear delayo yoffset offseto
    linear delayo yoffset -offseto
    linear delayo yoffset offseto
    linear delayo yoffset -offseto
    linear delayo yoffset offseto
    linear delayo yoffset -offseto
    linear delayo yoffset offseto
    linear delayo yoffset -offseto
    linear delayo yoffset offseto
    linear delayo yoffset -offseto
    linear delayo yoffset offseto
    linear delayo yoffset -offseto
    linear delayo yoffset offseto
    linear delayo yoffset -offseto
    yoffset 0.0
    repeat repeato 

# This can be used with screens 
transform basicfade:
    on show:
        alpha 0.0
        linear 3.0 alpha 1.0
    on hide:
        linear 3.0 alpha 0.0 

###############
###
### 
### TESTING COMPONENTS / REFERENCES 
###
###
###############

transform double_fade(starta=0.00, ta=2.5, enda=0.50, wait=2, tb=2.5, endb=0.00):
    alpha starta
    linear ta alpha enda
    pause wait
    linear tb alpha endb

transform scale_up_down:
    # linear 1.0 zoom 1.5: Scales the image up to 1.5x its original size over 1 second.
    linear 8.0 zoom 1.02
    linear 8.0 zoom 0.98
    repeat
transform cust_position:
    zoom 0.5
    rotate 0
    alpha 0.8
    anchor (0, 0) # Center of the image
    align (0.5, 0.5) # Center of the screen

transform scale_to_cover:
    xpos 0.5
    ypos 0.5
    xanchor 0.5
    yanchor 0.5
    zoom 10  # Adjust this zoom factor to ensure it covers the black bars

image dissolve_testC:
    "images/mainmenubg/bg1.png"
    linear 5.0 alpha 0.0

image dissolve_testCC:
    "images/mainmenubg/bg1.png"
    pause 1
    "images/mainmenubg/bg2.png"
    pause 1
    "images/mainmenubg/bg3.png"
    pause 1
    "images/mainmenubg/bg4.png"
    linear 3.0 alpha 0.0  # Gradually fade out over 5 seconds
    # match linear with the total time period

# This shows how you can combine effects with statements like hide 
init python:
    import renpy.exports as renpy

    def hide_with_dissolve(image, time):
        renpy.show(image, layer='master', what=None)
        renpy.with_statement(Dissolve(time))
        renpy.hide(image, layer='master')

init python:
    def manual_underlay(underlaytype, shakedelay, shakeoffset, shakecount):
        global underlaylast, underlaydelay

        renpy.scene(layer='under')
        if shakedelay > 0:
            renpy.show(underlaytype, layer='under', at_list=[shake_effect(shakedelay, shakeoffset, shakecount)])
            renpy.with_statement(Dissolve(underlaydelay))
        else:
            renpy.show(underlaytype, layer='under', what=None)
            renpy.with_statement(Dissolve(underlaydelay))

            log_event(f" ")
            log_event(f"show {underlaytype} onlayer under")
            log_event(f"with Dissolve({underlaydelay})") 

        underlaylast = underlaytype

init python:
    def hide_underlay(underlaytype):
        global underlaylast, underlaydelay

        renpy.hide(underlaytype, layer='under')
        renpy.with_statement(Dissolve(underlaydelay))

        log_event(f" ")
        log_event(f"hide {underlaytype}")
        log_event(f"with Dissolve({underlaydelay})") 


        underlaylast = "null"

init python:
    def hide_characters(characterdelay=0.5):
        global emotionlast
        renpy.scene(layer='chardrop00')
        renpy.scene(layer='chardrop0')
        renpy.scene(layer='chardrop1')
        renpy.scene(layer='chardrop2')
        renpy.scene(layer='chardrop3')
        renpy.with_statement(Dissolve(characterdelay))

        emotionlast = "nulll"



init python:
    def hide_all_char_layers(tag00, tag0, ctag1, ctag3, ctag4):
        global emotiondelay

        triggered = False

        log_event(f" ")

        renpy.hide(tag00, layer='chardrop00')
        renpy.hide(tag0, layer='chardrop0')
        renpy.hide(ctag1, layer='chardrop1')
        renpy.hide(ctag3, layer='chardrop3')
        renpy.hide(ctag4, layer='chardrop4')
        renpy.with_statement(Dissolve(emotiondelay))

        if tag00 != "nulll":
            triggered = True
            log_event(f"hide {tag00}")
        if tag0 != "nulll":
            triggered = True
            log_event(f"hide {tag0}")
        if ctag1 != "nulll":
            triggered = True
            log_event(f"hide {ctag1}")
        if ctag3 != "nulll":
            triggered = True
            log_event(f"hide {ctag3}")
        if ctag4 != "nulll":
            triggered = True
            log_event(f"hide {ctag4}")

        if triggered:
            log_event(f"with Dissolve({emotiondelay})") 



        log_event(f" ")


init python:
    def show_general_emotion(tag00, tag0, ctag1, ctag3, ctag4, dch, dcc, shadowstr, emotionstr, darkenstr):
        global emotiondelay

        log_event(f" ")


        triggered = False

        if dch is True:
            renpy.hide(tag00, layer='chardrop00')
            renpy.hide(tag0, layer='chardrop0')
            renpy.hide(ctag1, layer='chardrop1')
            renpy.hide(ctag3, layer='chardrop3')
            renpy.hide(ctag4, layer='chardrop4')
            renpy.with_statement(Dissolve(emotiondelay))

            if tag00 != "nulll":
                triggered = True
                log_event(f"hide {tag00}")
            if tag0 != "nulll":
                triggered = True
                log_event(f"hide {tag0}")
            if ctag1 != "nulll":
                triggered = True
                log_event(f"hide {ctag1}")
            if ctag3 != "nulll":
                triggered = True
                log_event(f"hide {ctag3}")
            if ctag4 != "nulll":
                triggered = True
                log_event(f"hide {ctag4}")

            if triggered:
                log_event(f"with Dissolve({emotiondelay})") 

            renpy.show(shadowstr, layer='chardrop00')
            renpy.show(emotionstr, layer='chardrop1')
            renpy.show(darkenstr, layer='chardrop3')
            renpy.with_statement(Dissolve(emotiondelay))

            log_event(f"$ lumafade = 0.1")
            log_event(f"show {shadowstr} onlayer chardrop00")
            log_event(f"show {emotionstr} onlayer chardrop1")
            log_event(f"show {darkenstr} onlayer chardrop3")
            log_event(f"with Dissolve({emotiondelay})")
            log_event(f" ")
        else:
            if dcc is False:
                renpy.hide(ctag1, layer='chardrop1')
                renpy.show(emotionstr, layer='chardrop1')
                renpy.with_statement(Dissolve(emotiondelay))

                log_event(f"$ lumafade = 0.001")
                log_event(f"hide {ctag1}")
                log_event(f"show {emotionstr} onlayer chardrop1")
                log_event(f"with Dissolve({emotiondelay})")
                log_event(f" ")
            else:
                renpy.hide(tag00, layer='chardrop00')
                renpy.hide(ctag1, layer='chardrop1')
                renpy.hide(ctag3, layer='chardrop3')
                renpy.show(shadowstr, layer='chardrop00')
                renpy.show(emotionstr, layer='chardrop1')
                renpy.show(darkenstr, layer='chardrop3')
                renpy.with_statement(Dissolve(emotiondelay))

                log_event(f"$ lumafade = 0.1")

                log_event(f"hide {tag00}")
                log_event(f"hide {ctag1}")
                log_event(f"hide {ctag3}")
                log_event(f"show {shadowstr} onlayer chardrop00")
                log_event(f"show {emotionstr} onlayer chardrop1")
                log_event(f"show {darkenstr} onlayer chardrop3")
                log_event(f"with Dissolve({emotiondelay})")


                log_event(f" ")

        log_event(f" ")


init python:
    def show_general_face(tag00, tag0, ctag1, ctag3, ctag4, dch, dcc, shadowstr, emotionstr, darkenstr, faceposi):
        global emotiondelay

        log_event(f" ")


        triggered = False

        if dch is True:
            renpy.hide(tag00, layer='chardrop00')
            renpy.hide(tag0, layer='chardrop0')
            renpy.hide(ctag1, layer='chardrop1')
            renpy.hide(ctag3, layer='chardrop3')
            renpy.hide(ctag4, layer='chardrop4')
            renpy.with_statement(Dissolve(emotiondelay))

            if tag00 != "nulll":
                triggered = True
                log_event(f"hide {tag00}")
            if tag0 != "nulll":
                triggered = True
                log_event(f"hide {tag0}")
            if ctag1 != "nulll":
                triggered = True
                log_event(f"hide {ctag1}")
            if ctag3 != "nulll":
                triggered = True
                log_event(f"hide {ctag3}")
            if ctag4 != "nulll":
                triggered = True
                log_event(f"hide {ctag4}")

            if triggered:
                log_event(f"with Dissolve({emotiondelay})") 

            if faceposi == "face_standard":
                renpy.show("facebackground", layer='chardrop00', 
                        at_list=[face_standard])
                renpy.show("facedark", layer='chardrop0', 
                        at_list=[face_standard])
                renpy.show(emotionstr, layer='chardrop1', 
                        at_list=[face_standard])
                renpy.show(darkenstr, layer='chardrop3', 
                        at_list=[face_standard])
                renpy.with_statement(Dissolve(emotiondelay))
            else:
                renpy.show("facebackground", layer='chardrop00', 
                        at_list=[face_wide])
                renpy.show("facedark", layer='chardrop0', 
                        at_list=[face_wide])
                renpy.show(emotionstr, layer='chardrop1', 
                        at_list=[face_wide])
                renpy.show(darkenstr, layer='chardrop3', 
                        at_list=[face_wide])
                renpy.with_statement(Dissolve(emotiondelay))

            log_event(f"$ lumafade = 0.1 ")
            log_event(f"show facebackground onlayer chardrop00 at {faceposi}")
            log_event(f"show facedark onlayer chardrop0 at {faceposi}")
            log_event(f"show {emotionstr} onlayer chardrop1 at {faceposi}")
            log_event(f"show {darkenstr} onlayer chardrop3 at {faceposi}")
            log_event(f"with Dissolve({emotiondelay})")
            log_event(f" ")
        else:
            if dcc is False:
                renpy.hide(ctag1, layer='chardrop1')
                if faceposi == "face_standard":
                    renpy.show(emotionstr, layer='chardrop1', 
                        at_list=[face_standard])
                else:
                    renpy.show(emotionstr, layer='chardrop1', 
                        at_list=[face_wide])
                renpy.with_statement(Dissolve(emotiondelay))

                log_event(f"$ lumafade = 0.001")
                log_event(f"hide {ctag1}")
                log_event(f"show {emotionstr} onlayer chardrop1 at {faceposi}")
                log_event(f"with Dissolve({emotiondelay})")
                log_event(f" ")
            else:
                renpy.hide(ctag1, layer='chardrop1')
                renpy.hide(ctag3, layer='chardrop3')
                if faceposi == "face_standard":
                    renpy.show(emotionstr, layer='chardrop1', 
                        at_list=[face_standard])
                    renpy.show(darkenstr, layer='chardrop3', 
                        at_list=[face_standard])
                else:
                    renpy.show(emotionstr, layer='chardrop1', 
                        at_list=[face_wide])
                    renpy.show(darkenstr, layer='chardrop3', 
                        at_list=[face_wide])
                renpy.with_statement(Dissolve(emotiondelay))

                log_event(f"$ lumafade = 0.1")

                log_event(f"hide {ctag1}")
                log_event(f"hide {ctag3}")
                log_event(f"show {emotionstr} onlayer chardrop1 at {faceposi}")
                log_event(f"show {darkenstr} onlayer chardrop3 at {faceposi}")
                log_event(f"with Dissolve({emotiondelay})")


                log_event(f" ")

        log_event(f" ")



init python:
    def show_new_line(frame, character, dialoguetype, emotion):
        global underlaylast, emotionlast, underlaydelay, emotiondelay, dialoguelast, characterlast

        # For optimised purpose, need a bunch of easily separated print
        # statements that clearly show the statements 
        # print("$$$$$$$ START NEW COMAND $$$$$$$$")

        # We first check if it's narration or not.
        # If not narration, we know for sure it's a character.
        # We can treat all characters the same way. 

        # Get the image names if available on the character layers
        undertag = next(iter(renpy.get_showing_tags(layer="under")), "nulll")
        tag00 = next(iter(renpy.get_showing_tags(layer="chardrop00")), "nulll")
        tag0 = next(iter(renpy.get_showing_tags(layer="chardrop0")), "nulll")
        ctag1 = next(iter(renpy.get_showing_tags(layer="chardrop1")), "nulll")
        ctag3 = next(iter(renpy.get_showing_tags(layer="chardrop3")), "nulll")
        ctag4 = next(iter(renpy.get_showing_tags(layer="chardrop4")), "nulll")


        # Check if the dialogue type has changed, if so
        # we need to clear the layers

        dch = False    
        if dialoguelast != dialoguetype:
            dch = True
            
        dialoguelast = dialoguetype

        # In the case that same dialogue type, but different character
        # We change just the required layers

        dcc = False
        if characterlast != character:
            dcc = True

        characterlast = character


        if "narrator" in character.lower() or "narrat" in dialoguetype.lower():
            if emotionlast != "nulll":
                # If the last emotion was not null, we clear it.
                hide_all_char_layers(tag00, tag0, ctag1, ctag3, ctag4)

                emotionlast = "nulll"

            if "4:3" in frame and underlaylast != "underlay":
                renpy.hide(undertag, layer='under')
                renpy.show("underlay", layer='under', what=None)
                renpy.with_statement(Dissolve(underlaydelay))

                log_event(f" ")
                log_event(f"hide {undertag}")
                log_event(f"show underlay onlayer under")
                log_event(f"with Dissolve({underlaydelay})")
                log_event(f" ")

                underlaylast = "underlay"
            elif "16:9" in frame and underlaylast != "underlay":
                renpy.hide(undertag, layer='under')
                renpy.show("underlay", layer='under', what=None)
                renpy.with_statement(Dissolve(underlaydelay))

                log_event(f" ")
                log_event(f"hide {undertag}")
                log_event(f"show underlay onlayer under")
                log_event(f"with Dissolve({underlaydelay})")
                log_event(f" ")

                underlaylast = "underlay"
            elif "21:9" in frame and underlaylast != "underlayc":
                renpy.hide(undertag, layer='under')
                renpy.show("underlayc", layer='under', what=None)
                renpy.with_statement(Dissolve(underlaydelay))

                log_event(f" ")
                log_event(f"hide {undertag}")
                log_event(f"show underlayc onlayer under")
                log_event(f"with Dissolve({underlaydelay})")
                log_event(f" ")

                underlaylast = "underlayc"
        else:
            # Get the underlay done first 
            if "standing" in dialoguetype.lower() or "face" in dialoguetype.lower():
                if "4:3" in frame and underlaylast != "underlayd":
                    hide_all_char_layers(tag00, tag0, ctag1, ctag3, ctag4)                                        

                    renpy.hide(undertag, layer='under')
                    renpy.show("underlayd", layer='under', what=None)
                    renpy.with_statement(Dissolve(underlaydelay))

                    log_event(f" ")
                    log_event(f"hide {undertag}")
                    log_event(f"show underlayd onlayer under")
                    log_event(f"with Dissolve({underlaydelay})")
                    log_event(f" ")

                    underlaylast = "underlayd"
                elif "16:9" in frame and underlaylast != "underlayb":
                    hide_all_char_layers(tag00, tag0, ctag1, ctag3, ctag4)

                    renpy.hide(undertag, layer='under')
                    renpy.show("underlayb", layer='under', what=None)
                    renpy.with_statement(Dissolve(underlaydelay))

                    log_event(f" ")
                    log_event(f"hide {undertag}")
                    log_event(f"show underlayb onlayer under")
                    log_event(f"with Dissolve({underlaydelay})")
                    log_event(f" ")

                    underlaylast = "underlayb"
                elif "21:9" in frame and underlaylast != "underlayb":
                    hide_all_char_layers(tag00, tag0, ctag1, ctag3, ctag4)

                    renpy.hide(undertag, layer='under')
                    renpy.show("underlayb", layer='under', what=None)
                    renpy.with_statement(Dissolve(underlaydelay))

                    log_event(f" ")
                    log_event(f"hide {undertag}")
                    log_event(f"show underlayb onlayer under")
                    log_event(f"with Dissolve({underlaydelay})")
                    log_event(f" ")

                    underlaylast = "underlayb"
            elif "zoom" in dialoguetype.lower():
                if "4:3" in frame and underlaylast != "underlay":
                    hide_all_char_layers(tag00, tag0, ctag1, ctag3, ctag4)

                    renpy.hide(undertag, layer='under')
                    renpy.show("underlay", layer='under', what=None)
                    renpy.with_statement(Dissolve(underlaydelay))

                    log_event(f" ")
                    log_event(f"hide {undertag}")
                    log_event(f"show underlay onlayer under")
                    log_event(f"with Dissolve({underlaydelay})")
                    log_event(f" ")

                    underlaylast = "underlay"
                elif "16:9" in frame and underlaylast != "underlay":
                    hide_all_char_layers(tag00, tag0, ctag1, ctag3, ctag4)

                    renpy.hide(undertag, layer='under')
                    renpy.show("underlay", layer='under', what=None)
                    renpy.with_statement(Dissolve(underlaydelay))

                    log_event(f" ")
                    log_event(f"hide {undertag}")
                    log_event(f"show underlay onlayer under")
                    log_event(f"with Dissolve({underlaydelay})")
                    log_event(f" ")

                    underlaylast = "underlay"
                elif "21:9" in frame and underlaylast != "underlayc":
                    hide_all_char_layers(tag00, tag0, ctag1, ctag3, ctag4)
                    
                    renpy.hide(undertag, layer='under')
                    renpy.show("underlayc", layer='under', what=None)
                    renpy.with_statement(Dissolve(underlaydelay))

                    log_event(f" ")
                    log_event(f"hide {undertag}")
                    log_event(f"show underlayc onlayer under")
                    log_event(f"with Dissolve({underlaydelay})")
                    log_event(f" ")

                    underlaylast = "underlayc"

            emotionstr = character.lower() + dialoguetype.lower() + emotion.lower()
            darkenstr = character.lower() + dialoguetype.lower() + "dark"
            shadowstr = character.lower() + dialoguetype.lower() + "shadow"

            ####
            #### NOTE: emotionstr does NOT account for face width
            #### NOTE: This means face switching 4:3 to 16:9 will not work
            ####
            if emotionstr == emotionlast:
                # same as the last one, we don't need to show it again.
                return

            # We can never have more than one image on a layer for char 


            if "4:3" in frame and dialoguetype.lower() == "face":
                show_general_face(tag00, tag0, ctag1, ctag3, ctag4, dch, dcc, shadowstr, emotionstr, darkenstr, "face_standard")
                emotionlast = emotionstr
            elif "16:9" in frame and dialoguetype.lower() == "face":
                show_general_face(tag00, tag0, ctag1, ctag3, ctag4, dch, dcc, shadowstr, emotionstr, darkenstr, "face_wide")
                emotionlast = emotionstr
            elif "21:9" in frame and dialoguetype.lower() == "face":
                show_general_face(tag00, tag0, ctag1, ctag3, ctag4, dch, dcc, shadowstr, emotionstr, darkenstr, "face_wide")            
                emotionlast = emotionstr
            else:
                show_general_emotion(tag00, tag0, ctag1, ctag3, ctag4, dch, dcc, shadowstr, emotionstr, darkenstr)                
                emotionlast = emotionstr


init python:
    class MouseTracker(renpy.Displayable):
        def __init__(self):
            super(MouseTracker, self).__init__()
            self.last_pos = (0, 0)
            # Add this displayable to overlays
            config.overlay_functions.append(self.overlay)

        def overlay(self):
            return self

        def render(self, width, height, st, at):
            return renpy.Render(1, 1)  # Invisible, but active

        def event(self, ev, x, y, st):
            import pygame


            #if ev.type == pygame.MOUSEMOTION:
            #    self.last_pos = (x, y)
            #    print("Mouse moved to:", self.last_pos)
            #return
        
#init python:
    #mouse_tracker = MouseTracker()


init python:
    import datetime

    def log_event(event_description):
        log_path = os.path.join(config.basedir, "directive_log.txt") 

        # Open (or create) a log file for writing in append mode
        with open(log_path, "a", encoding="utf-8") as log_file:
            # Add a timestamp and the event
            log_file.write(f"{event_description}\n")
