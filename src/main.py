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
from storybuilder.assets import common_rubi
from config import ASSET
# import scenes
from scenes import Cafeteria
from scenes import Company
from scenes import Home
from scenes import Labo
from scenes import MeetingRoom
from scenes import Pub
from scenes import SickRoom
from scenes import TestHall


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
COPY = "ろくでなしってやつは、本当にどうしようもないんだ"
ONELINE = "約8000字のSFヒューマンドラマ。AI研究者の男性は自分の亡くなった父をモデルにすることを思いつくが。"
OUTLINE = "AI研究者の正木（まさき）は研究が上手くいかず、ある時、幼い頃に亡くなった父をモデルにすることを考える。それは上手くいったように思えたが。"
THEME = "周囲の人がいくら評価しても子どもにとっての父親なんてロクデナシでしかない"
GENRE = "SF／ヒューマンドラマ"
TARGET = "30-40台（男女）"
SIZE = "〜8K"
CONTEST_INFO = "妄想コンテスト「お父さん」応募作"
CAUTION = ""
NOTE = ""
SITES = ["エブリスタ", "小説家になろう", "ノベルアッププラス", "カクヨム"]
RELEASED = (7, 12, 2020)
MAJOR, MINOR, MICRO = 1, 1, 0


# Episode
def ep_AI_project(w: World):
    return w.episode("$AIプロジェクト",
            Labo.awaking(w),
            Home.memorial(w),
            Pub.old_talk(w).omit(),
            )

def ep_researching(w: World):
    return w.episode("父ロボット",
            Labo.select_model(w),
            Labo.research_about_dad(w),
            Labo.research_about_dad2(w),
            Labo.wonderful_AI(w).omit(),
            Labo.meet_with_mam(w),
            Cafeteria.decided_presentation(w),
            Labo.preparation(w),
            )

def ep_press_conference(w: World):
    return w.episode("記者会見",
            MeetingRoom.meeting(w).omit(),
            Cafeteria.major_topic(w).omit(),
            TestHall.powerful_robo(w).omit(),
            TestHall.back_face(w).omit(),
            Cafeteria.decided_presentation(w),
            Labo.preparation(w),
            Labo.before_day(w).omit(),
            ).omit()

def ep_fire_and_truth(w: World):
    return w.episode("ミスター・ロクデナシ",
            Labo.awake_in_fire(w),
            Labo.appear_dad_robo(w),
            Company.escaping(w),
            Company.safely_escaped(w),
            SickRoom.awake_and_report(w),
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
            "内職とパートで家計を支えた母と、飲んだくれてパチンコ売ってる元消防士の父の下に生まれる",
            "一歳の頃に父は事故死し、それ以来シングルマザーの母に育てられる",
            "小さい頃から勉強だけはしておけと口すっぱく言われ、図書館に通って本を読む子どもになった",
            "奨学金で筑波大に入り、人工知能の研究に興味を持つ",
            "そのまま大学に残り、博士号を収める",
            "先輩からの口ききで、企業の$w_AI研究所に入社し、現在に至る",
            )

def hist_dad(w: World):
    return w.chara_note("$dad",
            "場末の風俗店で誰の子かも分からないまま生まれる",
            "周囲を酒と化粧臭い裸の女に囲まれながら、いろいろな母乳で育った",
            "母親が客と事実婚をし、父親らしい男ができる",
            "酒とタバコを父親から教え込まれる",
            "なんとか高校までは入ったが、犯されそうになった女を助けるために喧嘩をして、退学になる",
            "バイトや日雇いで日銭を稼いで過ごす",
            "ある時働いていた焼肉屋が火事になり、その時に助けられた消防士のかっこよさに当てられ、消防士を目指す",
            "消防士として勤務を始めるが、素行の悪さから首になる",
            "しかし消防士として助けた縁で、妻と結婚に至る",
            "息子を一人もうけるも、家族のために働くといった先で面倒おこしては首になる",
            "競馬にパチンコ、賭け事で金をなくしては妻に泣きつく",
            "あるとき、住んでいたアパートを自身のタバコの失火により延焼させ、その時に寝ていた息子を助け出しに戻り、煙に巻き込まれて、一酸化炭素中毒で亡くなった",
            )

def hist_mam(w: World):
    return w.chara_note("$mam",
            "四人兄弟姉妹の二番目として生まれる",
            "漁業が盛んな港町で、父は漁師の二代目、母は地元の魚市場で魚の加工をしていた",
            "高校を出て、地元で建設会社の事務員になった",
            "そこで恋をして、かけおち。東京に出るも、一年もせずに別れてしまった",
            "実家に帰ることはせず、カフェでアルバイトをしながら過ごす",
            "働いていた店が火事になり、その時に救出にきた$dadに恋をする",
            "結婚した時には消防士を首になっていたが、そのことは半年経つまで教えてもらえなかった",
            "教えてもらえたきっかけは、妊娠発覚",
            "それ以来、働く働く詐欺を疑うようになる",
            "それでもどこか憎めず、金をすってきたと泣きつく旦那を許してしまった",
            )

def hist_megu(w: World):
    return w.chara_note("$megu",
            "東北の雪深い街でひっそりと生まれる",
            "地元の役場勤務の母と、高校の国語教師の父の下に生まれる",
            "姉が一人、弟が一人いた",
            "弟の面倒を見ながら本を読むのが好きな子どもだった",
            "料理好きの姉とは違い、料理は苦手だったが、掃除や整理整頓をするのは好きで、",
            "几帳面な性格と世話焼きなところが学校では書紀などに選出される人望となった",
            "大学では数学を好んだが、プログラムから、人工知能への興味を抱くようになる",
            "教授の推薦で、今の研究所に就職が決まり、そこで$masakiと出会う",
            )

# Note
def abstract(w: World):
    return w.writer_note('概要',
            "幼い頃に父親を亡くした人工知能研究者の男性は、自分の研究成果を使い、父親を$w_AIモデルとして復活させようとする",
            "昔の知人を伝って父の情報を集めていくうちに、父親はどうも考えうる限りの最低な人間だということが分かってきた",
            "父親$w_AIが完成し、それを搭載したロボットがお披露目となる",
            "その時、建物火災が発生し、披露会に集まった人はピンチとなるが、そこで活躍したのが父ロボットだった",
            "父ロボの言動こそろくでなしそのものだったが、自らを犠牲にして大切な人を守るその精神だけは自分に受け継がれていることを知った",
            )


def main(): # pragma: no cover
    w = World.create_world(f"{TITLE}")
    w.config.set_version(MAJOR, MINOR, MICRO)
    w.db.set_from_asset(basic.ASSET)
    w.db.set_from_asset(common_rubi.ASSET)
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

