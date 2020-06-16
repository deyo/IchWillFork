###############################################################
########### CHARACTERS ########################################
###############################################################

define narrator = Character(ctc="ctc_charlotte", what_style="say_thought", window_background="custom_textbox")
define e = Character("Eileen", image="eileen", ctc="ctc_charlotte", who_color="#0a7af5", window_background="custom_textbox", namebox_backgroud="custom_namebox")
define p = Character("[povname]", ctc="ctc_charlotte", window_background="custom_textbox", namebox_backgroud="custom_namebox", who_color="#ffffff")
define c = Character("Charlotte", image="charlotte", ctc="ctc_charlotte", who_color="#be24db", window_background="custom_textbox", namebox_backgroud="custom_namebox")
define j = Character("Julia", image="julia", ctc="ctc_charlotte", window_background="custom_textbox", namebox_backgroud="custom_namebox")
define v = Character("Valerie", image="valerie", ctc="ctc_charlotte", who_color="#00560e", window_background="custom_textbox", namebox_backgroud="custom_namebox")
define l = Character("Laura", image="laura", ctc="ctc_charlotte", who_color="#ff8f00", window_background="custom_textbox", namebox_backgroud="custom_namebox")

define sol = Character("Soldier", image="soldier", ctc="ctc_charlotte", who_color="#920009", window_background="custom_textbox", namebox_backgroud="custom_namebox")
define cla = Character("Claire", image="claire", ctc="ctc_charlotte", who_color="#fff08e", window_background="custom_textbox", namebox_backgroud="custom_namebox")
define je = Character("Jean", image="jean", ctc="ctc_charlotte", who_color="#50a8d5", window_background="custom_textbox", namebox_backgroud="custom_namebox")

define ch = Character("Chloe", image="chloe", ctc="ctc_charlotte", who_color="#70619e", window_background="custom_textbox", namebox_backgroud="custom_namebox")
define ogr = Character("Ogre", image="ogr", ctc="ctc_charlotte", who_color="#b74852", window_background="custom_textbox", namebox_backgroud="custom_namebox")
define orc = Character("Orc", image="orc", ctc="ctc_charlotte", who_color="#577d60", window_background="custom_textbox", namebox_backgroud="custom_namebox")

define rob = Character("Robot", image="robot", what_font="digital-7.ttf", what_size=28, ctc="ctc_charlotte", who_color="#5574aa", window_background="custom_textbox", namebox_backgroud="custom_namebox")

define de = Character("Asma", image="devil", ctc="ctc_charlotte", who_color="#971b2a", window_background="custom_textbox", namebox_backgroud="custom_namebox")
define an = Character("Raquel", image="angel", ctc="ctc_charlotte", who_color="#e2c700", window_background="custom_textbox", namebox_backgroud="custom_namebox")

define unk = Character("???", ctc="ctc_charlotte", window_background="custom_textbox", namebox_backgroud="custom_namebox")
define unk2 = Character("???", ctc="ctc_charlotte", who_color="#e2c700", window_background="custom_textbox", namebox_backgroud="custom_namebox")

###############################################################
########### BACKGROUNDS #######################################
###############################################################

init python:
    class TransitionConditionSwitch(renpy.Displayable):
        def __init__(self, transition, *args, **kwargs):
            super(TransitionConditionSwitch, self).__init__(**kwargs)
            self.transition = transition
            self.d = zip(args[0::2], args[1::2])
            self.time_reset = True
            self.old_d = None
            self.current_d = None
            self.ta = None
            self.old_st = 0
        def render(self, width, height, st, at):
            if self.ta is None:
              self.per_interact()
            if self.time_reset:
                self.time_reset = False
                self.st = st
                self.at = at
                self.old_st = 0
            if st < self.old_st:
              self.st, self.at, st, at = 0, 0, 1000000.0, 1000000.0
            self.old_st = st
            return renpy.render(self.ta, width, height, st-self.st, at-self.at)
        def per_interact(self):
            for name, d in self.d:
                if eval(name):
                    change_to = d
                    break
            if change_to is not self.current_d:
                self.time_reset = True
                self.old_d = self.current_d
                self.current_d = change_to
                if self.old_d is None:
                    self.old_d = self.current_d
                self.ta = anim.TransitionAnimation(self.old_d, 0.00, self.transition, self.current_d)
                renpy.redraw(self, 0)
        def visit(self):
            return [self.ta]

