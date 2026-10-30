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
doc_path: /documentation/swift/uint128/binaryinteger-implementations
source_url: 'https://developer.apple.com/documentation/swift/uint128/binaryinteger-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint128/binaryinteger-implementations.json'
content_hash: 'sha256:4e8b7eb903217c46'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [数字与基础值](../numbers-and-basic-values.md) · [特殊用途数值类型](../special-use-numeric-types.md) · [UInt128](../uint128.md)

# BinaryInteger 实现

<sub>API 集合</sub>

## 主题

### 结构体

- [Words](words-swift.struct.md) — 一种表示二进制整数各个字（word）的类型。

### 运算符

- [!=(_:_:)](<!=(____)-9eyev.md>) — 返回一个布尔值，指示两个给定的值是否不相等。
- [&(_:_:)](<&(____).md>) — 返回对两个给定的值执行按位与（AND）运算的结果。
- [&=(_:_:)](<&=(____).md>) — 将对两个给定的值执行按位与运算的结果存储到左侧变量中。
- [==(_:_:)](<==(____)-4hd8l.md>) — 返回一个布尔值，指示两个给定的值是否相等。
- [^(_:_:)](<_(____)-1bfdp.md>) — 返回对两个给定的值执行按位异或（XOR）运算的结果。
- [\<(_:_:)](<_(____)-3fwln.md>) — 返回一个布尔值，指示第一个参数的值是否小于第二个参数的值。
- [%(_:_:)](<_(____)-3t4ck.md>) — 返回第一个值除以第二个值所得的余数。
- [\>(_:_:)](<_(____)-41n11.md>)
- [/(_:_:)](<_(____)-4hvzy.md>) — 返回第一个值除以第二个值所得的商。
- [\>(_:_:)](<_(____)-8enxk.md>) — 返回一个布尔值，指示第一个参数的值是否大于第二个参数的值。
- [|(_:_:)](<_(____)-k8pw.md>) — 返回对两个给定的值执行按位或（OR）运算的结果。
- [\>=(_:_:)](<_=(____)-1t601.md>) — 返回一个布尔值，指示第一个参数的值是否大于或等于第二个参数的值。
- [\>=(_:_:)](<_=(____)-36npw.md>)
- [\<=(_:_:)](<_=(____)-3wmkz.md>) — 返回一个布尔值，指示第一个参数的值是否小于或等于第二个参数的值。
- [^=(_:_:)](<_=(____)-4j7m1.md>) — 将对两个给定的值执行按位异或运算的结果存储到左侧变量中。
- [/=(_:_:)](<_=(____)-6xh2i.md>) — 将第一个值除以第二个值，并将商存储到左侧变量中。
- [%=(_:_:)](<_=(____)-75khj.md>) — 将第一个值除以第二个值，并将余数存储到左侧变量中。
- [|=(_:_:)](<_=(____)-8ko9m.md>) — 将对两个给定的值执行按位或运算的结果存储到左侧变量中。
- [\<=(_:_:)](<_=(____)-906fm.md>)
- [\<\<(_:_:)](<__(____)-3yi94.md>) — 返回将值的二进制表示向左移动指定位数的结果。
- [\<\<(_:_:)](<__(____)-70lq0.md>) — 返回将值的二进制表示向左移动指定位数的结果。
- [\>\>(_:_:)](<__(____)-9qcxu.md>) — 返回将值的二进制表示向右移动指定位数的结果。
- [\>\>(_:_:)](<__(____)-9tjzy.md>) — 返回将值的二进制表示向右移动指定位数的结果。
- [\<\<=(_:_:)](<__=(____)-22e6u.md>) — 将值的二进制表示向左移动指定位数的结果存储到左侧变量中。
- [\>\>=(_:_:)](<__=(____)-6t3cz.md>) — 将值的二进制表示向右移动指定位数的结果存储到左侧变量中。
- [~(_:)](<~(__).md>) — 返回对参数中已设置的位取反的结果。

### 初始化方法

- [init()](<init().md>) — 创建一个等于零的新值。
- [init(_:)](<init(__)-2b08e.md>) — 根据给定的浮点值创建一个整数，向零舍入。
- [init(_:)](<init(__)-luvl.md>) — 根据给定的整数创建一个新实例。
- [init(clamping:)](<init(clamping_).md>) — 创建一个新实例，其值为最接近给定整数的可表示值。
- [init(clamping:)](<init(clamping_)-7tt6l.md>) — 创建一个新实例，其值为最接近给定整数的可表示值。
- [init(exactly:)](<init(exactly_)-13dy3.md>) — 如果给定的浮点值可以被精确表示，则根据它创建一个整数。
- [init(truncatingIfNeeded:)](<init(truncatingifneeded_).md>) — 通过符号扩展或截断以适应此类型，根据给定实例的位模式创建一个新实例。
- [init(truncatingIfNeeded:)](<init(truncatingifneeded_)-1xc1t.md>) — 通过符号扩展或截断以适应此类型，根据给定实例的位模式创建一个新实例。

### 实例属性

- [bitWidth](bitwidth-swift.property.md) — 此值当前二进制表示中的位数。
- [description](description.md) — 此值的文本表示。
- [trailingZeroBitCount](trailingzerobitcount.md) — 此值二进制表示中尾随零的数量。
- [words](words-swift.property.md) — 按从最低有效到最高有效的顺序，包含此值二进制表示中各个字的集合。

### 实例方法

- [advanced(by:)](<advanced(by_).md>) — 返回从此值偏移指定距离得到的值。
- [distance(to:)](<distance(to_).md>) — 返回从此值到给定值的距离，以 stride 表示。
- [isMultiple(of:)](<ismultiple(of_).md>) — 如果此值是给定值的倍数，则返回 `true`；否则返回 `false`。
- [quotientAndRemainder(dividingBy:)](<quotientandremainder(dividingby_).md>) — 返回此值除以给定值所得的商和余数。
- [signum()](<signum().md>) — 如果此值为负，则返回 `-1`；为正，则返回 `1`；否则返回 `0`。
