#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Story: "title"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from config import ASSET
# import scenes
# from scenes import xxx


################################################################
#
#   1. Initialize
#   2. Story memo
#   3. Story structure - 1/8
#   4. Spec
#   5. Plot - 1/4
#   6. Scenes
#   7. Conte - 1/2
#   8. Layout
#   9. Draft - 1/1
#
################################################################

# Constant
TITLE = "ミスター・ロクデナシ"
COPY = "俺の知らない父親は最高のロクデナシだった"
ONELINE = "幼い頃に亡くなった父を人工知能として蘇らせた"
OUTLINE = "約5000字のSF短編。人工知能の研究者である男性は幼い頃に亡くなった父をAIとして蘇らせた。しかしその父は想像もしない挙動を見せる"
THEME = "周囲の人がいくら評価しても子どもにとっての父親なんてロクデナシでしかない"
GENRE = "SF／ヒューマンドラマ"
TARGET = "30-40台（男女）"
SIZE = "〜8K"
CONTEST_INFO = "妄想コンテスト「お父さん」応募作"
CAUTION = ""
NOTE = ""
SITES = ["エブリスタ", "小説家になろう", "ノベルアッププラス", "カクヨム"]
RELEASED = (1, 1, 2020)
MAJOR, MINOR, MICRO = 0, 3, 0


# Episode
def ep_AI_project(w: World):
    return w.episode("AIプロジェクト",
            w.plot_note("$masakiの体にはろくでなしの父がつけたという火傷の跡がある"),
            w.plot_note("人工知能研究者である$masakiは父のことをよく知らない"),
            w.plot_note("ある日、自分の技術を使って昔の人間をAIとして蘇らせるというプロジェクトを企画する"),
            w.plot_note("その企画用に自分の父をAIにすることを思いつく"),
            "会社から成果を出すよう要請されている",
            "$masakiは研究ができればいいだけで、別に商品や社会貢献とかは興味ない",
            "父親は火事で亡くなったと聞いている",
            "$masakiは熱いものが苦手",
            "値落ちから起こされるところから、始まる（助手に起こされる）",
            )

def ep_researching(w: World):
    return w.episode("聞き取り調査",
            w.plot_note("母や父の知人から父についての話を聞いて、データを集めて回る"),
            w.plot_note("しかし聞けば聞くほど父はろくでなしだった"),
            w.plot_note("データを集めて成長させた父AIの言動は確かにろくでなしそのものだった"),
            "聞き取りは三人くらい（実際はもっと沢山）",
            "母親、腐れ縁の友人、よく飲みに行っていた飲み屋のママ",
            "最初は内部プログラムだけなので、画面越しで父に対面",
            "第一声から「酒もタバコもできないなんて、AIってのはつまらんもんだな」と",
            "母親を連れてきて確認すると、確かに父だと証言する",
            "それでも毎日やってきて時間いっぱいまで話し込んでいくところを見て、親孝行も悪くないんじゃないですか、と助手に言われてしまう",
            )

def ep_press_conference(w: World):
    return w.episode("記者会見",
            w.plot_note("AIの話を聞きつけた上司が、大々的に宣伝して企業に売り込もうと提案する"),
            w.plot_note("そのAIを搭載した父ロボットができあがり、完成披露会見が開かれることになる"),
            w.plot_note("そつなくこなし、他人に迷惑をかけないことが信条だった$masakiは、睡眠不足から火事を起こしてしまう"),
            "ずっと自分の仕事以外の仕事も手をつけて寝不足になっていた",
            "助手から火の元の注意を受けていた",
            "よく寝落ちしてしまっていた",
            )

def ep_fire_and_truth(w: World):
    return w.episode("火事と真実",
            w.plot_note("研究所で目覚めた$masakiは炎の海から逃げられない"),
            w.plot_note("そこに現れたのは父ロボットだった"),
            w.plot_note("父ロボは自分の体が溶けるのも気にせず、$masakiを助け出す"),
            w.plot_note("火災現場からみんなを救出し、息絶えた父ロボット"),
            w.plot_note("母親から「また同じ死に方をした」と"),
            w.plot_note("父の死亡原因は、幼い$masakiと母親を火事の中から助けに戻り、一酸化炭素中毒での死亡だった"),
            "助手にもう一度蘇らせるか尋ねられて、断る。「きっとまたろくでなしだから」と笑う",
            )


# Chapter
def ch_main(w: World):
    return w.chapter('main',
            ep_AI_project(w),
            ep_researching(w),
            ep_press_conference(w),
            ep_fire_and_truth(w),
            w.symbol("（了）"),
            )

# History
def hist_masaki(w: World):
    return w.chara_note("$masaki",
            )

def hist_dad(w: World):
    return w.chara_note("$dad",
            )

def hist_mam(w: World):
    return w.chara_note("$mam",
            )

def hist_megu(w: World):
    return w.chara_note("$megu",
            )

# Note
def abstract(w: World):
    return w.writer_note('概要',
            "幼い頃に父親を亡くした人工知能研究者の男性は、自分の研究成果を使い、父親をAIモデルとして復活させようとする",
            "昔の知人を伝って父の情報を集めていくうちに、父親はどうも考えうる限りの最低な人間だということが分かってきた",
            "父親AIが完成し、それを搭載したロボットがお披露目となる",
            "その時、建物火災が発生し、披露会に集まった人はピンチとなるが、そこで活躍したのが父ロボットだった",
            "父ロボの言動こそろくでなしそのものだったが、自らを犠牲にして大切な人を守るその精神だけは自分に受け継がれていることを知った",
            )


def main(): # pragma: no cover
    w = World.create_world(f"{TITLE}")
    w.config.set_version(MAJOR, MINOR, MICRO)
    w.db.set_from_asset(basic.ASSET)
    w.db.set_from_asset(ASSET)
    # spec
    w.config.set_copy(f"{COPY}")
    w.config.set_oneline(f"{ONELINE}")
    w.config.set_outline(f"{OUTLINE}")
    w.config.set_theme(f"{THEME}")
    w.config.set_genre(f"{GENRE}")
    w.config.set_target(f"{TARGET}")
    w.config.set_size(f"{SIZE}")
    w.config.set_contest_info(f"{CONTEST_INFO}")
    w.config.set_caution(f"{CAUTION}")
    w.config.set_note(f"{NOTE}")
    w.config.set_sites(*SITES)
    w.config.set_released(*RELEASED)
    return w.run(
            abstract(w),
            ch_main(w),
            hist_masaki(w),
            hist_dad(w),
            hist_mam(w),
            hist_megu(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

