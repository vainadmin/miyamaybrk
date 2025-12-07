    ##
    ### SCENE 1 [ACT 1 SCENE 1]
    ##
    # #:50,80s/\<NU\>/RNU/g ###  

label scene_one:

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

    #play music1 "bgma.mp3" fadein 2.5 volume 0.3
    #play fx2 "doorclose.mp3" volume 0.7

    #show frame43  onlayer effects
    #show underlay onlayer under
    #with Dissolve(0.3)

    #scene snowfields onlayer imagedrop1
    #show snowfieldtrans onlayer imagedrop2
    #with Dissolve(2.5)

    # show rexneutralnarrator onlayer chardrop1

    #show testface onlayer imagedrop2
    #show face1 onlayer imagedrop3:
    #    zoom 0.5
    # show sorapainface onlayer chardrop1 at face_portrait

    #show backdroptest onlayer imagedrop1
    #show underlayc onlayer under 
    #show widetoultra onlayer effects

    #show bloodheadache onlayer imagedrop2:
    #   shake_effect(0.04, 10, 4)


    # $ underlayvar = 0.001
    # $ transhift = 0.15
    # $ aspectshift = 0.05
    # $ aspectshift = 0.167
    # $ underlayvar = 0.167

    # pause 2.0

    #$ ClearLayers()
    #$ SoundOff(2.0)

    scene blackbackground onlayer master
    show blackover onlayer effects 
    show frame169 onlayer imagedrop4 

    play music1 "sceneonestart.mp3" fadein 2.5 volume 0.3
    play music2 "rain.mp3" fadein 2.5 volume 0.2

    $ aspectshift = 0.100

    hide blackover
    show widetoultra onlayer imagedrop4
    show rainfx onlayer effects
    with Dissolve(1.5)

    show underlayc onlayer under
    with Dissolve(0.3)

    play fx2 "insertkick.mp3" volume 0.1
    show insertstoryone onlayer imagedrop3

    RNU """It all started that night, remember?"""

    RNU """I found your pale body on the grass."""

    play fx2 "insertkick.mp3" volume 0.1
    hide insertstoryone
    show insertstorytwo onlayer imagedrop3

    RNU """...Right next to my father's tombstone."""

    RNU """I was certain you were dead."""

    play fx1 "getup.mp3" volume 0.7
    play fx2 "insertkick.mp3" volume 0.1
    hide insertstorytwo
    show insertstorythree onlayer imagedrop3

    RNU """But you got up and stared at me."""

    RNU """And the first words you said to me?"""

    show underlaycstatic onlayer under:
        shake_effect(0.04, 10, 4)
    

    MNU """“I'm going to be the death of you.”"""

    play fx2 "insertkick.mp3" volume 0.1
    hide insertstorythree
    show insertstoryfive onlayer imagedrop3

    RNU """And before I could say anything back... you lunged at me."""

    RNU """I thought you were going to kill me."""

    play fx1 "knife.mp3" volume 0.7
    play fx2 "insertkick.mp3" volume 0.1
    hide insertstoryfive
    show insertstoryfour onlayer imagedrop3

    RNU """But then you crumbled into my arms."""

    RNU """You started sobbing."""

    RNU """Your tears and makeup stained my shirt."""

    play fx2 "insertkick.mp3" volume 0.1
    hide insertstoryfour
    show insertstorysix onlayer imagedrop3

    RNU """I couldn't make sense of what had happened."""

    RNU """It was absurd... simply absurd."""

    RNU """But as you kept sobbing, something miraculous happened."""

    show noisedistortfx onlayer imagedrop3

    RNU """I felt warmth... a warmth that felt almost suffocating."""

    RNU """A warmth that I had yearned to feel for years."""

    RNU """...At that point, I knew I was never going to be the same again."""

    $ renpy.music.set_volume(0.1, delay=3, channel='music1')

    RNU """Up until that night, I was throwing my life away for nothing."""

    $ renpy.music.set_volume(0.3, delay=3, channel='music2')

    hide insertstorysix
    with Dissolve(0.3)

    RNU """Now I'm willing to throw my life away for you."""

    $ SoundOff(2.0)
    hide noisedistortfx
    hide frame169
    hide widetoultra
    hide underlaycstatic
    hide underlayc 
    with Dissolve(0.5)

    pause 2.5

    play fx1 "lightning.mp3" volume 0.7
    show thunderfx onlayer effects2
    show inserttitle onlayer imagedrop4

    pause

    hide inserttitle
    hide rainfx
    with Dissolve(3.0)

    $ ClearLayers()

    pause 2.0

    #python:
    #    achievement.grant("a0")
    #    achievement.sync()

    show frame169 onlayer imagedrop4 
    show blackover onlayer imagedrop5

    play music1 "sceneoneatm2.mp3" fadein 2.5 volume 0.3

    show sceneonemain onlayer imagedrop1
    show underlay onlayer under
    pause 1.5

    
    NW """SECTION 56: ENTRANCE"""

    
    pause 1.0

    scene tranone onlayer imagedrop5
    pause 3.0


    python:
        achievement.grant("a0")
        achievement.sync()


    
    NW """Moonlight scatters across overgrown fields of weeds, shrubs, and trees."""
    NW """Rex and Mina make their way through the thick shrubbery."""

    scene widetoultra onlayer imagedrop4

    hide underlay 
    pause 1.0



    show sceneonechar onlayer imagedrop2
    with Dissolve(3.0)
            
    #show sectionentrance onlayer imagedrop2:
        #linear 3.0 zoom 1.1

    # pause 4.0

    $ shadowvar = 0.4
    $ shadowcharvar = 0.0
    $ darkcharvar = 0

    show underlayb onlayer under
    with Dissolve(0.5)
    
    $ renpy.music.set_volume(0.2, delay=2, channel='music1')
    
    show rexstandingshadow onlayer chardrop00
    show rexstandinglove onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    play fx1 "s56now.mp3" volume 0.15
    
    RSU """So this is Section 56..."""

    $ lumafade = 0.001
    
    hide rexstandinglove
    show rexstandingsmug onlayer chardrop1
    with Dissolve(0.2)

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    
    RSU """Seems pretty harmless, don't you think?"""

    $ lumafade = 0.1
    
    
    hide rexstandingshadow
    hide rexstandingsmug
    hide rexstandingdark
    show minastandingshadow onlayer chardrop00
    show minastandingregret onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSU """I'm not sure about that... This whole place makes me nervous."""
    MSU """I hope we're not making the wrong decision by coming here..."""
    
    hide minastandingshadow
    hide minastandingregret
    hide minastandingdark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlayc onlayer under
    with Dissolve(0.5)
    
    
    hide minastandingshadow
    hide minastandingregret
    hide minastandingdark
    with Dissolve(0.2)

    $ renpy.music.set_volume(0.2, delay=2, channel='music1')
    
    show rexzoomshadow onlayer chardrop00
    show rexzoomcontent onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    play fx2 "s56lore.mp3" volume 0.15

    show flowersfx onlayer imagedrop5:
        alpha 0.3
    with Dissolve(0.5)
    
    
    RZU """Don't worry, Mina. If we just keep going, paradise awaits us."""

    $ renpy.music.set_volume(1, delay=2, channel='music1')

    $ lumafade = 0.001
    
    
    hide rexzoomcontent
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """A paradise that will make everything we've been through worth it."""

    $ lumafade = 0.1
    
    
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomregret onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """What kind of paradise is possible, considering what we've done these past few days?"""
    
    hide minazoomshadow
    hide minazoomregret
    hide minazoomdark
    with Dissolve(0.2)
    
    
    hide underlayc
    show underlayb onlayer under
    with Dissolve(0.5)
    
    
    hide minazoomshadow
    hide minazoomregret
    hide minazoomdark
    with Dissolve(0.2)
    
    show minastandingshadow onlayer chardrop00
    show minastandingpain onlayer chardrop1
    show minastandingdark onlayer chardrop3
    hide flowersfx
    with Dissolve(0.2)
    
    
    MSU """I feel like maybe we're more deserving of hell."""

    ### START OVERTRANSITION START

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    show blackover onlayer imagedrop5
    show confrontation onlayer imagedrop6 
    show frame43 onlayer imagedrop7
    show blackover2 onlayer imagedrop8

    hide tranonereverse
    $ ClearChar()
    $ SoundOff(2.0)

    show tranone onlayer effects
    hide blackover2
    with Dissolve(0.2)

    play music1 "nightof.mp3" fadein 1.5 volume 0.3

    ### END OVERTRANSITION START


    show underlaystatic onlayer under:
        shake_effect(0.04, 10, 4)
    
    MNS """REX, WHAT THE FUCK?"""

    show underlaystatic onlayer under:
        shake_effect(0.04, 10, 4)
    
    RNS """Mina!"""

    show underlaystatic onlayer under:
        shake_effect(0.04, 10, 4)
    
    MNS """What do we do now?"""
    RNS """...We need to go to Section 56."""

    show underlaystatic onlayer under:
        shake_effect(0.04, 10, 4)
    
    MNS """What? No! It's too dangerous!"""
    RNS """Trust me, Mina. I know things about Section 56... It's our only choice!"""

    ### START OVERTRANSITION END
    # play fx2 "insertkick.mp3" volume 0.3
    # play music2 "endingonepartone.mp3" fadein 2.5 volume 0.5
    # shake_effect(0.04, 10, 3)
    # $ renpy.music.set_volume(1, delay=2, channel='music1')
    # show sceneonemain onlayer imagedrop1
    # scene widetoultra onlayer imagedrop4
    #    show introspectfx onlayer imagedrop6:
    #       alpha 0.8
    #    show blackover2 onlayer imagedrop5:
    #       alpha 0.5
    # scene ultratowide onlayer imagedrop4
    # show scenethreemain onlayer imagedrop2
    # with Dissolve(1.5)
    # hide scenethreechar



    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    $ ClearOverframe()
    $ SoundOff(2.0)

    play music2 "sceneoneatm2.mp3" fadein 2.5 volume 0.3

    show tranone onlayer imagedrop5
    hide tranonereverse
    with Dissolve(0.3)

    ### END OVERTRANSITION END

    pause 0.5
        
    
    show underlayc onlayer under
    with Dissolve(0.3)

    $ renpy.music.set_volume(0.2, delay=2, channel='music2')
    
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoomserious onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    play fx2 "s56lore.mp3" volume 0.2
    
    MZU """Ugh! ...What the fuck are we going to do?"""
    
    $ lumafade = 0.001
    hide minazoomserious
    show minazoomangry onlayer chardrop1
    with Dissolve(0.2)
    
    $ renpy.music.set_volume(1, delay=2, channel='music2')


    MZU """You still haven't fully explained why we had to come here, other than some vague myth about paradise!"""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomangry
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomneutral onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Relax, Mina. Let me explain."""
    
    $ lumafade = 0.001
    hide rexzoomneutral
    show rexzoomserious onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """Inside Section 56 is a paradise, a paradise made possible thanks to your father."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomserious
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomshock onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """My father? Making a paradise? That doesn't make any sense..."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomshock
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomserious onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Your father ruled the city with an iron fist; anyone who dared to question him ended up dead."""
    RZU """...Did you ever wonder why he was able to do such things—break the law and get away with it every single time?"""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomserious
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """I knew that he was doing incredibly shady things, but I tried to protect myself by staying as far away as possible."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomserious onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Well, you're about to find out the truth about your father."""
    
    $ lumafade = 0.001
    hide rexzoomserious
    show rexzoomneutral onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """The source behind your father's power, and the solution to our current predicament, is all here in Section 56."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomneutral
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomshock onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """What do you mean? Are you talking about the whole thing with your..."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomshock
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomsmug onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """You'll know what I mean soon enough."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomsmug
    hide rexzoomdark

    pause 1.0

    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    show introspectfx onlayer imagedrop6:
        alpha 0.8
    show blackover2 onlayer imagedrop5:
        alpha 0.5
    with Dissolve(1)


    MZU """(I hope to God I'm not making a mistake here.)"""
    
    $ lumafade = 0.001
    hide minazoompain
    show minazoomsad onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(I hate how I'm always so cynical about everything.)"""
    

    hide underlayc
    show blackover onlayer chardrop6:
        alpha 0.8
    with Dissolve(0.5)

    play fx2 "minachoice.mp3" volume 0.1

    menu:
        "(Why are you so cynical?)":
            pass

    
    $ lumafade = 0.1
    show underlayc onlayer under
    hide blackover
    with Dissolve(0.2)
    
    
    MZU """(Every guy I've ever trusted has always let me down...)"""
    
    hide minazoomshadow
    hide minazoomsad
    hide minazoomdark
    with Dissolve(1)
    
    
    hide underlayc
    hide introspectfx
    hide blackover2
    with Dissolve(1)

    pause 0.5

    show sceneonemain onlayer imagedrop1
    scene ultratowide onlayer imagedrop4
    with Dissolve(1)

    show underlay onlayer under
    hide sceneonechar
    with Dissolve(0.3)

    play fx2 "windgust.mp3" volume 0.4
    
    NW """As Rex and Mina continue walking, they face strong winds."""

    play fx3 "stumble.mp3" volume 0.4
    scene underlaystatic onlayer under:
        shake_effect(0.04, 10, 4)

    NW """The wind causes Rex to stumble for a moment."""
    
    
    hide underlaystatic
    show underlayb onlayer under
    with Dissolve(0.3)
    
    $ renpy.music.set_volume(0.1, delay=2, channel='music2')
    
    $ lumafade = 0.1 
    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show minafaceshock onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)

    
    play fx1 "romance.mp3" volume 0.15

    scene underlaybstatic onlayer under:
        shake_effect(0.04, 10, 4)
    
    MFW """Rex! You okay?"""

    $ renpy.music.set_volume(1, delay=2, channel='music2')
    
    $ lumafade = 0.1
    hide minafaceshock
    hide minafacedark
    show rexfacepain onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """...Yeah."""
    
    hide facebackground
    hide facedark
    hide rexfacepain
    hide rexfacedark
    with Dissolve(0.2)
    
    
    hide underlaybstatic
    show underlay onlayer under
    with Dissolve(0.3)
    
    NW """Mina helps Rex stand up again."""
    
    
    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1 
    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show rexfacesad onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """I wouldn't be able to go through with this without you, Mina."""
    
    $ lumafade = 0.1
    hide rexfacesad
    hide rexfacedark
    show minafacelove onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """Neither would I."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music2')
    
    $ lumafade = 0.1
    hide minafacelove
    hide minafacedark
    show rexfaceregret onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    play fx1 "gottabelieve.mp3" volume 0.05

    
    RFW """Listen, Mina. The journey ahead isn't going to be easy."""

    $ renpy.music.set_volume(1, delay=2, channel='music2')

    RFU """We're going to face a lot of situations where we'll have to help each other."""
    
    $ lumafade = 0.001
    hide rexfaceregret
    show rexfacepain onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFU """We just have to trust each other, and we'll be fine."""
    
    $ lumafade = 0.1
    hide rexfacepain
    hide rexfacedark
    show minafaceregret onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFU """Obviously. But why even mention that? Don't you trust me?"""
    
    $ lumafade = 0.1
    hide minafaceregret
    hide minafacedark
    show rexfaceserious onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFU """I do; it's just that I can't go back after this. I can't go back home."""
    
    $ lumafade = 0.001
    hide rexfaceserious
    show rexfacepain onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFU """I'll be killed on sight if somebody ever catches me back there..."""
    
    $ renpy.music.set_volume(0.1, delay=2, channel='music2')

    $ lumafade = 0.1
    hide rexfacepain
    hide rexfacedark
    show minafaceangry onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)

    play fx2 "minashooting.mp3" volume 0.15

    scene underlaybstatic onlayer under:
        shake_effect(0.04, 10, 4)


    $ renpy.music.set_volume(1, delay=2, channel='music2')

    MFU """I KNOW! It's my fault we're in this... I know."""
    
    $ lumafade = 0.001
    hide minafaceangry
    show minafacepain onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFU """It was because I had to save you... I'm so sorry, Rex."""
    
    $ lumafade = 0.1
    hide minafacepain
    hide minafacedark
    show rexfacepain onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFU """Don't apologize, Mina; you did what you did for me—you did it for us."""
    
    $ lumafade = 0.001
    hide rexfacepain
    show rexfacehappy onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFU """All I want you to do now is believe—believe that if we make it through this, we'll reach a better place."""
    
    hide facebackground
    hide facedark
    hide rexfacehappy
    hide rexfacedark
    with Dissolve(0.2)
    $ lumafade = 0.1
    show minastandingshadow onlayer chardrop00
    show minastandingneutral onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSU """...Okay."""
    
    hide minastandingshadow
    hide minastandingneutral
    hide minastandingdark
    with Dissolve(0.2)
    
    
    hide underlaybstatic
    show underlayc onlayer under
    with Dissolve(0.3)
    
    RNU """Alright, let's start moving. You see those train tracks in the distance?"""
    RNU """I think the tracks will lead us to where we need to be."""

    hide underlayc
    show underlay onlayer under
    with Dissolve(0.3)

    play fx1 "footsteps.ogg" volume 0.15
    
    NW """Mina and Rex move closer to the train tracks."""


    $ transhift = 0.167
    show tranonereverse onlayer effects
    pause 1.0

    $ SoundOff(2.0)
    $ ClearLayers()

    pause 1.0

    show frame169 onlayer imagedrop4
    show blackover onlayer imagedrop5
    show sceneonerailmain onlayer imagedrop1

    scene tranone onlayer imagedrop5
    scene frame169 onlayer imagedrop4
    with Dissolve(0.5)

    play music1 "sceneoneatm3.mp3" fadein 1.5 volume 0.4

    pause 1.5

    hide nulll
    show underlay onlayer under
    with Dissolve(0.3)

    python:
        achievement.grant("a1")
        achievement.sync()

    
    NW """They find a set of barren train tracks."""

    hide underlay
    scene widetoultra onlayer imagedrop4
    with Dissolve(0.5)

    show sceneonerailchar onlayer imagedrop2
    with Dissolve(3.0)

    pause 0.5

    scene blackover onlayer imagedrop1

    pause 1.5

    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show minastandingshadow onlayer chardrop00
    show minastandingneutral onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSU """Train tracks? Why do they look kind of weird?"""
    
    hide minastandingshadow
    hide minastandingneutral
    hide minastandingdark
    with Dissolve(0.2)
    
    $ renpy.music.set_volume(0.2, delay=2, channel='music1')
    
    hide underlayb
    show underlayc onlayer under
    with Dissolve(0.3)

    play fx2 "dumping.mp3" volume 0.15
    
    NU """Mina walks up to the tracks, inspecting them."""
    
    
    
    hide underlayc
    show underlayb onlayer under
    with Dissolve(0.3)

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    
    $ lumafade = 0.1
    show minastandingshadow onlayer chardrop00
    show minastandingneutral onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)

    show burnfx onlayer imagedrop5:
        alpha 0.2
    
    
    MSU """Why are there these weird burn marks on the sides?"""
    
    $ lumafade = 0.1
    hide minastandingshadow
    hide minastandingneutral
    hide minastandingdark
    show rexstandingshadow onlayer chardrop00
    show rexstandingserious onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    
    with Dissolve(0.2)
    
    
    RSU """It's because your father set them up to transport forbidden goods."""
    
    $ lumafade = 0.001
    hide rexstandingserious
    show rexstandingpain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RSU """...I read about it in the investigation files."""
    
    $ lumafade = 0.1
    hide rexstandingshadow
    hide rexstandingpain
    hide rexstandingdark
    show minastandingshadow onlayer chardrop00
    show minastandingshock onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSU """So you did read the files—the ones prepared by your father and..."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide minastandingshadow
    hide minastandingshock
    hide minastandingdark
    show rexstandingshadow onlayer chardrop00
    show rexstandingpain onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    hide burnfx
    with Dissolve(0.5)
    
    RSU """Yes, and yes..."""

    show flowersfx onlayer imagedrop5:
        alpha 0.3
    with Dissolve(0.5)

    play fx1 "redflowers.mp3" volume 0.15

    RSU """Have you heard about the red flowers that only bloom in Section 56?"""
    
    $ lumafade = 0.1
    hide rexstandingshadow
    hide rexstandingpain
    hide rexstandingdark
    show minastandingshadow onlayer chardrop00
    show minastandingserious onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    
    MSU """No?"""
    
    $ lumafade = 0.1
    hide minastandingshadow
    hide minastandingserious
    hide minastandingdark
    show rexstandingshadow onlayer chardrop00
    show rexstandingpain onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSU """It was the red flowers found deep in Section 56 that were the source of your father's money and power."""
    
    $ lumafade = 0.1
    hide rexstandingshadow
    hide rexstandingpain
    hide rexstandingdark
    show minastandingshadow onlayer chardrop00
    show minastandingserious onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSU """Are they used to make illegal substances? Weapons?"""
    
    $ lumafade = 0.1
    hide minastandingshadow
    hide minastandingserious
    hide minastandingdark
    show rexstandingshadow onlayer chardrop00
    show rexstandinglove onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSU """You'll find out when we get there—it's hard to explain."""
    
    $ lumafade = 0.1
    hide rexstandingshadow
    hide rexstandinglove
    hide rexstandingdark
    show minastandingshadow onlayer chardrop00
    show minastandingserious onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSU """I feel like it would be easier if you just explained everything to me up front..."""
    
    $ lumafade = 0.1
    hide minastandingshadow
    hide minastandingserious
    hide minastandingdark
    show rexstandingshadow onlayer chardrop00
    show rexstandingpain onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSU """I don't need to remind you how I got my hands on the investigation files, right?"""
    
    $ lumafade = 0.1
    hide rexstandingshadow
    hide rexstandingpain
    hide rexstandingdark
    show minastandingshadow onlayer chardrop00
    show minastandingpain onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSU """...Okay, okay. I get it."""
    
    $ lumafade = 0.1
    hide minastandingshadow
    hide minastandingpain
    hide minastandingdark
    show rexstandingshadow onlayer chardrop00
    show rexstandingserious onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSU """Just trust me."""
    
    hide rexstandingshadow
    hide rexstandingserious
    hide flowersfx
    hide rexstandingdark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlayc onlayer under
    with Dissolve(0.3)
    
    
    hide rexstandingshadow
    hide rexstandingserious
    hide rexstandingdark
    with Dissolve(0.2)

    $ lumafade = 0.1
    show rexzoomshadow onlayer chardrop00
    show rexzoompain onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    show introspectfx onlayer imagedrop6:
        alpha 0.8
    show blackover2 onlayer imagedrop5:
        alpha 0.5
    with Dissolve(0.4)
    
    
    RZU """(I really hope this works.)"""
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomsad onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(Mina wouldn't abandon me... But what if she does?)"""

    play fx3 "rexchoice.mp3" volume 0.1

    hide underlayc
    show blackover onlayer chardrop6:
        alpha 0.8
    with Dissolve(0.5)
    
    menu:
        "(Why do you think she'll abandon you?)":
            pass


    # Move it over here for the menu 
    # You need to do this so we don't double up on the characters later       
    hide rexzoomshadow
    hide rexzoomsad
    hide blackover
    hide rexzoomdark
    show underlayc onlayer under
    with Dissolve(0.2)

    
    $ lumafade = 0.1
    show rexzoomshadow onlayer chardrop00
    show rexzoompain onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """(It's not like I haven't been suddenly abandoned before...)"""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    hide rexzoomshadow
    hide blackover2
    hide introspectfx
    hide rexzoompain
    hide rexzoomdark
    with Dissolve(0.2)

    play fx3 "tension.mp3" volume 0.1
    
    NU """Rex notices that Mina is trailing him, leaving a large gap between them."""
    
    $ lumafade = 0.1
    show rexzoomshadow onlayer chardrop00
    show rexzoomangry onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    RZU """...Why are you walking so slowly?"""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomangry
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """I don't know. This whole place just makes me paranoid."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoompain onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """You were clinging to me when we first got here..."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomangry onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """I'm confused, I'm stressed. Just let me be, okay?"""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomangry
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomregret onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Alright, alright... I'm sorry."""

    ### START OVERTRANSITION START

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    show blackover onlayer imagedrop5
    show distortsketch onlayer imagedrop6 
    show frame43 onlayer imagedrop7
    show blackover2 onlayer imagedrop8

    hide tranonereverse
    $ ClearChar()
    $ SoundOff(2.0)

    show tranone onlayer effects
    hide blackover2
    with Dissolve(0.2)

    play music1 "nightof.mp3" fadein 1.5 volume 0.3

    ### END OVERTRANSITION START

    hide underlay
    show underlay onlayer under
    with Dissolve(0.3)

    RNS """Mina, stop calling me desperate; I've just been through a lot..."""
    MNS """Rex, have you read my voicemails? Why do you keep ignoring me?"""

    show distortsketchtwo onlayer imagedrop6 
    hide distortsketch

    show underlaystatic onlayer under:
        shake_effect(0.04, 10, 4)

    NS """Mina! Why would you betray your father?"""

    show underlaystatic onlayer under:
        shake_effect(0.04, 10, 4)

    NS """Rex! You underestimate how fragile your mother is!"""

    ### START OVERTRANSITION END

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    $ ClearOverframe()
    $ SoundOff(2.0)

    play music1 "sceneoneatm2.mp3" fadein 2.5 volume 0.3

    show tranone onlayer imagedrop5
    hide tranonereverse
    with Dissolve(0.3)

    ### END OVERTRANSITION END

    show sceneonerailmain onlayer imagedrop1
    scene ultratowide onlayer imagedrop4
    with Dissolve(0.5)

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')

    hide nulll
    show underlay onlayer under
    hide sceneonerailchar
    with Dissolve(0.3)

    play fx2 "sharedtrauma.mp3" volume 0.1
    play fx3 "grabhand.mp3" volume 0.6

    NW """Mina catches up to Rex and grabs his hands."""
    
    
    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1 
    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show rexfaceshock onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    RFW """...Mina?"""
    
    $ lumafade = 0.1
    hide rexfaceshock
    hide rexfacedark
    show minafaceserious onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """What?"""
    
    $ lumafade = 0.1
    hide minafaceserious
    hide minafacedark
    show rexfacehappy onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """N-Nothing."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    hide facebackground
    hide facedark
    hide rexfacehappy
    hide rexfacedark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)

    play fx2 "radiation.mp3" volume 0.2

    show dizzyfx onlayer imagedrop5:
        alpha 0.3
    with Dissolve(0.2)
    
    NW """After walking for about twenty minutes, Rex and Mina start to feel dizzy."""
    
    
    hide underlay
    show underlaybstatic onlayer under:
        shake_effect(0.04, 10, 4)
    with Dissolve(0.3)
    
    $ renpy.music.set_volume(1, delay=2, channel='music1')


    $ lumafade = 0.1 
    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show rexfacepain onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """...It's like these tracks are never-ending."""
    
    $ lumafade = 0.001
    hide rexfacepain
    show rexfaceregret onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """(I can't see properly...)"""
    
    $ lumafade = 0.001
    hide rexfaceregret
    show rexfacepain onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """Mina, you okay?"""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide rexfacepain
    hide rexfacedark
    show minafacepain onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)

    play fx1 "motherinmina.mp3" volume 0.2
    
    
    MFW """Y-Yeah, don't worry about me."""
    
    $ lumafade = 0.1
    hide minafacepain
    hide minafacedark
    show rexfaceangry onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    RFW """(I can tell she's lying; it's obvious she's dizzy too.)"""
    
    $ lumafade = 0.001
    hide rexfaceangry
    show rexfaceregret onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """(She should know she can be honest with me... vulnerable with me.)"""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide rexfaceregret
    hide rexfacedark
    show minafaceshock onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    play fx1 "fatherinrex.mp3" volume 0.2
    
    MFW """You look terrible, though. You sure you don't want to take a break?"""
    
    $ lumafade = 0.1
    hide minafaceshock
    hide minafacedark
    show rexfacelove onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    RFW """Nothing I can't handle; worry about yourself."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide rexfacelove
    hide rexfacedark
    show blackover2 onlayer imagedrop5:
        alpha 0.5
    show minafacepain onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)

    play fx2 "minafatherhelp.mp3" volume 0.1
    
    MFW """(Liar...)"""


    $ renpy.music.set_volume(1, delay=2, channel='music1')

    MFW """(...The dizziness is getting worse, though.)"""
    
    $ lumafade = 0.001
    hide minafacepain
    show minafacesad onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """(Maybe this is what I deserve, considering what I've done.)"""
    
    hide facebackground
    hide blackover2
    hide facedark
    hide minafacesad
    hide minafacedark
    with Dissolve(0.2)
    
    
    hide underlaybstatic
    show underlay onlayer under
    with Dissolve(0.3)
    
    NW """As Rex and Mina continue to follow the tracks in silence, the gap between them gradually increases."""
    
    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1 
    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show rexfaceregret onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    show blackover2 onlayer imagedrop5:
        alpha 0.5
    with Dissolve(0.2)
    
    play fx2 "rexguiltdad.mp3" volume 0.1
    
    RFW """(The dizziness keeps coming and going; when will it stop?)"""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide rexfaceregret
    show rexfacepain onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """(I really hope this works; my father's investigative work shouldn't fail me.)"""
    
    $ lumafade = 0.001
    hide rexfacepain
    show rexfaceshock onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """(But what if it does? As if it's some sort of revenge from beyond the grave.)"""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')

    hide blackover2
    show underlaybstatic onlayer under:
        shake_effect(0.04, 10, 4)
    with Dissolve(0.2)

    play fx2 "rexguiltmother.mp3" volume 0.2
    
    show momdeathstatic onlayer imagedrop5
    with Dissolve(0.1)

    pause 1

    hide momdeathstatic
    with Dissolve(0.3)


    RFW """FUCK!"""
    
    $ renpy.music.set_volume(1, delay=2, channel='music1')

    $ lumafade = 0.1
    hide rexfaceshock
    hide rexfacedark
    show minafaceshock onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """What? What's wrong?"""
    
    $ lumafade = 0.1
    hide minafaceshock
    hide minafacedark
    show rexfaceshock onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """I-I just want this fucking railroad to end. It's supposed to lead us to where we need to be."""
    
    $ lumafade = 0.001
    hide rexfaceshock
    show rexfaceangry onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """I didn't expect it to be this long."""
    
    $ lumafade = 0.1
    hide rexfaceangry
    hide rexfacedark
    show minafacelove onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """Relax, it's only been about an hour."""
    
    $ lumafade = 0.1
    hide minafacelove
    hide minafacedark
    show rexfaceangry onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """...I know."""
    
    $ lumafade = 0.1
    hide rexfaceangry
    hide rexfacedark
    show minafacesmug onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """Let's keep going for now; the dizziness might subside the farther we go."""
    
    $ lumafade = 0.1
    hide minafacesmug
    hide minafacedark
    show rexfaceneutral onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """That's all we can hope for."""
    
    $ lumafade = 0.001
    hide rexfaceneutral
    show rexfacesmug onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """Right now, I feel like we're two idiots who don't know what the fuck they're doing."""
    
    $ lumafade = 0.1
    hide rexfacesmug
    hide rexfacedark
    show minafacelove onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """I think we became bona fide idiots the moment we decided to enter this godforsaken area."""
    
    $ lumafade = 0.1
    hide minafacelove
    hide minafacedark
    show rexfacehappy onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """Can't argue with that."""


    hide underlaybstatic
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)
    
    hide facebackground
    hide facedark
    hide rexfacehappy
    hide rexfacedark
    hide dizzyfx
    with Dissolve(2)

    play fx2 "footsteps.ogg" volume 0.1
    
    NW """Rex and Mina continue to follow the train tracks..."""


