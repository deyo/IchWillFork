label introduction_end_laura:

    $ clock.hourclock = 4
    scene bg room with fade
    p "(Well, today was a busy day at class, as always. But let's point out to the elephant in the room.)"
    p "(I managed to get into my mom's mind. But her mind was so weird... I was left with more questions than answers.)"
    p "(But that was a confirmation of how this work, more or less.)"
    p "(Tomorrow I will properly start investigating these women.)"
    p "(But, what with eileen there?)"
    p "(Good night!)"
    "With that, I closed my eyes..."
    jump introduction

label introduction_end_charlotte:

    $ clock.hourclock = 4
    scene bg room with fade
    p "(Man... I'm beat.)"
    p "(Well, at least I have an ally now, sort of.)"
    p "(Charlotte seems genuinely worried about Eileen, but I don't blame her, she seems to be the only person she knows that remembers her.)"
    p "(I also didn't know they knew each other so now their relationship seems more clear.)"
    p "(Or is it? As far as I'm aware, Charlotte actually tormented Eileen, like she torments anyone in her path.)"
    p "(So I don't know exactly what she meant. And, as usual, I have more questions than answers.)"
    p "(For example, what the hell with Eileen there again?)"
    p "(And, honestly, I could have died in there, despite Charlotte being surprisingly leveled there.)"
    if charlotte_intro_option and julia_intro_option and valerie_intro_option:
        p "(But well, this means I can finally start to properly investigate each of them.)"
        p "(Starting next week, I should focus on this investigation now that I learned the ropes of this weird ability.)"
        p "(I better take note of everything I've been through in the last couple of days.)"
        p "(I should also take the time to revise Eileen's...)"
        p "Wait a minute, what does this say? It's upside down, seems like a note."
        e "(Escaping the mind of a person is so you can protect yourself from the dangers they may have. However, this is just in case of emergency.)"
        e "(Ejecting yourself off of someone's mind takes a toll on your own, and it's dangerous on it's own. You get shattered little by little.)"
        e "(More so than it does entering in their minds in the first place, and getting out of there after a day is a natural way to do it.)"
        e "That's why I think that doing this more than 4 times would shatter your mind.)"
        p "(So this means...)"
        p "I CAN'T ESCAPE THEIR MINDS AT WILL ANYMORE!" with vpunch
        p "(Talking about fucking up... So now it will be even more dangerous...)"
        p "(Ah... Well, it's my own fault for not reading everything before jumping in...)"
        p "(But then, I really should try to stay alive, or else... Does that mean, I will end like Eileen if I fail?)"
        "As I said that, I closed my eyes, waiting for a new week, and hopefully solve this once and for all..."
        p "(Wait for me, Eileen...)"
        p "(Good night.)"
        "..."
        $ clock.day = 0
        $ clock.hourclock = 0
        $ persistent.introfull = True
        jump menu_select
    else:
        p "(Well, no matter, tomorrow will be another heavy day. I hope it isn't as difficult as dealing with Charlotte.)"
        "Feeling some dread with that thought, I proceeded to close my eyes..."
        p "(Good night.)"
        "..."
        $ clock.hourclock = 0
        jump introduction

