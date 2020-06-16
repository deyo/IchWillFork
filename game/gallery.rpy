init python:

#    def MaxScale (img, minwidth=config.screen_width, minheigth=config.screen_height):
#        currwidth, currheight = renpy.image_size(img)
#        xscale = float(minwidth) / currwidth
#        yscale = float(minheight) / currheight
#
#        if xscale . yscale:
#            maxscale = xscale
#        else:
#            maxscale = yscale
#
#        return im.FactorScale(img, maxscale, maxscale)
#
    def MinScale(img, maxwidth=config.screen_width, maxheight=config.screen_height):
        currwidth, currheight = renpy.image_size(img)
        xscale = float(maxwidth) / currwidth
        yscale = float(maxheight) / currheight

        if xscale < yscale:
            minscale = xscale
        else:
            minscale = yscale

        return im.FactorScale(img, minscale, minscale)

    maxnumx = 2
    maxnumy = 1
    maxthumbx = config.screen_width / (maxnumx + 1)
    maxthumby = config.screen_height / (maxnumy + 1)
    maxperpage = maxnumx * maxnumy
    maxnumcharx = 3
    maxnumchary = 2
    maxthumbcharx = config.screen_width / (maxnumcharx + 1)
    maxthumbchary = config.screen_height / (maxnumchary + 1)
    maxpercharpage = maxnumcharx * maxnumchary
    maxnumextrax = 4
    maxnumextray = 2
    maxthumbextrax = config.screen_width / (maxnumextrax + 1)
    maxthumbextray = config.screen_height / (maxnumextray + 1)
    maxperextrapage = maxnumextrax * maxnumextray
    maxnummiscx = 4
    maxnummiscy = 2
    maxthumbmiscx = config.screen_width / (maxnummiscx + 1)
    maxthumbmiscy = config.screen_height / (maxnummiscy + 1)
    maxpermiscpage = maxnummiscx * maxnummiscy
    gallery_page = 0
    gallerychar_charlotte_page = 0
    gallerychar_julia_page = 0
    gallerychar_valerie_page = 0
    gallerychar_laura_page = 0
    gallerychar_eileen_page = 0
    galleryextra_extra_page = 0
    gallerymisc_misc_page = 0
    closeup_page = 0
    gal = Gallery()

    class Gallery:
        def __init__(self, name, images, thumb, replay = None, locked="gallery_locked"):
            self.name = name
            self.images = images
            self.thumb = thumb
            self.replay = replay
            self.locked = locked
            self.refresh_lock()

        def num_images(self):
            return len(self.images)

        def refresh_lock(self):
            self.num_unlock = 0
            lockme = False
            for img in self.images:
                if renpy.seen_image(img):
                    self.num_unlock += 1
            self.is_locked = self.num_unlock == 0

    gallery_images = []
    gallery_images.append(Gallery("Charlotte", ["charlotteintro1", "charlotte101", "charlotte201", "charlotte301", "charlotte401", "charlotte501", "charlotte601", "charlotteextra101", "charlotteextra201", "charlotteextra301", "charlotteextra401", "charlotteextra501", "charlotteextra601"], ["chibicharlottethumb1", "chibicharlottethumb2"]))
    gallery_images.append(Gallery("Julia", ["juliaintro1", "julia101", "julia201", "julia301", "julia401", "juliaextra101", "juliaextra201", "juliaextra301", "juliaextra401"], ["chibijuliathumb1", "chibijuliathumb2"]))
    gallery_images.append(Gallery("Valerie", ["valerieintro1", "valerie101", "valerie201", "valerie301", "valerie401", "valerieextra101", "valerieextra201", "valerieextra301", "valerieextra401"], ["chibivaleriethumb1", "chibivaleriethumb2"]))
    gallery_images.append(Gallery("Laura", ["lauraintro1", "laura101", "laura201", "lauraextra101", "lauraextra201"], ["chibilaurathumb1", "chibilaurathumb2"]))
    gallery_images.append(Gallery("Extra", ["charlotte p11_happy", "julia p11_happy", "valerie p11_happy"], ["chibiextrathumb1"]))
