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
            w.cmd.change_camera("masaki"),
            w.cmd.change_stage("Labo"),
            w.plot_note("いつものように研究室で目覚めた$masakiは、いつも夢にだけ登場する髭面の男性を「あの人は本当にろくでなしだったね」と語る母のことを思い出す"),
            w.plot_note("研究室のモニタには現在研究中の$w_AIが助手の$meguと端末を通して会話をしている",
                "ただ学習モデルが彼女や$masakiだけなので、本当にリアルな人間の性格のコピィができているか確信が持てなかった"),
            w.plot_note("一方で研究成果を発表するよう上司の$iwataからはせかされており、ある程度データが揃っていて、何かしら社会貢献できそうなロボットの基本モデルにできる対象を探していた"),
            "実家に帰る、という口実＝父親の命日で法事があるから",
            "どこかで給湯室か暖房器具を出して、いつもそこの上で白衣を乾かす癖があるのを$meguに指摘される",
            masa.be("研究室で目覚める"),
            "亡くなった季節を決めておく。秋か、冬か",
            masa.think("いつもの夢だった",
                "顔もよく覚えていない父親が、炎に消されていく",
                "$Sの父親は火事で死んだと聞かされている",
                "母や叔父の話では、酒や女にだらしなく、それで色々と仕事を首になったろくでなしだったと聞いている"),
            megu.be(),
            megu.talk("起きられました？"),
            megu.look("研究の助手をしている$full_megu",
                "ショートカットの茶髪で、フレームなしの眼鏡をかけている",
                "いつも綺麗にした白衣を着用している", "下はシャツとパンツ"),
            masa.talk("また寝落ちしてたみたいだ", "$AIの方は？"),
            "白衣がソファにかけられ、汚れている",
            "それを$meguが手にして、小言を言う",
            masa.do("モニタには学習中のデータの進捗状況が表示されている"),
            masa.do("会社の研究室で、作業ロボット用の人工知能の開発に携わっていた"),
            "研究室のレイアウトなど",
            iwata.come("部屋に入ってくる"),
            iwata.talk("そろそろ赤ん坊から小学生くらいに育ったか？"),
            iwata.look("上司の$iwataだった", "中途半端にカールした髪をこねくりまわしながら、$n_meguを見てにっこりと微笑む"),
            megu.talk("おはようございます"),
            masa.talk("そんな簡単に人間の代用品ができると思わないで下さいって、何度も言ったでしょう？"),
            iwata.talk("それは分かってるよ",
                "よその会社の作業ロボットが、麺を茹でるだけで精一杯とか、茶碗に盛り付けるだけが精々だとかさ、",
                "そんな夢のない話は耳にタコだから",
                "でもうちはそうじゃない", "お前がそう言わせてくれるんだろ？"),
            masa.talk("今試しているモデルが成功すれば、その可能性はあります"),
            iwata.go("じゃあよろしく、と言い残して出ていく"),
            masa.do("ただ画面に表示された$AIは、簡単な質疑応答もまだ難しそうだった"),
            megu.talk("そういえば週末、実家に帰られるんですよね？", "その間の報告はどうします？"),
            masa.talk("休日出勤はしなくてもいいよ", "この際ゆっくり休んでくれ"),
            megu.talk("ありがとうございます"),
            masa.think("法事のことを思い出して頭が痛くなる"),
            )


def select_model(w: World):
    masa = w.get('masaki')
    megu = w.get('megu')
    return w.scene("父を実験モデルに",
            w.plot_note("研究室に戻った$masakiは$n_meguに集めてきたデータを渡して、これで新しいモデルを作ると宣言する"),
            w.cmd.change_stage("Labo"),
            masa.be("週明け、研究室で$Sは記録して回ったものをデータ化していた"),
            megu.be(),
            megu.talk("今度はこちらを使われるんですか？"),
            masa.talk("ああ"),
            megu.talk("どなたのものか聞いてもいいですか？"),
            masa.talk("$meの父のものだよ"),
            megu.do("驚く$S"),
            )


