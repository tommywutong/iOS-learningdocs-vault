---
title: RangeReplaceableCollection 实现
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/slice/rangereplaceablecollection-implementations
source_url: 'https://developer.apple.com/documentation/swift/slice/rangereplaceablecollection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/slice/rangereplaceablecollection-implementations.json'
content_hash: 'sha256:0686d2d57ae1ad6e'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [集合](../collections.md) · [支持类型](../supporting-types.md) · [Slice](../slice.md)

# RangeReplaceableCollection 实现

<sub>API 集合</sub>

## 主题

### 运算符

- [+(_:_:)](<+(____)-298al.md>) — 通过拼接一个集合和一个序列的元素，创建一个新的集合。
- [+(_:_:)](<+(____)-4resp.md>) — 通过拼接一个序列和一个集合的元素，创建一个新的集合。
- [+(_:_:)](<+(____)-99wuu.md>) — 通过拼接两个集合的元素，创建一个新的集合。
- [+=(_:_:)](<+=(____).md>) — 将一个序列的元素追加到某个范围可替换的集合（range‑replaceable collection）中。

### 初始化方法

- [init()](<init().md>) — 创建一个新的、空的集合。
- [init(_:)](<init(__).md>) — 创建一个包含序列元素的新集合实例。
- [init(_:)](<init(__)-81eoy.md>) — 创建一个包含序列元素的新集合实例。
- [init(repeating:count:)](<init(repeating_count_).md>) — 创建一个包含指定数量重复值的新集合。
- [init(repeating:count:)](<init(repeating_count_)-6ps2q.md>) — 创建一个包含指定数量重复值的新集合。

### 实例方法

- [append(_:)](<append(__).md>) — 向集合末尾添加一个元素。
- [append(contentsOf:)](<append(contentsof_).md>) — 将一个序列或集合的元素添加到当前集合的末尾。
- [applying(_:)](<applying(__).md>) — 将给定的差异（difference）应用到当前集合。
- [filter(_:)](<filter(__)-9rk6d.md>) — 返回一个同类型的新集合，其中按序包含原集合中满足给定谓词（predicate）的元素。
- [insert(_:at:)](<insert(__at_)-6sg0.md>) — 在集合的指定位置插入一个新元素。
- [insert(_:at:)](<insert(__at_)-8i1dc.md>) — 在集合的指定位置插入一个新元素。
- [insert(contentsOf:at:)](<insert(contentsof_at_)-25pep.md>) — 在集合的指定位置插入一个序列的元素。
- [insert(contentsOf:at:)](<insert(contentsof_at_)-2xj4m.md>) — 在集合的指定位置插入一个序列的元素。
- [popLast()](<poplast()-30m9y.md>) — 移除并返回集合的最后一个元素。
- [popLast()](<poplast()-4rely.md>) — 移除并返回集合的最后一个元素。
- [remove(at:)](<remove(at_)-7ep9e.md>) — 移除并返回指定位置的元素。
- [remove(at:)](<remove(at_)-7xja6.md>) — 移除并返回指定位置的元素。
- [removeAll(keepingCapacity:)](<removeall(keepingcapacity_).md>) — 从集合中移除所有元素。
- [removeAll(where:)](<removeall(where_)-26lr3.md>) — 移除所有满足给定谓词的元素。
- [removeAll(where:)](<removeall(where_)-9u7g.md>) — 移除所有满足给定谓词的元素。
- [removeFirst()](<removefirst()-1iayr.md>) — 移除并返回集合的第一个元素。
- [removeFirst()](<removefirst()-3eija.md>) — 移除并返回集合的第一个元素。
- [removeFirst(_:)](<removefirst(__)-1pxgx.md>) — 从集合开头移除指定数量的元素。
- [removeFirst(_:)](<removefirst(__)-7hjja.md>) — 从集合开头移除指定数量的元素。
- [removeLast()](<removelast()-5mmgh.md>) — 移除并返回集合的最后一个元素。
- [removeLast()](<removelast()-wsbc.md>) — 移除并返回集合的最后一个元素。
- [removeLast(_:)](<removelast(__)-75mgx.md>) — 从集合末尾移除指定数量的元素。
- [removeLast(_:)](<removelast(__)-fxm2.md>) — 从集合末尾移除指定数量的元素。
- [removeSubrange(_:)](<removesubrange(__)-1y2qo.md>) — 从集合中移除指定子范围内的元素。
- [removeSubrange(_:)](<removesubrange(__)-7s7x9.md>) — 从集合中移除指定子范围内的元素。
- [removeSubrange(_:)](<removesubrange(__)-8m66i.md>) — 从集合中移除指定子范围内的元素。
- [removeSubranges(_:)](<removesubranges(__)-2ncra.md>) — 移除指定索引处的元素。
- [replaceSubrange(_:with:)](<replacesubrange(__with_)-8l6gb.md>) — 将指定子范围内的元素替换为给定的集合。 _(已废弃)_
- [replaceSubrange(_:with:)](<replacesubrange(__with_)-9le44.md>) — 将指定子范围内的元素替换为给定的集合。
- [replaceSubrange(_:with:)](<replacesubrange(__with_)-zwfk.md>) — 将指定子范围内的元素替换为给定的集合。
- [reserveCapacity(_:)](<reservecapacity(__).md>) — 在适当的情况下，为集合预留存储指定数量元素所需的空间。