##########
#####
###
#
#
# SCENE TWO
#
#
##
###
#####
##########


    $ transhift = 0.167
    show tranonereverse onlayer effects
    pause 1.0

    $ SoundOff(2.0)
    $ ClearLayers()

    pause 1.0

    show frame169 onlayer imagedrop4
    show blackover onlayer imagedrop5
    show scenetwoundermain onlayer imagedrop1

    NW """SECTION 56: ABANDONED UNDERPASS"""

    scene tranone onlayer imagedrop5
    scene frame169 onlayer imagedrop4
    with Dissolve(0.5)

    play music1 "scenetwoatm.mp3" fadein 1.5 volume 0.4

    pause 1.5

    python:
        achievement.grant("a2")
        achievement.sync()


    show underlay onlayer under
    with Dissolve(0.3)
    NW """Rex and Mina follow the train tracks for what feels like hours."""
    NW """Eventually, the train tracks go through a small underpass before finally reaching a dead end."""


    $ backdropvar = 0.13

    hide underlay
    with Dissolve(0.2)

    scene widetoultra onlayer imagedrop4

    show scenetwounderchar onlayer imagedrop2
    with Dissolve(3.5)

    pause 0.5

    show underlayb onlayer under
    with Dissolve(0.3)
    
    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    show rexstandingshadow onlayer chardrop00
    show rexstandingshock onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    play fx1 "s56now.mp3" volume 0.1
    
    RSU """Everything's so unkempt and overgrown."""
    
    $ lumafade = 0.001
    hide rexstandingshock
    show rexstandingserious onlayer chardrop1
    with Dissolve(0.2)

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    
    RSU """I wouldn't be surprised if this entire structure collapsed within a few months."""
    
    $ lumafade = 0.1
    hide rexstandingshadow
    hide rexstandingserious
    hide rexstandingdark
    show minastandingshadow onlayer chardrop00
    show minastandingserious onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSU """And all of this has to do with my father's organization? Did he build all of this?"""
    
    $ lumafade = 0.1
    hide minastandingshadow
    hide minastandingserious
    hide minastandingdark
    show rexstandingshadow onlayer chardrop00
    show rexstandingcontent onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSU """Kind of. It was an important component of Section 56's logistics."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide rexstandingshadow
    hide rexstandingcontent
    hide rexstandingdark
    show minastandingshadow onlayer chardrop00
    show minastandingshock onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    

    play fx3 "redflowers.mp3" volume 0.2

    MSU """Transporting the red flowers you mentioned earlier?"""
    
    $ lumafade = 0.1
    hide minastandingshadow
    hide minastandingshock
    hide minastandingdark
    show rexstandingshadow onlayer chardrop00
    show rexstandingneutral onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    RSU """That's right. He needed huge quantities moved back and forth from the city."""
    
    hide rexstandingshadow
    hide rexstandingneutral
    hide rexstandingdark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlayc onlayer under
    with Dissolve(0.3)
    
    play fx1 "pullsoil.mp3" volume 0.5

    NU """Rex kneels and inspects some of the overgrown roots spreading throughout the underpass."""
    
    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    
    hide underlayc
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show rexstandingshadow onlayer chardrop00
    show rexstandinghappy onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)

    play fx1 "dumping.mp3" volume 0.2

    show treeroot onlayer imagedrop5
    with Dissolve(0.2)

    
    RSU """Look at how weird and unnatural these roots look. It's exactly what my father predicted."""
    
    $ lumafade = 0.1
    hide rexstandingshadow
    hide rexstandinghappy
    hide rexstandingdark
    show minastandingshadow onlayer chardrop00
    show minastandingsad onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    
    MSU """...I see."""
    
    $ lumafade = 0.1
    hide minastandingshadow
    hide minastandingsad
    hide minastandingdark
    hide treeroot
    show rexstandingshadow onlayer chardrop00
    show rexstandinglove onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSU """But never mind that, Mina. Doesn't this remind you of our spot?"""
    
    $ lumafade = 0.001
    hide rexstandinglove
    show rexstandinghappy onlayer chardrop1
    with Dissolve(0.2)
    
    
    RSU """...When we used to sneak out of the club."""
    
    $ lumafade = 0.001
    hide rexstandinghappy
    show rexstandingshock onlayer chardrop1
    with Dissolve(0.2)
    
    
    RSU """Mina?"""
    
    hide rexstandingshadow
    hide rexstandingshock
    hide rexstandingdark
    with Dissolve(0.2)
    
    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    hide underlayb
    show underlayc onlayer under
    with Dissolve(0.3)

    play fx1 "tension.mp3" volume 0.2
    
    NU """Rex looks back to find Mina on the other side of the underpass."""

    $ renpy.music.set_volume(1, delay=2, channel='music1')


    NU """She grabs her wrist as if she's trying to hide something."""
    
    $ lumafade = 0.1
    show rexzoomshadow onlayer chardrop00
    show rexzoomangry onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """What are you doing?!"""
    
    $ lumafade = 0.001
    hide rexzoomangry
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """You make me worry I'll turn around and you won't be there anymore."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomregret onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """...Don't be silly."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomregret
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomangry onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)

    play fx1 "radiation.mp3" volume 0.2

    show sicknessfx onlayer imagedrop5:
        alpha 0.5
    with Dissolve(0.5)
    
    
    RZU """Why are you covering your wrist?"""

    $ renpy.music.set_volume(1, delay=2, channel='music1')

    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomangry
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """It's nothing. Don't worry about it and keep walking."""
    
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    with Dissolve(0.2)

    show rexstare onlayer imagedrop6    
    with Dissolve(0.2)
    
    NU """Rex stops in his tracks."""
    NU """He stares at Mina."""
    
    $ lumafade = 0.1
    show rexzoomshadow onlayer chardrop00
    show rexzoomangry onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    hide rexstare
    with Dissolve(0.2)
    
    
    RZU """Mina, show me your wrist."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomangry
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomsad onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """...It's really not that serious."""
    
    hide minazoomshadow
    hide minazoomsad
    hide minazoomdark
    with Dissolve(0.2)

    show minarash onlayer imagedrop6
    with Dissolve(0.2)

    play fx2 "unsheath.mp3" volume 0.5
    
    NU """Mina slowly moves her hand, revealing a large rash on her wrist."""
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    hide minarash
    with Dissolve(0.2)
    
    
    MZU """Are you surprised?"""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomregret onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """I see..."""
    
    $ lumafade = 0.001
    hide rexzoomregret
    show rexzoomcontent onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """It's just like when we first started going out."""

    ### START OVERTRANSITION START

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    show blackover onlayer imagedrop5
    show minarexstart onlayer imagedrop6 
    show frame43 onlayer imagedrop7
    show blackover2 onlayer imagedrop8

    hide tranonereverse
    $ ClearChar()
    $ SoundOff(2.0)

    show tranone onlayer effects
    hide blackover2
    with Dissolve(0.2)

    play music1 "underpassromance.mp3" fadein 1.5 volume 0.3

    ### END OVERTRANSITION START

    pause 1.0

    show underlay onlayer under
    with Dissolve(0.5)

    RNS """You were so scared your dad was going to find out."""
    RNS """You were so scared you always broke out into a rash every time we met up."""
    MNS """You'd probably get rashes too if you'd seen the things I've seen... I know what my father is capable of."""
    RNS """...I don't doubt it."""
    RNS """But after a few months, you stopped getting rashes when you were with me."""
    MNS """Yeah, that's because I was finally getting comfortable with you."""
    RNS """Took you a while."""
    MNS """You're a hard person to get comfortable around, you know?"""

    ### START OVERTRANSITION END

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    $ ClearOverframe()
    $ SoundOff(2.0)

    play music1 "sceneoneatm2.mp3" fadein 2.5 volume 0.3

    show tranone onlayer imagedrop5
    hide tranonereverse
    with Dissolve(0.3)

    ### END OVERTRANSITION END

    show underlayc onlayer under
    with Dissolve(0.3)
    
    $ lumafade = 0.1
    show rexzoomshadow onlayer chardrop00
    show rexzoomsad onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """...But why is it happening again?"""

    $ renpy.music.set_volume(0.1, delay=2, channel='music2')
    
    $ lumafade = 0.001
    hide rexzoomsad
    show rexzoomserious onlayer chardrop1
    with Dissolve(0.2)
    
    play fx1 "rexchoice.mp3" volume 0.1
    
    RZU """In fact, your rash looks worse and different from the ones you used to get with me."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music2')
    
    $ lumafade = 0.001
    hide rexzoomserious
    show rexzoomsad onlayer chardrop1
    show introspectfx onlayer imagedrop6:
        alpha 0.8
    show blackover2 onlayer imagedrop5:
        alpha 0.5
    with Dissolve(0.2)
    
    
    RZU """(This is bad. This is really bad.)"""
    
    $ lumafade = 0.001
    hide rexzoomsad
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(She might abandon me now. This might be too much for her to handle.)"""

    hide underlayc
    show blackover onlayer chardrop6:
        alpha 0.8
    with Dissolve(0.5)

    menu:
        "(Stop overreacting. Mina being uncomfortable doesn't mean she'll abandon you.)":
            play fx1 "trustchoice.mp3" volume 0.5
            $ trustmina = trustmina + 1
            pass
        "(It's definitely concerning. Just pray that she continues on this journey with you.)":
            play fx2 "notrustchoice.mp3" volume 0.5
            $ notrustmina = notrustmina + 1
            pass


    # Move it over here for the menu 
    # You need to do this so we don't double up on the characters later       
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    hide blackover2
    hide introspectfx
    with Dissolve(1.5)

    $ renpy.music.set_volume(0.1, delay=2, channel='music2')
    
    $ lumafade = 0.1
    show rexzoomshadow onlayer chardrop00
    hide blackover
    show underlayc onlayer under 
    show rexzoomsad onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    play fx3 "gottabelieve.mp3" volume 0.2


    RZU """M-Mina, stay strong. I know it looks bad, but..."""

    $ renpy.music.set_volume(1, delay=2, channel='music2')
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomsad
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomshock onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """I told you I'm fine. You're kind of creeping me out."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomshock
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomcontent onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Sorry, I just wanted to remind you to keep your hopes up."""
    RZU """This whole ordeal won't be for nothing. I'll make sure of it."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomcontent
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomneutral onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """I know, I know. You don't need to remind me."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music2')
    
    hide minazoomshadow
    hide minazoomneutral
    hide minazoomdark
    with Dissolve(0.2)

    show creamtube onlayer imagedrop6
    with Dissolve(0.2)

    play fx2 "romance.mp3" volume 0.2
    
    NU """Rex pulls out a small tube of hand cream from his pocket."""

    $ renpy.music.set_volume(1, delay=2, channel='music2')
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoomshock onlayer chardrop1
    show minazoomdark onlayer chardrop3
    hide creamtube
    with Dissolve(0.2)
    
    
    MZU """You brought that with you? That's my favourite brand too..."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomshock
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomhappy onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Well, you're prone to rashes, so I thought I'd bring this with me just in case."""
    
    hide rexzoomshadow
    hide rexzoomhappy
    hide rexzoomdark
    with Dissolve(0.2)

    play fx2 "applycream.mp3" volume 0.5
    
    show healedfx onlayer effects
    
    NU """Rex applies the cream to Mina's rash."""
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoomcontent onlayer chardrop1
    show minazoomdark onlayer chardrop3
    hide healedfx
    with Dissolve(0.2)


    MZU """It kind of feels better now... Thanks."""
    
    hide minazoomshadow
    hide minazoomcontent
    hide minazoomdark
    with Dissolve(0.2)

    hide underlayc

    show minadadeye onlayer imagedrop6:
        alpha 0.5

    $ renpy.music.set_volume(0.1, delay=2, channel='music2')

    pause 1.5

    hide minadadeye
    show underlayc onlayer under 
    with Dissolve(0.5)

    play fx2 "fatherinrex.mp3" volume 0.3
    
    ANU """You know I'll always protect my little princess. I'll make all your worries and pain go away."""
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)

    $ renpy.music.set_volume(1, delay=2, channel='music2')

    show underlaycstatic onlayer under:
        shake_effect(0.06, 10, 6)
    
    
    MZU """God damn it!"""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomshock onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """What? Is it hurting again?"""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomshock
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomserious onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """No, it's not that. It's not you, it's just..."""
    
    $ lumafade = 0.001
    hide minazoomserious
    show minazoomangry onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """Need I remind you of what we've done in the past 24 hours?"""

    ### START OVERTRANSITION START

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    show blackover onlayer imagedrop5
    show confrontationtwo onlayer imagedrop6 
    show frame43 onlayer imagedrop7
    hide underlaycstatic
    show blackover2 onlayer imagedrop8

    hide tranonereverse
    $ ClearChar()
    $ SoundOff(2.0)

    show tranone onlayer effects
    hide blackover2
    with Dissolve(0.2)

    play music1 "nightof.mp3" fadein 1.5 volume 0.3

    show underlaystatic onlayer under:
        shake_effect(0.06, 10, 6)
    with Dissolve(0.2)


    ANW """I'll fucking kill you! Stay away, Mina!"""
    ANW """Stay the fuck away, Mina!"""
    ANW """I'll kill you!"""


    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    $ ClearOverframe()
    $ SoundOff(2.0)

    play music2 "sceneoneatm2.mp3" fadein 2.5 volume 0.3

    show tranone onlayer imagedrop5
    hide tranonereverse
    with Dissolve(0.3)


    show underlayc onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    hide nulll
    hide nulll
    show rexzoomshadow onlayer chardrop00
    show rexzoompain onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Ah, right... Fuck! I was trying not to remember..."""
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomserious onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """I just want us to get through this and move on."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music2')
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomserious
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomsad onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    play fx2 "minashooting.mp3" volume 0.1
    
    MZU """I can't believe I got us into this mess in the first place."""

    $ renpy.music.set_volume(1, delay=2, channel='music2')
    
    $ lumafade = 0.001
    hide minazoomsad
    show minazoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """I'm such an idiot!"""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomneutral onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Don't beat yourself up."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomneutral
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    show introspectfx onlayer imagedrop6:
        alpha 0.8
    show blackover2 onlayer imagedrop5:
        alpha 0.4

    with Dissolve(0.2)

    play fx2 "minachoice.mp3" volume 0.3
    
    
    MZU """(If I was stupid enough to land us in this situation, maybe this is a mistake too?)"""
    MZU """(I never make the right choices. I'm too cynical to judge things rationally.)"""
    
    hide underlayc
    show blackover onlayer chardrop6:
        alpha 0.8
    with Dissolve(0.5)

    
    menu:
        "(Things are chaotic right now, but you need to trust Rex and be positive.)":
            $ trustrex = trustrex + 1
            play fx2 "trustchoice.mp3" volume 0.4
            pass
        "(Being too cynical is warranted. Section 56 is a dangerous place.)":
            $ notrustrex = notrustrex + 1
            play fx2 "notrustchoice.mp3" volume 0.4
            pass


    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    with Dissolve(0.2)

    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show underlayc onlayer under
    hide blackover
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    play fx3 "minafatherhelp.mp3" volume 0.2
    
    MZU """(The only times I've ever tried to trust someone have backfired.)"""
    
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    with Dissolve(0.2)

    show dizzyfx onlayer effects:
        alpha 0.6
    with Dissolve(2.0)
    
    ANU """Trust me, Mina. Just tell me what you saw."""

    hide dizzyfx
    with Dissolve(2.0)
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoomserious onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """(But Rex has been the exception.)"""
    
    $ lumafade = 0.001
    hide minazoomserious
    show minazoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(Rex is the exception...)"""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    hide blackover2
    hide introspectfx
    show rexzoomshadow onlayer chardrop00
    show rexzoomneutral onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Why are you all quiet all of a sudden?"""
    
    $ lumafade = 0.001
    hide rexzoomneutral
    show rexzoomregret onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """Maybe the hand cream isn't enough. Should we bandage it?"""
    
    hide rexzoomshadow
    hide rexzoomregret
    hide rexzoomdark
    with Dissolve(0.2)

    play fx2 "swoophand.mp3" volume 0.4
    
    NU """Rex tries to grab Mina's arm."""
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoomangry onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """Don't! Just leave it alone."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomangry
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomshock onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Alright, alright. Relax."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomshock
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomserious onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """We have more important things to worry about, okay?"""
    
    $ lumafade = 0.001
    hide minazoomserious
    show minazoomangry onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """...Just leave it alone."""
    
    hide minazoomshadow
    hide minazoomangry
    hide minazoomdark
    with Dissolve(0.2)

    ### START OVERTRANSITION START

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    show blackover onlayer imagedrop5
    show rexrat onlayer imagedrop6 
    show frame43 onlayer imagedrop7
    show blackover2 onlayer imagedrop8

    hide tranonereverse
    $ ClearChar()
    $ SoundOff(2.0)

    show tranone onlayer effects
    hide blackover2
    with Dissolve(0.2)

    play fx1 "rexguiltdad.mp3" volume 0.5

    ### END OVERTRANSITION START

    show underlayc onlayer under

    
    CNU """It's nothing, Rex. Go home and leave me alone."""
    RNU """You're his friends, right?"""
    RNU """My dad needs help. He's starting again..."""

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    $ ClearOverframe()
    $ SoundOff(2.0)

    show tranone onlayer imagedrop5
    hide tranonereverse
    with Dissolve(0.3)

    play music2 "sceneoneatm2.mp3" fadein 2.5 volume 0.3

    ### END OVERTRANSITION END

    show underlayc onlayer under
    with Dissolve(0.3)
    
    $ lumafade = 0.1
    show rexzoomshadow onlayer chardrop00
    show rexzoompain onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """(One bad decision after another.)"""
    RZU """(I can't screw this up with Mina.)"""
    RZU """(Just like how I screwed up with...)"""
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomlove onlayer chardrop1
    with Dissolve(0.2)

    $ renpy.music.set_volume(0.1, delay=2, channel='music2')
    
    play fx2 "sharedtrauma.mp3" volume 0.1
    
    RZU """If only we could go back to our old underpass meeting spot... before all of this bullshit happened."""

    $ renpy.music.set_volume(1, delay=2, channel='music2')


    RZU """Wouldn't that be amazing?"""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomlove
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """It would... if only it were possible."""
    
    $ lumafade = 0.001
    hide minazoompain
    show minazoomlove onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """But the thought itself is enough to keep me going."""
    
    $ lumafade = 0.001
    hide minazoomlove
    show minazoomhappy onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """Anyway, let's stop being idiots and keep going."""
    
    hide minazoomshadow
    hide minazoomhappy
    hide minazoomdark
    with Dissolve(0.2)
    
    
    hide underlayc
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    hide minazoomshadow
    hide minazoomhappy
    hide minazoomdark
    with Dissolve(0.2)
    $ lumafade = 0.1
    show minastandingshadow onlayer chardrop00
    show minastandinghappy onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSW """Let's get away from this underpass already!"""
    
    $ lumafade = 0.1
    hide minastandingshadow
    hide minastandinghappy
    hide minastandingdark
    show rexstandingshadow onlayer chardrop00
    show rexstandinghappy onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSW """I think I can see the end in the distance!"""
    
    hide rexstandingshadow
    hide rexstandinghappy
    hide rexstandingdark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)

    play fx2 "footsteps.ogg" volume 0.1
 
    NW """Rex and Mina head toward the end of the underpass."""


