---
title: FixedWidthInteger 实现
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/int8/fixedwidthinteger-implementations
source_url: 'https://developer.apple.com/documentation/swift/int8/fixedwidthinteger-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int8/fixedwidthinteger-implementations.json'
content_hash: 'sha256:da4046105d96d9ec'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [数字与基本值](../numbers-and-basic-values.md) · [特殊用途数值类型](../special-use-numeric-types.md) · [Int8](../int8.md)

# FixedWidthInteger 实现

<sub>API 集合</sub>

## 主题

### 运算符

- [&*(_:_:)](<&_(____).md>) — 返回两个给定值的乘积，在溢出时对结果进行回绕。
- [&*=(_:_:)](<&_=(____).md>) — 将两个值相乘，并将结果存储在左侧变量中，对任何溢出进行回绕。
- [&+(_:_:)](<&+(____).md>) — 返回两个给定值的和，在溢出时对结果进行回绕。
- [&+=(_:_:)](<&+=(____).md>) — 将两个值相加，并将结果存储在左侧变量中，对任何溢出进行回绕。
- [&-(_:_:)](<&-(____).md>) — 返回两个给定值的差，在溢出时对结果进行回绕。
- [&-=(_:_:)](<&-=(____).md>) — 从第一个值中减去第二个值，并将差值存储在左侧变量中，对任何溢出进行回绕。
- [&>\>(_:_:)](<&__(____)-1v821.md>) — 返回将值的二进制表示右移指定位数的结果，将移位量掩码到该类型的位宽。
- [&>\>(_:_:)](<&__(____)-24uqw.md>) — 返回将值的二进制表示右移指定位数的结果，将移位量掩码到该类型的位宽。
- [&<\<(_:_:)](<&__(____)-2a90q.md>) — 返回将值的二进制表示左移指定位数的结果，将移位量掩码到该类型的位宽。
- [&<\<(_:_:)](<&__(____)-4szuk.md>) — 返回将值的二进制表示左移指定位数的结果，将移位量掩码到该类型的位宽。
- [&<\<(_:_:)](<&__(____)-7028d.md>) — 返回将值的二进制表示左移指定位数的结果，将移位量掩码到该类型的位宽。
- [&>\>(_:_:)](<&__(____)-9x51j.md>) — 返回将值的二进制表示右移指定位数的结果，将移位量掩码到该类型的位宽。
- [&<\<=(_:_:)](<&__=(____)-6g9h1.md>) — 返回将值的二进制表示左移指定位数的结果，将移位量掩码到该类型的位宽，并将结果存储在左侧变量中。
- [&>\>=(_:_:)](<&__=(____)-9dar0.md>) — 计算将值的二进制表示右移指定位数的结果，将移位量掩码到该类型的位宽，并将结果存储在左侧变量中。

### 初始化方法

- [init(_:)](<init(__)-7lqol.md>)
- [init(_:)](<init(__)-89uu.md>) — 根据给定的字符串创建新的整数值。
- [init(_:radix:)](<init(__radix_).md>) — 根据给定的字符串和基数创建新的整数值。
- [init(bigEndian:)](<init(bigendian_).md>) — 根据整数的大端表示创建整数，必要时改变字节顺序。
- [init(exactly:)](<init(exactly_)-16mcu.md>)
- [init(littleEndian:)](<init(littleendian_).md>) — 根据整数的小端表示创建整数，必要时改变字节顺序。

### 实例属性

- [bigEndian](bigendian.md) — 此整数的大端表示。
- [littleEndian](littleendian.md) — 此整数的小端表示。

### 类型方法

- [random(in:)](<random(in_)-2fyvz.md>) — 返回指定范围内的随机值。
- [random(in:)](<random(in_)-5kgo1.md>) — 返回指定范围内的随机值。
- [random(in:using:)](<random(in_using_)-1n6up.md>) — 返回指定范围内的随机值，使用给定的生成器作为随机源。
- [random(in:using:)](<random(in_using_)-8ennz.md>) — 返回指定范围内的随机值，使用给定的生成器作为随机源。
