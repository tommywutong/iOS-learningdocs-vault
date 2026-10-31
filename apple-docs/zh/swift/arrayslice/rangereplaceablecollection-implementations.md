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
doc_path: /documentation/swift/arrayslice/rangereplaceablecollection-implementations
source_url: 'https://developer.apple.com/documentation/swift/arrayslice/rangereplaceablecollection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/arrayslice/rangereplaceablecollection-implementations.json'
content_hash: 'sha256:07c8e9f7378c82f8'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md) · [ArraySlice](../arrayslice.md)

# RangeReplaceableCollection 实现

<sub>API 集合</sub>

## 主题

### 运算符

- [+(_:_:)](<+(____)-2jvah.md>) — 通过连接两个集合的元素创建一个新集合。
- [+(_:_:)](<+(____)-3xq1b.md>) — 通过连接一个序列和一个集合的元素创建一个新集合。
- [+(_:_:)](<+(____)-8elcw.md>) — 通过连接一个集合和一个序列的元素创建一个新集合。
- [+=(_:_:)](<+=(____).md>) — 将一个序列的元素追加到某个范围可替换的集合（range‑replaceable collection）中。

### 初始化方法

- [init()](<init().md>) — 创建一个新的空数组。
- [init(_:)](<init(__)-4qauj.md>) — 创建一个包含序列元素的新集合实例。
- [init(repeating:count:)](<init(repeating_count_).md>) — 创建一个新数组，包含指定数量的单个重复值。
- [init(repeating:count:)](<init(repeating_count_)-95f9t.md>) — 创建一个新集合，包含指定数量的单个重复值。

### 实例方法

- [append(_:)](<append(__).md>) — 在数组末尾添加一个新元素。
- [append(_:)](<append(__)-88nog.md>) — 向集合末尾添加一个元素。
- [append(contentsOf:)](<append(contentsof_).md>) — 将一个序列的元素添加到数组末尾。
- [append(contentsOf:)](<append(contentsof_)-6pxfb.md>) — 将一个序列或集合的元素添加到此集合的末尾。
- [applying(_:)](<applying(__).md>) — 将给定的差异（difference）应用到当前集合。
- [filter(_:)](<filter(__)-95o1l.md>) — 返回一个与原集合相同类型的新集合，按顺序包含原集合中满足给定谓词的元素。
- [insert(_:at:)](<insert(__at_)-2orxu.md>) — 在集合的指定位置插入一个新元素。
- [insert(contentsOf:at:)](<insert(contentsof_at_).md>) — 将一个序列的元素插入到集合的指定位置。
- [popLast()](<poplast()-225tk.md>) — 移除并返回集合的最后一个元素。
- [popLast()](<poplast()-ftzx.md>) — 移除并返回集合的最后一个元素。
- [remove(at:)](<remove(at_)-8p8nf.md>) — 移除并返回指定位置处的元素。
- [removeAll(keepingCapacity:)](<removeall(keepingcapacity_).md>) — 移除数组中的所有元素。
- [removeAll(keepingCapacity:)](<removeall(keepingcapacity_)-1wh07.md>) — 移除集合中的所有元素。
- [removeAll(where:)](<removeall(where_)-10tcx.md>) — 移除所有满足给定谓词的元素。
- [removeAll(where:)](<removeall(where_)-23c5i.md>) — 移除所有满足给定谓词的元素。
- [removeFirst()](<removefirst()-60cu4.md>) — 移除并返回集合的第一个元素。
- [removeFirst()](<removefirst()-svki.md>) — 移除并返回集合的第一个元素。
- [removeFirst(_:)](<removefirst(__)-285s6.md>) — 从集合开头移除指定数量的元素。
- [removeFirst(_:)](<removefirst(__)-3up7n.md>) — 从集合开头移除指定数量的元素。
- [removeLast()](<removelast()-67p7c.md>) — 移除并返回集合的最后一个元素。
- [removeLast()](<removelast()-9iuw9.md>) — 移除并返回集合的最后一个元素。
- [removeLast(_:)](<removelast(__)-33c55.md>) — 从集合末尾移除指定数量的元素。
- [removeLast(_:)](<removelast(__)-5oepe.md>) — 从集合末尾移除指定数量的元素。
- [removeSubrange(_:)](<removesubrange(__)-2zu9f.md>) — 从集合中移除指定子范围内的元素。
- [removeSubrange(_:)](<removesubrange(__)-celt.md>) — 从集合中移除指定子范围内的元素。
- [removeSubranges(_:)](<removesubranges(__)-947o4.md>) — 移除指定索引处的元素。
- [replaceSubrange(_:with:)](<replacesubrange(__with_).md>) — 用指定集合中的元素替换一个范围内的元素。
- [replaceSubrange(_:with:)](<replacesubrange(__with_)-5g1qk.md>) — 将指定子范围内的元素替换为给定的集合。
- [replaceSubrange(_:with:)](<replacesubrange(__with_)-9rz4g.md>) — 将指定子范围内的元素替换为给定的集合。 _(已废弃)_
- [reserveCapacity(_:)](<reservecapacity(__)-11kse.md>) — 在适当的情况下，为集合预留存储指定数量元素所需的空间。
