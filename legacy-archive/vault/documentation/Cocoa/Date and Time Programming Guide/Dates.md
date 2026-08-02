---
title: 日期与时间编程指南
apple_id: 10000039i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/Articles/dtDates.html
archived_at: '2026-07-15T07:14:37.433655Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [日期与时间编程指南](About%20Dates%20and%20Times.md)


[下一页](Calendars%2C%20Date%20Components%2C%20and%20Calendar%20Units.md) · [上一页](About%20Dates%20and%20Times.md)

# 日期

日期对象允许你以可用于日期计算和转换的方式表示日期与时间。日期对象表示绝对时间点，因此不受地区、时区和日历影响，始终具有明确含义。

Cocoa 使用 [NSDate](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/cl/NSDate) 对象表示日期与时间。`NSDate` 是 Cocoa 的基本[值对象](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ValueObject.html#//apple_ref/doc/uid/TP40008195-CH51)之一。日期对象表示一个不变的时间点。由于日期是时间中的一个点，因此它既包含某一天，也隐含具体的时钟时间；所以无法定义一个只有日期而没有时间的日期对象。

要理解 Cocoa 如何处理日期，还必须了解 [NSCalendar](https://developer.apple.com/documentation/foundation/nscalendar) 和 [NSDateComponents](https://developer.apple.com/documentation/foundation/nsdatecomponents) 对象。在非技术语境中，一个时间点通常由时钟时间和特定日历（例如公历或希伯来历）中的某一天共同表示。支持不同日历对于[本地化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Internationalization.html#//apple_ref/doc/uid/TP40008195-CH23)很重要。在 Cocoa 中，你可以使用特定日历，将日期对象拆分成年、月、日、小时和分钟等日期组件。反过来，也可以使用日历，根据日期组件创建日期对象。[日历、日期组件与日历单位](Calendars%2C%20Date%20Components%2C%20and%20Calendar%20Units.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztinzqfvjvomi)中更详细地介绍了日历对象和日期组件对象。

`NSDate` 提供了用于创建日期、比较日期和计算时间间隔的方法。日期对象是[不可变](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectMutability.html#//apple_ref/doc/uid/TP40008195-CH42)的。日期对象的标准时间单位是以秒表示、类型为 [NSTimeInterval](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/tdef/NSTimeInterval) 的浮点值。该类型既可表示很大的日期与时间范围，也具有很高的精度；即使两个日期相隔 10,000 年，仍能达到毫秒以内的精度。

`NSDate` 以相对于一个绝对参考时间的秒数计算时间：格林尼治标准时间（GMT）2001 年 1 月 1 日的第一个瞬间。早于该时间的日期存储为负数，晚于该时间的日期存储为正数。`NSDate` 唯一的基础方法 [timeIntervalSinceReferenceDate](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/clm/NSDate/timeIntervalSinceReferenceDate)，为 `NSDate` 接口中的其他所有方法提供了基础。`NSDate` 会在各种日期和时间表示与相对于绝对参考日期的 [NSTimeInterval](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/tdef/NSTimeInterval) 值之间进行转换。

Cocoa 按照网络时间协议（NTP）标准实现时间，该标准以协调世界时为基础。

如果想要一个表示当前时间的日期，可分配一个 `NSDate` 对象并使用 `init` 初始化：

```objc
NSDate *now = [[NSDate alloc] init];
```

也可以使用 `NSDate` 的类方法 [date](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/clm/NSDate/date) 创建日期对象。如果需要当前时间以外的时间，可以使用 `NSDate` 的某个 `initWithTimeInterval...` 或 `dateWithTimeInterval...` 方法；不过通常会采用更完善的方式，即按照[日历基础知识](Calendars%2C%20Date%20Components%2C%20and%20Calendar%20Units.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztinzqfvjvomq)中的说明，结合使用日历和日期组件。

`initWithTimeInterval...` 方法会相对于方法名称所指明的特定时间初始化日期对象。你以秒为单位，指定日期对象相对该时间要晚多久或早多久。要指定一个早于该方法参考日期的日期，请使用负秒数。

清单 1 定义了两个日期对象。`tomorrow` 对象正好比当前日期与时间晚 24 小时，`yesterday` 则正好早 24 小时。

__清单 1__　使用时间间隔创建日期

```objc
NSTimeInterval secondsPerDay = 24 * 60 * 60;
NSDate *tomorrow = [[NSDate alloc] initWithTimeIntervalSinceNow:secondsPerDay];
NSDate *yesterday = [[NSDate alloc] initWithTimeIntervalSinceNow:-secondsPerDay];
```

清单 2 展示了如何使用 `dateByAddingTimeInterval:`，基于现有日期对象调整日期与时间值，从而获得新的日期对象。

__清单 2__　通过添加时间间隔创建日期

```objc
NSTimeInterval secondsPerDay = 24 * 60 * 60;
NSDate *today = [[NSDate alloc] init];
NSDate *tomorrow, *yesterday;

tomorrow = [today dateByAddingTimeInterval:secondsPerDay];
yesterday = [today dateByAddingTimeInterval:-secondsPerDay];
```


要[比较](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectComparison.html#//apple_ref/doc/uid/TP40008195-CH37)日期，可以使用 `isEqualToDate:`、`compare:`、`laterDate:` 和 `earlierDate:` 方法。这些方法执行精确比较，也就是说，它们能检测到日期之间不足一秒的差异。你也可能希望以较粗的粒度比较日期。例如，两个日期相差不到一分钟时，可以将它们视为相等。在这种情况下，请使用 `timeIntervalSinceDate:` 比较两个日期。下面的代码片段展示了如何使用 `timeIntervalSinceDate:` 判断两个日期是否相差不到一分钟（60 秒）。

```objc
if (fabs([date2 timeIntervalSinceDate:date1]) < 60) {
    // …
}
```

要获取日期对象与另一时间点之间的差值，可向该日期对象发送 `timeIntervalSince...` [消息](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Message.html#//apple_ref/doc/uid/TP40008195-CH59)。例如，`timeIntervalSinceNow` 会以秒为单位，给出当前时间与接收该消息的日期对象之间的时间差。

要获取日期的组成部分（例如星期几），请结合使用 `NSDateComponents` 对象和 `NSCalendar` 对象。[日历基础知识](Calendars%2C%20Date%20Components%2C%20and%20Calendar%20Units.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztinzqfvjvomq)介绍了这种方法。

[下一页](Calendars%2C%20Date%20Components%2C%20and%20Calendar%20Units.md) · [上一页](About%20Dates%20and%20Times.md)