image bg room = TransitionConditionSwitch(Dissolve(0.5),
    "clock.time == 'MORNING'", "images/Backgrounds/bg room morning.webp",
    "clock.time == 'NOON'", "images/Backgrounds/bg room noon.webp",
    "True", "images/Backgrounds/bg room night.webp")
image bg uni_hall = TransitionConditionSwitch(Dissolve(0.5),
    "clock.time == 'MORNING'", "images/Backgrounds/bg uni_hall morning.webp",
    "clock.time == 'NOON'", "images/Backgrounds/bg uni_hall noon.webp",
    "True", "images/Backgrounds/bg uni_hall night.webp")
image bg uni = TransitionConditionSwitch(Dissolve(0.5),
    "clock.time == 'MORNING'", "images/Backgrounds/bg uni morning.webp",
    "clock.time == 'NOON'", "images/Backgrounds/bg uni noon.webp",
    "True", "images/Backgrounds/bg uni night.webp")

image bg classroom = TransitionConditionSwitch(Dissolve(0.5),
    "clock.time == 'MORNING'", "images/Backgrounds/bg classroom morning.webp",
    "clock.time == 'NOON'", "images/Backgrounds/bg classroom noon.webp",
    "True", "images/Backgrounds/bg classroom night.webp")
image bg bathroom = TransitionConditionSwitch(Dissolve(0.5),
    "clock.time == 'MORNING'", "images/Backgrounds/bg bathroom morning.webp",
    "clock.time == 'NOON'", "images/Backgrounds/bg bathroom noon.webp",
    "True", "images/Backgrounds/bg bathroom night.webp")
image bg castle_town = TransitionConditionSwitch(Dissolve(0.5),
    "clock.time == 'MORNING'", "images/Backgrounds/bg castle_town morning.webp",
    "clock.time == 'NOON'", "images/Backgrounds/bg castle_town noon.webp",
    "True", "images/Backgrounds/bg castle_town night.webp")
image bg castle = TransitionConditionSwitch(Dissolve(0.5),
    "clock.time == 'MORNING'", "images/Backgrounds/bg castle morning.webp",
    "clock.time == 'NOON'", "images/Backgrounds/bg castle noon.webp",
    "True", "images/Backgrounds/bg castle night.webp")
image bg castle_hall = TransitionConditionSwitch(Dissolve(0.5),
    "clock.time == 'MORNING'", "images/Backgrounds/bg castle_hall morning.webp",
    "clock.time == 'NOON'", "images/Backgrounds/bg castle_hall noon.webp",
    "True", "images/Backgrounds/bg castle_hall night.webp")
image bg castle_room = TransitionConditionSwitch(Dissolve(0.5),
    "clock.time == 'MORNING'", "images/Backgrounds/bg castle_room morning.webp",
    "clock.time == 'NOON'", "images/Backgrounds/bg castle_room noon.webp",
    "True", "images/Backgrounds/bg castle_room night.webp")
image bg dungeon = TransitionConditionSwitch(Dissolve(0.5),
    "clock.time == 'MORNING'", "images/Backgrounds/bg dungeon.webp",
    "clock.time == 'NOON'", "images/Backgrounds/bg dungeon.webp",
    "True", "images/Backgrounds/bg dungeon.webp")
image bg dungeon_cell = TransitionConditionSwitch(Dissolve(0.5),
    "clock.time == 'MORNING'", "images/Backgrounds/bg dungeon_cell.webp",
    "clock.time == 'NOON'", "images/Backgrounds/bg dungeon_cell.webp",
    "True", "images/Backgrounds/bg dungeon_cell.webp")


image bg teachers = TransitionConditionSwitch(Dissolve(0.5),
    "clock.time == 'MORNING'", "images/Backgrounds/bg teachers morning.webp",
    "clock.time == 'NOON'", "images/Backgrounds/bg teachers noon.webp",
    "True", "images/Backgrounds/bg teachers night.webp")