def research_about_dad(w: World):
    masa = w.get('masaki')
    megu = w.get('megu')
    ohara = w.get('ohara')
    return w.scene("父についての情報（消防士時代）",
            w.plot_note("その日から膨大な量の聞き込みデータを$w_AIに学習させていく"),
            w.plot_note("データは母や父の知人、昔の消防士仲間や果ては働いていた左官屋の知り合いなどからの、聞き取り調査を元にしたものだった"),
            w.plot_note("消防士仲間は父は口ばっかりで、出動ベルが鳴っても寝たまま置きず、仲間に引きずり降ろされて、無理矢理に車に乗せられる、最悪の消防士だったと"),
            masa.be("研究室でモニタを見つめている"),
            masa.do("モニタには記録していた$oharaの映像が流れる"),
            ohara.voice("$dadさんは仕事の覚えは早かったです",
                "消防学校時代はいつも赤点ギリギリで教官たちから本気で消防士になる気があるのかと叱られてたらしいですが、",
                "現場に出て一番頼りになる同僚でしたね"),
            ohara.voice("ただ普段の訓練はサボる、いないと思ったら消防団の若い連中と飲み歩いてる",
                "合コンときけば仕事を放り出して駆けつけるなど、",
                "本当に人間性としては散々だったんで、",
                "最終的に首になったのも仕方ないかなって"),
            ohara.voice("でもね思うんです",
                "$dadさん、付き合うとそこまで憎めないんです",
                "ただ、いろいろとだらしないだけで",
                "現場で死人が出たときだってみんな陰鬱となるんですけど、",
                "あの人だけはいつも笑ってました", "それは俺たちの仕事じゃないって"),
            )


def research_about_dad2(w: World):
    masa = w.get('masaki')
    megu = w.get('megu')
    minobe = w.get('minobe')
    return w.scene("父についての情報（左官屋時代）",
            w.plot_note("それまでの左官屋時代も、金が入ったらすぐに飲みにでかけてしまって結局仕事に来ず、仕事先に行ってみたらそこの隣が飲み屋で玄関前で寝ていたとか"),
            w.plot_note("とにかく酒と女とだらしなさのエピソードが盛りだくさんで、とても規範となるような$w_AIにはならないと判断せざるをえなかった"),
            masa.be("別のデータを見ている"),
            masa.do("それは左官屋時代の知人のもの"),
            minobe.voice("いや、あいつはほんと、ただのろくでなしだったよ",
                "そりゃ手先は器用で仕事はできたけどな",
                "結局新人で入ってきた女に手つけて、親方の怒りかって、辞めたんだわ"),
            minobe.voice("とにかく金遣いが荒くて、日銭が入ればすぐパチだ、酒だ、タバコだ女だって、",
                "将来も何も考えてない、その日暮らしってのはああいつやつを言うんだな"),
            minobe.voice("ある日、電話しても出ないんで、仕方なく仕事に行ったら、その仕事先の隣が飲み屋で、その前で寝てたなんてこともあった"),
            minobe.voice("ま、あんな野郎でもいなくなっちまうと、寂しいがな"),
            )


def wonderful_AI(w: World):
    masa = w.get('masaki')
    megu = w.get('megu')
    dad = w.get('dad')
    return w.scene("素晴らしい$w_AI",
            w.plot_note("ただそのデータを学習した$w_AIは今までとは違い、とても人間味があるもので、ジョークを言ったり、嘘をついたり、笑ったり、従わなかったりと、",
                "$masakiたちが求めた人間らしい$w_AIの姿がそこにあり、研究を進めざるを得なかった"),
            masa.be(),
            masa.do("目の前のモニタには簡易$CGで髭面の男性が表現されている"),
            dad.talk("なんだよ", "お前が$meを$AIで蘇らせたんだろ？", "よう、息子", "ところで$AIっつーのは酒は飲めねえのか？"),
            masa.do("愕然とする$S"),
            megu.do("苦笑する"),
            )