label introduction_end_julia:

    $ clock.hourclock = 4
    scene bg room with fade
    p "(... Finally home.)"
    p "(I can't stop thinking about what happened over and over.)"
    p "(If it wasn't for the fact that Miss Julia almost killed me in her own mind, I would have spend far more time in her mind.)"
    p "(It's something I really wanted to learn more about but... If something, I wonder how real are things inside out subconcious.)"
    p "(I'm not an expert, but I'm sure that our subconcious tell us things we are not even aware of. Things we know, but that we are not aware of.)"
    p "(Or so it goes... So, if that's the case, Miss Julia is even more impressive than what I could ever thought...)"
    p "(On itself, she seems to be a lead to Eileen, seeing how she is the only person so far that remembers her, but she doesn't seem to even notice or care.)"
    if charlotte_intro_option and julia_intro_option and valerie_intro_option:
        p "(But well, this means I can finally start to properly investigate each of them.)"
        p "(Starting next week, I should focus on this investigation now that I learned the ropes of this weird ability.)"
        p "(I better take note of everything I've been through in the last couple of days.)"
        p "(I should also take the time to revise Eileen's...)"
        p "Wait a minute, what does this say? It's upside down, seems like a note."
        e "(Escaping the mind of a person is so you can protect yourself from the dangers they may have. However, this is just in case of emergency.)"
        e "(Ejecting yourself off of someone's mind takes a toll on your own, and it's dangerous on it's own. You get shattered little by little.)"
        e "(More so than it does entering in their minds in the first place, and getting out of there after a day is a natural way to do it.)"
        e "That's why I think that doing this more than 4 times would shatter your mind.)"
        p "(So this means...)"
        p "I CAN'T ESCAPE THEIR MINDS AT WILL ANYMORE!" with vpunch
        p "(Talking about fucking up... So now it will be even more dangerous...)"
        p "(Ah... Well, it's my own fault for not reading everything before jumping in...)"
        p "(But then, I really should try to stay alive, or else... Does that mean, I will end like Eileen if I fail?)"
        "As I said that, I closed my eyes, waiting for a new week, and hopefully solve this once and for all..."
        p "(Wait for me, Eileen...)"
        p "(Good night.)"
        "..."
        $ clock.day = 0
        $ clock.hourclock = 0
        $ persistent.introfull = True
        jump menu_select
    else:
        p "(If tomorrow will be as dangerous as it was today, I better try to stay calm.)"
        p "(After all, this is for Eileen, she trusted me to bring her back, and even if I have to face someone like Miss Julia...)"
        p "(I don't know what's more intimidating, killer robots, or the ice queen herself.)"
        "I shivered before I finally fell asleep."
        p "(Good night.)"
        $ clock.hourclock = 0
        jump introduction

label introduction_end_valerie:

    $ clock.hourclock = 4
    scene bg room with fade
    p "(I'm finally home.)"
    p "(Despite not having that much activity today, I feel like I was hit by a truck.)"
    p "(And something tells me it has to do with my little experience going inside Miss Valerie's mind.)"
    p "(I'm still amazed by what I saw. And I mean everything.)"
    p "(A minute more, and I could have died... Even Miss Valerie was worried in there.)"
    p "(But her own strenght in there is something to be scared off.)"
    p "(I also saw Eileen in there. Not to mention, I'm still not sure about the connection between Miss Valerie and Eileen.)"
    if charlotte_intro_option and julia_intro_option and valerie_intro_option:
        p "(But well, this means I can finally start to properly investigate each of them.)"
        p "(Starting next week, I should focus on this investigation now that I learned the ropes of this weird ability.)"
        p "(I better take note of everything I've been through in the last couple of days.)"
        p "(I should also take the time to revise Eileen's...)"
        p "Wait a minute, what does this say? It's upside down, seems like a note."
        e "(Escaping the mind of a person is so you can protect yourself from the dangers they may have. However, this is just in case of emergency.)"
        e "(Ejecting yourself off of someone's mind takes a toll on your own, and it's dangerous on it's own. You get shattered little by little.)"
        e "(More so than it does entering in their minds in the first place, and getting out of there after a day is a natural way to do it.)"
        e "That's why I think that doing this more than 4 times would shatter your mind.)"
        p "(So this means...)"
        p "I CAN'T ESCAPE THEIR MINDS AT WILL ANYMORE!" with vpunch
        p "(Talking about fucking up... So now it will be even more dangerous...)"
        p "(Ah... Well, it's my own fault for not reading everything before jumping in...)"
        p "(But then, I really should try to stay alive, or else... Does that mean, I will end like Eileen if I fail?)"
        "As I said that, I closed my eyes, waiting for a new week, and hopefully solve this once and for all..."
        p "(Wait for me, Eileen...)"
        p "(Good night.)"
        "..."
        $ clock.day = 0
        $ clock.hourclock = 0
        $ persistent.introfull = True
        jump menu_select
    else:
        p "(And if I'm honest... I do want to go back into her mind.)"
        p "(If it wasn't so dangerous I'd be more eager, though.)"
        p "(And Miss Valerie is a really pleasant person to be around.)"
        p "(If, again, a dangerous individual, even if she doesn't mean it.)"
        "I couldn't help but think about that beach I saw as my eyes closed..."
        p "(Good night.)"
        $ clock.hourclock = 0
        jump introduction

