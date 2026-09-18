from pathlib import Path
W=Path('/var/lib/hermes/awesome-adhd')

def add_source(path, src):
    p=W/path
    s=p.read_text()
    if src in s:
        return s
    start=s.index('sources: [')
    end=s.index(']\n', start)
    return s[:end] + ', ' + src + s[end:]

def insert_before_heading(path, heading, text):
    p=W/path
    s=p.read_text()
    if text.strip() in s:
        return s
    idx=s.index(heading)
    return s[:idx].rstrip()+"\n"+text+"\n"+s[idx:]

def write_text(path, s):
    (W/path).write_text(s)

# work-routines
p=Path('concepts/work-routines.md')
s=add_source(p, 'raw/articles/tweet-2087887849819459834-morning-ninety-minute-defense-time.md')
needle='- **企画力と実行部分を分業する**: アイデアを量産できるが最後まで一人で実行し切れない場合、「企画を立てるな」ではなく、面倒な実行部分を人に任せる・テンプレート化する・自動化する前提で仕事を組む。才能を潰すより、実行を一人で全部背負う設計を潰すという発想。^[raw/articles/tweet-2087645349330698667-delegate-automate-execution.md]'
add='\n- **朝90分を防衛タイムにする**: メール・Slack・小タスクの完了感に報酬を吸われ、本命タスクが進まない場合、朝の90分だけはメールもチャットも開かない会議扱いの防衛枠にする。小タスク処理を「仕事している感」ではなく注意のハイジャックとして扱い、最初の高エネルギー時間を[[task-initiation]]が必要な重い仕事へ予約する。^[raw/articles/tweet-2087887849819459834-morning-ninety-minute-defense-time.md]'
if add.strip() not in s:
    s=s.replace(needle, needle+add)
write_text(p,s)

# task-initiation
p=Path('concepts/task-initiation.md')
s=add_source(p, 'raw/articles/tweet-2087887849819459834-morning-ninety-minute-defense-time.md')
needle='- **過去TODOを「他人の引き継ぎ」として読み直す**: 思いついた瞬間は面白かったアイデアが、1時間後にはやりたくないタスクへ変わる前提で、過去のTODOを「どこの誰かが残した中途半端な引き継ぎ」として距離を取って読む。しばらく強制的に触るうちに、そのTODO周辺の新しい着想が戻ることがある。AI利用時は、Claude Codeなどに細かい引き継ぎ書を書かせ、「優先度が高く、自分が忘れていそうなもの」をリマインドさせる。[[digital-adhd-support]]と[[external-memory]]を、着手の再点火に使う実践。^[raw/articles/tweet-2087783566897991746-stale-idea-ai-handover.md]'
add='\n- **朝の最初90分は本命タスク専用にする**: メール返信やSlack既読は短い完了報酬が強く、重いタスクの着手を横取りしやすい。始業直後90分だけ通知・メール・チャットを開かず、本命タスクを先に進める防衛枠を置くと、小タスクの達成感へ逃げる前に作業興奮を起こしやすい。[[work-routines]]側の集中枠設計としても扱う。^[raw/articles/tweet-2087887849819459834-morning-ninety-minute-defense-time.md]'
if add.strip() not in s:
    s=s.replace(needle, needle+add)
write_text(p,s)

# forgetfulness
p=Path('concepts/forgetfulness-countermeasures.md')
s=(W/p).read_text()
s=s.replace('updated: 2026-08-11','updated: 2026-08-13')
s=add_source(p, 'raw/articles/tweet-2087875589726175569-pay-receive-one-set-chant.md')
needle='- **毎回同じ順序で出発前チェックを固定する**: 「忘れたら困る場面」を出発前に想像し、その不安を自己責めではなくチェック行動の起動トリガーにする。持ち物確認は気分で思い出すのではなく、毎回同じ順序で必ずなぞる手順に固定する。ASD的な同一性保持を借りた当事者メモとして扱い、実装上はドア貼りチェックリストや玄関ランディングパッドと組み合わせる。^[raw/articles/tweet-2087185060562907424-fixed-sequence-departure-check.md]'
add='\n- **支払いと受け取りをワンセットで唱える**: コンビニやレジで「支払い」が完了した瞬間にタスク終了扱いになり、商品を受け取らず離れる問題に対して、「払う→受け取る」を一つの固定フレーズとして唱える。記憶力ではなく、レジ前の動作列を2工程セットに固定する[[external-memory]]寄りの忘れ物対策。^[raw/articles/tweet-2087875589726175569-pay-receive-one-set-chant.md]'
if add.strip() not in s:
    s=s.replace(needle, needle+add)
write_text(p,s)

# external-memory
p=Path('concepts/external-memory.md')
s=add_source(p, 'raw/articles/tweet-2087875589726175569-pay-receive-one-set-chant.md')
needle='- **「できた」メモで成功体験を外へ出す**: 失敗だけが記憶に残り、できたことは薄く消える前提で、スマホに「できた」というメモを1枚作り、寝る前1分でその日やれたことを3つ書く。歯磨きや返信1件のような小さい実績でよく、「遅かったけど」「当たり前だけど」の評価語を足さない。週1回読み返すことで、記憶されなかった実績を後から戻す。[[emotion-regulation]]にも関係するが、ここでは自己肯定感を気合で上げるのではなく記録で補う外部記憶として扱う。^[raw/articles/tweet-2087735907990597693-done-record-success-memory.md]'
add='\n- **工程を口に出して固定する**: レジの「払う→受け取る」のように、抜けやすい連続動作を短い唱え言葉にして外へ出す。チェックリストを貼るほどではない一瞬の場面でも、動作列を言語化すると「支払いで完了」といった誤った終了判定を補正しやすい。^[raw/articles/tweet-2087875589726175569-pay-receive-one-set-chant.md]'
if add.strip() not in s:
    s=s.replace(needle, needle+add)
write_text(p,s)

# index bytes preserve invalid chars if any
ip=W/'index.md'
s=ip.read_bytes().decode('utf-8','replace')
s=s.replace('メモ・場所・タイマー・人・AI・履歴を使い', 'メモ・場所・タイマー・人・AI・履歴・唱え言葉を使い')
s=s.replace('固定順序チェック、制服化などで外部化する実践集。','固定順序チェック、レジでの「払う→受け取る」唱和、制服化などで外部化する実践集。')
s=s.replace('セルフ実況、カフェ外出、', 'セルフ実況、朝90分の防衛枠、カフェ外出、')
s=s.replace('短時間集中、左右タスク分割、', '短時間集中、朝90分のメール/Slack遮断、左右タスク分割、')
ip.write_text(s)

lp=W/'log.md'
log=lp.read_text()
entry='''\n## [2026-08-13] ingest | X/Twitter ADHDパワー系ソリューション定期検索 37\n- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated candidates by tweet ID; skipped already-ingested tweets, generic empathy/diagnosis discourse, stigma/attacks, medical/supplement claims without source, duplicate tactics without new detail, self-promotion without enough workflow detail, and posts exposing unnecessary personal detail.\n- Created raw sources:\n  - `raw/articles/tweet-2087887849819459834-morning-ninety-minute-defense-time.md`\n  - `raw/articles/tweet-2087875589726175569-pay-receive-one-set-chant.md`\n- Updated concept/navigation pages:\n  - `concepts/work-routines.md`\n  - `concepts/task-initiation.md`\n  - `concepts/forgetfulness-countermeasures.md`\n  - `concepts/external-memory.md`\n  - `index.md`\n- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.\n'''
if '定期検索 37' not in log:
    lp.write_text(log.rstrip()+"\n"+entry)
print('updated pages and log')
