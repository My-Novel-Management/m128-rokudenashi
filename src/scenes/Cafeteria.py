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
            w.cmd.change_stage("Cafeteria"),
            masa.be("珍しく食堂で昼食を取っていた"),
            iwata.come("隣にやってくる$S"),
            iwata.talk("なんかえらく評判らしいじゃないか、$dadAI", "来週には遂にロボットに載せてテストするんだろ？"),
            masa.talk("ええ、そうみたいですね"),
            iwata.talk("なんだよその他人事みたいな面は",
                "これが成功したら$meもお前も出世間違いなしだ", "研究資金だってもりもり出してくれるようになるんだぞ？"),
            masa.talk("それは嬉しいですけど"),
            masa.think("$Sの思惑とは違い、何故か$dadAIは今までの$AIが突破できなかった問題を次々とこなしていった",
                ""),
            )

def decided_presentation(w: World):
    masa = w.get('masaki')
    megu = w.get('megu')
    iwata = w.get('iwata')
    return w.scene("発表会の決定",
            w.plot_note("そんな中、大々的に一般向けの記者会見を行うことが決まり、$masakiは父$w_AIに頼み込んで、何とか問題を起こさないようにと注意する"),
            w.cmd.change_stage("Cafeteria"),
            masa.be("ぶすっとした顔で食べている"),
            iwata.come("隣にやってきて、握手を求める"),
            iwata.talk("おめでとう", "決まったよ", "今月末に業者向け記者会見を行う", "その席で$dadRoboがお披露目になる"),
            )