label introduction_end:

    $ clock.hourclock = 4
    scene bg room with fade
    show screen clock_marker with dissolve
    "(Starting next week, I should focus on this investigation now that I learned the ropes of this weird ability.)"
    p "(I better take note of everything I've been through in the last couple of days.)"
    p "(I should also take the time to revise Eileen's...)"
    p "Wait a minute, what does this say? It's upside down, seems like a note."
    e "(Escaping the mind of a person is so you can protect yourself from the dangers they may have. However, this is just in case of emergency.)"
    e "(Ejecting yourself off of someone's mind takes a toll on your own, and it's dangerous on it's own. You get shattered little by little.)"
    e "(More so than it does entering in their minds in the first place, and getting out of there after a day is a natural way to do it.)"
    e "That's why I think that doing this more than 4 times would shatter your mind.)"
    p "(So this means...)"
    p "I CAN'T ESCAPE THEIR MINDS AT WILL ANYMORE!" with vpunch
    p "(Talking about fucking up... So now it will be even more dangerous...)"
    p "(Ah... Well, it's my own fault for not reading everything before jumping in...)"
    p "(But then, I really should try to stay alive, or else... Does that mean, I will end like Eileen if I fail?)"
    "As I said that, I closed my eyes, waiting for a new week, and hopefully solve this once and for all..."
    p "(Wait for me, Eileen...)"
    p "(Good night.)"
    "..."
    $ clock.day = 0
    $ clock.hourclock = 0
    $ persistent.introfull = True
    jump menu_select

