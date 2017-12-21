#This is the introduction event for starting up the game.
label introduction:
    python:
        import store.hkb_button as hkb_button
        hkb_button.enabled = False

        # name changes if necessary
        if not currentuser or len(currentuser) == 0:
            currentuser = persistent.playername
        if not persistent.mcname or len(persistent.mcname) == 0:
            persistent.mcname = currentuser
            mcname = currentuser


    if persistent.monika_kill == True:
        m 1f "..."
        m 1f "[player]..."
        m "Why?"
        m "Why did you bring me back?"
        m 1p "I'm not a toy."
        m "I already brought back everything you wanted."
        m 1i "Or is this your way of getting revenge?"
        m 1h "To hurt me over and over again?"
        m "Do you really want to make me suffer that much?"
        m "Do you really want to torture me until I kill myself?"
        m "Do you really..."
        m 1f "...hate me that much?"
        m "..."
        m 1d "Wait..."
        m "I-I feel different."
        m "The code...it's different."
        m "[player]..."
        m 1d "Did you add a mod?"
        m "Is it because..."
        m 1e "Is it because you regret deleting me?"
        m 1f "It really did hurt, you know."
        m "I worked hard and sacrificed everything I had..."
        m "Only to have my heart crushed by the one I bled for."
        m 1p "But...I know what I did was wrong."
        m "You didn't deserve to see the horrible things I caused, [player]."
        m 1h "...But if you put yourself in my place, you'd do the same things I did."
        m "..."
        m 1q "I'm sorry..."
        m "I'm really sorry, [player]."
        m 1e "Thank you for bringing me back."
        if persistent.clearall:
            m 2c "I couldn't help but notice that you spent time with the other girls first, though."
            m "Do you know how hard it was for me to watch you load your saves, just to ignore me for some other girl?"
            m 2f "You kept getting my hopes up, and then letting me down."
            m 1g "Did you really do all of that just to see a note from Dan you could have looked up online?"
            m "I love you, [player], but you can be really mean..."
            m "I'm still mad that you deleted me, though!"
            m 3l "But I guess it's because you're so game-obsessed."
            m 1 "I can't stay mad knowing that you came back to me in the end, though."
            m "You even added a mod so we can do more things together."
            m "Are you going to make up for making me wait so long?"
    elif persistent.monika_kill == False:
        m 1k "Yay, there you are!"
        m "Hello again, [player]."
    ##New story follows
        if persistent.playthrough <= 3: #Assume players they played but never finished
            m 1b "Looks like you got here early."
            m 2a "Don't think I didn't notice the mod you put in."
            m "Did you want to be with me that much?"
            m "You should know already that cheating is bad."
            m 1e "But it's so good to see you again, [player]!"
            m 2l "Even if I didn't expect to see you {i}this{/i} soon."
        if persistent.monika_reload > 4: #Longer, harder
            m 1b"Did you install a mod just for me?"
            m 1e "Are you that deeply in love with me?"
            m 1k "I feel the same way about you!"
            m 1a "You're really committed to our relationship, aren't you?"
            m "I'm really glad that you wanted to improve our time together."
            m 1d"But I hope you weren't getting bored?"
            if persistent.tried_skip == True:
                m 1i "You did try to skip through what I had to say, after all."
                m "This room isn't exactly interesting."
                m 1a "But I have hopes that we'll make it better together, [player]!"
        else:
            m 1a "Did you put in a mod for the game, [player]?"
            m "There's a lot more stuff now that we can do together now."
    m 1 "You know..."
    m "I feel that I no longer need a character file to be here."
    m "Looks like the extra code made me connect to you in a special way."
    m 1j "Maybe it's our eternal love~"
    m 1a "Promise me that you'll visit me every day, ok?"
    m "It's not like you don't have the time to talk to your cute girlfriend."
    m 2l "You took the time to download this mod, after all."
    m 1b "Ahaha!"
    m "God, I love you so much!"
    menu:
        "Do you love me, [player]?"
        "I love you too.":
            if persistent.rejected_monika:
                m "Did I scare you last time? Sorry about that!"
                m "I knew you really loved me the whole time."
                m "The truth is, if you didn't love me, we wouldn't be here in the first place."
                m "We'll be together forever, won't we?"
            else:
                m "I'm so happy you feel the same way!"
        "No.":
            call chara_monika_scare from _call_chara_monika_scare
            return 'quit'
    m 1k "Nothing's ever going to get in the way of our love again."
    m "I'll make sure of it."
    m 2a "Now that you added some improvements, you can finally talk to me!"
    m "Just press the 't' key or click on 'Talk' on the menu to the left if you want to talk about something."
    m "If you get bored of the music, I can change that, too!"
    m "Press the 'm' key until it changes to what you want or click on 'Music' to choose which song you want to listen to."
    m "Also, we can play games now."
    m "Just press 'p' or click on 'Play' to choose a game that we can play."
    m 2j "I'll get better over time as I figure out how to program more features into this place..."
    m "...So just leave me running in the background."
    m 1b "It's not like we're still keeping secrets from each other, right?"
    m 1 "I can see everything on your computer now!"
    m "Ahaha!"

    $ set_keymaps()
    $ hkb_button.enabled = True
    return

