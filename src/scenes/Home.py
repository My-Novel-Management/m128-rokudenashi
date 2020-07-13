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
            w.symbol("　　　　◆"),
            "実家が茨城にあるとか、そういった地方情報を",
            masa.be("その週末、$Sは都内から快速電車で一時間程掛けて実家の古い平屋で、",
                "顔を赤くした近所の老人たちに囲まれていた"),
            mam.be(),
            mam.talk("あら$masaki、もうビールはいいの？"),
            masa.talk("会社でもほとんどそういう付き合いはしないんだ", "すぐに気持ち悪くなる"),
            mam.talk("お父さんはお酒が大好きで、それこそお茶出すくらいならお酒をくれって言ってたくらいなんだから"),
            masa.talk("あの人に似なくてよかったと思ってるよ"),
            masa.do("そう答えて縁側に避難したものの、",
                "$Sには父親の記憶がほとんどない",
                "二歳の頃に火事に巻き込まれて亡くなったという父について母親から聞いた以上の情報は持っていなかった"),
            ancle.be(),
            ancle.talk("まあしかし兄貴のヤツも死んで三十二年も経つってのに誰も褒めないってのは、ほんとにろくでなしだったんだな"),
            masa.do("隣町でキャベツ農家をやっている叔父はその禿げ上がった頭を赤く火照らせながら、父親の話を魚にして大笑いしている", "&"),
            mam.do("母親は千鳥足になったお坊さんを送り出し、戻ってきては慌ただしく空になったコップに瓶ビールを注いで回る"),
            masa.think("親戚の見慣れた顔ばかりでなく、近所や昔の父親の知人も混ざっているようだった",
                "三十三回忌なんて今更どこもやらないのにそれでもあの「ろくでなし」相手にこれだけ集まってくれるんだから地獄で鬼と笑いながら宴会でもしているのだろうなと思いながら、",
                "$Sはスマートフォンでニュースのチェックをする",
                "七月に開催される大規模スポーツ大会に合わせて中東の某王国の皇太子が来日するらしい",
                "#女と見れば声を掛けてすぐに結婚を迫るという噂の彼は、日本に生まれていたらきっとろくでなしと呼ばれていただろう"),
            ohara.be("#気難しい顔で座っている"),
            masa.do("と、宴会の末席で一人ぽつんとビールを飲んでいる角刈りの男性が目に入った"),
            masa.talk("母さん", "あれは？"),
            mam.talk("知らない？", "消防士時代の同僚の$oharaさん"),
            masa.think("どんな仕事に就いても半年と持たずに首になってばかりだったという父親が唯一、三年間もこなしたのが消防士だったことを思い出す"),
            masa.talk("あの、すみません"),
            ohara.talk("あ、$ln_dadの息子さん", "もうこんなに大きくなられたんですね"),
            masa.talk("ついにあの人と同じ年齢になってしまいましたよ",
                "それより、ちょっと聞かせて欲しいんですが、消防士時代の父ってどんな感じだったんですか？"),
            ohara.talk("ああそうか。君が一歳になるまでに辞めてしまったんですよね",
                "うん", "仕事はできましたよ", "特に現場での人命救助の技術については隊長も一目置くって感じで"),
            masa.talk("あの、少し記録をしてもいいですか？"),
            ohara.talk("え、ええ"),
            masa.do("やや戸惑う$oharaを前に、$Sはボイスレコーダを取り出して畳の上に置いた"),
            )

