---
title: NSWrapCalendarComponents
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nswrapcalendarcomponents-api
source_url: 'https://developer.apple.com/documentation/foundation/nswrapcalendarcomponents-api'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nswrapcalendarcomponents-api.json'
content_hash: 'sha256:344a7635ad49e60a'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [日期与时间](dates-and-times.md) · [NSCalendar](nscalendar.md)

# NSWrapCalendarComponents

<sub>API 集合</sub>

一个用于控制日期计算中溢出的旧式常量。

## 概述

> [!warning] 已废弃
> 请改用 [NSCalendarWrapComponents](nscalendar/options/wrapcomponents.md)。

## 主题

### 常量

- [NSWrapCalendarComponents](nswrapcalendarcomponents.md) — 指定应递增 `NSDateComponents` 对象所指定的分量，并在溢出时环绕到零/一，但不应导致更高单位递增。 _(已废弃)_

## 另请参阅

### 扫描日期

- [- startOfDayForDate:](<nscalendar/startofday(for_).md>) — 以日期实例形式返回给定日期的第一个时刻。
- [- enumerateDatesStartingAfterDate:matchingComponents:options:usingBlock:](<nscalendar/enumeratedates(startingafter_matching_options_using_).md>) — 计算与给定分量集合匹配（或最接近匹配）的日期，并为每个日期调用一次 block，直到枚举停止。
- [- nextDateAfterDate:matchingComponents:options:](<nscalendar/nextdate(after_matching_options_).md>) — 返回给定日期之后与给定分量匹配的下一个日期。
- [- nextDateAfterDate:matchingHour:minute:second:options:](<nscalendar/nextdate(after_matchinghour_minute_second_options_).md>) — 返回给定日期之后与给定小时、分钟和秒分量值匹配的下一个日期。
- [- nextDateAfterDate:matchingUnit:value:options:](<nscalendar/nextdate(after_matching_value_options_).md>) — 返回给定日期之后与给定日历单位值匹配的下一个日期。
- [Options](nscalendar/options.md) — 涉及日历的算术操作选项。
