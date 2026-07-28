---
title: 集合
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/collections
source_url: 'https://developer.apple.com/documentation/foundation/collections'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/collections.json'
content_hash: 'sha256:871b91fc285d94f5'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md)

# 集合

<sub>API 集合</sub>

使用数组、字典、集合和专用集合来存储并迭代对象组或值组。

## 主题

### 基本集合

- [Array](../swift/array.md) — 一个有序、可随机访问的集合。
- [Dictionary](../swift/dictionary.md) — 一个元素为键值对的集合。
- [Set](../swift/set.md) — 一个由唯一元素组成的无序集合。

### 索引

- [IndexPath](indexpath.md) — 一个索引列表，列表中的索引共同表示嵌套数组树中特定位置的路径。
- [IndexSet](indexset.md) — 一个由唯一整数值组成的集合，这些整数表示另一个集合中元素的索引。

### 专用集合

- [NSCountedSet](nscountedset.md) — 一个可变的无序集合，其中的不同对象可以在集合中出现多次。
- [NSOrderedSet](nsorderedset.md) — 一个静态的、有序的唯一对象集合。
- [NSMutableOrderedSet](nsmutableorderedset.md) — 一个动态的、有序的唯一对象集合。

### 可清除集合

- [NSCache](nscache.md) — 一个可变集合，用于临时存储短暂的键值对；当资源不足时，这些键值对可能会被逐出。
- [NSPurgeableData](nspurgeabledata.md) — 一个包含字节的可变数据对象，当不再需要这些字节时可将其丢弃。

### 指针集合

- [NSPointerArray](nspointerarray.md) — 一个类似于数组的集合，但提供了更广泛的内存语义。
- [NSMapTable](nsmaptable.md) — 一个类似于字典的集合，但提供了更广泛的内存语义。
- [NSHashTable](nshashtable.md) — 一个类似于集合的集合，但提供了更广泛的内存语义。

### 迭代

- [NSEnumerator](nsenumerator.md) — 一个抽象类，其子类枚举数组和字典等对象集合。
- [NSFastEnumeration](nsfastenumeration.md) — 对象为支持快速枚举而采用的协议。
- [NSFastEnumerationIterator](nsfastenumerationiterator.md)
- [NSIndexSetIterator](nsindexsetiterator.md) — 一个适合枚举索引集元素的迭代器。
- [NSEnumerationOptions](nsenumerationoptions.md) — block 枚举操作的选项。
- [NSSortOptions](nssortoptions.md) — block 排序操作的选项。

### 特殊语义值

- [NSNull](nsnull.md) — 一个单例对象，用于在不允许 `nil` 值的集合对象中表示空值。
- [NSNotFound](nsnotfound-9t5v2.md)
- [NSNotFound](nsnotfound-4qp9h.md) — 一个值，表示找不到或不存在请求的项目。

## 另请参阅

### 基础概念

- [数值、数据与基本值](numbers-data-and-basic-values.md) — 处理 Cocoa 中广泛使用的基本值和其他基础类型。
- [字符串与文本](strings-and-text.md) — 创建并处理 Unicode 字符串，使用正则表达式查找模式，以及对文本执行自然语言分析。
- [日期与时间](dates-and-times.md) — 比较日期和时间，以及执行日历和时区计算。
- [单位与测量](units-and-measurement.md) — 使用物理维度标记数值量，以便进行适应区域设置的格式化以及相关单位之间的转换。
- [数据格式化](data-formatting.md) — 在数值、日期、测量结果及其他值与适应区域设置的字符串表示形式之间进行转换。
- [过滤与排序](filters-and-sorting.md) — 使用谓词、表达式和排序描述符检查集合及其他服务中的元素。
