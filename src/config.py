# -*- coding: utf-8 -*-
'''
Story Config
============
'''

ASSET = {
        "PERSONS": (
            # (tag / name / full / age (birth) / job / call / info)
            ('masaki', '正木', '正木,豊', 35,(1,1), 'male', '研究者', 'me:僕:dad:父さん'),
            ("dad", "六輔", "正木,六輔", 60,(1,1), 'male', '無職', 'me:オレ:k_megu:めぐちゃん'),
            ('mam', '美千代', '正木,美千代', 59,(1,1), 'female', 'パート', 'me:あたし'),
            ('megu', '恵美', '新浦,恵美', 29,(1,1), 'female', '助手', 'me:私'),
            ("iwata", "岩田", "岩田,賢三", 40,(1,1), "male", "上司", "me:私"),
            ("ohara", "大原", "大原,健次", 55,(1,1), 'male', "消防士", "me:俺"),
            ("minobe", "美濃部", "美濃部,武男", 60,(1,1), 'male', "左官業", "me:ワシ"),
            ("ancle", "叔父", "", 57,(1,1), 'male', '干物屋', 'me:僕'),
            ("taichi", "太一", "鈴野,太一", 60,(1,1), 'male', '農家', 'me:俺'),
            ("miho", "美保", "伊坂,美保", 65,(1,1), 'female', '飲み屋', 'me:私'),
            ),
        "STAGES": (
            # (tag / name / parent / (geometry) / info)
            ("Ibaraki", "茨城県", "", (200,80)),
            ("Home", "正木家", "Ibaraki"),
            ("Pub", "飲み屋", "Ibaraki"),
            ("Pachi", "パチンコ屋", "Ibaraki"),
            ("FireStation", "消防署", "Ibaraki"),
            ("Company", "マグナテック", "Tokyo"),
            ("TestHall", "実験場", "Tokyo"),
            ("Labo", "研究室", "Tokyo"),
            ("Cafeteria", "社員食堂", "Tokyo"),
            ("MeetingRoom", "会議室", "Tokyo"),
            ("SickRoom", "病室", "Tokyo"),
            ("Cafe", "喫茶店", "Tokyo"),
            ),
        "DAYS": (
            # (tag / name / month / day / year)
            ),
        "TIMES": (
            # (tag / name / hour / minute)
            ),
        "ITEMS": (
            # (tag / name / cate / info)
            ),
        "WORDS": (
            # (tag / name / cate / info)
            ("AI", "ＡＩ"),
            ("CG", "ＣＧ"),
            ("dadAI", "ＡＩ六号"),
            ("dadRobo", "ロクス"),
            ("full_dadRobo", "高性能自律型作業ロボット"),
            ),
        "RUBIS": (
            # (origin / rubi / exclusions / always)
            ),
        }

