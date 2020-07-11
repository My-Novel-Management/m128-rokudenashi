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
            w.cmd.change_stage("SickRoom"),
            masa.be("$Sは病院のベッドで目が覚ます"),
            megu.be("傍で見守っていた$Sは目覚めたことに涙を浮かべて安堵している"),
            masa.talk("あいつは？"),
            megu.talk("それが、これを取りに戻って……"),
            megu.do("彼女の手には一升瓶が"),
            masa.talk("記念にって居酒屋から貰ったものじゃないか", "それで本体は？"),
            "ここは抱え落ち。消火した建物から発見された。見つかった父ロボットは焼酎の瓶を抱えて眠るように横たわっていたと",
            megu.explain("その後の状況説明を、$Sから受ける",
                "父ロボットはその記念品を持ち出して地面に置くと、機能停止してしまったという",
                "中のチップは焼け焦げ、とても復元はできなかった",
                "バックアップデータは一月以上も前のままで、それを使ってみたが、何故か同じようには喋ってくれず、ただの他の$AIと同じ結果だったと語った"),
            masa.talk("ほんと、ろくでなしだったよ、あんたは"),
            masa.do("下戸の$Sはコップに酒を注いでもらい、それを一口飲み込んで「ほんとに、ろくでなしで、最高の父親だ」と呟いた"),
            )

