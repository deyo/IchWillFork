label introduction_laura:

    scene bg uni with fade
    show laura p41_serious with dissolve
    $ clock.psychename = ["LAURA"]
label laura_introscene:
    p "Mom! Hey mom!"
    l "..."
    p "MOM!"
#    if persistent.charlotte_full_ending and persistent.julia_full_ending and persistent.valerie_full_ending:
#        scene lauraintro1 with dissolve
#    else:
#        scene lauraintro1fake with dissolve
    scene lauraintro1 with dissolve
    l "Oh! Hi, [povname]! I was hoping to find you around here. How is my sweet baby doing?"
    p "Mom, don't threat me like a kid anymore."
    l  "I'm sorry, baby, but you know you will always a little baby for me"
    p "Ah... I give up. What are you doing around here?"
    l "It is so weird that I came to look for you, baby?"
    p "You could have gone home, or call me beforehand, don't you think?"
    l "Aw, come on, [povname]..."
    "This is my mother. There's not a lot to say about her. She is in her early 40s."
    "She raised me by herself, and she have been quite a pain since, always being overly mellow and protective with me."
    "But she is a nice woman, nonetheless."
    scene bg uni with dissolve
    show laura p31_happy with dissolve
    "I don't want to sound cruel, but I need to say something to surprise her."
    p "It's just, mom, it's kind of embarrassing when you are so mellow with me."
    l p31_surprised "W-what...!?" with vpunch and flash
    p "(Hmmm... That flash was pretty weird. That must be the cue.)"
    p "(I'm sorry, mom... But I make a few movements with my hands, touch her, and...)"
    scene black with flash
    "After that, the sensation was something I couldn't explain with words."
    "What the... What the hell?" with vpunch
    "Just like that, I felt like I was in a completely different world while my body was warped left and right."
    "..."
    $ inpsyche = True
    $ clock.hourclock = 0
    scene bg white town with pixellate and flash
    p "..."
    p "(That didn't feel good, at all. The landing didn't help, and...)"
    p "(What is... This? This place is kinda boring, but... It also feels ominous, this is a place I don't really want to be in.)"
    p "(But this is supposed to be my mom's mind, isn't it?)" with flash
    p "(But seeing how I'm in this weird place, I might as well explore a bit.)"
    p "(...)"
    p "(But where am I supposed to go? Everything seems the same, and it's honestly kind of scary.)"
    unk "You shouldn't be here."
    p "W-what the hell was that?"
    p "Hello?"
#    if persistent.charlotte_full_ending and persistent.julia_full_ending and persistent.valerie_full_ending:
#        scene lauraintro2 with fade
#    else:
#        scene lauraintro2fake with fade
    scene lauraintro2 with fade
    unk "You should leave, or face the consequences."
    p "But, who are you, and what is this place? This is supposed to be my mother's mind."
    unk "LEAVE!" with vpunch
    p "(And this is it, a few hand movements and I should be out of-)"
    "...!" with flash
    $ renpy.end_replay()
    scene black with fade
    show eileen p41_neutral with dissolve
    "Is that... Eileen!?"
    hide eileen p41_neutral with dissolve
    $ inpsyche = False
    $ clock.hourclock = 1
    scene bg uni with flash
    show laura p31_surprised with pixellate
    l "W-what?"
    p "..."
    p "(HOLY FUCK, THAT WAS INTENSE!)"
    p "(I must have been inside mom's mind, but what the hell was that? I thought I I was going to die!)"
    p "(What the hell was that!? Wasn't that my mom's-)"
    l "[povname]...?"
    p "Ah...! Ehm, sorry, mom."
    l "What happened? I feel dizzy all of the sudden."
    p "(She probably doesn't even know what happened, but it seems like it affected her.)"
    p "You lost balance for a moment, are you ok?"
    l @ p21_sad "Yes, I..."
    l p31_angry "Young man, don't say such horrible things to your mother!" with vpunch
    p "I... I'm sorry, mom, I didn't meant to hurt you."
    l p11_serious "..."
    l p31_happy "Aw, you know I would never be mad at you, baby."
    p "(This is exactly why I said it in the first place, though...)"
    l p11_neutral "So how is your life going, baby? Found a job yet?"
    p "Ah... Well, I'm still on it. I've been to a few interviews, and you know, going out every day!"
    l p11_sad "Oh... Baby, you've always been a terrible liar..."
    l p11_happy "If you need money just ask, ok? I know things are not going great, but your mom will always be there for you."
    p "(Right...)"
    p "Thanks mom, but it's ok, I'm a grown man, and I need to take care of my own problems, ok?"
    l p21_sad "Oh, baby... Promise me you will call me nonetheless if everything happens, ok?"
    p "If you promise to call me before showing up out of nowhere"
    l p11_happy "Always the stingy one, huh? Ok, baby, see you later, it was nice seeing you again. Come visit soon!"
    hide laura p11_happy with dissolve
    p "Bye, mom."
    scene bg uni with fade
    p "(Ah... Dealing with my mom is always a tiring experience.)"
    p "(It's pretty weird that she is around here, though, and that white light worries me.)"
    p "(I don't think she is a bad person, but sometimes she overdo it...)"
    p "Well, I better start go back to class."
    p "(I can only do this once a day, so I better take it easy.)"
    jump introduction_end_laura

