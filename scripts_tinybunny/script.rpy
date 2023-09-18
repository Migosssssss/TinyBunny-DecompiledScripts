
default music_during_lines = 1.0
default music_during_lines_delay_on = 0.5
default music_during_lines_delay_off = 2.5
default music_general_volume = 1.0
init -10 python:
    def music_volume_adjustment(event, interact=True, **kwargs):
        global music_during_lines
        if not interact:
            return
        
        if event == "begin":
            renpy.music.set_volume(music_during_lines*music_general_volume, music_during_lines_delay_on, channel="music")
            renpy.music.set_volume(music_during_lines*music_general_volume, music_during_lines_delay_on, channel="music2")
        elif event == "end":
            renpy.music.set_volume(music_general_volume, music_during_lines_delay_off, channel="music")
            renpy.music.set_volume(music_general_volume, music_during_lines_delay_off, channel="music2")



define Ant = Character(_('Антон'),         what_prefix='"', what_suffix='"', callback=music_volume_adjustment)
define Ant_m = Character(None,               what_prefix='{i}', what_suffix='{/i}', callback=music_volume_adjustment)
define Oly = Character(_('Оля'),           what_prefix='"', what_suffix='"', callback=music_volume_adjustment)
define Mam = Character(_('Мама'),          what_prefix='"', what_suffix='"', callback=music_volume_adjustment)
define Pap = Character(_('Отец'),          what_prefix='"', what_suffix='"', callback=music_volume_adjustment)
define Gra = Character(_('Бабушка'),       what_prefix='"', what_suffix='"', callback=music_volume_adjustment)

define Pol = Character(_('Полина'),        what_prefix='"', what_suffix='"', callback=music_volume_adjustment)
define Kate = Character(_('Катя'),          what_prefix='"', what_suffix='"', callback=music_volume_adjustment)

define Ryz = Character(_('Рыжий'),         what_prefix='"', what_suffix='"', callback=music_volume_adjustment)
define Sem = Character(_('Семён'),         what_prefix='"', what_suffix='"', callback=music_volume_adjustment)
define Rom = Character(_('Рома'),          what_prefix='"', what_suffix='"', callback=music_volume_adjustment)
define Bya = Character(_('Бяша'),          what_prefix='"', what_suffix='"', callback=music_volume_adjustment)

define Tikhonov = Character(_('Тихонов'),          what_prefix='"', what_suffix='"', callback=music_volume_adjustment)

define Alis = Character(_('Алиса'),         what_prefix='"', what_suffix='"', callback=music_volume_adjustment)
define Alis_Color = Character(_('Алиса'),       what_prefix='"', what_suffix='"', callback=music_volume_adjustment, 
    window_background=Frame("images/interface/panel3.png", xalign=0.5, yalign=1.0, ysize=gui.textbox_height, xsize=1600),
    who_color = "#FCB892")

define Fox = Character(_('Лиса'),          what_prefix='"', what_suffix='"', callback=music_volume_adjustment)
define Bear = Character(_('Медвежутка'),       what_prefix='"', what_suffix='"', callback=music_volume_adjustment)
define Wolf = Character(_('Волчик'),          what_prefix='"', what_suffix='"', callback=music_volume_adjustment)
define Goat = Character(_('Козёл'),         what_prefix='"', what_suffix='"', callback=music_volume_adjustment)
define Owl = Character(_('Совушка'),          what_prefix='"', what_suffix='"', callback=music_volume_adjustment)
define Master = Character(_('Хозяин Леса'),          what_prefix='"', what_suffix='"', callback=music_volume_adjustment)

define Mil = Character(_('Милиционер'),    what_prefix='"', what_suffix='"', callback=music_volume_adjustment)
define Teacher = Character(_('Учительница'),   what_prefix='"', what_suffix='"', callback=music_volume_adjustment)
define Tam = Character(_('Тамара'),        what_prefix='"', what_suffix='"', callback=music_volume_adjustment)
define Dic = Character(_('Диктор'),        what_prefix='"', what_suffix='"', callback=music_volume_adjustment)
define Childs = Character(_('Дети'),          what_prefix='"', what_suffix='"', callback=music_volume_adjustment)
define Classmate = Character(_('Одноклассник'),          what_prefix='"', what_suffix='"', callback=music_volume_adjustment)
define Pupils = Character(_('Школьники'),          what_prefix='"', what_suffix='"', callback=music_volume_adjustment)

define Animals = Character(_('Звери'),          what_prefix='"', what_suffix='"', callback=music_volume_adjustment)
define Noname = Character('???',              what_prefix='"', what_suffix='"', callback=music_volume_adjustment)

define Narrator_color = Character(None, window_background=Frame("images/interface/panel3.png", xalign=0.5, yalign=1.0, ysize=gui.textbox_height, xsize=1600), what_prefix='{i}', what_suffix='{/i}')
define Narr_color = Character(None, window_background=Frame("images/interface/panel3.png", xalign=0.5, yalign=1.0, ysize=gui.textbox_height, xsize=1600), what_prefix='{i}', what_suffix='{/i}')

define Frost = Character(_('Дед Мороз'), what_prefix='"', what_suffix='"', callback=music_volume_adjustment)
define Ded = Character(_('Харитон'), what_prefix='"', what_suffix='"', callback=music_volume_adjustment)
define Bunny = Character(_('Зайчик'), what_prefix='"{i}', what_suffix='{/i}"', callback=music_volume_adjustment)

define Frost_Color = Character(_('Дед Мороз'),       what_prefix='"', what_suffix='"', callback=music_volume_adjustment,
    window_background=Frame("images/interface/panel3.png", xalign=0.5, yalign=1.0, ysize=gui.textbox_height, xsize=1600),
    who_color = "#DC4258")
define Olya_Color = Character(_('Оля'),       what_prefix='"', what_suffix='"', callback=music_volume_adjustment,
    window_background=Frame("images/interface/panel3.png", xalign=0.5, yalign=1.0, ysize=gui.textbox_height, xsize=1600),
    who_color = "#FF77EB")
define Ant_Color = Character(_('Антон'),       what_prefix='"', what_suffix='"', callback=music_volume_adjustment,
    window_background=Frame("images/interface/panel3.png", xalign=0.5, yalign=1.0, ysize=gui.textbox_height, xsize=1600),
    who_color = "#FFFFFF")
define Children_Color = Character(_('Дети'),       what_prefix='"', what_suffix='"', callback=music_volume_adjustment,
    window_background=Frame("images/interface/panel3.png", xalign=0.5, yalign=1.0, ysize=gui.textbox_height, xsize=1600),
    who_color = "#A4D6F6")

define Chorus = Character(_('Хор'),          what_prefix='"', what_suffix='"', callback=music_volume_adjustment)
define Radio = Character(_('Радио'),          what_prefix='"', what_suffix='"', callback=music_volume_adjustment)

define AntOly = Character(_('Антон и Оля'),         what_prefix='"', what_suffix='"', callback=music_volume_adjustment)

define Lilia_P = Character(_('Лилия Павловна'),   what_prefix='"', what_suffix='"', callback=music_volume_adjustment)

default is_save_allowed = True

label start:
    stop music fadeout 2.0
    $ reset_item_and_choice()


    jump day_1

    return

label after_load:
    if renpy.music.get_playing(channel='music') == config.main_menu_music:
        stop music fadeout .25
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
