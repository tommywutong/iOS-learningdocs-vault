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
doc_path: /documentation/swift/int128/binaryinteger-implementations
source_url: 'https://developer.apple.com/documentation/swift/int128/binaryinteger-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int128/binaryinteger-implementations.json'
content_hash: 'sha256:83ee3576915f0cbb'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [数字与基础值](../numbers-and-basic-values.md) · [特殊用途数值类型](../special-use-numeric-types.md) · [Int128](../int128.md)

# BinaryInteger 实现

<sub>API 集合</sub>

## 主题

### 运算符

- [!=(\_:\_:)](<!=(____)-4l6xf.md>) — 返回一个布尔值，指示两个给定值是否不相等。
- [&(\_:\_:)](<&(____).md>) — 返回对两个给定值执行按位与运算的结果。
- [&=(\_:\_:)](<&=(____).md>) — 将对两个给定值执行按位与运算的结果存储到左侧变量中。
- [==(\_:\_:)](<==(____)-31spp.md>) — 返回一个布尔值，指示两个给定值是否相等。
- [|(\_:\_:)](<_(____)-120rc.md>) — 返回对两个给定值执行按位或运算的结果。
- [\>(\_:\_:)](<_(____)-3jxf8.md>) — 返回一个布尔值，指示第一个参数的值是否大于第二个参数的值。
- [/(\_:\_:)](<_(____)-3u29x.md>) — 返回第一个值除以第二个值的商。
- [%(\_:\_:)](<_(____)-4kr9j.md>) — 返回第一个值除以第二个值的余数。
- [^(\_:\_:)](<_(____)-4wqvr.md>) — 返回对两个给定值执行按位异或运算的结果。
- [\<(\_:\_:)](<_(____)-6c38s.md>) — 返回一个布尔值，指示第一个参数的值是否小于第二个参数的值。
- [\>(\_:\_:)](<_(____)-71bfg.md>)
- [\>=(\_:\_:)](<_=(____)-2rq25.md>)
- [\<=(\_:\_:)](<_=(____)-3tzf9.md>)
- [/=(\_:\_:)](<_=(____)-4hmtz.md>) — 将第一个值除以第二个值，并将商存储到左侧变量中。
- [%=(\_:\_:)](<_=(____)-58nmj.md>) — 将第一个值除以第二个值，并将余数存储到左侧变量中。
- [|=(\_:\_:)](<_=(____)-791af.md>) — 将对两个给定值执行按位或运算的结果存储到左侧变量中。
- [\>=(\_:\_:)](<_=(____)-90wyd.md>) — 返回一个布尔值，指示第一个参数的值是否大于或等于第二个参数的值。
- [\<=(\_:\_:)](<_=(____)-9kicv.md>) — 返回一个布尔值，指示第一个参数的值是否小于或等于第二个参数的值。
- [^=(\_:\_:)](<_=(____)-ckwk.md>) — 将对两个给定值执行按位异或运算的结果存储到左侧变量中。
- [\>\>(\_:\_:)](<__(____)-10plt.md>) — 返回将值的二进制表示向右移动指定位数的结果。
- [\<\<(\_:\_:)](<__(____)-30yed.md>) — 返回将值的二进制表示向左移动指定位数的结果。
- [\<\<(\_:\_:)](<__(____)-6jhs3.md>) — 返回将值的二进制表示向左移动指定位数的结果。
- [\>\>(\_:\_:)](<__(____)-80gwd.md>) — 返回将值的二进制表示向右移动指定位数的结果。
- [\<\<=(\_:\_:)](<__=(____)-195op.md>) — 将值的二进制表示向左移动指定位数的结果存储到左侧变量中。
- [\>\>=(\_:\_:)](<__=(____)-3w1qu.md>) — 将值的二进制表示向右移动指定位数的结果存储到左侧变量中。
- [~(\_:)](<~(__).md>) — 返回参数中位的取反结果。

### 初始化方法

- [init()](<init().md>) — 创建一个等于零的新值。
- [init(\_:)](<init(__)-7ib60.md>) — 根据给定的浮点值创建一个整数，向零舍入。
- [init(\_:)](<init(__)-95d5.md>) — 根据给定的整数创建一个新实例。
- [init(clamping:)](<init(clamping_).md>) — 使用与给定整数最接近的可表示值创建一个新实例。
- [init(clamping:)](<init(clamping_)-4ogm3.md>) — 使用与给定整数最接近的可表示值创建一个新实例。
- [init(exactly:)](<init(exactly_)-7ybhb.md>) — 根据给定的浮点值创建一个整数（如果该值可以被精确表示）。
- [init(truncatingIfNeeded:)](<init(truncatingifneeded_).md>) — 通过对给定实例的位模式进行符号扩展或截断以适应此类型，来创建一个新实例。
- [init(truncatingIfNeeded:)](<init(truncatingifneeded_)-9tq25.md>) — 通过对给定实例的位模式进行符号扩展或截断以适应此类型，来创建一个新实例。

### 实例属性

- [bitWidth](bitwidth-swift.property.md) — 此值当前二进制表示中的位数。
- [description](description.md) — 此值的文本表示。
- [trailingZeroBitCount](trailingzerobitcount.md) — 此值二进制表示中尾部零的个数。
- [words](words-swift.property.md) — 一个包含此值二进制表示中各个字（words）的集合，顺序从最低有效位到最高有效位。

### 实例方法

- [advanced(by:)](<advanced(by_).md>) — 返回从该值偏移指定距离的值。
- [distance(to:)](<distance(to_).md>) — 返回从该值到给定值的距离，以步长（stride）表示。
- [isMultiple(of:)](<ismultiple(of_).md>) — 如果该值是给定值的倍数，则返回 `true`，否则返回 `false`。
- [quotientAndRemainder(dividingBy:)](<quotientandremainder(dividingby_).md>) — 返回该值除以给定值的商和余数。
- [signum()](<signum().md>) — 如果该值为负数则返回 `-1`，为正数则返回 `1`；否则返回 `0`。

### 类型别名

- [Words](words-swift.typealias.md) — 表示二进制整数中字的类型。