label introduction_charlotte:

    scene black with logodissolve_charlotte
    $ charlotte_intro_option = True
    scene bg uni_hall with fade
    $ intropoints += 1
    $ clock.hourclock = 1
    $ clock.psychename = ["CHARLOTTE"]
    show screen clock_marker with dissolve
label charlotte_introscene1:
    p "(I think I see Charlotte over there with her friends... If I'm going to approach, I should do it at once. No second guesses...)"
    scene charlotteintro1 with dissolve
    "This is Charlotte Engel and her friends. They are in the cheerleading squad, they are also really annoying, but they are at the top stars of the campus."
    "Meaning that they have a relatively high social position on their merits, but doesn't justify their behaviour."
    "They are also beautiful, and there are rumors of them and multiple students, even professors..."
    c "... With a dress like that, she better don't come around again. She looked like a whore~ Hahahaha!"
    p "(Lovely, as always.)"
    je "No wonder her boyfriend was all over you, eh, Charlotte?"
    c "Eh? That limp dick guy? I'd be death before I go that low."
    cla "But you are going out with him, aren't you?"
    c  "I only let him be around me to piss her off!"
    cla "No way!"
    cla "HAHAHAHAHA!"
    p "(... Why do I have to do this again? Alright, fuck it.)"
    scene bg uni_hall with dissolve
    show charlotte p11_happy with dissolve
    show jean p11_neutral at charaleftmost with dissolve
    show claire p11_neutral at chararightmost with dissolve
    p "Hey, Charlotte."
    c p11_neutral "Hm? [povname]? What do you want?"
    p "I'm here to ask you a question."
    c "Go ahead, we are listening."
    p "Well, it's... Private."
    c p41_surprised "What?"
    je p21_surprised "...!"
    cla @ p11_surprised "No way, are you here to confess to her?"
    je p21_happy "How pathetic is that?"
    c p11_happy "Face it, [povname], you have no chance with me, you might as well turn around."
    p "Eh... No. Well, I'm here to ask you a couple of things, but not asking you out."
    je p11_happy "Beat it, twerp, she already said she is not interested, regardless of your questions."
    p "I was asking her, doofus, not you. So please stop being such a pain in the ass and let the adults talk."
    je p21_angry "Why you...!"
    cla p11_neutral "Calm down, Jean. if he wish to be rejected by Charlotte, go ahead."
    cla @ p21_neutral "But you can always come back crying to me."
    je "Really...?"
    cla @ p11_neutral "Can't help it!"
    c "Alright, enough. Listen, [povname], if you have any question, just ask me right here, I'm not going alone with you, I'm not big on wasting time."
    p "As you wish, your highness."
    c "That's more like it."
    p "(It was meant as an insult, but I guess Royal Pain right here didn't realize.)"
    p "By any chance, does the name Eileen rings any bells?"
    c @ p41_surprised "...!" with vflash
    c "Wait, so you came here asking me for romantic advice? I don't even know you that well, nor her, for the record. But I feel flattered. I can't really help you, though."
    p "(Huh? What with that reaction? And what was that light?)"
    p "I see... Thanks for your time."
    c "You are welcome, weirdo. Hahahaha! I'm sure it was just an excuse to approach me."
    if _in_replay:
        jump charlotte_introscene2

    c "But there are way too many guys behind me for that, and better than you in all regards."
    p "(I really can't take this anymore. But she seems to know something, I need to push this forward.)"
    p "Really, now, self-entitled bitch. So the life of someone may be in the line and you are here being the same airhead we all know and love."
    p "I'd be dead before I decide to date someone as shallow and disgusting as you are, let alone consider her attractive."
    p "(Which I actually do, but only her body, really.)"
    show jean p11_angry at charaleftmost with dissolve
    show claire p21_surprised at chararightmost with dissolve
    c @ p41_surprised "...!"
    c p41_angry "Why you... You piece of...!"
    p "I thought that I could get some help, but if this is how it is, I'm better off by myself. See ya, stupid queen."
    c p31_serious "..."
    "..."
    scene bg uni_hall with fade
    p "(And that was Charlotte for you. If it was up to me to decide, I wouldn't be here in the first place.)"
    p "(But if Eileen notes says I have to approach her, then I will. Also, her reaction towards her name is something I should look into.)"
    p "(No one should really remember Eileen right now.)"
    show charlotte p21_serious with dissolve
    c "Hey, [povname], do you have a minute?"
    p "Charlotte?"
    c "You said something about someone's life being on the line. What is it about."
    p "Well, nevermind, from what I saw back then, it really isn't your problem."
    c @ p21_angry "Come on, big baby, I'm trying to make things right, ok?"
    p "(I really don't want to deal with her right now. Although, this may be my chance to get into her mind.)"
    p "Alright, Charlotte, I'm sorry."
    p "It is about a missing person. I asked you before, but... The missing person is Eileen, do you know her?"
    c @ p41_surprised "...!" with vflash
    p "(This must be my chance!)"
    "A hand movement, touch her shoulder and finally...!"
    scene black with pflash
    p "(What the... What the hell?)" with vpunch
    "..."
    $ inpsyche = True
    $ clock.hourclock = 0
    scene bg castle_town with pflash
    p "(Where am I...?)"
    "When I opened my eyes, all I saw was this barren, old looking town."
    "(Well, if something, this is a pretty town. Is that a castle in the background?)"
    "(Fuck, I've always wanted to be in a castle, let's go and check.)"
    scene black with fade
    "..."
    "I walked quite some time without really getting anywhere."
    "..."
    scene bg castle_town with fade
    p "(This town seems deserted.)"
    p "(And the castle nowhere close still.)"
    p "(I wonder where the hell everyone is. Although, I might be alone here.)"
    p "(Specially considering whose mind we are talking about here.)"
    sol "HALT!" with vpunch
    show soldier pp11 with dissolve
    p "(What with the storm trooper? Pretty jarring, if you ask me.)"
    sol "Citizen, why are you not wearing your uniform?"
    p "Hm? Uniform?"
    sol "Please show your identification or surrender yourself."
    p "(This isn't looking good...)"
    p "Listen, I'm new here, I really didn't know about an uniform, or any kind of ID."
    p "There's nothing I can do? Somewhere I can go?"
    sol "Yes, you can surrender and come with us."
    p "(That didn't go as smooth as I expected it to go.)"
    p "Alright, pal, listen, I will come with you, but first, can you help me with some information about a friend."
    p "Her name is Eileen, do you know anything about her?"
    show soldier pp11 as soldier2 at charaleftmost with moveinleft
    sol "..."
    p "Ok... What about Charlotte, does the name rings any bells?"
    show soldier pp11 as soldier3 at chararightmost with moveinright
    sol "Stranger, you are definitively coming with us. You have a lot to explain."
    p "Well, shit, why? And if I refuse?"
    sol "..." with vflash
    p "...!"
    sol "We will open fire."
    p "Will? What the fuck!?"
    sol "Foul language will be taken into consideration, surrender yourself."
    p "(Great, I have not spent even an hour here and I'm already at death's doorstep."
    p "(... Fuck...)"
    scene black with fade
    "..."
    "The soldiers put me in a vehicle. I couldn't really tell what kind."
    $ clock.advance_hour()
    "It felt like we went for hours. This town is really bigger than I expected."
    "So the castle was probably bigger than I expected."
    "..." with vpunch
    sol "Alright, we are here. Good luck, stranger."
    "..."
    "Before they took me out of the cart, they blindfolded me, for some reason."
    sol "Stranger, please step out the wagon."
    "And as I did, the blindfold came out to show me a person I really don't like seeing."
