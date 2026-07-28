---
title: 日期与时间
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/dates-and-times
source_url: 'https://developer.apple.com/documentation/foundation/dates-and-times'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dates-and-times.json'
content_hash: 'sha256:4991fade4a70ec86'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md)

# 日期与时间

<sub>API 集合</sub>

比较日期与时间，并执行日历和时区计算。

## 主题

### 日期表示

- [Date](date.md) — 不依赖任何日历或时区的特定时间点。
- [DateInterval](dateinterval.md) — 特定开始日期与结束日期之间的时间跨度。
- [TimeInterval](timeinterval.md) — 秒数。

### 日历计算

- [DateComponents](datecomponents.md) — 按单位（例如年、月、日、时和分）指定的日期或时间，将在日历系统和时区中进行求值。
- [Calendar](calendar.md) — 日历单位与绝对时间点之间关系的定义，提供日期计算和比较功能。
- [TimeZone](timezone.md) — 与特定地缘政治区域关联的标准时间惯例信息。

### 日期格式化

- [DateFormatter](dateformatter.md) — 在日期及其文本表示之间进行转换的格式化器。
- [DateComponentsFormatter](datecomponentsformatter.md) — 创建时长的字符串表示的格式化器。
- [DateIntervalFormatter](dateintervalformatter.md) — 创建时间间隔字符串表示的格式化器。
- [ISO8601DateFormatter](iso8601dateformatter.md) — 在日期及其 ISO 8601 字符串表示之间进行转换的格式化器。

### 国际化

- [Locale](locale.md) — 用于格式化待呈现数据的语言、文化和技术惯例信息。

## 另请参阅

### 基础

- [数字、数据与基本值](numbers-data-and-basic-values.md) — 使用 Cocoa 中普遍采用的原始值和其他基础类型。
- [字符串与文本](strings-and-text.md) — 创建和处理 Unicode 字符串，使用正则表达式查找模式，并对文本执行自然语言分析。
- [集合](collections.md) — 使用数组、字典、集合和专用集合来存储和迭代对象组或值组。
- [单位与测量](units-and-measurement.md) — 为数值标注物理维度，以便进行区域设置感知的格式化和相关单位间转换。
- [数据格式化](data-formatting.md) — 在数值、日期、测量值及其他值与区域设置感知的字符串表示之间进行转换。
- [筛选与排序](filters-and-sorting.md) — 使用谓词、表达式和排序描述符检查集合及其他服务中的元素。