image bg tutor = TransitionConditionSwitch(Dissolve(0.5),
    "clock.time == 'MORNING'", "images/Backgrounds/bg tutor morning.webp",
    "clock.time == 'NOON'", "images/Backgrounds/bg tutor noon.webp",
    "True", "images/Backgrounds/bg tutor night.webp")

image bg sports = TransitionConditionSwitch(Dissolve(0.5),
    "clock.time == 'MORNING'", "images/Backgrounds/bg sports morning.webp",
    "clock.time == 'NOON'", "images/Backgrounds/bg sports noon.webp",
    "True", "images/Backgrounds/bg sports night.webp")
image bg gym = TransitionConditionSwitch(Dissolve(0.5),
    "clock.time == 'MORNING'", "images/Backgrounds/bg gym morning.webp",
    "clock.time == 'NOON'", "images/Backgrounds/bg gym noon.webp",
    "True", "images/Backgrounds/bg gym night.webp")
image bg gym_storage = TransitionConditionSwitch(Dissolve(0.5),
    "clock.time == 'MORNING'", "images/Backgrounds/bg gym_storage morning.webp",
    "clock.time == 'NOON'", "images/Backgrounds/bg gym_storage noon.webp",
    "True", "images/Backgrounds/bg gym_storage night.webp")
image bg island = TransitionConditionSwitch(Dissolve(0.5),
    "clock.time == 'MORNING'", "images/Backgrounds/bg island morning.webp",
    "clock.time == 'NOON'", "images/Backgrounds/bg island noon.webp",
    "True", "images/Backgrounds/bg island night.webp")
image bg jungle = TransitionConditionSwitch(Dissolve(0.5),
    "clock.time == 'MORNING'", "images/Backgrounds/bg jungle morning.webp",
    "clock.time == 'NOON'", "images/Backgrounds/bg jungle noon.webp",
    "True", "images/Backgrounds/bg jungle night.webp")
image bg camp = TransitionConditionSwitch(Dissolve(0.5),
    "clock.time == 'MORNING'", "images/Backgrounds/bg camp morning.webp",
    "clock.time == 'NOON'", "images/Backgrounds/bg camp noon.webp",
    "True", "images/Backgrounds/bg camp night.webp")

image bg laura_hall = TransitionConditionSwitch(Dissolve(0.5),
    "clock.time == 'MORNING'", "images/Backgrounds/bg laura morning.webp",
    "clock.time == 'NOON'", "images/Backgrounds/bg laura noon.webp",
    "True", "images/Backgrounds/bg laura night.webp")

###############################################################
########### EFFECTS AND STYLES ################################
###############################################################

define flash = Fade(.25, 0, .75, color="#fff")
define dflash = ComposeTransition(dissolve, flash, None)
define vflash = ComposeTransition(flash, vpunch, None)
define pflash = ComposeTransition(flash, pixellate, None)

define logodissolve1 = MultipleTransition([
    False, Dissolve(0.5),
    "images/Miscellaneous/logo1.webp", Pause(1.5, hard=True),
    "images/Miscellaneous/logo1.webp", dissolve,
    True])

define logodissolve2 = MultipleTransition([
    False, Dissolve(0.5),
    "images/Miscellaneous/logo2.webp", Pause(1.5, hard=True),
    "images/Miscellaneous/logo2.webp", dissolve,
    True])

define logodissolve_charlotte = MultipleTransition([
    False, Dissolve(0.5),
    "images/Miscellaneous/galcharlotteself1.webp", Pause(1.5, hard=True),
    "images/Miscellaneous/galcharlotteself1.webp", dissolve,
    True])

define logodissolve_julia = MultipleTransition([
    False, Dissolve(0.5),
    "images/Miscellaneous/galjuliaself1.webp", Pause(1.5, hard=True),
    "images/Miscellaneous/galjuliaself1.webp", dissolve,
    True])

define logodissolve_valerie = MultipleTransition([
    False, Dissolve(0.5),
    "images/Miscellaneous/galvalerieself1.webp", Pause(1.5, hard=True),
    "images/Miscellaneous/galvalerieself1.webp", dissolve,
    True])

