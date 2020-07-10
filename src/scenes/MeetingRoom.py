# -*- coding: utf-8 -*-
'''
Stage: "会社の会議室"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def meeting(w: World):
    masa = w.get('masaki')
    iwata = w.get('iwata')
    return w.scene('大事な会議',
            w.plot_note("既にいくつかの競合他社が同じような災害救助ロボットを出していたが、どの$w_AIも柔軟に対応するには不十分で、まだまだ人間の補助的存在でしかなかった"),
            "ここで$masakiの正装が白衣であることを示す、か、逆に汚れてて注意される",
            )

