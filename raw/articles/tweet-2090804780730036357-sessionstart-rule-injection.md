---
source_url: https://x.com/suna_gaku/status/2090804780730036357
ingested: 2026-08-21
sha256: 5a052edcf9bafc0482111d3ab412bff2f4f4ce2002168aea0b6a0f93b306b1c3
---
# X/Twitter post

- Author: スナガク | Codex 本発売予定（@suna_gaku）
- Created: 2026-08-21 14:14:39 UTC
- Metrics at collection: 3 likes / 0 reposts / 1 reply
- Tweet URL: https://x.com/suna_gaku/status/2090804780730036357

## 本文

Claude Code の返答を毎回の追加プロンプトで直す代わりに、`i-have-adhd` の SessionStart hook で「結論から書く」「次の行動を明確にする」「脱線しない」といったルールをセッション開始・再開時に Context へ自動注入するという紹介。人が指示を思い出して入力し続けなくても、返答形式を一定に保てるという実践例。

## 同スレッドの具体的な運用・注意点

返信（https://x.com/suna_gaku/status/2090804788501872726）は、ルールを「次の行動から始める」「複数手順は番号付き」「最後は具体的な次の一手」「箇条書きは5項目まで」のように実行可能な粒度へ分解すること、詳説を求めた時や破壊的操作の前には例外規則を置くことを挙げる。また、第三者プラグインがローカルのシェルスクリプトを自動実行するため、導入前にリポジトリと実行内容を確認するよう促している。

## 取り込みメモ

当事者／開発者による実務上の紹介であり、ADHDへの医療的・臨床的効果を示すものではない。情報設計・外部記憶・着手支援の実装例として扱う。