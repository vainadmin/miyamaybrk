label demo:

##########
#####
###
#
#
# SCENE ONE
#
#
##
###
#####
##########

    scene blackbackground onlayer master
    show blackover onlayer effects 
    show frame169 onlayer imagedrop4 
    show sceneonelying onlayer backdrop1 


    $ transhift = 0.143
    show tranonereverse onlayer effects
    pause 2.0

    $ SoundOff(2.0)
    $ ClearLayers()

    pause 1.0

    NU """MUTUAL HARROW"""

    python:
        achievement.grant("a0")
        achievement.sync()

    show frame169 onlayer imagedrop4 
    show blackover onlayer imagedrop5

    play music1 "sceneoneatm2.mp3" fadein 2.5 volume 0.3

    show sceneonemain onlayer imagedrop1
    $ manual_underlay("underlay", 0, 0, 0)
    pause 1.5
    
    NW """SECTION 56: ENTRANCE"""

    $ hide_underlay("underlay")
    pause 1.0

    scene tranone onlayer imagedrop5
    pause 3.0

    $ show_new_line("16:9", "Narrator", "narrator", "neutral")
    pause 1.0
    NW """Moonlight scatters across fields of overgrown weeds, shrubs, and forest."""

    $ show_new_line("16:9", "Narrator", "narrator", "neutral")
    NW """Rex and Mina make their way through the thick shrubs."""

    scene widetoultra onlayer imagedrop4

    $ hide_underlay("underlay")
    pause 1.0


##########
#####
###
#
#
# DEMO ONE: 21:9 STAND 
#
#
##
###
#####
##########

    show sceneonechar onlayer imagedrop2
    with Dissolve(3.0)
            
    scene blackover onlayer imagedrop1

    hide nulll
    show underlayb onlayer under
    with Dissolve(0.5)

    $ shadowcharvar = 0
    $ shadowvar = 0.5

    show rexstandingshadow onlayer chardrop00
    show rexstandinglove onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.5)
    
    RSU """So this is Section 56..."""
    
    hide rexstandingshadow
    hide rexstandinglove
    hide rexstandingdark

    $ lumafade = 0.001
    
    show rexstandingshadow onlayer chardrop00
    show rexstandingsmug onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.5)
    
    RSU """Seems pretty harmless, don't you think?"""
    
    hide rexstandingshadow
    hide rexstandingsmug
    hide rexstandingdark
    with Dissolve(0.5)

    $ lumafade = 0.169
    
    
    show minastandingshadow onlayer chardrop00
    show minastandingregret onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.5)
    
    MSU """I'm not sure about that... This whole place makes me feel nervous."""
    MSU """I hope we're not making the wrong decision by coming here..."""
    
    hide minastandingshadow
    hide minastandingregret
    hide minastandingdark
    with Dissolve(0.5)

    $ ClearLayers()
    scene blackbackground onlayer master

##########
#####
###
#
#
# DEMO TWO: 21:9 ZOOM 
#
#
##
###
#####
##########

    show sceneonerailchar onlayer imagedrop1
    show frame219 onlayer imagedrop4 


    hide nulll
    show underlayc onlayer under
    with Dissolve(0.5)
    
    $ shadowcharvar = 0
    $ shadowvar = 0.5

    
    show rexzoomshadow onlayer chardrop00
    show rexzoomangry onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.5)
    
    RZU """...Why are you walking so slowly?"""
    
    hide rexzoomshadow
    hide rexzoomangry
    hide rexzoomdark
    with Dissolve(0.5)
    
    
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.5)
    
    MZU """I don't know. This whole place just makes me paranoid."""
    
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    with Dissolve(0.5)
    
    
    show rexzoomshadow onlayer chardrop00
    show rexzoompain onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.5)
    
    RZU """You were clinging to me when we first got here..."""
    
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    with Dissolve(0.5)
    
    
    show minazoomshadow onlayer chardrop00
    show minazoomangry onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.5)
    
    MZU """I'm confused and stressed; just let me be, okay?"""

    $ ClearLayers()
    scene blackbackground onlayer master

