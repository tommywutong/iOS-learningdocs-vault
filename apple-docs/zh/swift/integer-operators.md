---
title: 整型运算符
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/integer-operators
source_url: 'https://developer.apple.com/documentation/swift/integer-operators'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/integer-operators.json'
content_hash: 'sha256:e62a10744dae182c'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md) · [Int](int.md)

# 整型运算符

<sub>API 集合</sub>

执行算术与按位运算，或比较值。

## 主题

### 算术

- [+(_:_:)](<int/+(____).md>) — 将两个值相加并产生它们的和。
- [-(_:_:)](<int/-(____).md>) — 从一个值中减去另一个值并产生它们的差。
- [*(_:_:)](<int/_(____).md>) — 将两个值相乘并产生它们的乘积。
- [/(_:_:)](<int/_(____)-7j9bj.md>) — 返回第一个值除以第二个值的商。

### 带赋值的算术

- [+=(_:_:)](<int/+=(____).md>) — 将两个值相加，并把结果存储到左侧变量中。
- [*=(_:_:)](<int/_=(____).md>) — 将两个值相乘，并把结果存储到左侧变量中。
- [/=(_:_:)](<int/_=(____)-9lzpe.md>) — 用第一个值除以第二个值，并把商存储到左侧变量中。

### 掩码算术

- [&+(_:_:)](<int/&+(____).md>) — 返回两个给定值的和，若发生溢出则对结果进行回绕。
- [&-(_:_:)](<int/&-(____).md>) — 返回两个给定值的差，若发生溢出则对结果进行回绕。
- [&*(_:_:)](<int/&_(____).md>) — 返回两个给定值的积，若发生溢出则对结果进行回绕。
- [&+=(_:_:)](<int/&+=(____).md>) — 将两个值相加，并把结果存储到左侧变量中，任何溢出都进行回绕。
- [&-=(_:_:)](<int/&-=(____).md>) — 从第一个值中减去第二个值，并把差存储到左侧变量中，任何溢出都进行回绕。
- [&*=(_:_:)](<int/&_=(____).md>) — 将两个值相乘，并把结果存储到左侧变量中，任何溢出都进行回绕。

### 按位运算

- [&(_:_:)](<int/&(____).md>) — 返回对两个给定值执行按位与运算的结果。
- [&=(_:_:)](<int/&=(____).md>) — 将对两个给定值执行按位与运算的结果存储到左侧变量中。
- [~(_:)](<int/~(__).md>) — 返回实参中已置位的位的反转。

### 取负

- [-(_:)](<int/-(__).md>) — 返回指定值的加法逆元。
- [+(_:)](<int/+(__).md>) — 原样返回给定的数字。

### 比较

- [==(_:_:)](<int/==(____).md>) — 返回一个布尔值，指示两个值是否相等。
- [==(_:_:)](<int/==(____)-1zalu.md>) — 返回一个布尔值，指示两个给定值是否相等。
- [!=(_:_:)](<int/!=(____)-4jphg.md>) — 返回一个布尔值，指示两个给定值是否不相等。

### 范围表达式

- [...(_:_:)](<int/'...(____).md>) — 返回一个包含两个边界的封闭范围。
- [...(_:)](<int/'...(__)-6ct66.md>) — 返回一个从下界向上延伸的部分范围。
- [...(_:)](<int/'...(__)-4mm5u.md>) — 返回一个直到（并包含）其上界的部分范围。

### 已废弃

- [-=(_:_:)](<int/-=(____).md>) — 从第一个值中减去第二个值，并把差存储到左侧变量中。

## 另请参阅

### 执行计算

- [negate()](<int/negate().md>) — 将此值替换为它的加法逆元。
- [quotientAndRemainder(dividingBy:)](<int/quotientandremainder(dividingby_).md>) — 返回此值除以给定值的商和余数。
- [isMultiple(of:)](<int/ismultiple(of_).md>) — 如果此值是给定值的倍数，则返回 `true`，否则返回 `false`。
