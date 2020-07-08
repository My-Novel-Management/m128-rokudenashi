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
MAJOR, MINOR, MICRO = 0, 1, 0


# Episodes
def abstract(w: World):
    return w.writer_note('概要',
            "幼い頃に父親を亡くした人工知能研究者の男性は、自分の研究成果を使い、父親をAIモデルとして復活させようとする",
            "昔の知人を伝って父の情報を集めていくうちに、父親はどうも考えうる限りの最低な人間だということが分かってきた",
            "父親AIが完成し、それを搭載したロボットがお披露目となる",
            "その時、建物火災が発生し、披露会に集まった人はピンチとなるが、そこで活躍したのが父ロボットだった",
            "父ロボの言動こそろくでなしそのものだったが、自らを犠牲にして大切な人を守るその精神だけは自分に受け継がれていることを知った",
            )


def ch_main(w: World):
    return w.chapter('main',
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