#    gallery_images.append(Gallery("Miscellaneous", ["charlotte p11_happy", "julia p11_happy", "valerie p11_happy"], ["chibimiscthumb1"]))

    gallery_charlotteimages = []
    gallery_charlotteimages.append(Gallery("Introduction", ["charlotteintro1", "charlotteintro2"], "thumbcharlotteintro", "charlotte_introscene1"))
    gallery_charlotteimages.append(Gallery("Hidden at Bathroom", ["charlotte101", "charlotte102", "charlotte103", "charlotte104", "charlotte105", "charlotte106", "charlotte107", "charlotte108", "charlotte109", "charlotte110", "charlotte111", "charlotte112", "charlotte113", "charlotte114", "charlotte115"], "thumbcharlotte1", "charlotte_scene1"))
    gallery_charlotteimages.append(Gallery("Held at Castle", ["charlotte201", "charlotte202", "charlotte203", "charlotte204", "charlotte205", "charlotte206", "charlotte207", "charlotte208", "charlotte209", "charlotte210", "charlotte211", "charlotte212", "charlotte213", "charlotte214", "charlotte215", "charlotte216", "charlotte217", "charlotte218", "charlotte219", "charlotte220"], "thumbcharlotte2", "charlotte_scene2"))
    gallery_charlotteimages.append(Gallery("Discovered at Bathroom", ["charlotte301", "charlotte302", "charlotte303", "charlotte304", "charlotte305", "charlotte306", "charlotte307", "charlotte308", "charlotte309", "charlotte310", "charlotte311", "charlotte312", "charlotte313", "charlotte314", "charlotte315", "charlotte316", "charlotte317", "charlotte318", "charlotte319"], "thumbcharlotte3", "charlotte_scene3"))
    gallery_charlotteimages.append(Gallery("Alone, Together", ["charlotte401", "charlotte402", "charlotte403", "charlotte404", "charlotte405", "charlotte406", "charlotte407", "charlotte408", "charlotte409", "charlotte410", "charlotte411", "charlotte412", "charlotte413", "charlotte414", "charlotte415", "charlotte416", "charlotte417", "charlotte418", "charlotte419", "charlotte420", "charlotte421", "charlotte422", "charlotte423", "charlotte424", "charlotte425", "charlotte426"], "thumbcharlotte4", "charlotte_scene4"))
    gallery_charlotteimages.append(Gallery("Fuck my Ass", ["charlotte501", "charlotte502", "charlotte503", "charlotte504", "charlotte505", "charlotte506", "charlotte507", "charlotte508", "charlotte509", "charlotte510", "charlotte511", "charlotte512", "charlotte513", "charlotte514", "charlotte515", "charlotte516", "charlotte517", "charlotte518", "charlotte519", "charlotte520", "charlotte521", "charlotte522", "charlotte523", "charlotte524", "charlotte525", "charlotte526", "charlotte527", "charlotte528", "charlotte529", "charlotte530"], "thumbcharlotte5", "charlotte_scene5"))
    gallery_charlotteimages.append(Gallery("Torture Game", ["charlotte601", "charlotte602", "charlotte603", "charlotte604", "charlotte605", "charlotte606", "charlotte607", "charlotte608", "charlotte609", "charlotte610", "charlotte611", "charlotte612", "charlotte613", "charlotte614", "charlotte615", "charlotte616", "charlotte617", "charlotte618", "charlotte619", "charlotte620", "charlotte621", "charlotte622", "charlotte623", "charlotte624", "charlotte625", "charlotte626", "charlotte627", "charlotte628", "charlotte629", "charlotte630", "charlotte631", "charlotte632", "charlotte633", "charlotte634"], "thumbcharlotte6", "charlotte_scene6"))
    gallery_charlotteimages.append(Gallery("Classroom Reunion", ["charlotteextra101", "charlotteextra102"], "thumbcharlotteextra1"))
    gallery_charlotteimages.append(Gallery("Throne Room", ["charlotteextra201", "charlotteextra202"], "thumbcharlotteextra2"))
    gallery_charlotteimages.append(Gallery("Cheer!", ["charlotteextra301", "charlotteextra302", "charlotteextra303", "charlotteextra304", "charlotteextra305"], "thumbcharlotteextra3"))
    gallery_charlotteimages.append(Gallery("Too Close", ["charlotteextra401", "charlotteextra402", "charlotteextra403", "charlotteextra404", "charlotteextra405"], "thumbcharlotteextra4"))
    gallery_charlotteimages.append(Gallery("Technology", ["charlotteextra501", "charlotteextra502", "charlotteextra503", "charlotteextra504", "charlotteextra505"], "thumbcharlotteextra5"))
    gallery_charlotteimages.append(Gallery("Everything is Well", ["charlotteextra601", "charlotteextra602", "charlotteextra603", "charlotteextra604", "charlotteextra605", "charlotteextra606", "charlotteextra607", "charlotteextra608"], "thumbcharlotteextra6"))

    gallery_juliaimages = []
    gallery_juliaimages.append(Gallery("Introduction", ["juliaintro1", "juliaintro2"], "thumbjuliaintro", "julia_introscene1"))
    gallery_juliaimages.append(Gallery("Questioning", ["julia101", "julia102", "julia103", "julia104", "julia105", "julia106", "julia107", "julia108", "julia109", "julia110", "julia111", "julia112", "julia113", "julia114", "julia115", "julia116"], "thumbjulia1", "julia_scene1"))
    gallery_juliaimages.append(Gallery("Robot Torture", ["julia201", "julia202", "julia203", "julia204", "julia205", "julia206", "julia207", "julia208", "julia209", "julia210", "julia211", "julia212", "julia213", "julia214", "julia215", "julia216"], "thumbjulia2", "julia_scene2"))
    gallery_juliaimages.append(Gallery("Do Me, Right Here", ["julia301", "julia302", "julia303", "julia304", "julia305", "julia306", "julia307", "julia308", "julia309", "julia310", "julia311", "julia312", "julia313", "julia314", "julia315", "julia316", "julia317", "julia318", "julia319", "julia320", "julia321"], "thumbjulia3", "julia_scene3"))
    gallery_juliaimages.append(Gallery("Robot Overhaul", ["julia401", "julia402", "julia403", "julia404", "julia405", "julia406", "julia407", "julia408", "julia409", "julia410", "julia411", "julia412", "julia413", "julia414", "julia415", "julia416", "julia417", "julia418", "julia419", "julia420", "julia421", "julia422"], "thumbjulia4", "julia_scene4"))
    gallery_juliaimages.append(Gallery("Julia Files", ["juliaextra101", "juliaextra102"], "thumbjuliaextra1"))
    gallery_juliaimages.append(Gallery("Control Room", ["juliaextra201", "juliaextra202"], "thumbjuliaextra2"))
    gallery_juliaimages.append(Gallery("Mom?", ["juliaextra301", "juliaextra302", "juliaextra303"], "thumbjuliaextra3"))
    gallery_juliaimages.append(Gallery("Mecha Julia", ["juliaextra401", "juliaextra402", "juliaextra403", "juliaextra404", "juliaextra405", "juliaextra406", "juliaextra407", "juliaextra408"], "thumbjuliaextra4"))

    gallery_valerieimages = []
    gallery_valerieimages.append(Gallery("Introduction", ["valerieintro1", "valerieintro2"], "thumbvalerieintro", "valerie_introscene1"))
    gallery_valerieimages.append(Gallery("Midnight Storage", ["valerie101", "valerie102", "valerie103", "valerie104", "valerie105", "valerie106", "valerie107", "valerie108", "valerie109", "valerie110", "valerie111", "valerie112", "valerie113", "valerie114", "valerie115", "valerie116"], "thumbvalerie1", "valerie_scene1"))
    gallery_valerieimages.append(Gallery("Bonfire Heat", ["valerie201", "valerie202", "valerie203", "valerie204", "valerie205", "valerie206", "valerie207", "valerie208", "valerie209", "valerie210", "valerie211", "valerie212", "valerie213", "valerie214", "valerie215", "valerie216", "valerie217"], "thumbvalerie2", "valerie_scene2"))
    gallery_valerieimages.append(Gallery("Round One", ["valerie301", "valerie302", "valerie303", "valerie304", "valerie305", "valerie306", "valerie307", "valerie308", "valerie309", "valerie310", "valerie311", "valerie312", "valerie313", "valerie314", "valerie315", "valerie316", "valerie317", "valerie318", "valerie319", "valerie320", "valerie321"], "thumbvalerie3", "valerie_scene3"))
    gallery_valerieimages.append(Gallery("Show Me", ["valerie401", "valerie402", "valerie403", "valerie404", "valerie405", "valerie406", "valerie407", "valerie408", "valerie409", "valerie410", "valerie411", "valerie412", "valerie413", "valerie414", "valerie415", "valerie416", "valerie417", "valerie418", "valerie419", "valerie420", "valerie421", "valerie422"], "thumbvalerie4", "valerie_scene4"))
    gallery_valerieimages.append(Gallery("Topless Fight", ["valerieextra101", "valerieextra102"], "thumbvalerieextra1"))
    gallery_valerieimages.append(Gallery("Hidding from the Enemy", ["valerieextra201", "valerieextra202"], "thumbvalerieextra2"))
    gallery_valerieimages.append(Gallery("Getting Started", ["valerieextra301", "valerieextra302", "valerieextra303", "valerieextra304", "valerieextra305"], "thumbvalerieextra3"))
    gallery_valerieimages.append(Gallery("Captured by the Enemy", ["valerieextra401", "valerieextra402", "valerieextra403", "valerieextra404"], "thumbvalerieextra4"))

    gallery_lauraimages = []
    gallery_lauraimages.append(Gallery("Introduction", ["lauraintro1", "lauraintro2"], "thumblauraintro", "laura_introscene1"))
    gallery_lauraimages.append(Gallery("A Good Mother", ["laura101", "laura102", "laura103", "laura104", "laura105", "laura106", "laura107", "laura108", "laura109", "laura110", "laura111", "laura112", "laura113", "laura114", "laura115", "laura116"], "thumblaura1", "laura_scene1"))
    gallery_lauraimages.append(Gallery("Everything is White", ["laura201", "laura202", "laura203", "laura204", "laura205", "laura206", "laura207", "laura208", "laura209", "laura210", "laura211", "laura212", "laura213", "laura214", "laura215", "laura216", "laura217"], "thumblaura2", "laura_scene2"))
    gallery_lauraimages.append(Gallery("Family Time", ["lauraextra101", "lauraextra102"], "thumblauraextra1"))
    gallery_lauraimages.append(Gallery("Heaven or Hell", ["lauraextra201", "lauraextra202"], "thumblauraextra2"))

    gallery_extraimages = []
    gallery_extraimages.append(Gallery("Charlotte 1", ["charlotte p11_angry", "charlotte p11_happy", "charlotte p11_neutral", "charlotte p11_sad", "charlotte p11_serious", "charlotte p11_surprised", "charlotte p12_angry", "charlotte p12_happy", "charlotte p12_neutral", "charlotte p12_sad", "charlotte p12_serious", "charlotte p12_surprised", "charlotte p13_angry", "charlotte p13_happy", "charlotte p13_neutral", "charlotte p13_sad", "charlotte p13_serious", "charlotte p13_surprised", "charlotte pp11_angry", "charlotte pp11_happy", "charlotte pp11_neutral", "charlotte pp11_sad", "charlotte pp11_serious", "charlotte pp11_surprised", "charlotte pp12_angry", "charlotte pp12_happy", "charlotte pp12_neutral", "charlotte pp12_sad", "charlotte pp12_serious", "charlotte pp12_surprised", "charlotte pp13_angry", "charlotte pp13_happy", "charlotte pp13_neutral", "charlotte pp13_sad", "charlotte pp13_serious", "charlotte pp13_surprised", "charlotte p51_angry", "charlotte p51_happy", "charlotte p51_neutral", "charlotte p51_sad", "charlotte p51_serious", "charlotte p51_surprised"], "charlotte_sprite_thumb1"))
    gallery_extraimages.append(Gallery("Charlotte 2", ["charlotte p21_angry", "charlotte p21_happy", "charlotte p21_neutral", "charlotte p21_sad", "charlotte p21_serious", "charlotte p21_surprised", "charlotte p22_angry", "charlotte p22_happy", "charlotte p22_neutral", "charlotte p22_sad", "charlotte p22_serious", "charlotte p22_surprised", "charlotte p23_angry", "charlotte p23_happy", "charlotte p23_neutral", "charlotte p23_sad", "charlotte p23_serious", "charlotte p23_surprised", "charlotte pp21_angry", "charlotte pp21_happy", "charlotte pp21_neutral", "charlotte pp21_sad", "charlotte pp21_serious", "charlotte pp21_surprised", "charlotte pp22_angry", "charlotte pp22_happy", "charlotte pp22_neutral", "charlotte pp22_sad", "charlotte pp22_serious", "charlotte pp22_surprised", "charlotte pp23_angry", "charlotte pp23_happy", "charlotte pp23_neutral", "charlotte pp23_sad", "charlotte pp23_serious", "charlotte pp23_surprised", "charlotte p52_angry", "charlotte p52_happy", "charlotte p52_neutral", "charlotte p52_sad", "charlotte p52_serious", "charlotte p52_surprised"], "charlotte_sprite_thumb2"))
    gallery_extraimages.append(Gallery("Charlotte 3", ["charlotte p31_angry", "charlotte p31_happy", "charlotte p31_neutral", "charlotte p31_sad", "charlotte p31_serious", "charlotte p31_surprised", "charlotte p32_angry", "charlotte p32_happy", "charlotte p32_neutral", "charlotte p32_sad", "charlotte p32_serious", "charlotte p32_surprised", "charlotte p33_angry", "charlotte p33_happy", "charlotte p33_neutral", "charlotte p33_sad", "charlotte p33_serious", "charlotte p33_surprised", "charlotte pp31_angry", "charlotte pp31_happy", "charlotte pp31_neutral", "charlotte pp31_sad", "charlotte pp31_serious", "charlotte pp31_surprised", "charlotte pp32_angry", "charlotte pp32_happy", "charlotte pp32_neutral", "charlotte pp32_sad", "charlotte pp32_serious", "charlotte pp32_surprised", "charlotte pp33_angry", "charlotte pp33_happy", "charlotte pp33_neutral", "charlotte pp33_sad", "charlotte pp33_serious", "charlotte pp33_surprised", "charlotte p53_angry", "charlotte p53_happy", "charlotte p53_neutral", "charlotte p53_sad", "charlotte p53_serious", "charlotte p53_surprised"], "charlotte_sprite_thumb3"))
    gallery_extraimages.append(Gallery("Charlotte 4", ["charlotte p41_angry", "charlotte p41_happy", "charlotte p41_neutral", "charlotte p41_sad", "charlotte p41_serious", "charlotte p41_surprised", "charlotte p42_angry", "charlotte p42_happy", "charlotte p42_neutral", "charlotte p42_sad", "charlotte p42_serious", "charlotte p42_surprised", "charlotte p43_angry", "charlotte p43_happy", "charlotte p43_neutral", "charlotte p43_sad", "charlotte p43_serious", "charlotte p43_surprised", "charlotte pp41_angry", "charlotte pp41_happy", "charlotte pp41_neutral", "charlotte pp41_sad", "charlotte pp41_serious", "charlotte pp41_surprised", "charlotte pp42_angry", "charlotte pp42_happy", "charlotte pp42_neutral", "charlotte pp42_sad", "charlotte pp42_serious", "charlotte pp42_surprised", "charlotte pp43_angry", "charlotte pp43_happy", "charlotte pp43_neutral", "charlotte pp43_sad", "charlotte pp43_serious", "charlotte pp43_surprised", "charlotte p54_angry", "charlotte p54_happy", "charlotte p54_neutral", "charlotte p54_sad", "charlotte p54_serious", "charlotte p54_surprised"], "charlotte_sprite_thumb4"))
    gallery_extraimages.append(Gallery("Julia 1", ["julia p11_angry", "julia p11_happy", "julia p11_neutral", "julia p11_sad", "julia p11_serious", "julia p11_surprised", "julia p12_angry", "julia p12_happy", "julia p12_neutral", "julia p12_sad", "julia p12_serious", "julia p12_surprised", "julia p13_angry", "julia p13_happy", "julia p13_neutral", "julia p13_sad", "julia p13_serious", "julia p13_surprised", "julia pp11_angry", "julia pp11_happy", "julia pp11_neutral", "julia pp11_sad", "julia pp11_serious", "julia pp11_surprised", "julia pp12_angry", "julia pp12_happy", "julia pp12_neutral", "julia pp12_sad", "julia pp12_serious", "julia pp12_surprised"], "julia_sprite_thumb1"))
    gallery_extraimages.append(Gallery("Julia 2", ["julia p21_angry", "julia p21_happy", "julia p21_neutral", "julia p21_sad", "julia p21_serious", "julia p21_surprised", "julia p22_angry", "julia p22_happy", "julia p22_neutral", "julia p22_sad", "julia p22_serious", "julia p22_surprised", "julia p23_angry", "julia p23_happy", "julia p23_neutral", "julia p23_sad", "julia p23_serious", "julia p23_surprised", "julia pp21_angry", "julia pp21_happy", "julia pp21_neutral", "julia pp21_sad", "julia pp21_serious", "julia pp21_surprised", "julia pp22_angry", "julia pp22_happy", "julia pp22_neutral", "julia pp22_sad", "julia pp22_serious", "julia pp22_surprised"], "julia_sprite_thumb2"))
    gallery_extraimages.append(Gallery("Julia 3", ["julia p31_angry", "julia p31_happy", "julia p31_neutral", "julia p31_sad", "julia p31_serious", "julia p31_surprised", "julia p32_angry", "julia p32_happy", "julia p32_neutral", "julia p32_sad", "julia p32_serious", "julia p32_surprised", "julia p33_angry", "julia p33_happy", "julia p33_neutral", "julia p33_sad", "julia p33_serious", "julia p33_surprised", "julia pp31_angry", "julia pp31_happy", "julia pp31_neutral", "julia pp31_sad", "julia pp31_serious", "julia pp31_surprised", "julia pp32_angry", "julia pp32_happy", "julia pp32_neutral", "julia pp32_sad", "julia pp32_serious", "julia pp32_surprised"], "julia_sprite_thumb3"))
    gallery_extraimages.append(Gallery("Julia 4", ["julia p41_angry", "julia p41_happy", "julia p41_neutral", "julia p41_sad", "julia p41_serious", "julia p41_surprised", "julia p42_angry", "julia p42_happy", "julia p42_neutral", "julia p42_sad", "julia p42_serious", "julia p42_surprised", "julia p43_angry", "julia p43_happy", "julia p43_neutral", "julia p43_sad", "julia p43_serious", "julia p43_surprised", "julia pp41_angry", "julia pp41_happy", "julia pp41_neutral", "julia pp41_sad", "julia pp41_serious", "julia pp41_surprised", "julia pp42_angry", "julia pp42_happy", "julia pp42_neutral", "julia pp42_sad", "julia pp42_serious", "julia pp42_surprised"], "julia_sprite_thumb4"))
    gallery_extraimages.append(Gallery("Valerie 1", ["valerie p11_angry", "valerie p11_happy", "valerie p11_neutral", "valerie p11_sad", "valerie p11_serious", "valerie p11_surprised", "valerie p12_angry", "valerie p12_happy", "valerie p12_neutral", "valerie p12_sad", "valerie p12_serious", "valerie p12_surprised", "valerie p13_angry", "valerie p13_happy", "valerie p13_neutral", "valerie p13_sad", "valerie p13_serious", "valerie p13_surprised", "valerie pp11_angry", "valerie pp11_happy", "valerie pp11_neutral", "valerie pp11_sad", "valerie pp11_serious", "valerie pp11_surprised"], "valerie_sprite_thumb1"))
    gallery_extraimages.append(Gallery("Valerie 2", ["valerie p21_angry", "valerie p21_happy", "valerie p21_neutral", "valerie p21_sad", "valerie p21_serious", "valerie p21_surprised", "valerie p22_angry", "valerie p22_happy", "valerie p22_neutral", "valerie p22_sad", "valerie p22_serious", "valerie p22_surprised", "valerie p23_angry", "valerie p23_happy", "valerie p23_neutral", "valerie p23_sad", "valerie p23_serious", "valerie p23_surprised", "valerie pp21_angry", "valerie pp21_happy", "valerie pp21_neutral", "valerie pp21_sad", "valerie pp21_serious", "valerie pp21_surprised"], "valerie_sprite_thumb2"))
    gallery_extraimages.append(Gallery("Valerie 3", ["valerie p31_angry", "valerie p31_happy", "valerie p31_neutral", "valerie p31_sad", "valerie p31_serious", "valerie p31_surprised", "valerie p32_angry", "valerie p32_happy", "valerie p32_neutral", "valerie p32_sad", "valerie p32_serious", "valerie p32_surprised", "valerie p33_angry", "valerie p33_happy", "valerie p33_neutral", "valerie p33_sad", "valerie p33_serious", "valerie p33_surprised", "valerie pp31_angry", "valerie pp31_happy", "valerie pp31_neutral", "valerie pp31_sad", "valerie pp31_serious", "valerie pp31_surprised"], "valerie_sprite_thumb3"))
    gallery_extraimages.append(Gallery("Valerie 4", ["valerie p41_angry", "valerie p41_happy", "valerie p41_neutral", "valerie p41_sad", "valerie p41_serious", "valerie p41_surprised", "valerie p42_angry", "valerie p42_happy", "valerie p42_neutral", "valerie p42_sad", "valerie p42_serious", "valerie p42_surprised", "valerie p43_angry", "valerie p43_happy", "valerie p43_neutral", "valerie p43_sad", "valerie p43_serious", "valerie p43_surprised", "valerie pp41_angry", "valerie pp41_happy", "valerie pp41_neutral", "valerie pp41_sad", "valerie pp41_serious", "valerie pp41_surprised"], "valerie_sprite_thumb4"))
    gallery_extraimages.append(Gallery("Laura 1", ["laura p11_angry", "laura p11_happy", "laura p11_neutral", "laura p11_sad", "laura p11_serious", "laura p11_surprised", "laura p12_angry", "laura p12_happy", "laura p12_neutral", "laura p12_sad", "laura p12_serious", "laura p12_surprised", "laura p13_angry", "laura p13_happy", "laura p13_neutral", "laura p13_sad", "laura p13_serious", "laura p13_surprised", "laura pp11_angry", "laura pp11_happy", "laura pp11_neutral", "laura pp11_sad", "laura pp11_serious", "laura pp11_surprised", "laura pp12_angry", "laura pp12_happy", "laura pp12_neutral", "laura pp12_sad", "laura pp12_serious", "laura pp12_surprised", "laura pp13_angry", "laura pp13_happy", "laura pp13_neutral", "laura pp13_sad", "laura pp13_serious", "laura pp13_surprised"], "laura_sprite_thumb1"))
    gallery_extraimages.append(Gallery("Laura 2", ["laura p21_angry", "laura p21_happy", "laura p21_neutral", "laura p21_sad", "laura p21_serious", "laura p21_surprised", "laura p22_angry", "laura p22_happy", "laura p22_neutral", "laura p22_sad", "laura p22_serious", "laura p22_surprised", "laura p23_angry", "laura p23_happy", "laura p23_neutral", "laura p23_sad", "laura p23_serious", "laura p23_surprised", "laura pp21_angry", "laura pp21_happy", "laura pp21_neutral", "laura pp21_sad", "laura pp21_serious", "laura pp21_surprised", "laura pp22_angry", "laura pp22_happy", "laura pp22_neutral", "laura pp22_sad", "laura pp22_serious", "laura pp22_surprised", "laura pp23_angry", "laura pp23_happy", "laura pp23_neutral", "laura pp23_sad", "laura pp23_serious", "laura pp23_surprised"], "laura_sprite_thumb2"))
    gallery_extraimages.append(Gallery("Laura 3", ["laura p31_angry", "laura p31_happy", "laura p31_neutral", "laura p31_sad", "laura p31_serious", "laura p31_surprised", "laura p32_angry", "laura p32_happy", "laura p32_neutral", "laura p32_sad", "laura p32_serious", "laura p32_surprised", "laura p33_angry", "laura p33_happy", "laura p33_neutral", "laura p33_sad", "laura p33_serious", "laura p33_surprised", "laura pp31_angry", "laura pp31_happy", "laura pp31_neutral", "laura pp31_sad", "laura pp31_serious", "laura pp31_surprised", "laura pp32_angry", "laura pp32_happy", "laura pp32_neutral", "laura pp32_sad", "laura pp32_serious", "laura pp32_surprised", "laura pp33_angry", "laura pp33_happy", "laura pp33_neutral", "laura pp33_sad", "laura pp33_serious", "laura pp33_surprised"], "laura_sprite_thumb3"))
    gallery_extraimages.append(Gallery("Laura 4", ["laura p41_angry", "laura p41_happy", "laura p41_neutral", "laura p41_sad", "laura p41_serious", "laura p41_surprised", "laura p42_angry", "laura p42_happy", "laura p42_neutral", "laura p42_sad", "laura p42_serious", "laura p42_surprised", "laura p43_angry", "laura p43_happy", "laura p43_neutral", "laura p43_sad", "laura p43_serious", "laura p43_surprised", "laura pp41_angry", "laura pp41_happy", "laura pp41_neutral", "laura pp41_sad", "laura pp41_serious", "laura pp41_surprised", "laura pp42_angry", "laura pp42_happy", "laura pp42_neutral", "laura pp42_sad", "laura pp42_serious", "laura pp42_surprised", "laura pp43_angry", "laura pp43_happy", "laura pp43_neutral", "laura pp43_sad", "laura pp43_serious", "laura pp43_surprised"], "laura_sprite_thumb4"))
    gallery_extraimages.append(Gallery("Claire", ["claire p11_angry", "claire p11_happy", "claire p11_neutral", "claire p11_sad", "claire p11_serious", "claire p11_surprised", "claire p12_angry", "claire p12_happy", "claire p12_neutral", "claire p12_sad", "claire p12_serious", "claire p12_surprised", "claire p13_angry", "claire p13_happy", "claire p13_neutral", "claire p13_sad", "claire p13_serious", "claire p13_surprised", "claire p21_angry", "claire p21_happy", "claire p21_neutral", "claire p21_sad", "claire p21_serious", "claire p21_surprised", "claire p22_angry", "claire p22_happy", "claire p22_neutral", "claire p22_sad", "claire p22_serious", "claire p22_surprised", "claire p23_angry", "claire p23_happy", "claire p23_neutral", "claire p23_sad", "claire p23_serious", "claire p23_surprised", "claire p31_angry", "claire p31_happy", "claire p31_neutral", "claire p31_sad", "claire p31_serious", "claire p31_surprised", "claire p32_angry", "claire p32_happy", "claire p32_neutral", "claire p32_sad", "claire p32_serious", "claire p32_surprised"], "claire_sprite_thumb1"))
    gallery_extraimages.append(Gallery("Jean", ["jean p11_angry", "jean p11_happy", "jean p11_neutral", "jean p11_sad", "jean p11_serious", "jean p11_surprised", "jean p12_angry", "jean p12_happy", "jean p12_neutral", "jean p12_sad", "jean p12_serious", "jean p12_surprised", "jean p13_angry", "jean p13_happy", "jean p13_neutral", "jean p13_sad", "jean p13_serious", "jean p13_surprised", "jean p21_angry", "jean p21_happy", "jean p21_neutral", "jean p21_sad", "jean p21_serious", "jean p21_surprised", "jean p22_angry", "jean p22_happy", "jean p22_neutral", "jean p22_sad", "jean p22_serious", "jean p22_surprised", "jean p23_angry", "jean p23_happy", "jean p23_neutral", "jean p23_sad", "jean p23_serious", "jean p23_surprised", "jean p31_angry", "jean p31_happy", "jean p31_neutral", "jean p31_sad", "jean p31_serious", "jean p31_surprised", "jean p32_angry", "jean p32_happy", "jean p32_neutral", "jean p32_sad", "jean p32_serious", "jean p32_surprised"], "jean_sprite_thumb1"))
    gallery_extraimages.append(Gallery("Chloe", ["chloe p11_angry", "chloe p11_happy", "chloe p11_neutral", "chloe p11_sad", "chloe p11_serious", "chloe p11_surprised", "chloe p12_angry", "chloe p12_happy", "chloe p12_neutral", "chloe p12_sad", "chloe p12_serious", "chloe p12_surprised", "chloe p13_angry", "chloe p13_happy", "chloe p13_neutral", "chloe p13_sad", "chloe p13_serious", "chloe p13_surprised", "chloe p21_happy", "chloe p21_neutral", "chloe p21_sad", "chloe p21_serious", "chloe p21_surprised", "chloe p22_angry", "chloe p22_happy", "chloe p22_neutral", "chloe p22_sad", "chloe p22_serious", "chloe p22_surprised", "chloe p23_angry", "chloe p23_happy", "chloe p23_neutral", "chloe p23_sad", "chloe p23_serious", "chloe p23_surprised"], "chloe_sprite_thumb1"))
    gallery_extraimages.append(Gallery("Soldier", ["soldier pp11", "soldier pp12", "soldier pp13", "soldier pp21", "soldier pp22", "soldier pp23", "soldier pp31", "soldier pp32", "soldier pp33"], "soldier_sprite_thumb1"))
    gallery_extraimages.append(Gallery("Orc", ["orc pp11_angry", "orc pp11_happy", "orc pp11_neutral", "orc pp11_sad", "orc pp11_serious", "orc pp11_surprised", "orc pp12_angry", "orc pp12_happy", "orc pp12_neutral", "orc pp12_sad", "orc pp12_serious", "orc pp12_surprised", "orc pp21_angry", "orc pp21_happy", "orc pp21_neutral", "orc pp21_sad", "orc pp21_serious", "orc pp21_surprised", "orc pp22_angry", "orc pp22_happy", "orc pp22_neutral", "orc pp22_sad", "orc pp22_serious", "orc pp22_surprised", "orc pp31_panning", "orc pp32_panning"], "orc_sprite_thumb1"))
    gallery_extraimages.append(Gallery("Ogre", ["ogr pp11_angry", "ogr pp11_happy", "ogr pp11_neutral", "ogr pp11_sad", "ogr pp11_serious", "ogr pp11_surprised", "ogr pp12_angry", "ogr pp12_happy", "ogr pp12_neutral", "ogr pp12_sad", "ogr pp12_serious", "ogr pp12_surprised", "ogr pp21_angry", "ogr pp21_happy", "ogr pp21_neutral", "ogr pp21_sad", "ogr pp21_serious", "ogr pp21_surprised", "ogr pp22_angry", "ogr pp22_happy", "ogr pp22_neutral", "ogr pp22_sad", "ogr pp22_serious", "ogr pp22_surprised", "ogr pp31_panning", "ogr pp32_panning"], "ogr_sprite_thumb1"))
    gallery_extraimages.append(Gallery("Angel", ["angel pp11_angry", "angel pp11_happy", "angel pp11_neutral", "angel pp11_sad", "angel pp11_serious", "angel pp11_surprised", "angel pp12_angry", "angel pp12_happy", "angel pp12_neutral", "angel pp12_sad", "angel pp12_serious", "angel pp12_surprised", "angel pp13_angry", "angel pp13_happy", "angel pp13_neutral", "angel pp13_sad", "angel pp13_serious", "angel pp13_surprised", "angel pp21_angry", "angel pp21_happy", "angel pp21_neutral", "angel pp21_sad", "angel pp21_serious", "angel pp21_surprised", "angel pp22_angry", "angel pp22_happy", "angel pp22_neutral", "angel pp22_sad", "angel pp22_serious", "angel pp22_surprised", "angel pp23_angry", "angel pp23_happy", "angel pp23_neutral", "angel pp23_sad", "angel pp23_serious", "angel pp23_surprised"], "angel_sprite_thumb1"))
    gallery_extraimages.append(Gallery("Devil", ["devil pp11_angry", "devil pp11_happy", "devil pp11_neutral", "devil pp11_sad", "devil pp11_serious", "devil pp11_surprised", "devil pp12_angry", "devil pp12_happy", "devil pp12_neutral", "devil pp12_sad", "devil pp12_serious", "devil pp12_surprised", "devil pp21_angry", "devil pp21_happy", "devil pp21_neutral", "devil pp21_sad", "devil pp21_serious", "devil pp21_surprised", "devil pp22_angry", "devil pp22_happy", "devil pp22_neutral", "devil pp22_sad", "devil pp22_serious", "devil pp22_surprised"], "devil_sprite_thumb1"))
    gallery_extraimages.append(Gallery("Robot", ["robot pp11_angry", "robot pp11_happy", "robot pp11_neutral", "robot pp11_sad", "robot pp11_serious", "robot pp11_surprised", "robot pp12_angry", "robot pp12_happy", "robot pp12_neutral", "robot pp12_sad", "robot pp12_serious", "robot pp12_surprised"], "robot_sprite_thumb1"))
    gallery_extraimages.append(Gallery("Chapter Cards", ["logo1", "logo2"], "thumblogo1"))
    gallery_extraimages.append(Gallery("Charlotte Cards and Chibis", ["galcharlotteself1", "galcharlotteself2", "chibicharlotte1", "chibicharlotte2"], "thumbcharlotteself1"))
    gallery_extraimages.append(Gallery("Julia Cards and Chibis", ["galjuliaself1", "galjuliaself2", "chibijulia1", "chibijulia2"], "thumbjuliaself1"))
    gallery_extraimages.append(Gallery("Valerie Cards and Chibis", ["galvalerieself1", "galvalerieself2", "chibivalerie1", "chibivalerie2"], "thumbvalerieself1"))
    gallery_extraimages.append(Gallery("Laura Cards and Chibis", ["gallauraself1", "gallauraself2", "chibilaura1", "chibilaura2"], "thumblauraself1"))