def meet_with_mam(w: World):
    masa = w.get('masaki')
    megu = w.get('megu')
    mam = w.get('mam')
    dad = w.get('dad')
    return w.scene("母と$w_AIの面会",
            w.plot_note("最後に母親を連れてきて、学習し、成長した父$w_AIと対面させる"),
            w.plot_note("その第一声は「歳とったなあ、$mam」だった",
                "だがその失礼さにも関わらず「相変わらずね」と母親は嬉しそう"),
            w.br(),
            w.plot_note("それから母は毎日通ってきては、父$w_AIと会話をし、学習させていく",
                "日を追うごとにどんどん父らしい$w_AIが出来上がり、その仕上がりを見て上司からはついにロボットに搭載する許可が降りてしまった"),
            masa.be(),
            mam.come("母親が部屋に入ってくる"),
            mam.talk("本当に、あの人と話せるんだね？"),
            masa.talk("まあ……見てくれれば分かるよ"),
            dad.be("画面の中に、写真を元にして父に似せた$CGの頭が表示されている"),
            dad.talk("どうした、そんな顔して", "$meだよ、$me$me"),
            mam.talk("詐欺ですか、俺俺って"),
            dad.talk("なんか$AIってのは酒もタバコも駄目なんだと",
                "せめてお前の豚汁が飲めればなあ",
                "あとグラム千円くらいの肉を焼いて、すりおろしたニンニクとレモン汁、そこにラー油を垂らしたタレをいれて、",
                "一杯やりてえな"),
            mam.talk("$fn_masaki、今まであんたが何してるか全然わからなかったけど、",
                "こんなどえらいもん作ってたんだね！", "$meは嬉しくて涙が出るよ"),
            masa.think("作りたかったものじゃないんだとは、言えなかった"),
            )



def preparation(w: World):
    masa = w.get('masaki')
    megu = w.get('megu')
    return w.scene("準備で忙しい",
            w.plot_note("$masakiは発表会の準備で忙しくしていた",
                "睡眠不足もあり、研究室で寝落ちしてしまうことも以前より多かった",
                "会社への泊まり込みも続き、疲労困憊になっていた"),
            w.plot_note("$meguに心配されたが、どうしてもこの会見を成功させて、研究資金と次のもっとちゃんとした$w_AIモデル作成研究の許可をもらいたいと必死になっていた"),
            w.cmd.change_stage("Labo"),
            masa.be("パソコンに向かっている"),
            masa.look("髪の毛はぼさぼさで、目元も隈ができている"),
            megu.come(),
            megu.talk("いくら急遽決まった発表会向けに資料を作っているからって、ちゃんと休んでますか？"),
            megu.do("テーブルの上には食べ残した弁当が"),
            megu.talk("少しは帰って寝てください", "指示してくだされば$meが資料作成はしますから"),
            masa.talk("あいつ、最近訓練サボってるって聞いたんだが、どうなんだ？"),
            megu.talk("報告書に上げた通りです", "まるで人間みたいですよ", "体調不良なんて言葉を書き込むことになるとは思いませんでした",
                "ただ実際の計測値として異常が出ているので、$AIへのストレスが制御系全体へ悪影響を与えているという説は考えられます"),
            masa.think("その辺りも資料に組み込まないといけないと考える",
                "ただ率直な意見を盛り込むと絶対に実用化には至らないので、どうするか悩んでしまう"),
            megu.talk("もう、こんなところに放り出したままで"),
            megu.do("ソファにかけた白衣を手に取る",
                "それは汚れが目立ち、クリーニングに出した方がよさそうだった"),
            megu.talk("まとめてクリーニングに出しますから、他にもあったら言って下さい"),
            masa.talk("それはそこに置いといてくれ",
                "呼ばれた時に必要だ"),
            megu.talk("今日は置いときますけど、ちゃんと洗って下さいよ？"),
            )


