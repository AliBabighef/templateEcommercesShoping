from __future__ import unicode_literals
from kivy.factory import Factory
import requests
from kivymd.uix.list import MDList

from kivymd_extensions.akivymd.uix.dialogs import AKAlertDialog


import pause

import random
import kivymd_extensions.akivymd
from kivy.animation import Animation
  
  
from kivymd.uix.button import MDFlatButton
import datetime
from datetime import datetime
from kivymd.theming import ThemableBehavior
import threading
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import IRightBodyTouch
import json
from kivy.clock import Clock, mainthread
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty,StringProperty,ListProperty
import sys
from kivymd.uix.snackbar import Snackbar
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.keyboard_anim_args = {'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"

screen_helper = """
#:import hex kivy.utils.get_color_from_hex
#:import Snackbar kivymd.uix.snackbar.Snackbar
#:import MDFillRoundFlatIconButton kivymd.uix.button.MDFillRoundFlatIconButton
#:import Clipboard kivy.core.clipboard.Clipboard

#:import Window kivy.core.window.Window
#:import IconLeftWidget kivymd.uix.list.IconLeftWidget
#:import NoTransition kivy.uix.screenmanager.NoTransition

<On_active_button@Button_Item>
    icon_color: hex('#010101')
    
    text_color: 1, 1, 1, 1
    button_bg_color: hex('#7a54ff')
    mode: "color_on_active"
    badge_disabled: True

<ErrorDialog@BoxLayout>:
    orientation: "vertical"
    spacing: dp(10)
    padding: dp(20)

    MDLabel:
        text: "Download Failed"
        halign: "center"
        theme_text_color: "Custom"
        text_color: .9, 0, 0, 1

    MDLabel:
        text: "Download Failed. Make sure this are account not private and then try again!"
        halign: "center"
        theme_text_color: "Custom"
        text_color: .9, 0, 0, 1
        font_style: "Caption"

    MDFillRoundFlatButton:
        id: button
        text: "Dismiss"
        md_bg_color: .9, 0, 0, 1
        pos_hint: {"center_x": .5}



        
<SuccessDialog@BoxLayout>:
    orientation: "vertical"
    padding: dp(40)

    MDLabel:
        text: "Download Successful!"
        size_hint_y: None
        height: self.texture_size[1]
        halign: "center"
        valign: "center"
        bold: True
        theme_text_color: "Custom"
        text_color: 0, .7, 0, 1

    MDLabel:
        text: "You will be find your downloads in /Easysta folder"
        halign: "center"
        valign: "top"
        theme_text_color: "Custom"
        text_color: 0, .7, 0, 1
        font_style: "Caption"

    MDFillRoundFlatButton:
        id: button
        text: "Confirm"
        md_bg_color: 0, .7, 0, 1
        pos_hint: {"center_x": .5}



ScreenManager:
    SettingScreen:
        name: 'setting'
        
    ProfileScreen:
        name: 'youtube'
    ProfileInstgram:
        name: 'instagram'
    
<MagicButton@MagicBehavior+MDIconButton>
    bg_color: hex('#E5E5E5')

<MyAKBadgeLayout@AKBadgeLayout>
    pos:root.width-self.width+dp(10),root.height-self.height+dp(70)

    badgeitem_padding: dp(5)
    bold: True
    
<ProgressWidget>
    on_leave:
        progress_relative = 10
        progress_percent = 0



<ProfileScreen>:
    
    Widget:
        canvas:
            Color:
                rgba: hex('#292a4e')
            Rectangle:
                size: self.size
                pos: self.pos
    AKSpinnerFoldingCube:
        id: circleflip
        spinner_size: dp(50)
        pos_hint: {"center_x": .5, "center_y": .5}

    MDFloatLayout:
        id: box1
        md_bg_color: hex('#363867')
        radius: [20, 20, 20, 20]

        size_hint: None, None

        pos_hint: {"center_x": .5}
        pos:0,root.height-self.height-dp(240)
        size:root.width-dp(10),dp(120)
        MDIcon:
            theme_text_color: 'Custom'
            text_color: hex('#7CFC00')
            
            icon: 'av-timer'
            pos:box1.pos[0]+box1.width-self.width+dp(30),box1.pos[1]+box1.height-self.height+dp(20)
        MDIcon:
            theme_text_color: 'Custom'
            text_color: hex('#7CFC00')
            
            icon: 'video-outline'
            pos:box1.pos[0]+box1.width-self.width/2,box1.pos[1]+box1.height-self.height+dp(20)
        MDIconButton:
            theme_text_color: 'Custom'
            text_color: hex('#7CFC00')
            icon: 'lock-outline'
            pos:box1.pos[0]+box1.width-self.width-dp(20),box1.pos[1]+box1.height-self.height-dp(20)

        MDLabel:
            id: sspeed
            markup: True
            theme_text_color: 'Custom'
            text_color: [1,1,1,1]
            text: '00:00'
            font_size: '30sp'
            font_name: 'BebasNeue-Bold.ttf'
            pos:box1.pos[0]+box1.width-self.width+dp(28),box1.pos[1]+box1.height-self.height-dp(20)
        MDLabel:
            id: megaaa
            markup: True
            theme_text_color: 'Custom'
            text_color: [1,1,1,1]
            text: "0.0"
            font_size: '30sp'
            font_name: 'BebasNeue-Bold.ttf'
            pos:box1.pos[0]+box1.width-self.width/2,box1.pos[1]+box1.height-self.height-dp(15)

        MDLabel:
            markup: True
            font_size: '30sp'
            theme_text_color: 'Custom'
            text_color: [1,1,1,1]
            text: 'MB'
            font_name: 'BebasNeue-Regular.ttf'
            pos:box1.pos[0]+box1.width-self.width/2+dp(0),box1.pos[1]+box1.height-self.height-dp(45)
        MDLabel:
            markup: True
            font_size: '30sp'
            theme_text_color: 'Custom'
            text_color: [1,1,1,1]
            text: 'MIN'
            font_name: 'BebasNeue-Regular.ttf'
            pos:box1.pos[0]+box1.width-self.width+dp(30),box1.pos[1]+box1.height-self.height-dp(45)
        
    
    MDFloatLayout:
        id: gg
        size_hint: None, None
        size:(root.width/2)-dp(30),dp(120)
        md_bg_color: hex('#363867')
        radius: [20, 20, 20, 20]
            
        pos:root.width-self.width-dp(10),root.height-self.height-dp(370)
        MDIcon:
            theme_text_color: 'Custom'
            text_color: hex('#7CFC00')
            
            icon: 'speedometer'
            pos:gg.pos[0]+gg.width-self.width/2-dp(10),gg.pos[1]+gg.height-self.height+dp(30)
        MDLabel:
            id: spx
            markup: True
            theme_text_color: 'Custom'
            text_color: [1,1,1,1]
            text: "0.0"
            font_size: '30sp'
            font_name: 'BebasNeue-Bold.ttf'
            pos:gg.pos[0]+gg.width-self.width+dp(20),gg.pos[1]+gg.height-self.height-dp(15)
        
    MDFloatLayout:
        id: bo
        md_bg_color: hex('#363867')
        radius: [10, 10, 10, 10]
        size:root.width-dp(10)/2-dp(20),dp(120)
        size_hint: 0.5, None
        pos:dp(10),root.height-self.height-dp(370)
        MDProgressBar:
            id: azezrze
            orientation: "vertical"
            value: 0
            pos:bo.pos[0]+bo.width-self.width/2-dp(10),bo.pos[1]+bo.height-self.height-dp(10)
            size_hint: .1, None
            type: "determinate"
            running_duration: 1
            catching_duration: 1.5
        MDLabel:
            markup: True
            theme_text_color: 'Custom'
            text_color: [1,1,1,1]
            text: "Speed Net"
            font_size: '30sp'
            font_name: 'BebasNeue-Bold.ttf'
            pos:bo.pos[0]+bo.width-self.width,bo.pos[1]+bo.height-self.height-dp(40)
        MDIcon:
        
            theme_text_color: 'Custom'
            text_color: [1,1,1,1]
            icon: 'flash-circle'
            font_size: '30sp'
            pos:bo.pos[0]+bo.width-self.width+dp(5),bo.pos[1]+bo.height-self.height+dp(40)
        
        
    AKSpinnerFoldingCube:
        id: circleflip
        spinner_size: dp(50)
        pos_hint: {"center_x": .5, "center_y": .5}



        
    MDLabel:
        markup: True
        theme_text_color: 'Custom'
        text_color: [1,1,1,1]
        text: 'Dashbord'
        font_name: 'BebasNeue-Bold.ttf'
        size_hint_y: None
        height:self.texture_size[1]
        bold: 'True'
        font_size: sp(18)
        pos:dp(20),root.height-self.height-dp(210)
     
    MDLabel:
        markup: True
        theme_text_color: 'Custom'
        text_color: [1,1,1,1]
        text: 'Options'
        font_name: 'BebasNeue-Bold.ttf'
        size_hint_y: None
        height:self.texture_size[1]
        bold: 'True'
        font_size: sp(18)
        pos:dp(20),root.height-self.height-dp(100)
     
    MDIconButton:
        icon: 'settings-outline'
        theme_text_color: 'Custom'
        text_color: [1,1,1,1]
        pos:root.width-self.width-dp(10),root.height-self.height-dp(30)
        
    MDIconButton:
       
        theme_text_color: 'Custom'
        text_color: [1,1,1,1]
        icon: 'arrow-left-bold-hexagon-outline'
        pos:dp(10),root.height-self.height-dp(30)
        on_press: root.manager.current = "setting"
        
    MDBoxLayout:
        orientation: "vertical"
        spacing: dp(40)

        MDBoxLayout:
            orientation: "vertical"

        AKBottomNavigation2:
            bg_color: hex('#E5E5E5')

            On_active_button:
                text: "Home"
                icon: "home-outline"

            
    MDIconButton:
        pos:root.width-self.width/2-dp(30),root.height-self.height-dp(140)
        md_bg_color: hex('#FFFFFF')
        user_font_size: '12sp'
        icon: 'content-paste'
        bg_color: hex('#E5E5E5')
        on_release:
            youtu.text = Clipboard.paste()
        

    MDFloatLayout:
        id: qq
        md_bg_color: hex('#363867')
        radius: [20, 20, 20, 20]

        size_hint: None, None

        pos_hint: {"center_x": .45}
        pos:0,root.height-self.height-dp(130)
        size:root.width-dp(90),dp(60)   
        MDTextField:
            id: youtu
            hint_text: "Enter the Url"
            
            icon_right: "web"
            icon_right_color: app.theme_cls.primary_color      
            helper_text_mode: "on_error"
            helper_text: "Enter text"
            pos:qq.pos[0]+qq.width-self.width,qq.pos[1]+qq.height-self.height-dp(10)

            
        
     
    
    MDFloatingActionButtonSpeedDial:
        
        data: app.dataa
        root_button_anim: True
        callback: app.playnow
        x: root.width

    
<ProfileInstgram>:
    Widget:
        canvas:
            Color:
                rgba: hex('#292a4e')
            Rectangle:
                size: self.size
                pos: self.pos
                
            
    MDFloatLayout:
        id: box1
        md_bg_color: hex('#363867')
        radius: [20, 20, 20, 20]

        size_hint: None, None

        pos_hint: {"center_x": .5}
        pos:0,root.height-self.height-dp(240)
        size:root.width-dp(10),dp(120)
        MDIcon:
            theme_text_color: 'Custom'
            text_color: hex('#7CFC00')
            
            icon: 'speedometer'
            pos:box1.pos[0]+box1.width-self.width+dp(30),box1.pos[1]+box1.height-self.height+dp(20)
        MDIcon:
            theme_text_color: 'Custom'
            text_color: hex('#7CFC00')
            
            icon: 'video-outline'
            pos:box1.pos[0]+box1.width-self.width/2,box1.pos[1]+box1.height-self.height+dp(20)
        MDIconButton:
            theme_text_color: 'Custom'
            text_color: hex('#7CFC00')
            icon: 'lock-outline'
            pos:box1.pos[0]+box1.width-self.width-dp(20),box1.pos[1]+box1.height-self.height-dp(20)

        MDLabel:
            id: speed
            markup: True
            theme_text_color: 'Custom'
            text_color: [1,1,1,1]
            text: '0.0'
            font_size: '30sp'
            font_name: 'BebasNeue-Bold.ttf'
            pos:box1.pos[0]+box1.width-self.width+dp(28),box1.pos[1]+box1.height-self.height-dp(20)
        MDLabel:
            id: mega
            markup: True
            theme_text_color: 'Custom'
            text_color: [1,1,1,1]
            text: "0.0"
            font_size: '30sp'
            font_name: 'BebasNeue-Bold.ttf'
            pos:box1.pos[0]+box1.width-self.width/2-dp(4),box1.pos[1]+box1.height-self.height-dp(15)

        MDLabel:
            markup: True
            theme_text_color: 'Custom'
            text_color: [1,1,1,1]
            text: '[size=35]MB[/size]'
            font_name: 'BebasNeue-Regular.ttf'
            pos:box1.pos[0]+box1.width-self.width/2+dp(1),box1.pos[1]+box1.height-self.height-dp(45)
        MDLabel:
            markup: True
            theme_text_color: 'Custom'
            text_color: [1,1,1,1]
            text: '[size=35]Kb/s[/size]'
            font_name: 'BebasNeue-Regular.ttf'
            pos:box1.pos[0]+box1.width-self.width+dp(28),box1.pos[1]+box1.height-self.height-dp(45)


    
    MDFloatLayout:
        size_hint: None, None
        size:(root.width/2)-dp(30),dp(120)
        md_bg_color: hex('#363867')
        radius: [20, 20, 20, 20]
            
        pos:root.width-self.width-dp(10),root.height-self.height-dp(370)
        
    MDFloatLayout:
        id: bo
        md_bg_color: hex('#363867')
        radius: [10, 10, 10, 10]
        size:root.width-dp(10)/2-dp(20),dp(120)
        size_hint: 0.5, None
        pos:dp(10),root.height-self.height-dp(370)


        
    AKSpinnerFoldingCube:
        id: circleflip
        spinner_size: dp(50)
        pos_hint: {"center_x": .5, "center_y": .5}



        
    MDLabel:
        markup: True
        theme_text_color: 'Custom'
        text_color: [1,1,1,1]
        text: 'Dashbord'
        font_name: 'BebasNeue-Bold.ttf'
        size_hint_y: None
        height:self.texture_size[1]
        bold: 'True'
        font_size: sp(18)
        pos:dp(20),root.height-self.height-dp(210)
     
    MDLabel:
        markup: True
        theme_text_color: 'Custom'
        text_color: [1,1,1,1]
        text: 'Options'
        font_name: 'BebasNeue-Bold.ttf'
        size_hint_y: None
        height:self.texture_size[1]
        bold: 'True'
        font_size: sp(18)
        pos:dp(20),root.height-self.height-dp(100)
     
    MDIconButton:
        icon: 'settings-outline'
        theme_text_color: 'Custom'
        text_color: [1,1,1,1]
        pos:root.width-self.width-dp(10),root.height-self.height-dp(30)
        
    MDIconButton:
       
        theme_text_color: 'Custom'
        text_color: [1,1,1,1]
        icon: 'arrow-left-bold-hexagon-outline'
        pos:dp(10),root.height-self.height-dp(30)
        on_press: root.manager.current = "setting"
        
    MDBoxLayout:
        orientation: "vertical"
        spacing: dp(40)

        MDBoxLayout:
            orientation: "vertical"

        AKBottomNavigation2:
            bg_color: hex('#E5E5E5')

            On_active_button:
                text: "Home"
                icon: "home-outline"

            
    MDIconButton:
        pos:root.width-self.width/2-dp(30),root.height-self.height-dp(140)
        md_bg_color: hex('#FFFFFF')
        user_font_size: '12sp'
        icon: 'content-paste'
        bg_color: hex('#E5E5E5')
        on_release:
            putinstgram.text = Clipboard.paste()
        

    MDFloatLayout:
        id: qq
        md_bg_color: hex('#363867')
        radius: [20, 20, 20, 20]

        size_hint: None, None

        pos_hint: {"center_x": .45}
        pos:0,root.height-self.height-dp(130)
        size:root.width-dp(90),dp(60)   
        MDTextField:
            id: putinstgram
            hint_text: "Enter the Url"
            
            icon_right: "web"
            icon_right_color: app.theme_cls.primary_color      
            helper_text_mode: "on_error"
            helper_text: "Enter text"
            pos:qq.pos[0]+qq.width-self.width,qq.pos[1]+qq.height-self.height-dp(10)

            
        
     
    
    MDFloatingActionButtonSpeedDial:
        
        data: app.datahash
        root_button_anim: True
        callback: app.playnowhash
        x: root.width


                
<SettingScreen>:
    Widget:
        canvas:
            Color:
                rgba: hex('#292a4e')
            Rectangle:
                size: self.size
                pos: self.pos
                
    AKBottomNavigation2:
        bg_color: hex('#E5E5E5')

        On_active_button:
            text: "Home"
            icon: "home-outline"
        On_active_button:
            text: "Shop"
            icon: "shopping"

            
    MDLabel:
        markup: True
        theme_text_color: 'Custom'
        text_color: hex('#FFFFFF')
        text: 'Home'
        font_name: 'BebasNeue-Bold.ttf'
        size_hint_y: None
        height:self.texture_size[1]
        bold: 'True'
        font_size: sp(18)
        pos:dp(20),root.height-self.height-dp(50)
        
    
    MDIconButton:
        icon: 'settings-outline'
        theme_text_color: 'Custom'
        text_color: hex('#FFFFFF')
        pos:root.width-self.width-dp(10),root.height-self.height-dp(30)
         

    ScrollView:
        do_scroll_x: False
        do_scroll_y: True
        size_hint: None, None


        pos_hint: {"center_x": .5}
        pos:0,root.height-self.height-dp(70)
        size:root.width-dp(10),dp(460)  
        DrawerList:
            id: md_list
            
            MDList:                 
                
                
                MDFloatLayout:
                   
                 
                    radius: [20, 20, 20, 20]

                    size_hint: None, None

                    pos_hint: {"center_x": .5}
                    pos:0,root.height-self.height-dp(420)
                    size:root.width-dp(10),dp(10)
                MDCard:
                    id: boxa
                    
                    ripple_behavior: True
                    
                    md_bg_color: hex('#E1306C')
                    radius: [20, 20, 20, 20]

                    size_hint: None, None

                    pos_hint: {"center_x": .5}
                    pos:0,root.height-self.height-dp(420)
                    size:root.width-dp(10),dp(100)
                    on_press: root.manager.current = 'instagram'
           
                    MDIconButton:
                        id: livefollow
                        user_font_size: '25sp'
                        
                        icon: 'instagram'
                        pos:boxa.pos[0]+boxa.width-self.width-dp(10),boxa.pos[1]+boxa.height-self.height-dp(10)
                        theme_text_color: 'Custom'
                        text_color: hex('#FFFFFF')
                                    
                    MDIconButton:
                        id: icon
                        theme_text_color: 'Custom'
                        text_color: 1, 1, 1 ,1
                        icon: "arrow-right-bold-hexagon-outline"
                        font_size: "30sp"
                        opposite_colors: True
                     
                        on_press: root.manager.current = 'instagram'
                        pos_hint: {"center_y": .5}

                    MDLabel:
                        text: "Instagram Download Online"
                        font_name: 'BebasNeue-Bold.ttf'
                        size_hint_y: None
                        theme_text_color: 'Custom'
                        text_color: 1, 1, 1 ,1
                        height: self.texture_size[1]
                        pos_hint: {"center_y": .5}
                     
                        opposite_colors: True
                        

                MDFloatLayout:
                   
                 
                    radius: [20, 20, 20, 20]

                    size_hint: None, None

                    pos_hint: {"center_x": .5}
                    pos:0,root.height-self.height-dp(420)
                    size:root.width-dp(10),dp(10)

                MDCard:
                    id: box
                    
                    md_bg_color: hex('#FF0000')
                    radius: [20, 20, 20, 20]
                    on_press: root.manager.current = 'youtube'
                    size_hint: None, None

                    pos_hint: {"center_x": .5}
                    pos:0,root.height-self.height-dp(420)
                    size:root.width-dp(10),dp(100)
                    
           
                    
                    MDIconButton:
                        id: livefollow
                        
                        icon: 'youtube'
                        pos:box.pos[0]+box.width-self.width-dp(10),box.pos[1]+box.height-self.height-dp(10)
                        theme_text_color: 'Custom'
                        on_press: root.manager.current = 'youtube'
                        text_color: hex('#FFFFFF')
                        
                    MDIconButton:
                        id: icon
                        theme_text_color: 'Custom'
                        text_color: 1, 1, 1 ,1
                        icon: "arrow-right-bold-hexagon-outline"
                        font_size: "30sp"
                        opposite_colors: True
                        pos_hint: {"center_y": .5}
                        pos:box.pos[0]+box.width-self.width/2,box.pos[1]+box.height-self.height
                    MDLabel:
                        text: "Youtube Download Online"
                        font_name: 'BebasNeue-Bold.ttf'
                        size_hint_y: None
                        theme_text_color: 'Custom'
                        text_color: 1, 1, 1 ,1
                        height: self.texture_size[1]
                        pos_hint: {"center_y": .5}
                     
                        opposite_colors: True

                MDFloatLayout:
                   
                 
                    radius: [20, 20, 20, 20]

                    size_hint: None, None

                    pos_hint: {"center_x": .5}
                    pos:0,root.height-self.height-dp(420)
                    size:root.width-dp(10),dp(10)

                MDCard:
                    id: rtt
                    
                    md_bg_color: hex('#4267B2')
                    radius: [20, 20, 20, 20]

                    size_hint: None, None

                    pos_hint: {"center_x": .5}
                    pos:0,root.height-self.height-dp(420)
                    size:root.width-dp(10),dp(100)
                    
           
                    MDIconButton:
                        id: livefollow
                        
                        icon: 'facebook'
                        pos:rtt.pos[0]+rtt.width-self.width-dp(10),rtt.pos[1]+rtt.height-self.height-dp(10)
                        theme_text_color: 'Custom'
                        text_color: hex('#FFFFFF')
                
                        
                    MDIconButton:
                        id: icon
                        theme_text_color: 'Custom'
                        text_color: 1, 1, 1 ,1
                        icon: "arrow-right-bold-hexagon-outline"
                        font_size: "30sp"
                        opposite_colors: True
                        pos_hint: {"center_y": .5}
                        pos:rtt.pos[0]+rtt.width-self.width/2,rtt.pos[1]+rtt.height-self.height
                    MDLabel:
                        text: "Facebook Download Online"
                        font_name: 'BebasNeue-Bold.ttf'
                        size_hint_y: None
                        theme_text_color: 'Custom'
                        text_color: 1, 1, 1 ,1
                        height: self.texture_size[1]
                        pos_hint: {"center_y": .5}
                     
                        opposite_colors: True
                MDFloatLayout:
                    id: box2
                 
                    radius: [20, 20, 20, 20]

                    size_hint: None, None

                    pos_hint: {"center_x": .5}
                    pos:0,root.height-self.height-dp(420)
                    size:root.width-dp(10),dp(10)

                MDCard:
                    id: rtts
                    
                    md_bg_color: hex('#010101')
                    radius: [20, 20, 20, 20]

                    size_hint: None, None

                    pos_hint: {"center_x": .5}
                    pos:0,root.height-self.height-dp(420)
                    size:root.width-dp(10),dp(100)
                    
           
                    
                    MDIconButton:
                        id: icon
                        theme_text_color: 'Custom'
                        text_color: 1, 1, 1 ,1
                        icon: "arrow-right-bold-hexagon-outline"
                        user_font_size: "20sp"
                        opposite_colors: True
                        pos_hint: {"center_y": .5}
                        
                    MDLabel:
                        text: "Tiktok Download Online"
                        font_name: 'BebasNeue-Bold.ttf'
                        size_hint_y: None
                        theme_text_color: 'Custom'
                        text_color: 1, 1, 1 ,1
                        height: self.texture_size[1]
                        pos_hint: {"center_y": .5}
                     
                        opposite_colors: True
    


<ProfileScreen>:

















"""

Window.keyboard_anim_args = {'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"

#############################################
class ProfileScreen(Screen):
    pass
class SettingScreen(Screen):
    pass
class ProfileInstgram(Screen):
    pass

class DrawerList(ThemableBehavior, MDList):
        pass
##############################################
class DemoApp(MDApp):
    datahash = {'download': 'download'}
    dataa =  {'download': 'download'}

    def playnow(self, instance, *largs):
        if instance.icon == 'download':
            print (instance.icon)
            self.thread2()

    
    def thread2(self):
        import os
        try:  
            os.mkdir('/sdcard/easysta')
            os.mkdir('/sdcard/easysta/video')
            os.mkdir('/sdcard/easysta/images')  
        except:
            pass
            

            
        t = threading.Thread(target=self.youtube)
        t.start()
    def my_hook(self, d):
            dd = random.randint(0, 100)
            self.root.get_screen('youtube').ids.azezrze.value = int(dd)

            self.root.get_screen('youtube').ids.circleflip.active = True
            
        
            u = ", '_total_bytes_str': '"
            r = "'}"
            qqqx = 'MiB'
            qs = str(d)
            print (qs)
           
            dd = qs.partition(u)[2]
            op = dd.partition(r)[0]
            sx = op.partition(qqqx)[0]
            ##############
            u1 = ", '_speed_str': '"
            u2 = "B/s'"
            dd1 = qs.partition(u1)[2]
            op2 = dd1.partition(u2)[0]
            #########################
            u3 = ", '_eta_str': '"
            u4 = "'"
            dd2 = qs.partition(u3)[2]
            op3 = dd2.partition(u4)[0]
            
            self.root.get_screen('youtube').ids.spx.text = str(op2)
            self.root.get_screen('youtube').ids.megaaa.text = str(sx)
            self.root.get_screen('youtube').ids.sspeed.text = str(op3)
        
 
            if d['status'] == 'finished':
                print('ok')

    #################################################
    def youtube(self):
        import youtube_dl
        ecn = self.root.get_screen('youtube').ids.youtu.text
        
        ydl_opts = {
            'outtmpl': '/sdcard/video/'+'%(id)s'+".mp4",        
            'noplaylist' : True,        
            'progress_hooks': [self.my_hook],  
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([ecn])
        self.root.get_screen('youtube').ids.circleflip.active = False
        self.success()

    #################################################"

    def playnowhash(self, instance, *largs):
        if instance.icon == 'download':
            print (instance.icon)
            self.thread1()

    

    def success(self):
        dialog = AKAlertDialog(
            header_icon="check-circle-outline", header_bg=[0, 0.7, 0, 1]
        )
        content = Factory.SuccessDialog()
        content.ids.button.bind(on_release=dialog.dismiss)
        dialog.content_cls = content
        dialog.open()
        
    def error(self):
        dialog = AKAlertDialog(
            header_icon="close-circle-outline", header_bg=[0.9, 0, 0, 1]
        )
        content = Factory.ErrorDialog()
        content.ids.button.bind(on_release=dialog.dismiss)
        dialog.content_cls = content
        dialog.open()
        
    def thread1(self):
        import os
        try:  
            os.mkdir('/sdcard/easysta')
            os.mkdir('/sdcard/easysta/video')
            os.mkdir('/sdcard/easysta/images')  
        except:
            pass
            

            
        t = threading.Thread(target=self.start_instagram)
        t.start()
        
    def check_private(self):
        from kivy.animation import Animation
        from kivymd.uix.snackbar import Snackbar

        url = self.root.get_screen('instagram').ids.putinstgram.text

        login_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
        }
        f = '?'
        try:
            bb = url.partition(f)[0]
            urlg = (bb+"?__a=1")

            resp = requests.get(urlg, headers=login_headers)
        except:
            resp = requests.get(url, headers=login_headers)

        data = json.loads(resp.text)
        try:
            
           end_cursor = data['graphql']['shortcode_media']['owner']['is_private']
        except:
            self.error()
            sys.exit()
        
            
            
    def warning(self):
        dialog = AKAlertDialog(
            header_icon="exclamation",
            header_bg=[1, 0.75, 0, 1],
            progress_interval=3,
        )
        dialog.bind(on_progress_finish=dialog.dismiss)
        content = Factory.WarningDialog()
        content.ids.submit.bind(on_release=dialog.dismiss)
        content.bind(on_release=dialog.dismiss)
        dialog.content_cls = content
        dialog.open()
    def start_instagram(self):
            from hurry.filesize import size
            try:
                requests.get('https://google.com')
            
                sxs1 = random.randrange(100,900)
            except:
                sxs1 = '0'
                pass
            
            
            self.root.get_screen('instagram').ids.speed.text = str(sxs1)

            self.check_private()
            f = '?'
            login_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
            }
            url = self.root.get_screen('instagram').ids.putinstgram.text
            sfn = str(url)
            
            if 'reel' in sfn:
                self.root.get_screen('instagram').ids.circleflip.active = True
                bb = sfn.partition(f)[0]
                urlg = (bb+"?__a=1")
                reell = requests.get(urlg, headers=login_headers)
                data = json.loads(reell.text)
                end_cursors = data['graphql']['shortcode_media']['video_url']
                ids = data['graphql']['shortcode_media']['id']
                respimage = requests.get(end_cursors, headers=login_headers)
                ee= respimage.content

                qqx = (len(ee))
                sqdcq = "M"
                    
                    
                qqq = size(qqx)
                sxs = qqq.partition(sqdcq)[0]
                print (sxs)
                self.root.get_screen('instagram').ids.mega.text = (sxs)
                #'/sdcard/easysta/video/'+
                ioima = open('/sdcard/easysta/video/'+ids+'.mp4', 'wb')
                ioima.write(ee)
                ioima.close()
                self.success()
                self.root.get_screen('instagram').ids.circleflip.active = False

                
            else:

                s = requests.session()
                try:
                  bb = url.partition(f)[0]
                  urlg = (bb+"?__a=1")

                  resp = requests.get(urlg, headers=login_headers)
                except:
                    resp = requests.get(url, headers=login_headers)
                    
                data = json.loads(resp.text)
                end_cursor = data['graphql']['shortcode_media']['is_video']
                
                try:
                   down = data['graphql']['shortcode_media']['video_url']
                except:
                    pass
                con = str(end_cursor)
                if con == 'False':
                    downs = data['graphql']['shortcode_media']['display_url']
                    ids = data['graphql']['shortcode_media']['id']

                    respimage = requests.get(downs, headers=login_headers)
                    ee= respimage.content
                    
                    ioima = open('/sdcard/easysta/images/'+ids+'.jpg', 'wb')
                    ioima.write(ee)
                    ioima.close()
                    self.success()
                    self.root.get_screen('instagram').ids.circleflip.active = False

                
                else:
                    ids = data['graphql']['shortcode_media']['id']
                    io = open('/sdcard/easysta/video/'+ids+'.mp4', 'wb')

                    self.root.get_screen('instagram').ids.circleflip.active = True

                    re = requests.get(down, headers=login_headers)
                    download = re.content
                    
                    qqx = (len(download))
                    sqdcq = "M"
                    
                    
                    qqq = size(qqx)
                    sxs = qqq.partition(sqdcq)[0]
                    print (sxs)
                    self.root.get_screen('instagram').ids.mega.text = (sxs)
                    io.write(download)
                    io.close()
                    self.success()
                    self.root.get_screen('instagram').ids.circleflip.active = False

           
    def build(self):
            sm = ScreenManager()
            sm.add_widget(ProfileScreen(name='profile'))
            sm.add_widget(SettingScreen(name='setting'))
            sm.add_widget(ProfileInstgram(name='instagram'))
            
            screen = Builder.load_string(screen_helper)
            self.theme_cls.theme_style = "Light"
            return screen

DemoApp().run()