#    gallery_extraimages.append(Gallery("Eileen Card", ["lauraextra201", "lauraextra202"], "thumblauraextra2"))
    gallery_extraimages.append(Gallery("Extras and more Chibis", ["galextra1", "galextra2", "chibiextra1", "chibiextra2", "chibimisc1", "chibimisc2"], "thumbgalextra1"))

#    gallery_miscimages = []
#    gallery_miscimages.append(Gallery("Chapter Cards", ["logo1", "logo2"], "thumblogo1"))
#    gallery_miscimages.append(Gallery("Charlotte Cards and Chibis", ["galcharlotteself1", "galcharlotteself2", "images/Miscellaneous/chibicharlotte1.webp", "images/Miscellaneous/chibicharlotte2.webp"], "thumbcharlotteself1"))
#    gallery_miscimages.append(Gallery("Julia Cards and Chibis", ["galjuliaself1", "galjuliaself2", "images/Miscellaneous/chibijulia1.webp", "images/Miscellaneous/chibijulia2.webp"], "thumbjuliaself1"))
#    gallery_miscimages.append(Gallery("Valerie Cards and Chibis", ["galvalerieself1", "galvalerieself2", "images/Miscellaneous/chibivalerie1.webp", "images/Miscellaneous/chibivalerie2.webp"], "thumbvalerieself1"))
#    gallery_miscimages.append(Gallery("Laura Cards and Chibis", ["gallauraself1", "gallauraself2", "images/Miscellaneous/chibilaura1.webp", "images/Miscellaneous/chibilaura2.webp"], "thumblauraself1"))
#    gallery_miscimages.append(Gallery("Eileen Card", ["lauraextra201", "lauraextra202"], "thumblauraextra2"))
#    gallery_miscimages.append(Gallery("Extras and more Chibis", ["galextra1", "galextra2", "galmisc", "chibiextra1", "chibiextra2", "chibimisc1", "chibimisc2"], "thumbgalextra1"))