##########
#####
###
#
#
# DEMO THREE: 21:9 NARRATION 
#
#
##
###
#####
##########

    show scenetwoundermain onlayer imagedrop1
    show frame219 onlayer imagedrop4 

    hide nulll
    show underlayc onlayer under
    with Dissolve(0.5)

 
    NU """Rex looks back to find Mina on the other side of the underpass."""
    NU """She clutches her wrist as if she's trying to hide something."""


    $ ClearLayers()
    scene blackbackground onlayer master

##########
#####
###
#
#
# DEMO FOUR: 16:9 FACE
#
#
##
###
#####
##########

    show scenefivemain onlayer imagedrop1
    show frame169 onlayer imagedrop4 

    # $ shadowcharvar = 0
    # $ shadowvar = 0.5

    hide nulll
    show underlayb onlayer under
    with Dissolve(0.2)
    
    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show minafaceshock onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.5)
    
    MFW """I've never seen plants like this; they have such strange hues and shapes."""
        
    $ lumafade = 0.0001
    
    show minafaceserious onlayer chardrop1 at face_wide
    hide minafaceshock
    with Dissolve(0.2)

    
    MFW """I guess it's not a coincidence that my father chose Section 56 for his illegal activities."""

    # 0.2 seems to be ideal 
    
    hide facebackground
    hide facedark
    hide minafaceserious
    hide minafacedark
    with Dissolve(0.2)
    
    $ lumafade = 0.169

    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show rexfacecontent onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    RFW """Exactly. Section 56 has always been special compared to other areas nearby."""
        
    
    $ lumafade = 0.0001
    
    
    show rexfaceneutral onlayer chardrop1 at face_wide
    hide rexfacecontent
    with Dissolve(0.2)


    RFW """For one thing, it has wilderness and terrain that simply aren't found in the flat, grassy areas next to the city."""
        
    show rexfaceserious onlayer chardrop1 at face_wide
    hide rexfaceneutral
    with Dissolve(0.5)
    
    
    RFW """It's the perfect area to hide things... to develop things away from prying eyes."""

    $ ClearLayers()
    scene blackbackground onlayer master


##########
#####
###
#
#
# DEMO FIVE: 21:9 ZOOM EFFECTS 
#
#
##
###
#####
##########

    show scenesevenchar onlayer imagedrop1
    show frame219 onlayer imagedrop4 

    $ shadowcharvar = 0.9
    $ darkcharvar = 0.2


    hide nulll
    show underlayb onlayer under
    with Dissolve(0.5)
    
    
    show rexstandingshadow onlayer chardrop00
    show rexstandingregret onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.5)
    
    RSU """...I wish that were the case."""
    
    hide rexstandingshadow
    hide rexstandingregret
    hide rexstandingdark
    with Dissolve(0.5)

    hide underlayb
    show underlayc onlayer under
    with Dissolve(0.5)
    

    show minazoomshadow onlayer chardrop00
    show minazoomangry onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.5)
    
    MZU """Rex, please!"""
    MZU """I already have enough issues to deal with."""


    $ ClearLayers()
    scene blackbackground onlayer master


##########
#####
###
#
#
# DEMO SIX: 16:9 NARRATION
#
#
##
###
#####
##########

    $ shadowcharvar = 0
    $ darkcharvar = 0


    show sceneeightmain onlayer imagedrop1
    show frame169 onlayer imagedrop4 


    hide nulll
    show underlayc onlayer under
    with Dissolve(0.5)
    
    NU """Mina falls to her knees."""
    NU """She starts to cry."""

    $ ClearLayers()
    scene blackbackground onlayer master



##########
#####
###
#
#
# DEMO SEVEN: CHOICE
#
#
##
###
#####
##########


    show scenefourchar onlayer imagedrop1
    show frame219 onlayer imagedrop4 


    # $ shadowcharvar = 0.5
    # $ darkcharvar = 0.5



    $ show_new_line("16:9", "Narrator", "narrator", "neutral")
    NW """A short distance away from the playground, Rex and Mina encounter some abandoned apartments."""
    
    
    
    hide underlay
    show underlayc onlayer under
    with Dissolve(0.5)
    
    
    
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.5)
    
    
    MZU """(It's the root cause of all of this suffering)"""

    show blackover onlayer chardrop5:
        alpha 0.5

    hide underlayc

    return    