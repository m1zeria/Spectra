# The script of the game goes in this file.

# Characters. Colors will be set once we have a palette.
define m = Character("Morphia", color="#b8a0d0")
define you = Character("You", color="#e0e0e0")
define you2 = Character("You", color="#c0a080")


# Chapter 1 — The Dreamer's Rest

label chapter_1:

    # Show the clinic interior. Placeholder for now.
    scene bg clinic

    # Narration.
    "You wake up on a cot you do not recognize."
    "The ceiling is low. There is a window with bars, and beyond it a lamppost with a flickering bulb. The hum is everywhere. You have heard it your whole life, or someone has."
    "There is a woman sitting in the chair across from you. She is small and very still. She is looking at you as if in an attempt to look into your soul."
    "She wears a mask of white porcelain from the bridge of her nose to her forehead. Her eyes, only just visible, are pale, almost colorless."
    "She does not ask who you are."

    # Show Morphia. Placeholder.
    show morphia neutral

    m "You're awake."
    m "That's good. The last one was awake for about four minutes. You've been here for two hours."


    # CHOICE — HOW DO YOU RESPOND

    menu:

        "Admit you don't know where you are.":
            you "I don't know where I am."
            m "No. You don't."
            "She does not seem surprised. She writes something in a small notebook on her knee."
            m "That's the third time you've said that today. It's the first time you've said it in that voice, though."

        "Bluff. Pretend you remember.":
            you "I remember. I was just resting my eyes."
            m "You weren't."
            "She does not look up from her notebook."
            m "You were gone. All of you were gone. That's not resting."

        "Say nothing. Wait.":
            "You do not answer."
            "Morphia waits. She is very good at waiting. The hum fills the room. The bulb outside flickers, steadies, flickers again."
            "After a long moment, she sets the notebook down."
            m "Alright. We can do it your way."

        "Let whoever is behind you answer.":
            "You feel the words arrive before you decide to say them. That happens sometimes. You have never been sure what to call it."
            you2 "How long have I been here."
            "That is not your voice. Morphia hears it. She looks up, sharp, and for a moment you see her eyes go wide beneath the mask."
            m "Oh."
            m "You're not the one I was speaking to."
            "The room does not change. You do. The light from the window is different. The hum is different. The notebook on her knee is different, and it is the same notebook, and you have never seen it before and you have been looking at it for an hour."
            "You are not Light anymore. You are the one who was listening underneath."
            # Switch fronting alter.
            show morphia alert


    "Morphia stands. She moves to the window, and she does not turn back to face you when she speaks."
    m "I run a clinic here. People come to me when their dreams stop working. When they can't sleep, or when they sleep too much, or when they sleep and something else is there with them."
    m "Someone brought you in last night. They didn't leave a name. They left you on the cot and they left."


    # CHOICE — WHAT DO YOU ASK

    menu:

        "Who brought me in?":
            m "I don't know. They were wearing a green coat. That's all I saw."

        "What's wrong with me?":
            m "That's the wrong question."
            m "Nothing is wrong with you. Something is happening to you. There's a difference. I'm trying to find out which."

        "Can you help me?":
            "She is quiet for a moment. Then she turns, and looks at you, and you can see her eyes are not pale now. They are white. Blank. Luminous."
            "She is looking at something past you."
            m "I can try."
            m "I've been trying for two hours. You're the first mind I've ever failed to read."

        "Say nothing.":
            "She waits. She is patient. She has been patient for years."
            m "That's alright. You don't have to talk."
            m "I'll talk. You can listen."


    "Morphia sits back down. She folds her hands in her lap."
    m "I'm going to try something. It won't hurt. It might feel strange."
    m "I'm going to look at you. Not at your face. At the part of you that dreams."
    m "If you want me to stop, say stop. If you can't say stop, that's alright too. I'll know."
    "She closes her eyes. Her breath slows. The hum gets louder, or it seems to."
    "Nothing happens."
    "Nothing keeps happening."
    "Then her eyes open. They are white. She is looking at something that is not in the room. She is looking at something that is not in the waking world."
    "And then her eyes go normal, and she blinks, and she looks at you with an expression you cannot read because half her face is covered."
    # Morphia's read state. Placeholder for the white-eyed portrait.
    show morphia reading
    m "Huh."
    m "That's new."
    show morphia neutral


    # CHOICE — HOW DO YOU REACT TO THE FAILED READ

    menu:

        "Ask what she saw.":
            m "Nothing. That's the problem. I looked, and there was nothing to see, and there was also too much to see."
            m "I don't have a word for it. I don't think one exists yet."

        "Ask if you're broken.":
            m "No."
            "She says it fast. Faster than she meant to."
            m "No. Different is not broken. I would know."

        "Ask if she's going to turn you in.":
            m "To who?"
            m "If I turned in everyone I couldn't read, I'd have no patients at all."
            m "I'd also be dead. The Sanitarium does not like me."

        "Say nothing.":
            "She does not push. She simply waits, and the waiting is not a test. It is a courtesy."


    "Morphia stands. She crosses to the shelf and takes down a small glass vial, half full of something dark and shifting, and she holds it up to the lamplight."
    m "I need to tell you something. It's not about you. It's about everyone."
    m "Every patient I see, every dream I enter, every mind I touch. They all have the same dream. It started six months ago. It has not stopped."
    m "A light that consumes everything. Not bright. Not warm. Just white. And everything it touches stops being anything."
    "She sets the vial down."
    m "I don't know what it is. I have a guess. I don't like it."


    # CHOICE — HOW DO YOU RESPOND TO THE NIGHTMARE

    menu:

        "Ask her what her guess is.":
            m "I think it's something that was never supposed to happen."
            m "I think it's the opposite of everything the gods were. I think it's the end of the spectrum."
            m "I hope I'm wrong."

        "Tell her you've had the dream too.":
            m "Have you."
            "She says it very quietly. She sits down across from you again, and she looks at you, really looks, and something in her face changes."
            m "That's the first time anyone has said that."
            m "I've been carrying this alone for six months."

        "Say you don't care about dreams.":
            m "You will."
            "She does not say it coldly. She says it like a fact about the weather."

        "Say nothing.":
            "She nods. She picks up her notebook and writes something down."


    "Morphia opens the door. Outside, the undercity is grey and quiet. The hum is louder here. The wires overhead are thick, and they are moving, or they are not, and you cannot tell."

    # Move to exterior. Placeholder.
    scene bg undercity door

    show morphia neutral

    m "Come back if you need to. Anytime."
    m "I don't know what you are. I know you don't either. That's okay. It's the same thing."
    "She pauses."
    m "There's a place on Cassian Row. A tea house. The owner won't ask questions. If you get lost, go there and say my name."
    m "Don't say it to anyone else."
    "She closes the door."
    "You are outside. The street is long, and it does not look like any street you remember. You do not know if that is because you have not been here or because you are not the one who remembers."
    "The bulb above the door flickers. It steadies."
    "You walk."

    return