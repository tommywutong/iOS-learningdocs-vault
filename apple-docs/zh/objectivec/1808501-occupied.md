---
title: occupied
framework: Objective-C Runtime
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/1808501-occupied
source_url: 'https://developer.apple.com/documentation/objectivec/1808501-occupied'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/1808501-occupied.json'
content_hash: 'sha256:93d653657c4b0908'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md) · [Objective-C Runtime](objective-c-runtime.md) · [objc_cache](objc_cache.md)

# occupied

<sub>文章</sub>

一个整数，指定已占用的缓存桶（cache bucket）总数。

## See Also

### Fields

- [mask](1808499-mask.md) — 一个整数，指定已分配的缓存桶总数（减一）。在方法查找过程中，Objective-C runtime 用这个字段来确定从 `buckets` 数组的哪个索引开始进行线性搜索。方法选择器（selector）的指针会用逻辑 AND 运算与这个字段做掩码运算（`index = (mask & selector))`）。这相当于一个简单的哈希算法。
- [buckets](1808503-buckets.md) — 一个指向 [Method](method.md) 数据结构的指针数组。这个数组最多包含 `mask + 1` 个条目。注意指针可能为 `NULL`，表示该缓存桶未被占用，且已占用的桶不一定是连续的。这个数组会随时间增长。