def before_day(w: World):
    masa = w.get('masaki')
    megu = w.get('megu')
    return w.scene("発表会前日",
            w.plot_note("発表会前日、最後まで資料とスケジュールの調整をしていた$masakiは、$n_meguに言われていた発表会の衣装を何も考えておらず、仕方なく白衣を洗濯して、",
                "暖房器具の上に干しておき、また資料作りへと戻った"),
            w.plot_note("しかしそれが火元となり、研究所は火事になる"),
            masa.be("発表会前日、その日の深夜、まだパソコンに向かっていた"),
            "テーブルには上司が持ってきた祝い酒があった。「あいつも酒が飲めるといいのにな」と言われて",
            masa.do("静まり返った中で、プリンタからアウトプットする音だけが響く"),
            masa.do("一旦、休憩と立ち上がり、思い出して適当に洗濯機にかけておいた白衣を取り出すと、",
                "それを仮眠室の暖房器具の上に釣って、朝までには乾くだろうと研究室に戻る"),
            masa.think("既に会場へと$dadRoboは運び出され、そこで眠っている",
                "会場の準備は$n_meguにまかせていたが、そっちの確認もしないといけないと思っていた"),
            masa.do("時刻は四時", "三時間は寝れるかと思ってアラームをセットした"),
            )


def awake_in_fire(w: World):
    masa = w.get('masaki')
    megu = w.get('megu')
    return w.scene("炎の中での目覚め",
            w.plot_note("スマホに連絡があり、$masakiは目覚める",
                "気づくと既に研究室の外にまで煙が充満し、独力で逃げるのは不可能だと思えた"),
            w.plot_note("その失火の原因が、記者会見用に洗濯をした白衣を乾かしておいたことだと気づいて、",
                "普段自分が他人に迷惑を掛けないようにと生きてきたのに、結局は自分もロクデナシの父親と同じだったと失望する"),
            masa.be("スマートフォンの鳴る音で目覚めた"),
            masa.do("$n_meguからのメッセージを見て、既に発表会が始まっていることを知るが"),
            masa.do("既に部屋は煙臭い"),
            masa.do("窓の外を確認するとどこかから煙が流れ出している"),
            masa.do("警報機が鳴り響き、ドアを開けると炎が見えた"),
            masa.think("$n_meguに言われたことを思い出し、自分の責任で失火したものだと推測する"),
            masa.think("自分も父親と同じで、結局自分のやりたいように生きて、他人に迷惑をかけてしまう人生だったと悲観する"),
            masa.do("停電し、ネットや電話も繋がらず、スマートフォンは電源が切れた",
                "逃げ出すことは諦めて救助を待とうとするが、まだ消防車も救急車も到着していない"),
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
            "実は父の死因は息子を助けた際の一酸化炭素中毒だった、と実は母のインタビューで知っていた、というのを父ロボとの会話で発言して「あんたまた死ぬ気か？」とやる",
            "でも父ロボットは「俺はロボだからな。死ぬとかねえだろ？」と",
            masa.be("諦めたその瞬間、ドアが開けられた"),
            dad.come("現れた影", "一瞬消防士に見えた"),
            masa.talk("$dad？"),
            masa.do("なぜ会場ではなく、ここにいるのか問いただす$S"),
            dad.talk("息子が火事に巻き込まれているのを知って、放っておくほど、$meはロクデナシじゃないさ"),
            masa.do("本当は寝過ごしただけだと分かったが、とにかく助かった"),
            masa.talk("状況は？"),
            dad.explain("確認したところ道路が混雑していて、まだ十分以上到着にかかりそうなこと、",
                "施設内に残っていたスタッフは自分が脱出させ、残りは$masaki一人なことなどの、説明を受ける"),
            masa.talk("それじゃあ、さっさと脱出しよう"),
            dad.talk("そう、だな"),
            masa.think("歯切れの悪さに何か感じる"),
            dad.do("防火服を息子に手渡し、彼はドアを開ける"),
            dad.talk("$meが脱出口を確保するから、ついてこい"),
            masa.talk("こんな時だけ父親面を……わかった"),
            masa.do("彼についていく"),
            )