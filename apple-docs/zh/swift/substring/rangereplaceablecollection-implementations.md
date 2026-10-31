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
doc_path: /documentation/swift/substring/rangereplaceablecollection-implementations
source_url: 'https://developer.apple.com/documentation/swift/substring/rangereplaceablecollection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/substring/rangereplaceablecollection-implementations.json'
content_hash: 'sha256:61d8f95e41bb290e'
translated: true
---

> 导航： [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md) · [Substring](../substring.md)

# RangeReplaceableCollection 实现

<sub>API 集合</sub>

## 主题

### 运算符

- [+(_:_:)](<+(____)-6h592.md>) — 通过拼接一个序列和一个集合的元素，创建一个新的集合。
- [+(_:_:)](<+(____)-9fm63.md>) — 通过拼接两个集合的元素，创建一个新的集合。
- [+(_:_:)](<+(____)-n335.md>) — 通过拼接一个集合和一个序列的元素，创建一个新的集合。
- [+=(_:_:)](<+=(____).md>) — 将一个序列的元素追加到 range-replaceable collection 中。

### 初始化方法

- [init(_:)](<init(__)-1ip9z.md>) — 创建一个新的集合实例，其中包含一个序列的元素。
- [init(_:)](<init(__)-6lxbv.md>) — 创建一个新的集合实例，其中包含一个序列的元素。
- [init(repeating:count:)](<init(repeating_count_).md>) — 创建一个新的集合，其中包含指定数量的单个重复值。

### 实例方法

- [append(_:)](<append(__).md>) — 向集合末尾添加一个元素。
- [append(contentsOf:)](<append(contentsof_).md>) — 将一个序列或集合的元素添加到此集合的末尾。
- [append(contentsOf:)](<append(contentsof_)-9folw.md>) — 将一个序列或集合的元素添加到此集合的末尾。
- [applying(_:)](<applying(__).md>) — 将给定的差异应用到该集合。
- [filter(_:)](<filter(__)-66nvb.md>) — 返回一个同类型的新集合，其中按顺序包含原集合中满足给定谓词的元素。
- [insert(_:at:)](<insert(__at_).md>) — 在集合的指定位置插入一个新元素。
- [insert(contentsOf:at:)](<insert(contentsof_at_).md>) — 将一个序列的元素插入到集合的指定位置。
- [popLast()](<poplast()-70a2x.md>) — 移除并返回集合的最后一个元素。
- [popLast()](<poplast()-nrp9.md>) — 移除并返回集合的最后一个元素。
- [remove(at:)](<remove(at_).md>) — 移除并返回指定位置上的元素。
- [removeAll(keepingCapacity:)](<removeall(keepingcapacity_).md>) — 移除集合中的所有元素。
- [removeAll(where:)](<removeall(where_).md>) — 移除所有满足给定谓词的元素。
- [removeFirst()](<removefirst()-2cpd8.md>) — 移除并返回集合的第一个元素。
- [removeFirst()](<removefirst()-39om1.md>) — 移除并返回集合的第一个元素。
- [removeFirst(_:)](<removefirst(__)-43evo.md>) — 从集合开头移除指定数量的元素。
- [removeFirst(_:)](<removefirst(__)-5s82s.md>) — 从集合开头移除指定数量的元素。
- [removeLast()](<removelast()-4kq76.md>) — 移除并返回集合的最后一个元素。
- [removeLast()](<removelast()-5b56p.md>) — 移除并返回集合的最后一个元素。
- [removeLast(_:)](<removelast(__)-1xrzw.md>) — 从集合末尾移除指定数量的元素。
- [removeLast(_:)](<removelast(__)-5ulmx.md>) — 从集合末尾移除指定数量的元素。
- [removeSubrange(_:)](<removesubrange(__)-8mayj.md>) — 从集合中移除指定子范围内的元素。
- [removeSubrange(_:)](<removesubrange(__)-9twoc.md>) — 从集合中移除指定子范围内的元素。
- [removeSubranges(_:)](<removesubranges(__).md>) — 移除给定索引处的元素。
- [replaceSubrange(_:with:)](<replacesubrange(__with_)-3hke2.md>) — 用给定的集合替换指定子范围内的元素。 _(已废弃)_
- [replaceSubrange(_:with:)](<replacesubrange(__with_)-5g58l.md>) — 用给定的集合替换指定子范围内的元素。
- [replaceSubrange(_:with:)](<replacesubrange(__with_)-7293b.md>) — 用给定的集合替换指定子范围内的元素。
- [reserveCapacity(_:)](<reservecapacity(__).md>) — 在底层类型适用的情况下，为集合预留存储指定数量元素所需的空间。
