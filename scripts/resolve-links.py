#!/usr/bin/env python3
"""
リポジトリ root の Wiki コンテンツ → content/ へコピーしつつ、
[[wikilink]] を Quartz が解決できるパスに変換する。

元スクリプト: dd2030-wiki の scripts/resolve-links.py（wiki/ ディレクトリ前提）。
このリポジトリでは root 自体が Wiki なので、WIKI_INCLUDE の許可リストにある
ファイル/ディレクトリだけを content/ にコピーする形に適応させている。
新しいコンテンツ用ディレクトリを追加したら WIKI_INCLUDE にも追加すること。

処理:
1. WIKI_INCLUDE 配下の全 .md ファイルをスキャンし、title と aliases から名前→パスの対応表を構築
2. 全ファイルを content/ にコピーしつつ、[[リンク名]] を [[相対パス|リンク名]] に変換
3. 対応するページが存在しないリンクはそのまま残す（プレーンテキスト化）

編集は常に root 側のファイルに対して行い、content/ は直接編集しない
（自動生成物。gitignore 済み）。
"""

import os
import re
import shutil
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
CONTENT_DIR = os.path.join(REPO_ROOT, 'content')

# 公開対象（root からの相対パス。ファイルまたはディレクトリ）
WIKI_INCLUDE = [
    'index.md',
    'log.md',
    'SCHEMA.md',
    'concepts',
    'entities',
    'comparisons',
    'queries',
    'raw',
]


def iter_wiki_files(root, includes):
    """公開対象の全ファイルパスを yield する"""
    for entry in includes:
        path = os.path.join(root, entry)
        if os.path.isfile(path):
            yield path
        elif os.path.isdir(path):
            for dirpath, dirs, files in os.walk(path):
                dirs.sort()
                for fname in sorted(files):
                    yield os.path.join(dirpath, fname)


def extract_frontmatter(filepath):
    """ファイルからYAMLフロントマターを抽出"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if not content.startswith('---'):
        return {}, content
    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        fm = {}
    return fm, content


def build_link_map():
    """
    名前 → 相対パス（拡張子なし）の対応表を構築。

    以下の名前でマッチする:
    - ファイル名（拡張子なし）: e.g. "external-memory" → "concepts/external-memory"
    - title: e.g. "外部記憶" → "concepts/external-memory"
    - aliases の各エントリ
    """
    link_map = {}

    for filepath in iter_wiki_files(REPO_ROOT, WIKI_INCLUDE):
        if not filepath.endswith('.md'):
            continue

        rel_path = os.path.relpath(filepath, REPO_ROOT)
        # 拡張子を除去し、パス区切りを / に統一
        slug = rel_path.replace(os.sep, '/').removesuffix('.md')

        # ファイル名（拡張子なし）
        basename = os.path.basename(filepath).removesuffix('.md')
        link_map[basename] = slug

        # フロントマターから title と aliases を取得
        fm, _ = extract_frontmatter(filepath)

        if fm.get('title'):
            link_map[fm['title']] = slug

        for alias in (fm.get('aliases') or []):
            link_map[alias] = slug

    return link_map


def resolve_wikilinks(content, link_map, current_slug):
    """
    [[リンク名]] → [[解決済みパス|リンク名]] に変換。
    [[パス|表示名]] 形式は既に解決済みとしてスキップ。
    """
    def replace_link(match):
        inner = match.group(1)

        # 既に [[path|display]] 形式の場合
        if '|' in inner:
            path_part, display = inner.split('|', 1)
            # path_part がlink_mapにある場合はパスに変換
            if path_part in link_map:
                resolved = link_map[path_part]
                return f'[[{resolved}|{display}]]'
            # path_part が既にパスっぽい場合はそのまま
            return match.group(0)

        # [[リンク名]] 形式
        link_name = inner.strip()

        if link_name in link_map:
            resolved = link_map[link_name]
            # 自分自身へのリンクはそのまま
            if resolved == current_slug:
                return f'**{link_name}**'
            # 表示名がファイル名と同じならパスだけでOK
            if link_name == resolved.split('/')[-1]:
                return f'[[{resolved}]]'
            return f'[[{resolved}|{link_name}]]'

        # 対応するページがない場合はプレーンテキストに
        return link_name

    return re.sub(r'\[\[([^\]]+)\]\]', replace_link, content)


def main():
    # link_map を構築
    link_map = build_link_map()

    print(f"Link map ({len(link_map)} entries):")
    for name, slug in sorted(link_map.items()):
        print(f"  {name} → {slug}")
    print()

    # content/ をクリーンアップ
    if os.path.exists(CONTENT_DIR):
        shutil.rmtree(CONTENT_DIR)
    os.makedirs(CONTENT_DIR, exist_ok=True)

    # root の公開対象 → content/ にコピーしつつリンク解決
    file_count = 0

    for src in iter_wiki_files(REPO_ROOT, WIKI_INCLUDE):
        rel = os.path.relpath(src, REPO_ROOT)
        dst = os.path.join(CONTENT_DIR, rel)
        fname = os.path.basename(src)

        os.makedirs(os.path.dirname(dst), exist_ok=True)

        if fname.endswith('.md'):
            with open(src, 'r', encoding='utf-8') as f:
                content = f.read()

            slug = rel.replace(os.sep, '/').removesuffix('.md')
            new_content = resolve_wikilinks(content, link_map, slug)

            with open(dst, 'w', encoding='utf-8') as f:
                f.write(new_content)

            file_count += 1
        else:
            shutil.copy2(src, dst)

    print(f"Processed {file_count} markdown files")
    print(f"Output: {CONTENT_DIR}")

    # 検証: content/ 内の未解決リンク（対応するファイルが存在しないもの）を報告
    print("\nValidation - checking for broken links:")
    broken = []
    for root, dirs, files in os.walk(CONTENT_DIR):
        for fname in files:
            if not fname.endswith('.md'):
                continue
            filepath = os.path.join(root, fname)
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read()
            for m in re.finditer(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', text):
                link_target = m.group(1)
                target_path = os.path.join(CONTENT_DIR, link_target + '.md')
                if not os.path.exists(target_path):
                    rel_file = os.path.relpath(filepath, CONTENT_DIR)
                    broken.append((rel_file, link_target))

    if broken:
        print(f"  WARNING: {len(broken)} broken link(s) found:")
        for src_file, target in broken:
            print(f"    {src_file} → [[{target}]]")
    else:
        print("  All links valid!")


if __name__ == '__main__':
    main()
