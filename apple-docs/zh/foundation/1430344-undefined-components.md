---
title: 未定义分量
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/1430344-undefined-components
source_url: 'https://developer.apple.com/documentation/foundation/1430344-undefined-components'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/1430344-undefined-components.json'
content_hash: 'sha256:6c63ab037dba00a4'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md) · [Dates and Times](dates-and-times.md) · [NSDateComponents](nsdatecomponents.md)

# 未定义分量

<sub>API 集合</sub>

表示某个日期分量的值未定义的常量。

## 概述

举例来说，当某个 [NSDateComponents](nsdatecomponents.md) 对象是通过计算某个特定日历所表示的两个日期之间的时间距离而创建时，[NSCalendarUnitWeekOfYear](nscalendar/unit/weekofyear.md) 分量的值就会被设置为 [NSDateComponentUndefined](nsdatecomponentundefined.md)。

## 主题

### 常量

- [NSDateComponentUndefined](nsdatecomponentundefined.md) — 指定一个没有值的日期分量。
- [NSUndefinedDateComponent](nsundefineddatecomponent.md) — 指定一个没有值的日期分量。_(已废弃)_

## 另请参阅

### Validating a Date

- [validDate](nsdatecomponents/isvaliddate.md) — 一个布尔值，指示当前属性组合是否表示当前日历中存在的一个日期。
- [- isValidDateInCalendar:](<nsdatecomponents/isvaliddate(in_).md>) — 返回一个布尔值，指示当前属性组合是否表示指定日历中存在的一个日期。
- [date](nsdatecomponents/date.md) — 使用所存储的日历，根据当前分量计算出的日期。
