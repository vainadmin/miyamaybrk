
####
##
## Character Definitions 
##
######

#
##
### Narrator
##
#


# Wide or Square, 16:9, aka 1, also usable for 4:3 with wide underlay
define NW = Character(
    "", 
    what_style="say_thought", 
    ctc="ctcnarration",
    ctc_position="fixed")

define NS = Character(
    "", 
    what_style="say_thought", 
    ctc="ctcnarration",
    ctc_position="fixed")

# Ultrawide, 21:9, aka 2
define NU = Character(
    "", 
    what_style="frame1_ultrawide", 
    ctc="ctcwidescreen",
    ctc_position="fixed")

#
##
### Parents 
##
#

define ANW = Character(
    "??????", 
    namebox_style="say_thought_character_namebox", 
    what_style="say_thought_character", 
    callback=functools.partial(beepy_voice, 
                    beepfile="memorytalk.mp3",
                    speakerstyle="rexnarrationstandard"),
    ctc="ctcnarration",
    ctc_position="fixed")

define ANS = Character(
    "??????", 
    namebox_style="say_thought_character_namebox", 
    what_style="say_thought_character", 
    callback=functools.partial(beepy_voice, 
                    beepfile="memorytalk.mp3",
                    speakerstyle="rexnarrationwide"),
    ctc="ctcnarration",
    ctc_position="fixed")

define ANU = Character(
    "??????", 
    namebox_style="say_thought_charultra_namebox", 
    what_style="say_thought_charultra", 
    callback=functools.partial(beepy_voice, 
                        beepfile="memorytalk.mp3",
                        speakerstyle="rexnarrationultra"),
    ctc="ctcwidescreen",
    ctc_position="fixed")


define BNW = Character(
    "??????", 
    namebox_style="say_thought_character_namebox", 
    what_style="say_thought_character", 
    callback=functools.partial(beepy_voice, 
                    beepfile="memorytalk3.mp3",
                    speakerstyle="rexnarrationstandard"),
    ctc="ctcnarration",
    ctc_position="fixed")

define BNS = Character(
    "??????", 
    namebox_style="say_thought_character_namebox", 
    what_style="say_thought_character", 
    callback=functools.partial(beepy_voice, 
                    beepfile="memorytalk3.mp3",
                    speakerstyle="rexnarrationwide"),
    ctc="ctcnarration",
    ctc_position="fixed")

define BNU = Character(
    "??????", 
    namebox_style="say_thought_charultra_namebox", 
    what_style="say_thought_charultra", 
    callback=functools.partial(beepy_voice, 
                        beepfile="memorytalk3.mp3",
                        speakerstyle="rexnarrationultra"),
    ctc="ctcwidescreen",
    ctc_position="fixed")


define CNW = Character(
    "??????", 
    namebox_style="say_thought_character_namebox", 
    what_style="say_thought_character", 
    callback=functools.partial(beepy_voice, 
                    beepfile="memorytalk2.mp3",
                    speakerstyle="rexnarrationstandard"),
    ctc="ctcnarration",
    ctc_position="fixed")

define CNS = Character(
    "??????", 
    namebox_style="say_thought_character_namebox", 
    what_style="say_thought_character", 
    callback=functools.partial(beepy_voice, 
                    beepfile="memorytalk2.mp3",
                    speakerstyle="rexnarrationwide"),
    ctc="ctcnarration",
    ctc_position="fixed")

define CNU = Character(
    "??????", 
    namebox_style="say_thought_charultra_namebox", 
    what_style="say_thought_charultra", 
    callback=functools.partial(beepy_voice, 
                        beepfile="memorytalk2.mp3",
                        speakerstyle="rexnarrationultra"),
    ctc="ctcwidescreen",
    ctc_position="fixed")


define DNW = Character(
    "??????", 
    namebox_style="say_thought_character_namebox", 
    what_style="say_thought_character", 
    callback=functools.partial(beepy_voice, 
                    beepfile="memorytalk4.mp3",
                    speakerstyle="rexnarrationstandard"),
    ctc="ctcnarration",
    ctc_position="fixed")

define DNS = Character(
    "??????", 
    namebox_style="say_thought_character_namebox", 
    what_style="say_thought_character", 
    callback=functools.partial(beepy_voice, 
                    beepfile="memorytalk4.mp3",
                    speakerstyle="rexnarrationwide"),
    ctc="ctcnarration",
    ctc_position="fixed")