screen gallery:
    tag menu

    add "galbackground1"
    if persistent.eileen_full_ending:
        add None
    else:
        add "galeileen1"
    if charlotte_sixth_day_finish:
#    if persistent.charlotte_full_ending:
        add "galcharlotte1"
    elif julia_fourth_day_finish:
#    elif persistent.julia_full_ending:
        add "galjulia1"
    elif valerie_fourth_day_finish:
#    elif persistent.valerie_full_ending:
        add "galvalerie1"
    elif laura_second_day_finish:
#    elif persistent.laura_full_ending:
        add "gallaura1"
    elif persistent.eileen_full_ending:
        add "galeileentrue1"
    add "images/Miscellaneous/picture.webp" xalign 1.0 yalign 1.0
    add Solid("#000a")
    #    elif persistent.harem_full_ending:
    #        add "galharem1.webp"
    text "{font=digital-7.ttf}IMAGES{/font}" xalign 0.05 yalign 0.05 size 50
    hbox:
        xalign 0.5
        yalign 0.05
        spacing 20
        textbutton "{font=Digital-Medium.ttf}IMAGE GALLERY{/font}":
            action Show("gallery", dissolve)
        textbutton "{font=Digital-Medium.ttf}SCENE REPLAY{/font}":
            if gallery_page > 1:
                action [SetVariable("gallery_page", gallery_page - 1), Show("replay", dissolve)]
            else:
                action Show("replay", dissolve)

    $ start = gallery_page * maxperpage
    $ end = min(start + maxperpage - 1, len(gallery_images) - 1)

    #image grid
    grid maxnumx maxnumy:
        xfill True
        yfill True

        for i in range(start, end + 1):
            $ gallery_images[i].refresh_lock()
            if gallery_images[i].is_locked:
                null
            else:
                imagebutton idle gallery_images[i].thumb[0]:
                    if gallery_images[i].name == "Charlotte":
                        action [Show("gallerychar_charlotte", dissolve), Hide("gallery", dissolve)]
                    elif gallery_images[i].name == "Julia":
                        action [Show("gallerychar_julia", dissolve), Hide("gallery", dissolve)]
                    elif gallery_images[i].name == "Valerie":
                        action [Show("gallerychar_valerie", dissolve), Hide("gallery", dissolve)]
                    elif gallery_images[i].name == "Laura":
                        action [Show("gallerychar_laura", dissolve), Hide("gallery", dissolve)]
                    elif gallery_images[i].name == "Eileen":
                        action [Show("gallerychar_eileen", dissolve), Hide("gallery", dissolve)]
                    elif gallery_images[i].name == "Extra":
                        action [Show("gallerychar_extra", dissolve), Hide("gallery", dissolve)]
