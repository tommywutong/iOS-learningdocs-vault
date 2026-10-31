---
title: FixedWidthInteger 实现
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/int/fixedwidthinteger-implementations
source_url: 'https://developer.apple.com/documentation/swift/int/fixedwidthinteger-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int/fixedwidthinteger-implementations.json'
content_hash: 'sha256:e50a5f2da8c83907'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Int](../int.md)

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
- [&\<\<(_:_:)](<&__(____)-2kxph.md>) — 返回将值的二进制表示左移指定位数的结果，并将移位量按类型的位宽进行掩码处理。
- [&\>\>(_:_:)](<&__(____)-35o0c.md>) — 返回将值的二进制表示右移指定位数的结果，并将移位量按类型的位宽进行掩码处理。
- [&\<\<(_:_:)](<&__(____)-3euzz.md>) — 返回将值的二进制表示左移指定位数的结果，并将移位量按类型的位宽进行掩码处理。
- [&\>\>(_:_:)](<&__(____)-5zh5j.md>) — 返回将值的二进制表示右移指定位数的结果，并将移位量按类型的位宽进行掩码处理。
- [&\>\>(_:_:)](<&__(____)-76ndv.md>) — 返回将值的二进制表示右移指定位数的结果，并将移位量按类型的位宽进行掩码处理。
- [&\<\<(_:_:)](<&__(____)-voti.md>) — 返回将值的二进制表示左移指定位数的结果，并将移位量按类型的位宽进行掩码处理。
- [&\<\<=(_:_:)](<&__=(____)-13miv.md>) — 返回将值的二进制表示左移指定位数的结果，将移位量按类型的位宽进行掩码处理，并将结果存储在左侧变量中。
- [&\>\>=(_:_:)](<&__=(____)-704vj.md>) — 计算将值的二进制表示右移指定位数的结果，将移位量按类型的位宽进行掩码处理，并将结果存储在左侧变量中。

### 初始化方法

- [init(_:)](<init(__)-2hmii.md>) — 根据给定的字符串创建新的整数值。
- [init(_:)](<init(__)-6gt9z.md>)
- [init(_:radix:)](<init(__radix_).md>) — 根据给定的字符串和基数创建新的整数值。
- [init(bigEndian:)](<init(bigendian_).md>) — 根据整数的大端表示创建整数，必要时改变字节顺序。
- [init(exactly:)](<init(exactly_)-7yhn6.md>)
- [init(littleEndian:)](<init(littleendian_).md>) — 根据整数的小端表示创建整数，必要时改变字节顺序。

### 实例属性

- [bigEndian](bigendian.md) — 此整数的大端表示。
- [littleEndian](littleendian.md) — 此整数的小端表示。

### 类型方法

- [random(in:)](<random(in_)-8zzqh.md>) — 返回指定范围内的随机值。
- [random(in:)](<random(in_)-9mjpw.md>) — 返回指定范围内的随机值。
- [random(in:using:)](<random(in_using_)-3dwv4.md>) — 返回指定范围内的随机值，使用给定的生成器作为随机源。
- [random(in:using:)](<random(in_using_)-4lsb5.md>) — 返回指定范围内的随机值，使用给定的生成器作为随机源。