label charlotte_introscene2:
    scene charlotteintro2
    c "Is this the prisoner?"
    sol "Yes ma'am!"
    "And there she is, Charlotte, as always, surrounded by soldiers."
    "She is... Dressed in a really peculiar way, different from the other soldiers."
    "And this can only mean bad news for me."
    c "Did he resist?"
    p "Wait, Char-"
    sol "NO TALKING." with flash
    "The soldier gave me another hit with his gun."
    sol "He did not resist, ma'am."
    c "Very well, take him  in."
    sol "YES MA'AM!"
    scene black with fade
    "And with that they covered my face with a cloth or something like that."
    p "(That was definetively Charlotte. What with the outfit?)"
    p "(Well, I couldn't look too much around, but it seems like I'm finally in the castle.)"
    p "(Or at least, that's where I think they are taking me to.)"
    "And of course, that was it."
    "..."
    scene bg castle_hall with fade
    p "Holy crap, this castle is huge! I always wanted to go to Disneyland!"
    sol "Silence!"
    show charlotte pp21_serious with dissolve
    show soldier pp11 as soldier2 at charaleftmost with moveinleft
    show soldier pp11 as soldier3 at chararightmost with moveinright
    p "(But, of course, the happiest place on earth wouldn't have her. Or all these soldiers. Or the weapons.)"
    c "So... You are the stranger my soldiers found roaming around my town, huh?"
    p "Charlotte. So, how should I call you, your highness? Or-"
    p "...!" with vpunch
    p "Shit, mate, what was that for!?"
    sol "I already said, SILENCE!"
    sol "BE MORE RESPECTFUL TOWARDS OUR LEADER!"
    c pp41_surprised "Wait!"
    sol "... Leader...?"
    c "I-I mean... Stop."
    c pp31_serious "Let him speak, I will make sure he pays for his insolence later."
    c "In the meantime, stranger, answer my questions. Who are you? Where do you come from? And what do you want here?"
    p "(Well, it seems like she doesn't know who I am.)"
    p "Very well, \"your highness\"."
    c "..."
    p "I came here to save a friend. Her name is Eileen, do you know anything about he-"
    p "...!" with vflash
    p "Again!?" with vpunch
    sol "Don't utter that name in front of our leader!"
    c pp21_serious "Enough! Don't act if I don't command you to, soldier! You are dismissed!"
    sol "But leader, he was..."
    c @ pp31_angry "Dismissed!" with vpunch
    sol "Y-yes, ma'am!"
    hide soldier pp11 as soldier2 at left with dissolve
    c "Pardon me, stranger, soldiers tend to get heated towards that subject. I reccomend you to drop it around here."
    c "However, I can't overlook that you seems to be friends of this Eileen."
    c "Furthermore, the soldier that brought you here mentioned that you knew my name, even though this is our first meeting."
    c "I don't know who you are, or what you are doing here, but for that knowledge alone I'm afraid you are an enemy for our nation."
    p "What!? But why!? What have-"
    c pp21_angry "SILENCE!"
    "Here she goes again. I fucking hate that."
    c "Only speak when allowed!"
    c pp21_serious "Also, I don't need to give an stranger such as you any kind of explanation for my decisions."
    c "Hereby you are sentenced to spend the rest of your days in the dungeon, or until we find who you are and what to do with you."
    p "I'm... Pretty sure I'll die before that."
    c "Then so be it."
    p "What!?" with vpunch
    c "Soldiers, take him to his cell."
    p "W-wait!"
    sol "Yes, ma'am!"
    $ renpy.end_replay()

    scene black with fade
    "With that, the soldiers took me out of Charlotte's throne room. Again, they put me on "
    "Well... I'll be free in a couple of hours. But I don't like the idea of spending my time in a dungeon."
    "..."
    scene bg castle_room with fade
    p "So... This is the dungeon."
    p "Can I get life sentence? I'm guilty, I swear."
    "The guard was outside, locking the door."
    sol "... You are very annoying, stranger. See you in the morning."
    p "(Not a chance. Seems like it's time to get out of here.)"
    "With some movements of my hand..."
    "...!" with flash
    scene black with fade
    show eileen p41_serious with dissolve
    if intropoints == 1:
        p "(Eileen!? Again!?)"
    elif intropoints == 2:
        p "Wait, Eileen! Wait!"
    elif intropoints == 3:
        "I saw Eileen once more."
        "But this time..."
        e p41_happy "..."
        "She looked back at me and smiled. Right before she vanished."
        "Right before she vanished yet again."
    hide eileen with dissolve
    $ inpsyche = False
    $ clock.hourclock = 1
    scene bg uni_hall with pflash
    show charlotte p41_surprised with pixellate
    c "W-what happened!?"
    p "We..."
    p "(Don't fuck up, I came out of her mind! I need to think of something!)"
    p "I... Eh..."
    p "When I mentioned Eileen, you spaced out, are you ok?"
    c p21_sad "I... Am..."
    c "I see, I'm sorry... It's just a shock, you know? No one seems to notice that..."
    c "Eileen is missing."
    p "So you are aware...?"
    c "I just... It's scary. I know we are not close anymore... But..."
    p "(Eileen and her used to be friends?)"
    c "So, [povname], can I help you?"
    c "Can we help her?"
    p "Listen, Charlotte, I'm not entirely sure, but... I think we can."
    c p31_surprised "W-what should I do, then!?"
    p "(I can't go into her mind again, So I guess we wait.)"
    p "For now, Charlotte, you've done enough."
    c "W-what?"
    c p21_sad "Did I do something wrong? I'm sorry for what I said..."
    p "No no, it's ok, just trust me, ok?"
    c p31_surprised "A-alright!"
    c p31_sad "And..."
    c "..."
    c "I'm sorry, ok?"
    c p21_serious "If you need anything to bring Eileen back, just say so, ok?"
    c p31_neutral "See ya, [povname]."
    hide charlote p31_neutral with dissolve
    p "Y-yeah, see ya, Charlotte."
    p "(That was even more stressful than I thought. But just now... That's not the Charlotte I'm used to.)"
    p "(This is odd, her and Eileen being friends... This is really odd.)"
    p "(I better go back to class. It's true I'm not hungry nor tired.)"
    p "(At least not psysically, but man, I feel like I've been doing math all day.)"
    scene black with fade
    "And just like that, I turned myself back to classes."
    "Another long day, while questions just hanged in my head."
    "Even when I got home, of course."
    jump introduction_end_charlotte

