define e = Character("Eileen")

label start:
    scene bg room
    e "Let's play a rhythm game!"
    call screen rhythm_game()

    e "Wasn't that fun?"

    return
