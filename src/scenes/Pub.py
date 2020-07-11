# -*- coding: utf-8 -*-
'''
Stage: "父がよく通った飲み屋"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def old_talk(w: World):
    masa = w.get('masaki')
    taichi = w.get('taichi')
    miho = w.get('miho')
    return w.scene('父についての昔話',
            w.plot_note("$masakiには父の記憶がなかった",
                "まだ乳飲み子の頃に火事で亡くなったとだけ聞いている",
                "その父が元消防士だったと聞き、そのデータを集めれば上司の言っている条件を満たす$w_AIモデルができるのではないかと考える"),
            w.cmd.change_stage("Pub"),
            )

