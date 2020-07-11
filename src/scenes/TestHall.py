# -*- coding: utf-8 -*-
'''
Stage: "試験場"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def powerful_robo(w: World):
    masa = w.get('masaki')
    megu = w.get('megu')
    dad = w.get('dad')
    iwata = w.get('iwata')
    man = w.get('man')# 取引先
    return w.scene('素晴らしい性能',
            w.plot_note("しかし父$w_AIを搭載した救助ロボットは火災現場で、本物の消防士顔負けの働きを見せ、見学に訪れた専門家たちを驚かせていた"),
            w.cmd.change_stage("TestHall"),
            masa.be("$dadRoboを実験場に連れ出して、そこで試験をしていた"),
            dad.be("真面目に災害救助を実演している金属性の人間"),
            dad.look("簡易の防火服と防火ヘルメットを被っている"),
            dad.do("本物の消防士さながらの動きで次々と消化銃の消火剤を次々と火元に見立てた発煙筒にぶつけていく"),
            man.be("見学に訪れている役員たち"),
            man.talk("これはすごいじゃないか", "すぐにでも実用化できるんじゃないか？"),
            iwata.be(),
            iwata.talk("まだ人間の消防士との共同作業など、課題は多いですが、早ければ二年以内に実戦投入できると踏んでおります"),
            masa.do("その様子を見ながらも、内心はあまりよくない"),
            )


def back_face(w: World):
    masa = w.get('masaki')
    megu = w.get('megu')
    dad = w.get('dad')
    return w.scene("父ロボットの裏の姿",
            w.plot_note("だがその裏では父$w_AIは酒もタバコも女も何の楽しみもないロボットのことを愚痴り、会話学習の時間もサボりまくる",
                "自分のバッテリィを貰うためだけに仕方なく実験に参加することはあっても、必要以外はどこかに姿を消してしまうことも度々だった"),
            masa.come("控室に入ってくる$S"),
            dad.be("椅子に座り、$n_meguを相手にくだをまいている$dadRobo"),
            dad.talk("なあ$k_meguよ", "$meは人間じゃないんだから、どうしてこう何度も何度も同じことをやらされなきゃならねえんだ？",
                "そんなのプログラムでちょちょいと修正してくれりゃいいじゃねえか"),
            masa.talk("学習してプログラムを修正するようになっているのが$AIなんだ",
                "人間みたいなことを言わないでくれないか",
                "面倒だとか、やりたくないとか",
                "そもそも$meはあんたそっくりの$AIを作りたかった訳じゃない",
                "人間の代わりに困難な場所でも活動可能な代替ロボットの頭脳が作りたかったんだ"),
            dad.talk("じゃあこんなロクデナシじゃなく、もっとまともな人間をモデルにすればよかっただろ？",
                "全くよ", "勝手に$meのデータを使っといて、役立たずと思えば文句を言う",
                "酒かタバコがやりたくもなるよ", "そう思うだろ、$k_megu？"),
            megu.do("板挟みになって何も言えない$S"),
            )
