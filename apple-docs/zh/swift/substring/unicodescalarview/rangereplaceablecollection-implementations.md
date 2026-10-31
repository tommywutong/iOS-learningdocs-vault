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
doc_path: /documentation/swift/substring/unicodescalarview/rangereplaceablecollection-implementations
source_url: 'https://developer.apple.com/documentation/swift/substring/unicodescalarview/rangereplaceablecollection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/substring/unicodescalarview/rangereplaceablecollection-implementations.json'
content_hash: 'sha256:bad944c12f7c42bb'
translated: true
---

> 导航： [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [Substring](../../substring.md) · [StringProtocol Implementations](../stringprotocol-implementations.md) · [UnicodeScalarView](../unicodescalarview.md)

# RangeReplaceableCollection 实现

<sub>API 集合</sub>

## 主题

### 运算符

- [+(_:_:)](<+(____)-1c1pd.md>) — 通过拼接一个序列和一个集合的元素，创建一个新的集合。
- [+(_:_:)](<+(____)-1p67y.md>) — 通过拼接两个集合的元素，创建一个新的集合。
- [+(_:_:)](<+(____)-9qjws.md>) — 通过拼接一个集合和一个序列的元素，创建一个新的集合。
- [+=(_:_:)](<+=(____).md>) — 将一个序列的元素追加到 range-replaceable collection 中。

### 初始化方法

- [init()](<init().md>) — 创建一个新的空集合。
- [init(_:)](<init(__).md>) — 创建一个新的集合实例，其中包含一个序列的元素。
- [init(repeating:count:)](<init(repeating_count_).md>) — 创建一个新的集合，其中包含指定数量的单个重复值。

### 实例方法

- [append(_:)](<append(__).md>) — 向集合末尾添加一个元素。
- [append(contentsOf:)](<append(contentsof_).md>) — 将一个序列或集合的元素添加到此集合的末尾。
- [applying(_:)](<applying(__).md>) — 将给定的差异应用到该集合。
- [filter(_:)](<filter(__)-6e5i2.md>) — 返回一个同类型的新集合，其中按顺序包含原集合中满足给定谓词的元素。
- [insert(_:at:)](<insert(__at_).md>) — 在集合的指定位置插入一个新元素。
- [insert(contentsOf:at:)](<insert(contentsof_at_).md>) — 将一个序列的元素插入到集合的指定位置。
- [popLast()](<poplast()-46voy.md>) — 移除并返回集合的最后一个元素。
- [popLast()](<poplast()-7zgh4.md>) — 移除并返回集合的最后一个元素。
- [remove(at:)](<remove(at_).md>) — 移除并返回指定位置上的元素。
- [removeAll(keepingCapacity:)](<removeall(keepingcapacity_).md>) — 移除集合中的所有元素。
- [removeAll(where:)](<removeall(where_).md>) — 移除所有满足给定谓词的元素。
- [removeFirst()](<removefirst()-2a3ja.md>) — 移除并返回集合的第一个元素。
- [removeFirst()](<removefirst()-5t2ib.md>) — 移除并返回集合的第一个元素。
- [removeFirst(_:)](<removefirst(__)-2lfkb.md>) — 从集合开头移除指定数量的元素。
- [removeFirst(_:)](<removefirst(__)-5314w.md>) — 从集合开头移除指定数量的元素。
- [removeLast()](<removelast()-3izvn.md>) — 移除并返回集合的最后一个元素。
- [removeLast()](<removelast()-75qy7.md>) — 移除并返回集合的最后一个元素。
- [removeLast(_:)](<removelast(__)-30fw5.md>) — 从集合末尾移除指定数量的元素。
- [removeLast(_:)](<removelast(__)-74qgu.md>) — 从集合末尾移除指定数量的元素。
- [removeSubrange(_:)](<removesubrange(__)-2qm37.md>) — 从集合中移除指定子范围内的元素。
- [removeSubrange(_:)](<removesubrange(__)-5c1al.md>) — 从集合中移除指定子范围内的元素。
- [removeSubranges(_:)](<removesubranges(__).md>) — 移除给定索引处的元素。
- [replaceSubrange(_:with:)](<replacesubrange(__with_).md>) — 用给定的集合替换指定子范围内的元素。
- [replaceSubrange(_:with:)](<replacesubrange(__with_)-4kmx6.md>) — 用给定的集合替换指定子范围内的元素。 _(已废弃)_
- [replaceSubrange(_:with:)](<replacesubrange(__with_)-7xjpm.md>) — 用给定的集合替换指定子范围内的元素。
- [reserveCapacity(_:)](<reservecapacity(__).md>) — 在底层类型适用的情况下，为集合预留存储指定数量元素所需的空间。
