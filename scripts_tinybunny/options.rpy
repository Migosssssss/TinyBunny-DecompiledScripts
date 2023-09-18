

define config.image_cache_size_mb = 1024



define config.developer = False



define it_is_demo = True



define config.rollback_enabled = False



define config.mouse = { 'default' : [ ("images/interface/cursor.png", 0, 0)] }



define config.has_autosave = False



define config.afm_bonus = 5

define config.layers = [ 'master' , 'master1' , 'transient', 'screens', 'overlay' ]



define config.name = _("Tiny Bunny")




define gui.show_name = True



define config.version = "4.1"




define gui.about = _p("""
""")




define build.name = "TinyBunny"






define config.has_sound = True
define config.has_music = True
define config.has_voice = True
define config.default_music_volume = 0.8










define config.main_menu_music = "music/Menu_Tiny_Bunny.ogg"










define config.enter_transition = None
define config.exit_transition = None




define config.intra_transition = None




define config.after_load_transition = None




define config.end_game_transition = None
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)








default preferences.text_cps = 0





default preferences.afm_time = 15
















define config.save_directory = "TinyBunny 2.0.0"






define config.window_icon = "gui/window_icon.png"







init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('game/**.gif', None)
    build.classify('game/**.rpy', None)
    build.classify('game/**.rpym', None)



    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.ogv', 'archive')
    build.classify('game/**.otf', 'archive')
    build.classify('game/**.ttf', 'archive')
    build.classify('game/**.mp3', 'archive')
    build.classify('game/**.webm', 'archive')
    build.classify('game/**.rpyc', 'archive')
    build.classify('game/**.rpymc', 'archive')





    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