label introduction_julia:

    scene black with logodissolve_julia
    $ julia_intro_option = True
    scene bg uni_hall with fade
    $ intropoints += 1
    $ clock.hourclock = 1
    $ clock.psychename = ["JULIA"]
    show screen clock_marker with dissolve
label julia_introscene1:
    p "(Miss Julia usually spends time in the teacher's lounge. That will be a good place to start.)"
    scene bg teachers with fade
    scene juliaintro1 with dissolve
    "And there she is, the bombshell of the campus, Miss Julia Sauer."
    "Even though she is so sexy, most people avoid her, because she is... Kinda aggressive. Although I'm sure she doesn't mean it."
    "It's evident she is not only too good for this place, but she knows it. It bothers her, and... There's something else."
    j "Hey, you."
    "For some reason, she insists on sexually harass students. She do it in a way that is more obnoxious than anything, probably taking advantage of her charm."
    "Other than that, I think she is very admirable, and-"
    j "YOU! THE IDIOT BY THE DOOR!" with vpunch
    p "W-what!?"
    j "What do you want? You are distracting me."
    scene bg teachers with dissolve
    show julia p31_serious with dissolve
    p "I'm sorry, Miss Julia, I-"
    j @ p11_surprised "Ah, I recognize you, boy, you are [povname]."
    p "I yes, and I-"
    j p31_neutral "Don't be shy, handsome, what do you need?"
    p "(And here she goes...)"
    p "W-well, Miss Julia, I came to ask you a question."
    j p11_happy "Straight to the point, eh, boy? I'm willing to do it wherever and whenever you want to."
    j "In fact, right now there's no one around the roof and I have the key so we could-"
    p "N-no! Not that kind of stuff. It's actually a really delicated question."
    p "I was just wondering, have you seen Eileen?"
    j p41_serious "Hmmm...? Eileen..."
    j p41_surprised "Eileen...!" with flash
    p "(I can't really miss this chance, although this was pretty easy.)"
    "As I said that, with a few hands moevements and touching her shoulder"
    p "(Here goes no-)"
    scene black with pflash
    p "(Shit...!)" with vpunch
    "..."
    $ inpsyche = True
    $ clock.hourclock = 0
    scene bg future_city with pflash
    "The place I got to was amazing. Lights everywhere, buildings so tall you can't see beyind them."
    p "(Are those fucking flying cars!?)"
    p "(This doesn't feel real, but it must be Miss Julia's mind without a doubt.)"
    p "(I'm not even sure if it's morning or night, I can't see the sky, after all.)"
    p "(But... How the fuck am I supposed to find Miss Julia in all this mess?)"
    p "(Well, I need to find a bit more about this place...)"
    show robot pp11_neutral with dissolve
    rob "..."
    p "..."
    "I couldn't believe it. It was not only a robot, the robot looked exactly like Miss Julia."
    p "(If something, there's no doubt where am I now. Unless I'm in the mind of some kind of pervert.)"
    p "Hi...?"
    if _in_replay:
        jump julia_introscene2

    rob @ pp11_happy "Hello, carbon based human life form. What can I help you with?"
    p "(This is... Surreal, but if this is Miss Julia's mind, it makes sense that there are advanced stuff like this."
    p "(And condescendant too.)"
    p "I... I was wondering, I have a few questions about this place."
    rob @ pp11_happy "Proceed, carbon based human life form."
    p "Can you please not call me carbon based human life form? Kind of patronizing there."
    rob @ pp11_sad "My apologies, carbon based human life form. There is no precedent for this procedure."
    rob @ pp11_happy "It is not very common to find such an archaic life form."
    rob @ pp11_happy "Tell me, carbon based human life form, how can I adress you?"
    p "Alright, call me [povname], rude robot."
    rob @ pp11_happy "Understood, [povname] rude robot."
    p "No! I mean just [povname]!"
    rob @ pp11_happy "Understood, I mean just [povname]."
    p "... I need to try a different strategy."
    p "Ok, robot, can you change the way you adress me?"
    rob "But of course, I mean just [povname], how can I adress you?"
    p "[povname]."
    rob @ pp11_happy "Understood, [povname]."
    p "Finally..."
    rob @ pp11_sad "I apologize, I'm not... Used to carbon based human lifeforms"
    p "(...)"
