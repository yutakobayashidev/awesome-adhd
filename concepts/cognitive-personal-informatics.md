---
title: 認知パーソナルインフォマティクス
created: 2026-07-23
updated: 2026-09-17
type: concept
tags: [adhd, attention, executive-function, working-memory, accessibility, tool, research]
sources: [raw/papers/arxiv-cognitive-personal-informatics-chi26-2026.md, raw/papers/pubmed-adhd-digital-text-comprehension-self-monitoring-2019.md, raw/papers/arxiv-multilingual-text-to-pictogram-reading-rehabilitation-2026.md, raw/papers/pubmed-adhd-ema-daily-life-adolescents-2026.md, raw/papers/selin-2026-self-tracking-masking-neurodivergent.md, raw/papers/ruf-2023-diet-physical-activity-impulsivity-adult-adhd-ema.md, raw/papers/carr-2026-fielded-attention-adhd-context.md, raw/papers/yi-2026-context-dependent-adhd-risk-coupling-commentary.md, raw/papers/raffaelli-2025-thought-content-variability-adhd-context.md, raw/papers/kennedy-2024-ema-perceived-adhd-symptoms-adolescents.md]
source_additions_2026-08-31_research_watch: [raw/papers/koch-2021-e-diaries-adhd-jitai-review.md]
source_additions_2026-09-03_research_watch: [raw/papers/murray-2021-ema-emotional-dysregulation-adult-adhd-internalising.md]
source_additions_2026-09-03-setlog: [raw/articles/tweet-2095384585760886934-setlog-hourly-photo-log.md]
source_additions_2026-09-07_research_watch: [raw/papers/goh-2026-day-to-day-adhd-stress-college-ema.md]
source_additions_2026-09-17_research_watch: [raw/papers/mitchell-2014-ema-smoking-adults-adhd.md]
confidence: medium
---

# 認知パーソナルインフォマティクス

認知パーソナルインフォマティクスは、集中、記憶、読解、予定、切り替えなどの認知状態を、本人の生活文脈に沿って記録・可視化・支援する考え方である。ADHD Wiki では、平均的な集中力を点数化する道具ではなく、本人がどの条件で読みやすいか、戻りやすいか、忘れにくいかを扱う [[assistive-technology]] として読む。^[raw/papers/arxiv-cognitive-personal-informatics-chi26-2026.md]

## ADHD 支援への含意

- **状態を人格評価にしない**: 注意がそれた、読めなかった、戻れなかった、を「だらしない」ではなく、媒体・時間帯・通知・疲労・作業量の条件として記録する。
- **自己報告だけにしない**: ADHD 学生はデジタル文章で理解得点が下がり、自分の出来の予測もずれやすいという研究がある。自己モニタリングそのものが難しくなるため、読み終わり、要点確認、紙/画面の違いなど、行動指標も見る。^[raw/papers/pubmed-adhd-digital-text-comprehension-self-monitoring-2019.md]
- **読解の足場を作る**: text-to-pictogram のような読み支援は、長文理解や抽象語を外部化する [[external-memory]] として扱える。ただし障害名で固定せず、読みにくい条件で使える選択肢として置く。^[raw/papers/arxiv-multilingual-text-to-pictogram-reading-rehabilitation-2026.md]
- **日内変動を前提にする**: EMA（日常場面での短い反復記録）は、症状を一回の質問紙だけでなく場面ごとに見る方法である。負荷が高すぎる記録は継続しないため、最小限の入力と自動化が必要になる。^[raw/papers/pubmed-adhd-ema-daily-life-adolescents-2026.md]
- **測定が介入になる場合を分ける**: Kennedyら（2024）は、小児科で治療中の青年90人に17日間・1日4回のEMAを行い、自己評価ADHD症状が期間内に低下し、直前のEMA回答後には症状評価が低くなる傾向を報告した。ただし対象は青年で、自己評価の短期変化であり、EMAを単独治療として一般化するのではなく、[[digital-adhd-support]]の一部として「短い自己観察がその場の気づきや調整を促すかもしれない」程度に読む。^[raw/papers/kennedy-2024-ema-perceived-adhd-symptoms-adolescents.md]

## 設計パターン

- [[digital-interruptions]] と合わせて、通知を消す/まとめる/予告する条件ごとに作業復帰を比べる。
- [[task-resumption]] と合わせて、中断前の場所、次の一手、戻るまでの時間を記録する。
- [[working-memory]] と合わせて、頭の中に保持していた項目数を、メモ、予定、画面表示へ逃がす。
- [[fear-of-missing-out]] と合わせて、見逃し不安が強い場面で「確認済み範囲」と「次回確認時刻」が効くかを見る。
- **通知を時刻つきの最小ログへ変える**: 1時間ごとの通知を時間境界の合図にして、その時点の行動を一枚の写真などで素早く残し、後から「何時に何をしていたか」を振り返る個人実践がある。細かな日記を毎回書く負荷を避けられる一方、撮影物には位置情報、室内、本人・第三者の情報が入り得る。記録範囲、共有先、保持期間を先に限定し、他者の監視用途にしない。単一のX投稿に基づく低信頼度の実践候補。^[raw/articles/tweet-2095384585760886934-setlog-hourly-photo-log.md]

