# -*- coding: utf-8 -*-
'''
Stage: "主人公の勤める研究所のある会社"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def escaping(w: World):
    masa = w.get('masaki')
    dad = w.get('dad')
    return w.scene('脱出',
            w.plot_note("父ロボは拒否する$masakiに持ち込んだ防火服を着せ、自分は消防士時代の経験を活かして消化器や消化技術で脱出道を作り、彼を外へと導いていく"),
            w.plot_note("その背中を見ながら、$masakiは初めて母が言った「でもね、あの人かっこいいところもあるのよ」が理解できた"),
            )


def safely_escaped(w: World):
    masa = w.get('masaki')
    dad = w.get('dad')
    megu = w.get('megu')
    return w.scene("無事脱出したが",
            w.plot_note("建物から何とか脱出した$masakiたちだったが、駆けつけた消防隊員によって救急搬送される",
                "振り返った先に父ロボットの姿はなく、助手の$meguに頼んで意識を失う"),
            )
