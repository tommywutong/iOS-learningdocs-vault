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
doc_path: /documentation/swift/int128/fixedwidthinteger-implementations
source_url: 'https://developer.apple.com/documentation/swift/int128/fixedwidthinteger-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int128/fixedwidthinteger-implementations.json'
content_hash: 'sha256:a802ef879c56ef41'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [数字与基本值](../numbers-and-basic-values.md) · [特殊用途数值类型](../special-use-numeric-types.md) · [Int128](../int128.md)

# FixedWidthInteger 实现

<sub>API 集合</sub>

## 主题

### 运算符

- [&*(_:_:)](<&_(____).md>) — 返回两个给定值的乘积，在溢出时对结果进行回绕。
- [&*(_:_:)](<&_(____)-ctty.md>) — 返回两个给定值的乘积，在溢出时对结果进行回绕。
- [&*=(_:_:)](<&_=(____).md>) — 将两个值相乘，并将结果存储在左侧变量中，对任何溢出进行回绕。
- [&+(_:_:)](<&+(____).md>) — 返回两个给定值的和，在溢出时对结果进行回绕。
- [&+=(_:_:)](<&+=(____).md>) — 将两个值相加，并将结果存储在左侧变量中，对任何溢出进行回绕。
- [&-(_:_:)](<&-(____).md>) — 返回两个给定值的差，在溢出时对结果进行回绕。
- [&-=(_:_:)](<&-=(____).md>) — 从第一个值中减去第二个值，并将差值存储在左侧变量中，对任何溢出进行回绕。
- [&\>\>(_:_:)](<&__(____)-227qu.md>) — 返回将值的二进制表示右移指定位数的结果，将移位量掩码到该类型的位宽。
- [&\>\>(_:_:)](<&__(____)-71ih1.md>) — 返回将值的二进制表示右移指定位数的结果，将移位量掩码到该类型的位宽。
- [&\<\<(_:_:)](<&__(____)-9gig.md>) — 返回将值的二进制表示左移指定位数的结果，将移位量掩码到该类型的位宽。
- [&\<\<(_:_:)](<&__(____)-lkqj.md>) — 返回将值的二进制表示左移指定位数的结果，将移位量掩码到该类型的位宽。
- [&\<\<=(_:_:)](<&__=(____)-1pdlg.md>) — 返回将值的二进制表示左移指定位数的结果，将移位量掩码到该类型的位宽，并将结果存储在左侧变量中。
- [&\<\<=(_:_:)](<&__=(____)-2vr5o.md>) — 返回将值的二进制表示左移指定位数的结果，将移位量掩码到该类型的位宽，并将结果存储在左侧变量中。
- [&\>\>=(_:_:)](<&__=(____)-5pnjk.md>) — 计算将值的二进制表示右移指定位数的结果，将移位量掩码到该类型的位宽，并将结果存储在左侧变量中。
- [&\>\>=(_:_:)](<&__=(____)-69tya.md>) — 计算将值的二进制表示右移指定位数的结果，将移位量掩码到该类型的位宽，并将结果存储在左侧变量中。

### 初始化方法

- [init(_:)](<init(__)-3gl5w.md>)
- [init(_:)](<init(__)-9xe9j.md>) — 根据给定的字符串创建新的整数值。
- [init(_:radix:)](<init(__radix_).md>) — 根据给定的字符串和基数创建新的整数值。
- [init(bigEndian:)](<init(bigendian_).md>) — 根据整数的大端表示创建整数，必要时改变字节顺序。
- [init(exactly:)](<init(exactly_)-yans.md>)
- [init(littleEndian:)](<init(littleendian_).md>) — 根据整数的小端表示创建整数，必要时改变字节顺序。

### 实例属性

- [bigEndian](bigendian.md) — 此整数的大端表示。
- [byteSwapped](byteswapped.md) — 此整数在交换字节顺序后的表示。
- [leadingZeroBitCount](leadingzerobitcount.md) — 此值的二进制表示中前导零的数量。
- [littleEndian](littleendian.md) — 此整数的小端表示。
- [nonzeroBitCount](nonzerobitcount.md) — 此值的二进制表示中等于 1 的位的数量。

### 实例方法

- [addingReportingOverflow(_:)](<addingreportingoverflow(__).md>) — 返回此值与给定值的和，以及一个指示该运算中是否发生溢出的布尔值。
- [dividedReportingOverflow(by:)](<dividedreportingoverflow(by_).md>) — 返回此值除以给定值所得的商，以及一个指示该运算中是否发生溢出的布尔值。
- [multipliedFullWidth(by:)](<multipliedfullwidth(by_).md>) — 返回一个元组，包含此值与给定值相乘结果的高位和低位部分。
- [multipliedReportingOverflow(by:)](<multipliedreportingoverflow(by_).md>) — 返回此值与给定值的乘积，以及一个指示该运算中是否发生溢出的布尔值。
- [remainderReportingOverflow(dividingBy:)](<remainderreportingoverflow(dividingby_).md>) — 返回此值除以给定值所得的余数，以及一个指示除法过程中是否发生溢出的布尔值。
- [subtractingReportingOverflow(_:)](<subtractingreportingoverflow(__).md>) — 返回此值减去给定值所得的差，以及一个指示该运算中是否发生溢出的布尔值。

### 类型属性

- [bitWidth](bitwidth.md) — 用于此类型值的底层二进制表示的位数。
- [max](max.md) — 此类型可表示的最大整数。
- [min](min.md) — 此类型可表示的最小整数。

### 类型方法

- [random(in:)](<random(in_)-4lf3w.md>) — 返回指定范围内的随机值。
- [random(in:)](<random(in_)-55a79.md>) — 返回指定范围内的随机值。
- [random(in:using:)](<random(in_using_)-4e4vx.md>) — 返回指定范围内的随机值，使用给定的生成器作为随机源。
- [random(in:using:)](<random(in_using_)-7t428.md>) — 返回指定范围内的随机值，使用给定的生成器作为随机源。