define logodissolve_laura = MultipleTransition([
    False, Dissolve(0.5),
    "images/Miscellaneous/gallauraself1.webp", Pause(1.5, hard=True),
    "images/Miscellaneous/gallauraself1.webp", dissolve,
    True])

define charaleft = Position(xpos=0.35, ypos=1.0)
define chararight = Position(xpos=0.65, ypos=1.0)
define charaleftmost = Position(xpos=0.20, ypos=1.0)
define chararightmost = Position(xpos=0.80, ypos=1.0)

###############################################################
########### ROUTE FLAGS #######################################
###############################################################

default charlotte_intro_option = False
default julia_intro_option = False
default valerie_intro_option = False

default charlotte_first_day_finish = False
default charlotte_second_day_finish = False
default charlotte_third_day_finish = False
default charlotte_fourth_day_finish = False
default charlotte_fifth_day_finish = False
default charlotte_sixth_day_finish = False
default charlotte_seventh_day_finish = False
default charlotte_eighth_day_finish = False
default julia_first_day_finish = False
default julia_second_day_finish = False
default julia_third_day_finish = False
default julia_fourth_day_finish = False
default valerie_first_day_finish = False
default valerie_second_day_finish = False
default valerie_third_day_finish = False
default valerie_fourth_day_finish = False
default laura_first_day_finish = False
default laura_second_day_finish = False

default scenes = 0
default charlottescenes = 0
default juliascenes = 0
default valeriescenes = 0
default laurascenes = 0
default intropoints = 0
default charlotte_point = 0
default julia_point = 0
default valerie_point = 0
default laura_point = 0
default eileen_point = 0
default psychepoints = 0

default wardrobe_valerie = False
default desk_valerie = False
default diary_valerie = False
default behind_wardrobe_valerie = False

###############################################################
########### MENUS AND SCREENS #################################
###############################################################

screen introduction_menu:

    add "logo1"
    add Solid("#000a")
    text "{font=Digital-Medium.ttf}WHO SHOULD I GO AND MEET TODAY?{/font}" xalign 0.5 yalign 0.05 size 50
    textbutton "{font=Digital-Medium.ttf}What was my name again?{/font}" xalign 0.95 yalign 0.95 action Jump("change_name")

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        if charlotte_intro_option == False:
            imagebutton auto "images/Menu Icons/charlotte_%s.webp" action Jump("introduction_charlotte")
        if julia_intro_option == False:
            imagebutton auto "images/Menu Icons/julia_%s.webp" action Jump("introduction_julia")
        if valerie_intro_option == False:
            imagebutton auto "images/Menu Icons/valerie_%s.webp" action Jump("introduction_valerie")
    if charlotte_intro_option == False or julia_intro_option == False or valerie_intro_option == False:
        hbox:
            xalign 0.5
            yalign 0.85
            if persistent.introfull:
                textbutton "I already know them, though" action Jump("introduction_end")

screen menu_select:

    if julia_third_day_finish:
        add "logo2"
    else:
        add "logo1"
    add Solid("#000a")
    text "{font=Digital-Medium.ttf}WHO SHOULD I INVESTIGATE TODAY?{/font}" xalign 0.5 yalign 0.05 size 50
    textbutton "{font=Digital-Medium.ttf}What was my name again?{/font}" xalign 0.95 yalign 0.95 action Jump("change_name")
    textbutton "{font=Digital-Medium.ttf}Investigation Log{/font}" xalign 0.05 yalign 0.95 action Show("investigation", dissolve)

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 5
        hbox:
            xalign 0.5
            spacing 20
            showif charlotte_sixth_day_finish == False:
                imagebutton auto "images/Menu Icons/charlotte_%s.webp" action Jump("charlotte_select")
            showif julia_fourth_day_finish == False:
                imagebutton auto "images/Menu Icons/julia_%s.webp" action Jump("julia_select")
            showif valerie_fourth_day_finish == False:
                imagebutton auto "images/Menu Icons/valerie_%s.webp" action Jump("valerie_select")
        hbox:
            xalign 0.5
            spacing 20
            showif julia_third_day_finish:
                showif laura_second_day_finish == False:
                    imagebutton auto "images/Menu Icons/laura_%s.webp" action Jump("laura_select")
            showif persistent.charlotte_full_ending and persistent.julia_full_ending and persistent.valerie_full_ending and persistent.laura_full_ending:
                imagebutton idle "images/Menu Icons/eileen_%s.webp" action Jump("eileen_select")