define DNU = Character(
    "??????", 
    namebox_style="say_thought_charultra_namebox", 
    what_style="say_thought_charultra", 
    callback=functools.partial(beepy_voice, 
                        beepfile="memorytalk4.mp3",
                        speakerstyle="rexnarrationultra"),
    ctc="ctcwidescreen",
    ctc_position="fixed")



#
##
### Rex
##
#

# Narration 4:3/16:9/21:9
define RNS = Character(_("Rex"), 
    namebox_style="say_thought_character_namebox", 
    what_style="say_thought_character", 
    callback=functools.partial(beepy_voice, 
                            beepfile="soratalk.mp3",
                            speakerstyle="rexnarrationstandard"),
    ctc="ctcnarration",
    ctc_position="fixed")

define RNW = Character(_("Rex"), 
    namebox_style="say_thought_character_namebox", 
    what_style="say_thought_character", 
    callback=functools.partial(beepy_voice, 
                            beepfile="soratalk.mp3",
                            speakerstyle="rexnarrationwide"),
    ctc="ctcnarration",
    ctc_position="fixed")

define RNU = Character(_("Rex"), 
    namebox_style="say_thought_charultra_namebox", 
    what_style="say_thought_charultra", 
    callback=functools.partial(beepy_voice, 
                            beepfile="soratalk.mp3",
                            speakerstyle="rexnarrationultra"),
    ctc="ctcwidescreen",
    ctc_position="fixed")

# Standing 4:3/16:9/21:9
define RSS = Character(_("Rex"), 
    callback=functools.partial(beepy_voice, 
                beepfile="soratalk.mp3",
                speakerstyle="rexstandingmouth"),
    who_xpos = 70, 
    who_ypos = 23,
    what_style="widefour_dialogue",
    ctc="ctcfourthree",
    ctc_position="fixed")

define RSW = Character(_("Rex"), 
    callback=functools.partial(beepy_voice, 
                            beepfile="soratalk.mp3",
                            speakerstyle="rexstandingmouth"),
    ctc="ctcdialogue",
    ctc_position="fixed")

define RSU = Character(_("Rex"), 
    callback=functools.partial(beepy_voice, 
                            beepfile="soratalk.mp3",
                            speakerstyle="rexstandingmouth"),
    ctc="ctcdialogue",
    ctc_position="fixed")

# Face 4:3/16:9/21:9
define RFS = Character(_("Rex"), 
    callback=functools.partial(beepy_voice, 
                beepfile="soratalk.mp3",
                speakerstyle="rexfacestandardmouth"),
    who_xpos = 70, 
    who_ypos = 23,
    what_style="widefour_dialogue",
    ctc="ctcfourthree",
    ctc_position="fixed")

define RFW = Character(_("Rex"), 
    callback=functools.partial(beepy_voice, 
                            beepfile="soratalk.mp3",
                            speakerstyle="rexfacewidemouth"),
    ctc="ctcdialogue",
    ctc_position="fixed")

define RFU = Character(_("Rex"), 
    callback=functools.partial(beepy_voice, 
                            beepfile="soratalk.mp3",
                            speakerstyle="rexfacewidemouth"),
    ctc="ctcdialogue",
    ctc_position="fixed")

# Zoom 4:3/16:9/21:9
define RZS = Character(_("Rex"), 
    namebox_style="say_thought_character_namebox", 
    what_style="say_thought_character", 
    callback=functools.partial(beepy_voice, 
                            beepfile="soratalk.mp3",
                            speakerstyle="rexzoommouth"),
    ctc="ctcnarration",
    ctc_position="fixed")

define RZW = Character(_("Rex"), 
    namebox_style="say_thought_character_namebox", 
    what_style="say_thought_character", 
    callback=functools.partial(beepy_voice, 
                            beepfile="soratalk.mp3",
                            speakerstyle="rexzoommouth"),
    ctc="ctcnarration",
    ctc_position="fixed")

define RZU = Character(_("Rex"), 
    namebox_style="say_thought_charultra_namebox", 
    what_style="say_thought_charultra", 
    callback=functools.partial(beepy_voice, 
                            beepfile="soratalk.mp3",
                            speakerstyle="rexzoommouth"),
    ctc="ctcwidescreen",
    ctc_position="fixed")



#
##
### Mina
##
#

# Narration 4:3/16:9/21:9
define MNS = Character(_("Mina"), 
    namebox_style="say_thought_character_namebox", 
    what_style="say_thought_character", 
    callback=functools.partial(beepy_voice, 
                            beepfile="maydaytalk.mp3",
                            speakerstyle="minanarrationstandard"),
    ctc="ctcnarration",
    ctc_position="fixed")

