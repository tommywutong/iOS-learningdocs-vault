---
title: 数值、数据与基本值
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numbers-data-and-basic-values
source_url: 'https://developer.apple.com/documentation/foundation/numbers-data-and-basic-values'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numbers-data-and-basic-values.json'
content_hash: 'sha256:5d5d8e8115094e8e'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md)

# 数值、数据与基本值

<sub>API 集合</sub>

使用 Cocoa 中广泛采用的原始值和其他基础类型。

## 主题

### 数值

- [Int](../swift/int.md) — 一种有符号整数值类型。
- [Double](../swift/double.md) — 一种双精度（64 位）浮点值类型。
- [Decimal](decimal.md) — 一种表示十进制数的结构体。
- [NumberFormatter](numberformatter.md) — 在数值及其文本表示之间进行转换的格式化程序。

### 二进制数据

- [Data](data.md) — 内存中的字节缓冲区。
- [DataProtocol](dataprotocol.md) — 一种协议，为连续和非连续数据缓冲区底层的字节提供一致的数据访问。
- [MutableDataProtocol](mutabledataprotocol.md) — 一种协议，为连续和非连续可变数据缓冲区底层的字节提供一致的数据访问。
- [ContiguousBytes](contiguousbytes.md) — 一种协议，声明该类型以连续方式提供对底层原始字节的直接访问。

### URL

- [URL](url.md) — 标识资源位置的值，例如远程服务器上的项目或本地文件的路径。
- [URLComponents](urlcomponents.md) — 一种将 URL 解析为组成部分以及由组成部分构造 URL 的结构体。
- [URLQueryItem](urlqueryitem.md) — URL 查询部分中的单个名称-值对。

### 唯一标识符

- [UUID](uuid.md) — 用于标识类型、接口和其他项目的通用唯一值。

### 几何

- [CGFloat](../corefoundation/cgfloat-swift.struct.md) — Core Graphics 及相关框架中浮点标量值的基本类型。
- [NSPoint](nspoint.md) — 笛卡尔坐标系中的点。
- [NSSize](nssize.md) — 二维尺寸。
- [NSRect](nsrect.md) — 矩形。
- [AffineTransform](affinetransform.md) — 图形坐标变换。
- [NSEdgeInsets](nsedgeinsets.md) — 两个矩形边缘之间距离的描述。

### 范围

- [NSRange](nsrange-swift.typealias.md) — 一种用于描述序列某一部分的结构体，例如字符串中的字符或数组中的对象。

## 另请参阅

### 基础

- [字符串与文本](strings-and-text.md) — 创建和处理 Unicode 字符串，使用正则表达式查找模式，并对文本执行自然语言分析。
- [集合](collections.md) — 使用数组、字典、集合以及专用集合来存储和迭代对象组或值组。
- [日期与时间](dates-and-times.md) — 比较日期与时间，并执行日历和时区计算。
- [单位与测量](units-and-measurement.md) — 为数值量标注物理维度，以便根据区域设置进行格式化以及在相关单位间转换。
- [数据格式化](data-formatting.md) — 在数值、日期、测量值及其他值与根据区域设置生成的字符串表示之间进行转换。
- [筛选与排序](filters-and-sorting.md) — 使用谓词（predicate）、表达式和排序描述符检查集合及其他服务中的元素。