label day_end_charlotte:

    $ clock.hourclock = 4
    scene bg room with fade
    p "Finally home..."
    $ scenes += 1

    if charlottescenes == 1:
        p "(I... I can't believe it...)"
        p "(This feels like some kind of bad trip. Did I really touched Charlotte in a bathroom stall while her friends were listening outside?)"
        p "(What's more, she touched herself and came in front of me...)"
        p "(Really, I understand why she was so embarrassed. But she got herself into that.)"
        p "(Still, if there is something I now know for sure is that she really cares about what people think about her.)"
        p "(To the point she went this far with me...)"
        p "(And... What with the flash at the end? I think she is so embarrassed that this may be a good opportunity to try going into her mind next time.)"
        p "(I'm sure that just by mentioning this it will have the job done as it was today, and the only reason I didn't today was because she ran away.)"
        p "(Speaking of which, she avoided all my questions as to why Eileen and her stopped being friends in the first place...)"
        p "(But now I know more about their relationship. Maybe next time, her mind will give me more of an insight... But for now...)"
        p "I will get to the bottom of this. Even if Charlotte is such a handful. Oh well."
        p "Good night."
        "I closed my eyes, waiting for whatever tomorrow could bring."
        scene black with fade
        jump menu_select
    if charlottescenes == 2:
        p "(I still don't get her. She... She seems like a decent person at times. But she is so obsessed with her social status...)"
        p "(And man, what with her mind? Is a complete fucking chaos in there. The way things work in there makes no sense. Her society is not sustainable.)"
        p "(Even her technique while... Well, sucking my dick wasn't the best, she was very clumsy but... It still felt nice.)"
        p "(Her soldiers... They seem decent, but what the hell was that at night? And herself... She keeps shifting between a despicable leader.)"
        p "(But then she tries to be nice. She even helped me escape. I... I don't know what would have happened if she didn't help me there.)"
        p "(But most importantly, Eileen have been in there, clearly. She doesn't know who I am, but knows who Eileen is.)"
        p "(Makes sense, Eileen always have had this clock before me, after all.)"
        p "(But before we could even continue with Eileen's case, she got mad and fled for some reason...)"
        p "(I guess I was rude with her about... About what happened before, but, oh man, if she knew what went inside her mind...)"
        p "You know, I can't make heads or tails about her mind. Everything is so oddly confusing, including her. But I guess that's how a mind works."
        p "Hm... I wonder if Eileen have even been inside my mind..."
        p "... {i}sigh{/i}... I will find you sooner or later, Eileen, even if I have to keep dodging bullets, it seems."
        p "But as usual, I have more questions than answers..."
        "I couldn't even keep my eyes open from all the stress I endured today."
        p "Good night."
        p "Shit... My arms..."
        scene black with fade
        jump menu_select
    if charlottescenes == 3:
        p "..."
        p "(I'm tired, surprised, and scared at the same time. But, in a weird turn of events, I'm also hopeful.)"
        p "(Seems like I was finally able to go through Charlotte, I don't know what happened, but she seems to be willing cooperate.)"
        p "(So this pretty much means I'm one step closer to Eileen! Or so I hope. I'm very curious about what happened between them, specially because they don't seem to fit together.)"
        p "(But who knows. Maybe this means I don't need to go inside her mind anymore. And I'd be glad, her mind is a fucked up place indeed. And dangerous.)"
        p "..."
        p "(But... Getting involved with her does have consequences. Claire is clearly hitting on me, and Jean... She wants me dead, for some reason.)"
        p "(Both of them slid their phone numbers into my pockets, with lovely notes on them. \"If you want to wet that thick cock\", and \"You better add me, worm\".)"
        p "(Not hard to guess who is who. I hesitated in adding them both, but I don't want to die, as different as those two could kill me.)"
        p "(I sent them a message and they replied right away. Jean with a simple \"ok\" and Claire with a kiss emoji...)"
        p "No matter how you look at it... Getting close to Charlotte is getting dangerous, if it's not her mind and her soldiers, it's her friends and their dangerous mind games."
        p "And yet, I feel like this hides more than it looks like. I figured, I can even learn more about Charlotte through her friends, they seem close enough."
        p "Close enough to show me their bodies as I fake-fucked Charlotte..."
        "Before I got hard again from the thought of what happened, I decided to roll around bed, hoping to close my eyes sooner than later."
        p "Good night..."
        scene black with fade
        jump menu_select
    if charlottescenes == 4:
        p "(Well... What a day. What can I say... Let me try to go through it very quickly.)"
        p "(So, Charlotte mind is going through some kind of civil uproar. Which is very weird and... Oddly complicated.)"
        p "(At this point, I'm not exactly sure what that even can mean, but being her mind, it must be related to something.)"
        p "(That's something I do need to find out. After all, that Charlotte seems nice, and her soldiers too.)"
        p "(Speaking of nice, Charlotte herself... She is incredibly nice, and it makes me wonder why she acts otherwise.)"
        p "(And both Charlottes makes me beg a question: Who is the real Charlotte. And I mean, both of them have a soft side.)"
        p "(That's why I wonder, what is the true side? The soft side? The harsh side? Hmmm...)"
        p "(And well, I also learned about Eileen inside of Charlotte's mind. It makes sense, they were best friends.)"
        p "(And the most shocking revelation of them all: The reason why Charlotte is not friends with Eileen anymore.)"
        p "(Sounds to me that it was something neither of them wanted, but it happened... BECAUSE OF ME!)"
        p "I wasn't even aware of any of that. I mean, I stopped frequenting Eileen years ago, and I was never very familiar with Charlotte..."
        p "A lot of questions were answered, but a lot more questions are lingering, and every time things get interrupted..."
        p "I... I hope this trend doesn't last any longer... I just want Eileen to be back, and I'm sure Charlotte wants that too."
        "My eyes were closing already."
        p "Despite being an uneventful day, sort of, going inside someone's mind does tire me emotionally and mentally."
        p "I'm sure that... From now on, things will work out ok."
        p "Good night!"
        scene black with fade
        jump menu_select_charlotte
    if charlottescenes == 5:
        p "(Trying to think about today's day... What a disaster. And it started so so great... How did it go the way it did!?)"
        p "(I just wanted to get to know Charlotte more. For Eileen, of course. And well, I did learn about a very deep part of her.)"
        p "(Can't deny it felt amazing, though. But it's certainly not what I need right now... Again, not complaining, but what about Eileen?)"
        p "(And again, her friends are the biggest obstacle here. Charlotte... Charlotte is considered the queen bee. But who is she really?)"
        p "(She certainly doesn't seem as bad as I thought she was, at least by herself. But with her friends she looks like a different person.)"
        p "(And well, one of her friends wants me dead and the other wants me inside her. How things came to this in the first place?)"
        p "(Further more, I do have a theory, but nothing concrete. Next time we meet, I will surely get some answers.)"
        p "That's it, if my theory proves to be true, I should have a free pass to Charlotte's mind."
        p "As long as I get to the bottom of this... Charlotte is kind of a mystery, if I think about it. Nothing I thought I knew about her seems to be true."
        "Before I slept I quickly checked my phone. I was new messages in 3 chats, what a surprise."
        p "Message one: A picture of me fucking with Charlotte. Charming."
        p "Message two: \"You better think about what I said today...\" followed by a wink face."
        p "And last message: \"Looking forward for the next time\" with an smiley face."
        p "... These get more and more confused each time. It's even hard to tell who sent what, but I still can."
        "Exhausted from all the fucking from today, I was more than willing to sleep."
        p "Good night."
        scene black with fade
        jump menu_select_charlotte
    if charlottescenes == 6:
        p "What a fucking disaster."
        p "(Everything that could have gone wrong today did. I've gone through today's events over and over.)"
        p "(Maybe if I did something differently things would have been better...? But, I just did what I had to.)"
        p "(And now, everyone basically hates me or don't want to talk to me.)"
        "PING"
        p "(Except for...)"
        cla "Is everything ok? Neither Charlotte nor Jean are answering my messages. Please answer :("
        p "Yeah, I mean... I think I screwed up... It's too complicated to explain, and even if it wasn't, I don't even know where to begin."
        p "(On top of all of this, I also saw Golem murdered in front of me, and I couldn't do a single thing.)"
        p "(I couldn't protect Golem or Charlotte, and... I'm sure this is all my fault too...)"
        "PING"
        cla "Do you need to talk? I'm not sure if I can help, but I can do my best."
        p "Thanks, Claire, but I think I need to sleep right now, it was quite a long day... I'm sorry. Ttyl."
        p "(There are just so many things in my head right now, I... I'm not even sure how I'm going to face Charlotte.)"
        "I made sure to turn off my phone before going to sleep... And it didn't take long."
        p "Normally, this would keep me up for quite some time. But not today..."
        p "Good night."
        scene black with fade
        "This is marks the end of the first half of Charlotte's route!"
        "Next release will complete her story and include her endings."
        "Her route was very challenging to write so far, to say the least. However, I'm really liking how it is shaping up and the resolution it will have."
        "I planned for her whole story to be ended in this very patch, but it prolongued a lot more than I expected. This is twice as long as her entire introduction."
        "I hope you like the direction the story is taken. Here's a little extra for your interest and effort:"
        show charlotte_demo_end with dissolve
        "Stay tuned for the completion of her story."
        show galcharlotteself1
        hide galcharlotteself1
        show galcharlotteself2
        hide galcharlotteself2
        show chibicharlotte1
        hide chibicharlotte1
        show chibicharlotte2
        hide chibicharlotte2
        if charlotte_sixth_day_finish and julia_fourth_day_finish and valerie_fourth_day_finish and laura_second_day_finish:
            jump demo_end
        else:
            jump menu_select

