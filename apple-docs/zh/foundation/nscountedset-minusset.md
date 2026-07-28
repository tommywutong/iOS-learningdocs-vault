---
title: 'minusSet:'
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscountedset-minusset
source_url: 'https://developer.apple.com/documentation/foundation/nscountedset-minusset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscountedset-minusset.json'
content_hash: 'sha256:4a2235bb30816b62'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [集合](collections.md) · [NSCountedSet](nscountedset.md)

# minusSet:

<sub>文章</sub>

如果另一个给定集合中的对象存在于接收集合中，则从接收集合中移除这些对象。

## 概述

对于 `otherSet` 中存在于接收集合的每个对象，此方法会减少该对象的计数；如果计数变为 0，则从接收集合中移除该对象。

## 另请参阅

### 相关文档

- [NSCountedSet](nscountedset.md) — 一种可变的无序集合，其中包含的不同对象可以出现多次。
