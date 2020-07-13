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
            masa.think("$Sの思惑とは違い、何故か$dadAIは今までの$AIが突破できなかった問題を次々とこなしていった"),
            ) # NOTE: omit

def decided_presentation(w: World):
    masa = w.get('masaki')
    megu = w.get('megu')
    iwata = w.get('iwata')
    return w.scene("発表会の決定",
            w.plot_note("そんな中、大々的に一般向けの記者会見を行うことが決まり、$masakiは父$w_AIに頼み込んで、何とか問題を起こさないようにと注意する"),
            w.cmd.change_stage("Cafeteria"),
            w.symbol("　　　　◆"),
            masa.be("#ぶすっとした顔で食べている"),
            masa.do("初夏の陽気に「外で冷やしラーメンでも食べに行くか」という若い社員の集団の声を他所に、",
                "$Sは珍しく社員食堂に入ってカレーライスを手にしていた",
                "気分を害すると辛いものが食べたくなるのが小さい頃からの癖で、",
                "色々と仕事が行き詰まっている時にはカレーと麻婆豆腐定食を日替わりで注文することになる"),
            iwata.come("#隣にやってきて、握手を求める"),
            iwata.talk("珍しいな、社食にいるなんて"),
            masa.do("そうですか、と隣に座った男にむすっとした返答を投げつけ、$Sはスプーンの上の黄金色のとろみを口へと運ぶ", "&"),
            iwata.do("カールした前髪を指先でくるりと弄びながら上司の$Sは「$meもカレーにしとけば良かったかな」と自分の焼き魚定食を見ているが、",
                "表情がきりっと変化し、その右手を$masakiへと差し出した"),
            masa.talk("何ですか？"),
            iwata.talk("おめでとう", "決まったよ",
                "今月末に業者向け記者会見を行う", "その席で君の$full_dadRobo『$dadRobo』がお披露目になる"),
            )



