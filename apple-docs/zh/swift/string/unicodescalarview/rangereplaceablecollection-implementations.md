---
title: RangeReplaceableCollection 实现
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/unicodescalarview/rangereplaceablecollection-implementations
source_url: 'https://developer.apple.com/documentation/swift/string/unicodescalarview/rangereplaceablecollection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/unicodescalarview/rangereplaceablecollection-implementations.json'
content_hash: 'sha256:647f7e1d4371d095'
translated: true
---

> 导航：[技术](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [UnicodeScalarView](../unicodescalarview.md)

# RangeReplaceableCollection 实现

<sub>API 集合</sub>

## 主题

### 运算符

- [+(_:_:)](<+(____)-61ucr.md>) — 通过拼接一个序列和一个集合的元素，创建一个新的集合。
- [+(_:_:)](<+(____)-8g18j.md>) — 通过拼接一个集合和一个序列的元素，创建一个新的集合。
- [+(_:_:)](<+(____)-929xp.md>) — 通过拼接两个集合的元素，创建一个新的集合。
- [+=(_:_:)](<+=(____).md>) — 将一个序列的元素追加到某个范围可替换的集合（range‑replaceable collection）中。

### 初始化方法

- [init()](<init().md>) — 创建一个空的视图实例。
- [init(_:)](<init(__).md>) — 创建一个包含给定序列元素的新集合实例。
- [init(repeating:count:)](<init(repeating_count_).md>) — 创建一个包含指定数量重复值的新集合。

### 实例方法

- [append(_:)](<append(__).md>) — 将给定的 Unicode 标量追加到视图中。
- [append(_:)](<append(__)-5uy8n.md>) — 向集合末尾添加一个元素。
- [append(contentsOf:)](<append(contentsof_).md>) — 将给定序列中的 Unicode 标量值追加到视图中。
- [append(contentsOf:)](<append(contentsof_)-ton6.md>) — 将一个序列或集合的元素添加到当前集合的末尾。
- [applying(_:)](<applying(__).md>) — 将给定的差异（difference）应用到当前集合。
- [filter(_:)](<filter(__)-8zki.md>) — 返回一个同类型的新集合，其中按序包含原集合中满足给定谓词（predicate）的元素。
- [insert(_:at:)](<insert(__at_).md>) — 在集合的指定位置插入一个新元素。
- [insert(contentsOf:at:)](<insert(contentsof_at_).md>) — 在集合的指定位置插入一个序列的元素。
- [popLast()](<poplast().md>) — 移除并返回集合的最后一个元素。
- [remove(at:)](<remove(at_).md>) — 移除并返回指定位置的元素。
- [removeAll(keepingCapacity:)](<removeall(keepingcapacity_).md>) — 从集合中移除所有元素。
- [removeAll(where:)](<removeall(where_).md>) — 移除所有满足给定谓词的元素。
- [removeFirst()](<removefirst().md>) — 移除并返回集合的第一个元素。
- [removeFirst(_:)](<removefirst(__).md>) — 从集合开头移除指定数量的元素。
- [removeLast()](<removelast().md>) — 移除并返回集合的最后一个元素。
- [removeLast(_:)](<removelast(__).md>) — 从集合末尾移除指定数量的元素。
- [removeSubrange(_:)](<removesubrange(__)-62wlg.md>) — 从集合中移除指定子范围内的元素。
- [removeSubrange(_:)](<removesubrange(__)-6rv02.md>) — 从集合中移除指定子范围内的元素。
- [removeSubranges(_:)](<removesubranges(__).md>) — 移除指定索引处的元素。
- [replaceSubrange(_:with:)](<replacesubrange(__with_).md>) — 将指定范围内的元素替换为给定的 Unicode 标量值。
- [replaceSubrange(_:with:)](<replacesubrange(__with_)-5z8uw.md>) — 将指定子范围内的元素替换为给定的集合。
- [replaceSubrange(_:with:)](<replacesubrange(__with_)-914bq.md>) — 将指定子范围内的元素替换为给定的集合。 _(已废弃)_
- [reserveCapacity(_:)](<reservecapacity(__).md>) — 在视图的底层存储中预留足够的空间，以存储指定数量的 ASCII 字符。
- [reserveCapacity(_:)](<reservecapacity(__)-4ygoa.md>) — 在适当的情况下，为集合预留存储指定数量元素所需的空间。
