
init:
    $ generate_img('Mom', 'Angry', 'm_day', '00', 'norm', 'aside')
    $ generate_img('Mom', 'Angry', 'm_day', '01', 'norm', 'aside')
    $ generate_img('Mom', 'Angry', 'm_day', '00', 'norm', 'ahead')
    $ generate_img('Mom', 'Angry', 'm_day', '01', 'norm', 'ahead')
    $ generate_img('Mom', 'Angry', 'm_evening', '00', 'norm', 'aside')
    $ generate_img('Mom', 'Angry', 'm_evening', '01', 'norm', 'aside')
    $ generate_img('Mom', 'Angry', 'm_evening', '00', 'norm', 'ahead', blur='blur')
    $ generate_img('Mom', 'Angry', 'm_evening', '00', 'norm', 'ahead')
    $ generate_img('Mom', 'Angry', 'm_evening', '01', 'norm', 'ahead')

    $ generate_img('Mom', 'Scared', 'm_day', '00', 'norm', 'aside')
    $ generate_img('Mom', 'Scared', 'm_day', '00', 'norm', 'ahead')

    $ generate_img('Mom', 'Normal', 'm_day', '00', 'norm', 'aside')
    $ generate_img('Mom', 'Normal', 'm_day', '01', 'norm', 'aside')
    $ generate_img('Mom', 'Normal', 'm_day', '02', 'norm', 'aside')
    $ generate_img('Mom', 'Normal', 'm_day', '03', 'norm', 'aside')
    $ generate_img('Mom', 'Normal', 'm_day', '04', 'norm', 'aside')
    $ generate_img('Mom', 'Normal', 'm_day', '05', 'norm', 'aside')
    $ generate_img('Mom', 'Normal', 'm_day', '06', 'norm', 'aside')
    $ generate_img('Mom', 'Normal', 'm_day', '07', 'norm', 'aside')
    $ generate_img('Mom', 'Normal', 'm_day', '00', 'norm', 'ahead')
    $ generate_img('Mom', 'Normal', 'm_day', '01', 'norm', 'ahead')
    $ generate_img('Mom', 'Normal', 'm_day', '02', 'norm', 'ahead')
    $ generate_img('Mom', 'Normal', 'm_day', '03', 'norm', 'ahead')
    $ generate_img('Mom', 'Normal', 'm_day', '04', 'norm', 'ahead')
    $ generate_img('Mom', 'Normal', 'm_day', '05', 'norm', 'ahead')
    $ generate_img('Mom', 'Normal', 'm_day', '06', 'norm', 'ahead')
    $ generate_img('Mom', 'Normal', 'm_day', '07', 'norm', 'ahead')
    $ generate_img('Mom', 'Normal', 'm_evening', '00', 'norm', 'aside')
    $ generate_img('Mom', 'Normal', 'm_evening', '00', 'norm', 'aside', blur='blur')
    $ generate_img('Mom', 'Normal', 'm_evening', '01', 'norm', 'aside')
    $ generate_img('Mom', 'Normal', 'm_evening', '02', 'norm', 'aside')
    $ generate_img('Mom', 'Normal', 'm_evening', '03', 'norm', 'aside')
    $ generate_img('Mom', 'Normal', 'm_evening', '04', 'norm', 'aside')
    $ generate_img('Mom', 'Normal', 'm_evening', '05', 'norm', 'aside')
    $ generate_img('Mom', 'Normal', 'm_evening', '06', 'norm', 'aside')
    $ generate_img('Mom', 'Normal', 'm_evening', '07', 'norm', 'aside')
    $ generate_img('Mom', 'Normal', 'm_evening', '00', 'norm', 'ahead')
    $ generate_img('Mom', 'Normal', 'm_evening', '01', 'norm', 'ahead')
    $ generate_img('Mom', 'Normal', 'm_evening', '02', 'norm', 'ahead')
    $ generate_img('Mom', 'Normal', 'm_evening', '03', 'norm', 'ahead')
    $ generate_img('Mom', 'Normal', 'm_evening', '04', 'norm', 'ahead')
    $ generate_img('Mom', 'Normal', 'm_evening', '05', 'norm', 'ahead')
    $ generate_img('Mom', 'Normal', 'm_evening', '06', 'norm', 'ahead')
    $ generate_img('Mom', 'Normal', 'm_evening', '07', 'norm', 'ahead')
    $ generate_img('Mom', 'Normal', 'm_night', '00', 'norm', 'aside')
    $ generate_img('Mom', 'Normal', 'm_night', '00', 'norm', 'ahead')

    $ generate_img('Mom', 'Mask', 'b_night', '00')
    $ generate_img('Mom', 'Mask', 'm_night', '00')

    $ generate_img('Mom', 'Normal', 'm_evening', '01', 'norm', 'ahead', blur = 'blur')
    $ generate_img('Mom', 'Normal', 'm_evening', '07', 'norm', 'ahead', blur = 'blur')



    $ generate_img('Mom', 'Happy', 'b_evening', '01', 'norm', 'ahead')
    $ generate_img('Mom', 'Normal', 'b_evening', '01', 'norm', 'ahead')
    $ generate_img('Mom', 'Angry', 'b_evening', '01', 'norm', 'ahead', "01")
    $ generate_img('Mom', 'Evil', 'b_evening', '01', 'norm', 'ahead')
    $ generate_img('Mom', 'Evil', 'b_evening', '01', 'norm', 'ahead', '01')

    image Mom_Angry_m_day_00_norm_ahead_narco:
        contains:
            alpha 0.0
            linear 0.3 alpha 0.5
            contains:
                "Mom Angry m_day 00 norm ahead"
                alpha 1.0
                linear 0.25 xoffset -10 yoffset 0
                linear 0.25 xoffset -20 yoffset 0
                linear 0.45 xoffset -40 yoffset 0
                linear 0.35 xoffset -50 yoffset 0
                linear 0.25 xoffset -10 yoffset 0
                linear 0.55 xoffset 10 yoffset 0 alpha 0.0
            linear 15.00
            repeat

    image Mom_Normal_m_day_00_norm_ahead_narco:
        contains:
            alpha 0.0
            linear 0.3 alpha 0.5
            contains:
                "Mom Normal m_day 00 norm ahead"
                alpha 1.0
                linear 0.25 xoffset -10 yoffset 0
                linear 0.25 xoffset -20 yoffset 0
                linear 0.45 xoffset -40 yoffset 0
                linear 0.35 xoffset -50 yoffset 0
                linear 0.25 xoffset -10 yoffset 0
                linear 0.55 xoffset 10 yoffset 0 alpha 0.0
            linear 15.00
            repeat