##########
#####
###
#
#
# SCENE THREE
#
#
##
###
#####
##########


    $ transhift = 0.167
    show tranonereverse onlayer effects
    pause 1.0

    $ SoundOff(2.0)
    $ ClearLayers()

    pause 1.0

    show frame169 onlayer imagedrop4
    show blackover onlayer imagedrop5
    show scenethreemain onlayer imagedrop1

    NW """SECTION 56: DERELICT PLAYGROUND"""

    scene tranone onlayer imagedrop5
    scene frame169 onlayer imagedrop4
    with Dissolve(0.5)

    play music1 "scenethreeatm.mp3" fadein 1.5 volume 0.4

    pause 1.5

    show underlay onlayer under

    pause 1.5

    python:
        achievement.grant("a3")
        achievement.sync()



    NW """A few hundred meters from the underpass, Rex and Mina encounter a rusted, derelict playground."""

    hide underlay
    with Dissolve(0.5)

    scene widetoultra onlayer imagedrop4
    show scenethreechar onlayer imagedrop2:
        linear 3.0 zoom 1.1
    with Dissolve(0.5)

    pause 3.5

    hide scenethreemain

    hide nulll
    show underlayb onlayer under
    with Dissolve(0.3)
    
    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    show minastandingshadow onlayer chardrop00
    show minastandingshock onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    play fx2 "s56now.mp3" volume 0.1
    
    MSW """…A playground?"""
    
    $ lumafade = 0.1
    hide minastandingshadow
    hide minastandingshock
    hide minastandingdark
    show rexstandingshadow onlayer chardrop00
    show rexstandingpain onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    RSW """Yeah, looks like it…"""
    
    hide rexstandingshadow
    hide rexstandingpain
    hide rexstandingdark
    with Dissolve(0.2)

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')    
    
    hide underlayb
    show underlaystatic onlayer under:
        shake_effect(0.04, 10, 1)
    with Dissolve(0.3)

    show sicknessfx onlayer imagedrop5:
        alpha 0.6

    play fx1 "radiation.mp3" volume 0.3
    play fx3 "coughing.mp3" volume 0.5
    
    NW """Rex starts coughing."""
    

    hide underlay
    hide underlaystatic
    show underlayb onlayer under
    with Dissolve(0.3)
    
    $ renpy.music.set_volume(1, delay=2, channel='music1')

    
    $ lumafade = 0.1
    show minastandingshadow onlayer chardrop00
    show minastandingshock onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSW """Hey, are you okay?"""
    
    $ lumafade = 0.1
    hide minastandingshadow
    hide minastandingshock
    hide minastandingdark
    show rexstandingshadow onlayer chardrop00
    show rexstandingpain onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSW """It's just the stale air from the underpass earlier; it irritated my throat…"""
    
    $ lumafade = 0.001
    hide rexstandingpain
    show rexstandingneutral onlayer chardrop1
    hide sicknessfx
    with Dissolve(0.2)
    
    
    RSW """But don't worry. I'm already starting to feel better now that we've left that area."""
    
    hide rexstandingshadow
    hide rexstandingneutral
    hide rexstandingdark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlayc onlayer under
    with Dissolve(0.3)
    
    NU """Mina approaches one of the swings."""
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoomsad onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """I wonder how long it's been since kids played here."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    hide minazoomshadow
    hide minazoomsad
    hide minazoomdark
    with Dissolve(0.2)

    play fx1 "ninamother.mp3" volume 0.2
    play fx3 "crying.mp3" volume 0.5
    
    NU """Mina starts tearing up."""
    
    $ lumafade = 0.1
    show rexzoomshadow onlayer chardrop00
    show rexzoomshock onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)    
    
    RZU """Mina? What's the matter now?"""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomshock
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """It just… it just reminds me of my mother, that's all."""
    MZU """Whenever Dad was away, she'd take me to the local playground…"""

    $ renpy.music.set_volume(1, delay=2, channel='music1')

    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomregret onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """I see."""
    RZU """…It's a feeling I can relate to as well."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide rexzoomregret
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)

    play fx2 "motherinmina.mp3" volume 0.3

    show momdeathstatic onlayer imagedrop5
    with Dissolve(0.2)

    pause 1.0

    hide momdeathstatic
    with Dissolve(0.5)
    
    
    RZU """Ugh."""
    
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    with Dissolve(0.2)

    scene ultratowide onlayer imagedrop4
    show scenethreemain onlayer imagedrop2
    with Dissolve(1.5)


    hide scenethreechar
    
    
    hide underlayc
    show underlayb onlayer under
    with Dissolve(0.3)

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    with Dissolve(0.2)
    $ lumafade = 0.1 
    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show minafaceregret onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)

    play fx1 "minafatherhelp.mp3" volume 0.3

    show heavenlymother onlayer imagedrop5
    with Dissolve(0.5)
    
    
    MFW """I just wish my mother were still alive…"""
    
    $ lumafade = 0.001
    hide minafaceregret
    show minafacepain onlayer chardrop1 at face_wide
    with Dissolve(0.2)

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    
    MFW """None of this would've happened."""
    
    $ lumafade = 0.001
    hide minafacepain
    show minafaceangry onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """But I had to fuck everything up!"""
    
    $ lumafade = 0.001
    hide minafaceangry
    show minafacepain onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """My mother is probably ashamed of me; she'd probably want revenge against me."""
    
    $ lumafade = 0.1
    hide minafacepain
    hide minafacedark
    show rexfaceserious onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    hide heavenlymother
    with Dissolve(0.2)
    
    
    RFW """Mina, you know that's not true."""
    
    $ lumafade = 0.001
    hide rexfaceserious
    show rexfaceneutral onlayer chardrop1 at face_wide
    with Dissolve(0.2)

    show fathercloseup onlayer imagedrop5
    with Dissolve(0.5)
    
    
    RFW """You don't need to take any of the blame for the barbarity of your father; please stop beating yourself up."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide rexfaceneutral
    hide rexfacedark
    show minafaceangry onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)

    play fx2 "minashooting.mp3" volume 0.3
    
    
    MFW """How could you say that when you know I act just like my father?"""
    
    $ lumafade = 0.001
    hide minafaceangry
    show minafacepain onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    $ renpy.music.set_volume(1, delay=2, channel='music1')

    MFW """I told you to come over that night…"""
    
    $ lumafade = 0.001
    hide minafacepain
    show minafaceregret onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """You could've just run away; we could've ended everything."""
    MFW """But I forced you to come over…"""
    
    $ lumafade = 0.1
    hide minafaceregret
    hide minafacedark
    show rexfaceserious onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """Mina, you didn't force me to do anything."""
    
    $ lumafade = 0.1
    hide rexfaceserious
    hide rexfacedark
    show minafaceregret onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    hide fathercloseup
    with Dissolve(0.2)
    
    
    MFW """…Whatever you say."""
    
    hide facebackground
    hide facedark
    hide minafaceregret
    hide minafacedark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)

    play fx1 "pacing.mp3" volume 0.4
    
    NW """Mina begins to slowly pace around the playground."""
    
    
    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.1 
    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show minafaceregret onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    play fx2 "s56lore.mp3" volume 0.2

    MFW """So this abandoned playground is also thanks to my father?"""
    
    $ lumafade = 0.001
    hide minafaceregret
    show minafaceangry onlayer chardrop1 at face_wide
    with Dissolve(0.2)

    $ renpy.music.set_volume(1, delay=2, channel='music1')

    
    
    MFW """I wonder how many families he's ruined…"""
    
    $ lumafade = 0.1
    hide minafaceangry
    hide minafacedark
    show rexfaceneutral onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """You're right, your father essentially got rid of the previous residents of Section 56."""
    
    $ lumafade = 0.001
    hide rexfaceneutral
    show rexfaceserious onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """Of course, it wasn't called Section 56 back then."""
    
    hide facebackground
    hide facedark
    hide rexfaceserious
    hide rexfacedark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)

    play fx1 "pullsoil.mp3" volume 0.2

    show flowersfx onlayer imagedrop5:
        alpha 0.5
    with Dissolve(0.5)
    
    NW """Rex bends over and notices a bright red petal on the ground."""
    
    
    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1 
    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show rexfaceangry onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """…And it was all for these beautiful flowers."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide rexfaceangry
    show rexfacepain onlayer chardrop1 at face_wide
    with Dissolve(0.2)

    play fx2 "dumping.mp3" volume 0.2
    
    
    RFW """I'm pretty sure your father cleared out all the previous residents of this area."""
    
    $ lumafade = 0.001
    hide rexfacepain
    show rexfaceregret onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    RFW """All that remains are these abandoned areas…"""
    
    $ lumafade = 0.001
    hide rexfaceregret
    show rexfaceangry onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """I guess that's the price of doing business, especially when it comes to your father."""
    
    $ lumafade = 0.001
    hide rexfaceangry
    show rexfaceserious onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """Life's tough for some people."""
    
    hide facebackground
    hide facedark
    hide flowersfx
    hide rexfaceserious
    hide rexfacedark
    with Dissolve(0.2)
    
    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)

    show dizzyfx onlayer imagedrop5:
        alpha 0.6
    with Dissolve(0.5)

    pause 1.5

    play fx3 "fatherinrex.mp3" volume 0.4
    
    ANW """Life's tough, Mina. I'm just providing for my family. I'll pay whatever price if it means providing for my family."""

    hide dizzyfx
    with Dissolve(1.5)
    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.1 
    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show minafacepain onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """Life's tough, huh?"""
    
    hide facebackground
    hide facedark
    hide minafacepain
    hide minafacedark
    with Dissolve(0.2)

    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)


    $ renpy.music.set_volume(0.1, delay=2, channel='music1')

    show dizzyfx onlayer imagedrop5:
        alpha 0.6
    with Dissolve(0.5)

    pause 1.5

    play fx1 "tension.mp3" volume 0.4
    
    
    MNW """I'm going to be the death of you."""
    
    
    hide dizzyfx
    with Dissolve(1.5)

    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.1 
    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show minafacepain onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)

    show conflictfx onlayer imagedrop5:
        alpha 0.4
    with Dissolve(0.5)

        
    MFW """Sometimes, Rex… you make me feel so conflicted."""
    
    $ lumafade = 0.1
    hide minafacepain
    hide minafacedark
    show rexfaceshock onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """What? Why?"""
    
    $ lumafade = 0.1
    hide rexfaceshock
    hide rexfacedark
    show minafacesad onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """I don't really know… everything we've been through, all the lies I've been told."""
    
    $ lumafade = 0.001
    hide minafacesad
    show minafaceregret onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """It's hard not to think about what I've been told about your father…"""
    
    $ lumafade = 0.1
    hide minafaceregret
    hide minafacedark
    show rexfaceangry onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """But you know what you've been told is a lie, right?"""
    
    $ lumafade = 0.1
    hide rexfaceangry
    hide rexfacedark
    show minafacepain onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """I know—logically, I know…"""
    
    $ lumafade = 0.001
    hide minafacepain
    show minafaceregret onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """But emotionally, the scars are still there."""
    
    $ lumafade = 0.001
    hide minafaceregret
    show minafacesad onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """I just miss my mother… I'm sorry."""
    
    $ lumafade = 0.1
    hide minafacesad
    hide minafacedark
    show rexfaceregret onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """…I know."""
    
    hide facebackground
    hide facedark
    hide rexfaceregret
    hide rexfacedark
    hide conflictfx
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlayc onlayer under
    with Dissolve(0.3)

    scene widetoultra onlayer imagedrop4
    show scenethreemain onlayer imagedrop2
    with Dissolve(1.5)

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    
    hide facebackground
    hide facedark
    hide scenethreechar 
    hide rexfaceregret
    hide rexfacedark
    with Dissolve(0.2)
    $ lumafade = 0.1
    show rexzoomshadow onlayer chardrop00
    show rexzoompain onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    show introspectfx onlayer imagedrop6:
        alpha 0.8
    show blackover2 onlayer imagedrop5:
        alpha 0.5
    with Dissolve(0.2)


    play fx1 "rexguiltdad.mp3" volume 0.3
    
    RZU """(What am I even supposed to say to that?)"""
    RZU """(All of this could have been avoided.)"""
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomangry onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(I guess that's why I've been made to pay the price.)"""

    play fx1 "rexguiltmother.mp3" volume 0.3

    show momdeathstatic onlayer imagedrop5
    with Dissolve(0.2)

    pause 1.5

    hide momdeathstatic
    with Dissolve(0.5)

    
    $ lumafade = 0.001
    hide rexzoomangry
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(Ugh!)"""

    $ renpy.music.set_volume(1, delay=2, channel='music1')


    RZU """(How much more punishment can I take? Is this what I deserve?)"""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')

    play fx1 "rexchoice.mp3" volume 0.3

    RZU """(What if Mina blames me for everything?)"""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomserious onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(When she finds out the truth about what I've done.)"""
    
    $ lumafade = 0.001
    hide rexzoomserious
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(Surely she'll realize it's her father who's wrong, not me?)"""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    hide underlayc
    show blackover onlayer chardrop6:
        alpha 0.8
    with Dissolve(0.5)
    
    menu:
        "(Stop trying to take the blame for something outside of your control.)":
            $ trustmina = trustmina + 1
            play fx3 "trustchoice.mp3" volume 0.3
            pass
        "(Revealing your true self is going to push Mina away.)":
            $ notrustmina = notrustmina + 1
            play fx3 "notrustchoice.mp3" volume 0.3
            pass

    $ renpy.music.set_volume(1, delay=2, channel='music1')

    # Move it over here for the menu 
    # You need to do this so we don't double up on the characters later       
    hide rexzoomshadow
    hide rexzoompain
    hide blackover
    hide rexzoomdark
    with Dissolve(0.2)

    
    $ lumafade = 0.1
    show rexzoomshadow onlayer chardrop00
    show rexzoompain onlayer chardrop1
    show underlayc onlayer under 
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """(I just pray that Mina doesn't abandon me…)"""
    
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    with Dissolve(0.2)
    
    
    hide underlayc
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    hide introspectfx
    hide blackover2
    with Dissolve(0.2)

    scene ultratowide onlayer imagedrop4
    show scenethreemain onlayer imagedrop2
    with Dissolve(1.5)


    $ lumafade = 0.1 
    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show minafacesad onlayer chardrop1 at face_wide
    hide scenethreechar 
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """Rex… why are you so quiet?"""
    
    $ lumafade = 0.001
    hide minafacesad
    show minafaceregret onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """I'm sorry; I should've chosen my words better earlier."""
    
    $ lumafade = 0.1
    hide minafaceregret
    hide minafacedark
    show rexfaceregret onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """No, that's not the issue."""
    
    $ lumafade = 0.001
    hide rexfaceregret
    show rexfacesad onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """Maybe your feelings just mean we're not as close as I originally thought."""
    
    $ lumafade = 0.1
    hide rexfacesad
    hide rexfacedark
    show minafaceangry onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """That's not what I meant!"""
    
    $ lumafade = 0.1
    hide minafaceangry
    hide minafacedark
    show rexfaceserious onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """We've only known each other for less than a year."""
    
    $ lumafade = 0.001
    hide rexfaceserious
    show rexfacepain onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """We barely know each other…"""
    
    $ lumafade = 0.1
    hide rexfacepain
    hide rexfacedark
    show minafaceangry onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """That's not true!"""
    
    $ lumafade = 0.1
    hide minafaceangry
    hide minafacedark
    show rexfaceregret onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """…Whatever."""
    
    hide facebackground
    hide facedark
    hide rexfaceregret
    hide rexfacedark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlayc onlayer under
    with Dissolve(0.3)
    
    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    hide facebackground
    hide facedark
    hide rexfaceregret
    hide rexfacedark
    with Dissolve(0.2)

    scene widetoultra onlayer imagedrop4
    show scenethreechar onlayer imagedrop2
    with Dissolve(1.5)


    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoomregret onlayer chardrop1
    show minazoomdark onlayer chardrop3
    hide scenethreemain
    show introspectfx onlayer imagedrop6:
        alpha 0.8
    show blackover2 onlayer imagedrop5:
        alpha 0.5
    with Dissolve(0.2)
    
    play fx1 "minachoice.mp3" volume 0.4

    MZU """(What have I been saying? I should've kept my mouth shut.)"""
    
    $ lumafade = 0.001
    hide minazoomregret
    show minazoomsad onlayer chardrop1
    with Dissolve(0.2)
    
    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    MZU """(I know Rex's father wasn't responsible for my mother's murder.)"""
    MZU """(It was all my father's fault.)"""
    MZU """(Why do I always take out my frustrations on Rex?)"""
    
    $ lumafade = 0.001
    hide minazoomsad
    show minazoomregret onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(I should be thankful that he even forgave me for defacing his father's grave.)"""
    
    $ lumafade = 0.001
    hide minazoomregret
    show minazoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(He's the only good guy I've ever known…)"""
    
    $ lumafade = 0.001
    hide minazoompain
    show minazoomserious onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(And yet he's brought me here, to Section 56.)"""
    
    hide underlayc
    show blackover onlayer chardrop6:
        alpha 0.8
    with Dissolve(0.5)
    
    menu:
        "(Just because you misspoke doesn't mean you can trust Rex completely.)":
            $ notrustrex = notrustrex + 1
            play fx3 "notrustchoice.mp3" volume 0.3
            pass
        "(You were unfair towards Rex; he's proven that he's trustworthy.)":
            $ trustrex = trustrex + 1
            play fx3 "trustchoice.mp3" volume 0.3
            pass


    hide minazoomshadow
    hide blackover
    hide minazoomserious
    hide minazoomdark
    with Dissolve(0.2)

    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show underlayc onlayer under 
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """(What am I going to do…)"""
    
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    hide introspectfx
    hide blackover2
    with Dissolve(0.2)
    
    NU """Mina wipes away her tears and stands up."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoomhappy onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    play fx2 "sharedtrauma.mp3" volume 0.3
    play fx3 "standup.mp3" volume 0.5
    
    MZU """Being an orphan doesn't suck as much when you're with another orphan!"""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    hide minazoomshadow
    hide minazoomhappy
    hide minazoomdark
    with Dissolve(0.2)
    
    NU """Mina's striking words surprise Rex."""
    NU """Rex's eyes light up."""
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoomlove onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """In less than a year, you've gotten to know me better than anyone else on this planet."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomlove
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomshock onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Mina…"""
    
    $ lumafade = 0.001
    hide rexzoomshock
    show rexzoomlove onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """That's one way to put it… Two orphans together? I guess that just makes us stronger."""
    
    hide rexzoomshadow
    hide rexzoomlove
    hide rexzoomdark
    with Dissolve(0.2)
    
    
    hide underlayc
    show underlay onlayer under
    with Dissolve(0.3)

    play fx3 "hug.mp3" volume 0.5
    
    NW """Mina playfully wraps her arms around Rex."""
    
    
    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show minastandingshadow onlayer chardrop00
    show minastandinglove onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSW """Maybe things might just turn out all right, huh?"""
    
    $ lumafade = 0.1
    hide minastandingshadow
    hide minastandinglove
    hide minastandingdark
    show rexstandingshadow onlayer chardrop00
    show rexstandinghappy onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSW """So long as you stick with me, Mina, I think they just might…"""
    RSW """Anyway, let's get going. I think I can see some buildings in the distance."""
    
    hide rexstandingshadow
    hide rexstandinghappy
    hide rexstandingdark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)

    play fx1 "footsteps.ogg" volume 0.3
    
    NW """Rex and Mina walk away from the playground as they head deeper into Section 56."""



##########
#####
###
#
#
# SCENE FOUR
#
#
##
###
#####
##########




    $ transhift = 0.167
    show tranonereverse onlayer effects
    pause 1.0

    $ SoundOff(2.0)
    $ ClearLayers()

    pause 1.0

    $ backdropvar = 0.31    

    show frame169 onlayer imagedrop4
    show blackover onlayer imagedrop5
    show scenefourmain onlayer imagedrop1

    NW """SECTION 56: ABANDONED APARTMENTS"""

    scene tranone onlayer imagedrop5
    scene frame169 onlayer imagedrop4
    with Dissolve(0.5)

    play music1 "scenefouratm.mp3" fadein 1.5 volume 0.4

    pause 1.5

    show underlay onlayer under
    with Dissolve(0.3)

    python:
        achievement.grant("a4")
        achievement.sync()



    NW """A short distance away from the playground, Rex and Mina encounter some abandoned apartments."""

    hide underlay
    with Dissolve(0.5)

    scene widetoultra onlayer imagedrop4
    show scenefourchar onlayer imagedrop2:
        linear 3.0 zoom 1.1
    with Dissolve(0.5)

    pause 3.5
        
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show minastandingshadow onlayer chardrop00
    show minastandingshock onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSU """Apartments? I guess the playground makes sense now."""
    
    $ lumafade = 0.1
    hide minastandingshadow
    hide minastandingshock
    hide minastandingdark
    show rexstandingshadow onlayer chardrop00
    show rexstandingserious onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSU """Yeah, there used to be thousands of people who lived here."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide rexstandingserious
    show rexstandingangry onlayer chardrop1
    with Dissolve(0.2)
    
    play fx1 "s56lore.mp3" volume 0.3
    
    RSU """Thousands of people were forcibly removed from these residences."""
    
    $ lumafade = 0.1
    hide rexstandingshadow
    hide rexstandingangry
    hide rexstandingdark
    show minastandingshadow onlayer chardrop00
    show minastandingregret onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    
    MSU """All because of my father, right?"""
    
    $ lumafade = 0.1
    hide minastandingshadow
    hide minastandingregret
    hide minastandingdark
    show rexstandingshadow onlayer chardrop00
    show rexstandingneutral onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSU """Correct."""
    
    $ lumafade = 0.001
    hide rexstandingneutral
    show rexstandingserious onlayer chardrop1
    with Dissolve(0.2)
    
    
    RSU """He needed the entire area deserted so he could set up the harvesting of the red flowers."""
    RSU """He couldn't let anyone know about, or interrupt, what he was doing."""
    
    $ lumafade = 0.1
    hide rexstandingshadow
    hide rexstandingserious
    hide rexstandingdark
    show minastandingshadow onlayer chardrop00
    show minastandingpain onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSU """Just how much pain has my father inflicted upon this world...?"""
    
    hide minastandingshadow
    hide minastandingpain
    hide minastandingdark
    with Dissolve(0.2)
    
    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    hide underlayb
    show underlayc onlayer under
    with Dissolve(0.3)
    
    play fx2 "radiation.mp3" volume 0.2


    NU """Mina pauses mid-sentence, looking a bit concerned."""
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoomshock onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    $ renpy.music.set_volume(1, delay=2, channel='music1')

    show sicknessfx onlayer imagedrop5:
        alpha 0.5
    with Dissolve(0.5)
    
    MZU """Rex... have you noticed your mouth feeling kind of strange since the overpass?"""
    
    $ lumafade = 0.001
    hide minazoomshock
    show minazoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """I can't get rid of this... metallic taste."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomregret onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Now that you mention it, my mouth does feel kind of dry and weird."""
    
    hide rexzoomshadow
    hide rexzoomregret
    hide rexzoomdark
    with Dissolve(0.2)
    
    NU """Rex looks puzzled for a moment, then calms down."""

    $ shadowcharvar = 0.7
    
    $ lumafade = 0.1
    show rexzoomshadow onlayer chardrop00
    show rexzoomhappy onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """It's probably just stress, Mina. We've been on the run for hours now."""
    RZU """Nothing to worry about, I promise."""

    $ shadowcharvar = 0

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide sicknessfx
    hide rexzoomhappy
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    show introspectfx onlayer imagedrop6:
        alpha 0.8
    show blackover2 onlayer imagedrop5:
        alpha 0.5
    with Dissolve(0.2)
    
    play fx1 "minachoice.mp3" volume 0.2
    
    MZU """(That look he just had reminds me of my father...)"""

    $ renpy.music.set_volume(1, delay=2, channel='music1')


    MZU """(He'd always make this puzzled face whenever I asked him something uncomfortable.)"""
    
    $ lumafade = 0.001
    hide minazoompain
    show minazoomregret onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(Only to reply with some bullshit just to ease my suspicions.)"""
    
    $ lumafade = 0.001
    hide minazoomregret
    show minazoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(But is Rex trying to ease my suspicions of him?)"""
    
    $ lumafade = 0.001
    hide minazoompain
    show minazoomregret onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(Why would he think I'm suspicious of him in the first place?)"""
    
    $ lumafade = 0.001
    hide minazoomregret
    show minazoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(What if he's just trying to reassure me, and I'm being cynical as always?)"""
    
    $ lumafade = 0.001
    hide minazoompain
    show minazoomangry onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(Fuck! I hate overthinking like this.)"""
    
    hide minazoomshadow
    hide minazoomangry
    hide minazoomdark
    with Dissolve(0.2)
    
    
    hide underlayc
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    hide minazoomshadow
    hide minazoomangry
    hide minazoomdark
    hide introspectfx
    hide blackover2
    with Dissolve(0.2)
    $ lumafade = 0.1
    show rexstandingshadow onlayer chardrop00
    show rexstandingsmug onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSU """Mina, let's look inside the apartments."""
    
    $ lumafade = 0.001
    hide rexstandingsmug
    show rexstandingcontent onlayer chardrop1
    with Dissolve(0.2)
    
    
    RSU """There might be something useful inside."""
    
    hide rexstandingshadow
    hide rexstandingcontent
    hide rexstandingdark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    NW """Rex signals Mina to follow him."""

    play fx1 "stairsteps.mp3" volume 0.3

    NW """Rex and Mina quietly make their way inside one of the apartments."""


    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show minastandingshadow onlayer chardrop00
    show minastandingshock onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSU """Hey, aren't those the flowers?"""

    
    
    hide minastandingshadow
    hide minastandingshock
    hide minastandingdark
    with Dissolve(0.2)


    show vase onlayer imagedrop5
    with Dissolve(0.2)

    
    hide underlayb
    show underlayc onlayer under
    with Dissolve(0.3)
    
    NU """Mina looks at a vase on the ground next to the front door."""

    show flowersfx onlayer imagedrop6:
        alpha 0.2
    with Dissolve(0.3)

    NU """She finds a set of withered flowers."""
    
    
    
    hide underlayc
    hide vase
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show minastandingshadow onlayer chardrop00
    show minastandingneutral onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSU """Even though they're withered, they still have such a strong red hue..."""
    
    $ lumafade = 0.1
    hide minastandingshadow
    hide minastandingneutral
    hide minastandingdark
    show rexstandingshadow onlayer chardrop00
    show rexstandingsmug onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSU """They're special flowers... your father wouldn't have made such an effort to harvest them if they weren't."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    hide rexstandingshadow
    hide rexstandingsmug
    hide rexstandingdark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlayc onlayer under
    hide flowersfx
    with Dissolve(0.3)

    play fx3 "cardboard.mp3" volume 0.4
    play fx1 "dumping.mp3" volume 0.3
    
    NU """Rex begins to look through some boxes near the front entrance."""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    show rexzoomshadow onlayer chardrop00
    show rexzoomhappy onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """(Just as I thought...)"""
    RZU """(My father was right.)"""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomhappy
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomshock onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """What's that you've got there?"""

    show chainfx onlayer imagedrop5
    with Dissolve(0.3)

    MZU """What are all of these weird metal objects? They look like they belong to some industrial machine."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomshock
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomsmug onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Like most things in Section 56, these are also the work of your father, Mina."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomsmug
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomangry onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """What? There's more here than just the flowers?"""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomangry
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomcontent onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Kind of. I'm figuring things out for myself too."""
    
    $ lumafade = 0.001
    hide rexzoomcontent
    show rexzoomneutral onlayer chardrop1
    hide chainfx
    with Dissolve(0.2)
    
    
    RZU """Anyway, more on that later. There's still more stuff to explore here."""
    
    hide rexzoomshadow
    hide rexzoomneutral
    hide rexzoomdark
    with Dissolve(0.2)

    play fx1 "footsteps.ogg" volume 0.2
    
    NU """Rex walks down one of the corridors and sees the kitchen."""
    
    
    hide underlayc
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show rexstandingshadow onlayer chardrop00
    show rexstandinghappy onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSU """Mina, come over here—the kitchen has lots of stuff we could use."""
    
    hide rexstandingshadow
    hide rexstandinghappy
    hide rexstandingdark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlayc onlayer under
    with Dissolve(0.3)
    
    NU """Mina catches up to Rex and takes a glance at the kitchen."""

    play fx2 "knives.mp3" volume 0.3

    show insertstoryfive onlayer imagedrop5
    with Dissolve(0.3)


    NU """Mina sees Rex looking at some knives in the cupboard."""
    
    
    
    hide underlayc
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    hide insertstoryfive
    show minastandingshadow onlayer chardrop00
    show minastandingshock onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSU """Knives..."""
    
    $ lumafade = 0.1
    hide minastandingshadow
    hide minastandingshock
    hide minastandingdark
    show rexstandingshadow onlayer chardrop00
    show rexstandingneutral onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSU """Mina?"""
    
    $ lumafade = 0.1
    hide rexstandingshadow
    hide rexstandingneutral
    hide rexstandingdark
    show minastandingshadow onlayer chardrop00
    show minastandingangry onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSU """Ugh, it's just bringing back fucked-up memories."""
    
    ### START OVERTRANSITION START

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    show blackover onlayer imagedrop5
    show escapeplanone onlayer imagedrop6 
    show frame43 onlayer imagedrop7
    show blackover2 onlayer imagedrop8

    hide tranonereverse
    $ ClearChar()
    $ SoundOff(2.0)

    show tranone onlayer effects
    hide blackover2
    with Dissolve(0.2)

    play music1 "escapeplan.mp3" fadein 1.5 volume 0.3

    ### END OVERTRANSITION START

    show underlay onlayer under
    with Dissolve(0.5)

    
    BNS """Mina, I know you're very smart, and that makes it hard for you to believe the things I tell you."""
    BNS """Your teachers always comment on how you never stop asking questions... always trying to outsmart your peers."""
    BNS """But I need you to do something special for me. I want you to believe me and trust me for the next couple of months."""
    BNS """I'm going to be doing things that might seem odd and unusual, but I promise it's for the best for both of us."""
    BNS """So please, Mina... believe me and trust that I'm doing what's best for us."""
    BNS """Don't let your father know. Don't let your curiosity get the better of you."""

    show escapeplantwo onlayer imagedrop6 
    with Dissolve(0.3)

    BNS """I'm leaving with Mina! There's nothing you can do about it!"""

    hide escapeplaneone 

    BNS """Come any closer to me and I'll slit your throat!"""
    ANS """You think you can command me around, you whore?"""
    ANS """Who bought you this house? Who bought you your car?"""
    BNS """FUCK YOU!"""
    
    ### START OVERTRANSITION END

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    $ ClearOverframe()
    $ SoundOff(2.0)

    play music1 "scenefouratm.mp3" fadein 2.5 volume 0.3

    show tranone onlayer imagedrop5
    hide tranonereverse
    with Dissolve(0.3)

    ### END OVERTRANSITION END


    hide underlay
    show underlayc onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoomangry onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """The knives are exactly like the ones my mother used..."""
    
    $ lumafade = 0.001
    hide minazoomangry
    show minazoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """Everything she did for me... everything to protect me from my father."""
    
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    with Dissolve(0.2)

    ### START OVERTRANSITION START

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    show blackover onlayer imagedrop5
    show mafiameeting onlayer imagedrop6 
    show frame43 onlayer imagedrop7
    show blackover2 onlayer imagedrop8

    hide tranonereverse
    $ ClearChar()
    $ SoundOff(2.0)

    show tranone onlayer effects
    hide blackover2
    with Dissolve(0.2)

    play music1 "ninafather.mp3" fadein 1.5 volume 0.3

    ### END OVERTRANSITION START

    
    
    hide underlayc
    show underlay onlayer under
    with Dissolve(0.3)
    
    ANS """That's what I expect from you guys: loyalty."""
    ANS """It's us against the world."""

    hide mafiameeting
    show minadadeye onlayer imagedrop6
    with Dissolve(1.0)

    ANS """See, Mina? If you were more loyal, little princess, I'd give you the world."""
    ANS """My little princess."""
    ANS """Your mother has been acting a bit weird lately; do you know why, Mina?"""
    ANS """It's no big deal, but I know you're so smart... you're such a smart girl, Mina."""
    
    ### START OVERTRANSITION END

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    $ ClearOverframe()
    $ SoundOff(2.0)

    play music2 "scenefouratm.mp3" fadein 2.5 volume 0.3

    show tranone onlayer imagedrop5
    hide tranonereverse
    with Dissolve(0.3)

    ### END OVERTRANSITION END

    
    hide underlay
    show underlayc onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """...Asshole."""
    
    $ lumafade = 0.001
    hide minazoompain
    show minazoomangry onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """I'll never forgive my father for what he did!"""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomangry
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomserious onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    play fx1 "rexguiltdad.mp3" volume 0.3
    
    RZU """It's okay, Mina; we're done with all of that now."""


    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomserious
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomsad onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """Are we?"""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomsad
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomserious onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    show blackover2 onlayer imagedrop5:
        alpha 0.6
    with Dissolve(0.2)
    
    
    RZU """(...All the pain I've caused Mina.)"""
    
    $ lumafade = 0.001
    hide rexzoomserious
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(Maybe I wasn't the direct cause, but I still have to shoulder most of the blame.)"""
    RZU """(I hate to see her relive her pain...)"""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomshock onlayer chardrop1
    with Dissolve(0.2)
    
    play fx1 "rexguiltmother.mp3" volume 0.3
    
    RZU """(Is the pain Mina's feeling right now similar to the pain my mother felt?)"""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide rexzoomshock
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(If that's the case, I have grave concerns about my plans.)"""
    RZU """(Please don't leave me, Mina... please.)"""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomangry onlayer chardrop1
    show minazoomdark onlayer chardrop3
    hide blackover2
    with Dissolve(0.2)


    play fx2 "tension.mp3" volume 0.3
    
    MZU """Hey! Who told you to be all quiet and gloomy?"""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomangry
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomshock onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Huh? Oh, it's nothing, Mina."""
    
    $ lumafade = 0.001
    hide rexzoomshock
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """...I just feel a deep sense of sorrow whenever I see you remembering the fucked-up things that have happened to you."""
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomregret onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """After all, you're so important to me."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomregret
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomlove onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """...Rex, you don't need to feel sorry for me like that."""
    
    $ lumafade = 0.001
    hide minazoomlove
    show minazoomhappy onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """Sure, I'll feel shitty for a moment, but I always bounce back."""
    
    $ lumafade = 0.001
    hide minazoomhappy
    show minazoomsmug onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """You're the one who likes to brood and get sulky over things."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomsmug
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomhappy onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Maybe you're right."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide rexzoomhappy
    show rexzoomregret onlayer chardrop1
    show introspectfx onlayer imagedrop6:
        alpha 0.8
    show blackover2 onlayer imagedrop5:
        alpha 0.5   
    with Dissolve(0.2)

    play fx2 "motherinmina.mp3" volume 0.3
    
    
    RZU """(When she talks like that, she's a spitting image of my mother...)"""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide rexzoomregret
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(But beneath that forced positivity, maybe she's harboring something much darker.)"""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomshock onlayer chardrop1
    with Dissolve(0.2)

    play fx2 "rexchoice.mp3" volume 0.3
    
    
    RZU """(What if she's about to burst from everything she's holding on to?)"""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide rexzoomshock
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(Maybe she needs to hear the truth—the whole truth—in order to keep going.)"""
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomregret onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(But what if telling her the entire truth will just make her run away?)"""
    
    $ lumafade = 0.001
    hide rexzoomregret
    show rexzoomsad onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(Maybe if I keep going the way I have, she won't abandon me.)"""

 
    hide underlayc
    show blackover onlayer chardrop6:
        alpha 0.8
    with Dissolve(0.5)
   
    menu:
        "(Mina's not your mother; she won't abandon you.)":
            $ trustmina = trustmina + 1
            play fx3 "trustchoice.mp3" volume 0.3
            pass
        "(Mina is the kind of person who will abandon you without knowing the truth.)":
            $ notrustmina = notrustmina + 1
            play fx3 "notrustchoice.mp3" volume 0.3
            pass


    # Move it over here for the menu 
    # You need to do this so we don't double up on the characters later       
    hide rexzoomshadow
    hide rexzoomsad
    hide rexzoomdark
    hide blackover
    with Dissolve(0.2)

    
    $ lumafade = 0.1
    show rexzoomshadow onlayer chardrop00
    show underlayc onlayer under 
    show rexzoomregret onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """(...I guess I'll see what happens.)"""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide rexzoomregret
    hide introspectfx
    hide blackover2
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)

    play fx3 "sharedtrauma.mp3" volume 0.3
    
    
    RZU """Considering everything we've both been through, I wonder if I'd still be alive if it wasn't for you."""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomhappy onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """Oh, come on, don't be so dramatic."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomhappy
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomregret onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """But we're in such a messed-up situation, though."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomregret
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomsmug onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """And you're going to get us out of this situation by taking us to the end of Section 56, right?"""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomsmug
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoompain onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """R-Right..."""
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomserious onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """I need to snap out of this; we've got important things to do here."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomserious
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomserious onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """Don't be so tense about all of this."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide minazoomserious
    show minazoomsmug onlayer chardrop1
    with Dissolve(0.2)

    show lovefx onlayer imagedrop5:
        alpha 0.2
    with Dissolve(0.3)

    play fx2 "romance.mp3" volume 0.2
    
    MZU """Worst comes to worst, we can just turn this apartment into our new home."""

    $ renpy.music.set_volume(1, delay=2, channel='music1')


    MZU """...live in Section 56 forever."""
    
    hide minazoomshadow
    hide minazoomsmug
    hide minazoomdark
    with Dissolve(0.2)

    hide lovefx
    with Dissolve(0.5)
    
    NU """Rex strains a smile as he begins looking for more things in the apartment."""

    play fx1 "opendraw.mp3" volume 0.4

    NU """Mina begins opening various cupboards in the kitchen."""
    NU """...Ten minutes pass."""
    
    
    
    hide underlayc
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show minastandingshadow onlayer chardrop00
    show minastandingregret onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    play fx2 "bottles.mp3" volume 0.4
    
    MSU """...Empty bottles, dust. Nothing useful."""
    
    $ lumafade = 0.001
    hide minastandingregret
    show minastandinghappy onlayer chardrop1
    with Dissolve(0.2)
    
    
    MSU """Rex, there isn't anything useful in the kitchen."""
    
    $ lumafade = 0.001
    hide minastandinghappy
    show minastandingshock onlayer chardrop1
    with Dissolve(0.2)
    
    
    MSU """...Rex?"""
    
    hide minastandingshadow
    hide minastandingshock
    hide minastandingdark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlayc onlayer under
    with Dissolve(0.3)

    play fx3 "slowsteps.mp3" volume 0.4
    
    NU """Mina makes her way into the corridor."""
    NU """She notices Rex standing still, staring at one of the rooms."""
    
    
    
    hide underlayc
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show minastandingshadow onlayer chardrop00
    show minastandingshock onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)

    show noisedistortfx onlayer imagedrop5:
        alpha 0.5
    with Dissolve(0.2)
    
    
    MSU """Rex? Why are you standing there?"""
    
    hide minastandingshadow
    hide minastandingshock
    hide minastandingdark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlayc onlayer under
    with Dissolve(0.3)
    
    NU """Rex doesn't respond."""
    
    
    
    hide underlayc
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show minastandingshadow onlayer chardrop00
    show minastandingangry onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSU """Is there something in the room?"""
    
    hide minastandingshadow
    hide minastandingangry
    hide minastandingdark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlayc onlayer under
    with Dissolve(0.3)
    
    NU """Mina rushes up to Rex."""
    NU """She looks at the room for a moment."""
    
    
    
    hide underlayc
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show minastandingshadow onlayer chardrop00
    show minastandingshock onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSU """There's nothing here?"""
    
    hide minastandingshadow
    hide minastandingshock
    hide minastandingdark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlayc onlayer under
    with Dissolve(0.3)

    show stool onlayer imagedrop5
    with Dissolve(0.3)
    
    NU """Upon closer inspection, Mina notices a small stool in the corner of the room."""
    
    
    
    hide underlayc
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show minastandingshadow onlayer chardrop00
    show minastandingpain onlayer chardrop1
    show minastandingdark onlayer chardrop3
    hide stool 
    with Dissolve(0.2)
    
    
    MSU """Oh no..."""
    
    hide minastandingshadow
    hide minastandingpain
    hide minastandingdark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlayc onlayer under
    with Dissolve(0.3)

    show stool onlayer imagedrop5
    with Dissolve(0.3)
    
    
    NU """Rex stands silently, staring at the stool with an emotionless gaze."""

    ### START OVERTRANSITION START

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    show blackover onlayer imagedrop5
    show blackover2 onlayer imagedrop6 
    show frame43 onlayer imagedrop7
    show blackover2 onlayer imagedrop8

    hide tranonereverse
    hide stool
    $ ClearChar()
    $ SoundOff(2.0)

    show tranone onlayer effects
    hide blackover2
    with Dissolve(0.2)

    # play music1 "nightof.mp3" fadein 1.5 volume 0.3

    ### END OVERTRANSITION START

    
    hide underlayc
    show underlay onlayer under
    with Dissolve(0.3)
    
    RNS """Mom, I brought home dinner!"""

    play fx1 "twostepone.mp3" volume 0.3

    RNS """Mom?"""

    play fx2 "twostepone.mp3" volume 0.3

    RNS """...Where are you?"""

    show momdeadstool onlayer imagedrop6
    with Dissolve(0.2)

    show underlaystatic onlayer under:
        shake_effect(0.04, 10, 2)

    RNS """Mom!"""

    ### START OVERTRANSITION END

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    $ ClearOverframe()
    $ SoundOff(2.0)

    play music1 "scenefouratm.mp3" fadein 2.5 volume 0.3

    show tranone onlayer imagedrop5
    hide tranonereverse
    with Dissolve(0.3)

    show noisedistortfx onlayer imagedrop5:
        alpha 0.5
    with Dissolve(0.2)
    


    ### END OVERTRANSITION END

    
    
    
    hide underlay
    show underlayc onlayer under
    with Dissolve(0.3)
    
    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoomshock onlayer chardrop1
    show minazoomdark onlayer chardrop3
    show introspectfx onlayer imagedrop6: 
        alpha 0.8   
    show blackover2 onlayer imagedrop5:
        alpha 0.5
    with Dissolve(0.2)
    
    
    play fx1 "minashooting.mp3" volume 0.3

    MZU """(It appears the room has triggered a flashback to Rex's mother...)"""
    
    $ lumafade = 0.001
    hide minazoomshock
    show minazoomangry onlayer chardrop1
    with Dissolve(0.2)

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    
    MZU """(Fuck!)"""
    MZU """(This is only the third time I've ever seen Rex like this.)"""
    
    $ lumafade = 0.001
    hide minazoomangry
    show minazoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(He dissociates whenever something reminds him of his mother too much...)"""
    
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    with Dissolve(0.2)
    
    
    hide underlayc
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    with Dissolve(0.2)
    $ lumafade = 0.1
    show minastandingshadow onlayer chardrop00
    show minastandingsad onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSU """(Maybe if everything with my father hadn't happened, he wouldn't have to suffer like this.)"""
    
    $ lumafade = 0.001
    hide minastandingsad
    show minastandingpain onlayer chardrop1
    with Dissolve(0.2)
    
    
    MSU """(If I hadn't asked him... if I hadn't gotten him to do what he did...)"""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide minastandingpain
    show minastandingregret onlayer chardrop1
    with Dissolve(0.2)
    
    play fx3 "minafatherhelp.mp3" volume 0.3

    MSU """(But even before all of this happened...)"""
    
    $ renpy.music.set_volume(1, delay=2, channel='music1')

    $ lumafade = 0.001
    hide minastandingregret
    show minastandingsad onlayer chardrop1
    with Dissolve(0.2)
    
    
    MSU """(Why did I cave to my father?)"""
    
    $ lumafade = 0.001
    hide minastandingsad
    show minastandingpain onlayer chardrop1
    with Dissolve(0.2)
    
    
    MSU """(Why wasn't I able to just believe my mother...?)"""
    
    $ lumafade = 0.001
    hide minastandingpain
    show minastandingserious onlayer chardrop1
    with Dissolve(0.2)
    
    
    MSU """(I feel like it's all related.)"""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide minastandingserious
    show minastandingsad onlayer chardrop1
    with Dissolve(0.2)
    
    play fx3 "minachoice.mp3" volume 0.3
    
    MSU """(My inability to trust someone—to actually believe what they say...)"""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide minastandingsad
    show minastandingpain onlayer chardrop1
    with Dissolve(0.2)
    
    
    MSU """(It's the root cause of all this suffering.)"""
        
    
    hide underlayb
    show blackover onlayer chardrop6:
        alpha 0.8
    with Dissolve(0.5)

    menu:
        "(You're right; being too cynical is the cause of your troubles.)":
            $ trustrex = trustrex + 1
            play fx1 "trustchoice.mp3" volume 0.3
            pass
        "(You're wrong; your cynicism and skepticism saved you.)":
            $ notrustrex = notrustrex + 1
            play fx1 "notrustchoice.mp3" volume 0.3
            pass

    
    hide minastandingshadow
    hide minastandingpain
    hide minastandingdark
    hide blackover
    with Dissolve(0.2)

    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    show underlayc onlayer under 
    with Dissolve(0.2)
    
    
    MZU """(...I'll dwell on this later.)"""
    
    $ lumafade = 0.001
    hide minazoompain
    show minazoomserious onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(I have to help Rex out.)"""
    
    hide minazoomshadow
    hide minazoomserious
    hide minazoomdark
    hide introspectfx
    hide blackover2
    with Dissolve(0.2)

    show minastareshock onlayer imagedrop5
    with Dissolve(0.5)

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')

    play fx2 "romance.mp3" volume 0.3
    
    NU """Mina stands in front of Rex and stares into his eyes."""
    
    
    
    hide underlayc
    show underlayb onlayer under
    with Dissolve(0.3)

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    
    $ lumafade = 0.1
    show minastandingshadow onlayer chardrop00
    show minastandingshock onlayer chardrop1
    show minastandingdark onlayer chardrop3
    hide minastareshock
    with Dissolve(0.2)

    show underlaybstatic onlayer under:
        shake_effect(0.04, 10, 3)    

    play fx2 "shaking.mp3" volume 0.3
    
    MSU """Rex!"""
    
    hide minastandingshadow
    hide minastandingshock
    hide minastandingdark
    with Dissolve(0.2)
    
    
    hide underlayb
    hide underlaybstatic 
    show underlayc onlayer under
    hide noisedistortfx
    with Dissolve(0.3)

    show rexstare onlayer imagedrop5
    with Dissolve(0.5)

    
    NU """Rex's vacant eyes slowly regain life."""
    
    
    
    hide underlayc
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show rexstandingshadow onlayer chardrop00
    show rexstandingpain onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    hide rexstare
    with Dissolve(0.5)
    
    
    RSU """...Huh?"""
    RSU """What... what happened?"""
    
    hide rexstandingshadow
    hide rexstandingpain
    hide rexstandingdark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlayc onlayer under
    with Dissolve(0.3)
    
    play fx2 "grabhand.mp3" volume 0.3

    NU """Mina grabs Rex by the arm and leads him toward the back entrance of the apartment."""
    
    
    hide underlayc
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show minastandingshadow onlayer chardrop00
    show minastandingserious onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSU """We have to get going; follow me."""
    
    hide minastandingshadow
    hide minastandingserious
    hide minastandingdark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlayc onlayer under
    with Dissolve(0.3)
    
    NU """Rex begins to regain his composure."""
    
    
    
    hide underlayc
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show rexstandingshadow onlayer chardrop00
    show rexstandingpain onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSU """We need to head into the forested area over there... that's the direction we need to go..."""
    
    hide rexstandingshadow
    hide rexstandingpain
    hide rexstandingdark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)
    
    NW """Mina slowly guides Rex outside the apartment as they head toward the forested wilderness of Section 56."""


##########
#####
###
#
#
# SCENE FIVE
#
#
##
###
#####
##########


    $ transhift = 0.167
    show tranonereverse onlayer effects
    pause 1.0

    $ SoundOff(2.0)
    $ ClearLayers()

    pause 1.0

    $ backdropvar = 0.23

    show frame169 onlayer imagedrop4
    show blackover onlayer imagedrop5
    show scenefivemain onlayer imagedrop1

    NW """SECTION 56: FOREST WILDERNESS."""

    scene tranone onlayer imagedrop5
    scene frame169 onlayer imagedrop4
    with Dissolve(0.5)

    play music1 "scenefiveatm.mp3" fadein 1.5 volume 0.4

    pause 1.5

    show underlay onlayer under

    pause 1.5

    python:
        achievement.grant("a5")
        achievement.sync()


    NW """As Rex and Mina get farther from the apartments, the fog grows thicker and thicker."""
    NW """Eventually, they find themselves in the depths of a forest wilderness."""

    hide underlay
    with Dissolve(0.5)

    show widetoultra onlayer imagedrop4
    show scenefivechar onlayer imagedrop2:
        linear 3.0 zoom 1.1
    with Dissolve(0.5)

    pause 3.5

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    show underlay onlayer under
    with Dissolve(0.3)

    play fx2 "motherinmina.mp3" volume 0.3
    
    NW """Rex inches closer to Mina as they walk together through the trees."""

    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    $ renpy.music.set_volume(1, delay=2, channel='music1')

    $ lumafade = 0.1
    show rexstandingshadow onlayer chardrop00
    show rexstandingpain onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSU """…Thank you for taking care of me earlier."""
    
    $ lumafade = 0.1
    hide rexstandingshadow
    hide rexstandingpain
    hide rexstandingdark
    show minastandingshadow onlayer chardrop00
    show minastandinglove onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSU """Don't mention it."""
    
    $ lumafade = 0.001
    hide minastandinglove
    show minastandinghappy onlayer chardrop1
    with Dissolve(0.2)
    
    
    MSU """I'm here to protect you too, you know?"""
    
    $ lumafade = 0.1
    hide minastandingshadow
    hide minastandinghappy
    hide minastandingdark
    show rexstandingshadow onlayer chardrop00
    show rexstandingregret onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSU """…I know."""
    
    hide rexstandingshadow
    hide rexstandingregret
    hide rexstandingdark
    with Dissolve(0.2)

    ### START OVERTRANSITION START

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    show blackover onlayer imagedrop5
    show rexmomhome onlayer imagedrop6 
    show frame43 onlayer imagedrop7
    show blackover2 onlayer imagedrop8

    hide tranonereverse
    $ ClearChar()
    $ SoundOff(2.0)

    show tranone onlayer effects
    hide blackover2
    with Dissolve(0.2)

    play music1 "rexmother.mp3" fadein 1.5 volume 0.3

    ### END OVERTRANSITION START

    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)
    
    RNS """Mom, why haven't you made dinner?"""
    RNS """Just rest up. I'll take care of everything."""
    RNS """…Just don't leave me."""
    
    
    ### START OVERTRANSITION END

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    $ ClearOverframe()
    $ SoundOff(2.0)

    play music1 "scenefiveatm.mp3" fadein 2.5 volume 0.3

    show tranone onlayer imagedrop5
    hide tranonereverse
    with Dissolve(0.3)

    ### END OVERTRANSITION END

    hide underlay
    show underlayc onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show rexzoomshadow onlayer chardrop00
    show rexzoomsad onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """I feel like our relationship has been a distraction for me sometimes."""
    
    $ lumafade = 0.001
    hide rexzoomsad
    show rexzoomcontent onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """In a good way, not a bad way."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomcontent
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomcontent onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """It goes both ways."""
    
    hide minazoomshadow
    hide minazoomcontent
    hide minazoomdark
    with Dissolve(0.2)
    
    $ renpy.music.set_volume(0.1, delay=2, channel='music1')

    hide underlayc
    with Dissolve(0.5)

    scene ultratowide onlayer imagedrop4
    show scenefivemain onlayer imagedrop2
    with Dissolve(1.5)

    show underlay onlayer under
    hide scenefivechar
    with Dissolve(0.5)

    play fx1 "s56now.mp3" volume 0.3
    play fx2 "pullsoil.mp3" volume 0.5
    
    NW """Mina crouches for a moment to inspect some plants."""
    
    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    $ renpy.music.set_volume(1, delay=2, channel='music1')

    $ lumafade = 0.1 
    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show minafaceshock onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)

    show roottwo onlayer imagedrop5
    with Dissolve(0.5)
    
    
    MFW """I've never seen plants like these; they have such strange hues and shapes."""
    
    $ lumafade = 0.001
    hide minafaceshock
    show minafaceserious onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """I guess it's not a coincidence that my father chose Section 56 for his illegal activities."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide minafaceserious
    hide minafacedark
    show rexfacecontent onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    play fx2 "s56lore.mp3" volume 0.3

    
    RFW """Exactly. Section 56 has always been special compared with other nearby areas."""
    
    $ lumafade = 0.001
    hide rexfacecontent
    show rexfaceneutral onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    RFW """For one thing, it has wilderness and terrain that simply aren't found in the flat, grassy areas next to the city."""
    
    $ lumafade = 0.001
    hide rexfaceneutral
    show rexfaceserious onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """It's the perfect area to hide things… to develop things away from prying eyes."""
    
    $ lumafade = 0.001
    hide rexfaceserious
    hide roottwo
    show rexfaceneutral onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    show flowersfx onlayer imagedrop5:
        alpha 0.3
    with Dissolve(0.5)
    
    RFW """Once your father learned about the red flowers growing here, he had to hoard them all for himself."""
    
    $ lumafade = 0.1
    hide rexfaceneutral
    hide rexfacedark
    show minafaceangry onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """Sounds typical of him."""
    
    $ lumafade = 0.1
    hide minafaceangry
    hide minafacedark
    show rexfacecontent onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """So he essentially created a gigantic processing plant for the red flowers, which is where we're heading."""
    
    $ lumafade = 0.001
    hide rexfacecontent
    show rexfaceneutral onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """He built it right next to one of the largest fields of red flowers in all of Section 56."""
    
    $ lumafade = 0.001
    hide rexfaceneutral
    show rexfacelove onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """Once we get there, we'll be able to solve all of our problems, Mina."""
    
    $ lumafade = 0.1
    hide rexfacelove
    hide rexfacedark
    show minafaceangry onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """The red-flower processing plant? That's the key?"""
    
    $ lumafade = 0.1
    hide minafaceangry
    hide minafacedark
    show rexfacehappy onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """Exactly. When we're inside, you'll see how we can use it to our benefit."""
    
    $ lumafade = 0.1
    hide rexfacehappy
    hide rexfacedark
    show minafaceneutral onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    MFW """I see…"""
    
    hide facebackground
    hide facedark
    hide minafaceneutral
    hide minafacedark
    hide flowersfx
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)

    show redflowerclose onlayer imagedrop6
    with Dissolve(0.5)

    play fx3 "redflowers.mp3" volume 0.3
    
    NW """Mina notices some red flowers beneath one of the trees."""
    
    
    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.1 
    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show minafaceshock onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """It's the first time I've seen them growing in the wild…"""
    MFW """These are the red flowers you've been talking about, right?"""
    
    $ lumafade = 0.1
    hide minafaceshock
    hide minafacedark
    show rexfaceserious onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """That's right. It's my first time seeing them grow in the wild too…"""
    
    $ lumafade = 0.001
    hide rexfaceserious
    show rexfacecontent onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """It's a good sign; it means we're getting closer."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    hide facebackground
    hide facedark
    hide rexfacecontent
    hide rexfacedark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlay onlayer under
    show lovefx onlayer imagedrop5:
        alpha 0.2
    with Dissolve(0.3)



    play fx2 "romance.mp3" volume 0.3
    play fx3 "pullsoil.mp3" volume 0.5

    
    NW """Rex leans over and plucks a few of the red flowers."""

    $ renpy.music.set_volume(11, delay=2, channel='music1')

    NW """He tidies them up and bunches them together."""
    
    
    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1 
    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show rexfacelove onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """Here, take these."""
    
    $ lumafade = 0.1
    hide rexfacelove
    hide rexfacedark
    show minafaceshock onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """What do you mean?"""
    
    $ lumafade = 0.1
    hide minafaceshock
    hide minafacedark
    show rexfacesmug onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """What? Don't you like pretty flowers?"""
    
    $ lumafade = 0.1
    hide rexfacesmug
    hide rexfacedark
    show minafacelove onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """Now isn't the time to give me flowers, Rex…"""
    
    $ lumafade = 0.001
    hide minafacelove
    show minafacecontent onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """Maybe you can give me a box of chocolates next?"""
    
    $ lumafade = 0.1
    hide minafacecontent
    hide minafacedark
    show rexfacesmug onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.5)
    
    
    RFW """Maybe if you look close enough at the flowers, they'll turn into a box of chocolates."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    hide facebackground
    hide facedark
    hide rexfacesmug
    hide rexfacedark
    hide redflowerclose
    hide lovefx
    with Dissolve(1.5)
    
    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)

    play fx1 "dumping.mp3" volume 0.3
    
    NW """Just as Mina brings the flowers closer to her face, she notices something in the distance…"""
    
    
    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1 
    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show minafaceshock onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    MFW """Rex! What's that?"""
    
    hide facebackground
    hide facedark
    hide minafaceshock
    hide minafacedark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)
    
    play fx2 "running.mp3" volume 0.5

    NW """Mina begins running toward something sticking out of the bushes."""
    
    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1 
    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show minafaceshock onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """Is that what I think it is?"""
    
    $ lumafade = 0.001
    hide minafaceshock
    show minafacepain onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """It must be…"""
    
    hide facebackground
    hide facedark
    hide minafacepain
    hide minafacedark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)

    show slenderbone onlayer imagedrop5
    with Dissolve(1.0)
    
    NW """Rex runs up to Mina, noticing that she is looking at a large, slender bone sticking out of the bushes."""
    
    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1 
    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show minafaceangry onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """This has to be a human bone; look at it!"""
    
    $ lumafade = 0.001
    hide minafaceangry
    show minafacepain onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """It's shaped exactly like the leg bones you see in medical diagrams."""
    
    hide facebackground
    hide facedark
    hide minafacepain
    hide minafacedark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)
    
    NW """Rex turns pale for a moment but begins to take a few deep breaths."""
    NW """He regains his composure."""
    
    
    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1 
    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show rexfaceserious onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """Mina, I know it looks scary, but those aren't human bones."""
    
    $ lumafade = 0.1
    hide rexfaceserious
    hide rexfacedark
    show minafaceangry onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """What do you mean?"""
    
    $ lumafade = 0.1
    hide minafaceangry
    hide minafacedark
    show rexfacepain onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """They're animal bones, probably from a deer."""
    
    $ lumafade = 0.001
    hide rexfacepain
    show rexfaceneutral onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """They have long, skinny bones like humans, so it's easy to get them mixed up."""
    
    $ lumafade = 0.001
    hide rexfaceneutral
    show rexfacehappy onlayer chardrop1 at face_wide
    hide slenderbone 
    with Dissolve(0.2)
    
    
    RFW """Don't worry about it. Let's keep moving."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    hide facebackground
    hide facedark
    hide rexfacehappy
    hide rexfacedark
    with Dissolve(0.2)
    
    
    hide underlayb
    with Dissolve(0.5)

    scene widetoultra onlayer imagedrop4
    show scenefiveemain onlayer imagedrop2
    with Dissolve(1.5)

    show dizzyfx onlayer imagedrop5:
        alpha 0.2
    with Dissolve(1.5)

    show underlayc onlayer under
    hide scenefivemain
    with Dissolve(0.3)

    play fx3 "fatherinrex.mp3" volume 0.3
    
    ANU """Don't worry about it, Mina. Trust me."""

    $ renpy.music.set_volume(1, delay=2, channel='music1')

    ANU """Mina, your mother is fine. Trust me."""
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    show introspectfx onlayer imagedrop6:
        alpha 0.8
    show blackover2 onlayer imagedrop5:
        alpha 0.5
    with Dissolve(0.2)

    hide dizzyfx
    with Dissolve(1.5)
    
    
    MZU """(Yet again… he reminds me of my father.)"""
    
    $ lumafade = 0.001
    hide minazoompain
    show minazoomangry onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(Why am I like this?!)"""
    
    $ lumafade = 0.001
    hide minazoomangry
    show minazoomregret onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(I know that Rex is nothing like my father… but why does this keep happening?)"""
    
    $ lumafade = 0.001
    hide minazoomregret
    show minazoompain onlayer chardrop1
    with Dissolve(0.2)

    hide introspectfx
    show dizzyfx onlayer imagedrop5:
        alpha 0.4
    with Dissolve(2.0)
    
    
    MZU """(Wait, why is my vision going weird?)"""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    with Dissolve(0.2)

    play fx1 "radiation.mp3" volume 0.3
    
    NU """Mina's vision starts to distort as she slowly walks behind Rex."""
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    MZU """(What's going on?!)"""
    MZU """(If this keeps going, I'm going to go blind!)"""
    
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    with Dissolve(0.2)
    
    BNU """Mina, please, please believe me."""
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoomshock onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """(Mother!)"""
    
    $ lumafade = 0.001
    hide minazoomshock
    show minazoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(Ugh, why am I hearing my mother's voice?)"""
    MZU """(This entire area is really screwing with my mind…)"""
    
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    with Dissolve(0.2)
    
    ### START OVERTRANSITION START

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    hide blackover2

    show blackover onlayer imagedrop5
    show minadadeye onlayer imagedrop6 
    show frame43 onlayer imagedrop7
    hide dizzyfx
    show blackover2 onlayer imagedrop8

    hide tranonereverse
    $ ClearChar()
    $ SoundOff(2.0)

    show tranone onlayer effects
    hide blackover2
    with Dissolve(0.2)

    play music1 "ninafather.mp3" fadein 1.5 volume 0.3

    ### END OVERTRANSITION START
    
    hide underlayc
    show underlay onlayer under
    with Dissolve(0.3)
    
    ANS """You know I love you, right, Mina?"""
    ANS """You're my princess."""
    ANS """…I've been a little bit concerned about what your mother has been doing lately."""
    ANS """You know I only want the best for her too, right?"""
    ANS """You know, Mina, sometimes all it takes is to speak up and talk to someone when you're going through a rough time."""
    ANS """…And I'm afraid your mother isn't speaking up."""
    ANS """So if you want to help me and your mother get back on better terms, you'll tell me what's been happening, right?"""
    ANS """I only want us to be happy. I'd be nothing without you two."""
    ANS """So, will you tell me what you've been noticing? You're such a clever girl."""
    MNS """…Yes, Father."""

    ### START OVERTRANSITION END


    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    $ ClearOverframe()
    $ SoundOff(2.0)

    play music1 "scenefiveatm.mp3" fadein 2.5 volume 0.3

    show tranone onlayer imagedrop5
    hide tranonereverse
    with Dissolve(0.3)

    ### END OVERTRANSITION END

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')

    
    hide underlay
    show underlayc onlayer under
    with Dissolve(0.3)
    
    play fx1 "tension.mp3" volume 0.3

    NU """Mina's distorted vision starts to subside."""
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    MZU """Rex… You know that my hatred toward your father was because my father manipulated me, right?"""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoompain onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """…Why are you bringing this up again?"""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """It's just that… I remembered some things."""
    
    $ lumafade = 0.001
    hide minazoompain
    show minazoomsad onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """I regret many of the things I did, especially that time at your father's graveyard."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomsad
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomcontent onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """That's all in the past, Mina… You don't have to bring it up and apologize again."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomcontent
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """I know, but I also want you to know that…"""
    
    $ lumafade = 0.001
    hide minazoompain
    show minazoomsad onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """Part of the reason I hated your father so much was because I was trying to offload my own guilt."""
    
    $ lumafade = 0.001
    hide minazoomsad
    show minazoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """My own guilt regarding the role I had to play in my mother's murder."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomserious onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Mina, that wasn't your fault… your father manipulated you."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomserious
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomregret onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """That doesn't mean I didn't play a major role in her murder…"""
    
    hide minazoomshadow
    hide minazoomregret
    hide minazoomdark
    with Dissolve(0.2)
    
    ### START OVERTRANSITION START

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    show blackover onlayer imagedrop5
    show escapeplantwo onlayer imagedrop6 
    show frame43 onlayer imagedrop7
    show blackover2 onlayer imagedrop8

    hide tranonereverse
    $ ClearChar()
    $ SoundOff(2.0)

    show tranone onlayer effects
    hide blackover2
    with Dissolve(0.2)

    play music1 "escapeplan.mp3" fadein 1.5 volume 0.3

    ### END OVERTRANSITION START

    
    hide underlayc
    show underlay onlayer under
    with Dissolve(0.3)
    
    BNS """No! You've got the wrong idea; that's not what I'm doing!"""
    BNS """Please, I beg you! Please, don't… don't do it; think of Mina."""

    show fathercloseup onlayer imagedrop7
    with Dissolve(1.5)

    ANS """My own wife, the mother of my children, is a rat."""
    ANS """Why has God punished me? What did I do to deserve such betrayal?"""
    ANS """I'll make sure Mina never ends up like you. Mina will learn how to be a proper woman, not some ungrateful whore."""
    
    ### START OVERTRANSITION END

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    $ ClearOverframe()
    $ SoundOff(2.0)

    play music1 "scenefiveatm.mp3" fadein 2.5 volume 0.3

    show tranone onlayer imagedrop5
    hide tranonereverse
    with Dissolve(0.3)

    ### END OVERTRANSITION END

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    hide underlay
    show underlayc onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoomsad onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    play fx2 "minashooting.mp3" volume 0.3
    
    MZU """I hate myself for what I've done!"""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomsad
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomserious onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    $ renpy.music.set_volume(1, delay=2, channel='music1')

    RZU """Mina! You need to stop torturing yourself over this…"""
    
    hide rexzoomshadow
    hide rexzoomserious
    hide rexzoomdark
    with Dissolve(0.2)
    
    NU """Mina quietly nods and continues to walk with Rex in silence."""
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoomsad onlayer chardrop1
    show minazoomdark onlayer chardrop3
    show introspectfx onlayer imagedrop6:
        alpha 0.8
    show blackover2 onlayer imagedrop5:
        alpha 0.5
    with Dissolve(0.2)
    
    
    MZU """(Maybe I am just like my father…)"""
    
    $ lumafade = 0.001
    hide minazoomsad
    show minazoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(Maybe I've been molded into becoming just like him.)"""
    
    $ lumafade = 0.001
    hide minazoompain
    show minazoomregret onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(After all, I was the one who told Rex to come to my place when he should have gone on the run.)"""
    
    $ lumafade = 0.001
    hide minazoomregret
    show minazoomsad onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(…But I didn't want to be alone.)"""
    
    $ lumafade = 0.001
    hide minazoomsad
    show minazoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(So I guess I manipulated him just like my father manipulates people?)"""
    
    $ lumafade = 0.001
    hide minazoompain
    show minazoomserious onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(Or maybe I'm overthinking…)"""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide minazoomserious
    show minazoompain onlayer chardrop1
    with Dissolve(0.2)
    
    play fx1 "minafatherhelp.mp3" volume 0.3

    MZU """(But I was the one who couldn't believe my own mother…)"""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide minazoompain
    show minazoomsad onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(Because I was skeptical of my own mother, I ended up causing her murder.)"""
    
    $ lumafade = 0.001
    hide minazoomsad
    show minazoompain onlayer chardrop1
    with Dissolve(0.2)

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    
    MZU """(Why couldn't I just believe her? Why…)"""

    play fx2 "minachoice.mp3" volume 0.3
    
    hide underlayc
    show blackover onlayer chardrop6:
        alpha 0.8
    with Dissolve(0.5)

    menu:
        "(Your skepticism of your mother was warranted; don't blame yourself.)":
            $ notrustrex = notrustrex + 1
            play fx3 "notrustchoice.mp3" volume 0.3
            pass
        "(Your inability to trust people, even your mother, is one of your key faults.)":
            $ trustrex = trustrex + 1
            play fx3 "trustchoice.mp3" volume 0.3
            pass

    $ renpy.music.set_volume(1, delay=2, channel='music1')

    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    hide blackover
    with Dissolve(0.2)

    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    show underlayc onlayer under 
    with Dissolve(0.2)
    
    
    MZU """(…I have to stop brooding over this.)"""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide minazoompain
    hide introspectfx
    hide blackover2
    show minazoomlove onlayer chardrop1
    with Dissolve(0.2)
    

    play fx3 "sharedtrauma.mp3" volume 0.3
    
    MZU """Rex, I know it sounds messed up to say, but I'm so glad that you can understand me…"""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide minazoomlove
    show minazoomcontent onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """Because you've been through the same fucked-up situations as me."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomcontent
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomsmug onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """This whole area has got you overthinking again, hasn't it?"""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomsmug
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomserious onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """But isn't it true?"""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomserious
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomcontent onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Of course it is."""
    
    $ lumafade = 0.001
    hide rexzoomcontent
    show rexzoomsmug onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """But is it something worth reiterating? It makes it sound like you need extra reassurance."""
    
    $ lumafade = 0.001
    hide rexzoomsmug
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """…As if my actions aren't reassuring enough already."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomshock onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """No, no… that's not what I mean."""
    
    hide minazoomshadow
    hide minazoomshock
    hide minazoomdark
    with Dissolve(0.2)
    
    ### START OVERTRANSITION START

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    show blackover onlayer imagedrop5
    show fathersus onlayer imagedrop6 
    show frame43 onlayer imagedrop7
    show blackover2 onlayer imagedrop8

    hide tranonereverse
    $ ClearChar()
    $ SoundOff(2.0)

    show tranone onlayer effects
    hide blackover2
    with Dissolve(0.2)

    play music1 "rexfather.mp3" fadein 1.5 volume 0.3

    ### END OVERTRANSITION START

    
    hide underlayc
    show underlay onlayer under
    with Dissolve(0.3)
    
    RNS """I think he's starting again."""
    RNS """He's taking phone calls away from me and my mother."""
    RNS """Fucking degenerate gambler."""
    RNS """How could he do this to us again? How could he put Mother through this again?"""
    RNS """He's such a pathetic loser…"""
    RNS """This time, I'm going to need some extra help… I need to make sure this is the last time."""

    show rexrat onlayer imagedrop6
    with Dissolve(1.5)

    RNS """You guys are his friends, right?"""

    hide fathersus

    RNS """He won't listen to me or my mom."""
    RNS """Please! You gotta help me!"""
    RNS """Maybe he'll listen to you guys?"""

    show rexfatherdanger onlayer imagedrop7
    with Dissolve(0.5)

    CNS """REX! WHAT THE FUCK HAVE YOU DONE?!"""
    
    ### START OVERTRANSITION END

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    $ ClearOverframe()
    $ SoundOff(2.0)

    play music1 "scenefiveatm.mp3" fadein 2.5 volume 0.3

    show tranone onlayer imagedrop5
    hide tranonereverse
    with Dissolve(0.3)

    ### END OVERTRANSITION END

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')

    hide underlay
    show underlayc onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show rexzoomshadow onlayer chardrop00
    show rexzoomsad onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    show introspectfx onlayer imagedrop6:
        alpha 0.8
    show blackover2 onlayer imagedrop5:
        alpha 0.5
    with Dissolve(0.2)

    play fx2 "rexguiltdad.mp3" volume 0.3
    
    
    RZU """(My lack of judgment put me in this current predicament.)"""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide rexzoomsad
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(But it's more than that… it's a lack of values.)"""
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomsad onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(To rat out my own father? What the fuck was I thinking?)"""
    
    $ lumafade = 0.001
    hide rexzoomsad
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(I should've realized it was the gambling… that he was actually doing something good.)"""
    
    $ renpy.music.set_volume(0.1, delay=2, channel='music1')

    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomangry onlayer chardrop1
    with Dissolve(0.2)

    play fx2 "rexguiltmother.mp3" volume 0.3
    
    
    RZU """(It's the same lack of judgment I showed with my mother.)"""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide rexzoomangry
    show rexzoomserious onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(I should've seen the warning signs; I was such a fool.)"""
    
    $ lumafade = 0.001
    hide rexzoomserious
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(The way she carried on like nothing happened after my father's murder.)"""
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomsad onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(All the pain she must've repressed, just to make it seem like everything was all right.)"""
    
    $ lumafade = 0.001
    hide rexzoomsad
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(Only for all of that pain to burst because she couldn't get any help.)"""
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomangry onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(I should've realized! Why couldn't I help my mother?)"""
    
    $ lumafade = 0.001
    hide rexzoomangry
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(Maybe my lack of judgment is going to ruin my plans with Mina too…)"""

    hide underlayc
    show blackover onlayer chardrop6:
        alpha 0.8
    with Dissolve(0.5)

    menu:
        "(You're right; you need to explain everything to Mina or else she'll leave.)":
            $ notrustmina = notrustmina + 1
            play fx2 "notrustchoice.mp3" volume 0.3
            pass
        "(You're wrong; the right judgment is to do nothing rash and trust Mina.)":
            $ trustmina = trustmina + 1
            play fx2 "trustchoice.mp3" volume 0.3
            pass


    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    hide blackover
    with Dissolve(0.2)

    
    $ lumafade = 0.1
    show rexzoomshadow onlayer chardrop00
    show rexzoompain onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    show underlayc onlayer under 
    with Dissolve(0.2)
    
    
    RZU """(I'm going to have to do something soon…)"""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    hide introspectfx
    hide blackover2
    with Dissolve(0.2)

    show redflowerclose onlayer imagedrop5
    with Dissolve(0.5)

    play fx2 "gottabelieve.mp3" volume 0.3
    
    NU """Rex breaks his silence and points to more red flowers growing nearby."""
    
    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    hide underlayc
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show rexstandingshadow onlayer chardrop00
    show rexstandingshock onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSU """Look! There are more of them; we're getting close."""
    
    $ lumafade = 0.1
    hide rexstandingshadow
    hide rexstandingshock
    hide rexstandingdark
    show minastandingshadow onlayer chardrop00
    show minastandingshock onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSU """We're getting closer to the processing facility?"""
    
    $ lumafade = 0.1
    hide minastandingshadow
    hide minastandingshock
    hide minastandingdark
    show rexstandingshadow onlayer chardrop00
    show rexstandinghappy onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSU """That's right; the more red flowers we see, the closer we're getting."""
    
    hide rexstandingshadow
    hide rexstandinghappy
    hide rexstandingdark
    hide redflowerclose
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlayc onlayer under
    with Dissolve(0.3)

    play fx2 "flames.mp3" volume 0.5
    
    NU """The gentle rustling of flames can be heard in the distance."""
    
    
    hide underlayc
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show rexstandingshadow onlayer chardrop00
    show rexstandingshock onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSU """Did you hear that?"""
    
    $ lumafade = 0.1
    hide rexstandingshadow
    hide rexstandingshock
    hide rexstandingdark
    show minastandingshadow onlayer chardrop00
    show minastandingshock onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSU """Yeah, it sounds like a fire of some sort."""
    
    $ lumafade = 0.1
    hide minastandingshadow
    hide minastandingshock
    hide minastandingdark
    show rexstandingshadow onlayer chardrop00
    show rexstandingserious onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSU """Quick! Let's head over there."""
    
    hide rexstandingshadow
    hide rexstandingserious
    hide rexstandingdark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)

    play fx1 "footsteps.ogg" volume 0.3
    
    NW """Mina and Rex cautiously make their way toward the origin of the sound."""



##########
#####
###
#
#
# SCENE SIX
#
#
##
###
#####
##########


    $ transhift = 0.167
    show tranonereverse onlayer effects
    pause 1.0

    $ SoundOff(2.0)
    $ ClearLayers()

    pause 1.0

    show frame169 onlayer imagedrop4
    show blackover onlayer imagedrop5
    show scenesixmain onlayer imagedrop1

    NW """SECTION 56: ABANDONED CAMPSITE."""

    scene tranone onlayer imagedrop5
    scene frame169 onlayer imagedrop4
    with Dissolve(0.5)

    play music1 "scenesixatm.mp3" fadein 1.5 volume 0.4

    pause 1.5

    show underlay onlayer under
    with Dissolve(0.3)

    python:
        achievement.grant("a6")
        achievement.sync()


    NW """As Rex and Mina follow the sound, they notice a field in the distance."""
    NW """The sound is coming from a small campfire."""

    $ backdropvar = 0.2

    scene widetoultra onlayer imagedrop4

    show scenesixchar onlayer imagedrop2
    hide scenesixmain
    with Dissolve(3.5)

    pause 0.5
 
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    $ renpy.music.set_volume(0.1, delay=2, channel='music1')

    $ lumafade = 0.1
    show rexstandingshadow onlayer chardrop00
    show rexstandingshock onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)

    play fx2 "s56now.mp3" volume 0.3
    
    
    RSW """Someone was here? The fire looks like it was lit recently."""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide rexstandingshock
    show rexstandingserious onlayer chardrop1
    with Dissolve(0.2)
    
    
    RSW """But there isn't anyone here… I can't see anyone in the distance either."""
    
    $ lumafade = 0.1
    hide rexstandingshadow
    hide rexstandingserious
    hide rexstandingdark
    show minastandingshadow onlayer chardrop00
    show minastandingangry onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSW """Why would there be people here, Rex?"""
    
    hide minastandingshadow
    hide minastandingangry
    hide minastandingdark
    with Dissolve(1.2)

    scene ultratowide onlayer imagedrop4
    show scenesixmain onlayer imagedrop2
    with Dissolve(1.5)

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')

    $ lumafade = 0.1 
    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show rexfacepain onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    hide scenesixchar
    with Dissolve(0.5)
    
    play fx2 "s56lore.mp3" volume 0.3
    
    RFW """It must be scavengers…"""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide rexfacepain
    hide rexfacedark
    show minafaceshock onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """Scavengers?"""
    
    $ lumafade = 0.1
    hide minafaceshock
    hide minafacedark
    show rexfaceserious onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """Ever since Section 56 was cleared out, lots of rumours started to spread."""
    RFW """Of course, none of them were based on what your father was actually doing here."""
    
    $ lumafade = 0.001
    hide rexfaceserious
    show rexfacepain onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """However, within certain groups, they turned into powerful myths."""
    
    $ lumafade = 0.001
    hide rexfacepain
    show rexfacesad onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """These myths claimed Section 56 held hidden treasure."""
    
    $ lumafade = 0.001
    hide rexfacesad
    show rexfaceregret onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """So every now and again, there would be sightings of scavengers entering Section 56."""
    
    $ lumafade = 0.1
    hide rexfaceregret
    hide rexfacedark
    show minafaceshock onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """So these poor people fell for some myth about hidden treasure?"""
    
    hide facebackground
    hide facedark
    hide minafaceshock
    hide minafacedark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)
    
    NW """Rex sighs and gives Mina a depressed look before turning his head."""
    
    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1 
    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show rexfaceneutral onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    play fx3 "redflowers.mp3" volume 0.3
    
    show flowersfx onlayer imagedrop5:
        alpha 0.3
    with Dissolve(0.5)

    RFW """Look around, Mina… The red flowers are increasing in number."""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide rexfaceneutral
    show rexfaceserious onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """They’re even right next to the fire."""
    
    $ lumafade = 0.1
    hide rexfaceserious
    hide rexfacedark
    show minafaceshock onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """Does that mean…?"""
    
    $ lumafade = 0.1
    hide minafaceshock
    hide minafacedark
    show rexfaceserious onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """We're getting very close."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide rexfaceserious
    hide rexfacedark
    show minafaceangry onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    play fx1 "dumping.mp3" volume 0.3

    MFW """Close to the processing plant for the red flowers?"""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide minafaceangry
    hide minafacedark
    show rexfaceserious onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """…Yeah."""
    
    $ lumafade = 0.1
    hide rexfaceserious
    hide rexfacedark
    show minafaceangry onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    hide flowersfx
    with Dissolve(0.2)
    
    
    MFW """Rex, a lot of this isn't making any sense."""
    
    $ lumafade = 0.001
    hide minafaceangry
    show minafaceserious onlayer chardrop1 at face_wide
    with Dissolve(0.2)

    show conflictfx onlayer imagedrop5:
        alpha 0.3
    with Dissolve(0.5)
    
    
    MFW """Why is Section 56 abandoned right now? If the processing plant is so important to my father, why is it empty?"""
    
    $ lumafade = 0.1
    hide minafaceserious
    hide minafacedark
    show rexfacecontent onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """We'll get to that when the time comes."""
    
    $ lumafade = 0.1
    hide rexfacecontent
    hide rexfacedark
    show minafaceangry onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """Why can't you just let me know now? Why do you keep being so vague?"""
    
    $ lumafade = 0.1
    hide minafaceangry
    hide minafacedark
    show rexfaceangry onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """Because some things can't be explained with words, Mina."""
    
    $ lumafade = 0.1
    hide rexfaceangry
    hide rexfacedark
    show minafaceangry onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """What the fuck does that even mean?"""
    
    $ lumafade = 0.1
    hide minafaceangry
    hide minafacedark
    show rexfaceserious onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """Don't you trust me, Mina?"""
    
    $ lumafade = 0.1
    hide rexfaceserious
    hide rexfacedark
    show minafaceangry onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """That's unfair, Rex. You can't say that when I'm genuinely concerned about all of this!"""
    
    $ lumafade = 0.1
    hide minafaceangry
    hide minafacedark
    show rexfacepain onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """Just believe me, Mina."""
    
    $ lumafade = 0.1
    hide rexfacepain
    hide rexfacedark
    show minafaceregret onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """…I wasn't even able to believe my own mother, Rex."""
    
    $ lumafade = 0.1
    hide minafaceregret
    hide minafacedark
    show rexfaceangry onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """Then make things right with me."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    hide facebackground
    hide facedark
    hide rexfaceangry
    hide rexfacedark
    hide conflictfx
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)
    
    play fx2 "tension.mp3" volume 0.3

    show wovenbag onlayer imagedrop5 
    with Dissolve(0.5)

    NW """Rex notices a woven bag next to the fire."""

    $ renpy.music.set_volume(1, delay=2, channel='music1')

    play fx3 "opensack.mp3" volume 0.4


    NW """He opens it."""
    
    
    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1 
    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show rexfaceshock onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """Mina, this bag is full of useful supplies. It's got matches, food, water, tools…"""
    
    $ lumafade = 0.001
    hide rexfaceshock
    show rexfaceneutral onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """We should take this and keep going on our journey."""
    
    $ lumafade = 0.1
    hide rexfaceneutral
    hide rexfacedark
    show minafaceshock onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """Wait, wait… What? That's not our stuff, Rex."""
    
    $ lumafade = 0.1
    hide minafaceshock
    hide minafacedark
    show rexfaceangry onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """Really, Mina? You're worried about us being thieves now?"""
    
    $ lumafade = 0.1
    hide rexfaceangry
    hide rexfacedark
    show minafacepain onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """It's not that… Okay, that concerns me a little bit."""
    
    $ lumafade = 0.001
    hide minafacepain
    show minafacesad onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """They might come, stalk us, and take revenge on us later."""
    
    $ lumafade = 0.1
    hide minafacesad
    hide minafacedark
    show rexfaceserious onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """Don't be silly, Mina."""
    
    $ lumafade = 0.1
    hide rexfaceserious
    hide rexfacedark
    show minafaceangry onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)

    show conflictfx onlayer imagedrop5:
        alpha 0.3
    with Dissolve(0.5)
    
    
    MFW """I'm not! For fuck's sake, Rex, I'm not joking."""
    
    $ lumafade = 0.001
    hide minafaceangry
    show minafaceserious onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """If we steal their stuff, it could come back to hurt us later."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide minafaceserious
    hide minafacedark
    show rexfaceserious onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)

    play fx3 "motherinmina.mp3" volume 0.3
    
    
    RFW """This is survival, Mina. We need these supplies if we want to make it to the end."""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide rexfaceserious
    show rexfaceangry onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """You're being illogical and paranoid."""
    
    $ lumafade = 0.1
    hide rexfaceangry
    hide rexfacedark
    show minafaceangry onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """What the fuck, Rex?"""
    
    $ lumafade = 0.1
    hide minafaceangry
    hide minafacedark
    show rexfaceserious onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """I'm taking this stuff. That's that."""
    
    hide facebackground
    hide facedark
    hide rexfaceserious
    hide rexfacedark
    hide conflictfx
    with Dissolve(0.2)
    
    
    hide underlayb
    hide wovenbag
    with Dissolve(0.5)

    scene widetoultra onlayer imagedrop4
    show scenesixchar onlayer imagedrop2
    with Dissolve(1.5)


    show underlayc onlayer under
    hide scenesixmain
    with Dissolve(0.3)

    play fx2 "grabbag.mp3" volume 0.5
    
    NU """Rex grabs the bag and tries to swing it over his shoulder."""

    play fx3 "pullback.mp3" volume 0.5


    NU """However, Mina stops him by violently grabbing his arm."""

    show minastareangry onlayer imagedrop5
    with Dissolve(0.5)

    NU """She stares at him; there's rage in her eyes."""

    hide minastareangry
    show rexstare onlayer imagedrop5
    with Dissolve(0.5)


    NU """He stares back…"""

    ### START OVERTRANSITION START

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    show blackover onlayer imagedrop5
    show rexstare onlayer imagedrop6 
    show frame43 onlayer imagedrop7
    hide conflictfx
    show blackover2 onlayer imagedrop8

    hide tranonereverse
    $ ClearChar()
    $ SoundOff(2.0)

    show tranone onlayer effects
    hide blackover2
    with Dissolve(0.2)

    play music1 "firstglance.mp3" fadein 1.5 volume 0.3

    ### END OVERTRANSITION START

    
    hide underlayc
    show underlay onlayer under
    with Dissolve(0.3)
    
    DNS """Rex, what are you looking at?"""

    show rexstreetmina onlayer imagedrop6
    with Dissolve(0.5)

    hide rexstare

    DNS """Rex, stop staring. We need to go inside; it's about to begin."""
    RNS """…Who is she?"""

    show minastreetrex onlayer imagedrop6
    with Dissolve(0.5)

    pause 0.5

    hide rexstreetmina

    MNS """…Who is he?"""

    ### START OVERTRANSITION END

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    $ ClearOverframe()
    $ SoundOff(2.0)

    play music1 "scenesixatm.mp3" fadein 2.5 volume 0.3

    show tranone onlayer imagedrop5
    hide tranonereverse
    with Dissolve(0.3)

    ### END OVERTRANSITION END

    

    hide underlay
    show underlayc onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show rexzoomshadow onlayer chardrop00
    show rexzoomangry onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Mina! What are you doing?"""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomangry
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)

    play fx1 "fatherinrex.mp3" volume 0.3
    
    
    MZU """It just makes me wonder."""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide minazoompain
    show minazoomangry onlayer chardrop1
    with Dissolve(0.2)
    
    show tensionfx onlayer imagedrop5:
        alpha 0.3
    with Dissolve(0.5)
    
    MZU """If I told you there was danger ahead, would you believe me?"""
    MZU """If I told you we were being chased and needed to hide, would you believe me?"""
    
    $ lumafade = 0.001
    hide minazoomangry
    show minazoomserious onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """If I told you that you needed to kill me in order to survive, would you believe me?"""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomserious
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomangry onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Oh my God, Mina… Please, not now."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomangry
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomangry onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """Why not now?"""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')

    play fx1 "minafatherhelp.mp3" volume 0.3

    MZU """Why do you always dismiss my concerns? Do you think you're that much better than me?"""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomangry
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomangry onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """What have we been doing these past few hours?"""
    
    $ lumafade = 0.001
    hide rexzoomangry
    show rexzoomserious onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """We've worked as a team!"""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomserious
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomangry onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """Well, we won't be a team when whoever owns those supplies comes and murders us later!"""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomangry
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomangry onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """This is Section 56, Mina! It's just some scavenger!"""
    
    $ lumafade = 0.001
    hide rexzoomangry
    show rexzoomserious onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """There aren't any military marauders or police tactical units here."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomserious
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomangry onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """So?"""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomangry
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomserious onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Are you even listening to what I'm saying?"""
    
    $ lumafade = 0.001
    hide rexzoomserious
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """You're acting just like when we first met…"""
    
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    with Dissolve(0.2)

    ### START OVERTRANSITION START

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    show blackover onlayer imagedrop5
    show minastareangry onlayer imagedrop6 
    show frame43 onlayer imagedrop7
    show blackover2 onlayer imagedrop8

    hide tranonereverse
    $ ClearChar()
    $ SoundOff(2.0)

    show tranone onlayer effects
    hide blackover2
    with Dissolve(0.2)

    play music1 "graveyard.mp3" fadein 1.5 volume 0.3

    ### END OVERTRANSITION START
    
    hide underlayc
    show underlay onlayer under
    with Dissolve(0.3)
    
    show rainfx onlayer effects
    with Dissolve(0.5)

    MNS """I'm going to be the death of you…"""

    MNS """My mother would still be here if it weren't for your dad!"""

    show rexstare onlayer imagedrop5
    with Dissolve(0.5)

    hide minastareangry

    RNS """That's not what happened; what are you talking about?"""

    show thunderfx onlayer effects2
    play fx3 "lightning.mp3" volume 0.4

    show minastareangry onlayer imagedrop5
    with Dissolve(0.5)

    show underlaystatic onlayer under:
        shake_effect(0.04, 10, 3)

    MNS """Fuck you! I just told you!"""

    hide underlaystatic
    hide thunderfx

    show rexstare onlayer imagedrop5
    with Dissolve(0.5)

    hide minastareangry

    RNS """And I just told you too! My dad didn't have anything to do with it!"""

    show thunderfx onlayer effects
    play fx2 "lightning.mp3" volume 0.4

    show minastareangry onlayer imagedrop5
    hide rexstare
    hide thunderfx
    with Dissolve(0.5)


    show underlaystatic onlayer under:
        shake_effect(0.04, 10, 3)

    MNS """I hate you!"""
    
    show underlayd onlayer under
    hide underlaystatic
    hide underlay
    with Dissolve(0.3)
    
    $ shadowvar = 0.1
    $ shadowcharvar = 1
    $ darkcharvar = 0.9
    
    $ lumafade = 0.1
    show rexstandingshadow onlayer chardrop00
    show rexstandingneutral onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    hide minastareangry
    with Dissolve(0.2)
    
    
    RSS """Get the fuck away from my dad's grave, you crazy bitch!"""
    
    hide rexstandingshadow
    hide rexstandingneutral
    hide rexstandingdark
    with Dissolve(0.2)
    
    
    hide underlayd
    show underlay onlayer under
    with Dissolve(0.3)
    
    MNS """…I know it's my dad's fault."""
    
    hide underlay
    show underlayd onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show rexstandingshadow onlayer chardrop00
    show rexstandingneutral onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSS """Huh?"""
    
    hide rexstandingshadow
    hide rexstandingneutral
    hide rexstandingdark
    with Dissolve(0.2)
    
    
    hide underlayd
    show underlay onlayer under
    with Dissolve(0.3)
    
    MNS """I'm sorry, I'm sorry."""
    MNS """…Just stay with me here. Please."""
    
    hide underlay
    hide underlaystatic
    hide rainfx
    with Dissolve(1.0)

    ### START OVERTRANSITION END

    $ shadowvar = 0.3
    $ shadowcharvar = 0.1
    $ darkcharvar = 0

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    $ ClearOverframe()
    $ SoundOff(2.0)

    play music1 "scenesixatm.mp3" fadein 2.5 volume 0.3

    show tranone onlayer imagedrop5
    hide tranonereverse
    with Dissolve(0.3)

    ### END OVERTRANSITION END

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    show underlayc onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    play fx2 "minashooting.mp3" volume 0.3
    
    MZU """…I feel like I'm fulfilling my father's wishes by hating you."""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    
    $ lumafade = 0.001
    hide minazoompain
    show minazoomregret onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """It's so fucking difficult to unlearn all the things he told me about you and your father."""
    
    $ lumafade = 0.001
    hide minazoomregret
    show minazoomsad onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """…So when you get aggressive toward me, it reminds me of all the lies my father told about you."""
    
    $ lumafade = 0.001
    hide minazoomsad
    show minazoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """There's a fine line between love and hate, Rex."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoompain onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Ugh… Why is our relationship so screwed up?"""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomsad onlayer chardrop1
    with Dissolve(0.2)
    
    play fx2 "rexguiltdad.mp3" volume 0.3
    
    RZU """I'm sorry about earlier… This whole experience has been frustrating for me."""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide rexzoomsad
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """Partly it's because, Mina… there are things about me you still don't know."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomserious onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """So? You don't know everything about me either."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomserious
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomregret onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """No, it's that I feel guilty for what happened not only to my father, but to your mother too."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomregret
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomangry onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """Why would you feel that? You were a victim too."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomangry
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomsad onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """No, I played a part in getting my father murdered; that's a fact."""
    
    $ lumafade = 0.001
    hide rexzoomsad
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """And, by extension, getting your mother murdered too."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomserious onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """What do you mean?"""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomserious
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoompain onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """I misjudged my father… I thought he was doing something wrong to me and my mother."""
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomsad onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """It turned out he was just trying to help us… and I screwed everything up."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomsad
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomserious onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)

    play fx3 "rexguiltmother.mp3" volume 0.3
    
    
    MZU """Rex, my father was behind your father's murder. How could you have caused it?"""


    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomserious
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoompain onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Like I said, a lack of judgement."""
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomregret onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """The same lack of judgement that caused my mother to die too…"""
    
    $ lumafade = 0.001
    hide rexzoomregret
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """Maybe the same lack of judgement that will cost us…"""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomangry onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """Stop! I don't want to hear this!"""
    MZU """You're clearly overthinking everything, wallowing in self-pity."""
    
    $ lumafade = 0.001
    hide minazoomangry
    show minazoomserious onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """You've never been like this before; I swear you're acting really fucking weird ever since we got here."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomserious
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoompain onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """So? Are you going to ditch me now?"""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomangry onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """Come on, don't be like that."""
    
    $ lumafade = 0.001
    hide minazoomangry
    show minazoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """Ugh… All of this is getting to be too much."""
    
    $ lumafade = 0.001
    hide minazoompain
    show minazoomregret onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """You haven't told me why we needed to come to Section 56 in the first place."""
    
    $ lumafade = 0.001
    hide minazoomregret
    show minazoomsad onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """After that, you've been super vague about my father being behind the area being abandoned."""
    
    $ lumafade = 0.001
    hide minazoomsad
    show minazoomserious onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """…And all this stuff about the red flowers we've found? You still haven't fully explained that either."""
    
    $ lumafade = 0.001
    hide minazoomserious
    show minazoomangry onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """Why do I need to be here anyway? If the flowers are the solution, couldn't you have done all of this yourself?"""
    
    $ lumafade = 0.001
    hide minazoomangry
    show minazoomserious onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """Why throw me into all this danger too?"""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomserious
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoompain onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """…I told you, it's hard to explain."""
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomsad onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """I guess I was right; you don't trust me."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    hide rexzoomshadow
    hide rexzoomsad
    hide rexzoomdark
    with Dissolve(1.2)

    play fx2 "windgust.mp3" volume 0.5    
    play fx1 "radiation.mp3" volume 0.3    
    
    NU """A gust of wind suddenly rushes through the area."""

    $ renpy.music.set_volume(1, delay=2, channel='music1')

    show flowersfx onlayer imagedrop5:
        alpha 0.4
    with Dissolve(0.5)

    NU """Hundreds of red flower petals swirl through the campsite, engulfing Rex and Mina."""

    show dizzyfx onlayer imagedrop6:
        alpha 0.2
    with Dissolve(0.5)

    NU """Rex and Mina's vision starts to distort."""

    show sicknessfx onlayer imagedrop5:
        alpha 0.2
    with Dissolve(0.5)

    play fx3 "coughing.mp3" volume 0.3    

    NU """Rex starts coughing violently."""


    show minarash onlayer imagedrop7
    with Dissolve(0.2)

    play fx1 "pullback.mp3" volume 0.3    

    NU """Mina clutches her arm in pain."""
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    hide minarash
    with Dissolve(0.2)
    
    play fx2 "sizzle.mp3" volume 0.5
    
    MZU """My arm, it's burning!"""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoompain onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """I can't see… Ugh! I can't fucking see!"""
    
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    with Dissolve(0.2)

    play fx2 "fallover.mp3" volume 0.6
    
    NU """Mina grabs Rex as they fall to the ground."""
    
    $ lumafade = 0.1
    show rexzoomshadow onlayer chardrop00
    show rexzoompain onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Mina…"""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """…I can't handle this pain for much longer."""
    
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    with Dissolve(0.2)
    
    NU """Rex and Mina writhe in pain for a few minutes…"""

    hide flowersfx
    hide dizzyfx
    hide sicknessfx
    with Dissolve(2.0)


    NU """Eventually, their symptoms begin to fade."""

    play fx2 "getup.mp3" volume 0.4    

    NU """Rex helps Mina back to her feet."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    show rexzoomshadow onlayer chardrop00
    show rexzoomshock onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    play fx1 "rexchoice.mp3" volume 0.3    

    RZU """Are you okay, Mina?"""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomshock
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """Barely… I have no idea what the hell just happened."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomserious onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """The wind must've spread the pollen from the red flowers around."""
    
    $ lumafade = 0.001
    hide rexzoomserious
    show rexzoomregret onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """In large amounts, pollen from the red flowers is known to irritate the human body."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomregret
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """…I see."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomserious onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Mina, we're already deep into Section 56. Will you please keep going with me?"""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomserious
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomregret onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """You're right; we've already come this far."""
    
    $ lumafade = 0.001
    hide minazoomregret
    show minazoomserious onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """It's not that I don't trust you, Rex; I just wish you'd explain everything better."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomserious
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomcontent onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """I know, I know. Everything will be revealed in due time."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomcontent
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """…Okay."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoompain onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    show introspectfx onlayer imagedrop6:
        alpha 0.8
    show blackover2 onlayer imagedrop5:
        alpha 0.5
    with Dissolve(0.2)
    
    
    RZU """(Oh great, you've fucking done it now.)"""
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomsad onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(Mina has practically admitted she might ditch me.)"""
    
    $ lumafade = 0.001
    hide rexzoomsad
    show rexzoomregret onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(She has all these questions, and she won't trust me unless I answer them.)"""
    RZU """(She doesn't trust me.)"""
    
    $ lumafade = 0.001
    hide rexzoomregret
    show rexzoomsad onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(She'll ditch me before we reach the end.)"""
    
    $ lumafade = 0.001
    hide rexzoomsad
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(Should I prepare myself to tell her everything?)"""
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomshock onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(But maybe telling her everything will just ensure she'll leave me?)"""

    hide underlayc
    show blackover onlayer chardrop6:
        alpha 0.8
    with Dissolve(0.5)

    menu:
        "(Unless you tell her everything, she'll leave you.)":
            $ notrustmina = notrustmina + 1
            play fx2 "notrustchoice.mp3" volume 0.3
            pass
        "(Trust Mina, you don't need to reveal everything to her.)":
            $ trustmina = trustmina + 1
            play fx2 "trustchoice.mp3" volume 0.3
            pass


    hide rexzoomshadow
    hide rexzoomshock
    hide rexzoomdark
    hide blackover
    with Dissolve(0.2)

    
    $ lumafade = 0.1
    show rexzoomshadow onlayer chardrop00
    show rexzoompain onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    show underlayc onlayer under 
    with Dissolve(0.2)
    
    
    RZU """(…I'll need to make a decision sooner or later.)"""
    
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    hide introspectfx
    hide blackover2
    with Dissolve(0.2)
    
    NU """Mina begins to walk at a pace slightly slower than Rex…"""
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    show introspectfx onlayer imagedrop6:
        alpha 0.8
    show blackover2 onlayer imagedrop5:
        alpha 0.5
    with Dissolve(0.2)
    
    
    MZU """(I swear Rex has been acting really suspicious since we got here.)"""
    
    $ lumafade = 0.001
    hide minazoompain
    show minazoomregret onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(At the same time, I can't tell whether I'm just projecting my hatred of my father onto him.)"""
    
    $ lumafade = 0.001
    hide minazoomregret
    show minazoomsad onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(It's like my mind wants to pollute every relationship with the trauma my father inflicted.)"""
    
    $ lumafade = 0.001
    hide minazoomsad
    show minazoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(But maybe the opposite is true?)"""
    
    $ lumafade = 0.001
    hide minazoompain
    show minazoomregret onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(Maybe because I know my father so well, I can see the same traits in someone else?)"""
    
    $ lumafade = 0.001
    hide minazoomregret
    show minazoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(My instincts might be telling me that Rex isn't who I think he is.)"""
    
    $ lumafade = 0.001
    hide minazoompain
    show minazoomserious onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(Or maybe it's just my usual cynicism distorting everything?)"""

    hide underlayc
    show blackover onlayer chardrop6:
        alpha 0.8
    with Dissolve(0.5)

    menu:
        "(Rex is acting suspicious; you're not being delusional.)":
            $ notrustrex = notrustrex + 1
            play fx2 "notrustchoice.mp3" volume 0.3
            pass
        "(Rex isn't acting suspicious; you're misinterpreting this chaotic situation.)":
            $ trustrex = trustrex + 1
            play fx2 "trustchoice.mp3" volume 0.3
            pass

    
    # Move it over here for the menu 
    # You need to do this so we don't double up on the characters later       
    hide minazoomshadow
    hide minazoomserious
    hide minazoomdark
    hide blackover 
    with Dissolve(0.2)

    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    show underlayc onlayer under
    with Dissolve(0.2)
    
    
    MZU """(…Why does everything have to be so difficult?)"""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    hide introspectfx
    hide blackover2
    with Dissolve(0.2)

    play fx2 "sharedtrauma.mp3" volume 0.3
    
    NU """Rex notices Mina trailing behind him."""

    $ renpy.music.set_volume(1, delay=2, channel='music1')

    show rexstare onlayer imagedrop5
    with Dissolve(0.5)


    NU """He stops and turns around, looking Mina straight in the eyes."""
    
    $ lumafade = 0.1
    show rexzoomshadow onlayer chardrop00
    show rexzoomcontent onlayer chardrop1
    hide rexstare
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """…You know what, I don't want to argue."""
    
    $ lumafade = 0.001
    hide rexzoomcontent
    show rexzoomlove onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """You're my only reason for living, Mina. I'm not afraid to admit that."""
    RZU """You were right; we shouldn't steal the scavenger's belongings."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomlove
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomlove onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """Rex…"""
    
    $ lumafade = 0.001
    hide minazoomlove
    show minazoomhappy onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """That's all I wanted to hear."""
    
    $ lumafade = 0.001
    hide minazoomhappy
    show minazoomlove onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """…We can go back and take them if you want?"""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    hide minazoomshadow
    hide minazoomlove
    hide minazoomdark
    with Dissolve(0.2)

    play fx2 "romance.mp3" volume 0.3
    play fx3 "hug.mp3" volume 0.5
    
    NU """Rex embraces Mina."""


    $ renpy.music.set_volume(1, delay=2, channel='music1')

    RNU """It's okay; let's just keep going."""
    MNU """Okay."""
    
    hide underlayc
    show underlay onlayer under
    with Dissolve(0.3)
    
    NW """Rex and Mina head farther into Section 56, leaving the campsite behind."""


##########
#####
###
#
#
# SCENE SEVEN
#
#
##
###
#####
##########


    $ shadowvar = 0.3
    $ shadowcharvar = 0.1
    $ darkcharvar = 0


    $ transhift = 0.167
    show tranonereverse onlayer effects
    pause 1.0

    $ SoundOff(2.0)
    $ ClearLayers()

    pause 1.0

    show frame169 onlayer imagedrop4
    show blackover onlayer imagedrop5
    show scenesevenmain onlayer imagedrop1

    NW """SECTION 56: CROSSROADS."""

    scene tranone onlayer imagedrop5
    scene frame169 onlayer imagedrop4
    with Dissolve(0.5)

    play music1 "scenesevenatm.mp3" fadein 1.5 volume 0.4

    pause 1.5

 
    hide nulll
    show underlay onlayer under
    with Dissolve(0.3)
    
    python:
        achievement.grant("a7")
        achievement.sync()


    NW """About half an hour away from the campsite, the air begins to thicken."""
    NW """Within minutes, Mina and Rex find themselves entrenched in fog."""
    NW """Unable to see clearly into the distance, they both stop at a crossroads."""
    
    
    
    hide underlay
    with Dissolve(0.3)

    scene widetoultra onlayer imagedrop4    
    show scenesevenchar onlayer imagedrop2
    with Dissolve(1.5)


    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show rexstandingshadow onlayer chardrop00
    show rexstandingangry onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSW """Goddamn it!"""
    
    hide rexstandingshadow
    hide rexstandingangry
    hide rexstandingdark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)
    
    NW """Within the thick fog, they realize they are standing at a crossroads."""
    
    
    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show rexstandingshadow onlayer chardrop00
    show rexstandingregret onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSW """Do you think we should just keep going straight ahead?"""
    
    $ lumafade = 0.1
    hide rexstandingshadow
    hide rexstandingregret
    hide rexstandingdark
    show minastandingshadow onlayer chardrop00
    show minastandingregret onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSW """Um, I don't think we were going straight the entire time."""
    
    $ lumafade = 0.001
    hide minastandingregret
    show minastandingpain onlayer chardrop1
    with Dissolve(0.2)
    
    
    MSW """I was following you, but I swear you curved left and right a few times."""
    
    hide minastandingshadow
    hide minastandingpain
    hide minastandingdark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)
    
    NW """Rex scrunches his face and thinks for a moment."""
    
    
    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show rexstandingshadow onlayer chardrop00
    show rexstandingangry onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSW """...Fuck!"""
    
    $ lumafade = 0.001
    hide rexstandingangry
    show rexstandingpain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RSW """Alright, maybe you're right, Mina."""
    
    $ lumafade = 0.1
    hide rexstandingshadow
    hide rexstandingpain
    hide rexstandingdark
    show minastandingshadow onlayer chardrop00
    show minastandingangry onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSW """Don't worry, I'm used to you being like this."""
    
    $ lumafade = 0.1
    hide minastandingshadow
    hide minastandingangry
    hide minastandingdark
    show rexstandingshadow onlayer chardrop00
    show rexstandingshock onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSW """Huh? What do you mean?"""
    
    $ lumafade = 0.1
    hide rexstandingshadow
    hide rexstandingshock
    hide rexstandingdark
    show minastandingshadow onlayer chardrop00
    show minastandingpain onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSW """Nothing. Nothing at all."""
    
    hide minastandingshadow
    hide minastandingpain
    hide minastandingdark
    with Dissolve(0.2)

    ### START OVERTRANSITION START

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    show blackover onlayer imagedrop5
    show minarexstart onlayer imagedrop6 
    show frame43 onlayer imagedrop7
    show blackover2 onlayer imagedrop8

    hide tranonereverse
    $ ClearChar()
    $ SoundOff(2.0)

    show tranone onlayer effects
    hide blackover2
    with Dissolve(0.2)

    play music1 "underpassromance.mp3" fadein 1.5 volume 0.3

    ### END OVERTRANSITION START

    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)
    
    MNS """Hey, it's Mina... About the other night, maybe I crossed the line. Either way, I'm sorry."""
    MNS """Rex... It's been a week. Are you okay? Why aren't you answering?"""
    MNS """Rex! What the fuck? Why are you doing this to me? I told you I'm sorry."""
    MNS """Rex! I'm sorry! Please, please, please don't leave me."""
    MNS """Rex, I don't think I can live without you."""
    RNS """Oh, yeah?"""
    MNS """Rex, you know you mean everything to me."""
    RNS """Really?"""
    MNS """Rex, I'll never leave you..."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')

    play fx2 "rexguiltmother.mp3" volume 0.4

    show momdeathstatic onlayer imagedrop6:
        alpha 0.8
    with Dissolve(0.2)

    pause 1.0

    hide momdeathstatic
    with Dissolve(0.3)

    MNS """...Like how your mother left you."""


    RNS """...Huh?"""

    play fx3 "rexmother.mp3" volume 0.4

    show rexmomhome onlayer imagedrop6
    with Dissolve(0.2)

    DNS """I'll see you when you get back from school, Rex."""
    RNS """Make sure to get out of the house today, Mom. Exercise helps, you know?"""
    DNS """Yes, yes. I'll see you later tonight."""

    hide rexmomhome
    show momdeath onlayer imagedrop7:
        alpha 0.8
    with Dissolve(0.1)

    pause 1.0

    hide momdeath
    hide minarexstart
    with Dissolve(0.1)

    RNS """...MOM!"""
    
    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    ### START OVERTRANSITION END

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    $ ClearOverframe()
    $ SoundOff(2.0)

    play music1 "scenesevenatm.mp3" fadein 2.5 volume 0.3

    show tranone onlayer imagedrop5
    hide tranonereverse
    with Dissolve(0.3)

    ### END OVERTRANSITION END

    hide underlay
    show underlayc onlayer under
    with Dissolve(0.3)


    $ renpy.music.set_volume(0.1, delay=2, channel='music1')

    
    $ lumafade = 0.1
    show rexzoomshadow onlayer chardrop00
    show rexzoompain onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    play fx2 "gottabelieve.mp3" volume 0.3
    
    RZU """This situation... It's messing with my mind."""


    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """I'm stressed too; I can't even get a hold of my thoughts."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomneutral onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """...We have to believe in each other, or we're doomed. We won't make it out of here without each other."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomneutral
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomregret onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """That's easier said than done."""
    
    $ lumafade = 0.001
    hide minazoomregret
    show minazoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """I agree with you, though. I'd probably be dead if it weren't for you."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomhappy onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """I'd be dead too if it weren't for you, Mina."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide rexzoomhappy
    show rexzoomlove onlayer chardrop1
    with Dissolve(0.2)

    play fx1 "sharedtrauma.mp3" volume 0.3
    
    
    RZU """We need to combine all our mental baggage, ease the burden... Deal with it together."""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomlove
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomcontent onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """...You make a good point."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomcontent
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomhappy onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Exactly."""
    
    hide rexzoomshadow
    hide rexzoomhappy
    hide rexzoomdark
    with Dissolve(0.2)

    play fx1 "grabhand.mp3" volume 0.5
    
    NU """Mina inches closer to Rex as the fog thickens even more."""
    RNU """Alright, let's keep going ahead for now."""

    play fx2 "slowsteps.mp3" volume 0.5

    NU """The two continue forward for another five minutes or so."""

    show dizzyfx onlayer imagedrop5:
        alpha 0.2
    with Dissolve(0.5)

    NU """It is becoming harder and harder for them to see."""
    
    $ lumafade = 0.1
    show rexzoomshadow onlayer chardrop00
    show rexzoompain onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Ugh! I... I don't know where we're going. I can barely see."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomsad onlayer chardrop1
    with Dissolve(0.2)


    play fx3 "rexguiltdad.mp3" volume 0.3
    
    RZU """I'm sorry, Mina. I think I may have led us in the wrong direction. We might be going around in circles."""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomsad
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomcontent onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """Trust me, we haven't."""
    
    hide minazoomshadow
    hide minazoomcontent
    hide minazoomdark
    with Dissolve(0.2)

    play fx2 "hug.mp3" volume 0.5
    
    NU """Mina grabs Rex's shoulders."""
    MNU """Why do you think I'm here?"""

    play fx3 "pullback.mp3" volume 0.5


    NU """Mina gently pushes Rex as if to change the direction he's walking."""
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoomhappy onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """Ever since the fog started getting thicker, I've been making sure you were going straight."""
    
    $ lumafade = 0.001
    hide minazoomhappy
    show minazoomcontent onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """That's why I was walking a few steps behind you... To make sure you weren't walking in circles."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomcontent
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomlove onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """...Mina."""
    
    $ lumafade = 0.001
    hide rexzoomlove
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """In situations like this, I feel like you're too good for me."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomsmug onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """Oh, please. You're joking, right?"""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomsmug
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomsad onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """I'm not. I don't deserve you."""
    
    $ lumafade = 0.001
    hide rexzoomsad
    show rexzoomregret onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """And this whole predicament we're in? It's really me... It's my fault."""
    
    hide rexzoomshadow
    hide rexzoomregret
    hide rexzoomdark
    hide dizzyfx
    with Dissolve(0.2)

    ### START OVERTRANSITION START

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    show blackover onlayer imagedrop5
    show rexfatherdanger onlayer imagedrop6 
    show frame43 onlayer imagedrop7
    show blackover2 onlayer imagedrop8

    hide tranonereverse
    $ ClearChar()
    $ SoundOff(2.0)

    show tranone onlayer effects
    hide blackover2
    with Dissolve(0.2)

    play music1 "rexfather.mp3" fadein 1.5 volume 0.3

    ### END OVERTRANSITION START

    hide underlayc
    show underlay onlayer under
    with Dissolve(0.3)
    
    CNS """Rex! Why did you do this? Don't you trust me?"""
    CNS """...Ah, fuck. I don't have time for this."""
    CNS """Rex, get out of the way. I have to leave here quickly."""
    CNS """Fuck!"""
    CNS """Listen, Rex. Take care of your mother."""
    CNS """She never deserved any of this."""

    ### START OVERTRANSITION END

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    $ ClearOverframe()
    $ SoundOff(2.0)

    play music1 "scenesevenatm.mp3" fadein 2.5 volume 0.3

    show tranone onlayer imagedrop5
    hide tranonereverse
    with Dissolve(0.3)

    ### END OVERTRANSITION END


    
    hide underlay
    show underlayc onlayer under
    with Dissolve(0.3)

    play fx2 "pacing.mp3" volume 0.5
    
    NU """Rex starts walking at a pace Mina can't keep up with."""

    play fx3 "running.mp3" volume 0.5


    NU """Mina runs beside him to catch up."""
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoomangry onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """Stop!"""
    
    $ lumafade = 0.001
    hide minazoomangry
    show minazoomshock onlayer chardrop1
    with Dissolve(0.2)
    
    show noisedistortfx onlayer imagedrop5:
        alpha 0.3
    with Dissolve(0.5)
    
    MZU """What are you talking about? It's all your fault?"""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomshock
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoompain onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """You don't want to know, Mina. Trust me."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomangry onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)

    play fx1 "minashooting.mp3" volume 0.3
    
    
    MZU """That's because whatever you're talking about is bullshit."""

    $ renpy.music.set_volume(1, delay=2, channel='music1')


    MZU """It's MY father who died, Rex."""
    MZU """And you know damn well the role I had in what happened to MY father."""
    MZU """So I don't want you to start overthinking and coming up with some idiotic reason as to why you're at fault."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomangry
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoompain onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """...I wish that were the case."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomangry onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """Rex, please!"""
    MZU """I've already got enough issues I'm dealing with."""
    
    $ lumafade = 0.001
    hide minazoomangry
    show minazoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """I don't want you to add to them by acting like you're the instigator of this whole situation."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')

    play fx1 "fatherinrex.mp3" volume 0.3

    MZU """You'd better stop with all these mind games you're playing on me."""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomregret onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """They're not mind games, Mina."""
    
    $ lumafade = 0.001
    hide rexzoomregret
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """I know what I've been saying has been all over the place since we came here."""
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomregret onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """But don't accuse me of manipulating you. These are just my honest thoughts."""
    
    $ lumafade = 0.001
    hide rexzoomregret
    show rexzoomsad onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """If you don't trust me on that, then we don't have a relationship. We have nothing."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomsad
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomsad onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """...Rex."""
    
    hide minazoomshadow
    hide minazoomsad
    hide noisedistortfx
    hide minazoomdark
    with Dissolve(0.2)

    ### START OVERTRANSITION START

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    show blackover onlayer imagedrop5
    show minadadeye onlayer imagedrop6 
    show frame43 onlayer imagedrop7
    show blackover2 onlayer imagedrop8

    hide tranonereverse
    $ ClearChar()
    $ SoundOff(2.0)

    show tranone onlayer effects
    hide blackover2
    with Dissolve(0.2)

    play music1 "ninafather.mp3" fadein 1.5 volume 0.3

    ### END OVERTRANSITION START

    
    
    hide underlayc
    show underlay onlayer under
    with Dissolve(0.3)
    
    ANS """Mina, you don't know how much pain you cause me when you say things like that."""
    ANS """I love your mother more than anything in the world."""
    ANS """But to accuse your own father of lying... To accuse your own father of being a manipulator..."""
    ANS """Saying things like that makes me want to cry."""
    ANS """How could my little princess say such hurtful things? God, what did I do to deserve this!"""

    ### START OVERTRANSITION END

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    $ ClearOverframe()
    $ SoundOff(2.0)

    play music1 "scenesevenatm.mp3" fadein 2.5 volume 0.3

    show tranone onlayer imagedrop5
    hide tranonereverse
    with Dissolve(0.3)

    ### END OVERTRANSITION END
        
    hide underlay
    show underlayc onlayer under
    with Dissolve(0.3)
    
    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    play fx2 "s56now.mp3" volume 0.3
    
    MZU """(I can't let myself be consumed by these thoughts.)"""

    $ renpy.music.set_volume(1, delay=2, channel='music1')


    MZU """(...But they're starting to convince me.)"""
    
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    with Dissolve(0.2)
    
    NU """As Rex and Mina continue walking, Mina makes a startling discovery on the ground."""

    show bloodpools onlayer imagedrop6
    with Dissolve(0.5)

    NU """Dried pools of some sort of dark red liquid are scattered around."""
    
    
    
    hide underlayc
    with Dissolve(0.2)

    scene ultratowide onlayer imagedrop4
    show scenesevenmain onlayer imagedrop2
    with Dissolve(1.5)

    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1 
    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show minafaceshock onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """Rex... That's not what I think it is, right?"""
    
    $ lumafade = 0.1
    hide minafaceshock
    hide minafacedark
    show rexfacepain onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """That's dried blood, Mina."""
    
    $ lumafade = 0.1
    hide rexfacepain
    hide rexfacedark
    show minafacepain onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """Just as I thought."""
    
    $ lumafade = 0.001
    hide minafacepain
    show minafaceangry onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """But why? What's going on here?"""
    
    $ lumafade = 0.1
    hide minafaceangry
    hide minafacedark
    show rexfacepain onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """I told you earlier, scavengers often come to Section 56..."""
        
    $ lumafade = 0.1
    hide rexfacepain
    hide rexfacedark
    show minafaceangry onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """And they end up dead?"""
    
    $ lumafade = 0.1
    hide minafaceangry
    hide minafacedark
    show rexfaceserious onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """Section 56 is dangerous; what else do you want me to say?"""
    
    $ lumafade = 0.1
    hide rexfaceserious
    hide rexfacedark
    show minafaceangry onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    show tensionfx onlayer imagedrop5:
        alpha 0.2
    with Dissolve(0.5)
    
    MFW """What guarantee is there that we won't end up bleeding to death somewhere?"""
    
    $ lumafade = 0.1
    hide minafaceangry
    hide minafacedark
    show rexfacepain onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """Mina..."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide rexfacepain
    hide rexfacedark
    show minafaceshock onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    play fx3 "dumping.mp3" volume 0.3
    
    MFW """Ah!"""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    hide facebackground
    hide facedark
    hide minafaceshock
    hide minafacedark
    with Dissolve(0.2)
    
    
    hide underlayb
    hide bloodpools
    show underlay onlayer under
    with Dissolve(0.3)


    play fx2 "wetstep.mp3" volume 0.5

    show bloodpoolfresh onlayer imagedrop6
    with Dissolve(0.2)

    
    NW """Mina steps into a wet pool of blood."""
    
    
    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1 
    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show minafaceshock onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """Rex! This blood is still wet!"""
    
    $ lumafade = 0.001
    hide minafaceshock
    show minafaceangry onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """That means someone was bleeding here recently!"""
    
    $ lumafade = 0.1
    hide minafaceangry
    hide minafacedark
    show rexfaceshock onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """...You're right."""
    
    $ lumafade = 0.001
    hide rexfaceshock
    show rexfaceregret onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """We might run into them if we proceed any further."""
    
    $ lumafade = 0.001
    hide rexfaceregret
    show rexfaceserious onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """We'll be fine, though, Mina."""
    
    $ lumafade = 0.001
    hide rexfaceserious
    show rexfaceangry onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """I'll protect you if anything happens, like I always have."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    hide facebackground
    hide facedark
    hide rexfaceangry
    hide rexfacedark
    with Dissolve(0.2)
    
    
    hide underlayb
    hide tensionfx
    hide bloodpoolfresh
    show underlay onlayer under
    with Dissolve(0.3)
    
    play fx3 "radiation.mp3" volume 0.3

    NW """Mina's face suddenly turns pale."""

    $ renpy.music.set_volume(1, delay=2, channel='music1')


    NW """Rex's words fail to make any sense to Mina as she reacts to all the blood around her."""
    
    
    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1 
    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show minafacepain onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """...Rex."""
    
    hide facebackground
    hide facedark
    hide minafacepain
    hide minafacedark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)

    show sicknessfx onlayer imagedrop5:
        alpha 0.3
    with Dissolve(0.5)

    play fx1 "femalecough.mp3" volume 0.5    
    
    NW """Mina starts violently coughing into her hands."""

    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1 
    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show rexfaceshock onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """Mina!"""
    
    hide facebackground
    hide facedark
    hide rexfaceshock
    hide rexfacedark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)

    play fx3 "coughing.mp3" volume 0.5    
    
    NW """Rex also starts to feel sick."""
    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1 
    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show rexfacepain onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """...Mina, there's something off about this area. We need to move forward."""
    
    $ lumafade = 0.1
    hide rexfacepain
    hide rexfacedark
    show minafaceangry onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """Rex, look!"""
    
    hide facebackground
    hide facedark
    hide minafaceangry
    hide minafacedark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)


    show palmblood onlayer imagedrop6
    with Dissolve(0.3)

    
    NW """Mina shows Rex that her palms are covered in blood."""
    
    
    
    hide underlay
    hide palmblood
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1 
    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show minafaceangry onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """The people who came before us must have experienced the same thing."""
    
    $ lumafade = 0.001
    hide minafaceangry
    show minafacepain onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """Ugh..."""
    
    hide facebackground
    hide facedark
    hide minafacepain
    hide minafacedark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)
    

    play fx2 "grabhand.mp3" volume 0.6

    NW """Rex immediately grabs Mina's arms and rushes forward."""
    NW """...As they progress, the pools of dried blood become fewer in number."""

    hide sicknessfx
    with Dissolve(1.5)

    NW """Both Mina and Rex's symptoms start to ease a little."""
    
    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    hide underlay
    with Dissolve(0.5)

    scene widetoultra onlayer imagedrop4
    show scenesevenchar onlayer imagedrop2    
    with Dissolve(1.5)

    show underlayc onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    play fx1 "s56lore.mp3" volume 0.3

    show conflictfx onlayer imagedrop5:
        alpha 0.3
    with Dissolve(0.5)
    
    MZU """Rex... what the hell was that?"""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoompain onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """That's how Section 56 is set up—it's purposefully dangerous."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """...Huh?"""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomneutral onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Your father obviously didn't want anyone to discover what he was doing here."""
    
    $ lumafade = 0.001
    hide rexzoomneutral
    show rexzoomserious onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """So he set up traps to ensure anyone who tried to infiltrate would end up injured or sick."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomserious
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomserious onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """So you're saying the pools of blood earlier and the sickness we experienced were all some kind of trap?"""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomserious
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomserious onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Exactly."""
    
    $ lumafade = 0.001
    hide rexzoomserious
    show rexzoomangry onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """Your father likely released some sort of poison when we passed the previous area."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomangry
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomserious onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """Poison... but what about the weird symptoms we experienced earlier?"""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomserious
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomserious onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Same kind of thing."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomserious
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomangry onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """What does that mean?"""
    MZU """Sometimes it feels like you're making things up as we go."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomangry
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomangry onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """What the fuck, Mina?"""
    RZU """Why would I do that?"""
    
    $ lumafade = 0.001
    hide rexzoomangry
    show rexzoomserious onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """Stop projecting all the bullshit between you and your father onto me."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomserious
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomangry onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """It's not projection!"""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomangry
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomsad onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Do you know how hurtful it feels when you make such accusations?"""
    
    $ lumafade = 0.001
    hide rexzoomsad
    hide conflictfx
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """It makes me so fucking depressed."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomsad onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """...Alright, alright, maybe I went too far."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomsad
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomangry onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    play fx2 "minafatherhelp.mp3" volume 0.3
    
    RZU """All of this gets so exhausting..."""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomangry
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomsad onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """It wouldn't be so exhausting if you'd just be upfront with everything."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomsad
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomangry onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Mina, I told you to trust me!"""
    
    $ lumafade = 0.001
    hide rexzoomangry
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """The whole point of trust is that you don't ask unnecessary questions all the time."""
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomserious onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """Trusting me means believing I want the best for you... the best for us."""
    
    $ lumafade = 0.001
    hide rexzoomserious
    show rexzoomangry onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """Do you think I don't want the best for us?"""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomangry
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """I do... but you're sending mixed signals too."""
    
    $ lumafade = 0.001
    hide minazoompain
    show minazoomangry onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """Earlier you said this wasn't my fault but yours."""
    MZU """You were sad and moody before, and now you're aggressive and combative."""
    
    $ lumafade = 0.001
    hide minazoomangry
    show minazoomserious onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """Can you blame me for acting this way?"""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomserious
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoompain onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """...You've got a point."""
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomregret onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """I also need to be accountable for my actions."""
    
    $ lumafade = 0.001
    hide rexzoomregret
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """It's just all the stress of everything..."""
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomsad onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """I'm sorry for losing my temper."""
    
    $ lumafade = 0.001
    hide rexzoomsad
    show rexzoompain onlayer chardrop1
    show introspectfx onlayer imagedrop6:
        alpha 0.8
    show blackover2 onlayer imagedrop5:
        alpha 0.5
    with Dissolve(0.2)
    
    
    RZU """(Fuck, I might've done it now...)"""
    RZU """(This might be the last straw for Mina...)"""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    hide introspectfx
    hide blackover2
    show minazoomshadow onlayer chardrop00
    show minazoomregret onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """...Don't worry about it, Rex. Let's keep going."""
    
    $ lumafade = 0.001
    hide minazoomregret
    show minazoompain onlayer chardrop1
    show introspectfx onlayer imagedrop6:
        alpha 0.8
    show blackover2 onlayer imagedrop5:
        alpha 0.5

    with Dissolve(0.2)
    
    
    MZU """(What if my guilt over what happened with my father is clouding my judgment?)"""
    MZU """(Maybe I've been seeing red flags this entire time.)"""
    
    $ lumafade = 0.001
    hide minazoompain
    show minazoomregret onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(Or maybe I'm still clinging to the lies my father told me, just seeking revenge.)"""
    
    $ lumafade = 0.001
    hide minazoomregret
    show minazoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(I can't trust myself.)"""
    
    $ lumafade = 0.001
    hide minazoompain
    show minazoomangry onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(But I need to make a choice soon.)"""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    hide minazoomshadow
    hide minazoomangry
    hide minazoomdark
    hide introspectfx
    hide blackover2
    with Dissolve(0.2)

    play fx2 "motherinmina.mp3" volume 0.3
    
    NU """Rex begins to notice Mina's brooding demeanor."""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    show rexzoomshadow onlayer chardrop00
    show rexzoompain onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    show introspectfx onlayer imagedrop6:
        alpha 0.8
    show blackover2 onlayer imagedrop5:
        alpha 0.5

    with Dissolve(0.2)
    
    
    RZU """(Mother acted exactly like this in the days after my father went missing.)"""
    RZU """(It was as if she could tell he was dead.)"""
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomsad onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(She was simply too smart.)"""
    
    $ lumafade = 0.001
    hide rexzoomsad
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(She had it all worked out before I even caught on.)"""
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomregret onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(Who's to say Mina isn't the same?)"""
    
    $ lumafade = 0.001
    hide rexzoomregret
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(Maybe I've been underestimating Mina.)"""
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomregret onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(Maybe this plan was never going to work from the beginning.)"""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    hide rexzoomshadow
    hide rexzoomregret
    hide rexzoomdark
    hide introspectfx
    hide blackover
    with Dissolve(0.2)
    
    play fx3 "rexchoice.mp3" volume 0.3

    NU """Mina stops dead in her tracks."""

    $ renpy.music.set_volume(1, delay=2, channel='music1')

    play fx1 "crying.mp3" volume 0.5

    NU """She looks straight down at the ground."""
    
    $ lumafade = 0.1
    show rexzoomshadow onlayer chardrop00
    show rexzoomshock onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Mina, what's the matter?"""
    
    $ lumafade = 0.001
    hide rexzoomshock
    show rexzoompain onlayer chardrop1
    show introspectfx onlayer imagedrop6:
        alpha 0.8
    show blackover2 onlayer imagedrop5:
        alpha 0.5
    with Dissolve(0.2)
    
    
    RZU """(Oh fuck, oh fuck... this might be it.)"""
    RZU """(Has she finally cracked?)"""
    
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    with Dissolve(0.2)
    
    # NU """(Yeah, you shouldn't have been so secretive.)"""
    # NU """(No, she's confused, but she's still on your side.)"""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')

    hide introspectfx
    hide blackover2
    with Dissolve(1.0)


    play fx3 "redflowers.mp3" volume 0.3
    play fx1 "windgust.mp3" volume 0.5

    NU """A gust of wind echoes through the crossroads."""

    $ renpy.music.set_volume(1, delay=2, channel='music1')

    show flowersfx onlayer imagedrop5:
        alpha 0.3
    with Dissolve(0.5)

    NU """A peculiar and somewhat suffocating scent catches both Rex and Mina off-guard."""
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """That smell... that's the scent of the red flowers you've been talking about, right?"""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomregret onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """It has to be."""
    
    $ lumafade = 0.001
    hide rexzoomregret
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """Although we can't see them, I know we're only minutes away from the main area where they bloom."""
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomsad onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """...We're so close to the end, Mina. We just have to follow the scent."""

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomsad
    hide flowersfx 
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomangry onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)

    play fx1 "minachoice.mp3" volume 0.5
    

    show tensionfx onlayer imagedrop5:
        alpha 0.2
    with Dissolve(0.5)


    MZU """And what exactly is the end, Rex?"""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomangry
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomsad onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Why are you asking in such an aggressive way?"""
    
    $ lumafade = 0.001
    hide rexzoomsad
    show rexzoomhappy onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """The end means all our problems will be over."""
    RZU """I'll show you what your father has been hiding from you."""
    
    $ lumafade = 0.001
    hide rexzoomhappy
    show rexzoomlove onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """It will all make sense, and you'll know that paradise is just around the corner for us."""
    
    $ lumafade = 0.001
    hide rexzoomlove
    show rexzoomserious onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """You just have to trust me."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomserious
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomregret onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """Trust..."""
    
    $ lumafade = 0.001
    hide minazoomregret
    hide tensionfx 
    show minazoompain onlayer chardrop1
    show introspectfx onlayer imagedrop6:
        alpha 0.8
    show blackover2 onlayer imagedrop5:
        alpha 0.5

    with Dissolve(0.2)
    
    
    MZU """(This might be my last chance to get out of this.)"""
    MZU """(But abandon Rex... how could I do such a thing?)"""

    hide underlayc
    show blackover onlayer chardrop6:
        alpha 0.8
    with Dissolve(0.5)


    menu:
        "(Don't trust Rex.)":
            $ notrustrex = notrustrex + 1
            play fx2 "notrustchoice.mp3" volume 0.6
            pass
        "(Trust Rex.)":
            $ trustrex = trustrex + 1
            play fx2 "trustchoice.mp3" volume 0.3
            pass

    hide minazoomshadow
    hide minazoompain
    hide blackover
    hide minazoomdark
    with Dissolve(0.2)

    ##########
    #####
    ###
    #
    #
    # ENDING ONE: DON'T TRUST REX
    #
    #
    ##
    ###
    #####
    ##########


    if trustrex < 1:
 
        hide nulll
        show underlayb onlayer under
        with Dissolve(0.3)
        
        $ renpy.music.set_volume(0, delay=2, channel='music1')
        
        $ lumafade = 0.1
        show minastandingshadow onlayer chardrop00
        show minastandingregret onlayer chardrop1
        show minastandingdark onlayer chardrop3
        hide introspectfx
        hide blackover2
        with Dissolve(0.2)
        
        play music2 "endingonepartone.mp3" fadein 2.5 volume 0.5
        
        python:
            achievement.grant("a8")
            achievement.sync()


        MSW """Rex, I don't think I can continue."""
        
        $ lumafade = 0.001
        hide minastandingregret
        show minastandingpain onlayer chardrop1
        with Dissolve(0.2)
        
        
        MSW """The way you've been acting this entire time in Section 56 is suspicious."""
        MSW """You haven't been acting like the Rex I knew before..."""
        
        $ lumafade = 0.1
        hide minastandingshadow
        hide minastandingpain
        hide minastandingdark
        show rexstandingshadow onlayer chardrop00
        show rexstandingshock onlayer chardrop1
        show rexstandingdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RSW """What do you mean? You can't just stop!"""
        
        $ lumafade = 0.1
        hide rexstandingshadow
        hide rexstandingshock
        hide rexstandingdark
        show minastandingshadow onlayer chardrop00
        show minastandingsad onlayer chardrop1
        show minastandingdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MSW """I have a feeling that if I don't stop, something terrible is about to happen."""
        
        $ lumafade = 0.001
        hide minastandingsad
        show minastandingregret onlayer chardrop1
        with Dissolve(0.2)
        
        
        MSW """It's just unfortunate that you haven't been upfront with me this entire time."""
        
        $ lumafade = 0.001
        hide minastandingregret
        show minastandingpain onlayer chardrop1
        with Dissolve(0.2)
        
        
        MSW """Everything—the blood, the flowers, the weird health effects here..."""
        
        $ lumafade = 0.001
        hide minastandingpain
        show minastandingserious onlayer chardrop1
        with Dissolve(0.2)
        
        
        MSW """You haven't explained any of it properly!"""
        
        $ lumafade = 0.001
        hide minastandingserious
        show minastandingangry onlayer chardrop1
        with Dissolve(0.2)
        
        
        MSW """And more than that, I think you've been manipulating me this entire time!"""
        
        $ lumafade = 0.001
        hide minastandingangry
        show minastandingsad onlayer chardrop1
        with Dissolve(0.2)
        
        
        MSW """The Rex I used to know would have been honest and told me everything from the beginning."""
        
        $ lumafade = 0.001
        hide minastandingsad
        show minastandingpain onlayer chardrop1
        with Dissolve(0.2)
        
        
        MSW """It's not too late; I can make it back to the city within a day."""
        MSW """I'll just follow the path that got us here in the first place."""
        
        $ lumafade = 0.1
        hide minastandingshadow
        hide minastandingpain
        hide minastandingdark
        show rexstandingshadow onlayer chardrop00
        show rexstandingshock onlayer chardrop1
        show rexstandingdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RSW """Mina... you can't, you can't do this."""
        
        $ lumafade = 0.001
        hide rexstandingshock
        show rexstandingangry onlayer chardrop1
        with Dissolve(0.2)
        
        
        RSW """What do you mean I'm not the Rex you used to know?"""
        RSW """I'm exactly the same person today as I was yesterday!"""
        RSW """I'm telling you, Mina, you need to trust me and we'll be all right."""
        RSW """There's nothing left back home for us—we're doomed!"""
        RSW """You just can't get over those stupid fucking lies your father told you about me!"""
        RSW """He's corrupted you—he's corrupted your very ability to trust!"""
        
        $ lumafade = 0.1
        hide rexstandingshadow
        hide rexstandingangry
        hide rexstandingdark
        show minastandingshadow onlayer chardrop00
        show minastandingpain onlayer chardrop1
        show minastandingdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MSW """...He's corrupted me, that's true."""
        
        $ lumafade = 0.001
        hide minastandingpain
        show minastandingangry onlayer chardrop1
        with Dissolve(0.2)
        
        
        MSW """But this is different! You're just manipulating me!"""
        
        $ lumafade = 0.001
        hide minastandingangry
        show minastandingserious onlayer chardrop1
        with Dissolve(0.2)
        
        
        MSW """And I'm not the one who's doomed, Rex."""
        MSW """I can go home and say you murdered my father."""
        
        $ lumafade = 0.001
        hide minastandingserious
        show minastandingneutral onlayer chardrop1
        with Dissolve(0.2)
        
        
        MSW """I'll say you manipulated me and that I was helpless."""
        MSW """That you murdered my dear father in front of my eyes and tried to abduct me to Section 56."""
        
        $ lumafade = 0.1
        hide minastandingshadow
        hide minastandingneutral
        hide minastandingdark
        show rexstandingshadow onlayer chardrop00
        show rexstandingangry onlayer chardrop1
        show rexstandingdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RSW """You wouldn't say such a thing!"""
        
        $ lumafade = 0.1
        hide rexstandingshadow
        hide rexstandingangry
        hide rexstandingdark
        show minastandingshadow onlayer chardrop00
        show minastandingneutral onlayer chardrop1
        show minastandingdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MSW """I would now, Rex."""
        
        hide minastandingshadow
        hide minastandingneutral
        hide minastandingdark
        with Dissolve(0.2)
        
        
        hide underlayb
        show underlay onlayer under
        with Dissolve(0.3)

        play fx1 "running.mp3" volume 0.3
        
        NW """Rex frantically rushes toward Mina."""

        play fx2 "grabhand.mp3" volume 0.5

        NW """He grabs her by the shoulders and stares into her eyes."""

        show minacatseye onlayer imagedrop5
        with Dissolve(0.3)

        MNW """What are you going to do, Rex?"""
        NW """Rex desperately looks into Mina's eyes."""

        show minadeathstare onlayer imagedrop5
        hide minacatseye
        with Dissolve(0.3)

        MNW """Are you going to kill me, Rex?"""
        MNW """Are you going to kill me like my father killed my mother?"""

        play fx3 "swoophand.mp3" volume 0.5

    
        NW """Rex's grip on Mina loosens."""

        play fx1 "fallover.mp3" volume 0.6

        show rexdoomed onlayer imagedrop5
        hide minadeathstare
        with Dissolve(0.3)

        NW """Rex drops to the ground."""


        RNW """I'm a failure..."""

        RNW """I'm doomed to be abandoned..."""

        show minacatseye onlayer imagedrop5
        hide rexdoomed
        with Dissolve(0.3)


        NW """Mina stares at Rex with a mixture of sympathy and disgust."""
        MNW """That's what you get for lying to me, Rex."""

        show rexdoomed onlayer imagedrop5
        hide minacatseye
        with Dissolve(0.3)


        RNW """...But I didn't lie."""

        show minacatseye onlayer imagedrop5
        hide rexdoomed
        with Dissolve(0.3)

        MNW """...Whatever."""

        play fx2 "running.mp3" volume 0.3

        show minarunaway onlayer imagedrop5
        hide minacatseye
        with Dissolve(0.3)

        NW """Mina runs back toward the campsite, tears falling from her eyes."""

        show rexdoomed onlayer imagedrop5
        hide minarunaway
        with Dissolve(0.3)

        $ renpy.music.set_volume(0.1, delay=2, channel='music2')

        NW """Rex remains motionless, staring into the abyss."""

        hide rexdoomed
        with Dissolve(2)

        $ renpy.music.set_volume(1, delay=2, channel='music2')

        play music2 "endingoneparttwo.mp3" fadein 2.5 volume 0.5    

        scene blackover onlayer imagedrop2
        scene sceneonemain onlayer imagedrop3
        scene ultratowide onlayer imagedrop4
        hide minarunaway
        hide scenesevenchar
        hide scenesevenmain
        with Dissolve(4.3)


        NW """After significant effort, Mina miraculously makes it back to the entrance of Section 56."""

        show minahome onlayer imagedrop3
        hide sceneonemain
        with Dissolve(1.3)


        NW """From there, she eventually makes it back home."""
        NW """Her father's henchmen search the city to find her."""
        NW """Ironically, Mina doesn't have to lie to them about Rex killing her father."""
        NW """Someone else in her extended family takes over her deceased father's role, and life returns to normal—for everyone but Mina."""
        NW """However, the normalcy is only on the surface."""

        show minashell onlayer imagedrop3
        hide minahome
        with Dissolve(0.3)

        NW """Mina becomes a shell of her former self and often stays in her room for weeks on end."""
        NW """As the daughter of one of the most powerful mob bosses in the city, nobody bothers her."""
        NW """Everyone assumes her father's death turned her into a recluse."""
        NW """In reality, she is tormented."""
        NW """Mina agonizes over whether she made the right decision."""
        NW """Every waking thought is about what happened to Rex and whether there could have been a better solution."""


        play fx2 "lightning.mp3" volume 0.4

        show rexdeadbody onlayer imagedrop3
        show thunderfx onlayer effects
        hide minashell
        with Dissolve(0.3)

        NW """Little does Mina know, back in Section 56..."""
        NW """The carcass of Rex's body is rotting in the exact spot she last saw him."""

        hide rexdeadbody
        hide thunderfx
        with Dissolve(3)

        NW """Mina never finds out what really happened to Rex."""
        NW """...A few years pass, and Mina's reclusive state becomes the norm."""

        show minasickly onlayer imagedrop3
        show specialsicknessfx onlayer imagedrop4
        with Dissolve(1.5)

        NW """She starts to become very frail and sickly."""
        NW """Mina develops cancer."""
        NW """She is diagnosed with acute myeloid leukemia, directly caused by her short but intense time in Section 56."""
        NW """Tormented mentally by guilt over Rex, she is now tormented physically by cancer."""

        hide minasickly
        hide speicalsickness
        show flowersfx onlayer imagedrop3
        with Dissolve(1.0)

        NW """A few months after her diagnosis, Mina passes away."""
        NW """Her final thoughts are about Rex and whether a paradise awaits them in the afterlife..."""

        hide flowersfx
        hide speicalsickness
        hide underlay
        with Dissolve(2.0)

        $ ClearLayers()
        $ SoundOff(3.0)

        show endofgame onlayer backdrop1
        with Dissolve(2.0)

        pause

        return

    show underlayc onlayer under
    with Dissolve(0.2)


 
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoomsad onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """(...But I can't just abandon him.)"""
    MZU """(Honestly, I've been going back and forth on trusting him this entire time.)"""
    MZU """(I'm very suspicious, but I guess I'll let him explain himself.)"""
    MZU """(After all, we're moments away from the red flower fields.)"""
    
    $ lumafade = 0.001
    hide minazoomsad
    show minazoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(We've already come this far...)"""
    
    $ lumafade = 0.001
    hide minazoompain
    show minazoomcontent onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """(I may as well see this through.)"""
    
    hide minazoomshadow
    hide minazoomcontent
    hide minazoomdark
    with Dissolve(0.2)
    
    
    hide underlayc
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    hide minazoomshadow
    hide minazoomcontent
    hide minazoomdark
    hide introspectfx
    hide blackover2
    with Dissolve(0.2)


    $ lumafade = 0.1
    show minastandingshadow onlayer chardrop00
    show minastandingneutral onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSU """Just forget what I said... I'm just stressed out."""
    
    $ lumafade = 0.001
    hide minastandingneutral
    show minastandingpain onlayer chardrop1
    with Dissolve(0.2)
    
    
    MSU """Let's not get too worked up over these things right now."""
    
    $ lumafade = 0.001
    hide minastandingpain
    show minastandinglove onlayer chardrop1
    with Dissolve(0.2)
    
    
    MSU """We're just two idiots stuck in Section 56, right?"""
    
    $ lumafade = 0.1
    hide minastandingshadow
    hide minastandinglove
    hide minastandingdark
    show rexstandingshadow onlayer chardrop00
    show rexstandinglove onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSU """No need to overcomplicate any of this bullshit."""
    
    $ lumafade = 0.001
    hide rexstandinglove
    show rexstandingsmug onlayer chardrop1
    with Dissolve(0.2)
    
    
    RSU """It all comes down to trust, Mina—trust that I want the best for us..."""
    
    hide rexstandingshadow
    hide rexstandingsmug
    hide rexstandingdark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlayc onlayer under
    with Dissolve(0.3)
    
    RNU """Look, the fog is starting to lift, and the scent is getting stronger."""

    play fx1 "footsteps.ogg" volume 0.3

    RNU """Hey! I think I see the fields!"""


##########
#####
###
#
#
# SCENE EIGHT
#
#
##
###
#####
##########

    $ transhift = 0.167
    show tranonereverse onlayer effects
    pause 1.0

    $ SoundOff(2.0)
    $ ClearLayers()

    pause 1.0

    show frame169 onlayer imagedrop4
    show blackover onlayer imagedrop5
    show sceneeightmain onlayer imagedrop1

    NW """SECTION 56: FLOWER FIELDS"""

    scene tranone onlayer imagedrop5
    scene frame169 onlayer imagedrop4
    with Dissolve(0.5)

    play music1 "sceneeightatm.mp3" fadein 1.5 volume 0.4

    pause 1.5

    show underlay onlayer under

    pause 1.5

    python:
        achievement.grant("a9")
        achievement.sync()


    NW """Rex and Mina are taken aback once they reach the field of red flowers."""
    NW """A glowing, vibrant, endless row of red flowers blooms in front of them."""

    hide underlay
    with Dissolve(0.5)

    scene widetoultra onlayer imagedrop4
    show sceneeightchar onlayer imagedrop2:
        linear 3.0 zoom 1.1
    with Dissolve(2.5)

    pause 3.5

    show underlayb onlayer under

    pause 1.5

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')    
    
    $ lumafade = 0.1
    show rexstandingshadow onlayer chardrop00
    show rexstandingshock onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    play fx1 "redflowers.mp3" volume 0.5
    
    RSW """…This is the field, Mina!"""
    RSW """These are literally the red flowers that your father harvested and used."""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide rexstandingshadow
    hide rexstandingshock
    hide rexstandingdark
    show minastandingshadow onlayer chardrop00
    show minastandingshock onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSW """Holy shit."""
    
    hide minastandingshadow
    hide minastandingshock
    hide minastandingdark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)

    play fx2 "stumble.mp3" volume 0.4
    
    NW """Mina falls to her knees."""

    play fx3 "crying.mp3" volume 0.4


    NW """She starts to cry."""
    
    
    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1 
    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show rexfaceshock onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """Mina, what's the matter?"""
    
    $ lumafade = 0.1
    hide rexfaceshock
    hide rexfacedark
    show minafacesad onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """It's just… seeing all of this reminds me of…"""
    
    $ lumafade = 0.001
    hide minafacesad
    show minafaceregret onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """It reminds me of what could've been."""
    
    $ lumafade = 0.001
    hide minafaceregret
    show minafacepain onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """It's suffocating at times."""
    
    $ lumafade = 0.001
    hide minafacepain
    show minafaceneutral onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """…Rex, considering that we've finally reached these fields of red flowers…"""
    
    $ lumafade = 0.001
    hide minafaceneutral
    show minafaceserious onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """I think it's time we open up about everything."""
    
    $ lumafade = 0.001
    hide minafaceserious
    show minafacepain onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """We need to be honest about everything that's happened up until now."""
    
    $ lumafade = 0.001
    hide minafacepain
    show minafaceregret onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """I won't lie—I’ve been struggling to trust you this entire time."""
    
    $ lumafade = 0.001
    hide minafaceregret
    show minafacepain onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """Whether that's because of my father or something else, I can't say."""
    
    $ lumafade = 0.001
    hide minafacepain
    show minafaceserious onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """All I know is I can't deal with this conflict within myself much longer."""
    MFW """We need to get serious."""
    
    $ lumafade = 0.1
    hide minafaceserious
    hide minafacedark
    show rexfaceshock onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """…I agree, Mina."""
    
    $ lumafade = 0.1
    hide rexfaceshock
    hide rexfacedark
    show minafacelove onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """I know you do, Rex."""
    
    $ lumafade = 0.001
    hide minafacelove
    show minafaceneutral onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """So let me start by coming clean about everything on my end."""
    
    $ lumafade = 0.001
    hide minafaceneutral
    show minafaceregret onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """Things you might still not know about me and my family…"""
    
    $ lumafade = 0.001
    hide minafaceregret
    show minafaceserious onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """Then, after that, you can finally reveal the truth about these flowers and my father's plan…"""
    
    $ lumafade = 0.001
    hide minafaceserious
    show minafaceregret onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """As well as why you said we needed to come here to Section 56 in the first place."""
    
    $ lumafade = 0.1
    hide minafaceregret
    hide minafacedark
    show rexfaceserious onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """Got it. Let's do that."""
    
    $ lumafade = 0.1
    hide rexfaceserious
    hide rexfacedark
    show minafacepain onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """Alright, well…"""
    
    hide facebackground
    hide facedark
    hide minafacepain
    hide minafacedark
    with Dissolve(0.2)
    
    ### START OVERTRANSITION START

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    show blackover onlayer imagedrop5
    show motherstoryone onlayer imagedrop6 
    show frame43 onlayer imagedrop7
    show blackover2 onlayer imagedrop8

    hide tranonereverse
    $ ClearChar()
    $ SoundOff(2.0)

    show tranone onlayer effects
    hide blackover2
    with Dissolve(0.2)

    play music1 "ninafather.mp3" fadein 1.5 volume 0.3

    ### END OVERTRANSITION START

    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)
    
    MNS """Ever since I can remember, I saw my father disrespecting my mother in ways that made me sick."""
    MNS """It'll come as no surprise that my father was notorious for cheating on my mother."""
    MNS """My mother used to turn a blind eye, but I know deep down she was hurt."""
    MNS """I know you're probably thinking, What did she expect? She was the one who chose to marry a powerful criminal."""
    MNS """…But the story isn't as simple as that."""

    show motherstorytwo onlayer imagedrop6 
    with Dissolve(0.5)

    hide motherstoryone

    MNS """My mother was exploited into marrying my father; she came from a family deeply indebted to organized criminals."""
    MNS """My father saw her one night and instantly became obsessed."""
    MNS """He said my mother was going to be his wife, and that was that—no ifs or buts."""
    MNS """So, essentially, my mother was thrown into this life without any say; it was like her future had been chosen by someone else."""
    MNS """That's why I knew the cheating hurt her so much."""
    MNS """She'd already been stripped of her dignity—it was like rubbing salt into her wounds."""
    MNS """…But it didn't stop there."""

    play fx1 "punch.mp3" volume 0.5
    show violencefx onlayer imagedrop6:
        shake_effect(0.04, 10, 3)
    with Dissolve(0.2)

    MNS """My father used to beat my mother constantly."""

    hide violencefx
    hide motherstorytwo
    show minastareshock onlayer imagedrop6
    with Dissolve(0.5)

    MNS """And it all happened right in front of my eyes."""
    MNS """It was like my father wanted me to see—like he wanted to use my mother as a warning not to cross him."""
    MNS """…And it worked."""

    hide minastareshock
    show minadadeye onlayer imagedrop6
    with Dissolve(0.5)

    MNS """I grew up absolutely terrified of my father."""


    MNS """My sadness for my mother was overrun by the genuine fear I felt for my life whenever my father was around."""
    
    ### START OVERTRANSITION END

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    $ ClearOverframe()
    $ SoundOff(2.0)

    play music1 "sceneeightatm.mp3" fadein 2.5 volume 0.4

    show tranone onlayer imagedrop5
    hide tranonereverse
    with Dissolve(0.3)

    ### END OVERTRANSITION END

    
    hide underlay
    show underlayc onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """…Just talking about it… it feels like I can't breathe."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomserious onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Mina… you've never spoken so candidly about all of this."""
    
    $ lumafade = 0.001
    hide rexzoomserious
    show rexzoomregret onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """I don't know what to say."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomregret
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """That's because there really isn't much to say… It was just a terrible situation."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomsad onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """…Mina."""
    
    hide rexzoomshadow
    hide rexzoomsad
    hide rexzoomdark
    with Dissolve(0.2)
    
    ### START OVERTRANSITION START

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    show blackover onlayer imagedrop5
    show deviseplaneone onlayer imagedrop6 
    show frame43 onlayer imagedrop7
    show blackover2 onlayer imagedrop8

    hide tranonereverse
    $ ClearChar()
    $ SoundOff(2.0)

    show tranone onlayer effects
    hide blackover2
    with Dissolve(0.2)

    play music1 "escapeplan.mp3" fadein 1.5 volume 0.3

    ### END OVERTRANSITION START

    hide underlayc
    show underlay onlayer under
    with Dissolve(0.3)
    
    MNS """With everything going on, my mother was hopeless… so she devised a plan."""
    MNS """She started to spy on what my father was doing—his business plans, his extortion rackets."""
    MNS """I don't know exactly what she found, but it was huge and potentially devastating for my father."""

    show deviseplantwo onlayer imagedrop6 
    with Dissolve(0.5)

    hide deviseplaneone


    MNS """…And, as you already know, that's how my mother and your father got in contact."""
    MNS """Your dad, being a cop, had the tools necessary to build a case and take my father down."""
    MNS """…But I didn't know about any of this until afterward. At the time, I was completely ignorant of what my mother was doing."""

    show fathercloseup onlayer imagedrop5
    with Dissolve(0.5)

    MNS """During this time, my father started to catch on to the suspicious things my mother was doing."""
    MNS """…So when my father became even more suspicious…"""
    MNS """He approached me."""

    hide deviseplantwo
    with Dissolve(0.5)

    ANS """You know you can tell me anything, right? You know I love you and your mother, right?"""
    MNS """I caved to his pressure instantly."""
    MNS """…I spied on my mother and told my father everything she was doing."""
    MNS """I had no clue what he was planning to do."""
    MNS """…I just didn't want to get hurt. I didn't want him to do to me what he'd done to my mother."""
    MNS """I was such a fucking idiot."""

    show escapeplanone onlayer imagedrop6 
    with Dissolve(0.5)

    hide fathercloseup


    MNS """…And it hurts my soul to this very day that my mother was doing all of this for me."""
    MNS """She never told me the specifics. She thought I hadn't caught on."""

    show escapeplantwo onlayer imagedrop6 
    with Dissolve(0.5)

    hide escapeplanone


    MNS """…It was only when it was too late that I realized she was risking her life so I could go somewhere and live a better one."""
    MNS """A life I controlled—unlike the life my poor mother had been given."""

    play fx3 "shatter.mp3" volume 0.4
    show violencefx onlayer imagedrop6:
        shake_effect(0.04, 10, 3)
    with Dissolve(0.1)

    MNS """Once my father confronted her in the kitchen, she tried to fight back with knives."""

    hide violencefx
    hide escapeplantwo
    with Dissolve(1.0)


    MNS """…But she was no match. She just begged and begged, not for herself, but for me."""
    MNS """And that was the last I ever saw of her—until her funeral."""
    
    ### START OVERTRANSITION END

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    $ ClearOverframe()
    $ SoundOff(2.0)

    play music1 "sceneeightatm.mp3" fadein 2.5 volume 0.4

    show tranone onlayer imagedrop5
    hide tranonereverse
    with Dissolve(0.3)

    ### END OVERTRANSITION END

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    hide underlay
    show underlayc onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    play fx2 "minafatherhelp.mp3" volume 0.4

    MZU """…And the guilt I feel to this day is indescribable."""


    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide minazoompain
    show minazoomsad onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """It's what makes life unenjoyable… except for those fleeting moments."""
    
    $ lumafade = 0.001
    hide minazoomsad
    show minazoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """…I just want my mother to be alive."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomneutral onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """You can't blame yourself for your father's actions."""
    
    $ lumafade = 0.001
    hide rexzoomneutral
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """…Besides, you don't know the whole story."""
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomserious onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """Mina, I know you’ve heard little bits and pieces about me, but you haven't got the whole picture."""
    
    $ lumafade = 0.001
    hide rexzoomserious
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """Let me explain, and you'll understand why you're not to blame."""
    
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    with Dissolve(0.2)

    ### START OVERTRANSITION START

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    show blackover onlayer imagedrop5
    show fatherstoryone onlayer imagedrop6 
    show frame43 onlayer imagedrop7
    show blackover2 onlayer imagedrop8

    hide tranonereverse
    $ ClearChar()
    $ SoundOff(2.0)

    show tranone onlayer effects
    hide blackover2
    with Dissolve(0.2)

    play music1 "rexfather.mp3" fadein 1.5 volume 0.3

    ### END OVERTRANSITION START

    
    hide underlayc
    show underlay onlayer under
    with Dissolve(0.3)
    
    RNS """You need to understand that my father was a deeply, deeply flawed person."""
    RNS """It's no coincidence he ended up trying to help your mother."""
    RNS """My father was always a bit of a loner—a weirdo."""

    show fatherstorytwo onlayer imagedrop6 
    with Dissolve(0.5)

    hide fatherstoryone


    RNS """My mother was perhaps his greatest blessing."""
    RNS """To this day, I can't see what my mother saw in him—enough to marry him."""
    RNS """But all of my dad's eccentric behaviors were softened thanks to my mother's presence."""
    RNS """Because of my mother, my father made it through police training and became a cop."""
    RNS """Thanks to his job, we were able to function and survive as a family."""


    show fatherstorythree onlayer imagedrop6 
    hide fatherstorytwo
    with Dissolve(0.5)



    RNS """…Until he developed a gambling addiction."""
    RNS """He always explained his strategies as if he were a genius who’d cracked the code for infinite wealth through gambling."""
    RNS """Things took a real turn for the worse when he went into debt to feed that addiction."""

    show fathercloseup onlayer imagedrop5 
    with Dissolve(0.5)


    RNS """…So you can see he eventually got involved with your father."""
    RNS """…And borrowing money from your father came at a very steep price."""

    show minadadeye onlayer imagedrop6 
    hide fathercloseup
    with Dissolve(0.5)

    RNS """It was a price my father couldn't pay, so he cleared his debt by becoming corrupt."""
    RNS """He'd tip off your father about ongoing investigations, potential searches—things like that."""
    RNS """He hated himself for it; he felt he'd already lost all dignity by becoming a degenerate gambler."""
    RNS """Now it was worse—he was your father's slave, and he resented him more than you can imagine."""
    
    ### START OVERTRANSITION END

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    $ ClearOverframe()
    $ SoundOff(2.0)

    play music1 "sceneeightatm.mp3" fadein 2.5 volume 0.3

    show tranone onlayer imagedrop5
    hide tranonereverse
    with Dissolve(0.3)

    ### END OVERTRANSITION END
    


    hide underlay
    show underlayc onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoomshock onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """So that's why your father got involved with my father and his syndicate?"""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomshock
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomangry onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Yeah—it was because he was a useless gambler."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomangry
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomshock onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """But the whole deal with my mother?"""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomshock
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoompain onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Yeah, that's the thing…"""
    
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    with Dissolve(0.2)
    
    ### START OVERTRANSITION START

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    show blackover onlayer imagedrop5
    show rexfatherdanger onlayer imagedrop6 
    show frame43 onlayer imagedrop7
    show blackover2 onlayer imagedrop8

    hide tranonereverse
    $ ClearChar()
    $ SoundOff(2.0)

    show tranone onlayer effects
    hide blackover2
    with Dissolve(0.2)

    play music1 "escapeplan.mp3" fadein 1.5 volume 0.3

    ### END OVERTRANSITION START

    
    hide underlayc
    show underlay onlayer under
    with Dissolve(0.3)
    
    RNS """My father's resentment of your father grew every day."""
    RNS """Whenever he had to leave late at night to meet him, I could tell by his demeanor he wanted revenge."""

    show deviseplantwo onlayer imagedrop6 
    with Dissolve(0.5)

    hide rexfatherdanger


    RNS """That's where the plan with your mother began."""

    play fx1 "paper.mp3" volume 0.4

    hide deviseplantwo
    show documents onlayer imagedrop6
    with Dissolve(0.5)

    RNS """I learned some of the details from the notes and documents my father left behind after he died."""
    RNS """It turns out he eventually discovered something huge."""

    show flowersfx onlayer imagedrop5:
        alpha 0.5
    with Dissolve(0.5)

    RNS """He found out about the red-flower operation your father was running here in Section 56."""
    RNS """During that discovery, he noticed your mother was involved as well."""
    RNS """By working with her, he could build a major case to arrest your father and send him away for life."""

    hide flowersfx
    hide documents
    show rexstare onlayer imagedrop5
    with Dissolve(1.5)

    RNS """Unfortunately, he didn't realize how nosy I was about what he was doing."""
    RNS """I mainly wanted to make sure he wasn't gambling again."""

    show deviseplantwo  onlayer imagedrop5
    hide rexstare
    with Dissolve(1.0)

    RNS """When he went to meet your mother to build the case, he acted differently."""
    RNS """I could tell from his demeanor he wasn't going to meet your father—he looked hopeful."""
    RNS """…But he also had a hopeful, smug look whenever he went gambling."""

    hide deviseplantwo
    show rexstare onlayer imagedrop5
    with Dissolve(1.5)

    RNS """So, naturally, I assumed the worst."""
    RNS """I assumed he'd started gambling again."""
    RNS """I didn't want our family to fall apart—I wanted a better way."""
    RNS """So I did something incredibly stupid."""

    hide rexstare
    show rexrat onlayer imagedrop5
    with Dissolve(1.5)

    RNS """I told my father's coworkers about his behavior."""
    RNS """Considering they were police officers, I thought they'd be the best people to handle it."""
    RNS """They knew my father and his past issues."""
    RNS """But, of course, my father hadn't relapsed into gambling."""

    show fathercloseup onlayer imagedrop5
    with Dissolve(1.5)

    RNS """And little did I know, he wasn't the only crooked cop on the force."""


    RNS """When I told them I suspected he was gambling again, they looked confused at first."""
    RNS """Then they started asking for more details."""
    RNS """And I told them everything I could."""
    RNS """I thought I was giving them names of people running gambling dens in the city."""
    RNS """In reality, I was ratting out your mother and the information she had been giving my father."""
    RNS """They were smart. They feigned concern about his supposed relapse, but they knew he'd become a snitch."""

    hide rexrat
    hide fathercloseup
    with Dissolve(0.5)

    play fx2 "shotdead.mp3" volume 0.6

    show violencefx onlayer imagedrop6:
        shake_effect(0.04, 10, 3)
    with Dissolve(0.2)


    RNS """My father was murdered a week later."""
    RNS """I realized what I'd done only after he died."""

    hide violencefx
    show office onlayer imagedrop5
    with Dissolve(0.5)

    RNS """As I said earlier, I got access to his office."""

    play fx2 "paper.mp3" volume 0.6
    
    show documents onlayer imagedrop5
    with Dissolve(0.5)

    RNS """The sinking feeling I got while going through those documents…"""

    hide documents
    with Dissolve(0.5)

    RNS """I knew my actions had signed my father's death warrant."""
    RNS """…And your mother's, Mina."""
    
    ### START OVERTRANSITION END

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    $ ClearOverframe()
    $ SoundOff(2.0)

    play music1 "sceneeightatm.mp3" fadein 2.5 volume 0.4

    show tranone onlayer imagedrop5
    hide tranonereverse
    with Dissolve(0.3)

    ### END OVERTRANSITION END


    $ renpy.music.set_volume(0.1, delay=2, channel='music1')

    hide underlay
    show underlayc onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    play fx2 "rexguiltdad.mp3" volume 0.4
    
    MZU """Oh my God…"""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomangry onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Do you see what I mean, Mina?"""
    
    $ lumafade = 0.001
    hide rexzoomangry
    show rexzoomregret onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """…It's not your fault."""
    
    $ lumafade = 0.001
    hide rexzoomregret
    show rexzoomangry onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """It's my fault."""
    
    hide rexzoomshadow
    hide rexzoomangry
    hide rexzoomdark
    with Dissolve(0.2)
    
    ### START OVERTRANSITION START

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    show blackover onlayer imagedrop5
    show deviseplantwo onlayer imagedrop6 
    show violencefx onlayer imagedrop6
    show frame43 onlayer imagedrop7
    show blackover2 onlayer imagedrop8

    hide tranonereverse
    $ ClearChar()
    $ SoundOff(2.0)

    show tranone onlayer effects
    hide blackover2
    with Dissolve(0.2)

    play music1 "rexmother.mp3" fadein 1.5 volume 0.3

    ### END OVERTRANSITION START

    
    hide underlayc
    show underlay onlayer under
    with Dissolve(0.3)
    
    RNS """Your mother would be alive—my father would be alive—if it weren't for me."""


    RNS """I paid the ultimate price for my actions."""

    hide deviseplantwo
    hide violencefx
    show insertstorysix onlayer imagedrop6
    with Dissolve(1.5)
    
    RNS """The day I discovered what my father was really doing felt like being thrown off a cliff."""

    hide insertstorysix
    show rexmomhome onlayer imagedrop6
    with Dissolve(1.5)

    RNS """But what I didn't realize at the time was that my mother was thrown off the cliff with me."""


    RNS """Unfortunately for her, she didn't know how to swim."""

    show dizzyfx onlayer imagedrop6:
        alpha 0.3
    with Dissolve(1.0)

    RNS """The weeks and months after my father's death are a blur."""
    RNS """Every day was a cat-and-mouse game as I tried to fend off thoughts that could drown me for good."""
    RNS """But my mother… she just sank."""
    RNS """I always thought my father was being lifted up by my mother."""
    RNS """To my shock, it turns out my father was actually lifting her up, too."""
    RNS """My father was my mother's anchor—her rock—even despite all his flaws."""
    RNS """I tried to help: I cooked, I cleaned, I took odd jobs."""
    RNS """I never talked to her about what happened, though."""
    RNS """…I was afraid."""
    RNS """Deathly afraid she'd find out I was the cause."""
    RNS """Find out I went to my father's coworkers—became the snitch who ruined everything."""
    RNS """So I ignored it—and ignored it."""

    hide dizzyfx
    show lovefx onlayer imagedrop6:
        alpha 0.3
    with Dissolve(1.0)


    RNS """Then, suddenly, my mother started acting as though things were back to normal."""

    RNS """For a few days she went outside, did her chores, and behaved as if my father had come back to life."""
    RNS """…But soon after that…"""

    hide lovefx
    show momdeath onlayer imagedrop6
    with Dissolve(2.0)

    RNS """I found her in the living room."""

    hide momdeath
    show momdeadstool onlayer imagedrop6
    with Dissolve(1.0)

    RNS """…I couldn't."""
    RNS """…I failed—I failed everything."""
    RNS """So the price I paid was to lose everyone."""
    
    ### START OVERTRANSITION END

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    $ ClearOverframe()
    $ SoundOff(2.0)

    play music1 "sceneeightatm.mp3" fadein 2.5 volume 0.4

    show tranone onlayer imagedrop5
    hide tranonereverse
    with Dissolve(0.3)

    ### END OVERTRANSITION END



    hide underlay
    show underlayd onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show rexstandingshadow onlayer chardrop00
    show rexstandingneutral onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSS """That was my punishment."""
    
    hide rexstandingshadow
    hide rexstandingneutral
    hide rexstandingdark
    with Dissolve(0.2)
    
    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    hide underlayd
    show underlayc onlayer under
    with Dissolve(0.3)
    
    
    hide rexstandingshadow
    hide rexstandingneutral
    hide rexstandingdark
    with Dissolve(0.2)
    $ lumafade = 0.1
    show rexzoomshadow onlayer chardrop00
    show rexzoompain onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    play fx3 "rexguiltmother.mp3" volume 0.3
    
    RZU """…And just when I thought the weight of my punishment was unbearable…"""

    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomlove onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """I met you, Mina."""
    
    $ lumafade = 0.001
    hide rexzoomlove
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """Honestly, I wasn't planning to stick around much longer."""
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomhappy onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """But you put an end to that."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomhappy
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomsad onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """…Rex."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomsad
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomsad onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """…You can abandon me now—now that you know the truth."""
    
    $ lumafade = 0.001
    hide rexzoomsad
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """Now that you know it wasn't you—it was all because of me."""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoompain
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomneutral onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """You know, Rex… the way you're talking right now reminds me of when we first met…"""
    
    hide minazoomshadow
    hide minazoomneutral
    hide minazoomdark
    with Dissolve(0.2)
    
    ### START OVERTRANSITION START

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    show blackover onlayer imagedrop5
    show minastreetrex onlayer imagedrop6 
    show frame43 onlayer imagedrop7
    show blackover2 onlayer imagedrop8

    hide tranonereverse
    $ ClearChar()
    $ SoundOff(2.0)

    show tranone onlayer effects
    hide blackover2
    with Dissolve(0.2)

    play music1 "nightof.mp3" fadein 1.5 volume 0.3

    ### END OVERTRANSITION START

    hide underlayc
    show underlay onlayer under
    with Dissolve(0.3)
    
    MNS """I knew it was destiny when we first exchanged glances."""

    show rexstreetmina onlayer imagedrop6
    hide minastreetrex
    with Dissolve(0.5)

    MNS """Your father's funeral was held right next to my mother's."""

    hide rexstreetmina
    show noisedistortfx onlayer imagedrop5:
        alpha 0.3
    with Dissolve(0.5)

    MNS """My father put me in the backseat and drove right in front of your father's funeral."""

    show fathercloseup onlayer imagedrop6
    with Dissolve(0.5)

    MNS """He pointed at you from inside the car and told me—"""
    ANS """You see that guy there? His father is the reason your mother had to die."""

    hide fathercloseup
    show minastareangry onlayer imagedrop6
    with Dissolve(0.5)

    MNS """I stared at you with immense hatred…"""
    MNS """I wanted to kill you."""

    hide minastareangry
    show rexstare onlayer imagedrop6
    with Dissolve(0.5)



    MNS """I guess you caught on to my stare, because you stared back at me."""
    MNS """But your eyes didn't flinch at my intensity."""
    MNS """It felt like I could've walked up, gun in hand, and shot you right then and there."""
    MNS """And you would've done nothing—you would've just let me."""

    hide noisedistortfx
    show dizzyfx onlayer imagedrop5:
        alpha 0.3
    with Dissolve(0.5)

    MNS """That situation sent me spiraling…"""

    show rainfx onlayer effects 
    with Dissolve(0.2)

    MNS """…That's why you found me like that next to your father's grave that night."""
    MNS """I don't even remember exactly why I was there; the whole night was a blur."""
    MNS """But I think I wanted to ask your father for the truth."""

    hide dizzyfx
    hide rexstare
    show insertstorythree onlayer imagedrop6
    with Dissolve(0.5)

    MNS """Was he really the root cause of everything? Why did he want to kill my mother?"""
    MNS """And then I saw you."""

    hide insertstorythree
    show insertstoryfour onlayer imagedrop6
    with Dissolve(0.5)


    MNS """You accepted and held me despite everything I'd said earlier."""
    MNS """My hateful glances, my verbal assaults toward you and your father—"""
    MNS """You just accepted it."""
    MNS """I'd never met anyone like that before."""

    hide insertstoryfour
    show insertstorythree onlayer imagedrop6
    show lovefx onlayer imagedrop5:
        alpha 0.5
    with Dissolve(0.5)

    MNS """…So it wasn't a surprise that I fell for you. Hard."""
    MNS """My father would've never approved."""

    show sicknessfx onlayer imagedrop5:
        alpha 0.2
    with Dissolve(0.5)

    MNS """The anxiety I felt whenever we met—the rashes I'd get at the thought—"""
    MNS """But you still accepted all of it—and not only that, you embraced it."""
    MNS """That's why, Rex…"""
    
    ### START OVERTRANSITION END

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    $ ClearOverframe()
    $ SoundOff(2.0)
    hide rainfx 

    play music1 "sceneeightatm.mp3" fadein 2.5 volume 0.5

    show tranone onlayer imagedrop5
    hide tranonereverse
    with Dissolve(0.3)

    ### END OVERTRANSITION END

    
    hide underlay
    show underlayc onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoomserious onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """I can't blame you for what happened to my mother."""
    
    $ lumafade = 0.001
    hide minazoomserious
    show minazoomneutral onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """Even after everything you've told me."""
    
    $ lumafade = 0.001
    hide minazoomneutral
    show minazoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """I believe… I believe in us."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomsad onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """Do you really believe—after everything?"""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomsad
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomlove onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """…Yeah."""
    
    $ lumafade = 0.001
    hide minazoomlove
    show minazoomsmug onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """That's how I feel right now."""
    
    $ lumafade = 0.1
    hide minazoomshadow
    hide minazoomsmug
    hide minazoomdark
    show rexzoomshadow onlayer chardrop00
    show rexzoomshock onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RZU """But your father?"""
    
    $ lumafade = 0.1
    hide rexzoomshadow
    hide rexzoomshock
    hide rexzoomdark
    show minazoomshadow onlayer chardrop00
    show minazoomserious onlayer chardrop1
    show minazoomdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MZU """I don't regret a thing about what happened."""
    
    $ lumafade = 0.001
    hide minazoomserious
    show minazoomangry onlayer chardrop1
    with Dissolve(0.2)
    
    
    MZU """That fucker deserved it."""
    
    hide minazoomshadow
    hide minazoomangry
    hide minazoomdark
    with Dissolve(0.2)

    ### START OVERTRANSITION START

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    show blackover onlayer imagedrop5
    show noisedistortfx onlayer imagedrop5:
        alpha 0.5 
    show frame43 onlayer imagedrop7
    show blackover2 onlayer imagedrop8

    hide tranonereverse
    $ ClearChar()
    $ SoundOff(2.0)

    show tranone onlayer effects
    hide blackover2
    with Dissolve(0.2)

    play music1 "nightof.mp3" fadein 1.5 volume 0.3

    ### END OVERTRANSITION START


    hide underlayc
    show underlay onlayer under
    with Dissolve(0.3)
    
    MNS """I tried as hard as I could to hide our relationship."""

    show fathercloseup onlayer imagedrop6
    with Dissolve(0.5)

    MNS """But knowing my father and how controlling he was, it was only a matter of time before we were found out."""
    ANS """The son of a rat! He's a fucking son of a rat!"""
    ANS """I can't believe this—my own daughter."""
    ANS """My own daughter is a fucking whore."""

    hide noisedistortfx
    show tensionfx onlayer imagedrop5:
        alpha 0.5
    with Dissolve(0.5)

    MNS """…Shut up."""
    NS """WHAT DID YOU SAY?"""
    ANS """Listen here—you'd better shut your fucking mouth while I clean this mess up."""
    ANS """This is why I always make sure to kill the entire family—to prevent things like this from happening."""
    ANS """Why has God punished me for showing mercy?"""
    ANS """Anyway, Mina, go stay in your room."""
    ANS """And forget about that rat boyfriend of yours—he'll be buried right next to his snitch of a father very soon."""

    hide fathercloseup
    hide tensionfx
    show noisedistortfx onlayer imagedrop5:
        alpha 0.4
    show insertstorythree onlayer imagedrop6
    with Dissolve(0.5)

    MNS """…I knew I had to act fast."""
    MNS """That's why I called you immediately afterward and told you to come to my house."""
    MNS """…The one spot my father and his minions wouldn't think to search was his own tightly guarded home."""
    MNS """But getting you in was one thing—the question then was…"""

    hide insertstorythree
    show minarexstart onlayer imagedrop6
    with Dissolve(0.5)

    MNS """What do we do now?"""
    MNS """I know we weren't thinking straight, but confronting my father and getting him to accept our relationship seemed like the only option."""
    MNS """…But deep down we knew what we were really going to do."""

    play fx2 "dooropen.mp3" volume 0.3
    hide minarexstart
    show fatherroom onlayer imagedrop6
    with Dissolve(0.5)

    MNS """When we ambushed my father in his bedroom, I knew right away he wouldn't be convinced."""

    play fx1 "gunload.mp3" volume 0.3



    MNS """…Thankfully, I knew where he kept his guns."""
    MNS """So I did what I had to do."""

    play fx3 "gunshot.mp3" volume 0.3
    show violencefx onlayer imagedrop6:
        shake_effect(0.04, 10, 3)

    MNS """And it felt fucking amazing."""

    hide violencefx
    with Dissolve(2.0)

    MNS """But with my father dead, I knew we were now as good as dead, too."""
    MNS """That's why, when you suggested we run to Section 56, I knew it was our only option…"""
    
    ### START OVERTRANSITION END

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    $ ClearOverframe()
    $ SoundOff(2.0)

    play music1 "sceneeightatm.mp3" fadein 2.5 volume 0.4

    show tranone onlayer imagedrop5
    hide tranonereverse
    with Dissolve(0.3)

    ### END OVERTRANSITION END


    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)

    $ renpy.music.set_volume(0.1, delay=2, channel='music1')
    
    
    $ lumafade = 0.1
    show minastandingshadow onlayer chardrop00
    show minastandinglove onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    play fx1 "minashooting.mp3" volume 0.4
    
    MSW """…So here we are, Rex."""
    
    $ lumafade = 0.001
    hide minastandinglove
    show minastandingcontent onlayer chardrop1
    with Dissolve(0.2)
    
    $ renpy.music.set_volume(1, delay=2, channel='music1')
    
    MSW """We've made it all the way to the red flowers you've been talking about."""
    
    $ lumafade = 0.1
    hide minastandingshadow
    hide minastandingcontent
    hide minastandingdark
    show rexstandingshadow onlayer chardrop00
    show rexstandinglove onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSW """…That's right."""
    
    $ lumafade = 0.1
    hide rexstandingshadow
    hide rexstandinglove
    hide rexstandingdark
    show minastandingshadow onlayer chardrop00
    show minastandingcontent onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSW """…Ah, it feels good to let everything out."""
    
    $ lumafade = 0.001
    hide minastandingcontent
    show minastandingpain onlayer chardrop1
    with Dissolve(0.2)
    
    
    MSW """I feel like we've been holding it in this entire journey."""
    
    $ lumafade = 0.001
    hide minastandingpain
    show minastandingregret onlayer chardrop1
    with Dissolve(0.2)
    
    
    MSW """I still feel guilty… unsure about everything."""
    
    $ lumafade = 0.1
    hide minastandingshadow
    hide minastandingregret
    hide minastandingdark
    show rexstandingshadow onlayer chardrop00
    show rexstandingregret onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSW """Maybe we could've done things differently."""
    
    $ lumafade = 0.1
    hide rexstandingshadow
    hide rexstandingregret
    hide rexstandingdark
    show minastandingshadow onlayer chardrop00
    show minastandingsad onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSW """I should've just killed my father without you… all of this could've been avoided."""
    
    $ lumafade = 0.1
    hide minastandingshadow
    hide minastandingsad
    hide minastandingdark
    show rexstandingshadow onlayer chardrop00
    show rexstandingneutral onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSW """They still would've come after me, Mina."""
    
    $ lumafade = 0.1
    hide rexstandingshadow
    hide rexstandingneutral
    hide rexstandingdark
    show minastandingshadow onlayer chardrop00
    show minastandingregret onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSW """Maybe… or maybe you could've lived somewhere without me burdening you."""
    
    $ lumafade = 0.1
    hide minastandingshadow
    hide minastandingregret
    hide minastandingdark
    show rexstandingshadow onlayer chardrop00
    show rexstandingsmug onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSW """Let's carry the weight together. We'll get through this."""
    
    $ lumafade = 0.001
    hide rexstandingsmug
    show rexstandinghappy onlayer chardrop1
    with Dissolve(0.2)
    
    
    RSW """Besides, we're almost there, Mina."""
    
    $ lumafade = 0.001
    hide rexstandinghappy
    show rexstandingcontent onlayer chardrop1
    with Dissolve(0.2)
    
    
    RSW """The truth behind these red flowers—it's right over there."""
    
    $ lumafade = 0.001
    hide rexstandingcontent
    show rexstandinghappy onlayer chardrop1
    with Dissolve(0.2)
    
    
    RSW """It's inside that processing factory over there."""
    
    $ lumafade = 0.001
    hide rexstandinghappy
    show rexstandingsmug onlayer chardrop1
    with Dissolve(0.2)
    
    
    RSW """See how it's glowing?"""
    
    $ lumafade = 0.001
    hide rexstandingsmug
    show rexstandinglove onlayer chardrop1
    with Dissolve(0.2)
    
    
    RSW """That's the spot."""
    
    $ lumafade = 0.001
    hide rexstandinglove
    show rexstandingcontent onlayer chardrop1
    with Dissolve(0.2)
    
    
    RSW """That's where everything begins."""
    
    $ lumafade = 0.001
    hide rexstandingcontent
    show rexstandinghappy onlayer chardrop1
    with Dissolve(0.2)
    
    
    RSW """Inside, I'll show you how your father used these red flowers to become powerful and rule the city."""
    
    $ lumafade = 0.001
    hide rexstandinghappy
    show rexstandinglove onlayer chardrop1
    with Dissolve(0.2)
    
    
    RSW """Our solution—our ticket out of this hell—is in there."""
    
    $ lumafade = 0.1
    hide rexstandingshadow
    hide rexstandinglove
    hide rexstandingdark
    show minastandingshadow onlayer chardrop00
    show minastandinglove onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSW """…Let's go."""
    MSW """After everything we've talked about… I… I trust you, Rex."""
    
    hide minastandingshadow
    hide minastandinglove
    hide minastandingdark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)
    
    NW """Rex grabs Mina's hands."""
    RNW """Let's go."""

    play fx2 "footsteps.ogg" volume 0.4

    NW """Rex and Mina head toward the factory beside the flower fields."""


