#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 phase2 来源报告与 plans.json 构造尚未进入现有索引的新文档记录。"""
import os, re, sys, json
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vaultlib import split_front, sanitize, main_platform

H1 = re.compile(r'^#+ +(.*)$', re.M)


def dispname(stem, h1):
    """索引子页显示名：H1 去 <tag>、去 _ *（不去 #），不折空白不截断；对不上文件名则退回 stem。"""
    if h1:
        c = re.sub(r'<[^>]*>', '', h1)
        c = re.sub(r'[_*]', '', c)
        s = sanitize(c)
        base = re.sub(r'-\d+$', '', stem)
        if s == stem or s == base:
            return c
    return stem


def main(vault, plansf, sourcesf, oldf, out):
    plans = json.load(open(plansf))
    sources = json.load(open(sourcesf))['documents']
    old_aids = {d.get('apple_id') for d in json.load(open(oldf))['docs']}
    # 旧仓库已有的 分类目录名 -> 分类 id
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import catmap
    cat_ids = catmap.build(vault)

    docs = []
    tn_cats = {}
    for aid, source in sorted(sources.items()):
        if source.get('status') == 'unresolved' or aid in old_aids:
            continue
        if aid in plans:
            rels = plans[aid]['rels']
        elif source.get('paths'):
            rels = source['paths']
        elif source.get('path'):
            rels = [source['path']]
        else:
            raise AssertionError((aid, source))
        entry = rels[0]
        p = os.path.join(vault, entry)
        raw, fm, body = split_front(open(p, encoding='utf-8').read())
        parts = entry.split('/')
        top = parts[0]
        # 已有分类映射优先；新分类要求至少有 type/cat/doc/page 四段。
        cat = parts[1] if len(parts) >= 2 and (top, parts[1]) in cat_ids else None
        if cat is None and len(parts) >= 4:
            cat = parts[1]
        cat_id = None
        if cat:
            if (top, cat) in cat_ids:
                cat_id = cat_ids[(top, cat)]
            else:
                # 新分类（technotes）：id 取自源 URL 第二段
                cat_id = fm['source_url'].split('/library/archive/', 1)[1].split('/')[1]
                cat_ids[(top, cat)] = cat_id
                tn_cats[(top, cat)] = cat_id
        subs = []
        for r in rels[1:]:
            stem = os.path.basename(r)[:-3]
            t = open(os.path.join(vault, r), encoding='utf-8').read()
            m = H1.search(t)
            subs.append([dispname(stem, m.group(1).strip() if m else None), r])
        docs.append(dict(title=fm['title'], entry=entry, resource_type=fm['resource_type'],
                         published=fm['published'], platform=fm['platform'],
                         technology=fm['technology'], topic=fm['topic'],
                         pages=len(rels), apple_id=aid, top=top, cat=cat,
                         cat_id=cat_id, subs=subs, new=True))
    json.dump({'docs': docs, 'new_cats': {'%s\t%s' % k: v for k, v in tn_cats.items()}},
              open(out, 'w'), ensure_ascii=False)

    print('新文档:', len(docs), ' 页数合计:', sum(d['pages'] for d in docs))
    print('按顶层:', dict(Counter(d['top'] for d in docs)))
    print('按 resource_type:', dict(Counter(d['resource_type'] for d in docs)))
    print('新分类:', len(tn_cats))
    for k, v in sorted(tn_cats.items()):
        n = sum(1 for d in docs if (d['top'], d['cat']) == k)
        print('   %-12s -> %-10s %3d 份' % (k[1], v, n))
    print()
    print('== 受影响的 索引分组 ==')
    print('顶层×分类:', dict(Counter((d['top'], d['cat']) for d in docs)))
    print('by-type × 主平台:', dict(Counter((d['resource_type'], main_platform(d['platform']))
                                          for d in docs)))
    print('by-platform × 顶层:', dict(Counter((main_platform(d['platform']), d['top'])
                                            for d in docs)))
    # 子页显示名自检
    bad = [(d['entry'], s) for d in docs for s in d['subs']
           if sanitize(s[0]) != os.path.basename(s[1])[:-3]
           and sanitize(s[0]) != re.sub(r'-\d+$', '', os.path.basename(s[1])[:-3])]
    print('子页显示名 sanitize 回不到文件名的:', len(bad), bad[:3])


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