screen menu_select_charlotte:

    add "galcharlotteself1"
    add Solid("#000a")
    text "{font=Digital-Medium.ttf}DO I NEED TO DO ANYTHING ELSE?{/font}" xalign 0.5 yalign 0.05 size 50
    textbutton "{font=Digital-Medium.ttf}What was my name again?{/font}" xalign 0.95 yalign 0.95 action Jump("change_name")
    textbutton "{font=Digital-Medium.ttf}Investigation Log{/font}" xalign 0.05 yalign 0.95 action Show("investigation", dissolve)

    vbox:
        xalign 0.5
        yalign 0.5
        textbutton "{font=Digital-Medium.ttf}CONTINUE{/font}" xalign 0.95 yalign 0.95 action Jump("charlotte_select_route")


label charlotte_select:

    if charlotte_first_day_finish == False and charlotte_second_day_finish == False and charlotte_third_day_finish == False:
        jump first_day_charlotte
    elif charlotte_first_day_finish == True and charlotte_second_day_finish == False and charlotte_third_day_finish == False:
        jump second_day_charlotte
    elif charlotte_first_day_finish == True and charlotte_second_day_finish == True and charlotte_third_day_finish == False:
        jump third_day_charlotte
    elif charlotte_first_day_finish == True and charlotte_second_day_finish == True and charlotte_third_day_finish == True:
        jump fourth_day_charlotte

label charlotte_select_route:

    if charlotte_fifth_day_finish == False and charlotte_sixth_day_finish == False and charlotte_seventh_day_finish == False:
        jump charlotte_one
    elif charlotte_fifth_day_finish == True and charlotte_sixth_day_finish == False and charlotte_seventh_day_finish == False:
        jump charlotte_two
    elif charlotte_fifth_day_finish == True and charlotte_sixth_day_finish == True and charlotte_seventh_day_finish == False:
        jump charlotte_three
    elif charlotte_fifth_day_finish == True and charlotte_sixth_day_finish == True and charlotte_seventh_day_finish == True:
        jump charlotte_four

label julia_select:

    if julia_first_day_finish == False and julia_second_day_finish == False and julia_third_day_finish == False:
        jump first_day_julia
    elif julia_first_day_finish == True and julia_second_day_finish == False and julia_third_day_finish == False:
        jump second_day_julia
    elif julia_first_day_finish == True and julia_second_day_finish == True and julia_third_day_finish == False:
        jump third_day_julia
    elif julia_first_day_finish == True and julia_second_day_finish == True and julia_third_day_finish == True:
        if julia_fourth_day_finish == False:
            jump fourth_day_julia
        elif julia_fourth_day_finish == True:
            jump fourth_day_end

label valerie_select:

    if valerie_first_day_finish == False and valerie_second_day_finish == False and valerie_third_day_finish == False:
        jump first_day_valerie
    elif valerie_first_day_finish == True and valerie_second_day_finish == False and valerie_third_day_finish == False:
        jump second_day_valerie
    elif valerie_first_day_finish == True and valerie_second_day_finish == True and valerie_third_day_finish == False:
        jump third_day_valerie
    elif valerie_first_day_finish == True and valerie_second_day_finish == True and valerie_third_day_finish == True:
        if valerie_fourth_day_finish == False:
            jump fourth_day_valerie
        elif valerie_fourth_day_finish == True:
            jump fourth_day_end

label laura_select:

    if laura_first_day_finish == False and laura_second_day_finish == False:
        jump first_day_laura
    elif laura_first_day_finish == True and laura_second_day_finish == False:
        jump second_day_laura

