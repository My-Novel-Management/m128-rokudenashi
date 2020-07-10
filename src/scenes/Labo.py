# -*- coding: utf-8 -*-
'''
Stage: "研究室"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# scenes
def awaking(w: World):
    masa = w.get('masaki')
    megu = w.get('megu')
    iwata = w.get('iwata')
    return w.scene('いつもの目覚め',
            w.plot_note("いつものように研究室で目覚めた$masakiは、いつも夢にだけ登場する髭面の男性を「あの人は本当にろくでなしだったね」と語る母のことを思い出す"),
            w.plot_note("研究室のモニタには現在研究中の$w_AIが助手の$meguと端末を通して会話をしている",
                "ただ学習モデルが彼女や$masakiだけなので、本当にリアルな人間の性格のコピィができているか確信が持てなかった"),
            w.plot_note("一方で研究成果を発表するよう上司の$iwataからはせかされており、ある程度データが揃っていて、何かしら社会貢献できそうなロボットの基本モデルにできる対象を探していた"),
            "実家に帰る、という口実＝父親の命日で法事があるから",
            "どこかで給湯室か暖房器具を出して、いつもそこの上で白衣を乾かす癖があるのを$meguに指摘される",
            )


def select_model(w: World):
    masa = w.get('masaki')
    megu = w.get('megu')
    return w.scene("父を実験モデルに",
            w.plot_note("研究室に戻った$masakiは$meguに集めてきたデータを渡して、これで新しいモデルを作ると宣言する"),
            )


def research_about_dad(w: World):
    masa = w.get('masaki')
    megu = w.get('megu')
    ohara = w.get('ohara')
    return w.scene("父についての情報（消防士時代）",
            w.plot_note("その日から膨大な量の聞き込みデータを$w_AIに学習させていく"),
            w.plot_note("データは母や父の知人、昔の消防士仲間や果ては働いていた左官屋の知り合いなどからの、聞き取り調査を元にしたものだった"),
            w.plot_note("消防士仲間は父は口ばっかりで、出動ベルが鳴っても寝たまま置きず、仲間に引きずり降ろされて、無理矢理に車に乗せられる、最悪の消防士だったと"),
            )


def research_about_dad2(w: World):
    masa = w.get('masaki')
    megu = w.get('megu')
    minobe = w.get('minobe')
    return w.scene("父についての情報（左官屋時代）",
            w.plot_note("それまでの左官屋時代も、金が入ったらすぐに飲みにでかけてしまって結局仕事に来ず、仕事先に行ってみたらそこの隣が飲み屋で玄関前で寝ていたとか"),
            w.plot_note("とにかく酒と女とだらしなさのエピソードが盛りだくさんで、とても規範となるような$w_AIにはならないと判断せざるをえなかった"),
            )


def wonderful_AI(w: World):
    masa = w.get('masaki')
    megu = w.get('megu')
    return w.scene("素晴らしい$w_AI",
            w.plot_note("ただそのデータを学習した$w_AIは今までとは違い、とても人間味があるもので、ジョークを言ったり、嘘をついたり、笑ったり、従わなかったりと、",
                "$masakiたちが求めた人間らしい$w_AIの姿がそこにあり、研究を進めざるを得なかった"),
            )


def meet_with_mam(w: World):
    masa = w.get('masaki')
    megu = w.get('megu')
    mam = w.get('mam')
    return w.scene("母と$w_AIの面会",
            w.plot_note("最後に母親を連れてきて、学習し、成長した父$w_AIと対面させる"),
            w.plot_note("その第一声は「歳とったなあ、$mam」だった",
                "だがその失礼さにも関わらず「相変わらずね」と母親は嬉しそう"),
            w.br(),
            w.plot_note("それから母は毎日通ってきては、父$w_AIと会話をし、学習させていく",
                "日を追うごとにどんどん父らしい$w_AIが出来上がり、その仕上がりを見て上司からはついにロボットに搭載する許可が降りてしまった"),
            )



def decided_presentation(w: World):
    masa = w.get('masaki')
    megu = w.get('megu')
    iwata = w.get('iwata')
    return w.scene("発表会の決定",
            w.plot_note("そんな中、大々的に一般向けの記者会見を行うことが決まり、$masakiは父$w_AIに頼み込んで、何とか問題を起こさないようにと注意する"),
            )


def preparation(w: World):
    masa = w.get('masaki')
    megu = w.get('megu')
    return w.scene("準備で忙しい",
            w.plot_note("$masakiは発表会の準備で忙しくしていた",
                "睡眠不足もあり、研究室で寝落ちしてしまうことも以前より多かった",
                "会社への泊まり込みも続き、疲労困憊になっていた"),
            w.plot_note("$meguに心配されたが、どうしてもこの会見を成功させて、研究資金と次のもっとちゃんとした$w_AIモデル作成研究の許可をもらいたいと必死になっていた"),
            )


def before_day(w: World):
    masa = w.get('masaki')
    megu = w.get('megu')
    return w.scene("発表会前日",
            w.plot_note("発表会前日、最後まで資料とスケジュールの調整をしていた$masakiは、$meguに言われていた発表会の衣装を何も考えておらず、仕方なく白衣を洗濯して、",
                "暖房器具の上に干しておき、また資料作りへと戻った"),
            w.plot_note("しかしそれが火元となり、研究所は火事になる"),
            )


def awake_in_fire(w: World):
    masa = w.get('masaki')
    megu = w.get('megu')
    return w.scene("炎の中での目覚め",
            w.plot_note("スマホに連絡があり、$masakiは目覚める",
                "気づくと既に研究室の外にまで煙が充満し、独力で逃げるのは不可能だと思えた"),
            w.plot_note("その失火の原因が、記者会見用に洗濯をした白衣を乾かしておいたことだと気づいて、",
                "普段自分が他人に迷惑を掛けないようにと生きてきたのに、結局は自分もロクデナシの父親と同じだったと失望する"),
            )


def appear_dad_robo(w: World):
    masa = w.get('masaki')
    megu = w.get('megu')
    dad = w.get('dad')
    return w.scene("現れた父ロボット",
            w.plot_note("死を覚悟した$masakiの前に現れたのは消防隊員ではなく、父ロボだった"),
            w.plot_note("「なんで来た？」「歩いてきた。ただのコンピュータだった頃は歩けなかったからなあ」と無駄口を叩く父",
                "その様に憤りを感じるが、状況を確認する$masaki"),
            w.plot_note("既に火は建物中に回り、消防車は渋滞の中、まだ現場に到着できないらしい",
                "ネット回線も繋がらなくなり、停電が発生する",
                "ただ既に他の所員、スタッフについては脱出し終えたと、父ロボから聞いた"),
            w.plot_note("「それじゃあなぜここに来た？　もう助からないんだろ？」と聞き返す$masakiに、父ロボは「息子を助けない父親は、本当のロクデナシだろ」と笑う"),
            )
