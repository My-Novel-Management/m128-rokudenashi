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
    mam = w.get('mam')
    return w.scene('脱出',
            w.plot_note("父ロボは拒否する$masakiに持ち込んだ防火服を着せ、自分は消防士時代の経験を活かして消化器や消化技術で脱出道を作り、彼を外へと導いていく"),
            w.plot_note("その背中を見ながら、$masakiは初めて母が言った「でもね、あの人かっこいいところもあるのよ」が理解できた"),
            w.cmd.change_stage("Company"),
            masa.come("煙が充満する中、屈みながら通路を進む"),
            masa.look("$Sだけ防火服を着せられている"),
            dad.be("瓦礫をどけて脱出口を確保する$S"),
            dad.look("既にお飾りの上着は破けたり、燃えたりして、なくなっている"),
            dad.do("その逞しい背中を見せながら、$Sは黙々と先を調べ、安全を確保してから$masakiに声を掛ける"),
            masa.do("$Sはただ彼に従うだけ"),
            masa.think("あとについていきながらも、その背中に母親から聞いた父の唯一かっこいい部分を感じていた"),
            mam.voice("あれでも消防士として誰かを助けてるときの背中は、本当にかっこよかったのよ"),
            dad.talk("どうした？"),
            masa.talk("いや", "その、ありが……"),
            masa.do("目の前の天井が落ちてくる"),
            dad.do("身を挺して$masakiを守る"),
            dad.look("背中で支え、一部、右腕がひしゃげている"),
            dad.do("それでも構わず「先に行くぞ」と進む$S"),
            masa.do("黙ってついていく$S"),
            )


def safely_escaped(w: World):
    masa = w.get('masaki')
    dad = w.get('dad')
    megu = w.get('megu')
    return w.scene("無事脱出したが",
            w.plot_note("建物から何とか脱出した$masakiたちだったが、駆けつけた消防隊員によって救急搬送される",
                "振り返った先に父ロボットの姿はなく、助手の$meguに頼んで意識を失う"),
            masa.come("父ロボットに連れ出され、建物の外へと出てくる$S"),
            masa.do("既に建物は全体が炎に包まれ、研究所のある方は屋根が落ちていた",
                "現場には救急車と消防車が次々と入ってきて、父ロボットにより助け出された人たちが運ばれていく"),
            masa.do("父ロボットにありがとうを言おうとして振り返ると、何故か彼が建物へと戻っていく背中が見えた"),
            masa.do("そこで意識が途切れた"),
            )