## 文脈・感情労働・日常測定

Selinら（2026）は、自閉・ADHDを含む神経多様者がマスキング経験を視覚化し、少人数でセルフトラッキングを試した研究で、記録が自己洞察だけでなく解釈負荷や感情労働を生むことを示した。認知パーソナルインフォマティクスでは、測る対象を増やすより、本人が安全に読める形式、文脈を失わない記録、ピア共有の支えを設計する必要がある。^[raw/papers/selin-2026-self-tracking-masking-neurodivergent.md]

Rufら（2023）の成人ADHDを含むEMA研究は、食事、身体活動、状態衝動性の短時間関係を日常生活で測ろうとした例である。結果は食事成分と衝動性の単純な短時間関連を支持せず、EMAは「原因をすぐ特定する装置」ではなく、仮説の粒度・入力負荷・測定期間を慎重に設計する方法として扱う。^[raw/papers/ruf-2023-diet-physical-activity-impulsivity-adult-adhd-ema.md]

Mitchellら（2014）は、成人ADHDの喫煙者17人に7日間の電子日誌を使い、喫煙前後の状況を日常場面で測定した。喫煙は退屈、ストレス、心配、落ち着かなさ、他者の喫煙、アルコール/カフェイン摂取などと関連し、喫煙後には渇望・ネガティブ感情・ストレス・ADHD症状の自己評価が下がったと報告された。小規模で喫煙者に限られるため一般的なADHD支援とは分けるが、物質使用や[[emotion-regulation]]に関わる行動を、平均症状ではなく文脈・直前状態・直後変化として見るEMA設計例になる。^[raw/papers/mitchell-2014-ema-smoking-adults-adhd.md]

Carr（2026）のFielded Attentionは、注意を個人内の固定特性だけでなく、リズム、環境の手がかり、社会・物質的文脈との関係で生じるものとして捉える。これは[[attention-control]]や[[environment-design]]のページで扱う「注意を環境側にも分散する」発想を、概念面から補強する。^[raw/papers/carr-2026-fielded-attention-adhd-context.md, raw/papers/yi-2026-context-dependent-adhd-risk-coupling-commentary.md]

Raffaelliら（2025）は、発話思考課題と7日間EMAを組み合わせ、過活動症状が高い人では「思考への制約が弱い」場面に限って思考内容の変動性が高いと報告した。認知パーソナルインフォマティクスでは、注意や思考のばらつきを個人内の固定値として測るだけでなく、課題の制約、自由度、環境の手がかりを同時に記録する必要がある。^[raw/papers/raffaelli-2025-thought-content-variability-adhd-context.md]


## e-diary / JITAI と文脈に合わせた介入

Kochら（2021）は、ADHD研究でe-diaryやambulatory assessmentを使う意義を、症状の平均値ではなく時間的連鎖と環境トリガーを見る点に置いている。将来的なJITAIは、本人が困っている瞬間に短い支援を返す可能性を持つが、ADHD支援では「記録するほどよい」とは限らない。入力回数、通知のタイミング、センサー利用、他者への共有範囲を最小化し、[[digital-adhd-support]]と[[environment-design]]の境界で本人に役立つ文脈だけを戻す設計が必要になる。^[raw/papers/koch-2021-e-diaries-adhd-jitai-review.md]

Murrayら（2021）の成人EMA研究は、14日間の生活内感情データから、ADHD症状・感情調整・内在化症状の関係を一回の質問紙より細かく捉えようとした例である。設計上は、[[emotion-regulation]]を「気分を記録させる」だけにせず、本人がどの場面で不安・落ち込み・先延ばしに巻き込まれやすいかを安全に読み返せる形へ戻す必要がある。^[raw/papers/murray-2021-ema-emotional-dysregulation-adult-adhd-internalising.md]

## 注意点

認知状態の記録は、支援にも監視にもなりうる。学校・職場・家族が本人同意なしに行動ログを評価へ使うと害が大きい。ADHD 支援では、本人が自分の条件を知るための記録と、他者が監督するための記録を明確に分ける。

## 大学生のADHD症状・ストレスの日々の相互作用

Gohら（2026）は、ADHD関連の困りごとがある大学生187人を28日間EMAで追跡し、ADHD症状と知覚ストレスが同日・翌日・個人差の各レベルで正に関連すると報告した。とくに集中困難と先延ばしは翌日のストレス上昇に、ストレス側では「コントロールできていない感覚」が翌日のADHD症状上昇に関連した。これは因果や治療効果を断定するものではないが、[[emotion-regulation]]と[[task-initiation]]を別々に測るだけでなく、「先延ばし・集中困難・制御不能感」が悪循環の早期警戒シグナルになりうることを示す。^[raw/papers/goh-2026-day-to-day-adhd-stress-college-ema.md]


## 関連

- [[assistive-technology]]
- [[digital-adhd-support]]
- [[task-resumption]]
- [[digital-interruptions]]
- [[external-memory]]
- [[fear-of-missing-out]]
