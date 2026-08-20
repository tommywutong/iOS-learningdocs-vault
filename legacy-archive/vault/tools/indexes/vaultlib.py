#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""旧仓库格式的共用工具：frontmatter 解析、sanitize、导航行、平台优先级、URL 编码。

全部规则来自 meta/recon/VAULT_FORMAT_SPEC.md（§1/§2/§4/§6/§9）。
"""
import os, re, io, sys, yaml, base64, urllib.parse
from collections import OrderedDict

FM_KEYS = ['title', 'apple_id', 'resource_type', 'platform', 'topic',
           'technology', 'published', 'source_url', 'archived_at']

# §1.3 platform 书写顺序（frontmatter 里从左到右）
PLATFORM_WRITE_ORDER = ['watchOS', 'tvOS', 'iAd System JS', 'Safari (Mobile)', 'Safari',
                        'CloudKit JS', 'iAd Producer', 'Java', 'iOS',
                        'Xcode Developer Tools', 'macOS']
# §6.4 索引分组用的主平台优先级
PLATFORM_MAIN_PRIORITY = ['iOS', 'macOS', 'watchOS', 'tvOS', 'Xcode Developer Tools',
                          'Java', 'Safari', 'CloudKit JS', 'Safari (Mobile)',
                          'iAd Producer', 'iAd System JS']

NAV_PREFIX = '> 导航：'
SEP = ' · '


# ---------------------------------------------------------------- frontmatter
def split_front(text):
    """返回 (raw_fm_without_fences, data_dict, body)。不是文档页则返回 (None, None, text)。"""
    if not text.startswith('---\n'):
        return None, None, text
    end = text.find('\n---\n', 3)
    if end < 0:
        return None, None, text
    raw = text[4:end + 1]
    body = text[end + 5:]
    try:
        data = yaml.safe_load(raw)
    except Exception:
        data = None
    return raw, data, body


def dump_front(data):
    """按 §13.1 复现旧仓库的 frontmatter 序列化。"""
    return yaml.safe_dump(OrderedDict((k, data[k]) for k in FM_KEYS),
                          sort_keys=False, allow_unicode=True,
                          default_flow_style=False)


# 让 safe_dump 支持 OrderedDict
yaml.SafeDumper.add_representer(
    OrderedDict,
    lambda d, m: d.represent_mapping('tag:yaml.org,2002:map', m.items()))


# ------------------------------------------------------------------- sanitize
def sanitize(name):
    """§2.4"""
    s = re.sub(r'<[^>]*>', '', name)
    s = re.sub(r'[_*#]', '', s)
    s = re.sub(r'[<>:"/\\|?\[\]]', '-', s)
    s = re.sub(r'\s+', ' ', s).strip()
    s = s[:80]
    s = s.rstrip(' .-')
    return s


# ------------------------------------------------------------------------ nav
def nav_line(depth, top, doc_title=None, entry_file=None):
    """§4.1 / §13.3"""
    up = '../' * depth
    s = '%s[总目录](%sREADME.md)%s[%s](%s_indexes/%s.md)' % (
        NAV_PREFIX, up, SEP, top, up, top)
    if doc_title is not None and entry_file is not None:
        s += '%s[%s](%s)' % (SEP, doc_title, quote(entry_file))
    return s


def quote(p):
    """§9.2  urllib.parse.quote 默认 safe='/'"""
    return urllib.parse.quote(p)


def anchor(apple_ref):
    """§8.8"""
    return 'apple-' + base64.b32encode(apple_ref.encode()).decode().lower().rstrip('=')


# -------------------------------------------------------------------- platform
def main_platform(platform):
    toks = platform.split('|')
    for p in PLATFORM_MAIN_PRIORITY:
        if p in toks:
            return p
    return toks[0]


def platform_order_ok(platform):
    toks = platform.split('|')
    try:
        idx = [PLATFORM_WRITE_ORDER.index(t) for t in toks]
    except ValueError:
        return False
    return idx == sorted(idx)


# ------------------------------------------------------------------ 索引排序
def sort_key(title):
    """索引条目排序键。旧仓库观察：按 title 的码位序（区分大小写），见 verify_sort()。"""
    return title


def kebab(s):
    return s.lower().replace(' ', '-')


# ------------------------------------------------------------------ 文件遍历
def iter_md(root, skip=('.git',)):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in skip]
        for fn in sorted(filenames):
            if fn.endswith('.md'):
                p = os.path.join(dirpath, fn)
                yield os.path.relpath(p, root), p