label day_end_julia:

    $ clock.hourclock = 4
    scene bg room with fade
    p "Finally home..."
    $ scenes += 1

    if juliascenes == 1:
        p "(This is... Humiliating. Miss Julia toyed with me the whole time.)"
        p "(She didn't only make me wait on her, but made me cum with her foot alone.)"
        p "(I manage to see her naked, but... At the cost of my disgnity, it seems.)"
        p "(Miss Julia was acting very very thirsty, more so than usual, and she usually is very thirsty.)"
        p "(But that even feels even more odd... I can't exactly point at it, but it is.)"
        p "(Furthermore, I know as a matter of fact that she knows more than she claims she does.)"
        p "(Between all her notes, I found something very interesting.)"
        p "(I found a picture of this very watch I'm wearing.)" with flash
        p "(The watch Eileen left behind...)"
        p "(I will ask her about this as soon as possible... But, with her last warning...)"
        p "(I'm very afraid of what can happen. This is certainly a very delicated matter.)"
        p "(Whatever this watch is, and wherever Eileen got it, Miss Julia clearly has an answer.)"
        p "(And that answer may lie inside her mind. So very soon...)"
        p "Miss Julia can't intimidate me forever. Even if I'm risking my life, I will find out."
        p "Good night."
        "I closed my eyes, knowing full well I will have to face Miss Julia later on."
        scene black with fade
        jump menu_select
    if juliascenes == 2:
        p "(Miss Julia basically kept me like a sex slave in her mind for a whole day. While her real self was... A pain in the ass.)"
        p "(But I can't deny, Miss Julia knows a lot about this, but judging by her reaction...)"
        p "(Sounds like Eileen did something very terrible to her. And it would make sense.)"
        p "(Out of all my suspects at the moment, Miss Julia was the closes to Eileen. Eileen was her best student, so...)"
        p "(What if Eileen stole this watch from her? After all, it would make all the pieces fall together.)"
        p "(But even if that was true, it doesn't put me any closer to bringing Eileen back, just an explanation as to why she ended in this mess.)"
        p "(What reason could Eileen have to steal this watch? Now that I remember, Eileen never mentioned much about her own life back then...)"
        p "(And to make matters worse, dealing with Miss Julia now will be even harder than before, if that's even possible.)"
        p "(She threatened me inside her mind and outside of it. She goes from being a crazy nymphomaniac to a very hostile ice queen in a second.)"
        p "But I won't stop here. I will bring Eileen back, and this is the best lead I have right now."
        "Even though I don't feel psysically tired from being abused for a full day by multiple androids, my mind was leaving my body."
        p "I can't keep my eyes open anymore..."
        p "Good night."
        scene black with fade
        jump menu_select
    if juliascenes == 3:
        p "(... Damn her. She is... She is kind of ruthless. She is the ice queen, after all, she knows what she wants and go for it.)"
        p "(Miss Julia. You are my biggest lead and yet the biggest mystery. How can someone that hides so much avoid being investigated so often!)"
        p "(Well, of course I know how... Despite everything, she is way too hot and charming, so of course she gets away with it easily.)"
        p "(... I need to find a way to avoid that from happening, so I need to be firm and sharp, and keep it in my pants, of course.)"
        p "(Even though I didn't interact with her as much, I got hold of very interesting information. Mom... What is her relationship with Julia?)"
        p "(This all makes less and less sense, but I should be able to use this information to my advantage.)"
        p "(Likewise, I don't know what to think about what we did today either. Did she truly enjoy it? Was she acting? Hmmm... Well... I...)"
        p "(Maybe next time I'll... Wait, next time? Hmm... Well, I hope I can do it again, really, but... She is very obviously trying to manipulate me.)"
        p "I should be careful around her. Also, I... I think I should investigate my mom as well, she seems to be involved."
        "I was starting closing my eyes."
        p "Well, good night."
        scene black with fade
        jump menu_select
    if juliascenes == 4:
        p "(I'm not sure if I should trust Julia. She seems to be honest. But you never know with her.)"
        p "(Well... At least I'm one step close to Eileen, now, or so I hope...)"
        p "(I don't know what happened to her, but I still don't trust that 180 degrees turn. She must be plotting something herself...)"
        p "(Her mind is still as threatening as ever. I almost died, and it's either that or becoming a sex slave.)"
        p "(Eileen was there, though, that much is clear as well. I'm not sure what she did, but Julia is pissed at her, both in reality and in her mind.)"
        p "S-shit... This is confusing, and... Julia was right, I'm in no state of thinking about all of this."
        p "But I need to keep myself sharp and react to anything she tried to do... Soon enough, I will find out!"
        "With conviction and a really weird partnership, I was ready to sleep."
        p "If there's someone who can help me with Eileen, that's Julia..."
        p "Good night!"
        show galjuliaself1
        hide galjuliaself1
        show galjuliaself2
        hide galjuliaself2
        show chibijulia1
        hide chibijulia1
        show chibijulia2
        hide chibijulia2
        scene black with fade
        if charlotte_sixth_day_finish and julia_fourth_day_finish and valerie_fourth_day_finish and laura_second_day_finish:
            jump demo_end
        else:
            jump menu_select