##########
#####
###
#
#
# SCENE NINE
#
#
##
###
#####
##########

    $ transhift = 0.167
    show tranonereverse onlayer effects
    pause 1.0

    $ SoundOff(2.0)
    $ ClearLayers()

    pause 1.0

    show frame169 onlayer imagedrop4
    show blackover onlayer imagedrop5
    show sceneninemain onlayer imagedrop1

    NW """SECTION 56: ABANDONED FACTORY"""

    scene tranone onlayer imagedrop5
    scene frame169 onlayer imagedrop4
    with Dissolve(0.5)

    play music1 "scenenineatm.mp3" fadein 1.5 volume 0.4

    pause 1.5

    show underlay onlayer under

    pause 1.5

    python:
        achievement.grant("a10")
        achievement.sync()


    NW """Rex and Mina begin walking through the abandoned factory."""
    NW """The walls are gigantic, and surrounding them are glowing puddles of red liquid."""
    NW """On the other end of the factory, they see a strong, vibrant red light."""

    hide underlay
    with Dissolve(0.5)

    scene widetoultra onlayer imagedrop4
    show sceneninechar onlayer imagedrop2:
        linear 3.0 zoom 1.1
    with Dissolve(0.5)

    pause 3.5
 
    hide nulll
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show rexstandingshadow onlayer chardrop00
    show rexstandinglove onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSW """You see that light at the end? That's got to be it, Mina."""
    
    $ lumafade = 0.1
    hide rexstandingshadow
    hide rexstandinglove
    hide rexstandingdark
    show minastandingshadow onlayer chardrop00
    show minastandingshock onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSW """That's the source? That's where the red flowers are processed?"""
    
    $ lumafade = 0.1
    hide minastandingshadow
    hide minastandingshock
    hide minastandingdark
    show rexstandingshadow onlayer chardrop00
    show rexstandinghappy onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSW """Pretty much."""
    
    $ lumafade = 0.001
    hide rexstandinghappy
    show rexstandingsmug onlayer chardrop1
    with Dissolve(0.2)
    
    
    RSW """We need to get to the source so I can show you the secret behind your father's power and wealth."""
    
    $ lumafade = 0.1
    hide rexstandingshadow
    hide rexstandingsmug
    hide rexstandingdark
    show minastandingshadow onlayer chardrop00
    show minastandingneutral onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSW """...Right."""
    
    hide minastandingshadow
    hide minastandingneutral
    hide minastandingdark
    with Dissolve(0.2)

    ### START OVERTRANSITION START

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    show blackover onlayer imagedrop5
    show rexstare onlayer imagedrop6 
    show frame43 onlayer imagedrop7
    show blackover2 onlayer imagedrop8

    hide tranonereverse
    $ ClearChar()
    $ SoundOff(2.0)

    show tranone onlayer effects
    hide blackover2
    with Dissolve(0.2)

    play music1 "ninafather.mp3" fadein 1.5 volume 0.3

    ### END OVERTRANSITION START

    show noisedistortfx onlayer imagedrop5:
        alpha 0.3
    with Dissolve(0.2)
    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)
    
    RNS """You can't blame yourself, Mina."""
    RNS """You can't blame yourself."""
 
    show fathercloseup onlayer imagedrop6
    hide rexstare
    with Dissolve(0.5)

    ANS """It's not your fault, Mina; your mother's actions aren't your fault."""
    ANS """Nothing bad is ever your fault... You're my little princess."""
    
    ### START OVERTRANSITION END

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    $ ClearOverframe()
    $ SoundOff(2.0)

    play music1 "scenenineatm.mp3" fadein 2.5 volume 0.4

    show tranone onlayer imagedrop5
    hide tranonereverse
    with Dissolve(0.3)

    ### END OVERTRANSITION END
    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show minastandingshadow onlayer chardrop00
    show minastandingsad onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSW """Rex... you really don't blame me for what's happened?"""
    
    $ lumafade = 0.1
    hide minastandingshadow
    hide minastandingsad
    hide minastandingdark
    show rexstandingshadow onlayer chardrop00
    show rexstandingcontent onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSW """...Mina, you need to stop asking that question."""
    
    $ lumafade = 0.001
    hide rexstandingcontent
    show rexstandinghappy onlayer chardrop1
    with Dissolve(0.2)
    
    
    RSW """I could never blame you."""
    
    $ lumafade = 0.1
    hide rexstandingshadow
    hide rexstandinghappy
    hide rexstandingdark
    show minastandingshadow onlayer chardrop00
    show minastandingregret onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSW """...Okay."""
    
    hide minastandingshadow
    hide minastandingregret
    hide minastandingdark
    with Dissolve(0.2)
    
    ### START OVERTRANSITION START

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    show blackover onlayer imagedrop5
    show rexstare onlayer imagedrop6 
    show frame43 onlayer imagedrop7
    show blackover2 onlayer imagedrop8

    hide tranonereverse
    $ ClearChar()
    $ SoundOff(2.0)

    show tranone onlayer effects
    hide blackover2
    with Dissolve(0.2)

    play music1 "ninafather.mp3" fadein 1.5 volume 0.3

    ### END OVERTRANSITION START

    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)

    show dizzyfx onlayer imagedrop5
    with Dissolve(0.2)
    
    RNS """You can leave me now, Mina."""
    RNS """You see, I'm to blame for everything, Mina."""

    show fathercloseup onlayer imagedrop6
    hide rexstare
    with Dissolve(0.5)

    ANS """Why, God? Why has God done this to me?"""

    ### START OVERTRANSITION END


    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    $ ClearOverframe()
    $ SoundOff(2.0)

    play music1 "scenenineatm.mp3" fadein 2.5 volume 0.4

    show tranone onlayer imagedrop5
    hide tranonereverse
    with Dissolve(0.3)

    ### END OVERTRANSITION END
    
    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show minastandingshadow onlayer chardrop00
    show minastandingpain onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSW """Isn't the air getting kind of thick in here?"""
    
    $ lumafade = 0.1
    hide minastandingshadow
    hide minastandingpain
    hide minastandingdark
    show rexstandingshadow onlayer chardrop00
    show rexstandinghappy onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSW """We're almost there, Mina."""
    
    $ lumafade = 0.001
    hide rexstandinghappy
    show rexstandingsmug onlayer chardrop1
    with Dissolve(0.2)
    
    
    RSW """You'll keep pushing through until the end for me, right?"""
    
    hide rexstandingshadow
    hide rexstandingsmug
    hide rexstandingdark
    with Dissolve(0.2)

    ### START OVERTRANSITION START

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    show blackover onlayer imagedrop5
    show insertstorythree onlayer imagedrop6 
    show frame43 onlayer imagedrop7
    show blackover2 onlayer imagedrop8

    hide tranonereverse
    $ ClearChar()
    $ SoundOff(2.0)

    show tranone onlayer effects
    hide blackover2
    with Dissolve(0.2)

    play music1 "rexmother.mp3" fadein 1.5 volume 0.3

    ### END OVERTRANSITION START
    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)


    
    MNS """I believe in us."""
    MNS """...That's how I feel right now."""
    MNS """How I feel right now."""

    show rexmomhome onlayer imagedrop6
    hide insertstorythree
    with Dissolve(0.5)


    DNS """I'm feeling fine right now, Rex; I'll see you when you get back."""



    DNS """I'm feeling fine right now."""
    
    ### START OVERTRANSITION END

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    $ ClearOverframe()
    $ SoundOff(2.0)

    play music1 "scenenineatm.mp3" fadein 2.5 volume 0.4

    show tranone onlayer imagedrop5
    hide tranonereverse
    with Dissolve(0.3)

    ### END OVERTRANSITION END

    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show rexstandingshadow onlayer chardrop00
    show rexstandingpain onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    show dizzyfx onlayer imagedrop5:
        alpha 0.3
    with Dissolve(0.2)
    
    
    RSW """Ugh, this area is making me a bit dizzy, too."""
    
    hide rexstandingshadow
    hide rexstandingpain
    hide rexstandingdark
    with Dissolve(0.2)


    ### START OVERTRANSITION START

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    hide dizzyfx
    show blackover onlayer imagedrop5
    show minastareshock onlayer imagedrop6 
    show frame43 onlayer imagedrop7
    show blackover2 onlayer imagedrop8

    hide tranonereverse
    $ ClearChar()
    $ SoundOff(2.0)

    show tranone onlayer effects
    hide blackover2
    with Dissolve(0.2)

    play music1 "rexmother.mp3" fadein 1.5 volume 0.3

    ### END OVERTRANSITION START

    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)
    
    show sicknessfx onlayer imagedrop5:
        alpha 0.5
    with Dissolve(0.2)

    MNS """It's suffocating."""

    show insertstorysix onlayer imagedrop6
    hide minastareshock
    with Dissolve(0.5)

    RNS """Mina, why do you keep leaving a gap?"""

    hide sicknessfx
    show conflictfx onlayer imagedrop5:
        alpha 0.5
    with Dissolve(0.5)

    RNS """Hey, where are you?"""



    RNS """Mother, I'm home... I brought some food from down the street."""

    hide conflictfx
    with Dissolve(0.5)

    RNS """Mother?"""
    

    ### START OVERTRANSITION END

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    $ ClearOverframe()
    $ SoundOff(2.0)

    play music1 "scenenineatm.mp3" fadein 2.5 volume 0.4

    show tranone onlayer imagedrop5
    hide tranonereverse
    with Dissolve(0.3)

    ### END OVERTRANSITION END

    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show rexstandingshadow onlayer chardrop00
    show rexstandingshock onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSW """...Mina, Mina, why aren't you walking next to me anymore?"""
    
    $ lumafade = 0.1
    hide rexstandingshadow
    hide rexstandingshock
    hide rexstandingdark
    show minastandingshadow onlayer chardrop00
    show minastandingpain onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSW """...Rex, I'm sorry, I'm just feeling a bit nauseous."""
    
    $ lumafade = 0.1
    hide minastandingshadow
    hide minastandingpain
    hide minastandingdark
    show rexstandingshadow onlayer chardrop00
    show rexstandingpain onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSW """Let's slow down. I don't want you to get too far away."""
    
    hide rexstandingshadow
    hide rexstandingpain
    hide rexstandingdark
    with Dissolve(0.2)

    

    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)
    
    NW """Rex stops in the middle of the factory, waiting for Mina to catch up."""
    NW """He waits for Mina to catch up."""

    ### START OVERTRANSITION START

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    show blackover onlayer imagedrop5
    show violencefx onlayer imagedrop6 
    show frame43 onlayer imagedrop7
    show blackover2 onlayer imagedrop8

    hide tranonereverse
    $ ClearChar()
    $ SoundOff(2.0)

    show tranone onlayer effects
    hide blackover2
    with Dissolve(0.2)

    play music1 "nightof.mp3" fadein 1.5 volume 0.3

    ### END OVERTRANSITION START

    show conflictfx onlayer imagedrop5:
        alpha 0.5
    with Dissolve(0.2)  

    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)


    MNS """FUCK! Rex, he's dead. What are we going to do?"""
    RNS """Mina, you know what we need to do."""
    RNS """We're both better than dead—we killed the most powerful mob boss in the city."""
    MNS """We? I was the one who killed him."""
    RNS """Mina, we need to go to Section 56."""
    MNS """Section 56? Wait, why?"""
    RNS """We have to go there, Mina; it's our only hope."""
    RNS """We need to go to Section 56."""
    
    ### START OVERTRANSITION END


    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    $ ClearOverframe()
    $ SoundOff(2.0)

    play music1 "scenenineatm.mp3" fadein 2.5 volume 0.4

    show tranone onlayer imagedrop5
    hide tranonereverse
    with Dissolve(0.3)

    ### END OVERTRANSITION END


    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show rexstandingshadow onlayer chardrop00
    show rexstandingserious onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSW """...This is where everything will be fixed."""
    
    $ lumafade = 0.001
    hide rexstandingserious
    show rexstandinghappy onlayer chardrop1
    with Dissolve(0.2)
    
    
    RSW """We'll find paradise here. This is what you wanted for us."""
    
    $ lumafade = 0.001
    hide rexstandinghappy
    show rexstandinglove onlayer chardrop1
    with Dissolve(0.2)
    
    
    RSW """Remember? You wanted this outcome, too."""
    
    hide rexstandingshadow
    hide rexstandinglove
    hide rexstandingdark
    with Dissolve(0.2)
    
    ### START OVERTRANSITION START

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    show blackover onlayer imagedrop5
    show violencefx onlayer imagedrop6 
    show frame43 onlayer imagedrop7
    show blackover2 onlayer imagedrop8

    hide tranonereverse
    $ ClearChar()
    $ SoundOff(2.0)

    show tranone onlayer effects
    hide blackover2
    with Dissolve(0.2)

    play music1 "nightof.mp3" fadein 1.5 volume 0.3

    ### END OVERTRANSITION START

    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)

    show tensionfx onlayer imagedrop5:
        alpha 0.5
    with Dissolve(0.2)  

    
    MNS """Rex! Are you there? Rex?"""
    RNS """What is it? What's going on?"""
    MNS """We've been found out."""
    MNS """I tried my best... FUCK!"""
    RNS """Okay, okay, calm down."""
    MNS """I can't... You're in serious fucking danger."""
    MNS """My father has sent his goons to kill you."""
    MNS """Come to my place as soon as you can."""
    RNS """Wait, why your place?"""
    RNS """Wouldn't it be better if I just left the city?"""
    
    $ shadowcharvar = 1
    $ shadowvar = 0.12
    $ darkcharvar = 0.95
    
    hide underlay
    show underlayd onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show rexstandingshadow onlayer chardrop00
    show rexstandingneutral onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSS """It's tough, but isn't that the best option?"""
    
    hide rexstandingshadow
    hide rexstandingneutral
    hide rexstandingdark
    with Dissolve(0.2)
    
    
    hide underlayd
    show underlay onlayer under
    with Dissolve(0.3)
    
    MNS """NO!"""
    MNS """Look, you're in danger, Rex; we can't have a big conversation right now."""
    MNS """Come to my place."""
    MNS """Right now. I'm hanging up, okay? Please come right now."""

    hide tensionfx
    with Dissolve(1.5)

    MNS """I love you."""
    
    ### START OVERTRANSITION END

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    $ ClearOverframe()
    $ SoundOff(2.0)

    play music1 "scenenineatm.mp3" fadein 2.5 volume 0.4

    show tranone onlayer imagedrop5
    hide tranonereverse
    with Dissolve(0.3)

    ### END OVERTRANSITION END

    $ shadowcharvar = 1
    $ shadowvar = 0.2
    $ darkcharvar = 0.2

    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show rexstandingshadow onlayer chardrop00
    show rexstandingsmug onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSW """We're so fucking close."""
    
    $ lumafade = 0.1
    hide rexstandingshadow
    hide rexstandingsmug
    hide rexstandingdark
    show minastandingshadow onlayer chardrop00
    show minastandingsmug onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSW """...Rex?"""
    
    hide minastandingshadow
    hide minastandingsmug
    hide minastandingdark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)
    
    NW """Mina points to a large object on the ground."""

    play fx1 "slowsteps.mp3" volume 0.5

    NW """Mina slowly walks over to get a better look."""
    
    
    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1 
    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show minafaceshock onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """What the fuck?"""
    
    hide facebackground
    hide facedark
    hide minafaceshock
    hide minafacedark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlay onlayer under
    with Dissolve(0.3)


    show deadbody onlayer imagedrop6
    with Dissolve(1.5)
    
    NW """Mina discovers the rotting body of a young male, surrounded by a pool of blood."""
    
    
    
    hide underlay
    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1 
    show facebackground onlayer chardrop00 at face_wide
    show facedark onlayer chardrop0 at face_wide
    show rexfacepain onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """...That's tragic."""
    
    $ lumafade = 0.1
    hide rexfacepain
    hide rexfacedark
    show minafaceangry onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """Why the fuck is there a dead body here, Rex?"""
    MFW """Look! The blood hasn't dried up yet!"""
    
    $ lumafade = 0.001
    hide minafaceangry
    show minafacepain onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """...He must've died recently."""
    
    $ lumafade = 0.001
    hide minafacepain
    show minafaceshock onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """It must be the scavenger from the campfire earlier!"""
    
    $ lumafade = 0.1
    hide minafaceshock
    hide minafacedark
    show rexfaceneutral onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """I think you're right, Mina."""
    
    $ lumafade = 0.001
    hide rexfaceneutral
    show rexfacepain onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """So tragic... He was duped by the myth."""
    
    $ lumafade = 0.1
    hide rexfacepain
    hide rexfacedark
    show minafaceangry onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """You're talking about the myth that there's treasure here in Section 56?"""
    
    $ lumafade = 0.1
    hide minafaceangry
    hide minafacedark
    show rexfacepain onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """Exactly."""
    
    $ lumafade = 0.001
    hide rexfacepain
    show rexfaceregret onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """It's a shame such dangerous rumors and myths spread because of what your father did here."""
    
    $ lumafade = 0.001
    hide rexfaceregret
    show rexfacepain onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """I hope he's in a better place now..."""
    
    $ lumafade = 0.1
    hide rexfacepain
    hide rexfacedark
    show minafaceangry onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """Rex, that's not the issue."""
    MFW """Why is he fucking dead?"""

    show sicknessfx onlayer imagedrop5:
        alpha 0.4
    with Dissolve(0.5)

    MFW """Does that mean the symptoms we've been experiencing are signs that we're being poisoned or something?"""
    MFW """Are we going to end up dead like this scavenger?"""
    
    $ lumafade = 0.1
    hide minafaceangry
    hide minafacedark
    show rexfaceshock onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """...Mina?"""
    
    $ lumafade = 0.1
    hide rexfaceshock
    hide rexfacedark
    show minafaceangry onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """Answer the fucking question!"""
    
    $ lumafade = 0.1
    hide minafaceangry
    hide minafacedark
    show rexfacepain onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """Mina, relax; it's just another one of your mood swings."""
    
    $ lumafade = 0.001
    hide rexfacepain
    show rexfaceneutral onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """We had an important discussion—a moment of clarity—earlier in the red flower fields."""
    
    $ lumafade = 0.001
    hide rexfaceneutral
    show rexfacepain onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """I thought we were done arguing."""
    
    $ lumafade = 0.001
    hide rexfacepain
    show rexfaceregret onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """But considering the way you acted at my father's gravesite, erratic mood swings are to be expected."""
    
    $ lumafade = 0.1
    hide rexfaceregret
    hide rexfacedark
    show minafaceangry onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """This isn't a mood swing!"""
    MFW """Stop trying to avoid the question—answer me!"""
    
    $ lumafade = 0.1
    hide minafaceangry
    hide minafacedark
    show rexfacepain onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """Alright, alright..."""
    
    $ lumafade = 0.001
    hide rexfacepain
    show rexfaceneutral onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """I told you earlier that your father purposely made Section 56 dangerous so people couldn't find out what he's doing here."""
    RFW """Simply put, the scavenger probably ate something poisonous and died because of it."""
    
    $ lumafade = 0.1
    hide rexfaceneutral
    hide rexfacedark
    show minafaceangry onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """So I just have to take your word that we haven't been poisoned like the scavenger?"""
    
    $ lumafade = 0.1
    hide minafaceangry
    hide minafacedark
    show rexfaceserious onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """No, of course not."""
    RFW """Mina, have we eaten or drunk anything the entire time we've been here?"""
    
    $ lumafade = 0.1
    hide rexfaceserious
    hide rexfacedark
    show minafaceserious onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """...No?"""
    
    $ lumafade = 0.1
    hide minafaceserious
    hide minafacedark
    show rexfacecontent onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """Exactly."""
    
    $ lumafade = 0.001
    hide rexfacecontent
    show rexfaceserious onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """I knew that doing so would likely poison us more than we could handle."""
    RFW """Mina, you remember that I have access to my father's notes and reports on Section 56, right?"""
    
    $ lumafade = 0.1
    hide rexfaceserious
    hide rexfacedark
    show minafaceserious onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """...Yeah."""
    
    $ lumafade = 0.1
    hide minafaceserious
    hide minafacedark
    show rexfacecontent onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """That's what I mean—I know more about Section 56 than any of these scavengers."""
    RFW """That's why I made sure we didn't eat or drink anything; I've done everything to ensure we're safe."""
    RFW """...Of course, we haven't been able to avoid everything, but I guarantee we're not going to end up dead."""
    
    $ lumafade = 0.001
    hide rexfacecontent
    show rexfacelove onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    hide sicknessfx
    show flowersfx onlayer imagedrop5:
        alpha 0.4
    with Dissolve(0.5)
    
    RFW """Just earlier, in the flower fields, you said you trusted me, right?"""
    
    $ lumafade = 0.1
    hide rexfacelove
    hide rexfacedark
    show minafacepain onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """...Right."""
    MFW """But I don't see why you couldn't have just told me this stuff earlier."""
    
    $ lumafade = 0.001
    hide minafacepain
    show minafaceregret onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    MFW """And to be honest, looking at this dead body, it's hard to completely believe that we're safe."""
    
    $ lumafade = 0.1
    hide minafaceregret
    hide minafacedark
    show rexfacelove onlayer chardrop1 at face_wide
    show rexfacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    RFW """Mina, just believe me. I've got this under control for us."""
    
    $ lumafade = 0.001
    hide rexfacelove
    show rexfacehappy onlayer chardrop1 at face_wide
    with Dissolve(0.2)
    
    
    RFW """Remember, your mother told you to believe."""
    
    $ lumafade = 0.1
    hide rexfacehappy
    hide rexfacedark
    show minafacepain onlayer chardrop1 at face_wide
    show minafacedark onlayer chardrop3 at face_wide
    with Dissolve(0.2)
    
    
    MFW """...I know."""
    
    hide facebackground
    hide facedark
    hide flowersfx
    hide minafacepain
    hide minafacedark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlayc onlayer under
    with Dissolve(0.3)
    
    
    hide facebackground
    hide facedark
    hide minafacepain
    hide minafacedark
    hide deadbody
    with Dissolve(0.2)
    $ lumafade = 0.1
    show minazoomshadow onlayer chardrop00
    show minazoompain onlayer chardrop1
    show minazoomdark onlayer chardrop3
    show introspectfx onlayer imagedrop6:
        alpha 0.8
    show blackover2 onlayer imagedrop5:
        alpha 0.5
    with Dissolve(0.2)
    
    
    MZU """(None of this is making any sense.)"""
    MZU """(It feels more and more like Rex is manipulating me.)"""
    MZU """(This dead body was the last straw.)"""
    MZU """(...But I know what he's saying is technically true.)"""
    MZU """(He did have the notes his father kept on this area.)"""
    MZU """(He did make sure that we didn't eat or drink anything while we were here.)"""
    MZU """(But something is definitely off, especially since the flower fields.)"""
    MZU """(Or maybe this is just self-sabotage?)"""
    
    hide minazoomshadow
    hide minazoompain
    hide minazoomdark
    with Dissolve(0.2)

    hide underlayc
    show blackover onlayer chardrop6:
        alpha 0.8
    with Dissolve(0.5)
    
    menu:
        "(Try to trust Rex.)":
            play fx1 "trustchoice.mp3" volume 0.4
            $ trustrex = trustrex + 1
            pass
        "(Try to give up on Rex.)":
            play fx1 "notrustchoice.mp3" volume 0.4
            $ notrustrex = notrustrex + 1
            pass

    
    $ lumafade = 0.1
    show rexzoomshadow onlayer chardrop00
    show rexzoomcontent onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    show underlayc onlayer under
    hide blackover 
    with Dissolve(0.2)
    
    
    RZU """(I can't believe we're almost there.)"""
    RZU """(I can almost imagine us being in paradise.)"""
    RZU """(If we've come this far, then it surely means Mina wants to go to paradise too.)"""
    
    $ lumafade = 0.001
    hide rexzoomcontent
    show rexzoompain onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(But that stupid fucking dead body...)"""
    RZU """(That dead body has potentially ruined everything...)"""
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomcontent onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(Or maybe it hasn't?)"""
    RZU """(After all, Mina told me not to run away when her father was out to kill me.)"""
    RZU """(There was a reason she wanted me to come over to her place instead of running.)"""
    RZU """(Running to another city would've meant I would be safe.)"""
    RZU """(She knew what she was doing when she told me to go to her place.)"""
    RZU """(She knew it meant we were going to kill her father.)"""
    RZU """(She knew killing her father would mean I was as good as dead.)"""
    RZU """(So of course, that means she wanted all of this to happen.)"""
    
    $ lumafade = 0.001
    hide rexzoomcontent
    show rexzoomsmug onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(Maybe she can't put it into words, but she knows it emotionally.)"""
    
    $ lumafade = 0.001
    hide rexzoomsmug
    show rexzoomlove onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(She would rather die than see me abandoned in a faraway city.)"""
    RZU """(Even if it means killing her father, even if it means dying, she wants to be with me.)"""
    
    $ lumafade = 0.001
    hide rexzoomlove
    show rexzoomcontent onlayer chardrop1
    with Dissolve(0.2)

    show lovefx onlayer imagedrop5:
        alpha 0.3
    with Dissolve(0.5)
    
    
    RZU """(Unconditional love, undying love.)"""
    RZU """(Perhaps Mina is a message sent by my mother?)"""
    RZU """(Mina exists because my mother wants to apologize for abandoning me.)"""
    
    hide rexzoomshadow
    hide rexzoomcontent
    hide rexzoomdark
    with Dissolve(0.2)
    
    ### START OVERTRANSITION START

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    hide lovefx
    hide introspectfx
    hide blackover2
    show blackover onlayer imagedrop5
    show office onlayer imagedrop6 
    show frame43 onlayer imagedrop7
    show blackover2 onlayer imagedrop8

    hide tranonereverse
    $ ClearChar()
    $ SoundOff(2.0)

    show tranone onlayer effects
    hide blackover2
    with Dissolve(0.2)

    play music1 "explanation.mp3" fadein 1.5 volume 0.4

    ### END OVERTRANSITION START

    
    hide underlayc
    show underlay onlayer under
    with Dissolve(0.3)

    show flowersfx onlayer imagedrop5:
        alpha 0.4
    with Dissolve(0.5)
    
    RNS """When I finally gained access to my father's notes and reports after he died, I was shocked by what I found."""

    show documents onlayer imagedrop6
    hide office
    with Dissolve(0.5)

    RNS """Section 56 was indeed how Mina's father gained most of his wealth and power."""


    RNS """However, the red flowers had nothing to do with it."""

    hide flowersfx
    show fathercloseup onlayer imagedrop6
    show chainfx onlayer imagedrop5:
        alpha 0.5
    with Dissolve(0.5)

    RNS """Mina's father had many connections to shady government officials."""
    RNS """It turns out that some of these officials wanted to conduct nuclear testing."""
    RNS """However, conducting major experiments with radioactive materials would be very unpopular with the public."""
    RNS """Furthermore, they wanted to keep it secret so enemy countries wouldn't find out."""
    RNS """They needed an area where they could conduct as much testing as they wanted in complete secrecy."""
    RNS """This is how the plan for Section 56 was created."""

    hide fathercloseup
    hide chainfx
    hide documents
    show skull onlayer imagedrop6
    show violencefx onlayer imagedrop5
    with Dissolve(0.5)

    RNS """Mina's father proposed forcefully clearing out an impoverished and struggling town on the outskirts of the city."""
    RNS """This meant forcefully removing, abducting, even murdering anyone in the town who wouldn't leave."""
    RNS """Estimates vary, but my father estimated that at least one hundred people were murdered for refusing to comply."""
    RNS """After the area was cleared, Mina's father would continue to provide security around it while the experiments were conducted."""
    RNS """Once the experiments finished, Mina's father would help facilitate turning the area into a dump for all the radioactive waste and materials used in the experiments."""

    hide fathercloseup
    hide skull
    hide documents
    show crown onlayer imagedrop6
    with Dissolve(0.5)

    RNS """...And all of this came with an extraordinarily large price."""
    RNS """Due to the incredibly sensitive political nature of the operation, Mina's father was paid extremely large sums of money to carry out the plan."""
    RNS """Mina's father also gained significant political power, as he could blackmail city officials by threatening to scapegoat them over Section 56."""
    RNS """Clearly, if my father and Mina's mother were able to expose what happened in Section 56, it would be catastrophic."""

    hide crown
    with Dissolve(0.5)

    RNS """It's easy to see why they were both murdered without a second thought."""
    RNS """Over the years since the experiments finished, Section 56 has contained dangerous levels of radiation."""

    show flowersfx onlayer imagedrop5
    hide violencefx
    with Dissolve(0.5)

    RNS """That's where the red flowers come into play."""
    RNS """The red flowers are a strange, mutated form of the flowers that were once native to the area."""
    RNS """Other than that, they don't serve any purpose except as a symbol of the radiation present throughout the area."""

    hide flowersfx
    show pathway onlayer imagedrop6
    with Dissolve(2.5)

    RNS """Either way, the goal here is to reach the inner sanctum of this facility."""
    RNS """The inner sanctum contains the remains of the most radioactive and lethal experiments conducted here."""
    RNS """In essence, it's the key to paradise."""
    RNS """Once I get there with Mina, the final solution to our problem will be within my grasp..."""
    RNS """I can probably take Mina there in the next five minutes or so."""
    RNS """We're already too deep inside Section 56..."""

    show sicknessfx onlayer imagedrop5:
        alpha 0.8
    with Dissolve(1.5)

    RNS """I would say we've both got an hour at most before we die from radiation poisoning."""

    show skull onlayer imagedrop6
    with Dissolve(0.3)

    RNS """We're essentially walking ghosts."""
    RNS """I did well in convincing Mina that the symptoms of radiation poisoning up until now have been nothing to worry about."""

    hide skull
    hide sicknessfx
    with Dissolve(1.5)

    RNS """Our fates are sealed; now it's just about finishing the final step..."""

    ### START OVERTRANSITION END

    $ transhift = 0.067
    show tranonereverse onlayer effects
    pause 1.0

    $ ClearOverframe()
    $ SoundOff(2.0)

    play music1 "scenenineatm.mp3" fadein 2.5 volume 0.4

    show tranone onlayer imagedrop5
    hide tranonereverse
    with Dissolve(0.3)

    ### END OVERTRANSITION END


    
    hide underlay
    show underlayc onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show rexzoomshadow onlayer chardrop00
    show rexzoompain onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    show introspectfx onlayer imagedrop6:
        alpha 0.8
    show blackover2 onlayer imagedrop5:
        alpha 0.5
    with Dissolve(0.2)
    
    
    RZU """(But before going into the inner sanctum, I need to answer a final question.)"""
    RZU """(Should I reveal the whole truth, the entire truth, to Mina?)"""
    RZU """(She told me not to run away to another city for a reason.)"""
    
    $ lumafade = 0.001
    hide rexzoompain
    show rexzoomcontent onlayer chardrop1
    with Dissolve(0.2)
    
    
    RZU """(Although she hasn't said it, her actions have proven to me that she understands.)"""
    RZU """(She knew that inviting me back and killing her father meant she wanted this.)"""
    RZU """(She wanted this suicide pact.)"""
    RZU """(Even if she doesn't consciously know that she wanted this suicide pact.)"""
    RZU """(Her soul wants to die together with me.)"""
    RZU """(So maybe revealing everything is actually a bad idea?)"""
    RZU """(Sometimes our minds can confuse what our soul yearns for.)"""
    RZU """(Explaining everything would be an unnecessary burden for what her soul really wants.)"""
    RZU """(...But what should I do?)"""
    
    hide rexzoomshadow
    hide rexzoomcontent
    hide rexzoomdark
    with Dissolve(0.2)
    
    hide underlayc
    show blackover onlayer chardrop6:
        alpha 0.8
    with Dissolve(0.5)
    
    menu:
        "(Try to explain everything to Mina.)":
            play fx1 "notrustchoice.mp3" volume 0.3
            $ notrustmina = notrustmina + 1
            pass
        "(Don't try to explain everything to Mina.)":
            play fx1 "trustchoice.mp3" volume 0.3
            $ trustmina = trustmina + 1
            pass

    
    $ lumafade = 0.1
    show rexzoomshadow onlayer chardrop00
    show rexzoomcontent onlayer chardrop1
    show rexzoomdark onlayer chardrop3
    hide blackover
    show underlayc onlayer under 
    with Dissolve(0.2)
    
    
    RZU """(Let's see how she reacts from now on...)"""
    
    hide rexzoomshadow
    hide rexzoomcontent
    hide rexzoomdark
    with Dissolve(0.2)

    ##########
    #####
    ###
    #
    #
    # ENDING TWO: DON'T TRUST REX TWO 
    #
    #
    ##
    ###
    #####
    ##########

 
    if trustrex < notrustrex:

        $ renpy.music.set_volume(0, delay=2, channel='music1')

        hide underlayc
        hide introspectfx
        hide blackover2
        show underlayc onlayer under
        with Dissolve(0.3)


        play fx2 "twostepone.mp3" volume 0.6
        play music2 "endingonepartone.mp3" fadein 2.5 volume 0.5

        show minacatseye onlayer imagedrop5
        with Dissolve(0.5)
        
        python:
            achievement.grant("a11")
            achievement.sync()



        NU """Mina steps away from the dead body and stares at Rex."""
        NU """Mina's piercing eyes cause Rex to feel a wave of anxiety."""
        
        $ lumafade = 0.1
        show minazoomshadow onlayer chardrop00
        hide minacatseye
        show minazoomserious onlayer chardrop1
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MZU """Rex, this dead body is the last straw."""
        MZU """I need you to tell me the truth, or this is over."""
        
        $ lumafade = 0.001
        hide minazoomserious
        show minazoomangry onlayer chardrop1
        with Dissolve(0.2)
        
        
        MZU """Tell me the fucking truth!"""
        
        $ lumafade = 0.1
        hide minazoomshadow
        hide minazoomangry
        hide minazoomdark
        show rexzoomshadow onlayer chardrop00
        show rexzoomshock onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """Mina... Mina, calm down."""
        
        $ lumafade = 0.1
        hide rexzoomshadow
        hide rexzoomshock
        hide rexzoomdark
        show minazoomshadow onlayer chardrop00
        show minazoomangry onlayer chardrop1
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MZU """Okay, that's it. I'm fucking done."""
        
        hide minazoomshadow
        hide minazoomangry
        hide minazoomdark
        with Dissolve(0.2)

        play fx1 "footsteps.ogg" volume 0.4
        
        NU """Mina begins walking back towards the flower fields."""
        
        $ lumafade = 0.1
        show rexzoomshadow onlayer chardrop00
        show rexzoomshock onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """Okay! Okay, stop..."""
        
        hide rexzoomshadow
        hide rexzoomshock
        hide rexzoomdark
        with Dissolve(0.2)

        show minadeathstare onlayer imagedrop5
        with Dissolve(0.5)

        
        NU """Mina stands in silence, staring at Rex."""
        
        $ lumafade = 0.1
        show rexzoomshadow onlayer chardrop00
        show rexzoompain onlayer chardrop1
        hide minadeathstare
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """Mina... if I were ever in danger, if I were ever in a hopeless scenario..."""
        
        $ lumafade = 0.001
        hide rexzoompain
        show rexzoomangry onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """Would you die for me?"""
        
        $ lumafade = 0.1
        hide rexzoomshadow
        hide rexzoomangry
        hide rexzoomdark
        show minazoomshadow onlayer chardrop00
        show minazoomshock onlayer chardrop1
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MZU """Huh?"""
        
        $ lumafade = 0.001
        hide minazoomshock
        show minazoomangry onlayer chardrop1
        with Dissolve(0.2)
        
        
        MZU """What kind of question is that?"""
        
        $ lumafade = 0.1
        hide minazoomshadow
        hide minazoomangry
        hide minazoomdark
        show rexzoomshadow onlayer chardrop00
        show rexzoomangry onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """It's a question that determines whether your love has been bullshit this entire time or not."""
        
        $ lumafade = 0.001
        hide rexzoomangry
        show rexzoompain onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """Whether our entire relationship was a lie or not..."""
        
        $ lumafade = 0.1
        hide rexzoomshadow
        hide rexzoompain
        hide rexzoomdark
        show minazoomshadow onlayer chardrop00
        show minazoomserious onlayer chardrop1
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MZU """Rex, of course I love you..."""
        
        $ lumafade = 0.001
        hide minazoomserious
        show minazoomangry onlayer chardrop1
        with Dissolve(0.2)
        
        
        MZU """But that's a really fucking weird question to ask!"""
        
        $ lumafade = 0.1
        hide minazoomshadow
        hide minazoomangry
        hide minazoomdark
        show rexzoomshadow onlayer chardrop00
        show rexzoomserious onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """Why would it be weird?"""
        RZU """You're the one who told me not to run, don't you remember?"""
        
        $ lumafade = 0.001
        hide rexzoomserious
        show rexzoomangry onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """You're the one who signed my death warrant by telling me to come to your place once our relationship was exposed."""
        RZU """You knew without a doubt that if I came over, we would be murdering your father!"""
        
        $ lumafade = 0.001
        hide rexzoomangry
        show rexzoomserious onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """Didn't you?"""
        
        $ lumafade = 0.1
        hide rexzoomshadow
        hide rexzoomserious
        hide rexzoomdark
        show minazoomshadow onlayer chardrop00
        show minazoomshock onlayer chardrop1
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MZU """What... no? What are you talking about?"""
        
        $ lumafade = 0.1
        hide minazoomshadow
        hide minazoomshock
        hide minazoomdark
        show rexzoomshadow onlayer chardrop00
        show rexzoomangry onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """Stop lying! Stop acting like your fucking father!"""
        RZU """You knew exactly what you were doing!"""
        
        $ lumafade = 0.1
        hide rexzoomshadow
        hide rexzoomangry
        hide rexzoomdark
        show minazoomshadow onlayer chardrop00
        show minazoomangry onlayer chardrop1
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MZU """I was acting just like my father? Fuck you!"""
        
        $ lumafade = 0.1
        hide minazoomshadow
        hide minazoomangry
        hide minazoomdark
        show rexzoomshadow onlayer chardrop00
        show rexzoomangry onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """Oh come on, you have no reason to get all upset like that."""
        
        $ lumafade = 0.001
        hide rexzoomangry
        show rexzoomserious onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """You still haven't answered my question."""
        
        $ lumafade = 0.001
        hide rexzoomserious
        show rexzoomneutral onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """Why didn't you tell me to run away from the city, Mina?"""
        
        $ lumafade = 0.1
        hide rexzoomshadow
        hide rexzoomneutral
        hide rexzoomdark
        show minazoomshadow onlayer chardrop00
        show minazoompain onlayer chardrop1
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MZU """I... I don't know."""
        
        $ lumafade = 0.1
        hide minazoomshadow
        hide minazoompain
        hide minazoomdark
        show rexzoomshadow onlayer chardrop00
        show rexzoomserious onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """Exactly! So you knew what you were getting yourself into when we came here!"""
        
        $ lumafade = 0.1
        hide rexzoomshadow
        hide rexzoomserious
        hide rexzoomdark
        show minazoomshadow onlayer chardrop00
        show minazoomangry onlayer chardrop1
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MZU """You're the one who suggested that we come here, not me!"""
        
        $ lumafade = 0.001
        hide minazoomangry
        show minazoomregret onlayer chardrop1
        with Dissolve(0.2)
        
        
        MZU """Look, you're right that I should've told you to run away when my father was looking for you."""
        
        $ lumafade = 0.001
        hide minazoomregret
        show minazoompain onlayer chardrop1
        with Dissolve(0.2)
        
        
        MZU """...But I couldn't stand the thought of us not being together."""
        
        $ lumafade = 0.001
        hide minazoompain
        show minazoomserious onlayer chardrop1
        with Dissolve(0.2)
        
        
        MZU """I didn't want to be alone; that's why I told you to come over instead of running away."""
        
        $ lumafade = 0.001
        hide minazoomserious
        show minazoomangry onlayer chardrop1
        with Dissolve(0.2)
        
        
        MZU """But I wasn't the one who suggested we go to Section 56 afterward!"""
        MZU """That was you!"""
        
        hide minazoomshadow
        hide minazoomangry
        hide minazoomdark
        with Dissolve(0.2)

        play fx3 "twosteptwo.mp3" volume 0.5

        show minadeathstare onlayer imagedrop5
        with Dissolve(0.5)

        
        NU """Mina takes a step towards Rex."""
        
        $ lumafade = 0.1
        show minazoomshadow onlayer chardrop00
        hide minadeathstare
        show minazoomangry onlayer chardrop1
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MZU """So I ask you one more time, tell me the truth!"""
        
        $ lumafade = 0.1
        hide minazoomshadow
        hide minazoomangry
        hide minazoomdark
        show rexzoomshadow onlayer chardrop00
        show rexzoomangry onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """Fine, you want the fucking truth?"""
        RZU """It's all bullshit, Mina, everything I've told you."""
        
        $ lumafade = 0.1
        hide rexzoomshadow
        hide rexzoomangry
        hide rexzoomdark
        show minazoomshadow onlayer chardrop00
        show minazoomshock onlayer chardrop1
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MZU """...What do you mean?"""
        
        $ lumafade = 0.1
        hide minazoomshadow
        hide minazoomshock
        hide minazoomdark
        show rexzoomshadow onlayer chardrop00
        show rexzoomangry onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """The red flowers being the source of your father's power—that's bullshit."""
        RZU """Literally everything I told you about Section 56 is a lie."""
        
        $ lumafade = 0.1
        hide rexzoomshadow
        hide rexzoomangry
        hide rexzoomdark
        show minazoomshadow onlayer chardrop00
        show minazoomangry onlayer chardrop1
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MZU """Why... why would you do that?"""
        
        $ lumafade = 0.1
        hide minazoomshadow
        hide minazoomangry
        hide minazoomdark
        show rexzoomshadow onlayer chardrop00
        show rexzoomangry onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """This entire area is a dumping ground for radioactive waste."""
        RZU """It's all thanks to some corrupt deal your father made."""
        RZU """The red flowers glow the way they do because they're mutated."""
        
        $ lumafade = 0.1
        hide rexzoomshadow
        hide rexzoomangry
        hide rexzoomdark
        show minazoomshadow onlayer chardrop00
        show minazoomangry onlayer chardrop1
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MZU """So it was all a lie!"""
        
        $ lumafade = 0.1
        hide minazoomshadow
        hide minazoomangry
        hide minazoomdark
        show rexzoomshadow onlayer chardrop00
        show rexzoomlove onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """...Not everything."""
        RZU """We can still reach paradise together; that's not a lie."""
        
        $ lumafade = 0.001
        hide rexzoomlove
        show rexzoomhappy onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """In fact, that's the whole purpose of us being here."""
        
        $ lumafade = 0.001
        hide rexzoomhappy
        show rexzoomcontent onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """When you asked me to come over to your place instead of running, do you know what you did, Mina?"""
        
        $ lumafade = 0.1
        hide rexzoomshadow
        hide rexzoomcontent
        hide rexzoomdark
        show minazoomshadow onlayer chardrop00
        show minazoomangry onlayer chardrop1
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MZU """Huh?"""
        
        $ lumafade = 0.1
        hide minazoomshadow
        hide minazoomangry
        hide minazoomdark
        show rexzoomshadow onlayer chardrop00
        show rexzoomhappy onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """You told me that you wanted to die."""
        RZU """You told me that you wanted to die together."""
        
        $ lumafade = 0.001
        hide rexzoomhappy
        show rexzoomcontent onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """You knew that once we murdered your father, I would be hunted down all over the world."""
        RZU """There would be no way I could survive."""
        
        $ lumafade = 0.001
        hide rexzoomcontent
        show rexzoomhappy onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """But you knew that when you invited me over, right?"""
        
        $ lumafade = 0.001
        hide rexzoomhappy
        show rexzoomlove onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """So it was a message of love that you were sending."""
        RZU """That you wanted to kill your father and then die with me."""
        RZU """That's why I said we needed to come here, to Section 56."""
        RZU """We'd be able to die in peace, without worrying about being hunted down."""
        RZU """Nobody would dare come here unless they wanted to die."""
        
        $ lumafade = 0.001
        hide rexzoomlove
        show rexzoomhappy onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """In fact, we're already dead!"""
        
        $ lumafade = 0.1
        hide rexzoomshadow
        hide rexzoomhappy
        hide rexzoomdark
        show minazoomshadow onlayer chardrop00
        show minazoomshock onlayer chardrop1
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MZU """Already dead?"""
        
        $ lumafade = 0.1
        hide minazoomshadow
        hide minazoomshock
        hide minazoomdark
        show rexzoomshadow onlayer chardrop00
        show rexzoomhappy onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """The flower fields are among the most radioactive parts of Section 56."""
        
        $ lumafade = 0.001
        hide rexzoomhappy
        show rexzoomlove onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """Our long chats there mean we've already been exposed to a lethal amount of radiation."""
        
        $ lumafade = 0.001
        hide rexzoomlove
        show rexzoomsmug onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """I'd say we probably have half an hour or so before we die."""
        
        $ lumafade = 0.001
        hide rexzoomsmug
        show rexzoomlove onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """So come on, Mina."""
        RZU """We're almost at paradise; let's finish the journey together."""
        RZU """I love you, Mina."""
        
        $ lumafade = 0.1
        hide rexzoomshadow
        hide rexzoomlove
        hide rexzoomdark
        show minazoomshadow onlayer chardrop00
        show minazoomshock onlayer chardrop1
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MZU """Oh my God... oh my God."""
        MZU """This can't be happening; I can't believe this is happening."""
        
        hide minazoomshadow
        hide minazoomshock
        hide minazoomdark
        with Dissolve(0.2)

        play fx2 "hyperventilation.mp3" volume 0.5

        show minahyperventilate onlayer imagedrop5
        with Dissolve(0.5)
        
        NU """Mina starts hyperventilating."""
        
        $ lumafade = 0.1
        show minazoomshadow onlayer chardrop00
        show minazoomshock onlayer chardrop1
        hide minahyperventilate
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MZU """This can't be real; this has to be a bad dream."""
        
        hide minazoomshadow
        hide minazoomshock
        hide minazoomdark
        with Dissolve(0.2)

        play fx1 "shove.mp3" volume 0.6

        show minahyperventilate onlayer imagedrop5
        with Dissolve(0.5)


        
        NU """She clenches her chest."""
        
        $ lumafade = 0.1
        show minazoomshadow onlayer chardrop00
        show minazoomshock onlayer chardrop1
        show minazoomdark onlayer chardrop3
        hide minahyperventilate
        with Dissolve(0.2)
        
        
        MZU """I've got to get the fuck out of here!"""
        
        hide minazoomshadow
        hide minazoomshock
        hide minazoomdark
        with Dissolve(0.2)

        show minaragestare onlayer imagedrop5
        with Dissolve(0.5)
        
        NU """Mina glances at Rex for a final time."""
        NU """Rage and panic fill her eyes."""
        
        $ lumafade = 0.1
        show minazoomshadow onlayer chardrop00
        show minazoomangry onlayer chardrop1
        hide minaragestare
        show specialintrospectfx onlayer imagedrop6
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MZU """You're just like my fucking father."""
        MZU """In fact, you're worse."""
        MZU """I would've killed myself too if I had a son like you."""
        
        hide minazoomshadow
        hide minazoomangry
        hide specialintrospectfx
        hide minazoomdark
        with Dissolve(0.2)

        play fx1 "running.mp3" volume 0.3

        show minarunaway onlayer imagedrop5
        with Dissolve(0.5)
        
        NU """Mina begins running out of the factory, heading towards the flower fields."""
        
        $ lumafade = 0.1
        show rexzoomshadow onlayer chardrop00
        hide minarunaway
        show rexzoomangry onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """MINA, WAIT!"""
        
        hide rexzoomshadow
        hide rexzoomangry
        hide rexzoomdark
        with Dissolve(0.2)

        play fx1 "running.mp3" volume 0.3

        show rexchase onlayer imagedrop5
        with Dissolve(0.5)

        
        NU """Rex begins to frantically run after Mina."""

        $ renpy.music.set_volume(0.1, delay=2, channel='music2')


        hide scenetenmain
        hide rexchase
        scene sceneeightmain onlayer imagedrop2
        scene ultratowide onlayer imagedrop4
        with Dissolve(4.0)

        $ renpy.music.set_volume(1, delay=2, channel='music2')


        play music2 "endingtwoparttwo.mp3" fadein 2.5 volume 0.5


        NU """For what felt like hours, but was actually only minutes, they ran through the flower fields."""


        NU """But slowly, their running pace began to slow."""

        show specialsicknessfx onlayer imagedrop5
        with Dissolve(0.3)

        NU """Extreme nausea, fatigue, and delirium take over their bodies."""
        NU """Rex tries desperately to catch up to Mina, but she's barely within his line of sight."""
        NU """Mina uses every ounce of energy left in her body to stay away from Rex."""

        play fx1 "fallover.mp3" volume 0.5

        NU """Within half an hour, both Mina and Rex no longer have the ability to move."""
        NU """They both lie on the ground, separated a fair distance away from each other."""
        NU """However, they are both within the same red flower field."""

        show minarexdying onlayer imagedrop5
        with Dissolve(0.5)

        NU """They both start foaming at the mouth and convulsing."""
        NU """Mina and Rex both die within minutes of each other."""

        show minarexdead onlayer imagedrop5
        with Dissolve(0.5)

    
        NU """Nobody ever comes looking for them."""
        NU """Nobody ever finds out what happened to them."""
        NU """As the months and years pass, their remains fully decompose and become one with the earth."""

        show blackover onlayer imagedrop6
        show frame43 onlayer imagedrop7
        show flowersfx onlayer imagedrop8
        hide minarexdead
        hide sceneeightmain
        with Dissolve(3.0)

        NU """Strange red flowers continue to bloom in Section 56."""

        $ renpy.music.set_volume(0, delay=2, channel='music2')

        hide flowersfx 
        with Dissolve(2.0)

        $ ClearLayers()
        $ SoundOff(3.0)

        show endofgame onlayer backdrop1
        with Dissolve(2.0)

        pause

        return


    ##########
    #####
    ###
    #
    #
    # ENDING THREE: DON'T TRUST MINA
    #
    #
    ##
    ###
    #####
    ##########


    if trustmina < notrustmina:
        $ renpy.music.set_volume(0, delay=2, channel='music1')

        hide underlayc
        hide introspectfx
        hide blackover2
        show underlayc onlayer under
        with Dissolve(0.3)

        play fx2 "slowsteps.mp3" volume 0.6
        play music2 "endingthreepartone.mp3" fadein 2.5 volume 0.5


        python:
            achievement.grant("a12")
            achievement.sync()


        NU """Rex starts slowly walking toward Mina."""
        NU """Mina takes her eyes off the dead body and seems confused as Rex approaches."""
        
        $ lumafade = 0.1
        show rexzoomshadow onlayer chardrop00
        show rexzoomsmug onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """Mina, do you believe that actions speak louder than words?"""
        
        hide rexzoomshadow
        hide rexzoomsmug
        hide rexzoomdark
        with Dissolve(0.2)

        show minastareshock onlayer imagedrop5
        with Dissolve(0.5)

        NU """Mina looks confused."""
        
        $ lumafade = 0.1
        show minazoomshadow onlayer chardrop00
        show minazoomshock onlayer chardrop1
        show minazoomdark onlayer chardrop3
        hide minastareshock
        with Dissolve(0.2)
        
        
        MZU """Rex, why are you asking such a weird question?"""
        MZU """Don't we need to go further to find the truth about my father?"""
        
        $ lumafade = 0.1
        hide minazoomshadow
        hide minazoomshock
        hide minazoomdark
        show rexzoomshadow onlayer chardrop00
        show rexzoomsmug onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """Of course, but I need you to answer my question first."""
        
        $ lumafade = 0.001
        hide rexzoomsmug
        show rexzoomlove onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """The question has a lot to do with the truth about what your father has been doing here."""
        
        $ lumafade = 0.1
        hide rexzoomshadow
        hide rexzoomlove
        hide rexzoomdark
        show minazoomshadow onlayer chardrop00
        show minazoomshock onlayer chardrop1
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MZU """Okay..."""
        
        $ lumafade = 0.001
        hide minazoomshock
        show minazoomserious onlayer chardrop1
        with Dissolve(0.2)
        
        
        MZU """Well, obviously it's better to judge someone based on their actions rather than their words."""
        
        $ lumafade = 0.1
        hide minazoomshadow
        hide minazoomserious
        hide minazoomdark
        show rexzoomshadow onlayer chardrop00
        show rexzoomcontent onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """Exactly."""
        RZU """Another question, Mina."""
        
        $ lumafade = 0.001
        hide rexzoomcontent
        show rexzoomhappy onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """Would you die for me?"""
        
        hide rexzoomshadow
        hide rexzoomhappy
        hide rexzoomdark
        with Dissolve(0.2)

        show minastareshock onlayer imagedrop5
        with Dissolve(0.5)

        
        NU """Mina's confusion turns into intense anxiety."""
        
        $ lumafade = 0.1
        show minazoomshadow onlayer chardrop00
        show minazoomshock onlayer chardrop1
        show minazoomdark onlayer chardrop3
        hide minastareshock
        with Dissolve(0.2)
        
        
        MZU """W-What? Die?"""
        MZU """You're not making any sense, Rex!"""
        
        $ lumafade = 0.1
        hide minazoomshadow
        hide minazoomshock
        hide minazoomdark
        show rexzoomshadow onlayer chardrop00
        show rexzoomhappy onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """It's a pretty simple question, Mina."""
        
        $ lumafade = 0.1
        hide rexzoomshadow
        hide rexzoomhappy
        hide rexzoomdark
        show minazoomshadow onlayer chardrop00
        show minazoomshock onlayer chardrop1
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MZU """Why do you want to ask such a fucked-up question right now?"""
        
        $ lumafade = 0.1
        hide minazoomshadow
        hide minazoomshock
        hide minazoomdark
        show rexzoomshadow onlayer chardrop00
        show rexzoomsmug onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """As I was saying earlier, I just wanted to confirm that you believe actions speak louder than words."""
        
        $ lumafade = 0.001
        hide rexzoomsmug
        show rexzoomlove onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """And considering you do believe your actions are more important than your words..."""
        
        $ lumafade = 0.001
        hide rexzoomlove
        show rexzoomsmug onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """I think I already have the answer to my second question."""
        
        $ lumafade = 0.001
        hide rexzoomsmug
        show rexzoomlove onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """You would die for me, right, Mina?"""
        RZU """That's what you set all of this up for, right?"""
        
        $ lumafade = 0.1
        hide rexzoomshadow
        hide rexzoomlove
        hide rexzoomdark
        show minazoomshadow onlayer chardrop00
        show minazoomshock onlayer chardrop1
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MZU """Rex, I didn't set any of this up!"""
        
        $ lumafade = 0.1
        hide minazoomshadow
        hide minazoomshock
        hide minazoomdark
        show rexzoomshadow onlayer chardrop00
        show rexzoomlove onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """But you did, Mina."""
        
        $ lumafade = 0.001
        hide rexzoomlove
        show rexzoomsmug onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """That's why you told me not to run away when we were exposed by your father."""
        
        $ lumafade = 0.001
        hide rexzoomsmug
        show rexzoomhappy onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """When your father and his henchmen were out to kill me, you told me to stay and come to your place."""
        
        $ lumafade = 0.001
        hide rexzoomhappy
        show rexzoomsmug onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """You told me to come over because you wanted to die with me, right?"""
        
        $ lumafade = 0.1
        hide rexzoomshadow
        hide rexzoomsmug
        hide rexzoomdark
        show minazoomshadow onlayer chardrop00
        show minazoomshock onlayer chardrop1
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MZU """What? No?"""
        
        $ lumafade = 0.001
        hide minazoomshock
        show minazoomregret onlayer chardrop1
        with Dissolve(0.2)
        
        
        MZU """I just didn't want to be alone..."""
        
        $ lumafade = 0.001
        hide minazoomregret
        show minazoompain onlayer chardrop1
        with Dissolve(0.2)
        
        
        MZU """I couldn't bear the thought of you running away to another city and us never seeing each other again."""
        
        $ lumafade = 0.1
        hide minazoomshadow
        hide minazoompain
        hide minazoomdark
        show rexzoomshadow onlayer chardrop00
        show rexzoomsmug onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """But isn't that essentially the same as wanting to die together?"""
        
        $ lumafade = 0.1
        hide rexzoomshadow
        hide rexzoomsmug
        hide rexzoomdark
        show minazoomshadow onlayer chardrop00
        show minazoomshock onlayer chardrop1
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MZU """No!"""
        
        $ lumafade = 0.1
        hide minazoomshadow
        hide minazoomshock
        hide minazoomdark
        show rexzoomshadow onlayer chardrop00
        show rexzoomcontent onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """This is what I meant by my question earlier, Mina."""
        RZU """Your actions speak louder than words."""
        
        $ lumafade = 0.001
        hide rexzoomcontent
        show rexzoomlove onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """You knew that if I came over to your place, we would have to kill your father, right?"""
        RZU """You knew that if we killed your father, I would be blamed for it, right?"""
        RZU """You knew that if I was blamed for killing your father, I would be hunted down no matter where I went, right?"""
        
        $ lumafade = 0.1
        hide rexzoomshadow
        hide rexzoomlove
        hide rexzoomdark
        show minazoomshadow onlayer chardrop00
        show minazoomangry onlayer chardrop1
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MZU """I didn't! None of that's true!"""
        
        $ lumafade = 0.001
        hide minazoomangry
        show minazoompain onlayer chardrop1
        with Dissolve(0.2)
        
        
        MZU """I didn't think that far ahead at all; I just wanted to be with you, Rex..."""
        
        $ lumafade = 0.1
        hide minazoomshadow
        hide minazoompain
        hide minazoomdark
        show rexzoomshadow onlayer chardrop00
        show rexzoomhappy onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """Exactly—you wanted to be with me."""
        RZU """But the only way to continue being with me after killing your father was to come here, Mina."""
        
        $ lumafade = 0.001
        hide rexzoomhappy
        show rexzoomlove onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """To come to Section 56 and die together."""
        
        $ lumafade = 0.001
        hide rexzoomlove
        show rexzoomhappy onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """The moment we killed your father, I essentially died too."""
        RZU """That's why I said let's come here."""
        RZU """Here we can end it properly—we can end everything in peace."""
        
        $ lumafade = 0.001
        hide rexzoomhappy
        show rexzoomcontent onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """We'll both go to paradise together and love each other for eternity."""
        
        hide rexzoomshadow
        hide rexzoomcontent
        hide rexzoomdark
        with Dissolve(0.2)

        show minadoom onlayer imagedrop5
        with Dissolve(0.5)
        
        NU """Mina comes to her senses and realizes something catastrophic has happened."""

        play fx3 "twostepone.mp3" volume 0.6

        NU """As she processes Rex's words, she starts to take a few steps backward."""
        
        $ lumafade = 0.1
        show minazoomshadow onlayer chardrop00
        show minazoomshock onlayer chardrop1
        show minazoomdark onlayer chardrop3
        hide minadoom
        with Dissolve(0.2)
        
        
        MZU """...Rex, you're scaring me."""
        MZU """Why are you talking about all of these things? It's confusing and scary."""
        
        $ lumafade = 0.001
        hide minazoomshock
        show minazoomangry onlayer chardrop1
        with Dissolve(0.2)
        
        
        MZU """Can you just tell me what the hell we're doing here?"""
        MZU """Was everything a lie?"""
        
        $ lumafade = 0.1
        hide minazoomshadow
        hide minazoomangry
        hide minazoomdark
        show rexzoomshadow onlayer chardrop00
        show rexzoomlove onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """Not the part about paradise."""
        
        $ lumafade = 0.001
        hide rexzoomlove
        show rexzoomsmug onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """Isn't reaching paradise the most important thing anyway?"""
        
        $ lumafade = 0.001
        hide rexzoomsmug
        show rexzoomcontent onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """The ends justify the means, no matter what they may be."""
        
        $ lumafade = 0.1
        hide rexzoomshadow
        hide rexzoomcontent
        hide rexzoomdark
        show minazoomshadow onlayer chardrop00
        show minazoomangry onlayer chardrop1
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MZU """You're not answering my question!"""
        
        $ lumafade = 0.1
        hide minazoomshadow
        hide minazoomangry
        hide minazoomdark
        show rexzoomshadow onlayer chardrop00
        show rexzoomhappy onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """Is it really necessary to say it out loud? Your actions have shown me that you wanted this."""
        
        $ lumafade = 0.1
        hide rexzoomshadow
        hide rexzoomhappy
        hide rexzoomdark
        show minazoomshadow onlayer chardrop00
        show minazoomangry onlayer chardrop1
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MZU """Rex!"""
        
        $ lumafade = 0.1
        hide minazoomshadow
        hide minazoomangry
        hide minazoomdark
        show rexzoomshadow onlayer chardrop00
        show rexzoomcontent onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """Okay, okay—relax."""
        RZU """As you already know, everything I told you about the red flowers is bullshit."""
        
        $ lumafade = 0.1
        hide rexzoomshadow
        hide rexzoomcontent
        hide rexzoomdark
        show minazoomshadow onlayer chardrop00
        show minazoomangry onlayer chardrop1
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MZU """As I already know? What the fuck!"""
        MZU """Everything you said about the red flowers is bullshit?"""
        
        $ lumafade = 0.1
        hide minazoomshadow
        hide minazoomangry
        hide minazoomdark
        show rexzoomshadow onlayer chardrop00
        show rexzoomshock onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """What? Why are you so shocked?"""
        
        $ lumafade = 0.001
        hide rexzoomshock
        show rexzoomcontent onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """Clearly, the whole thing about the red flowers was just a euphemistic way of talking about what really happened here."""
        
        $ lumafade = 0.001
        hide rexzoomcontent
        show rexzoomhappy onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """Your father gained extraordinary amounts of money and power by dumping radioactive waste, Mina."""
        RZU """This entire area was created by your father for nuclear experiments and radioactive-waste dumping."""
        RZU """He did it all to help some of the country's most corrupt officials."""
        RZU """And he became the powerful man he was because of it."""
        RZU """Didn't you already know this?"""
        
        $ lumafade = 0.001
        hide rexzoomhappy
        show rexzoomsmug onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """I mean, who would believe a story about some magical red flowers?"""
        
        $ lumafade = 0.1
        hide rexzoomshadow
        hide rexzoomsmug
        hide rexzoomdark
        show minazoomshadow onlayer chardrop00
        show minazoomshock onlayer chardrop1
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MZU """...Rex, I didn't know any of this."""
        
        $ lumafade = 0.1
        hide minazoomshadow
        hide minazoomshock
        hide minazoomdark
        show rexzoomshadow onlayer chardrop00
        show rexzoomcontent onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """You did, Mina."""
        RZU """Your heart knew all of this, but your mind didn't."""
        
        $ lumafade = 0.001
        hide rexzoomcontent
        show rexzoompain onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """That's why I was debating whether it was worth talking about all of this."""
        RZU """I didn't want to block your soul from getting what it wanted."""
        RZU """You know how your mind can sometimes be the biggest hurdle for what you really want?"""
        
        $ lumafade = 0.1
        hide rexzoomshadow
        hide rexzoompain
        hide rexzoomdark
        show minazoomshadow onlayer chardrop00
        show minazoomshock onlayer chardrop1
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MZU """...Rex, if this is a nuclear testing zone, then what's going to happen to us?"""
        
        hide minazoomshadow
        hide minazoomshock
        hide minazoomdark
        with Dissolve(0.2)

        play fx2 "hyperventilation.mp3" volume 0.3

        show minahyperventilate onlayer imagedrop5
        with Dissolve(0.5)
        
        NU """Mina experiences a sudden and intense rush of panic."""
        
        $ lumafade = 0.1
        show minazoomshadow onlayer chardrop00
        show minazoomshock onlayer chardrop1
        show minazoomdark onlayer chardrop3
        hide minahyperventilate
        with Dissolve(0.2)
        
        
        MZU """Oh my God... What's going to happen..."""
        
        $ lumafade = 0.1
        hide minazoomshadow
        hide minazoomshock
        hide minazoomdark
        show rexzoomshadow onlayer chardrop00
        show rexzoomhappy onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """We'll go to paradise together."""
        RZU """We're already pretty much there."""
        
        $ lumafade = 0.001
        hide rexzoomhappy
        show rexzoomcontent onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """And I know you're not going to abandon me like my mother."""
        
        $ lumafade = 0.1
        hide rexzoomshadow
        hide rexzoomcontent
        hide rexzoomdark
        show minazoomshadow onlayer chardrop00
        show minazoomshock onlayer chardrop1
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)


        
        
        MZU """Pretty much there? What?"""
        
        $ lumafade = 0.1
        hide minazoomshadow
        hide minazoomshock
        hide minazoomdark
        hide minahyperventilate
        show rexzoomshadow onlayer chardrop00
        show rexzoomhappy onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """The red flower field has one of the highest concentrations of radiation in Section 56."""
        
        $ lumafade = 0.001
        hide rexzoomhappy
        show rexzoomlove onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """Having our discussion there meant we were exposed to lethal amounts of radiation."""
        
        $ lumafade = 0.001
        hide rexzoomlove
        show rexzoomcontent onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """That's why we've been feeling even sicker this past hour."""
        
        $ lumafade = 0.001
        hide rexzoomcontent
        show rexzoomsmug onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """I'd say we have less than an hour before we die."""
        
        $ lumafade = 0.1
        hide rexzoomshadow
        hide rexzoomsmug
        hide rexzoomdark
        show minazoomshadow onlayer chardrop00
        show minazoomshock onlayer chardrop1
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MZU """I-I can't... I don't know what to..."""
        
        hide minazoomshadow
        hide minazoomshock
        hide minazoomdark
        with Dissolve(0.2)

        play fx2 "unsheath.mp3" volume 0.5

        show minadoom onlayer imagedrop5
        with Dissolve(0.5)
        
        NU """Rex stretches out his arm toward Mina."""
        
        $ lumafade = 0.1
        show rexzoomshadow onlayer chardrop00
        show rexzoomhappy onlayer chardrop1
        hide minadoom
        show rexzoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        RZU """We're minutes away from the final area, Mina."""
        RZU """There, we can reach paradise together."""
        
        $ lumafade = 0.001
        hide rexzoomhappy
        show rexzoomlove onlayer chardrop1
        with Dissolve(0.2)
        
        
        RZU """Let's go, Mina."""
        RZU """Mina, I love you."""
        
        hide rexzoomshadow
        hide rexzoomlove
        hide rexzoomdark
        with Dissolve(0.2)

        play fx3 "swoophand.mp3" volume 0.3        

        show minadeathstare onlayer imagedrop5
        with Dissolve(0.5)
        
        NU """Mina slaps away Rex's arm."""
        
        $ lumafade = 0.1
        show rexzoomshadow onlayer chardrop00
        show rexzoomshock onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        hide minadeathstare
        with Dissolve(0.2)
        
        
        RZU """Mina!"""
        
        $ lumafade = 0.1
        hide rexzoomshadow
        hide rexzoomshock
        hide rexzoomdark
        show minazoomshadow onlayer chardrop00
        show minazoomshock onlayer chardrop1
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MZU """You told me you wanted to die together!"""
        
        hide minazoomshadow
        hide minazoomshock
        hide minazoomdark
        with Dissolve(0.2)
        
        play fx2 "hyperventilation.mp3" volume 0.3

        NU """Mina starts hyperventilating and becomes unhinged."""
        
        $ lumafade = 0.1
        show minazoomshadow onlayer chardrop00
        show minazoomshock onlayer chardrop1
        show minazoomdark onlayer chardrop3
        with Dissolve(0.2)
        
        
        MZU """This is all a bad dream... All a bad dream."""
        
        hide minazoomshadow
        hide minazoomshock
        hide minazoomdark
        with Dissolve(0.2)

        play fx1 "shove.mp3" volume 0.6        

        show minadeathstare onlayer imagedrop5
        with Dissolve(0.5)

        
        NU """She clenches her chest."""
        
        $ lumafade = 0.1
        show minazoomshadow onlayer chardrop00
        show minazoomshock onlayer chardrop1
        show minazoomdark onlayer chardrop3
        hide minadeathstare
        with Dissolve(0.2)
        
        
        MZU """I need to get the fuck out of here... I need to fucking escape..."""
        
        hide minazoomshadow
        hide minazoomshock
        hide minazoomdark
        with Dissolve(0.2)

        show minaragestare onlayer imagedrop5
        with Dissolve(0.5)

        
        NU """Mina points her finger at Rex."""
        NU """Her eyes are filled with a mixture of depression and rage."""
        
        $ lumafade = 0.1
        show minazoomshadow onlayer chardrop00
        show minazoomangry onlayer chardrop1
        show minazoomdark onlayer chardrop3
        show specialintrospectfx onlayer imagedrop6
        hide minaragestare
        with Dissolve(0.2)
        
        
        MZU """I can't believe I trusted you... I can't believe I gave you all these chances!"""
        MZU """You're just like my father—a manipulative psychopath!"""
        MZU """No... No... You're worse!"""
        MZU """No wonder your mother killed herself."""
        MZU """It's a fucking shame she didn't take you with her!"""
        
        hide minazoomshadow
        hide specialintrospectfx
        hide minazoomangry
        hide minazoomdark
        with Dissolve(0.2)

        play fx2 "running.mp3" volume 0.3

        show minarunaway onlayer imagedrop5
        with Dissolve(0.5)
        
        NU """Mina desperately tries to escape, running toward the flower fields."""
        
        $ lumafade = 0.1
        show rexzoomshadow onlayer chardrop00
        show rexzoomangry onlayer chardrop1
        show rexzoomdark onlayer chardrop3
        hide minarunaway
        with Dissolve(0.2)

        play fx2 "running.mp3" volume 0.3
      
        
        RZU """MINA! MINA!"""

        $ renpy.music.set_volume(0, delay=2, channel='music1')
        
        hide rexzoomshadow
        hide rexzoomangry
        hide rexzoomdark
        with Dissolve(0.2)

        show blackover onlayer imagedrop6
        hide sceneninemain
        hide sceneninechar
        with Dissolve(0.5)
        
        NU """Rex chases after Mina."""

        $ renpy.music.set_volume(1, delay=2, channel='music2')

        play music2 "endingtwoparttwo.mp3" fadein 2.5 volume 0.5

        hide blackover
        scene sceneeightmain onlayer imagedrop2
        scene ultratowide onlayer imagedrop4
        with Dissolve(4.0)

        NU """For what feels like hours, but is actually only minutes, Rex chases Mina."""
        NU """However, Rex is eventually unable to keep up with Mina."""
        
        show specialsicknessfx onlayer imagedrop4
        with Dissolve(0.5)

        NU """Extreme nausea, fatigue, and delirium start to set in."""
                
        play fx1 "fallover.mp3" volume 0.6

        NU """Rex begins stumbling in the fields of red flowers, unable to see Mina anymore."""
        NU """Meanwhile, Mina desperately tries to run toward the crossroads so she can head back home."""
        NU """However, radiation poisoning sets in and both Rex and Mina are incapacitated within minutes."""

        show minarexdying onlayer imagedrop5
        with Dissolve(0.5)

        NU """Rex and Mina collapse onto the ground, far away from each other."""
        NU """However, they are both within the same red flower fields."""
        NU """They both start foaming at the mouth and convulsing."""

        show minarexdead onlayer imagedrop5
        with Dissolve(0.5)


        NU """Mina and Rex die within minutes of each other."""
        NU """Nobody ever comes looking for them."""
        NU """Nobody ever finds out what happened to them."""

        show blackover onlayer imagedrop6
        show frame43 onlayer imagedrop7
        show flowersfx onlayer imagedrop8
        hide minarexdead
        hide sceneeightmain
        with Dissolve(3.0)

        NU """As the months and years pass, their remains fully decompose and become one with the earth."""
        NU """Strange red flowers continue to bloom in Section 56."""

        $ renpy.music.set_volume(0, delay=2, channel='music2')

        hide flowersfx 
        with Dissolve(2.0)


        $ ClearLayers()
        $ SoundOff(3.0)

        show endofgame onlayer backdrop1
        with Dissolve(2.0)

        pause

        return


    ##########
    #####
    ###
    #
    #
    # ENDING FOUR: TRUST EACHOTHER
    #
    #
    ##
    ###
    #####
    ##########


    hide underlayc
    hide introspectfx
    hide blackover2
    show underlay onlayer under
    with Dissolve(0.3)
    
    NW """Mina clenches her fist and slowly walks toward Rex."""
    MNW """(I've come too far...)"""
    MNW """(Out of all the people I know, Rex is the last person who would betray me.)"""
    NW """(...I'm going to trust Rex)"""

    play fx2 "swoophand.mp3" volume 0.3

    NW """Mina silently stretches out her hand toward Rex."""

    play fx3 "hug.mp3" volume 0.5

    NW """They hold hands and begin walking slowly toward the inner sanctum of Section 56."""
    RNW """(I knew Mina wouldn't abandon me...)"""
    RNW """(My mother would be proud of Mina...)"""
    NW """In front of them is a corridor with a blinding bright red glow emanating from its depths."""
    NW """They take a step inside together."""