define MNW = Character(_("Mina"), 
    namebox_style="say_thought_character_namebox", 
    what_style="say_thought_character", 
    callback=functools.partial(beepy_voice, 
                            beepfile="maydaytalk.mp3",
                            speakerstyle="minanarrationwide"),
    ctc="ctcnarration",
    ctc_position="fixed")

define MNU = Character(_("Mina"), 
    namebox_style="say_thought_charultra_namebox", 
    what_style="say_thought_charultra", 
    callback=functools.partial(beepy_voice, 
                            beepfile="maydaytalk.mp3",
                            speakerstyle="minanarrationultra"),
    ctc="ctcwidescreen",
    ctc_position="fixed")

# Standing 4:3/16:9/21:9
define MSS = Character(_("Mina"), 
    callback=functools.partial(beepy_voice, 
                beepfile="maydaytalk.mp3",
                speakerstyle="minastandingmouth"),
    who_xpos = 70, 
    who_ypos = 23,
    what_style="widefour_dialogue",
    ctc="ctcfourthree",
    ctc_position="fixed")

define MSW = Character(_("Mina"), 
    callback=functools.partial(beepy_voice, 
                            beepfile="maydaytalk.mp3",
                            speakerstyle="minastandingmouth"),
    ctc="ctcdialogue",
    ctc_position="fixed")

define MSU = Character(_("Mina"), 
    callback=functools.partial(beepy_voice, 
                            beepfile="maydaytalk.mp3",
                            speakerstyle="minastandingmouth"),
    ctc="ctcdialogue",
    ctc_position="fixed")

# Face 4:3/16:9/21:9
define MFS = Character(_("Mina"), 
    callback=functools.partial(beepy_voice, 
                beepfile="maydaytalk.mp3",
                speakerstyle="minafacestandardmouth"),
    who_xpos = 70, 
    who_ypos = 23,
    what_style="widefour_dialogue",
    ctc="ctcfourthree",
    ctc_position="fixed")

define MFW = Character(_("Mina"), 
    callback=functools.partial(beepy_voice, 
                            beepfile="maydaytalk.mp3",
                            speakerstyle="minafacewidemouth"),
    ctc="ctcdialogue",
    ctc_position="fixed")

define MFU = Character(_("Mina"), 
    callback=functools.partial(beepy_voice, 
                            beepfile="maydaytalk.mp3",
                            speakerstyle="minafacewidemouth"),
    ctc="ctcdialogue",
    ctc_position="fixed")

# Zoom 4:3/16:9/21:9
define MZS = Character(_("Mina"), 
    namebox_style="say_thought_character_namebox", 
    what_style="say_thought_character", 
    callback=functools.partial(beepy_voice, 
                            beepfile="maydaytalk.mp3",
                            speakerstyle="minazoommouth"),
    ctc="ctcnarration",
    ctc_position="fixed")

define MZW = Character(_("Mina"), 
    namebox_style="say_thought_character_namebox", 
    what_style="say_thought_character", 
    callback=functools.partial(beepy_voice, 
                            beepfile="maydaytalk.mp3",
                            speakerstyle="minazoommouth"),
    ctc="ctcnarration",
    ctc_position="fixed")

define MZU = Character(_("Mina"), 
    namebox_style="say_thought_charultra_namebox", 
    what_style="say_thought_charultra", 
    callback=functools.partial(beepy_voice, 
                            beepfile="maydaytalk.mp3",
                            speakerstyle="minazoommouth"),
    ctc="ctcwidescreen",
    ctc_position="fixed")







####
##
## Core Variables (They get saved with file)
##
######

#default endingA = False
#default endingB = False
#default endingC = True
#default location = "kowkow"
#default nocairo = 0

### Ending Variables

default trustrex = 0
default notrustrex = 0
default trustmina = 0
default notrustmina = 0


default freewill = False
default totalcontrol = False
default depression = False

### ATL Variables
#### NOTE: YOU MUST RE-SCENE or RE-SHOW FOR CHANGES TO TAKE EFFECT!
# default standfade = 0.167

default choice_position = None 

# Programming variables 
default say_what = "null"
default say_who = "null"
default facestage = "rexstanding"
default underlaylast = "null"
default emotionlast = "null"
default emotiondone = False
default dialoguelast = "null"
default characterlast = "null"