#                    elif gallery_images[i].name == "Miscellaneous":
#                        action [Show("gallerychar_misc", dissolve), Hide("gallery", dissolve)]
                    xalign 0.5
                    yalign 0.5

        for i in range(end - start + 1, maxperpage):
            null

    #names
    grid maxnumx maxnumy:
        xfill True
        yfill True

        for i in range(start, end + 1):
            hbox:
                spacing maxthumby - 150
                xalign 0.5
                yalign 0.9
                $ total = gallery_images[i].num_images()
                $ partial = gallery_images[i].num_unlock
                if gallery_images[i].is_locked:
                    null
                else:
                    if gallery_images[i].name == "Extra":
                        text gallery_images[i].name
                    elif gallery_images[i].name == "Miscellaneous":
                        text gallery_images[i].name
                    else:
                        text gallery_images[i].name
                        text "[partial]/[total]"

        for i in range(end - start + 1, maxperpage):
            null

    #previous and next buttons
    if gallery_page > 0:
        textbutton "{size=+15}<<<{/size}":
            action SetVariable("gallery_page", gallery_page - 1)
            xalign 0.1
            yalign 1.0
    if (gallery_page + 1) * maxperpage < len(gallery_images):
        textbutton "{size=+15}>>>{/size}":
            action SetVariable("gallery_page", gallery_page + 1)
            xalign 0.9
            yalign 1.0
    #return button
    textbutton "Return":
        action Return()
        xalign 0.95
        yalign 0.05

    $ gallery_page_count = gallery_page + 1
    $ gallery_page_total = maxperpage / 2 - 1

    textbutton "{color=#F8F8F8}{font=Digital-Medium.ttf}[gallery_page_count]/3{/font}{/color}":
        xalign 0.5
        yalign 1.0

    key "mousedown_3":
        action Return()

screen gallerychar_charlotte:

    add "galcharlotteself1"
    add "images/Miscellaneous/picture.webp" xalign 1.0 yalign 1.0
    add Solid("#000a")
    text "Charlotte Gallery" xalign 0.05 yalign 0.05 size 40
    hbox:
        xalign 0.5
        yalign 0.05
        spacing 20
        textbutton "{font=Digital-Medium.ttf}IMAGE GALLERY{/font}":
            action [Show("gallerychar_charlotte", dissolve), Hide("replaychar_charlotte", dissolve)]
        textbutton "{font=Digital-Medium.ttf}SCENE REPLAY{/font}":
            action [Show("replaychar_charlotte", dissolve), Hide("gallerychar_charlotte", dissolve)]

    $ start = gallerychar_charlotte_page * maxpercharpage
    $ end = min(start + maxpercharpage - 1, len(gallery_charlotteimages) - 1)

    #image grid
    grid maxnumcharx maxnumchary:
        xfill True
        yfill True

        for i in range(start, end + 1):
            $ gallery_charlotteimages[i].refresh_lock()
            if gallery_charlotteimages[i].is_locked:
                add gallery_charlotteimages[i].locked:
                    xalign 0.5
                    yalign 0.5
            else:
                imagebutton idle gallery_charlotteimages[i].thumb:
                    action Show("gallery_closeup", dissolve, gallery_charlotteimages[i].images)
                    xalign 0.5
                    yalign 0.5

        for i in range(end - start + 1, maxpercharpage):
            null

    #names
    grid maxnumcharx maxnumchary:
        xfill True
        yfill True

        for i in range(start, end + 1):
            hbox:
                spacing 50
                xalign 0.5
                yalign 0.9
                $ total = gallery_charlotteimages[i].num_images()
                $ partial = gallery_charlotteimages[i].num_unlock
                if gallery_charlotteimages[i].is_locked:
                    null
                else:
                    text gallery_charlotteimages[i].name
                    text "[partial]/[total]"

        for i in range(end - start + 1, maxpercharpage):
            null

    #previous and next buttons
    if gallerychar_charlotte_page > 0:
        textbutton "{size=+15}<<<{/size}":
            action SetVariable("gallerychar_charlotte_page", gallerychar_charlotte_page - 1)
            xalign 0.1
            yalign 1.0
    if (gallerychar_charlotte_page + 1) * maxpercharpage < len(gallery_charlotteimages):
        textbutton "{size=+15}>>>{/size}":
            action SetVariable("gallerychar_charlotte_page", gallerychar_charlotte_page + 1)
            xalign 0.9
            yalign 1.0
    #return button
    textbutton "Return":
        action [SetVariable("gallerychar_charlotte_page", 0), Hide("gallerychar_charlotte", dissolve), Show("gallery", dissolve)]
        xalign 0.95
        yalign 0.05

    $ gallery_page_count = gallerychar_charlotte_page + 1
    $ gallery_page_total = maxpercharpage / 2 - 1

    textbutton "{color=#F8F8F8}{font=Digital-Medium.ttf}[gallery_page_count]/2{/font}{/color}":
        xalign 0.5
        yalign 1.0


    key "mousedown_3":
        action [SetVariable("gallerychar_charlotte_page", 0), Hide("gallerychar_charlotte", dissolve), Show("gallery", dissolve)]

screen gallerychar_julia:

    add "galjuliaself1"
    add "images/Miscellaneous/picture.webp" xalign 1.0 yalign 1.0
    add Solid("#000a")
    text "Julia Gallery" xalign 0.05 yalign 0.05 size 40
    hbox:
        xalign 0.5
        yalign 0.05
        spacing 20
        textbutton "{font=Digital-Medium.ttf}IMAGE GALLERY{/font}":
            action [Show("gallerychar_julia", dissolve), Hide("replaychar_julia", dissolve)]
        textbutton "{font=Digital-Medium.ttf}SCENE REPLAY{/font}":
            action [Show("replaychar_julia", dissolve), Hide("gallerychar_julia", dissolve)]

    $ start = gallerychar_julia_page * maxpercharpage
    $ end = min(start + maxpercharpage - 1, len(gallery_juliaimages) - 1)

    #image grid
    grid maxnumcharx maxnumchary:
        xfill True
        yfill True

        for i in range(start, end + 1):
            $ gallery_juliaimages[i].refresh_lock()
            if gallery_juliaimages[i].is_locked:
                add gallery_juliaimages[i].locked:
                    xalign 0.5
                    yalign 0.5
            else:
                imagebutton idle gallery_juliaimages[i].thumb:
                    action Show("gallery_closeup", dissolve, gallery_juliaimages[i].images)
                    xalign 0.5
                    yalign 0.5

        for i in range(end - start + 1, maxpercharpage):
            null

    #names
    grid maxnumcharx maxnumchary:
        xfill True
        yfill True

        for i in range(start, end + 1):
            hbox:
                spacing 20
                xalign 0.5
                yalign 0.9
                $ total = gallery_juliaimages[i].num_images()
                $ partial = gallery_juliaimages[i].num_unlock
                if gallery_juliaimages[i].is_locked:
                    null
                else:
                    text gallery_juliaimages[i].name
                    text "[partial]/[total]"

        for i in range(end - start + 1, maxpercharpage):
            null

    #previous and next buttons
    if gallerychar_julia_page > 0:
        textbutton "{size=+15}<<<{/size}":
            action SetVariable("gallerychar_julia_page", gallerychar_julia_page - 1)
            xalign 0.1
            yalign 1.0
    if (gallerychar_julia_page + 1) * maxpercharpage < len(gallery_juliaimages):
        textbutton "{size=+15}>>>{/size}":
            action SetVariable("gallerychar_julia_page", gallerychar_julia_page + 1)
            xalign 0.9
            yalign 1.0
    #return button
    textbutton "Return":
        action [SetVariable("gallerychar_julia_page", 0), Hide("gallerychar_julia", dissolve), Show("gallery", dissolve)]
        xalign 0.95
        yalign 0.05

    $ gallery_page_count = gallerychar_julia_page + 1
    $ gallery_page_total = maxpercharpage / 2 - 1

    textbutton "{color=#F8F8F8}{font=Digital-Medium.ttf}[gallery_page_count]/2{/font}{/color}":
        xalign 0.5
        yalign 1.0

    key "mousedown_3":
        action [SetVariable("gallerychar_julia_page", 0), Hide("gallerychar_julia", dissolve), Show("gallery", dissolve)]

