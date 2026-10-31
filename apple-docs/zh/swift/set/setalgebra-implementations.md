---
title: SetAlgebra 实现
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/set/setalgebra-implementations
source_url: 'https://developer.apple.com/documentation/swift/set/setalgebra-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/setalgebra-implementations.json'
content_hash: 'sha256:eab53b995a79e51c'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [集合](../collections.md) · [Set](../set.md)

# SetAlgebra 实现

<sub>API 集合</sub>

## 主题

### 初始化方法

- [init()](<init().md>) — 创建一个空集合。
- [init(_:)](<init(__).md>) — 用一个有限的元素序列创建一个新集合。
- [init(_:)](<init(__)-9cgks.md>) — 用一个有限的元素序列创建一个新集合。
- [init(arrayLiteral:)](<init(arrayliteral_)-85a3x.md>) — 创建一个包含给定数组字面量元素的集合。

### 实例方法

- [contains(_:)](<contains(__).md>) — 返回一个布尔值，指示给定元素是否存在于集合中。
- [formIntersection(_:)](<formintersection(__).md>) — 移除集合中不在给定序列里的元素。
- [formSymmetricDifference(_:)](<formsymmetricdifference(__)-22p0m.md>) — 移除集合中也在给定序列里的元素，并添加序列中尚不在集合里的成员。
- [formUnion(_:)](<formunion(__).md>) — 把给定序列的元素插入集合。
- [insert(_:)](<insert(__)-nads.md>) — 如果给定元素尚不存在，则把它插入集合。
- [intersection(_:)](<intersection(__)-1zh8f.md>) — 返回一个新集合，包含此集合与给定序列共有的元素。
- [isDisjoint(with:)](<isdisjoint(with_)-8ngmk.md>) — 返回一个布尔值，指示此集合与给定集合是否没有共同的成员。
- [isSubset(of:)](<issubset(of_)-1d7pp.md>) — 返回一个布尔值，指示此集合是否是给定集合的子集。
- [isSuperset(of:)](<issuperset(of_)-9iz62.md>) — 返回一个布尔值，指示此集合是否是给定集合的超集。
- [remove(_:)](<remove(__)-8p2tv.md>) — 从集合中移除指定的元素。
- [subtract(_:)](<subtract(__)-7uaak.md>) — 从此集合中移除给定集合的元素。
- [subtract(_:)](<subtract(__)-8gc48.md>) — 从此集合中移除给定集合的元素。
- [subtracting(_:)](<subtracting(__)-3n4lc.md>) — 返回一个新集合，包含此集合中未出现在给定集合里的元素。
- [symmetricDifference(_:)](<symmetricdifference(__).md>) — 返回一个新集合，包含只属于此集合或只属于给定序列（而非两者共有）的元素。
- [union(_:)](<union(__).md>) — 返回一个新集合，包含此集合和给定序列两者的元素。
- [update(with:)](<update(with_)-2n6tk.md>) — 无条件地把给定元素插入集合。
