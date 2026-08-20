#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""重建 README.md，并把新页面插入 _unindexed/index.md。

README：§7 的固定 6 段，散文原样保留，数字重算。先做基线数据自证。
_unindexed/index.md：以 phase2 基线 ec0477976 的五段条目数切分 resource_type，
  段内按页面标题原始码位序。因段内已被翻译打乱，
  采用「保留旧行不动、按英文标题在非中文邻居之间插入」的方式，不重排旧行。

用法：buildroot.py <vault> <old_docs.json> <new_docs.json> [--write]
"""
import os, re, sys, json, urllib.parse
from collections import defaultdict, Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vaultlib import quote, main_platform, kebab, split_front
import buildtype as BT

RT_ORDER = ['Guide', 'QA', 'Release Note', 'Sample Code', 'Technical Note']
BASELINE_SEGMENTS = {
    'Guide': 9156,
    'QA': 1503,
    'Release Note': 2544,
    'Sample Code': 24794,
    'Technical Note': 798,
}
LINE = re.compile(r'^- \[(.*)\]\((.*)\)$')


# ----------------------------------------------------------------- README
def build_readme(vault, docs, prose, tips, npages):
    bytop = Counter(d['top'] for d in docs)
    byrt = Counter(d['resource_type'] for d in docs)
    byplat = Counter(main_platform(d['platform']) for d in docs)
    L = ['# Apple Developer Documentation Archive（Obsidian 版）', '', prose, '',
         '## 统计', '',
         '- 文档：%d 份' % len(docs),
         '- 页面：%d 个 Markdown 文件' % npages,
         '- 来源：https://developer.apple.com/library/archive/navigation/', '',
         '## 按归档分类浏览', '']
    for t in sorted(bytop):                       # 顶层目录名按原始 ASCII 序
        L.append('- [%s](_indexes/%s.md)（%d 份）' % (t, t, bytop[t]))
    L += ['', '## 按资源类型浏览', '']
    for rt in sorted(byrt, key=str.lower):
        L.append('- [%s](_indexes/by-type/%s.md)（%d 份）' % (rt, kebab(rt), byrt[rt]))
    L += ['', '## 按平台浏览', '']
    for p in sorted(byplat, key=str.lower):
        L.append('- [%s](_indexes/by-platform/%s.md)（%d 份）' % (p, kebab(p), byplat[p]))
    L += ['', '## 使用提示', ''] + tips
    return '\n'.join(L) + '\n'


def read_readme_parts(vault):
    t = open(os.path.join(vault, 'README.md'), encoding='utf-8').read()
    lines = t.split('\n')
    prose = lines[2]
    i = lines.index('## 使用提示')
    tips = [l for l in lines[i + 2:] if l.strip()]
    return prose, tips


def count_pages(vault):
    """§7「页面」= 全部 .md 减去 _indexes/、README.md、doc/、BACKFILL_REPORT.md。"""
    n = 0
    for dp, dn, fn in os.walk(vault):
        dn[:] = [d for d in dn if d != '.git']
        for f in fn:
            if not f.endswith('.md'):
                continue
            rel = os.path.relpath(os.path.join(dp, f), vault)
            if rel.startswith('_indexes/') or rel.startswith('doc/') \
                    or rel in ('README.md', 'BACKFILL_REPORT.md'):
                continue
            n += 1
    return n


# ------------------------------------------------------- _unindexed/index.md
CJK = BT.CJK


def merge_unindexed(vault, newdocs, oldblocks):
    p = os.path.join(vault, '_unindexed/index.md')
    lines = open(p, encoding='utf-8').read().split('\n')
    head = lines[:4]
    ent = []
    for l in lines[4:]:
        m = LINE.match(l)
        if m:
            ent.append((m.group(1), l))
    assert len(ent) == sum(BASELINE_SEGMENTS.values()), len(ent)
    segs = {}
    offset = 0
    for rt in RT_ORDER:
        count = BASELINE_SEGMENTS[rt]
        segs[rt] = ent[offset:offset + count]
        offset += count

    # 新页面：按 resource_type 分段，段内按 (标题, 文档序, 页序)
    newseg = defaultdict(list)
    for di, d in enumerate(sorted(newdocs, key=lambda x: x['title'])):
        pages = [d['entry']] + [s[1] for s in d['subs']]
        for pi, rel in enumerate(pages):
            newseg[d['resource_type']].append(
                (d['title'], di, pi, '- [%s](%s)' % (d['title'], quote('../' + rel))))
    for rt in newseg:
        newseg[rt].sort(key=lambda x: (x[0], x[1], x[2]))

    out = list(head)
    for rt in RT_ORDER:
        old = segs.get(rt, [])
        new = newseg.get(rt, [])
        if not old:
            out += [x[3] for x in new]
            continue
        # nextkey[i] = 位置 i 及其后第一个非中文条目的标题
        nk = [None] * (len(old) + 1)
        cur = None
        for i in range(len(old) - 1, -1, -1):
            if not CJK.search(old[i][0]):
                cur = old[i][0]
            nk[i] = cur
        j = 0
        for i, (t, l) in enumerate(old):
            bound = nk[i]
            while j < len(new) and (bound is None or new[j][0] < bound):
                out.append(new[j][3])
                j += 1
            out.append(l)
        while j < len(new):
            out.append(new[j][3])
            j += 1
    return '\n'.join(out) + '\n', len(ent), sum(len(v) for v in newseg.values())


def main():
    vault, oldf, newf = sys.argv[1], sys.argv[2], sys.argv[3]
    o = json.load(open(oldf))
    olddocs = o['docs']
    cat = {tuple(k.split('\t')): v for k, v in o['cat'].items()}
    for d in olddocs:
        pp = d['entry'].split('/')
        d['cat'] = pp[1] if len(pp) >= 3 and (pp[0], pp[1]) in cat else None
    newdocs = json.load(open(newf))['docs']
    prose, tips = read_readme_parts(vault)

    # --- README 自证：只用旧文档 + 旧页面数，应与仓库现有 README 完全一致 ---
    cur = open(os.path.join(vault, 'README.md'), encoding='utf-8').read()
    baseline_pages = int(re.search(
        r'^- 页面：(\d+) 个 Markdown 文件$', cur, re.M
    ).group(1))
    r_old = build_readme(vault, olddocs, prose, tips, baseline_pages)
    print('README 旧数据自证:', '一致' if r_old == cur else '不一致')
    if r_old != cur:
        import difflib
        for l in list(difflib.unified_diff(cur.split('\n'), r_old.split('\n'),
                                           'repo', 'gen', lineterm='', n=1))[:30]:
            print('   ' + l[:150])

    new_payload = json.load(open(newf))
    # README 的历史“页面”口径包含索引页；phase2 因此增加正文页和新分类索引页，
    # 但不计 doc/ 下的审计说明。
    npages = (
        baseline_pages
        + sum(d['pages'] for d in newdocs)
        + len(new_payload.get('new_cats', {}))
    )
    r_new = build_readme(vault, olddocs + newdocs, prose, tips, npages)
    print('新 README：文档 %d 份，页面 %d 个' % (len(olddocs) + len(newdocs), npages))

    oldblocks, _ = BT.parse_old_blocks(vault)
    u_new, nold, nnew = merge_unindexed(vault, newdocs, oldblocks)
    print('_unindexed/index.md：旧 %d 条 + 新 %d 条 = %d 条' % (nold, nnew, nold + nnew))
    got = sum(1 for l in u_new.split('\n') if LINE.match(l))
    print('   实际生成条目:', got, '（应为 %d）' % (nold + nnew))
    # 旧行是否全部原样保留且顺序不变
    oldlines = [l for l in open(os.path.join(vault, '_unindexed/index.md'),
                                encoding='utf-8').read().split('\n') if LINE.match(l)]
    newlines = [l for l in u_new.split('\n') if LINE.match(l)]
    oldset = set(oldlines)
    keep = [l for l in newlines if l in oldset]
    print('   旧行顺序保持不变:', keep == oldlines)

    if '--write' in sys.argv:
        open(os.path.join(vault, 'README.md'), 'w', encoding='utf-8').write(r_new)
        open(os.path.join(vault, '_unindexed/index.md'), 'w', encoding='utf-8').write(u_new)
        print('已写入 README.md 与 _unindexed/index.md')


if __name__ == '__main__':
    main()