label julia_introscene2:
    rob @ pp11_happy "What can I help you with, [povname]?"
    p "As I said, I was wondering about this-"
    "At that moment, a huge screen behind me turned on."
    "And inside, was Miss Julia, with more robots like her."
    scene juliaintro2 with dissolve
    j "I salute you, my units."
    "There she was, wearing some kind of strange suit, similar to the ones the robots use."
    "It looked like some kind of control room."
    j "Units, I detected there's an unidentified life form in the premises of this city."
    p "(She is already aware I'm here...?)"
    j "It is biologic in origin. Most likely a human."
    j "This is very unusual, as you may know. There are no biologic organisms in these premises."
    j "Specially not without my permission."
    j "Units, this is an emergency state. This lifeform can be malicious."
    j "I detect it around area CL4-Cyrus."
    j "If you see it..."
    j "Kill it." with flash
    j "Transmission over."
    scene bg future_city with dissolve
    p "..."
    "I looked at the robot next to me. I was honestly terrified."
    show robot pp11_neutral with dissolve
    rob "..."
    p "(Time to get the fuck out of here.)"
    rob pp11_surprised "Wait, human, don't-!"
    $ renpy.end_replay()
    "I couldn't move my hands faster, and then..."
    "...!" with flash
    scene black with fade
    show eileen p41_serious with dissolve
    if intropoints == 1:
        p "(Eileen!? Again!?)"
    elif intropoints == 2:
        p "Wait, Eileen! Wait!"
    elif intropoints == 3:
        "I saw Eileen once more."
        "But this time..."
        e "..."
        "She looked back at me, right before she vanished yet again."
    hide Eileen with dissolve
    $ inpsyche = False
    $ clock.hourclock = 1
    scene bg teachers with pflash
    show julia p41_surprised with pixellate
    p "I almost didn't make it!"
    j "...!"
    p "(She seems shocked. I better calm her down!)"
    p "Y-yeah, I mean, I almost don't make it here, I'm sorry, I have a lot of work to do, that's why I want to make this quick."
    j p41_serious "..."
    p "I... Yeah, my question is about Eileen, Miss Julia, Eileen Becker, do you know her?"
    j "Right..."
    j p11_neutral "Now that you mention it, I have some time I don't see her around. I nearly forgot about her. But... She have come every day since I know her."
    j @ p31_happy "At least the days we have classes, of course."
    j "Even then. I'm sure she shows up for extra activities on weekends."
    j "I wonder where she is... Why do you ask?"
    j "Ah... Don't tell me..."
    j p31_happy "You are into her! She is certainly a pretty one."
    p "E-eh... It's not like that. I'm just worried about her, have not seen her in a couple of days."
    j "No need to be embarrassed around me, boy."
    j p21_sad "But it hurts me a little, you know, here is your teacher, all for yourself."
    j "Why would you want such a young girl when I have all this experience under my belt, huh? Don't you like mature women?"
    p "A-as I said it's not like that."
    j p21_happy "Oh really? Then that does mean I could undo your pants right now and feel your hard-"
    p "I-I don't think this is appropiate." with vpunch
    j "That's why it's so exciting, don't you think?"
    j @ p21_surprised "Oh...!"
    j "So you want a threesome, you little devil!"
    p "W-WHAT?!" with vpunch
    p "I... Miss Julia, I... Thanks for your insight about Eileen. See you later." with vpunch
    "And I left the room as fast as I could possibly could."
    j p31_neutral "..."
    j "See you later, boy."
    scene bg uni_hall with fade
    p "(Well, that was awkward. Seems like Miss Julia thinks highly of Eileen. But... She actually seems to remember her, when everyone else doesn't.)"
    p "(This is certainly a lead. I just need to find out exactly why.)"
    "And as I thought about that, I had no other option but go back to classes."
    scene black with fade
    "And I spent the whole day like so before going back home, tired and with so many questions."
    "I was still trembling. I could have died in Miss Julia's mind."
    "As she let herself seen, she is brilliant, but also really dangerous, that's no surprise."
    "Next time, I gotta be prepared."
    jump introduction_end_julia

