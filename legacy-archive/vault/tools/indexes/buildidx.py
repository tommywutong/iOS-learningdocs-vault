#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""重建 _indexes/by-type/*.md 与 _indexes/by-platform/*.md。

先用「仅旧文档」重建并与仓库现有字节 diff，证明生成器正确；再带上新文档重建。
用法：buildidx.py <vault> <old_docs.json> [--write] [--with-new <new_docs.json>]
"""
import os, re, sys, json, difflib, urllib.parse
from collections import defaultdict, OrderedDict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vaultlib import quote, main_platform, kebab
import catmap

THRESH = 20


def entry_line(d, depth):
    """§6.2 文档条目行。depth = 索引文件所在目录相对 vault 根的层数。"""
    href = quote('../' * depth + d['entry'])
    s = '- **[%s](%s)** — %s · %s，%s' % (d['title'], href, d['resource_type'],
                                         d['published'], d['platform'])
    if d.get('technology'):
        s += ' · ' + d['technology']
    if d.get('pages', 1) != 1:
        s += '，%d 页' % d['pages']
    return s


def sk(t):
    return t.lower()


CJK = re.compile(r'[　-鿿＀-￯]')


def eng(d):
    """已翻译文档的原始英文名（= 文档目录名 / 文件 stem）。索引生成时用的是英文标题，
    翻译只改了标签不改位置，所以复现排序必须回到英文名。"""
    parts = d['entry'].split('/')
    parent = parts[-2] if len(parts) >= 2 else None
    if parent and parent != d['top'] and parent != d.get('cat'):
        return parent
    return parts[-1][:-3]


def key(d):
    return sk(eng(d) if CJK.search(d['title']) else d['title'])


DOCLINE = re.compile(r'^- \*\*\[(.*)\]\((.*?)\)\*\* — ')


def ordered(vault, index_rel, depth, docs):
    """保持既有条目顺序不动，只把新条目按英文排序键插入。"""
    by_entry = {d['entry']: d for d in docs}
    old = []
    path = os.path.join(vault, index_rel)
    if os.path.exists(path):
        for line in open(path, encoding='utf-8'):
            m = DOCLINE.match(line.rstrip('\n'))
            if not m:
                continue
            rel = urllib.parse.unquote(m.group(2))
            prefix = '../' * depth
            if rel.startswith(prefix) and rel[len(prefix):] in by_entry:
                old.append(by_entry.pop(rel[len(prefix):]))
    new = sorted(by_entry.values(), key=key)
    out = []
    j = 0
    for item in old:
        while j < len(new) and key(new[j]) < key(item):
            out.append(new[j])
            j += 1
        out.append(item)
    out.extend(new[j:])
    return out


def head(title, nav, total):
    return ['# ' + title, '', '> 导航：' + nav, '', '共 %d 份文档。' % total]


# ------------------------------------------------------------------ by-type
def build_by_type(vault, docs):
    out = {}
    byrt = defaultdict(list)
    for d in docs:
        byrt[d['resource_type']].append(d)
    for rt, ds in byrt.items():
        index_rel = '_indexes/by-type/%s.md' % kebab(rt)
        groups = defaultdict(list)
        for d in ds:
            groups[main_platform(d['platform'])].append(d)
        L = head(rt, '[总目录](../../README.md)', len(ds))
        for plat in sorted(groups, key=sk):
            L += ['', '## %s（%d 份）' % (plat, len(groups[plat])), '']
            L += [entry_line(d, 2) for d in ordered(
                vault, index_rel, 2, groups[plat]
            )]
        out[index_rel] = '\n'.join(L) + '\n'
    return out


# -------------------------------------------------------------- by-platform
def build_by_platform(vault, docs, cat_ids, cat_labels):
    out = {}
    byp = defaultdict(list)
    for d in docs:
        byp[main_platform(d['platform'])].append(d)
    for plat, ds in byp.items():
        index_rel = '_indexes/by-platform/%s.md' % kebab(plat)
        L = head(plat, '[总目录](../../README.md)', len(ds))
        bytop = defaultdict(list)
        for d in ds:
            bytop[d['top']].append(d)
        for top in sorted(bytop):  # 顶层目录名按原始 ASCII 序（README 同序）
            tds = bytop[top]
            L += ['', '## %s（%d 份）' % (top, len(tds)), '']
            has_cat = any(d.get('cat') for d in tds)
            if has_cat:
                bycat = defaultdict(list)
                other = []
                for d in tds:
                    (bycat[d['cat']] if d.get('cat') else other).append(d)
                for cat in sorted(bycat, key=sk):
                    cds = bycat[cat]
                    label = cat_labels.get((top, cat), cat)
                    L += ['### [%s](../%s/%s.md)（%d 份）' % (
                        label, top, cat_ids[(top, cat)], len(cds)), '']
                    L += emit_topic(
                        cds, 2, '####',
                        lambda items: ordered(vault, index_rel, 2, items),
                    )
                    L += ['']
                if other:
                    L += ['### 其他', '']
                    L += emit_topic(
                        other, 2, '####',
                        lambda items: ordered(vault, index_rel, 2, items),
                    )
                    L += ['']
                while L and L[-1] == '':
                    L.pop()
            else:
                L += emit_topic(
                    tds, 2, '###',
                    lambda items: ordered(vault, index_rel, 2, items),
                )
        out[index_rel] = '\n'.join(L) + '\n'
    return out


def emit_topic(ds, depth, hlevel, order):
    """≥ THRESH 时按 topic 分子组，否则直接列条目。"""
    if len(ds) < THRESH:
        return [entry_line(d, depth) for d in order(ds)]
    bytopic = defaultdict(list)
    for d in ds:
        bytopic[d['topic'] or '未分类主题'].append(d)
    L = []
    for t in sorted(bytopic, key=sk):
        L += ['%s %s（%d 份）' % (hlevel, t, len(bytopic[t])), '']
        L += [entry_line(d, depth) for d in order(bytopic[t])]
        L += ['']
    L.pop()
    return L


# ------------------------------------------------------------------- 主流程
def main():
    vault, oldf = sys.argv[1], sys.argv[2]
    data = json.load(open(oldf))
    docs = data['docs']
    cat_ids = catmap.build(vault)
    cat_labels = catmap.labels(vault)
    newdocs = []
    if '--with-new' in sys.argv:
        nj = json.load(open(sys.argv[sys.argv.index('--with-new') + 1]))
        newdocs = nj['docs']
        for k_, v in nj['new_cats'].items():
            cat_ids[tuple(k_.split('\t'))] = v
        for d in newdocs:
            if d.get('cat'):
                cat_ids[(d['top'], d['cat'])] = d['cat_id']
    for d in docs:
        pp = d['entry'].split('/')
        d['cat'] = pp[1] if len(pp) >= 3 and (pp[0], pp[1]) in cat_ids else None
    all_docs = docs + newdocs
    built = {}
    built.update(build_by_type(vault, all_docs))
    built.update(build_by_platform(vault, all_docs, cat_ids, cat_labels))
    write = '--write' in sys.argv
    nd = 0
    for rel, txt in sorted(built.items()):
        p = os.path.join(vault, rel)
        old = open(p, encoding='utf-8').read() if os.path.exists(p) else ''
        if old == txt:
            print('  ==  %s' % rel)
        else:
            nd += 1
            print('  !=  %s  (旧 %d 字节 / 新 %d 字节)' % (rel, len(old), len(txt)))
            if not newdocs:
                d = list(difflib.unified_diff(old.split('\n'), txt.split('\n'),
                                              'old', 'new', lineterm='', n=1))
                for l in d[:40]:
                    print('      ' + l[:160])
        if write:
            open(p, 'w', encoding='utf-8').write(txt)
    print('差异文件数:', nd, '/', len(built))


if __name__ == '__main__':
    main()