screen gallerychar_valerie:

    add "galvalerieself1"
    add "images/Miscellaneous/picture.webp" xalign 1.0 yalign 1.0
    add Solid("#000a")
    text "Valerie Gallery" xalign 0.05 yalign 0.05 size 40
    hbox:
        xalign 0.5
        yalign 0.05
        spacing 20
        textbutton "{font=Digital-Medium.ttf}IMAGE GALLERY{/font}":
            action [Show("gallerychar_valerie", dissolve), Hide("replaychar_valerie", dissolve)]
        textbutton "{font=Digital-Medium.ttf}SCENE REPLAY{/font}":
            action [Show("replaychar_valerie", dissolve), Hide("gallerychar_valerie", dissolve)]


    $ start = gallerychar_valerie_page * maxpercharpage
    $ end = min(start + maxpercharpage - 1, len(gallery_valerieimages) - 1)

    #image grid
    grid maxnumcharx maxnumchary:
        xfill True
        yfill True

        for i in range(start, end + 1):
            $ gallery_valerieimages[i].refresh_lock()
            if gallery_valerieimages[i].is_locked:
                add gallery_valerieimages[i].locked:
                    xalign 0.5
                    yalign 0.5
            else:
                imagebutton idle gallery_valerieimages[i].thumb:
                    action Show("gallery_closeup", dissolve, gallery_valerieimages[i].images)
                    xalign 0.5
                    yalign 0.5

        for i in range(end - start + 1, maxpercharpage):
            null

    #names
    grid maxnumcharx maxnumchary:
        xfill True
        yfill True

        for i in range(start, end + 1):
            hbox:
                spacing 20
                xalign 0.5
                yalign 0.9
                $ total = gallery_valerieimages[i].num_images()
                $ partial = gallery_valerieimages[i].num_unlock
                if gallery_valerieimages[i].is_locked:
                    null
                else:
                    text gallery_valerieimages[i].name
                    text "[partial]/[total]"

        for i in range(end - start + 1, maxpercharpage):
            null

    #previous and next buttons
    if gallerychar_valerie_page > 0:
        textbutton "{size=+15}<<<{/size}":
            action SetVariable("gallerychar_valerie_page", gallerychar_valerie_page - 1)
            xalign 0.1
            yalign 1.0
    if (gallerychar_valerie_page + 1) * maxpercharpage < len(gallery_valerieimages):
        textbutton "{size=+15}>>>{/size}":
            action SetVariable("gallerychar_valerie_page", gallerychar_valerie_page + 1)
            xalign 0.9
            yalign 1.0
    #return button
    textbutton "Return":
        action [SetVariable("gallerychar_valerie_page", 0), Hide("gallerychar_valerie", dissolve), Show("gallery", dissolve)]
        xalign 0.95
        yalign 0.05

    $ gallery_page_count = gallerychar_valerie_page + 1
    $ gallery_page_total = maxpercharpage / 2 - 1

    textbutton "{color=#F8F8F8}{font=Digital-Medium.ttf}[gallery_page_count]/2{/font}{/color}":
        xalign 0.5
        yalign 1.0

    key "mousedown_3":
        action [SetVariable("gallerychar_valerie_page", 0), Hide("gallerychar_valerie", dissolve), Show("gallery", dissolve)]

screen gallerychar_laura:

    add "gallauraself1"
    add "images/Miscellaneous/picture.webp" xalign 1.0 yalign 1.0
    add Solid("#000a")
    text "Laura Gallery" xalign 0.05 yalign 0.05 size 40
    hbox:
        xalign 0.5
        yalign 0.05
        spacing 20
        textbutton "{font=Digital-Medium.ttf}IMAGE GALLERY{/font}":
            action [Show("gallerychar_laura", dissolve), Hide("replaychar_laura", dissolve)]
        textbutton "{font=Digital-Medium.ttf}SCENE REPLAY{/font}":
            action [Show("replaychar_laura", dissolve), Hide("gallerychar_laura", dissolve)]


    $ start = gallerychar_laura_page * maxpercharpage
    $ end = min(start + maxpercharpage - 1, len(gallery_lauraimages) - 1)

    #image grid
    grid maxnumcharx maxnumchary:
        xfill True
        yfill True

        for i in range(start, end + 1):
            $ gallery_lauraimages[i].refresh_lock()
            if gallery_lauraimages[i].is_locked:
                add gallery_lauraimages[i].locked:
                    xalign 0.5
                    yalign 0.5
            else:
                imagebutton idle gallery_lauraimages[i].thumb:
                    action Show("gallery_closeup", dissolve, gallery_lauraimages[i].images)
                    xalign 0.5
                    yalign 0.5

        for i in range(end - start + 1, maxpercharpage):
            null

    #names
    grid maxnumcharx maxnumchary:
        xfill True
        yfill True

        for i in range(start, end + 1):
            hbox:
                spacing 20
                xalign 0.5
                yalign 0.9
                $ total = gallery_lauraimages[i].num_images()
                $ partial = gallery_lauraimages[i].num_unlock
                if gallery_lauraimages[i].is_locked:
                    null
                else:
                    text gallery_lauraimages[i].name
                    text "[partial]/[total]"

        for i in range(end - start + 1, maxpercharpage):
            null

    #previous and next buttons
    if gallerychar_laura_page > 0:
        textbutton "{size=+15}<<<{/size}":
            action SetVariable("gallerychar_laura_page", gallerychar_laura_page - 1)
            xalign 0.1
            yalign 1.0
    if (gallerychar_laura_page + 1) * maxpercharpage < len(gallery_lauraimages):
        textbutton "{size=+15}>>>{/size}":
            action SetVariable("gallerychar_laura_page", gallerychar_laura_page + 1)
            xalign 0.9
            yalign 1.0
    #return button
    textbutton "Return":
        action [SetVariable("gallerychar_laura_page", 0), Hide("gallerychar_laura", dissolve), Show("gallery", dissolve)]
        xalign 0.95
        yalign 0.05

    $ gallery_page_count = gallerychar_laura_page + 1
    $ gallery_page_total = maxpercharpage / 2 - 1

    textbutton "{color=#F8F8F8}{font=Digital-Medium.ttf}[gallery_page_count]/2{/font}{/color}":
        xalign 0.5
        yalign 1.0

    key "mousedown_3":
        action [SetVariable("gallerychar_laura_page", 0), Hide("gallerychar_laura", dissolve), Show("gallery", dissolve)]

screen gallerychar_extra:

    add "galextra1"
    add "images/Miscellaneous/picture.webp" xalign 1.0 yalign 1.0
    add Solid("#000a")

    $ start = galleryextra_extra_page * maxperextrapage
    $ end = min(start + maxperextrapage - 1, len(gallery_extraimages) - 1)

    #image grid
    grid maxnumextrax maxnumextray:
        xfill True
        yfill True

        for i in range(start, end + 1):
            $ gallery_extraimages[i].refresh_lock()
            if gallery_extraimages[i].is_locked:
                add gallery_extraimages[i].locked:
                    xalign 0.5
                    yalign 0.5
            else:
                imagebutton idle gallery_extraimages[i].thumb:
                    action Show("gallery_closeup", dissolve, gallery_extraimages[i].images)
                    xalign 0.5
                    yalign 0.5

        for i in range(end - start + 1, maxperextrapage):
            null

    #names
    grid maxnumextrax maxnumextray:
        xfill True
        yfill True

        for i in range(start, end + 1):
            hbox:
                spacing maxthumbextray - 200
                xalign 0.5
                yalign 0.9
                $ total = gallery_extraimages[i].num_images()
                $ partial = gallery_extraimages[i].num_unlock
                if gallery_extraimages[i].is_locked:
                    null
                else:
                    text gallery_extraimages[i].name

        for i in range(end - start + 1, maxperextrapage):
            null

    #previous and next buttons
    text "Extra Gallery" xalign 0.05 yalign 0.05 size 40

    if galleryextra_extra_page > 0:
        textbutton "{size=+15}<<<{/size}":
            action SetVariable("galleryextra_extra_page", galleryextra_extra_page - 1)
            xalign 0.1
            yalign 1.0
    if (galleryextra_extra_page + 1) * maxperextrapage < len(gallery_extraimages):
        textbutton "{size=+15}>>>{/size}":
            action SetVariable("galleryextra_extra_page", galleryextra_extra_page + 1)
            xalign 0.9
            yalign 1.0
    #return button
    textbutton "Return":
        action [SetVariable("galleryextra_extra_page", 0), Hide("galleryextra_extra", dissolve), Show("gallery", dissolve)]
        xalign 0.95
        yalign 0.05

    $ gallery_page_count = galleryextra_extra_page + 1
    $ gallery_page_total = maxperextrapage / 2 - 1

    textbutton "{color=#F8F8F8}{font=Digital-Medium.ttf}[gallery_page_count]/4{/font}{/color}":
        xalign 0.5
        yalign 1.0

    key "mousedown_3":
        action [SetVariable("galleryextra_extra_page", 0), Hide("galleryextra_extra", dissolve), Show("gallery", dissolve)]

