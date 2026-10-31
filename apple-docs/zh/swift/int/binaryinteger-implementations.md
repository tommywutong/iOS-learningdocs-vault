---
title: BinaryInteger 实现
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/int/binaryinteger-implementations
source_url: 'https://developer.apple.com/documentation/swift/int/binaryinteger-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int/binaryinteger-implementations.json'
content_hash: 'sha256:bb723d2d6cf365c6'
translated: true
---

> 导航： [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int](../int.md)

# BinaryInteger 实现

<sub>API 集合</sub>

## 主题

### 运算符

- [!=(_:_:)](<!=(____)-4jphg.md>) — 返回一个布尔值，指示两个给定值是否不相等。
- [&(_:_:)](<&(____).md>) — 对两个给定值执行按位与运算，返回所得结果。
- [&(_:_:)](<&(____)-1gv8r.md>) — 对两个给定值执行按位与运算，返回所得结果。
- [*(_:_:)](<_(____).md>) — 将两个值相乘，得到它们的乘积。
- [+(_:_:)](<+(____).md>) — 将两个值相加，得到它们的和。
- [-(_:_:)](<-(____).md>) — 从一个值中减去另一个值，得到它们的差。
- [==(_:_:)](<==(____)-1zalu.md>) — 返回一个布尔值，指示两个给定值是否相等。
- [|(_:_:)](<_(____)-1e0ee.md>) — 对两个给定值执行按位或运算，返回所得结果。
- [|(_:_:)](<_(____)-26x3w.md>) — 对两个给定值执行按位或运算，返回所得结果。
- [^(_:_:)](<_(____)-2yuui.md>) — 对两个给定值执行按位异或运算，返回所得结果。
- [\<(_:_:)](<_(____)-3r70c.md>) — 返回一个布尔值，指示第一个参数的值是否小于第二个参数的值。
- [\>(_:_:)](<_(____)-4e53i.md>)
- [^(_:_:)](<_(____)-591r5.md>) — 对两个给定值执行按位异或运算，返回所得结果。
- [%(_:_:)](<_(____)-6lyj3.md>) — 返回第一个值除以第二个值所得的余数。
- [\>(_:_:)](<_(____)-7d57p.md>) — 返回一个布尔值，指示第一个参数的值是否大于第二个参数的值。
- [/(_:_:)](<_(____)-7j9bj.md>) — 返回第一个值除以第二个值所得的商。
- [\<=(_:_:)](<_=(____)-6cfca.md>)
- [\>=(_:_:)](<_=(____)-7tmrx.md>)
- [\>=(_:_:)](<_=(____)-7v58y.md>) — 返回一个布尔值，指示第一个参数的值是否大于或等于第二个参数的值。
- [\<=(_:_:)](<_=(____)-yera.md>) — 返回一个布尔值，指示第一个参数的值是否小于或等于第二个参数的值。
- [\<\<(_:_:)](<__(____)-2xfjq.md>) — 返回将值的二进制表示左移指定位数的结果。
- [\<\<(_:_:)](<__(____)-60q97.md>) — 返回将值的二进制表示左移指定位数的结果。
- [\>\>(_:_:)](<__(____)-635pg.md>) — 返回将值的二进制表示右移指定位数的结果。
- [\>\>(_:_:)](<__(____)-97tkh.md>) — 返回将值的二进制表示右移指定位数的结果。
- [\<\<=(_:_:)](<__=(____)-66xgb.md>) — 将值的二进制表示左移指定位数所得的结果存储到左侧变量中。
- [\>\>=(_:_:)](<__=(____)-9p0ct.md>) — 将值的二进制表示右移指定位数所得的结果存储到左侧变量中。
- [~(_:)](<~(__).md>) — 返回对参数中已置位的位取反的结果。

### 初始化方法

- [init()](<init().md>) — 创建一个等于零的新值。
- [init(clamping:)](<init(clamping_).md>) — 用最接近给定整数的可表示值创建一个新实例。
- [init(truncatingIfNeeded:)](<init(truncatingifneeded_).md>) — 通过对给定实例的位模式进行符号扩展或截断以适配此类型，从而创建新实例。

### 实例属性

- [bitWidth](bitwidth-swift.property.md) — 此值当前二进制表示中的位数。
- [description](description.md) — 此值的文本表示。

### 实例方法

- [isMultiple(of:)](<ismultiple(of_).md>) — 如果此值是给定值的倍数，则返回 `true`，否则返回 `false`。
- [quotientAndRemainder(dividingBy:)](<quotientandremainder(dividingby_).md>) — 返回此值除以给定值所得的商和余数。
