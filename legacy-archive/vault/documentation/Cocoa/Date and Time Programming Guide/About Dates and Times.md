---
title: 日期与时间编程指南
apple_id: 10000039i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html
archived_at: '2026-07-15T07:14:38.449676Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md)


[下一页](Dates.md)

# 关于日期与时间

日期与时间对象允许你存储对特定时刻的引用。你可以使用日期与时间对象执行计算和比较，并妥善处理日期与时间计算中的各种边界情况。

![日历图标](attachments/Art/iCal.png)

处理日期与时间时主要使用以下三个类：

- [NSDate](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/cl/NSDate) 用于表示绝对时间点。
- [NSCalendar](https://developer.apple.com/documentation/foundation/nscalendar) 用于表示特定的日历，例如公历或希伯来历。它提供了大多数基于日期的计算接口，并允许你在 `NSDate` 对象与 `NSDateComponents` 对象之间进行转换。
- [NSDateComponents](https://developer.apple.com/documentation/foundation/nsdatecomponents) 用于表示特定日期的组成部分，例如小时、分钟、日、年等。

除了这些类之外，[NSTimeZone](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTimeZoneClassCluster/Description.html#//apple_ref/occ/cl/NSTimeZone) 还用于表示某个地缘政治区域的时区信息。它简化了跨时区处理，以及执行可能受夏令时切换影响的计算等任务。

在 Cocoa 中，日期对象表示日期与时间。日期对象允许你存储绝对时间点；无论地区、日历和时区如何，这些时间点都具有明确含义。

日期组件允许你将一个日期拆分为组成它的各个部分，例如日、月、年、小时等。日历表示一种特定的计时体系，例如公历或中国农历。日历对象允许你在日期对象与日期组件对象之间转换，也可在不同日历之间转换。

日历和日期组件可用于执行各种计算，例如计算两个日期之间相隔的天数或小时数，或查找本周的星期日。你还可以为日期添加组件，或判断某个日期落在何时。

时区对象允许你将绝对时间显示为本地时间，也就是墙上时钟所显示的时间。除了时间偏移量之外，它们还会跟踪夏令时差异。正确使用时区对象，可避免因夏令时切换或用户前往其他时区而错误计算已用时间等问题。

历史日期存在许多现代日期不会遇到的边界情况。这些情况包括某些日期在特定日历中并不存在——例如公历没有公元 0 年——或者发生过历法转换——例如中世纪从儒略历过渡到公历。此外，某些纪元中的时间看起来会倒流，例如公历中的公元前年份。

如果你的应用需要跟踪日期与时间，请阅读从[日期](Dates.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge4dglkcineuiqsbirba)到[使用时区](Using%20Time%20Zones.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge4dklkcijbuerchjfca)的各章。这些章节中介绍的 [NSDate](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/cl/NSDate)、[NSCalendar](https://developer.apple.com/documentation/foundation/nscalendar)、[NSDateComponents](https://developer.apple.com/documentation/foundation/nsdatecomponents) 和 [NSTimeZone](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTimeZoneClassCluster/Description.html#//apple_ref/occ/cl/NSTimeZone) 类相互配合，用于存储、比较和操作日期与时间。

如果你的应用需要处理历史日期——尤其是 20 世纪初以前的日期——还应阅读[历史日期](Historical%20Dates.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydenbqfvjvomi)，了解处理历史日期时可能出现的一些问题。

如果你需要向用户显示日期与时间，或根据用户输入创建日期，请阅读：

- _[数据格式化指南](../Data%20Formatting%20Guide/Introduction%20to%20Data%20Formatting%20Programming%20Guide%20For%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgazds2i)_，其中说明了如何根据日期对象创建并格式化用户可读的字符串，以及如何根据格式化字符串创建日期对象。

[下一页](Dates.md)