#    if laura_first_day_finish == False and laura_second_day_finish == False and laura_third_day_finish == False:
#        jump first_day_laura
#    elif laura_first_day_finish == True and laura_second_day_finish == False and laura_third_day_finish == False:
#        jump second_day_laura
#    elif laura_first_day_finish == True and laura_second_day_finish == True and laura_third_day_finish == False:
#        jump third_day_laura
#    elif laura_first_day_finish == True and laura_second_day_finish == True and laura_third_day_finish == True:
#        if laura_fourth_day_finish == False:
#            jump fourth_day_laura
#        elif laura_fourth_day_finish == True:
#            jump fourth_day_end

screen investigation:

    tag menu
    modal True
    if julia_third_day_finish:
        add "logo2"
    else:
        add "logo1"
    add Solid("#000a")
    text "{font=Digital-Medium.ttf}INVESTIGATION LOG{/font}" xalign 0.5 yalign 0.05 size 50

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 50
        vbox:
            xalign 0.5
            spacing 20
            text "{font=Digital-Medium.ttf}DAYS OF INVESTIGATION: [scenes]{/font}"
            text "{font=Digital-Medium.ttf}TIMES INSIDE A PSYCHE: [psychepoints]{/font}"

        vbox:
            xalign 0.5
            spacing 20
            text "{font=Digital-Medium.ttf}DAYS SPENT WITH CHARLOTTE: [charlottescenes]{/font}"
            text "{font=Digital-Medium.ttf}DAYS SPENT WITH JULIA: [juliascenes]{/font}"
            text "{font=Digital-Medium.ttf}DAYS SPENT WITH VALERIE: [valeriescenes]{/font}"

    textbutton "Return":
        action Hide("investigation", dissolve)
        xalign 0.95
        yalign 0.05

label change_name_first:

    if julia_third_day_finish:
        show logo2
    else:
        show logo1
    $ povname = renpy.input("What was my name again?")
    if povname is "":
        $ povname = "Dmitri"
    $ persistent.povname = povname.strip()
    menu:
        p "Is that really my name?"

        "Yes, it's [povname].":
            jump intro_eileen
        "I don't really think so.":
            jump change_name_first

label change_name_intro:

    if julia_third_day_finish:
        show logo2
    else:
        show logo1
    $ povname = renpy.input("What was my name again?")
    if povname is "":
        $ povname = "Dmitri"
    $ persistent.povname = povname.strip()
    menu:
        p "Is that really my name?"

        "Yes, it's [povname].":
            p "Right, right, [povname]. With all of these problems happening is hard to remember."
            jump introduction
        "I don't really think so.":
            jump change_name_intro

label change_name:

    if julia_third_day_finish:
        show logo2
    else:
        show logo1
    $ povname = renpy.input("What was my name again?")
    if povname is "":
        $ povname = "Dmitri"
    $ persistent.povname = povname.strip()
    menu:
        p "Is that really my name?"

        "Yes, it's [povname].":
            p "Right, right, [povname]. With all of these problems happening is hard to remember."
            jump menu_select
        "I don't really think so.":
            jump change_name

label change_name_menu:

    if julia_third_day_finish:
        show logo2
    else:
        show logo1
    $ povname = renpy.input("What is my name?")
    if povname is "":
        $ povname = "Dmitri"
    $ persistent.povname = povname.strip()
    menu:
        p "Is that really my name?"

        "Yes, it's [povname].":
            p "Right, right, [povname]. With all of these problems happening is hard to remember."
            return
        "I don't really think so.":
            jump change_name_menu

label demo_end:
    scene black with fade
    show galextra1
    hide galextra1
    show galextra2
    hide galextra2
    show chibiextra1
    hide chibiextra1
    show chibiextra2
    hide chibiextra2
    show chibimisc1
    hide chibimisc1
    show chibimisc2
    hide chibimisc2
    window hide
    show text "{size=+10}{font=Digital-Medium.ttf}THIS IS THE END OF THIS BUILD.{/font}{/size}" at truecenter with dissolve
    $ renpy.pause(5, hard=True)
    show text "{size=+10}{font=Digital-Medium.ttf}IF YOU LIKED THE DEMO OR HAVE ANY CRITIQUE YOU ARE WELCOMED TO DO SO!{/font}{/size}" at truecenter with dissolve
    $ renpy.pause(5, hard=True)
    show text "{size=+10}{font=Digital-Medium.ttf}SEE YOU AROUND.{/font}{/size}" at truecenter with dissolve
    $ renpy.pause(5, hard=True)
    return