screen gallerychar_misc:

    add "galmisc"
    add "images/Miscellaneous/picture.webp" xalign 1.0 yalign 1.0
    add Solid("#000a")

    $ start = gallerymisc_misc_page * maxpermiscpage
    $ end = min(start + maxpermiscpage - 1, len(gallery_miscimages) - 1)

    #image grid
    grid maxnummiscx maxnummiscy:
        xfill True
        yfill True

        for i in range(start, end + 1):
            $ gallery_miscimages[i].refresh_lock()
            if gallery_miscimages[i].is_locked:
                add gallery_miscimages[i].locked:
                    xalign 0.5
                    yalign 0.5
            else:
                imagebutton idle gallery_miscimages[i].thumb:
                    action Show("gallery_closeup", dissolve, gallery_miscimages[i].images)
                    xalign 0.5
                    yalign 0.5

        for i in range(end - start + 1, maxpermiscpage):
            null

    #names
    grid maxnummiscx maxnummiscy:
        xfill True
        yfill True

        for i in range(start, end + 1):
            hbox:
                spacing maxthumbmiscy - 200
                xalign 0.5
                yalign 0.9
                $ total = gallery_miscimages[i].num_images()
                $ partial = gallery_miscimages[i].num_unlock
                text gallery_miscimages[i].name

        for i in range(end - start + 1, maxpermiscpage):
            null

    #previous and next buttons
    text "Miscellaneous" xalign 0.05 yalign 0.05 size 40

    if gallerymisc_misc_page > 0:
        textbutton "{size=+15}<<<{/size}":
            action SetVariable("gallerymisc_misc_page", gallerymisc_misc_page - 1)
            xalign 0.1
            yalign 1.0
    if (gallerymisc_misc_page + 1) * maxpermiscpage < len(gallery_miscimages):
        textbutton "{size=+15}>>>{/size}":
            action SetVariable("gallerymisc_misc_page", gallerymisc_misc_page + 1)
            xalign 0.9
            yalign 1.0
    #return button
    textbutton "Return":
        action [SetVariable("gallerymisc_misc_page", 0), Hide("gallerymisc_misc", dissolve), Show("gallery", dissolve)]
        xalign 0.95
        yalign 0.05

    $ gallery_page_count = gallerymisc_misc_page + 1
    $ gallery_page_total = maxpermiscpage / 2 - 1

    textbutton "{color=#F8F8F8}{font=Digital-Medium.ttf}[gallery_page_count]/4{/font}{/color}":
        xalign 0.5
        yalign 1.0

    key "mousedown_3":
        action [SetVariable("gallerymisc_misc_page", 0), Hide("gallerymisc_misc", dissolve), Show("gallery", dissolve)]

screen gallery_closeup(images):

    modal True
    add "black"
    add images[closeup_page] at center
    $ total = len(images)
    $ partial = closeup_page + 1
    textbutton "{color=#F8F8F8}{font=Digital-Medium.ttf}[partial]/[total]{/font}{/color}":
        xalign 0.0
        yalign 0.0
        background "black"

    if closeup_page > 0:
        textbutton "{font=Digital-Medium.ttf}Previous{/font}":
            action SetVariable("closeup_page", closeup_page - 1)
            xalign 0.1
            yalign 1.0
            background "black"
    if closeup_page < len(images) - 1:
        textbutton "{font=Digital-Medium.ttf}Next{/font}":
            action SetVariable("closeup_page", closeup_page + 1)
            xalign 0.9
            yalign 1.0
            background "black"

    textbutton "{font=Digital-Medium.ttf}Return{/font}":
        action [SetVariable("closeup_page", 0), Hide("gallery_closeup", dissolve)]
        xalign 0.5
        yalign 1.0
        background "black"

    key "mousedown_3":
        action [SetVariable("closeup_page", 0), Hide("gallery_closeup", dissolve)]

screen replay:
    tag menu

    add "galbackground2"
    if persistent.eileen_full_ending:
        add None
    else:
        add "galeileen2"
    if charlotte_sixth_day_finish:
#    if persistent.charlotte_full_ending:
        add "galcharlotte2"
    elif julia_fourth_day_finish:
#    elif persistent.julia_full_ending:
        add "galjulia2"
    elif valerie_fourth_day_finish:
#    elif persistent.valerie_full_ending:
        add "galvalerie2"
    elif laura_second_day_finish:
#    elif persistent.laura_full_ending:
        add "gallaura2"
    elif persistent.eileen_full_ending:
        add "galeileentrue2"
    add "images/Miscellaneous/reel.webp" xalign 1.0 yalign 1.0
    add Solid("#000a")
        #    elif persistent.harem_full_ending:
        #        add "galharem1.webp"
    text "{font=digital-7.ttf}SCENES{/font}" xalign 0.05 yalign 0.05 size 50
    hbox:
        xalign 0.5
        yalign 0.05
        spacing 20
        textbutton "{font=Digital-Medium.ttf}IMAGE GALLERY{/font}":
            action Show("gallery", dissolve)
        textbutton "{font=Digital-Medium.ttf}SCENE REPLAY{/font}":
            action Show("replay", dissolve)


    $ start = gallery_page * maxperpage
    $ end = min(start + maxperpage - 1, len(gallery_images) - 1)

    #image grid
    grid maxnumx maxnumy:
        xfill True
        yfill True

        for i in range(start, end + 1):
            $ gallery_images[i].refresh_lock()
            if gallery_images[i].is_locked:
                null
            elif gallery_images[i].name == "Extra":
                null
            elif gallery_images[i].name == "Miscellaneous":
                null
            else:
                imagebutton idle gallery_images[i].thumb[1]:
                    if gallery_images[i].name == "Charlotte":
                        action [Show("replaychar_charlotte", dissolve), Hide("replay", dissolve)]
                    elif gallery_images[i].name == "Julia":
                        action [Show("replaychar_julia", dissolve), Hide("replay", dissolve)]
                    elif gallery_images[i].name == "Valerie":
                        action [Show("replaychar_valerie", dissolve), Hide("replay", dissolve)]
                    elif gallery_images[i].name == "Laura":
                        action [Show("replaychar_laura", dissolve), Hide("replay", dissolve)]
                    elif gallery_images[i].name == "Eileen":
                        action [Show("replaychar_eileen", dissolve), Hide("replay", dissolve)]
                    elif gallery_images[i].name == "Harem":
                        action [Show("replaychar_harem", dissolve), Hide("replay", dissolve)]
                    xalign 0.5
                    yalign 0.5

        for i in range(end - start + 1, maxperpage):
            null

    #names
    grid maxnumx maxnumy:
        xfill True
        yfill True

        for i in range(start, end + 1):
            hbox:
                spacing maxthumby - 150
                xalign 0.5
                yalign 0.9
                $ total = gallery_images[i].num_images()
                $ partial = gallery_images[i].num_unlock
                if gallery_images[i].is_locked:
                    null
                elif gallery_images[i].name == "Extra":
                    null
                elif gallery_images[i].name == "Miscellaneous":
                    null
                else:
                    text gallery_images[i].name
                    text "[partial]/[total]"

        for i in range(end - start + 1, maxperpage):
            null

    #previous and next buttons
    if gallery_page > 0:
        textbutton "{size=+15}<<<{/size}":
            action SetVariable("gallery_page", gallery_page - 1)
            xalign 0.1
            yalign 1.0
    if (gallery_page + 1) * maxperpage < len(gallery_images) - 2:
        textbutton "{size=+15}>>>{/size}":
            action SetVariable("gallery_page", gallery_page + 1)
            xalign 0.9
            yalign 1.0
    #return button
    textbutton "Return":
        action Return()
        xalign 0.95
        yalign 0.05

    $ gallery_page_count = gallery_page + 1
    $ gallery_page_total = maxperpage / 2 - 1

    textbutton "{color=#F8F8F8}{font=Digital-Medium.ttf}[gallery_page_count]/2{/font}{/color}":
        xalign 0.5
        yalign 1.0

    key "mousedown_3":
        action Return()

screen replaychar_charlotte:

    add "galcharlotteself2"
    add "images/Miscellaneous/reel.webp" xalign 1.0 yalign 1.0
    add Solid("#000a")
    text "Charlotte Replay" xalign 0.05 yalign 0.05 size 40
    hbox:
        xalign 0.5
        yalign 0.05
        spacing 20
        textbutton "{font=Digital-Medium.ttf}IMAGE GALLERY{/font}":
            action [Show("gallerychar_charlotte", dissolve), Hide("replaychar_charlotte", dissolve)]
        textbutton "{font=Digital-Medium.ttf}SCENE REPLAY{/font}":
            action [Show("replaychar_charlotte", dissolve), Hide("gallerychar_charlotte", dissolve)]

    $ start = gallerychar_charlotte_page * maxpercharpage
    $ end = min(start + maxpercharpage - 1, len(gallery_charlotteimages) - 1)

    #image grid
    grid maxnumcharx maxnumchary:
        xfill True
        yfill True

        for i in range(start, end + 1):
            $ gallery_charlotteimages[i].refresh_lock()
            if gallery_charlotteimages[i].replay is None:
                null
            elif gallery_charlotteimages[i].is_locked:
                add gallery_charlotteimages[i].locked:
                    xalign 0.5
                    yalign 0.5
            else:
                imagebutton idle gallery_charlotteimages[i].thumb:
                    action Replay(gallery_charlotteimages[i].replay)

                    xalign 0.5
                    yalign 0.5

        for i in range(end - start + 1, maxpercharpage):
            null

    #names
    grid maxnumcharx maxnumchary:
        xfill True
        yfill True

        for i in range(start, end + 1):
            hbox:
                spacing 20
                xalign 0.5
                yalign 0.9
                $ total = gallery_charlotteimages[i].num_images()
                $ partial = gallery_charlotteimages[i].num_unlock
                if gallery_charlotteimages[i].replay is None:
                    null
                elif gallery_charlotteimages[i].is_locked:
                    null
                else:
                    text gallery_charlotteimages[i].name

        for i in range(end - start + 1, maxpercharpage):
            null

    #previous and next buttons
    if gallerychar_charlotte_page > 0:
        textbutton "{size=+15}<<<{/size}":
            action SetVariable("gallerychar_charlotte_page", gallerychar_charlotte_page - 1)
            xalign 0.1
            yalign 1.0
    if (gallerychar_charlotte_page + 1) * maxpercharpage < (len(gallery_charlotteimages) / 2):
        textbutton "{size=+15}>>>{/size}":
            action SetVariable("gallerychar_charlotte_page", gallerychar_charlotte_page + 1)
            xalign 0.9
            yalign 1.0
    #return button
    textbutton "Return":
        action [SetVariable("gallerychar_charlotte_page", 0), Hide("replaychar_charlotte", dissolve), Show("replay", dissolve)]
        xalign 0.95
        yalign 0.05

    $ gallery_page_count = gallerychar_charlotte_page + 1

    textbutton "{color=#F8F8F8}{font=Digital-Medium.ttf}[gallery_page_count]/1{/font}{/color}":
        xalign 0.5
        yalign 1.0

    key "mousedown_3":
        action [SetVariable("gallerychar_charlotte_page", 0), Hide("gallerychar_charlotte", dissolve), Show("replay", dissolve)]