label day_end_valerie:

    $ clock.hourclock = 4
    scene bg room with fade
    p "Finally home..."
    $ scenes += 1

    if valeriescenes == 1:
        p "(Miss Valerie is more of a pervert than I could have thought.)"
        p "(Masturbating inside the storage room of her own gym, not flinching when I was there.)"
        p "(And what's more, she was waiting for me. She let me watch and finish on her, without even touching myself...)"
        p "(I don't know what's wrong with me... But, furthermore, and more important.)"
        p "(Seems like she really knows something about Eileen, and that worries me.)"
        p "(But from her reaction today, this may be an opportunity for me to go inside her mind.)"
        p "(Also, her sister is a very interesting person, specially since they don't look that much alike.)"
        p "(I wonder what's their story but... I don't mean to pray into her life. But... She is evidently sleeping in the gym.)"
        p "I can't fucking feel my body though, holy shit, everything hurts!"
        p "If I need to go another day like this, I wonder what will happen to me..."
        p "But I'm doing this for Eileen... Even though it this be easily avoided if Miss Valerie wasn't... Miss Valerie."
        p "Oh, well, good night."
        "I closed my eyes, trying to sleep on the pain in my muscules."
        scene black with fade
        jump menu_select
    if valeriescenes == 2:
        p "(My god... My body...)"
        p "(And... I'm not only exhausted psysically, but my little experience in Miss Valerie's mind was more intense than I anticipated.)"
        p "(It seems like she is as much of a pervert in her mind as she is in real life. But...)"
        p "(She seems to be way more violent, though. If she is so genuine normally, seems like she is even more inside her own mind...)"
        p "(And today happened two important things. One, she knew Eileen in her mind. And... She seems to be hurt because Eileen left her.)"
        p "(I don't know how long will it take me to get as strong as Miss Valerie. But I don't want to let her down.)"
        p "(That's why I think doing exercise is not half a bad idea, and spending time with Valerie is very nice.)"
        p "(But more importantly: That log book. Valerie told me the page was empty and she was weirded out by that.)"
        p "(The thing is... It wasn't. Eileen's information was right there.)" with flash
        p "(I didn't want to push the subject, since she was looking at the same page I was, she was sure it was empty.)"
        p "Why does Miss Valerie don't remember Eileen or even see information about her? Specially if she have been in her own mind."
        "As I was lying down the bed I was starting to drift away."
        p "Eileen... What are you even into...?"
        p "Good night."
        scene black with fade
        jump menu_select
    if valeriescenes == 3:
        p "(Second tim in a row I feel destroyed after going to the gym, but...)"
        p "(It feels rewarding. I can feel myself becoming stronger. And I could even beat Valerie today! Although... It was an accident, of course.)"
        p "(But I just have to keep going. I got to find out some stuff that may open me her mind, I can't forget about that just yet.)"
        p "(Her conscious self may not be the best help for Eileen, at least not that I'm aware of. But her mind may still hold some clues.)"
        p "(Or so I hope... I feel like I'm hitting a dead end. Why would Eileen want me to investigate Valerie? I can't even see any pattern.)"
        p "(But I trust Eileen and, honestly, I like spending time with Valerie. She is a very cheerful and positive person.)"
        p "(Sex with her was fantastic, she is lovely, and nice... I... Can't really stop thinking about her.)"
        p "(But I can't help but feeling she is hidding something. Whether that something has to do with Eileen or not, I want to know...)"
        p "Trying again wouldn't hurt... I have more reasons to try than not, including... Including Valerie herself."
        "I was thinking three things before falling asleep: Save Eileen, get closer to Valerie, and how much my body hurts."
        p "Good night."
        p "Ouch..."
        jump menu_select
    if valeriescenes == 4:
        p "(It seems like I'm finally getting stronger, the gym is paying off! And what's more...)"
        p "(I got myself a girlfriend today, and I'm glad it is Miss Valerie!)"
        p "(Then again... I was still a bit worried... She was very sad this morning. Nothing like the Valerie I'm used to.)"
        p "(I guess she isn't what she shows to be. None of us are at some degree... I wonder if it's the same with Eileen. What was she hidding?)"
        p "(Speaking of which, I saw her yet again in Valerie's mind. Her messages are confusing, but I assume they mean I'm going the right way!)"
        p "(And speaking of Miss Valerie's mind... Well, yeah, I hope I'm getting stronger, but what exactly are those monsters?)"
        p "(Using simple logic, they may have to do with Valerie's in some way, that is her mind, after all, and I wouldn't be surprised.)"
        p "(Specially with all the data I gathered today about her. Her life is rough, and yet she smiles all the time. She is admirable...)"
        p "(Or maybe just an airhead. But I don't think she is dumb at all. That's why I think there's something about those monsters, specially since they increased size.)"
        p "Well, now I'm free to explore even further. I'm her boyfriend, after all, but this time, I want her to tell me directly!"
        "After all the excitement of today, I was already nodding off."
        p "Well, good night!"
        show galvalerieself1
        hide galvalerieself1
        show galvalerieself2
        hide galvalerieself2
        show chibivalerie1
        hide chibivalerie1
        show chibivalerie2
        hide chibivalerie2
        scene black with fade
        if charlotte_sixth_day_finish and julia_fourth_day_finish and valerie_fourth_day_finish and laura_second_day_finish:
            jump demo_end
        else:
            jump menu_select

