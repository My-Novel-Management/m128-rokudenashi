# -*- coding: utf-8 -*-
'''
Stage: "試験場"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def powerful_robo(w: World):
    masa = w.get('masaki')
    megu = w.get('megu')
    dad = w.get('dad')
    iwata = w.get('iwata')
    man = w.get('man')# 取引先
    return w.scene('素晴らしい性能',
            w.plot_note("しかし父$w_AIを搭載した救助ロボットは火災現場で、本物の消防士顔負けの働きを見せ、見学に訪れた専門家たちを驚かせていた"),
            )


def back_face(w: World):
    masa = w.get('masaki')
    megu = w.get('megu')
    dad = w.get('dad')
    return w.scene("父ロボットの裏の姿",
            w.plot_note("だがその裏では父$w_AIは酒もタバコも女も何の楽しみもないロボットのことを愚痴り、会話学習の時間もサボりまくる",
                "自分のバッテリィを貰うためだけに仕方なく実験に参加することはあっても、必要以外はどこかに姿を消してしまうことも度々だった"),
            )
