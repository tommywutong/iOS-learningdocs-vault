---
title: 集合
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/collections
source_url: 'https://developer.apple.com/documentation/swift/collections'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collections.json'
content_hash: 'sha256:1fdf42d889c08598'
translated: true
---

> 导航： [技术](../technologies.md) · [Swift](../swift.md) · [Swift 标准库](swift-standard-library.md)

# 集合

<sub>API 集合</sub>

使用数组、字典、Set 以及其他数据结构来存储和组织数据。

## 主题

### 数组与字典

- [Array](array.md) — 一种有序的、可随机访问的集合。
- [Dictionary](dictionary.md) — 一种元素为键值对的集合。
- [InlineArray](inlinearray.md) — 一种固定大小的数组。

### Set 类型

- [Set](set.md) — 一种由唯一元素组成的无序集合。
- [OptionSet](optionset.md) — 一种为位集合呈现数学化集合接口的类型。

### 区间

- [..\<(_:_:)](<comparable/'.._(____).md>) — 返回一个半开区间，包含其下界但不包含其上界。
- [Range](range.md) — 一个从下界到上界（但不包括上界）的半开区间。
- [RangeSet](rangeset.md) — 由任意可比较类型的值组成的集合，以区间形式表示。
- [...(_:_:)](<comparable/'...(____).md>) — 返回一个闭区间，同时包含其两端的边界。
- [ClosedRange](closedrange.md) — 一个从下界到上界（包括上界）的区间。

### 步进

- [stride(from:to:by:)](<stride(from_to_by_).md>) — 返回一个从起始值到（但不包括）结束值、按指定步长递增的序列。
- [stride(from:through:by:)](<stride(from_through_by_).md>) — 返回一个从起始值朝向（可能包括）结束值、按指定步长递增的序列。

### 特殊用途集合

- [repeatElement(_:count:)](<repeatelement(__count_).md>) — 创建一个包含指定数量给定元素的集合。
- [CollectionOfOne](collectionofone.md) — 一种只包含单个元素的集合。
- [EmptyCollection](emptycollection.md) — 一种元素类型为 `Element` 但始终为空的集合。
- [KeyValuePairs](keyvaluepairs.md) — 一种轻量级的键值对集合。
- [DictionaryLiteral](dictionaryliteral.md)

### 动态序列

- [sequence(first:next:)](<sequence(first_next_).md>) — 返回一个由 `first` 及对 `next` 反复进行惰性调用所构成的序列。
- [sequence(state:next:)](<sequence(state_next_).md>) — 返回一个由对可变 `state` 反复进行 `next` 惰性调用所构成的序列。

### 联合迭代

- [zip(_:_:)](<zip(____).md>) — 由两个底层序列创建一个由元素对组成的序列。

### 集合进阶主题

- [Sequence and Collection Protocols](sequence-and-collection-protocols.md) — 编写适用于任意集合的通用代码，或构建你自己的集合类型。
- [Supporting Types](supporting-types.md) — 在对集合进行切片、展平和反转等操作时，使用包装器、索引和迭代器。
- [Managed Buffers](managed-buffers.md) — 构建你自己的、由缓冲区支持的集合类型。

## 另请参阅

### 值与集合

- [Numbers and Basic Values](numbers-and-basic-values.md) — 使用数字、布尔值和其他基础类型为数据建模。
- [Strings and Text](strings-and-text.md) — 使用 Unicode 安全的字符串处理文本。
- [Time](time-and-duration.md) — 测量一次操作耗费的时长，并确定未来的时间安排。
