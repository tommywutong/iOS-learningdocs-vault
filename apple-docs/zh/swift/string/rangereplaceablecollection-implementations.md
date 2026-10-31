---
title: RangeReplaceableCollection 实现
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/rangereplaceablecollection-implementations
source_url: 'https://developer.apple.com/documentation/swift/string/rangereplaceablecollection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/rangereplaceablecollection-implementations.json'
content_hash: 'sha256:53c8cd3ec4d90b86'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# RangeReplaceableCollection 实现

<sub>API 集合</sub>

## 主题

### 运算符

- [+(_:_:)](<+(____)-6h59y.md>) — 通过拼接一个序列和一个集合的元素，创建一个新的集合。
- [+(_:_:)](<+(____)-9fm57.md>) — 通过拼接两个集合的元素，创建一个新的集合。
- [+(_:_:)](<+(____)-n329.md>) — 通过拼接一个集合和一个序列的元素，创建一个新的集合。
- [+=(_:_:)](<+=(____)-676gx.md>) — 将一个序列的元素追加到 range-replaceable collection 中。

### 初始化方法

- [init(_:)](<init(__)-1ip93.md>) — 创建一个新的集合实例，其中包含一个序列的元素。
- [init(_:)](<init(__)-8og6g.md>) — 创建一个包含给定序列中字符的新字符串。
- [init(repeating:count:)](<init(repeating_count_)-11bpi.md>) — 创建一个表示给定字符重复指定次数的字符串。
- [init(repeating:count:)](<init(repeating_count_)-5y5em.md>) — 创建一个新的集合，其中包含指定数量的单个重复值。

### 实例方法

- [append(_:)](<append(__)-1re5n.md>) — 向集合末尾添加一个元素。
- [append(_:)](<append(__)-4xi3j.md>) — 将给定的字符追加到字符串。
- [append(contentsOf:)](<append(contentsof_)-7est5.md>) — 将给定序列中的字符追加到字符串。
- [append(contentsOf:)](<append(contentsof_)-9foms.md>) — 将一个序列或集合的元素添加到此集合的末尾。
- [applying(_:)](<applying(__).md>) — 将给定的差异应用到该集合。
- [filter(_:)](<filter(__)-66nw7.md>) — 返回一个同类型的新集合，其中按顺序包含原集合中满足给定谓词的元素。
- [insert(_:at:)](<insert(__at_).md>) — 在指定位置插入一个新字符。
- [insert(_:at:)](<insert(__at_)-88yqh.md>) — 在集合的指定位置插入一个新元素。
- [insert(contentsOf:at:)](<insert(contentsof_at_).md>) — 在指定位置插入一个字符集合。
- [insert(contentsOf:at:)](<insert(contentsof_at_)-rdu9.md>) — 将一个序列的元素插入到集合的指定位置。
- [popLast()](<poplast().md>) — 移除并返回集合的最后一个元素。
- [remove(at:)](<remove(at_).md>) — 移除并返回指定位置的字符。
- [remove(at:)](<remove(at_)-5g0wm.md>) — 移除并返回指定位置上的元素。
- [removeAll(keepingCapacity:)](<removeall(keepingcapacity_).md>) — 用空字符串替换此字符串。
- [removeAll(keepingCapacity:)](<removeall(keepingcapacity_)-6xw7h.md>) — 移除集合中的所有元素。
- [removeAll(where:)](<removeall(where_).md>) — 移除所有满足给定谓词的元素。
- [removeFirst()](<removefirst().md>) — 移除并返回集合的第一个元素。
- [removeFirst(_:)](<removefirst(__).md>) — 从集合开头移除指定数量的元素。
- [removeLast()](<removelast().md>) — 移除并返回集合的最后一个元素。
- [removeLast(_:)](<removelast(__).md>) — 从集合末尾移除指定数量的元素。
- [removeSubrange(_:)](<removesubrange(__).md>) — 移除给定范围内的字符。
- [removeSubrange(_:)](<removesubrange(__)-8maxn.md>) — 从集合中移除指定子范围内的元素。
- [removeSubrange(_:)](<removesubrange(__)-9twng.md>) — 从集合中移除指定子范围内的元素。
- [removeSubranges(_:)](<removesubranges(__).md>) — 移除给定索引处的元素。
- [replaceSubrange(_:with:)](<replacesubrange(__with_).md>) — 用给定的字符替换指定边界内的文本。
- [replaceSubrange(_:with:)](<replacesubrange(__with_)-3hkd6.md>) — 用给定的集合替换指定子范围内的元素。 _(已废弃)_
- [replaceSubrange(_:with:)](<replacesubrange(__with_)-72947.md>) — 用给定的集合替换指定子范围内的元素。
- [reserveCapacity(_:)](<reservecapacity(__).md>) — 在字符串的底层存储中预留足够的空间，以存储指定数量的 ASCII 字符。
- [reserveCapacity(_:)](<reservecapacity(__)-8lw57.md>) — 在底层类型适用的情况下，为集合预留存储指定数量元素所需的空间。
