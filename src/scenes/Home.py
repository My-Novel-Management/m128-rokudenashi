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
    ohara = w.get('ohara')
    return w.scene('法事の日に',
            w.plot_note("父の命日に珍しく実家に帰省し、そこで全然知らない父の話を聞かされる"),
            "$masakiは熱いものが苦手",
            "そういうところが父に似てる、って話",
            w.cmd.change_stage("Home"),
            "実家が茨城にあるとか、そういった地方情報を",
            masa.be("法事の席にいた"),
            masa.do("既にお坊さんの経は終わり、宴会になっている"),
            mam.come("新しいビールを運んでくる"),
            mam.talk("$masakiはあんまり飲まないのね", "会社の付き合いとかないの？"),
            masa.talk("そういうのをしなくていいから、今の仕事をしているんだ",
                "それよりあの人だれ？"),
            ohara.be("気難しい顔で座っている"),
            mam.talk("知らなかったっけ？", "あの人の消防士時代の同僚の$oharaさん"),
            masa.think("消防士もやっていたんだと思い出す"),
            masa.talk("でも消防もすぐ首になったんでしょ？"),
            mam.talk("すぐでもないわよ", "勤務態度さえ真面目だったらって、今でも言われるもの"),
            masa.do("少し興味が出て、聞いてみる"),
            masa.talk("あの、すみません"),
            ohara.talk("ああ、息子さん", "もうこんなに大きくなられたんですね"),
            masa.talk("今は人工知能の研究をしています",
                "消防士時代の父って、どんなだったんですか？"),
            ohara.explain("父の消防士時代の活躍の説明を始める"),
            masa.do("あ、少し記録をしてもいいですか？"),
            ohara.talk("え、ええ"),
            )

