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
doc_path: /documentation/swift/uint64/fixedwidthinteger-implementations
source_url: 'https://developer.apple.com/documentation/swift/uint64/fixedwidthinteger-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint64/fixedwidthinteger-implementations.json'
content_hash: 'sha256:71295c1cb917fa2f'
translated: true
---

> 导航： [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Numbers and Basic Values](../numbers-and-basic-values.md) · [Special-Use Numeric Types](../special-use-numeric-types.md) · [UInt64](../uint64.md)

# FixedWidthInteger 实现

<sub>API 集合</sub>

## 主题

### 运算符

- [&*(_:_:)](<&_(____).md>) — 返回两个给定值的乘积，若发生任何溢出则对结果进行回绕。
- [&*=(_:_:)](<&_=(____).md>) — 将两个值相乘并把结果存储到左侧变量中，任何溢出都会回绕。
- [&+(_:_:)](<&+(____).md>) — 返回两个给定值的和，若发生任何溢出则对结果进行回绕。
- [&+=(_:_:)](<&+=(____).md>) — 将两个值相加并把结果存储到左侧变量中，任何溢出都会回绕。
- [&-(_:_:)](<&-(____).md>) — 返回两个给定值的差，若发生任何溢出则对结果进行回绕。
- [&-=(_:_:)](<&-=(____).md>) — 从第一个值中减去第二个值并把差存储到左侧变量中，任何溢出都会回绕。
- [&\<\<(_:_:)](<&__(____)-20r54.md>) — 返回将值的二进制表示左移指定位数的结果，并将移位量按类型的位宽进行掩码处理。
- [&\>\>(_:_:)](<&__(____)-47n63.md>) — 返回将值的二进制表示右移指定位数的结果，并将移位量按类型的位宽进行掩码处理。
- [&\>\>(_:_:)](<&__(____)-4ncka.md>) — 返回将值的二进制表示右移指定位数的结果，并将移位量按类型的位宽进行掩码处理。
- [&\<\<(_:_:)](<&__(____)-67e3c.md>) — 返回将值的二进制表示左移指定位数的结果，并将移位量按类型的位宽进行掩码处理。
- [&\<\<(_:_:)](<&__(____)-8qsy.md>) — 返回将值的二进制表示左移指定位数的结果，并将移位量按类型的位宽进行掩码处理。
- [&\>\>(_:_:)](<&__(____)-9phvf.md>) — 返回将值的二进制表示右移指定位数的结果，并将移位量按类型的位宽进行掩码处理。
- [&\<\<=(_:_:)](<&__=(____)-487ah.md>) — 返回将值的二进制表示左移指定位数并将移位量按类型的位宽进行掩码处理所得的结果，并把结果存储到左侧变量中。
- [&\>\>=(_:_:)](<&__=(____)-4hmss.md>) — 计算将值的二进制表示右移指定位数并将移位量按类型的位宽进行掩码处理所得的结果，并把结果存储到左侧变量中。

### 初始化方法

- [init(_:)](<init(__)-5j67w.md>)
- [init(_:)](<init(__)-6f9pj.md>) — 根据给定的字符串创建一个新的整数值。
- [init(_:radix:)](<init(__radix_).md>) — 根据给定的字符串和基数创建一个新的整数值。
- [init(bigEndian:)](<init(bigendian_).md>) — 根据给定的大端表示创建一个整数，必要时改变字节序。
- [init(exactly:)](<init(exactly_)-7m1hy.md>)
- [init(littleEndian:)](<init(littleendian_).md>) — 根据给定的小端表示创建一个整数，必要时改变字节序。

### 实例属性

- [bigEndian](bigendian.md) — 此整数的大端表示。
- [littleEndian](littleendian.md) — 此整数的小端表示。

### 类型方法

- [random(in:)](<random(in_)-4xxb6.md>) — 返回指定范围内的一个随机值。
- [random(in:)](<random(in_)-5grii.md>) — 返回指定范围内的一个随机值。
- [random(in:using:)](<random(in_using_)-75uk1.md>) — 使用给定的生成器作为随机源，返回指定范围内的一个随机值。
- [random(in:using:)](<random(in_using_)-8r8yl.md>) — 使用给定的生成器作为随机源，返回指定范围内的一个随机值。