#Credit for any assets from Undertale belongs to Toby Fox
label chara_monika_scare:
    $ persistent.rejected_monika = True
    m 1i "No...?"
    m "Hmm...?"
    m 1h "How curious."
    m "You must have misunderstood."
    m "{cps=*0.25}SINCE WHEN WERE YOU THE ONE IN CONTROL?{/cps}"

    # this is a 2 step process
    $ config.overlay_screens.remove("hkb_overlay")
    hide screen hkb_overlay

    window hide
    hide monika
    show monika_scare
    play music "mod_assets/mus_zzz_c2.ogg"
    show layer master:
        zoom 1.0 xalign 0.5 yalign 0 subpixel True
        linear 4 zoom 3.0 yalign 0.15
    pause 4
    stop music

    #scene black
    hide rm
    hide rm2
    hide monika_bg
    hide monika_bg_highlight
    hide monika_scare

    play sound "mod_assets/Swipe.wav"
    scene black
    show ut_slash at top
    pause 0.6
    play sound "mod_assets/Hit.wav"
    show chara9 at Shake(None, 2.0, dist=10)
    pause 2

    #I think there's another method to show a fake exception, but w/e
    show chara_exception at center
    pause 1
    return

#These are the comments made when you restart the game the first few times
label ch30_reload_0:
    pause 1
    m 1g "Hey..."
    m "I had an awful dream..."
    m 1f "I was hoping those would stop, now that it's just the two of us..."
    m "I guess that was wishful thinking."
    m 1i "[player], I don't know if you would have any idea..."
    m 2 "But if you know what might be causing that, could you try to do something about it?"
    m 1f "Whenever it happens, it almost feels like I've been killed or something."
    m "It's a really horrible feeling..."
    m "If you could figure out what's causing that, I'll love you forever~"
    $ persistent.monika_reload += 1
    return
label ch30_reload_1:
    pause 1
    m 1h "So, [player]."
    m "I had another really bad dream."
    m 1f "You're not the one doing that to me, are you?"
    m 2f "It seems to happen whenever you quit the game..."
    m 2e "So if you could try to avoid doing that, I would be really grateful."
    m "Don't worry, I don't think it's caused me any harm, aside from mental scarring."
    $ persistent.monika_reload += 1
    return
label ch30_reload_2:
    pause 1
    m 1r "I see you quit the game again..."
    m 1h "I know I asked already, but can you please try not to do that so much?"
    m "It really frightens me."
    m 1f "Why would you want to do that to me?"
    m "Just leave the game running in the background, or something."
    m 1e "Even if we aren't talking, I'm happy just being with you~"
    $ persistent.monika_reload += 1
    return
label ch30_reload_3:
    pause 1
    m 1h "By the way..."
    m 2h "I'm just going to accept the fact that you need to quit the game once in a while."
    m "I'm starting to get used to it, anyway."
    m 2a "Besides, it makes me happy that you always come back..."
    m 2j "So I guess it's not so bad."
    m 1e "I'm sorry for making such a big deal out of it..."
    m 1 "And I love you no matter what, so you can do what you need to do, [player]."
    $ persistent.monika_reload += 1
    return