##########
#####
###
#
#
# SCENE TEN
#
#
##
###
#####
##########

    $ transhift = 0.167
    show tranonereverse onlayer effects
    pause 1.0

    $ SoundOff(2.0)
    $ ClearLayers()

    pause 1.0

    show frame169 onlayer imagedrop4
    show blackover onlayer imagedrop5
    show scenetenmain onlayer imagedrop1

    NW """SECTION 56: INNER SANCTUM."""

    scene tranone onlayer imagedrop5
    scene frame169 onlayer imagedrop4
    with Dissolve(0.5)

    play music1 "scenetenatm.mp3" fadein 1.5 volume 0.4

    pause 1.5

    show underlay onlayer under

    pause 1.5

    NW """Mina and Rex take slow steps toward the end of the tunnel."""

    hide underlay
    with Dissolve(0.5)

    scene widetoultra onlayer imagedrop4
    show scenetenchar onlayer imagedrop2:
        linear 3.0 zoom 1.1
    with Dissolve(0.5)

    pause 3.5

    show underlayb onlayer under
    with Dissolve(0.3)
    
    
    $ lumafade = 0.1
    show rexstandingshadow onlayer chardrop00
    show rexstandinghappy onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSW """...Mina, we're almost there."""
    RSW """At the end of the corridor is the key to your father's power."""
    
    $ lumafade = 0.001
    hide rexstandinghappy
    show rexstandingcontent onlayer chardrop1
    with Dissolve(0.2)
    
    
    RSW """You'll know how your father used the red flowers from earlier for monetary and political gain."""
    
    $ lumafade = 0.001
    hide rexstandingcontent
    show rexstandinglove onlayer chardrop1
    with Dissolve(0.2)
    
    
    RSW """You'll also find out how those red flowers are going to be the ultimate solution for us."""
    
    $ lumafade = 0.001
    hide rexstandinglove
    show rexstandingcontent onlayer chardrop1
    with Dissolve(0.2)
    
    
    RSW """...We're about to reach paradise."""
    
    $ lumafade = 0.1
    hide rexstandingshadow
    hide rexstandingcontent
    hide rexstandingdark
    show minastandingshadow onlayer chardrop00
    show minastandingpain onlayer chardrop1
    show minastandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    MSW """...Paradise."""
    MSW """...So all the answers are just at the end of that corridor?"""
    
    $ lumafade = 0.1
    hide minastandingshadow
    hide minastandingpain
    hide minastandingdark
    show rexstandingshadow onlayer chardrop00
    show rexstandinglove onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(0.2)
    
    
    RSW """Exactly—you'll understand when we're there."""
    
    $ lumafade = 0.001
    hide rexstandinglove
    show rexstandingcontent onlayer chardrop1
    with Dissolve(0.2)
    
    
    RSW """It's hard to explain with words—you'll just know when you see it."""
    
    hide rexstandingshadow
    hide rexstandingcontent
    hide rexstandingdark
    with Dissolve(0.2)
    
    
    hide underlayb
    show underlayc onlayer under
    with Dissolve(0.3)

    show blackover onlayer imagedrop6

    
    RNU """Are you ready, Mina?"""
    MNU """...Yes."""

    play fx1 "slowsteps.mp3" volume 0.4    

    $ renpy.music.set_volume(0, delay=2, channel='music1')

    NU """Rex and Mina slowly walk toward the end of the corridor."""

    hide scenetenmain

    play music2 "endingfourpartone.mp3" fadein 2.5 volume 0.5

    hide blackover
    scene sanctumdoor onlayer imagedrop2
    with Dissolve(2.0)



    NU """They find a huge sealed door with a small latch on the side."""
    RNU """It's just behind this door, Mina."""
    MNU """...Okay."""

    play fx2 "swoophand.mp3" volume 0.5


    RNU """Mina, grab my hand."""

    play fx1 "grabhand.mp3" volume 0.5

    NU """Mina grabs Rex's hand as he slowly places it on the latch."""

    $ renpy.music.set_volume(0, delay=2, channel='music2')


    RNU """Three... Two... One..."""

    play fx3 "openlatch.mp3" volume 0.7

    hide sanctumdoor
    with Dissolve(0.2)


    NU """Rex opens the latch."""

    show bluelight onlayer imagedrop2
    with Dissolve(0.1)

    play music3 "endingfourparttwo.mp3" fadein 2.5 volume 0.5


    NU """A blinding blue light immediately fills the entire area."""
    NU """Rex and Mina are blinded as the blue light slowly begins to fade."""
    NU """Behind the sealed door is a room with what appears to be melted materials."""
    NU """One of the materials looks like a gigantic foot."""

    play fx1 "slowsteps.mp3" volume 0.5


    NU """They slowly walk inside."""
    NU """However, all the cuts and scrapes from their journey begin to rupture."""
    NU """Blood slowly trickles over their bodies, and their eyes start to become bloodshot."""
    RNU """This... This is paradise, Mina."""
    MNU """...Paradise?"""

    show specialsicknessfx onlayer imagedrop3
    with Dissolve(2.0)

    NU """Rex and Mina notice their minds starting to slow down."""
    NU """Suddenly, every step, every movement, feels incredibly heavy."""

    show minabackstare onlayer imagedrop5
    with Dissolve(0.5)

    NU """Mina has a distressed and confused look on her face."""

    show rexdoomstare onlayer imagedrop5
    hide minabackstare
    with Dissolve(0.5)


    RNU """...You believe... right?"""

    show minabackstare onlayer imagedrop5
    hide rexdoomstare
    with Dissolve(0.5)

    NU """Mina hesitates for a moment."""
    MNU """.....Yes"""

    show rexdoomstare onlayer imagedrop5
    hide minabackstare
    with Dissolve(0.5)

    NU """She stares deeply into Rex's eyes."""

    hide rexdoomstare
    with Dissolve(0.5)

    show coverart onlayer imagedrop3
    with Dissolve(3.0)

    python:
            achievement.grant("a13")
            achievement.sync()


    NU """As if she has given up, Mina uses her last ounce of energy to grab onto Rex."""
    MNU """....Rex"""
    NU """Both Mina and Rex turn pale."""
    NU """Their muscles begin to twitch uncontrollably."""

    play fx2 "fallover.mp3" volume 0.6

    scene blackover2 onlayer imagedrop4
    show minarexdyingspecial onlayer imagedrop5
    with Dissolve(2.5)

    NU """They fall to the ground."""
    
    
    hide underlayc
    show underlayb onlayer under
    with Dissolve(0.3)
    
    $ shadowcharvar = 0.99
    $ darkcharvar = 0.99

    $ lumafade = 0.1
    show rexstandingshadow onlayer chardrop00
    show rexstandingneutral onlayer chardrop1
    show rexstandingdark onlayer chardrop3
    with Dissolve(1.5)
    
    
    RSU """...Mina."""
    
    hide rexstandingshadow
    hide rexstandingneutral
    hide rexstandingdark
    with Dissolve(1.5)
    
    
    hide underlayb
    show underlayc onlayer under
    with Dissolve(0.3)

    play fx2 "bloodrupture.mp3" volume 0.6

    show violencefx onlayer imagedrop5
    with Dissolve(2.0)

    
    NU """Both Mina and Rex experience internal organ hemorrhaging."""

    $ renpy.music.set_volume(0, delay=2, channel='music3')

    NU """At this stage, their bodies are so weak they can't even feel pain."""

    NU """Soon, their breathing begins to slow."""

    play music3 "endingfourpartthree.mp3" fadein 2.5 volume 0.5

    $ renpy.music.set_volume(1, delay=2, channel='music3')

    hide violencefx
    hide minarexdyingspecial
    with Dissolve(1.5)

    NU """Nobody ever finds their bodies."""
    NU """Section 56 remains untouched."""

    show flowersfx onlayer imagedrop6
    with Dissolve(1.5)

    NU """Strange red flowers continue to bloom in Section 56."""

    hide flowersfx
    with Dissolve(1.5)


    $ ClearLayers()
    $ SoundOff(2.0)

    show endofgame onlayer backdrop1
    with Dissolve(2.0)

    pause

    return




