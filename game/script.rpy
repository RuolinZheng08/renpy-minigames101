define e = Character("Eileen")

label start:
    scene bg room
    e "Let's play a rhythm game!"
    call screen rhythm_game(
        'audio/my-music.mp3', 
        'audio/my-music.beatmap.txt'
        )

    e "Wasn't that fun?"

    return
