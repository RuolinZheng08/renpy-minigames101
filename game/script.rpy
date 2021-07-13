define e = Character("Eileen")

label start:
    scene bg room
    e "Let's play a rhythm game!"
    call screen rhythm_game(
        'audio/music-by-tallbeard.wav', 
        'audio/music-by-tallbeard.beatmap.txt'
        )

    e "Wasn't that fun?"

    return
