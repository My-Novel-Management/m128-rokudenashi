# -*- coding: utf-8 -*-
'''
Stage: "会社の食堂"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def major_topic(w: World):
    masa = w.get('masaki')
    iwata = w.get('iwata')
    return w.scene('社内で話題に',
            w.plot_note("会社として初めての救助$w_AI搭載ロボットを開発したことが話題になっていた"),
            )

