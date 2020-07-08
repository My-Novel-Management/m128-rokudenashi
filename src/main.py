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
#   3. Story structure
#   4. Plot
#   5. Scenes
#   6. Conte
#   7. Layout
#   8. Draft
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
MAJOR, MINOR, MICRO = 0, 2, 0


# Episode


# Chapter
def ch_main(w: World):
    return w.chapter('main',
            w.plot_note("$masakiの体にはろくでなしの父がつけたという火傷の跡がある"),
            w.plot_note("人工知能研究者である$masakiは父のことをよく知らない"),
            w.plot_note("ある日、自分の技術を使って昔の人間をAIとして蘇らせるというプロジェクトを企画する"),
            w.plot_note("その企画用に自分の父をAIにすることを思いつく"),
            w.plot_note("母や父の知人から父についての話を聞いて、データを集めて回る"),
            w.plot_note("しかし聞けば聞くほど父はろくでなしだった"),
            w.plot_note("データを集めて成長させた父AIの言動は確かにろくでなしそのものだった"),
            w.plot_note("そのAIを搭載した父ロボットができあがり、完成披露会見が開かれることになる"),
            w.plot_note("そつなくこなし、他人に迷惑をかけないことが信条だった$masakiは、睡眠不足から火事を起こしてしまう"),
            w.plot_note("披露会会場には多くの人が集まっていたが、主催者たちは登場しない"),
            w.plot_note("研究所で目覚めた$masakiは炎の海から逃げられない"),
            w.plot_note("そこに現れたのは父ロボットだった"),
            w.plot_note("父ロボは自分の体が溶けるのも気にせず、$masakiを助け出す"),
            w.plot_note("火災現場からみんなを救出し、息絶えた父ロボット"),
            w.plot_note("母親から「また同じ死に方をした」と"),
            w.plot_note("父の死亡原因は、幼い$masakiと母親を火事の中から助けに戻り、一酸化炭素中毒での死亡だった"),
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
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