label day_end_laura:

    $ clock.hourclock = 4
    scene bg room with fade
    p "Finally home..."
    $ laurascenes += 1
    if laurascenes == 1:
        p "(Mom... I was surely not expecting that full force reaction she had. And I couldn't explain myself at all.)"
        p "(I know mom meant well, but this is way too much, even for her. I think she... Drugged me somehow?)"
        p "(I must be crazy for admitting this: Mom is freaking hot. Like, her body doesn't look like she aged.)"
        p "(That being said, I still find no way why she would do this. Sure, she may be worried, but seriously.)"
        p "(Drugs? A Handjob? And there's still the fact that her mind is a freaking puzzle ever since I went there for the first time.)"
        p "(Luckily, I have enough things to try and push my luck inside her mind... Pushing my luck inside her sounds easier.)"
        p "(And man... That sounds so wrong.)"
        p "(I should go and face her soon...)"
        p "I know I'm alone and all, so I can make this terrible pun before going to sleep: I'm a motherfucker."
        "That pun was so terrible that I got to sleep inmediately. Or maybe because mom made me cum so much."
        p "Good night."
        scene black with fade
        jump menu_select
    if laurascenes == 2:
        p "(My god... My head... My body...)"
        p "(It feels just like I've been ran over by a truck...)"
        p "..."
        p "(What the hell was mom's mind? The whole place seems... Frozen? I'm not sure that's the word.)"
        p "(It's very sketchy in every way. Specially since... I really, really didn't expect to see her there.)"
        p "(But I saw Eileen as I was leaving mom's mind.)" with flash
        p "(And mom was acting so... So weird, I still wonder if that's truly my mom...)"
        p "(She basically ejected me from her mind. I'm sure it wasn't the time yet, I checked the clock.)"
        p "I feel mom is trying to hide something from me. But... Honestly, it isn't the first time."
        p "I'm her son... Why do you have to do this to me, mom..."
        "As soon as I touched the bed I couldn't take it anymore. The mental and physical stress were weighting my eyes."
        p "Good night."
        scene black with fade
        show gallauraself1
        hide gallauraself1
        show gallauraself2
        hide gallauraself2
        show chibilaura1
        hide chibilaura1
        show chibilaura2
        hide chibilaura2
        "This is marks the end of the first half of Laura introduction!"
        "Next release will complete her introduction along the complete route of Charlotte."
        "However, I'm still thinking if I should, since Laura route is very spoiler heavy for the other routes, hence why she was planned originally as an unlockable character."
        "I do hope that you like this little taste of her story, though, since I'm actually enjoyed it quite a lot."
        "And so you don't go empty handed, here's a little something:"
        show laura_demo_end with dissolve
        "Look forward to it."
        if charlotte_sixth_day_finish and julia_fourth_day_finish and valerie_fourth_day_finish and laura_second_day_finish:
            jump demo_end
        else:
            jump menu_select