screen replaychar_julia:

    add "galjuliaself2"
    add "images/Miscellaneous/reel.webp" xalign 1.0 yalign 1.0
    add Solid("#000a")
    text "Julia Replay" xalign 0.05 yalign 0.05 size 40
    hbox:
        xalign 0.5
        yalign 0.05
        spacing 20
        textbutton "{font=Digital-Medium.ttf}IMAGE GALLERY{/font}":
            action [Show("gallerychar_julia", dissolve), Hide("replaychar_julia", dissolve)]
        textbutton "{font=Digital-Medium.ttf}SCENE REPLAY{/font}":
            action [Show("replaychar_julia", dissolve), Hide("gallerychar_julia", dissolve)]

    $ start = gallerychar_julia_page * maxpercharpage
    $ end = min(start + maxpercharpage - 1, len(gallery_juliaimages) - 1)

    #image grid
    grid maxnumcharx maxnumchary:
        xfill True
        yfill True

        for i in range(start, end + 1):
            $ gallery_juliaimages[i].refresh_lock()
            if gallery_juliaimages[i].replay is None:
                null
            elif gallery_juliaimages[i].is_locked:
                add gallery_juliaimages[i].locked:
                    xalign 0.5
                    yalign 0.5
            else:
                imagebutton idle gallery_juliaimages[i].thumb:
                    action Replay(gallery_juliaimages[i].replay)

                    xalign 0.5
                    yalign 0.5

        for i in range(end - start + 1, maxpercharpage):
            null

    #names
    grid maxnumcharx maxnumchary:
        xfill True
        yfill True

        for i in range(start, end + 1):
            hbox:
                spacing 20
                xalign 0.5
                yalign 0.9
                $ total = gallery_juliaimages[i].num_images()
                $ partial = gallery_juliaimages[i].num_unlock
                if gallery_juliaimages[i].replay is None:
                    null
                elif gallery_juliaimages[i].is_locked:
                    null
                else:
                    text gallery_juliaimages[i].name

        for i in range(end - start + 1, maxpercharpage):
            null

    #previous and next buttons
    if gallerychar_julia_page > 0:
        textbutton "{size=+15}<<<{/size}":
            action SetVariable("gallerychar_julia_page", gallerychar_julia_page - 1)
            xalign 0.1
            yalign 1.0
    if (gallerychar_julia_page + 1) * maxpercharpage < (len(gallery_juliaimages) / 2):
        textbutton "{size=+15}>>>{/size}":
            action SetVariable("gallerychar_julia_page", gallerychar_julia_page + 1)
            xalign 0.9
            yalign 1.0
    #return button
    textbutton "Return":
        action [SetVariable("gallerychar_julia_page", 0), Hide("replaychar_julia", dissolve), Show("replay", dissolve)]
        xalign 0.95
        yalign 0.05

    $ gallery_page_count = gallerychar_julia_page + 1

    textbutton "{color=#F8F8F8}{font=Digital-Medium.ttf}[gallery_page_count]/1{/font}{/color}":
        xalign 0.5
        yalign 1.0

    key "mousedown_3":
        action [SetVariable("gallerychar_julia_page", 0), Hide("gallerychar_julia", dissolve), Show("replay", dissolve)]

screen replaychar_valerie:

    add "galvalerieself2"
    add "images/Miscellaneous/reel.webp" xalign 1.0 yalign 1.0
    add Solid("#000a")
    text "Valerie Replay" xalign 0.05 yalign 0.05 size 40
    hbox:
        xalign 0.5
        yalign 0.05
        spacing 20
        textbutton "{font=Digital-Medium.ttf}IMAGE GALLERY{/font}":
            action [Show("gallerychar_valerie", dissolve), Hide("replaychar_valerie", dissolve)]
        textbutton "{font=Digital-Medium.ttf}SCENE REPLAY{/font}":
            action [Show("replaychar_valerie", dissolve), Hide("gallerychar_valerie", dissolve)]

    $ start = gallerychar_valerie_page * maxpercharpage
    $ end = min(start + maxpercharpage - 1, len(gallery_valerieimages) - 1)

    #image grid
    grid maxnumcharx maxnumchary:
        xfill True
        yfill True

        for i in range(start, end + 1):
            $ gallery_valerieimages[i].refresh_lock()
            if gallery_valerieimages[i].replay is None:
                null
            elif gallery_valerieimages[i].is_locked:
                add gallery_valerieimages[i].locked:
                    xalign 0.5
                    yalign 0.5
            else:
                imagebutton idle gallery_valerieimages[i].thumb:
                    action Replay(gallery_valerieimages[i].replay)

                    xalign 0.5
                    yalign 0.5

        for i in range(end - start + 1, maxpercharpage):
            null

    #names
    grid maxnumcharx maxnumchary:
        xfill True
        yfill True

        for i in range(start, end + 1):
            hbox:
                spacing 20
                xalign 0.5
                yalign 0.9
                $ total = gallery_valerieimages[i].num_images()
                $ partial = gallery_valerieimages[i].num_unlock
                if gallery_valerieimages[i].replay is None:
                    null
                elif gallery_valerieimages[i].is_locked:
                    null
                else:
                    text gallery_valerieimages[i].name

        for i in range(end - start + 1, maxpercharpage):
            null

    #previous and next buttons
    if gallerychar_valerie_page > 0:
        textbutton "{size=+15}<<<{/size}":
            action SetVariable("gallerychar_valerie_page", gallerychar_valerie_page - 1)
            xalign 0.1
            yalign 1.0
    if (gallerychar_valerie_page + 1) * maxpercharpage < (len(gallery_valerieimages) / 2):
        textbutton "{size=+15}>>>{/size}":
            action SetVariable("gallerychar_valerie_page", gallerychar_valerie_page + 1)
            xalign 0.9
            yalign 1.0
    #return button
    textbutton "Return":
        action [SetVariable("gallerychar_valerie_page", 0), Hide("replaychar_valerie", dissolve), Show("replay", dissolve)]
        xalign 1.0
        yalign 0.01

    $ gallery_page_count = gallerychar_valerie_page + 1

    textbutton "{color=#F8F8F8}{font=Digital-Medium.ttf}[gallery_page_count]/1{/font}{/color}":
        xalign 0.5
        yalign 1.0

    key "mousedown_3":
        action [SetVariable("gallerychar_valerie_page", 0), Hide("gallerychar_valerie", dissolve), Show("replay", dissolve)]

screen replaychar_laura:

    add "gallauraself2"
    add "images/Miscellaneous/reel.webp" xalign 1.0 yalign 1.0
    add Solid("#000a")
    text "Laura Replay" xalign 0.05 yalign 0.05 size 40
    hbox:
        xalign 0.5
        yalign 0.05
        spacing 20
        textbutton "{font=Digital-Medium.ttf}IMAGE GALLERY{/font}":
            action [Show("gallerychar_laura", dissolve), Hide("replaychar_laura", dissolve)]
        textbutton "{font=Digital-Medium.ttf}SCENE REPLAY{/font}":
            action [Show("replaychar_laura", dissolve), Hide("gallerychar_laura", dissolve)]

    $ start = gallerychar_laura_page * maxpercharpage
    $ end = min(start + maxpercharpage - 1, len(gallery_lauraimages) - 1)

    #image grid
    grid maxnumcharx maxnumchary:
        xfill True
        yfill True

        for i in range(start, end + 1):
            $ gallery_lauraimages[i].refresh_lock()
            if gallery_lauraimages[i].replay is None:
                null
            elif gallery_lauraimages[i].is_locked:
                add gallery_lauraimages[i].locked:
                    xalign 0.5
                    yalign 0.5
            else:
                imagebutton idle gallery_lauraimages[i].thumb:
                    action Replay(gallery_lauraimages[i].replay)

                    xalign 0.5
                    yalign 0.5

        for i in range(end - start + 1, maxpercharpage):
            null

    #names
    grid maxnumcharx maxnumchary:
        xfill True
        yfill True

        for i in range(start, end + 1):
            hbox:
                spacing 20
                xalign 0.5
                yalign 0.9
                $ total = gallery_lauraimages[i].num_images()
                $ partial = gallery_lauraimages[i].num_unlock
                if gallery_lauraimages[i].replay is None:
                    null
                elif gallery_lauraimages[i].is_locked:
                    null
                else:
                    text gallery_lauraimages[i].name

        for i in range(end - start + 1, maxpercharpage):
            null

    #previous and next buttons
    if gallerychar_laura_page > 0:
        textbutton "{size=+15}<<<{/size}":
            action SetVariable("gallerychar_laura_page", gallerychar_laura_page - 1)
            xalign 0.1
            yalign 1.0
    if (gallerychar_laura_page + 1) * maxpercharpage < (len(gallery_lauraimages) / 2):
        textbutton "{size=+15}>>>{/size}":
            action SetVariable("gallerychar_laura_page", gallerychar_laura_page + 1)
            xalign 0.9
            yalign 1.0
    #return button
    textbutton "Return":
        action [SetVariable("gallerychar_laura_page", 0), Hide("replaychar_laura", dissolve), Show("replay", dissolve)]
        xalign 1.0
        yalign 0.01

    $ gallery_page_count = gallerychar_laura_page + 1

    textbutton "{color=#F8F8F8}{font=Digital-Medium.ttf}[gallery_page_count]/1{/font}{/color}":
        xalign 0.5
        yalign 1.0

    key "mousedown_3":
        action [SetVariable("gallerychar_laura_page", 0), Hide("gallerychar_laura", dissolve), Show("replay", dissolve)]

define config.enter_replay_transition = Fade(0.5, 0.0, 0.5)
define config.exit_replay_transition = Fade(0.5, 0.0, 0.5)
define config.replay_scope = {"povname": persistent.povname}
