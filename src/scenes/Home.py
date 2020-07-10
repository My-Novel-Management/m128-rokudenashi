# -*- coding: utf-8 -*-
'''
Stage: "主人公の実家"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def memorial(w: World):
    masa = w.get('masaki')
    mam = w.get('mam')
    dad = w.get('dad')
    ancle = w.get('ancle')
    return w.scene('法事の日に',
            w.plot_note("父の命日に珍しく実家に帰省し、そこで全然知らない父の話を聞かされる"),
            "$masakiは熱いものが苦手",
            "そういうところが父に似てる、って話",
            )

