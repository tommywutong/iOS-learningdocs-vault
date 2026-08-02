#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从仓库现有的 _indexes/by-type/*.md 抽出基线文档记录，
再补上 topic（从文档入口页 frontmatter 读）。这是「旧文档清单」的权威来源，
因为 by-type 的 4 个文件正好覆盖 4,121 份文档、且每行都带完整元信息。
"""
import os, re, sys, json, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vaultlib import split_front, main_platform

ENTRY = re.compile(r'^- \*\*\[(.*)\]\((.*?)\)\*\* — (.+?) · (\d{4}-\d{2}-\d{2})，(.*)$')


def parse_meta_tail(tail):
    """'tvOS|iOS · UIKit，4 页' -> (platform, technology, pages)"""
    pages = 1
    m = re.search(r'，(\d+) 页$', tail)
    if m:
        pages = int(m.group(1))
        tail = tail[:m.start()]
    if ' · ' in tail:
        plat, tech = tail.split(' · ', 1)
    else:
        plat, tech = tail, None
    return plat, tech, pages


def load_old(vault):
    docs = []
    for fn, rt in (('guide.md', 'Guide'), ('qa.md', 'QA'),
                   ('release-note.md', 'Release Note'),
                   ('sample-code.md', 'Sample Code'),
                   ('technical-note.md', 'Technical Note')):
        p = os.path.join(vault, '_indexes/by-type', fn)
        for line in open(p, encoding='utf-8'):
            m = ENTRY.match(line.rstrip('\n'))
            if not m:
                continue
            title, href, rtype, pub, tail = m.groups()
            plat, tech, pages = parse_meta_tail(tail)
            rel = urllib.parse.unquote(href)
            assert rel.startswith('../../'), rel
            rel = rel[6:]
            docs.append(dict(title=title, entry=rel, resource_type=rtype,
                             published=pub, platform=plat, technology=tech,
                             pages=pages, new=False))
    return docs


def attach_topic(vault, docs):
    """topic 从入口页 frontmatter 读。"""
    miss = 0
    for d in docs:
        p = os.path.join(vault, d['entry'])
        if not os.path.exists(p):
            d['topic'] = None
            miss += 1
            continue
        raw, fm, body = split_front(open(p, encoding='utf-8').read())
        d['topic'] = (fm or {}).get('topic')
        d['apple_id'] = (fm or {}).get('apple_id')
    return miss


def top_and_cat(vault, entry, cat_ids):
    """(顶层目录, 分类目录名 or None, 分类 id or None)"""
    parts = entry.split('/')
    top = parts[0]
    if len(parts) >= 3 and (top, parts[1]) in cat_ids:
        return top, parts[1], cat_ids[(top, parts[1])]
    return top, None, None


def build_cat_ids(vault):
    """从 _indexes/<type>.md 的 '## [<目录名>](<type>/<id>.md)' 行反查 目录名->id。"""
    out = {}
    H = re.compile(r'^## \[(.*)\]\(([^/]+)/(.*)\.md\)（(\d+) 份）$')
    for fn in os.listdir(os.path.join(vault, '_indexes')):
        if not fn.endswith('.md'):
            continue
        top = fn[:-3]
        for line in open(os.path.join(vault, '_indexes', fn), encoding='utf-8'):
            m = H.match(line.rstrip('\n'))
            if m:
                assert m.group(2) == top, (fn, line)
                out[(top, m.group(1))] = m.group(3)
    return out


if __name__ == '__main__':
    vault = sys.argv[1]
    docs = load_old(vault)
    print('by-type 抽出文档数:', len(docs))
    miss = attach_topic(vault, docs)
    print('入口页文件缺失:', miss)
    import catmap
    cat = catmap.build(vault)
    print('分类映射条数:', len(cat))
    from collections import Counter
    c = Counter()
    for d in docs:
        t, cn, ci = top_and_cat(vault, d['entry'], cat)
        d['top'], d['cat'], d['cat_id'] = t, cn, ci
        c[(t, cn)] += 1
    print('顶层×分类 组数:', len(c))
    json.dump({'docs': docs, 'cat': {'%s\t%s' % k: v for k, v in cat.items()}},
              open(sys.argv[2], 'w'), ensure_ascii=False)
