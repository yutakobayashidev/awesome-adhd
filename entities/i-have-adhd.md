---
title: i-have-adhd
created: 2026-07-22
updated: 2026-07-23
type: entity
tags: [adhd, tool, accessibility, executive-function, working-memory, work]
sources: [raw/articles/i-have-adhd-github-2026.md, raw/articles/i-have-adhd-agent-output-skill-2026.md]
confidence: medium
---

# i-have-adhd

`i-have-adhd` は、コーディング用エージェントの返答をADHDのある読者が実行しやすい形へ寄せる skill / plugin。答えを前置きや長い説明の中に埋めず、次の行動、番号つき手順、現在地、具体的な時間見積もりを見える位置に置く。

これは医療的な支援ではなく、[[assistive-technology]] と [[external-memory]] の間にある情報設計の道具として扱う。ADHD症状を改善する根拠ではなく、LLMや開発支援道具の出力を読みやすく・動きやすくする実装例である。^[raw/articles/i-have-adhd-github-2026.md]

## 何を変えるか

中心の考え方は、読む側の[[working-memory]]と[[task-initiation]]の負荷を下げること。

- 最初に「次に何をするか」を置く。
- 複数手順は番号つきにし、1手順を小さくする。
- 返答の最後に、2分以内にできる次の行動を1つだけ置く。
- 横道や挨拶を減らし、完了したことを目に見える形で示す。
- エラーは原因・場所・直し方を淡々と書く。

## 対応面

READMEとインストール文書では、Claude Code、Codex、Zed、Hermes、Gemini、Cursor、Antigravityなどのエージェント環境で使う方法が示されている。Claude Codeでは `/i-have-adhd` で呼び出し、任意で `~/.claude/.i-have-adhd-always` を作ると SessionStart hook が常時読み込む。

## 評価の姿勢

誤投入側から移した `i-have-adhd-agent-output-skill-2026` は、この道具を agent の文章出力契約として見る補助資料である。単なる短文化ではなく、answer-first、番号つき手順、次の一手、余談抑制、見える完了を出力形式へ固定する点が重要である。^[raw/articles/i-have-adhd-agent-output-skill-2026.md]


リポジトリには `evals/` があり、正確さ、自律性、実行しやすさ、安全性、簡潔さで返答品質を評価する方針がある。これは「短ければよい」ではなく、正確さや安全性を落とさず、行動に移しやすい返答へ寄せるという設計意図を示している。

## 注意点

- ADHDの診断や治療に関する道具ではない。
- 出力形式の工夫であり、効果検証済みの臨床介入ではない。
- 常時有効化は便利だが、説明を深く求める場面では例外規則が必要になる。
- 破壊的操作や曖昧な依頼では、短さより安全確認を優先する。

## 関連

- [[assistive-technology]]
- [[external-memory]]
- [[working-memory]]
- [[task-initiation]]
- [[work-routines]]
- [[executive-function]]
