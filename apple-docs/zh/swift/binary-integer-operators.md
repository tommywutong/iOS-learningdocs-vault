---
title: 二元整数运算符
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/binary-integer-operators
source_url: 'https://developer.apple.com/documentation/swift/binary-integer-operators'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/binary-integer-operators.json'
content_hash: 'sha256:dc6108b5e4e18e9a'
translated: true
---

> 导航： [Technologies](../technologies.md) · [Swift](../swift.md) · [Swift Standard Library](swift-standard-library.md) · [Numbers and Basic Values](numbers-and-basic-values.md) · [Numeric Protocols](numeric-protocols.md) · [BinaryInteger](binaryinteger.md)

# 二元整数运算符

<sub>API 集合</sub>

执行算术和位运算操作，或比较值。

## 主题

### 算术运算

- [+(_:_:)](<binaryinteger/+(____).md>) — 将两个值相加，得到它们的和。
- [-(_:_:)](<binaryinteger/-(____).md>) — 从一个值中减去另一个值，得到它们的差。
- [*(_:_:)](<binaryinteger/_(____).md>) — 将两个值相乘，得到它们的乘积。
- [/(_:_:)](<binaryinteger/_(____)-8zc6l.md>) — 返回第一个值除以第二个值所得的商。

### 带赋值的算术运算

- [+=(_:_:)](<binaryinteger/+=(____).md>) — 将两个值相加并把结果存储到左侧变量中。
- [-=(_:_:)](<binaryinteger/-=(____).md>) — 从第一个值中减去第二个值，并把差存储到左侧变量中。
- [*=(_:_:)](<binaryinteger/_=(____).md>) — 将两个值相乘并把结果存储到左侧变量中。
- [/=(_:_:)](<binaryinteger/_=(____)-20xv1.md>) — 用第一个值除以第二个值，并把商存储到左侧变量中。

### 按位运算

- [&(_:_:)](<binaryinteger/&(____).md>) — 对两个给定值执行按位与运算，返回所得结果。
- [&=(_:_:)](<binaryinteger/&=(____).md>) — 对两个给定值执行按位与运算，并把结果存储到左侧变量中。
- [~(_:)](<binaryinteger/~(__).md>) — 返回对参数中已置位的位取反的结果。

### 比较运算

- [!=(_:_:)](<binaryinteger/!=(____)-9ooa7.md>) — 返回一个布尔值，指示两个给定值是否不相等。
- [!=(_:_:)](<binaryinteger/!=(____)-4ljme.md>) — 返回一个布尔值，指示两个值是否不相等。

## 另请参阅

### 执行计算

- [quotientAndRemainder(dividingBy:)](<binaryinteger/quotientandremainder(dividingby_).md>) — 返回此值除以给定值所得的商和余数。
- [isMultiple(of:)](<binaryinteger/ismultiple(of_).md>) — 如果此值是给定值的倍数，则返回 `true`，否则返回 `false`。
