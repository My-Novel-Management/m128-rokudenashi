# -*- coding: utf-8 -*-
'''
Stage: "病室"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def awake_and_report(w: World):
    masa = w.get('masaki')
    megu = w.get('megu')
    return w.scene('目覚めと報告',
            w.plot_note("病院のベッドで目覚めた$masakiは$meguから父ロボットどこにも見つからなかったことを聞いて「いくらかかったと思ってるんだよ。ほんと、最後までロクデナシだった」と愚痴りながら笑った"),
            "実は父の死因は息子を助けた際の一酸化炭素中毒だった、と実は母のインタビューで知っていた、というのを父ロボとの会話で発言して「あんたまた死ぬ気か？」とやる",
            "でも父ロボットは「俺はロボだからな。死ぬとかねえだろ？」と",
            )