label introduction_valerie:

    scene black with logodissolve_valerie
    scene bg sports with fade
    $ valerie_intro_option = True
    scene bg uni_hall with fade
    $ clock.hourclock = 1
    $ clock.psychename = ["VALERIE"]
    show screen clock_marker with dissolve
label valerie_introscene1:
    scene bg sports with fade
    p "(I don't come here that often. And I've never seen Eileen coming here either. Not like I see her that much lately.)"
    p "(I don't know that much about about Miss Valerie. I've seen that her body is... Well built.)"
    p "(I'm not that much of an sportsman myself, so I've never been around here that much.)"
    p "Now, I wonder where-"
    scene valerieintro1 with dissolve
    "And there she was, Miss Valerie Lang."
    "When I stepped in, all I saw was a graceful girl flying around with a big smile in her face."
    "Miss Valerie is quite attractive on top of being so good for sports."
    "And she seems to genuinely enjoy them. She is quite forceful, though."
    "I've heard she is rather clumsy, and more often than not she-"
    scene bg sports with dissolve
    show valerie p21_surprised with moveinright
    v "HEY YOU! LOOK OUT!"
    p "Wha-!"
    scene black with vpunch
    p "(And that's it. I'm dead. I'm sorry, Eileen...)"
    v "Hey..."
    p "(I didn't achieve much, now that I think about it.)"
    v "Oh shit... Don't tell me I killed him."
    p "(I'll die a virgin. Nobody needs to know that, though.)"
    scene bg sports with fade
    show valerie p11_surprised with dissolve
    v "HEY! WAKE UP!" with vpunch
    p "HOLY SHIT!" with vpunch
    v p41_happy "Oh... Great! I thought I was going to jail!"
    p "..."
    v @ p31_surprised "I-I mean, I'm glad you are ok!"
    p "Barely, but I will live. You should be more careful, Miss Valerie!"
    v @ p31_serious "But man, you just stood right there in the middle of the field and I was running as fast as possible with the ball."
    v @ p11_neutral "So maybe you should be more careful."
    p "Are you kidding me!?" with vpunch
    if _in_replay:
        jump valerie_introscene2

    p "I was out of the field!"
    v @ p11_surprised "O-oh, right. I'm very sorry about it nonetheless."
    p "It's ok, don't wo-"
    v "But man, what a wimp. Can't really take a tackle from a woman, huh?"
    p "..."
    p "(I'm pretty sure you are no normal woman...)"
    p "Right. Miss Valerie, I just came here to ask you a question."
    v "I give classes on sundays and I don't charge a lot! You'll need all the time I can give you, kid."
    p "No, I appreciate the offer, but that's not it, I was just wondering-"
    v "Oh, then a secret admirer? That's sweet, kid, but I doubt you can handle this."
    p "For fuck sakes, miss! Can you let me talk already?"
    v @ p41_surprised "O-ok. Sure kid, go ahead"
    p "Can we go to the hallway for a second?"
    v "Eh, sure. The game is over anyway."
    p "(Really? I wonder how long I was out cold...)"
    scene bg uni_hall with fade
    show valerie p11_neutral with dissolve
    v "Come on, dude, spit it."
    v @ p21_happy "Is it really a confession. I already said no, remember?"
    p "No... Listen."
    p "I was wondering if you know Eileen Becker. An small girl? With a ponytail?"
    v p11_surprised "...!" with flash
    p "(She is surprised indeed! This does mean she knows Eileen somehow.)"
    p "(So now I only have to go into her mind.)"
    "I moved my hands as Eileen notes said, and..."
    scene black with pflash
    p "(Ahrg...!)" with vpunch
    "..."
    $ inpsyche = True
    $ clock.hourclock = 0
    "Opening my eyes was kind of surprised, since everything was so bright, it was hard to see at first."
    "Yet, when I got used to the intense brightness, I was taken back."
    scene bg island with pflash
    p "(...)"
    p "(Well, shit, this place is beautiful.)"
    p "(Is this really Miss Valerie's mind? I mean, no offense, but I thought I'd end up in a colliseum of something.)"
    p "(This is surprisingly calmer and more beutiful than I thought it'd be.)"
    p "(But no sign of Miss Valerie. I guess I have no move around the island to figure out exactly where she is.)"
    scene black with fade
    "..."
