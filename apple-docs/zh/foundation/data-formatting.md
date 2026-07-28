---
title: 数据格式化
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/data-formatting
source_url: 'https://developer.apple.com/documentation/foundation/data-formatting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data-formatting.json'
content_hash: 'sha256:4590ba992836842e'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md)

# 数据格式化

<sub>API 集合</sub>

在数值、日期、测量值及其他值与区域设置感知的字符串表示之间进行转换。

## 概述

Foundation 支持两种数据格式化方法：

- 在 Swift 中工作时，直接对要格式化的类型使用 `formatted` 方法，还可以选择使用 [FormatStyle](formatstyle.md) 及其子类型来自定格式化器输出。此方法支持日期、整数、浮点数、测量值、序列和人名组件。Foundation 会在内部缓存配置相同的格式化器实例，让你能够专注于 App 的格式化需求。
- 在 Objective-C 中，创建 [Formatter](formatter.md) 及其子类型的实例，并使用 [- stringForObjectValue:](<formatter/string(for_).md>) 方法将对象转换为格式化字符串。

## 主题

### 基础

- [构建本地化的餐饮订购 App](building-a-localized-food-ordering-app.md) — 使用字符串格式化、属性字符串和自动语法一致性，对 App 的文本进行格式化、设置样式和本地化，以供多种语言使用。
- [显示易于理解的内容](displaying-human-friendly-content.md) — 使用格式化器将数据转换为可读字符串或 Swift 对象。

### Swift 中的数据格式化

- [Language Introspector](language-introspector.md) — 使用格式化器和区域设置将数据转换为易读文本。
- [FormatStyle](formatstyle.md) — 将给定数据类型转换为另一种类型表示（例如字符串）的类型。
- [IntegerFormatStyle](integerformatstyle.md) — 在整数值与其文本表示之间进行转换的结构体。
- [FloatingPointFormatStyle](floatingpointformatstyle.md) — 在浮点值与其文本表示之间进行转换的结构体。
- [FormatStyle](decimal/formatstyle.md) — 在十进制值与其文本表示之间进行转换的结构体。
- [ListFormatStyle](listformatstyle.md) — 使用适合给定区域设置的分隔符和连词来格式化项目列表的类型。
- [StringStyle](stringstyle.md)
- [FormatStyle](url/formatstyle.md) — 在 URL 实例与其文本表示之间进行转换的结构体。
- [FormatStyleCapitalizationContext](formatstylecapitalizationcontext.md) — 格式化日期和时间时使用的大小写格式化上下文。
- [格式样式配置](format-style-configurations.md) — 用于格式化和解析数值的行为，例如数值精度、舍入和比例等特性。

### Swift 中的数据解析

- [ParseableFormatStyle](parseableformatstyle.md) — 可将给定输入数据类型转换为输出类型表示的类型。
- [ParseStrategy](parsestrategy.md) — 将输入表示（例如格式化字符串）解析为所提供数据类型的类型。
- [IntegerParseStrategy](integerparsestrategy.md) — 从格式化字符串创建整数值的解析策略。
- [FloatingPointParseStrategy](floatingpointparsestrategy.md) — 从格式化字符串创建浮点值的解析策略。
- [ParseStrategy](decimal/parsestrategy.md) — 从格式化字符串创建十进制值的解析策略。

### 数值与货币

- [NumberFormatter](numberformatter.md) — 在数值及其文本表示之间进行转换的格式化器。

### 姓名

- [PersonNameComponentsFormatter](personnamecomponentsformatter.md) — 提供人名各组件本地化表示的格式化器。
- [PersonNameComponents](personnamecomponents.md) — 人名的各个独立部分，支持区域设置感知的格式化。

### 日期与时间

- [DateFormatter](dateformatter.md) — 在日期及其文本表示之间进行转换的格式化器。
- [DateComponentsFormatter](datecomponentsformatter.md) — 创建时长的字符串表示的格式化器。
- [RelativeDateTimeFormatter](relativedatetimeformatter.md) — 创建相对日期或时间的区域设置感知字符串表示的格式化器。
- [DateIntervalFormatter](dateintervalformatter.md) — 创建时间间隔字符串表示的格式化器。
- [ISO8601DateFormatter](iso8601dateformatter.md) — 在日期及其 ISO 8601 字符串表示之间进行转换的格式化器。

### 数据大小

- [ByteCountFormatter](bytecountformatter.md) — 将字节数值转换为本地化描述的格式化器，该描述使用适当的字节修饰符（KB、MB、GB 等）进行格式化。

### 测量值

- [MeasurementFormatter](measurementformatter.md) — 提供单位和测量值本地化表示的格式化器。

### 列表

- [ListFormatter](listformatter.md) — 使用适当的分隔符和连词，以符合区域设置的方式格式化项目列表的对象。

### 国际化

- [Locale](locale.md) — 用于格式化待呈现数据的语言、文化和技术惯例信息。

### 自定格式化器

- [Formatter](formatter.md) — 声明接口的抽象类，供创建、解释和验证值的文本表示的对象使用。

### 自动语法一致性

- [InflectionRule](inflectionrule.md) — 影响属性字符串如何执行自动语法一致性的规则。
- [Morphology](morphology.md) — 字符串语法属性的描述。
- [TermOfAddress](termofaddress.md) — 表示本地化文本中语法性别的类型。
- [InflectionConcept](inflectionconcept.md) — 本地化文本时使用的词形变化方法。
- [Pronoun](morphology/pronoun.md) — 用于指代第三人称的自定代词。

### 已废弃

- [LengthFormatter](lengthformatter.md) — 提供线性距离（例如长度和高度测量值）本地化描述的格式化器。
- [MassFormatter](massformatter.md) — 提供质量和重量值本地化描述的格式化器。
- [EnergyFormatter](energyformatter.md) — 提供能量值本地化描述的格式化器。

## 另请参阅

### 基础

- [数字、数据与基本值](numbers-data-and-basic-values.md) — 使用 Cocoa 中普遍采用的原始值和其他基础类型。
- [字符串与文本](strings-and-text.md) — 创建和处理 Unicode 字符串，使用正则表达式查找模式，并对文本执行自然语言分析。
- [集合](collections.md) — 使用数组、字典、集合和专用集合来存储和迭代对象组或值组。
- [日期与时间](dates-and-times.md) — 比较日期与时间，并执行日历和时区计算。
- [单位与测量](units-and-measurement.md) — 为数值标注物理维度，以便进行区域设置感知的格式化和相关单位间转换。
- [筛选与排序](filters-and-sorting.md) — 使用谓词、表达式和排序描述符检查集合及其他服务中的元素。