# Backdrop and transition variables
default aspectshift = 0.167
default transhift = 0.167
default backdropvar = 0.167


# Underlays 
default underlayvar = 0.1 # transition speed for underlay
default underlaydelay = 0.3 # dissolve delay for underlay

# Emotional Display Variables 
default lumafade = 0.1 # transition speed for luma
default emotiondelay = 0.2 # dissolve delay for emotion
default shadowvar = 0.10 # speed of shadow
default shadowcharvar = 0.5 # opacity of shadow
default darkcharvar = 0 # opacity of general darkener 
default mouthvariable = 0.167 # mouth speed
default blinkingvar = 0.4 # blinking speed
default facebackvariable = 0.5 # face bg speed
define fxvar = 0.167 # fx speed
default insertvar = 0.167 # insert speed



## Menu References

##  play sound "choicebeep.mp3"
##  menu:
##    "Go Straight to Scene 1 of Mine Memory":
##        # jump means we CANNOT go back
##        jump act_one
##    "Continue to Test Section":
##        pass

## menu:
##    "Explore the house":
##        # call ensures we can GO BACK
##        call explore_house from _call_explore_house
##    "Stay here":
##        # call ensures we can GO BACK
##        call stay_here from _call_stay_here

## label explore_house:
##      c "I think we should explore the house. There might be clues around."
##      return
## label stay_here:
##      c "Let's stay here for now. It's too dangerous to move around."
##      return

##
## Text Effect Reference
##
# h "What's that?{w} ...It's not what I think it is {nw=1.0}"
#
# c "{i}It is... {/i} {w=0.2} it's a screening session for... {w=0.2}\n{b}MINE MEMORY{/b}"
#
# h ".{w=0.2}.{w=0.2}.{w=0.2}. that's my favorite movie"
#
# c "Mine too. {size=*1.2}Shut the fuck up{/size},{size=*0.5} ...I wanna watch{/size}{nw=0.5}"
#
# h "{size=*2} HEY! {/size}{fast} {nw=1.0}"
#
# n "The {k=1.5}MINE MEMORY{/k} 
#
# {alpha=0.5}screening is about to begin...{/alpha}"
#
# show eileen concerned
# e "Sometimes, I feel sad.{nw}"
# show eileen happy
# extend " But I usually quickly get over it!" 
#
#     This is same as {w}
#     B "Remind me again why it seems like you’re the only one in the company that"
#    extend " can’t even pretend to stay focused during such an important presentation?"
#
#
# This is how masks work
# show layer master4 at CharSpriteMask
# show hanatest onlayer master4 at shake_effect(0.04, 25, 5) with Dissolve(1.0)
#
#show hanatest onlayer master4:
#     linear 9.0 xzoom(0.5)
#
# show hanatest onlayer master3:
#    parallel:
#        pass
#        shake_effect(0.04, 50, 5)
#    parallel:
#        linear_fade(5, 0, 0.8)
#    parallel:
#        pass
#        linear_move(5, -50, -100)
#    parallel:
#        linear_scale(5, 1.2)
#
#    scene scene1q with shake_effect(0.0458, 10)
#    scene s1backdrop onlayer master2 at linear_fade(5, 0, 1)
#    scene lightingback1 onlayer master3 at double_fade(0, 5, 1, 2, 2, 0)
#    show hanatest onlayer master3 at linear_fade(5, 0, 1)
#
#    Split across multiple lines
#   
#    B """To be honest, you should be working twice as hard as everyone else … 
#           Considering your background"""
#
#
# Audio ... 
#
#    play music4 "django.mp3" fadein 1.0 volume 0.2
#    play music2 "scenefivesfxbgm.mp3" fadein 4.0 volume 0.3
#    play fx1 "bango.mp3" volume 1.0
#
#    stop music fadeout 1.0
#    stop fx1 fadeout 1.0
#    stop music2 fadeout 1.0
#
#    play audio [ "<silence .5>", "boom.opus" ]
#
#    $ renpy.music.set_volume(1, delay=0.5, channel='music')
#    $ renpy.music.set_volume(0, delay=1, channel='music4')
#
#    $ renpy.music.set_pan(pan, delay, channel='music')
#    pan  between -1 and 1 that control the placement of the audio. 
#    If this is -1, then all audio is sent to the left channel. If it's 0, 
#    then the two channels are equally balanced
#


label start:
    scene expression "#000"
    with Dissolve(2.0)
    with Pause(2)

    scene blackbackground onlayer master

    # jump demo 
    jump scene_one
