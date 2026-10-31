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
doc_path: /documentation/swift/uint64/binaryinteger-implementations
source_url: 'https://developer.apple.com/documentation/swift/uint64/binaryinteger-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint64/binaryinteger-implementations.json'
content_hash: 'sha256:e4a762de972cbcf6'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [数字与基本值](../numbers-and-basic-values.md) · [特殊用途数值类型](../special-use-numeric-types.md) · [UInt64](../uint64.md)

# BinaryInteger 实现

<sub>API 集合</sub>

## 主题

### 运算符

- [!=(_:_:)](<!=(____)-67tzk.md>) — 返回一个布尔值，指示两个给定值是否不相等。
- [&(_:_:)](<&(____).md>) — 返回对两个给定值执行按位与（bitwise AND）运算的结果。
- [&(_:_:)](<&(____)-3x1yh.md>) — 返回对两个给定值执行按位与运算的结果。
- [*(_:_:)](<_(____).md>) — 将两个值相乘并得出它们的乘积。
- [+(_:_:)](<+(____).md>) — 将两个值相加并得出它们的和。
- [-(_:_:)](<-(____).md>) — 将一个值减去另一个值并得出它们的差。
- [==(_:_:)](<==(____)-6ra49.md>) — 返回一个布尔值，指示两个给定值是否相等。
- [^(_:_:)](<_(____)-1kwg2.md>) — 返回对两个给定值执行按位异或（bitwise XOR）运算的结果。
- [|(_:_:)](<_(____)-2girh.md>) — 返回对两个给定值执行按位或（bitwise OR）运算的结果。
- [^(_:_:)](<_(____)-5hgaz.md>) — 返回对两个给定值执行按位异或运算的结果。
- [\>(_:_:)](_(____)-5jero.md)
- [%(_:_:)](<_(____)-68vrk.md>) — 返回第一个值除以第二个值的余数。
- [|(_:_:)](<_(____)-6ykmm.md>) — 返回对两个给定值执行按位或运算的结果。
- [\<(_:_:)](<_(____)-75vtz.md>) — 返回一个布尔值，指示第一个参数的值是否小于第二个参数的值。
- [/(_:_:)](<_(____)-8b3l2.md>) — 返回第一个值除以第二个值的商。
- [\>(_:_:)](<_(____)-9xpv.md>) — 返回一个布尔值，指示第一个参数的值是否大于第二个参数的值。
- [\<=(_:_:)](<_=(____)-1clb5.md>) — 返回一个布尔值，指示第一个参数的值是否小于或等于第二个参数的值。
- [\<=(_:_:)](_=(____)-4pbv7.md)
- [\>=(_:_:)](<_=(____)-5p2f4.md>) — 返回一个布尔值，指示第一个参数的值是否大于或等于第二个参数的值。
- [\>=(_:_:)](_=(____)-5sy3d.md)
- [\>\>(_:_:)](<__(____)-25f5d.md>) — 返回将值的二进制表示右移指定位数的结果。
- [\<\<(_:_:)](<__(____)-5so09.md>) — 返回将值的二进制表示左移指定位数的结果。
- [\>\>(_:_:)](<__(____)-7rk6f.md>) — 返回将值的二进制表示右移指定位数的结果。
- [\<\<(_:_:)](<__(____)-83yhh.md>) — 返回将值的二进制表示左移指定位数的结果。
- [\>\>=(_:_:)](<__=(____)-25p32.md>) — 将值的二进制表示向右移动指定位数的结果存储到左侧变量中。
- [\<\<=(_:_:)](<__=(____)-7usr.md>) — 将值的二进制表示向左移动指定位数的结果存储到左侧变量中。
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
