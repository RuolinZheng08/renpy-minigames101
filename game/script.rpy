define e = Character("Eileen")

label start:
    scene bg room
    e "Let's play a rhythm game!"

    # start the rhythm game
    # window hide
    $ quick_menu = False

    # avoid rolling back and losing game state
    $ renpy.block_rollback()
    
    call screen rhythm_game(
        'audio/music-by-tallbeard.wav', 
        'audio/music-by-tallbeard.beatmap.txt'
        )
    # avoid rolling back and entering the game again
    $ renpy.block_rollback()

    # restore rollback from this point on
    $ renpy.checkpoint()

    $ quick_menu = True
    window show

    $ num_hits, num_notes = _return
    e "You hit [num_hits] notes out of [num_notes]. Good work!"

    return
