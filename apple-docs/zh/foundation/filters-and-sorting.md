---
title: 筛选与排序
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filters-and-sorting
source_url: 'https://developer.apple.com/documentation/foundation/filters-and-sorting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filters-and-sorting.json'
content_hash: 'sha256:114e3e3d94f58e61'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md)

# 筛选与排序

<sub>API 集合</sub>

使用谓词、表达式和排序描述符检查集合及其他服务中的元素。

## 主题

### 筛选

- [Predicate](predicate.md) — 用于测试一组输入值以进行搜索或筛选的逻辑条件。
- [PredicateError](predicateerror.md) — 评估谓词时抛出的错误。
- [PredicateCodableConfiguration](predicatecodableconfiguration.md) — 对归档谓词中预期类型和键路径的说明。
- [PredicateCodableKeyPathProviding](predicatecodablekeypathproviding.md) — 提供归档谓词中预期键路径的类型。
- [PredicateExpression](predicateexpression.md) — 构成谓词一部分的组件表达式。
- [StandardPredicateExpression](standardpredicateexpression.md) — 构成谓词一部分且受标准谓词类型支持的组件表达式。
- [PredicateExpressions](predicateexpressions.md) — 构成谓词的表达式。
- [PredicateBindings](predicatebindings.md) — 从谓词的输入变量到其值的映射。
- [NSPredicate](nspredicate.md) — 用于约束获取搜索或内存筛选的逻辑条件定义。
- [NSExpression](nsexpression.md) — 用于比较谓词的表达式。
- [NSComparisonPredicate](nscomparisonpredicate.md) — 用于比较表达式的特殊谓词。
- [NSCompoundPredicate](nscompoundpredicate.md) — 评估其他谓词逻辑组合的特殊谓词。

### 排序

- [NSSortDescriptor](nssortdescriptor.md) — 根据所有对象共有的属性，对对象集合进行排序方式的不可变描述。
- [ComparisonResult](comparisonresult.md) — 表明排序顺序的常量。
- [SortDescriptor](sortdescriptor.md) — 对数值和字符串排序方式的可序列化描述。
- [SortComparator](sortcomparator.md) — 用于指定类型的比较算法。
- [ComparableComparator](comparablecomparator.md) — 根据类型对 Comparable 协议的符合情况进行比较的比较器。
- [KeyPathComparator](keypathcomparator.md) — 使用另一个排序比较器对键路径处的值进行比较的比较器。
- [SortOrder](sortorder.md) — 可用于执行排序的顺序。

## 另请参阅

### 基础

- [数字、数据和基本值](numbers-data-and-basic-values.md) — 使用 Cocoa 中普遍采用的原始值和其他基础类型。
- [字符串与文本](strings-and-text.md) — 创建和处理 Unicode 字符串，使用正则表达式查找模式，并对文本执行自然语言分析。
- [集合](collections.md) — 使用数组、字典、集合和特殊集合存储并迭代对象或值的分组。
- [日期与时间](dates-and-times.md) — 比较日期和时间，并执行日历与时区计算。
- [单位与测量](units-and-measurement.md) — 使用物理维度标记数值量，以便进行区域设置感知的格式化以及相关单位之间的转换。
- [数据格式化](data-formatting.md) — 在数值、日期、测量值和其他值与区域设置感知的字符串表示之间进行转换。
