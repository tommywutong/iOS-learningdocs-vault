---
title: objc_cache
framework: Objective-C Runtime
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/objc_cache
source_url: 'https://developer.apple.com/documentation/objectivec/objc_cache'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_cache.json'
content_hash: 'sha256:ab8136a837e769ac'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md) · [Objective-C Runtime](objective-c-runtime.md)

# objc_cache

针对方法调用的性能优化。包含指向最近使用过的方法的指针。

## 概述

为了减少对常用方法定义进行线性搜索的需要——这种操作会显著拖慢方法查找的速度——Objective-C runtime 函数会将该类最近调用过的方法的定义指针存储在一个 `objc_cache` 数据结构中。

## 主题

### Fields

- [mask](1808499-mask.md) — 一个整数，指定已分配的缓存桶总数（减一）。在方法查找过程中，Objective-C runtime 用这个字段来确定从 `buckets` 数组的哪个索引开始进行线性搜索。方法选择器（selector）的指针会用逻辑 AND 运算与这个字段做掩码运算（`index = (mask & selector))`）。这相当于一个简单的哈希算法。
- [occupied](1808501-occupied.md) — 一个整数，指定已占用的缓存桶总数。
- [buckets](1808503-buckets.md) — 一个指向 [Method](method.md) 数据结构的指针数组。这个数组最多包含 `mask + 1` 个条目。注意指针可能为 `NULL`，表示该缓存桶未被占用，且已占用的桶不一定是连续的。这个数组会随时间增长。

## 另请参阅

### Class-Definition Data Structures

- [Method](method.md) — 一个不透明类型，表示类定义中的一个方法。
- [Ivar](ivar.md) — 一个不透明类型，表示一个实例变量。
- [Category](category.md) — 一个不透明类型，表示一个分类。
- [objc_property_t](objc_property_t.md) — 一个不透明类型，表示一个 Objective-C 声明的属性。
- [IMP](imp.md) — 一个指向方法实现起始位置的指针。
- [objc_method_description](objc_method_description.md) — 定义一个 Objective-C 方法。
- [objc_property_attribute_t](objc_property_attribute_t.md) — 定义一个属性特性。
