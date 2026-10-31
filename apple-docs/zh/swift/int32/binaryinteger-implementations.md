---
title: BinaryInteger 实现
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/int32/binaryinteger-implementations
source_url: 'https://developer.apple.com/documentation/swift/int32/binaryinteger-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int32/binaryinteger-implementations.json'
content_hash: 'sha256:7dfd8584475bc082'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [数字与基本值](../numbers-and-basic-values.md) · [特殊用途数值类型](../special-use-numeric-types.md) · [Int32](../int32.md)

# BinaryInteger 实现

<sub>API 集合</sub>

## 主题

### 运算符

- [!=(_:_:)](<!=(____)-2y35c.md>) — 返回一个布尔值，指示两个给定值是否不相等。
- [&(_:_:)](<&(____).md>) — 返回对两个给定值执行按位与（bitwise AND）运算的结果。
- [&(_:_:)](<&(____)-ui0w.md>) — 返回对两个给定值执行按位与运算的结果。
- [*(_:_:)](<_(____).md>) — 将两个值相乘并得出它们的乘积。
- [+(_:_:)](<+(____).md>) — 将两个值相加并得出它们的和。
- [-(_:_:)](<-(____).md>) — 将一个值减去另一个值并得出它们的差。
- [==(_:_:)](<==(____)-1giba.md>) — 返回一个布尔值，指示两个给定值是否相等。
- [^(_:_:)](<_(____)-1xb80.md>) — 返回对两个给定值执行按位异或（bitwise XOR）运算的结果。
- [^(_:_:)](<_(____)-2t9oy.md>) — 返回对两个给定值执行按位异或运算的结果。
- [%(_:_:)](<_(____)-41rsu.md>) — 返回第一个值除以第二个值的余数。
- [\>(_:_:)](<_(____)-4jn4j.md>) — 返回一个布尔值，指示第一个参数的值是否大于第二个参数的值。
- [|(_:_:)](<_(____)-5i6yu.md>) — 返回对两个给定值执行按位或（bitwise OR）运算的结果。
- [|(_:_:)](<_(____)-5zn2u.md>) — 返回对两个给定值执行按位或运算的结果。
- [\<(_:_:)](<_(____)-67qna.md>) — 返回一个布尔值，指示第一个参数的值是否小于第二个参数的值。
- [/(_:_:)](<_(____)-6fvom.md>) — 返回第一个值除以第二个值的商。
- [\>(_:_:)](_(____)-9adkd.md)
- [\<=(_:_:)](<_=(____)-1nkpl.md>) — 返回一个布尔值，指示第一个参数的值是否小于或等于第二个参数的值。
- [\>=(_:_:)](_=(____)-3jitm.md)
- [\<=(_:_:)](_=(____)-4p7mg.md)
- [\>=(_:_:)](<_=(____)-86dc4.md>) — 返回一个布尔值，指示第一个参数的值是否大于或等于第二个参数的值。
- [\<\<(_:_:)](<__(____)-27cld.md>) — 返回将值的二进制表示左移指定位数的结果。
- [\>\>(_:_:)](<__(____)-2ny6e.md>) — 返回将值的二进制表示右移指定位数的结果。
- [\>\>(_:_:)](<__(____)-5xz7g.md>) — 返回将值的二进制表示右移指定位数的结果。
- [\<\<(_:_:)](<__(____)-78esh.md>) — 返回将值的二进制表示左移指定位数的结果。
- [\>\>=(_:_:)](<__=(____)-1o1y1.md>) — 将值的二进制表示向右移动指定位数的结果存储到左侧变量中。
- [\<\<=(_:_:)](<__=(____)-80z6h.md>) — 将值的二进制表示向左移动指定位数的结果存储到左侧变量中。
- [~(_:)](<~(__).md>) — 返回对参数中已置位的位取反的结果。

### 初始化方法

- [init()](<init().md>) — 创建一个等于零的新值。
- [init(clamping:)](<init(clamping_).md>) — 使用最接近给定整数的可表示值创建新实例。
- [init(truncatingIfNeeded:)](<init(truncatingifneeded_).md>) — 通过对给定实例的位模式进行符号扩展或截断以适配此类型，从而创建新实例。

### 实例属性

- [bitWidth](bitwidth-swift.property.md) — 此值当前二进制表示中的位数。
- [description](description.md) — 此值的文本表示。

### 实例方法

- [advanced(by:)](<advanced(by_).md>) — 返回一个从此值偏移指定距离的值。
- [distance(to:)](<distance(to_).md>) — 返回从此值到给定值的距离，以步长表示。
- [isMultiple(of:)](<ismultiple(of_).md>) — 如果此值是给定值的倍数，则返回 `true`，否则返回 `false`。
- [quotientAndRemainder(dividingBy:)](<quotientandremainder(dividingby_).md>) — 返回此值除以给定值所得的商和余数。