transform mom_right:
    xpos 100 ypos 0 xzoom -1.0

transform mom_left:
    xpos 300 ypos 0 xzoom 1.0

transform mom_income:
    xzoom -1.0
    alpha 0.0
    ypos 0
    xpos 350
    linear 0.5 alpha 0.5 xpos 280 ypos 20
    linear 0.5 alpha 1.0 xpos 210 ypos 0
    linear 0.5 alpha 1.0 xpos 140 ypos 20
    linear 0.5 alpha 1.0 xpos 100 ypos 0

transform mom_income_left:
    xzoom 1.0
    alpha 0.0
    ypos 0
    xpos -350
    parallel:
        linear 2. xpos 0
    parallel:
        linear .5 alpha .5
        linear .5 alpha 1
    parallel:
        linear .5 ypos 20
        linear .5 ypos 0
        repeat 2

transform mom_reverse_and_out1:
    xpos 1920+100-674 ypos 0 xzoom 1.0
    linear 0.25 alpha 1.00 xpos 1920+140-674 ypos 0
    linear 0.25 alpha 1.00 xpos 1920+210-674 ypos 20
    linear 0.25 alpha 0.75 xpos 1920+280-674 ypos 0
    linear 0.25 alpha 0.50 xpos 1920+350-674 ypos 20
    linear 0.25 alpha 0.00 xpos 1920+450-674 ypos 0

transform mom_reverse_and_out_1eft:
    xpos -1920+600+100 ypos 0 xzoom -1.0
    alpha 1.0
    parallel:
        linear 0.5 xpos -1920+600 +40
        linear 0.5 xpos -1920+600 -20
        linear 0.5 xpos -1920+600 -70
        linear 0.5 xpos -1920+600 -100
    parallel:
        pause 1.
        linear 1.0 alpha 0.
    parallel:
        linear 0.5 ypos 20
        linear 0.5 ypos 0
        repeat 2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
