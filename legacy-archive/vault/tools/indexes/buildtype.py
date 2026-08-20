#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""重建 _indexes/<type>.md 与 _indexes/<type>/<cat>.md。

旧文档的「条目行 + 子页行」整块从现有索引里原样取出（子页顺序无法从产物推导），
新文档的块现场生成。先做「仅旧文档」的字节 diff 自证，再带新文档写盘。

用法：buildtype.py <vault> <old_docs.json> <new_docs.json> [--write]
"""
import os, re, sys, json, urllib.parse
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vaultlib import quote, main_platform
import catmap

THRESH = 20
CJK = re.compile(r'[　-鿿＀-￯]')
DOCLINE = re.compile(r'^- \*\*\[(.*)\]\((.*?)\)\*\* — ')
SUBLINE = re.compile(r'^  - \[')
# 无分类层的顶层目录
NOCAT = {'samplecode', 'featuredarticles', 'recipes', 'ApplePay_Guide', 'LucidDreams'}


def eng(d):
    """已翻译文档的原始英文名（= 文档目录名 / 文件 stem），用于复现索引排序。"""
    parts = d['entry'].split('/')
    parent = parts[-2] if len(parts) >= 2 else None
    if parent and parent != d['top'] and parent != d.get('cat'):
        return parent
    return parts[-1][:-3]


def key(d):
    return (eng(d) if CJK.search(d['title']) else d['title']).lower()


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


def entry_line(d, depth):
    href = quote('../' * depth + d['entry'])
    s = '- **[%s](%s)** — %s · %s，%s' % (d['title'], href, d['resource_type'],
                                         d['published'], d['platform'])
    if d.get('technology'):
        s += ' · ' + d['technology']
    if d.get('pages', 1) != 1:
        s += '，%d 页' % d['pages']
    return s


def block(d, depth, oldblocks):
    """文档块 = 条目行 + 子页行。旧文档原样复用。"""
    if not d.get('new'):
        return list(oldblocks[(depth, d['entry'])])
    L = [entry_line(d, depth)]
    for disp, rel in d['subs']:
        L.append('  - [%s](%s)' % (disp, quote('../' * depth + rel)))
    return L


def parse_old_blocks(vault):
    """从现有 _indexes/<type>.md 与 <type>/<cat>.md 抽出 (depth, entry) -> 块行。"""
    out = {}
    extra = {}
    base = os.path.join(vault, '_indexes')
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = [d for d in dirnames if not d.startswith('by-')]
        for fn in filenames:
            if not fn.endswith('.md'):
                continue
            p = os.path.join(dirpath, fn)
            depth = os.path.relpath(p, base).count('/') + 1
            lines = open(p, encoding='utf-8').read().split('\n')
            i = 0
            while i < len(lines):
                m = DOCLINE.match(lines[i])
                if not m:
                    i += 1
                    continue
                rel = urllib.parse.unquote(m.group(2))
                rel = rel[3 * depth:]
                blk = [lines[i]]
                j = i + 1
                while j < len(lines) and SUBLINE.match(lines[j]):
                    blk.append(lines[j])
                    j += 1
                out[(depth, rel)] = blk
                i = j
    # documentation.md 的「## 未编入索引的页面」段原样保留
    p = os.path.join(base, 'documentation.md')
    lines = open(p, encoding='utf-8').read().split('\n')
    if '## 未编入索引的页面' in lines:
        k = lines.index('## 未编入索引的页面')
        seg = lines[k:]
        while seg and seg[-1] == '':
            seg.pop()
        extra['documentation'] = seg
    return out, extra


def platform_groups(ds):
    g = defaultdict(list)
    for d in ds:
        g[main_platform(d['platform'])].append(d)
    return g


def build(vault, alldocs, oldblocks, extra, cat_ids, cat_labels):
    out = {}
    bytop = defaultdict(list)
    for d in alldocs:
        bytop[d['top']].append(d)
    for top, ds in bytop.items():
        # ---------- 二级分类索引 ----------
        bycat = defaultdict(list)
        nocat = []
        for d in ds:
            (bycat[d['cat']] if d.get('cat') else nocat).append(d)
        for cat, cds in bycat.items():
            index_rel = '_indexes/%s/%s.md' % (top, cat_ids[(top, cat)])
            L = ['# %s / %s' % (top, cat), '',
                 '> 导航：[总目录](../../README.md) · [%s](../%s.md)' % (top, top), '',
                 '共 %d 份文档。' % len(cds), '']
            if len(cds) >= THRESH:
                g = platform_groups(cds)
                for plat in sorted(g, key=str.lower):
                    L += ['## %s（%d 份）' % (plat, len(g[plat])), '']
                    for d in ordered(vault, index_rel, 2, g[plat]):
                        L += block(d, 2, oldblocks)
                    L += ['']
                L.pop()
            else:
                for d in ordered(vault, index_rel, 2, cds):
                    L += block(d, 2, oldblocks)
            out[index_rel] = '\n'.join(L) + '\n'

        # ---------- 一级类型索引 ----------
        L = ['# %s' % top, '', '> 导航：[总目录](../README.md)', '',
             '共 %d 份文档。' % len(ds), '']
        index_rel = '_indexes/%s.md' % top
        if bycat:
            for cat in sorted(bycat, key=str.lower):
                label = cat_labels.get((top, cat), cat)
                L += ['## [%s](%s/%s.md)（%d 份）' % (
                    label, top, cat_ids[(top, cat)], len(bycat[cat])), '']
        if nocat:
            L += ['## 文档', '']
            if len(nocat) >= THRESH:   # 与是否有分类层无关，只看无分类文档数
                g = platform_groups(nocat)
                for plat in sorted(g, key=str.lower):
                    L += ['### %s（%d 份）' % (plat, len(g[plat])), '']
                    for d in ordered(vault, index_rel, 1, g[plat]):
                        L += block(d, 1, oldblocks)
                    L += ['']
                L.pop()
            else:
                for d in ordered(vault, index_rel, 1, nocat):
                    L += block(d, 1, oldblocks)
        if top in extra:
            L += [''] + extra[top]
        while L and L[-1] == '':
            L.pop()
        out[index_rel] = '\n'.join(L) + '\n'
    return out


def main():
    vault, oldf, newf = sys.argv[1], sys.argv[2], sys.argv[3]
    o = json.load(open(oldf))
    olddocs = o['docs']
    cat_ids = catmap.build(vault)
    cat_labels = catmap.labels(vault)
    n = json.load(open(newf))
    newdocs = n['docs']
    for k_, v in n['new_cats'].items():
        cat_ids[tuple(k_.split('\t'))] = v
    # 新文档的分类目录名 -> id（technotes 之外的沿用旧映射）
    for d in newdocs:
        if d.get('cat') and (d['top'], d['cat']) not in cat_ids:
            cat_ids[(d['top'], d['cat'])] = d['cat_id']
    oldblocks, extra = parse_old_blocks(vault)
    print('抽出旧文档块:', len(oldblocks))

    withnew = '--write' in sys.argv or '--with-new' in sys.argv
    docs = olddocs + (newdocs if withnew else [])
    built = build(vault, docs, oldblocks, extra, cat_ids, cat_labels)
    nd = 0
    for rel, txt in sorted(built.items()):
        p = os.path.join(vault, rel)
        old = open(p, encoding='utf-8').read() if os.path.exists(p) else None
        if old == txt:
            print('  ==  %s' % rel)
        else:
            nd += 1
            tag = '新建' if old is None else '旧 %d / 新 %d 字节' % (len(old), len(txt))
            print('  !=  %s  (%s)' % (rel, tag))
            if not withnew and old is not None:
                import difflib
                for l in list(difflib.unified_diff(old.split('\n'), txt.split('\n'),
                                                   'old', 'new', lineterm='', n=1))[:24]:
                    print('      ' + l[:150])
    print('差异文件数:', nd, '/', len(built))
    if '--write' in sys.argv:
        for rel, txt in built.items():
            p = os.path.join(vault, rel)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            open(p, 'w', encoding='utf-8').write(txt)
        print('已写入', len(built), '个文件')


if __name__ == '__main__':
    main()
