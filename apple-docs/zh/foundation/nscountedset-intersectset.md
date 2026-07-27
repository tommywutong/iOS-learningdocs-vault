---
title: 'intersectSet:'
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscountedset-intersectset
source_url: 'https://developer.apple.com/documentation/foundation/nscountedset-intersectset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscountedset-intersectset.json'
content_hash: 'sha256:8907966766b750df'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [集合](collections.md) · [NSCountedSet](nscountedset.md)

# intersectSet:

<sub>文章</sub>

从接收集合中移除不在另一个给定集合中的每个对象。

## 概述

对于接收集合中不存在于 `otherSet` 的每个对象，此方法会减少该对象的计数；如果计数变为 0，则从接收集合中移除该对象。

## 另请参阅

### 相关文档

- [NSCountedSet](nscountedset.md) — 一种可变的无序集合，其中包含的不同对象可以出现多次。
