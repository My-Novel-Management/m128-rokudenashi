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
            masa.come("通路の天井は茶色っぽい煙で覆われ、自分がいる場所が一瞬分からなくなる"),
            dad.be("#瓦礫をどけて脱出口を確保する$S"),
            dad.talk("煙を吸うなよ", "脳の酸素供給が途切れて意識を失うぞ"),
            masa.talk("それくらいの知識はある"),
            masa.do("強気で答えたものの、$dadRoboが持ってきた酸素ボンベがなければ一分と持たなかっただろう",
                "彼の背から伸びたマスクを口にしたまま、何度か苦しそうに呼吸をした", "&"),
            dad.look("$dadRoboはメタリックなボディを剥き出しにしたままだ", "&"),
            masa.look("彼が着ていた防火服とヘルメットは$Sが着込んでいる", "&").omit(),
            masa.think("消火作業用のロボットだから耐火性能は一般の作業ロボよりも気を遣っているが、",
                "それでもフラッシュオーバーが起これば温度はまたたく間に千度を超える",
                "そんな中でまともに稼働し続けられるほどの性能は備えていない"),
            masa.think("この炎の中でどこまで正常に動作するのか", "さながら実証実験の場になってしまった").omit(),
            masa.talk("なあ"),
            dad.do("いつもは無駄に口数の多い$dadRoboが一言も会話なく、",
                "盛り上がった金属の背中を見せつけながら目の前の瓦礫を退けていく"),
            dad.talk("何だ？"),
            masa.talk("いや"),
            masa.think("本物の消防士みたいだと思った、なんてとても口にはできない").omit(),
            masa.think("よちよち歩きだった息子を助ける為に燃え盛るアパートに飛び込んだ結果、自分は一酸化炭素中毒で亡くなった",
                "母からそう告白されたことを思い出したが、頭を揺すって振り払う"),
            dad.talk("一階まで降りられれば脱出口は確保してあるから、安心して付いてこい"),
            masa.talk("心配はしてないさ", "自分で作ったプログラムだ"),
            dad.do("そうだな、と$dadRoboは答え、再び背を向け、先に歩いていく", "&"),
            masa.do("$Sはマスクから酸素を吸い込み、額の汗が次々蒸発するのを気にしつつ、その後に続いた"),
            dad.talk("こいつは駄目だな"),
            dad.do("ドアをこじ開けて覗き込んだエレベータシャフトはそのまま炎の通り道になり、ショートした配線が煙の中で何度も光っている"),
            dad.do("$dadRoboは$masakiの方を一度見ると、煙が上がってくる階段を睨み付ける", "「少し待ってろ」と言い残し、彼は一人先に階下へと降りていった","&"),
            masa.do("三十秒、いや、一分も待ったろうか",
                "呼吸するのすら苦しくなり始めた$Sの前に右の頭部が赤く変色している$dadRoboが現れた"),
            dad.talk("こっちは駄目だ", "一番奥まで進むぞ"),
            masa.talk("大丈夫かよ、そんな姿で"),
            dad.look("見ているうちにも表面のコーティングが破れ、右目のカメラがチカチカと点滅を繰り返している"),
            dad.talk("まだ左目があるさ"),
            masa.do("通路は炎が龍のようにうねりながら$Sたちの頭上を抜けて進む方向へと消えていく"),
            dad.talk("大丈夫だ", "$meを信じろ"),
            dad.do("サムズアップした$dadRoboに同じように親指を立てて返し、その背中に続いた"),
            mam.voice("あれでも消防士として誰かを助けてるときの背中は、本当にかっこよかったのよ"),
            masa.think("今なら母親の言葉が嘘じゃないと信じられる気がした"),
            dad.talk("どうした？"),
            masa.talk("いや", "その、ありが……"),
            masa.do("と、目の前に天井ブロックが落ちてくる"),
            masa.think("――もう駄目だ"),
            masa.do("そう覚悟して身を屈めた$Sの上に、何かが覆いかぶさった", "$dadRoboだ",
                "その背中と右腕で剥離したブロックを防ぎ、潰されないように守ってくれていた",
                "何とか$Sを先に出し、自分も抜け出したが、彼の右腕は大きくひしゃげてしまった"),
            dad.talk("行くぞ"),
            masa.do("それでも構わずに歩き出した父の背に、$Sは黙って続いた"),
            )


def safely_escaped(w: World):
    masa = w.get('masaki')
    dad = w.get('dad')
    megu = w.get('megu')
    man = w.get('man')
    return w.scene("無事脱出したが",
            w.plot_note("建物から何とか脱出した$masakiたちだったが、駆けつけた消防隊員によって救急搬送される",
                "振り返った先に父ロボットの姿はなく、助手の$meguに頼んで意識を失う"),
            w.symbol("　　　　◆"),
            masa.come("#$dadRoboの背中を必死に追いかけ、彼が突き破った壁を抜ける"),
            masa.think("外だ", "やっと死地から抜け出たのだ").omit(),
            man.talk("大丈夫ですか！"),
            masa.do("煙から抜け出し、やっとの思いでコンクリートの地面に両手を突いた$Sに、銀色の消防服を身にまとった隊員が駆け寄る",
                "それに「はい」と答えるのが精一杯で、歪んだ視界には十台以上の消防車と救急車が並び、各員が忙しそうに行き来しているのが映った"),
            masa.do("振り返れば既に建物は全体が炎に包まれ、奥の研究所の棟は三階部分が完全に崩落しているのが分かる",
                "残っていたら完全に助からなかった",
                "その考えに至り、$dadRoboの影を探す",
                "しかしどこにもその姿が見つけられず、$Sの視界は煙に紛れるようにブラックアウトしていった"),
            )