label valerie_introscene2:
    scene bg island with fade
    "I walked around the island for quite some time. I was wondering if it was just an island at all."
    "The jungle was actually the scariest part, standing tall and endless."
    p "(It seems like I'm the only person around, despite how huge the island is."
    p "(There is no sign of Miss Valerie or anything else, really...)"
    p "I know Miss Valerie is not the brightest person, but her mind being empty..."
    p "Sure, it's beautiful, but-"
    p "...!" with vpunch
    "A huge noise nearby made all the sand and trees tremble."
    p "W-what the hell!?"
    "I rushed towards there because, well, there was anything else here."
    "And there, I saw her, among other outlandish things."
    scene valerieintro2 with dissolve
    ogr "YOU THINK THAT WILL BE ENOUGH TO STOP ME!?"
    v "..."
    "It was... Amazing, to say the least."
    "There was Miss Valerie fighting against two towering humanoids of different colors."
    "And it was a fierce battle at that."
    orc "How much more can you last?"
    v "...!" with vpunch
    ogr "I don't even feel it!"
    v "... Neither do I"
    "Over and over kicks flied as that big club like weapon was moved around."
    orc "Hm...? Hey, who are you?"
    "Those huge things both looked at me, ignoring Miss Valerie altogether."
    scene bg island with dissolve
    show orc pp31_panning at charaleft with dissolve
    show ogr pp31_panning at chararight with dissolve
    p "(T-they are huge!)"
    hide orc pp31_panning at charaleft with dissolve
    hide ogr pp31_panning at charaleft with dissolve
    show orc pp11_happy at charaleft with dissolve
    show ogr pp21_angry at chararight with dissolve
    ogr "Who are you, pipsqueak?"
    orc "Does it really matter? Now we have something else to have fun with!"
    ogr "True..."
    v "ENOUGH!" with vpunch
    hide orc pp11_happy at charaleftmost with moveoutleft
    hide ogr pp21_angry at chararightmost with moveoutleft
    show valerie pp31_angry with moveinright
    v "I don't know who are you, but you should flee."
    v "You are no match for them, and I..."
    v @ pp31_sad "I can't protect you..."
    show orc pp11_happy at charaleftmost with dissolve
    show ogr pp21_angry at chararightmost with dissolve
    orc "Isn't that sad?"
    ogr "YOU HAVE NOWHERE TO RUN!"
    p "(That's where you are wrong.)"
    "So many things were happening, my mind raced as I made the motions."
    p "...!" with flash
    $ renpy.end_replay()
    scene black with fade
    "But couldn't help but wonder..."
    p "(Will Miss Valerie be ok on her own?)"
    "It was her own mind, though..."
    scene black with fade
    show eileen p41_serious with dissolve
    if intropoints == 1:
        p "(Eileen!? Again!?)"
    elif intropoints == 2:
        p "Wait, Eileen! Wait!"
    elif intropoints == 3:
        "I saw Eileen once more."
        "But this time..."
        e p41_happy "..."
        "She looked back at me and smiled. Right before she vanished."
        "Right before she vanished yet again."
    hide eileen with dissolve
    $ inpsyche = False
    $ clock.hourclock = 1
    scene bg uni_hall with pflash
    show valerie p11_surprised with pixellate
    v "What the hell!?"
    p "(That was amazing, it didn't only looked amazing, but scary at the same time.)"
    v @ p31_surprised "Hey, what is happening!?"
    v "Are you ok, Miss Valerie? You spaced out a bit?"
    v p11_serious "I did...? hmmm..."
    p "(Can't really tell her I was inside her mind, can ?)"
    p "Y-yeah... Just as I was asking you a question..."
    v p11_neutral "Oh, I'm... Sorry, what was it?"
    p "I was wondering, do you know who Eileen is?"
    v @ p11_surprised "Eileen?" with flash
    p "Yes, Eileen Becker."
    v p11_neutral "Hmmmm... I don't really remember her. Although I think I've heard about her before."
    p "Really? She is pale and... Small?"
    p "(I could say she is sweet, but that is very embarassing.)"
    v @ p41_happy "I have way too many students, kid, and the ones I remember are worth remembering."
    v "Doesn't help that I also give private lessons in a gym nearby, and some of the students from the campus go there as well."
    v "Maybe I can find more about her in my log back at the gym, if she ever showed there."
    v "Can't promise you anything, ok? But come and check it yourself if you want. The gym is around the corner."
    p "Really!? Alright! I'll be there."
    v @ p41_happy "Alright squirt, and I'll give you the first lesson for free. You need it."
    p "(Rude...)"
    p "Of course... Thanks, Miss Valerie."
    v "Call me Valerie. See you there, then!"
    hide valerie p11_neutral with dissolve
    p "(That was surprisingly helpful. Or, at least, seems like a promising lead.)"
    p "(But doesn't seem like Valerie knows Eileen at all. I wonder why Eileen would note her if so.)"
    p "(But seeing how she reacted to her name despite not knowing her must mean something...)"
    p "(Oh well. Classes are about to start.)"
    scene black with fade
    "If I'm honest, I couldn't stop thinking about what I saw in Miss Valerie's mind."
    "She seems to be much more than she looks. Or maybe she is that and more..."
    jump introduction_end_valerie
