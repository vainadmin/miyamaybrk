################################################################################
## Initialization
################################################################################

init offset = -1

####
##
## Talkback Setup
##
######


init python:
    import functools
    def beepy_voice(event, 
                    interact=True, 
                    beepfile="hanatalk.mp3",
                    speakerstyle="nostyle", 
                    **kwargs):

        # This is true if the dialogue causes an interaction to occur
        # if not interact:
        #    return

        #print(renpy.get_say_attributes())


        print("beepy_voice_triggered")
        print(f"beepy_voice: event >>>>{event}><<<<")
        print(f"Who: {say_who} Saying: {say_what}, Style: {speakerstyle}")

        #if speakerstyle is "minanarrationultra":
        #    renpy.show("tranonereverse", layer='effects', what=None)


        if event == "begin":
            print(f"Music File: {beepfile}")
            print("begin begin")
            renpy.music.play(beepfile, channel="talk", loop=True, fadein=0.1)
        elif event == "show_done":
            print("show done show done")
            # renpy.music.set_pause(False, channel="talk")
            renpy.music.set_volume(0.8, delay=0.1, channel='talk')
            if (
                "narrat" not in speakerstyle
                and (
                    "rex" in speakerstyle
                    or "mina" in speakerstyle
                )
            ):
                if "widemouth" in speakerstyle:
                    renpy.show(speakerstyle, layer='chardrop2', at_list=[face_wide])
                elif "standardmouth" in speakerstyle:
                    renpy.show(speakerstyle, layer='chardrop2', at_list=[face_standard])
                else:
                    renpy.show(speakerstyle, layer='chardrop2', what=None)
        elif event == "slow_done":
            print("slow done slow done")
            renpy.music.set_volume(0, delay=0.1, channel='talk')
            if (
                "narrat" not in speakerstyle
                and (
                    "rex" in speakerstyle
                    or "mina" in speakerstyle
                )
            ):
                renpy.hide(speakerstyle, layer='chardrop2')
        elif event == "end":
            print("end end end")
            renpy.music.stop(channel="talk", fadeout=0.1)

####
##
## Audio Channel Setup 
##
######

# Create the talk and SFX/BGM channel
init python:
    renpy.music.register_channel("talk", 
                                "voice", 
                                loop=True, 
                                stop_on_mute=True, 
                                tight=False, 
                                file_prefix='', 
                                file_suffix='', 
                                buffer_queue=True, 
                                movie=False, 
                                framedrop=True)

    renpy.music.register_channel("music1", 
                                "music", 
                                loop=True, 
                                stop_on_mute=False, 
                                tight=True, 
                                file_prefix='', 
                                file_suffix='', 
                                buffer_queue=True, 
                                movie=False, 
                                framedrop=True)

    renpy.music.register_channel("music2", 
                                "music", 
                                loop=True, 
                                stop_on_mute=False, 
                                tight=True, 
                                file_prefix='', 
                                file_suffix='', 
                                buffer_queue=True, 
                                movie=False, 
                                framedrop=True)

    renpy.music.register_channel("music3", 
                                "music", 
                                loop=True, 
                                stop_on_mute=False, 
                                tight=True, 
                                file_prefix='', 
                                file_suffix='', 
                                buffer_queue=True, 
                                movie=False, 
                                framedrop=True)

    renpy.music.register_channel("music4", 
                                "music", 
                                loop=True, 
                                stop_on_mute=False, 
                                tight=True, 
                                file_prefix='', 
                                file_suffix='', 
                                buffer_queue=True, 
                                movie=False, 
                                framedrop=True)

    renpy.music.register_channel("fx1", 
                                "sound", 
                                loop=False, 
                                stop_on_mute=False, 
                                tight=True, 
                                file_prefix='', 
                                file_suffix='', 
                                buffer_queue=True, 
                                movie=False, 
                                framedrop=True)

    renpy.music.register_channel("fx2", 
                                "sound", 
                                loop=False, 
                                stop_on_mute=False, 
                                tight=True, 
                                file_prefix='', 
                                file_suffix='', 
                                buffer_queue=True, 
                                movie=False, 
                                framedrop=True)

    renpy.music.register_channel("fx3", 
                                "sound", 
                                loop=False, 
                                stop_on_mute=False, 
                                tight=True, 
                                file_prefix='', 
                                file_suffix='', 
                                buffer_queue=True, 
                                movie=False, 
                                framedrop=True)