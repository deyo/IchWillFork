#codes:
# doyouevenlift: sets Valerie ending to true and unlocks her gallery
# 2smart4me: Sets Julia ending to true and unlocks her gallery
# killerqueen: sets Charlotte ending to true and unlocks her gallery
# gsides: the effect of all 3 previous codes conbined
# eddiepuss: sets Laura ending to true and unlocks her gallery
# yellowflute: sets Eileen ending to true and unlocks her gallery
# hailtothekingbaby: sets Harem ending to true and unlocks it's gallery
# duhasstmich: Unlocks all the gallery

label start:

if persistent.povname is None:
    $ povname = renpy.input("My name is")
    if povname is "":
        $ povname = "Dmitri"
    $ persistent.povname = povname.strip()
    menu:
        p "Is that really my name?"

        "Yes, it is.":
            jump intro_eileen
        "I don't really think so.":
            jump change_name_first

else:
    $ povname = persistent.povname

label intro_eileen:

    e "Hey..."
    "..."
    e "HEY!" with vpunch
    scene bg room with pixellate
    $ clock.day = 0
    $ clock.hourclock = 1
    "W-what!?"
    show eileen p21_neutral with dissolve
    e "Wake up!"
    e "Are you paying attention to me at all?"
    p "Yeah, I'm sorry, this is just hard to believe, you know?"
    e "Travelling to people's minds to see the inside of their psyches?"
    e "Or me going back to your life?"
    p "..."
    e "{i}sigh{/i}..."
    e @ p21_sad "Listen, I'm sorry, ok?"
    e @ p21_serious "But I'm being completely honest here. This is why I called you here."
    p "Ok, I get it, but why so urgent, sounds like something fun to do, actually."
    e "It's an ability that is useful, but it comes to a price..."
    e "It's a power that you shouldn't take lightly. Just remember you can't fix people."
    e "At least not their psyche. That's the way they are, after all."
    p "So, if this is to be believed, you've been inside my mind?"
    e "..."
    e "I've been in a lot of places, I've seen so many things, but..."
    e "Even then, I still feel powerless."
    p "Powerless? What you say you do is amazing!"
    e p21_sad "And yet, I can't change a thing."
    e "If I can't do anything with it, it's useless."
    e "..."
    p "..."
    p "But, why am I here for?"
    e p21_neutral "I abused this power, and now, I will have to pay for it."
    p "What do you- mean? That doesn't-"
    "In just a second, Eileen closed the gap between us, and..."
    if persistent.charlotte_full_ending and persistent.julia_full_ending and persistent.valerie_full_ending and persistent.laura_full_ending:
        scene eileenintro1 with flash
    else:
        scene eileenintro1fake with flash
    p "...!" with vpunch
    p "(Did she just... Kiss me?)"
    scene bg room with dissolve
    show eileen p21_happy with dissolve
    e "I've always felt the same."
    e "I will be waiting for you."
    hide eileen p21_happy with dflash
    "That was the last thing I heard from her before she just dissappeared in front of me."
    "Just leaving an small pocket watch in her place."
    hide screen clock_marker
    scene black with fade
    "My name is [povname]."
    "I'm an university student, I live by myself but I have not been able to find a job recently."
    "If things keep going this way I will be evicted. My mother is helping me with my studies."
    "A few days an old childhood friend contacted me, she wanted me to help her with something."
    "Eileen. We used to be friends since we were very young but some time after we started school she started to ignore me altogether."
    "That something turned out to be a magic trick, she explained to me that it allowed her to delve into people's psyche."
    "She said she couldn't show it to me, because it's something I wouldn't realize at all, but she said it was something serious, and that I would need this power."
    "She left me her notes and just like that, she kissed me and disappeared."
    "No one remembers her anymore, and I'm not even sure if it was all true or I was hallucinating, if she ever was real in the first place."
    "But I still have all her notes, so I will get to the bottom of this."
    "My university, Eileen and I go to the same campus, so that will be a good place to start."
    $ clock.hourclock = 0
    $ clock.advance_weekday()
    $ clock.hourclock = 0
    scene bg uni with fade
    show screen clock_marker with dissolve
    "Thankfully, Eileen left some notes for me to have an idea of what to do, she wants me to go to the minds of people close to her."
    "First of all, the trick she used on me, I'm not exactly sure if it worked or not, she already said I was not going to notice."
    "She mentions that this trick is not possible without the watch she left behind. This here will help traverse their minds."
    "She also detailed how it is done to others. I must say something surprising to them, I couple of hands movements, touch them, and I'm in their minds."
    "Secondly, I only have a whole day inside their mind. The watch will come in handy because of this."
    "I can force myself out of their minds, but it will take me a whole day in order to get inside their minds again."
    "Thirdly, if I die inside the mind of someone, I die for real..."
    "I'm not sure how does that work, but I suspect, this is what happened to Eileen... I really hope that's not the case, though."
    "Lastly, there is a possibility that doing what the notes say will bring her back, which is why she being dead is less likely."
    "The people listed in here, however, seems to have little to no connection to Eileen..."
    "So first is Charlotte. Charlotte is the queen bee of the campus, a girl that would sleep around for status, can't imagine what they have in common, but Eileen wants me to go into her mind."
    "Second is Miss Julia, she is a psychology teacher. She is very professional, an ice queen of sorts, but... Some students complains about her flirting. Eileen is her best student, so that's a lead."
    "And finally, Miss Valerie, the sports teacher. It's a bit dangerous to approach her, she is really energetic but tend to be really clumsy. Eileen wasn't very fit, but Ms. Valerie is on the list."
    show laura p41_serious with dissolve
    p "(Hmmm...? Isn't that my mom?)"
    p "(You know, I don't really know how this all will work. So I guess I can make a test tide with my mom.)"
    jump introduction_laura

label introduction:

    hide screen clock_marker with dissolve
    $ clock.advance_weekday()
    if persistent.charlotte_full_ending and persistent.julia_full_ending and persistent.valerie_full_ending and persistent.laura_full_ending and persistent.eileen_full_ending:
        scene black with logodissolve3
    else:
        if julia_third_day_finish:
            scene black with logodissolve2
        else:
            scene black with logodissolve1
    call screen introduction_menu with dissolve

label menu_select:

    hide screen clock_marker with dissolve
    $ clock.advance_weekday()
    if persistent.charlotte_full_ending and persistent.julia_full_ending and persistent.valerie_full_ending and persistent.laura_full_ending and persistent.eileen_full_ending:
        scene black with logodissolve3
    else:
        if julia_third_day_finish:
            scene black with logodissolve2
        else:
            scene black with logodissolve1
    call screen menu_select with dissolve

label menu_select_charlotte:

    hide screen clock_marker with dissolve
    $ clock.advance_weekday()
    scene black with logodissolve_charlotte
    call screen menu_select_charlotte with dissolve

label bad_end:

    scene black with fade
    "Hmm...? What is... This...?"
    "This is feels like... My own mind?"
    "I've never been the brightest, but I'm not dumb enough to be surrounded by darkness."
    "I can't really feel anything here..."
    "I feel so lonely, can't even feel my own body."
    "Well, of course, this is my mind."
    "This... This must be what happened to Eileen."
    "I'm... I'm so sorry, Eileen. I couldn't save you."
    "I couldn't even save myself."
    "Was it because I was being selfish? Because I lacked clues?"
    "Doesn't seem to matter..."
    "I'm doomed because I couldn't make my mind and abused this power?"
    "So maybe drifting in my own mind without a body is an appropiated punishment."
    "Forever."
    "..."
    "..."
    "..."
    e "Isn't it?"
    e "..."
