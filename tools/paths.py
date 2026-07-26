#!/usr/bin/env python3
"""路径规范化——fetch.py 与 render.py 共用，两边必须完全一致。

为什么单独抽一个模块：缓存文件名由 fetch.py 生成、由 render.py 查找，输出的
md 文件名又同时是链接目标。任何一处规则不一致，都会表现为「缓存明明抓到了但
渲染说缺文件」或者「链接指向一个不存在的文件」，而且都是静默出错。

三条规则，缺一不可：

1. **统一小写**。Apple 的 index 端点给全小写路径，但页面内 references 有 21%
   带大写。macOS 文件系统大小写不敏感所以本地看不出问题，一推到 Linux/GitHub
   上链接就全断。
2. **替换文件系统非法字符**。Apple 路径里有 7,000 多个冒号（`init(a:b:)` 这种
   Swift 方法签名），冒号在 Windows 上非法，会导致仓库无法 checkout。
3. **限制单个路径组件长度**。macOS/Linux 的单组件上限是 255 字节，而 Apple 有
   像 `init(animationtool:colorprimaries:...:spatialvideoc-j1vm)` 这样的方法，
   百分号编码后能超过 400 字节，直接 OSError。超长的截断后拼哈希保证唯一。
"""
from __future__ import annotations

import hashlib
import re
import urllib.parse
from pathlib import Path

# Windows 非法字符（冒号占绝大多数）
ILLEGAL = r'[<>:"\\|?*]'

# 单个路径组件的字节上限。取 180 而不是 255，留出余量给 `.json.tmp` 这类后缀，
# 以及未来可能加的 `.zh.md` 之类。
MAX_COMPONENT = 180
# 截断后保留的字节数，剩下的位置留给 `-<10位哈希>`
KEEP = 160


def _fit(component: str, original: str) -> str:
    """把超长组件截断并拼上原始内容的哈希，保证唯一且可复现。"""
    if len(component.encode("utf-8")) <= MAX_COMPONENT:
        return component
    digest = hashlib.sha256(original.encode("utf-8")).hexdigest()[:10]
    # 按字节截断后用 ignore 解码，避免把多字节字符切成半个
    head = component.encode("utf-8")[:KEEP].decode("utf-8", "ignore")
    return f"{head}-{digest}"


def safe_rel(doc_path: str) -> str:
    """/documentation/uikit/uiapplicationdelegate/application(_:options:)
       → uikit/uiapplicationdelegate/application(__options_)

    产出仓库内的相对路径（不含 .md 后缀）。既用于输出文件名，也用于生成链接目标，
    所以必须是纯函数。
    """
    rel = doc_path.removeprefix("/documentation/").strip("/").lower()
    parts = []
    for raw in rel.split("/"):
        parts.append(_fit(re.sub(ILLEGAL, "_", raw), raw))
    return "/".join(parts)


def cache_rel(archive: str, doc_path: str) -> Path:
    """缓存里的相对路径：<archive>/<百分号编码的各级组件>.json

    这里刻意用百分号编码而不是 safe_rel——缓存要能无损还原原始路径，便于排查
    「这个 json 对应线上哪一页」。已经抓下来的几万个文件也是这个规则，不能改。
    """
    rel = doc_path.removeprefix("/documentation/").strip("/")
    parts = []
    for raw in rel.split("/"):
        parts.append(_fit(urllib.parse.quote(raw, safe=""), raw))
    return Path(archive) / (("/".join(parts)) + ".json")