###############################################################
########### DAYS, TIME AND PSYCHE #############################
###############################################################

init python:
    class Calendar(object):

            def __init__(self):
                self.day = 0
                self.hourclock = 0
                self.weekdays = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY"]
                self.psychename = ["CHARLOTTE","JULIA","VALERIE","LAURA","EILEEN"]
                self.hour_of_day = ["08:00 A.M.", "12:00 P.M.", "04:00 P.M.", "08:00 P.M.", "12:00 A.M."]
                self.time_of_day = ["MORNING", "NOON", "NIGHT"]

            @property
            def personpsyche(self):
                return self.psychename[0]

            @property
            def weekday(self):
                if self.day > 4:
                    self.day = 0
                return self.weekdays[self.day]

            @property
            def hour(self):
                if self.hourclock > 4:
                    self.hourclock = 0
                return self.hour_of_day[self.hourclock]

            @property
            def time(self):
                if (self.hourclock<=1):
                    return self.time_of_day[0]
                elif (self.hourclock==2):
                    return self.time_of_day[1]
                elif (self.hourclock>=1):
                    return self.time_of_day[2]

            def advance_weekday(self, step=1):
                self.day += step
                return fade

            def advance_hour(self, step=1):
                self.hourclock += step
                return fade

default clock = Calendar()

default inpsyche = False

screen clock_marker:
    add "gui/clock_background.png" xalign 0.0 yalign 0.0
    vbox:
        xalign 0.05
        yalign 0.02
        spacing 10
        if inpsyche == True:
            text "{size=33}{font=digital-7.ttf}[clock.personpsyche]{/font}{/size}"
        else:
            text "{size=33}{font=digital-7.ttf}[clock.weekday]{/font}{/size}"
        text "{size=33}{font=digital-7.ttf}[clock.time]{/font}{/size}"
        text "{size=33}{font=digital-7.ttf}[clock.hour]{/font}{/size}"
    add "clock_display" xalign 0.0 yalign 0.0

# $ clock.advance_weekday()
# $ clock.advance_hour()
# $ clock.day =
# $ clock.hourclock =

image clock_display = TransitionConditionSwitch(Dissolve(0.5),
    "inpsyche and clock.personpsyche == 'CHARLOTTE'", "gui/clock_display_charlotte.png",
    "inpsyche and clock.personpsyche == 'JULIA'", "gui/clock_display_julia.png",
    "inpsyche and clock.personpsyche == 'VALERIE'", "gui/clock_display_valerie.png",
    "inpsyche and clock.personpsyche == 'LAURA'", "gui/clock_display_laura.png",
    "True", "gui/clock_display.png")

image custom_textbox = TransitionConditionSwitch(Dissolve(0.5),
    "inpsyche and clock.personpsyche == 'CHARLOTTE'", "gui/textboxcharlotte.png",
    "inpsyche and clock.personpsyche == 'JULIA'", "gui/textboxjulia.png",
    "inpsyche and clock.personpsyche == 'VALERIE'", "gui/textboxvalerie.png",
    "inpsyche and clock.personpsyche == 'LAURA'", "gui/textboxlaura.png",
    "True", "gui/textbox.png")

image custom_namebox = TransitionConditionSwitch(Dissolve(0.5),
    "inpsyche and clock.personpsyche == 'CHARLOTTE'", "gui/nameboxcharlotte.png",
    "inpsyche and clock.personpsyche == 'JULIA'", "gui/nameboxjulia.png",
    "inpsyche and clock.personpsyche == 'VALERIE'", "gui/nameboxvalerie.png",
    "inpsyche and clock.personpsyche == 'LAURA'", "gui/nameboxlaura.png",
    "True", "gui/namebox.png")
