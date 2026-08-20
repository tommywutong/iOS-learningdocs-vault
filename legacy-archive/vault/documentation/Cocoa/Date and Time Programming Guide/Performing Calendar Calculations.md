---
title: 日期与时间编程指南
apple_id: 10000039i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/Articles/dtCalendricalCalculations.html
archived_at: '2026-07-15T07:14:36.936414Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [日期与时间编程指南](About%20Dates%20and%20Times.md)


[下一页](Using%20Time%20Zones.md) · [上一页](Calendars%2C%20Date%20Components%2C%20and%20Calendar%20Units.md)

# 执行日历计算

`NSDate` 为日期与时间提供绝对时间尺度和纪元，随后可以将其呈现到特定日历中，以便执行日历计算或向用户显示。执行日历计算时，通常需要获取日期的组成元素，例如年、月和日。应使用系统提供的方法来处理日历计算，因为这些方法会考虑夏令时开始或结束以及闰年等边界情况。

可以使用 [dateByAddingComponents:toDate:options:](https://developer.apple.com/documentation/foundation/nscalendar/1409577-date) 方法，为现有日期添加日期组件（例如小时或月）。你可以提供任意数量的组件。清单 9 展示了如何计算一个半小时后的日期。

__清单 9__　从现在起一个半小时后

```objc
NSDate *today = [[NSDate alloc] init];
NSCalendar *gregorian = [[NSCalendar alloc] initWithCalendarIdentifier:NSGregorianCalendar];
NSDateComponents *offsetComponents = [[NSDateComponents alloc] init];
[offsetComponents setHour:1];
[offsetComponents setMinute:30];
// 计算汤姆·莱勒所说的第三次世界大战将于何时结束
NSDate *endOfWorldWar3 = [gregorian dateByAddingComponents:offsetComponents toDate:today options:0];
```

要添加的组件可以为负数。清单 10 展示了如何获取本周的星期日（使用公历）。

__清单 10__　获取本周的星期日

```objc
NSDate *today = [[NSDate alloc] init];
NSCalendar *gregorian = [[NSCalendar alloc] initWithCalendarIdentifier:NSGregorianCalendar];

// 获取当前日期的星期组件
NSDateComponents *weekdayComponents = [gregorian components:NSWeekdayCalendarUnit fromDate:today];

/*
创建一个日期组件，用于表示需要从当前日期减去的天数。
在公历中，星期日的星期值为 1，因此将待计算日期的星期值减去 1，即可得到需要减去的天数。（如果今天是星期日，则减去 0 天。）
*/
NSDateComponents *componentsToSubtract = [[NSDateComponents alloc] init];
[componentsToSubtract setDay:(0 - ([weekdayComponents weekday] - 1))];

NSDate *beginningOfWeek = [gregorian dateByAddingComponents:componentsToSubtract toDate:today options:0];

/*
可选步骤：
beginningOfWeek 目前的小时、分钟和秒与原日期（今天）相同。
要将时间归一化到午夜，请提取年、月和日组件，并根据这些组件创建新日期。
*/
NSDateComponents *components = [gregorian components:(NSYearCalendarUnit | NSMonthCalendarUnit | NSDayCalendarUnit) fromDate:beginningOfWeek];
beginningOfWeek = [gregorian dateFromComponents:components];
```

并非所有地区都以星期日作为一周的开始。清单 11 展示了如何计算一周开始的时刻（由日历的地区设置定义）：

__清单 11__　获取一周的开始

```objc
NSDate *today = [[NSDate alloc] init];
NSDate *beginningOfWeek = nil;
BOOL ok = [gregorian rangeOfUnit:NSWeekCalendarUnit startDate:&beginningOfWeek interval:NULL forDate:today];
```


计算日期间隔有多种方式。用户期望的行为可能随计算场景而不同。无论使用哪种计算，都应让用户清楚了解计算方式。由于 Cocoa 按照 NTP 标准实现时间，这些方法在计算中会忽略闰秒。可以使用 [components:fromDate:toDate:options:](https://developer.apple.com/documentation/foundation/nscalendar/1407925-components)，以秒以外的单位确定两个日期之间的时间差（秒数可使用 `NSDate` 的 [timeIntervalSinceDate:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/instm/NSDate/timeIntervalSinceDate:) 方法计算）。清单 12 展示了如何使用公历获取两个日期之间相隔的月数和天数。

__清单 12__　获取两个日期之间的差值

```objc
NSDate *startDate = ...;
NSDate *endDate = ...;

NSCalendar *gregorian = [[NSCalendar alloc] initWithCalendarIdentifier:NSGregorianCalendar];

NSUInteger unitFlags = NSMonthCalendarUnit | NSDayCalendarUnit;

NSDateComponents *components = [gregorian components:unitFlags fromDate:startDate  toDate:endDate options:0];
NSInteger months = [components month];
NSInteger days = [components day];
```

该方法会按预期处理溢出。如果 _fromDate:_ 与 _toDate:_ 参数相隔一年零 3 天，而你只请求两者间的天数，则返回的 `NSDateComponents` 对象中，日组件值为 368（闰年为 369）。不过，该方法会将计算结果截断到所提供的最小单位。例如，如果 _fromDate:_ 参数对应 2010 年 1 月 14 日晚上 11:30，_toDate:_ 参数对应 2010 年 1 月 15 日上午 8:00，那么两个日期之间仅相隔 8.5 小时。如果请求天数，结果为 0，因为 8.5 小时不足 1 天。在某些场景中，结果可能应该是 1 天。你必须根据具体情况决定用户期望哪种行为。如果确实需要按两个日期之间经过的午夜次数来计算并返回天数，可以像清单 13 那样为 `NSCalendar` 添加一个[类别](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Category.html#//apple_ref/doc/uid/TP40008195-CH5)。

__清单 13__　按经过的午夜次数计算两个日期间的天数

```objc
@implementation NSCalendar (MySpecialCalculations)
- (NSInteger)daysWithinEraFromDate:(NSDate *)startDate toDate:(NSDate *)endDate {
     NSInteger startDay=[self ordinalityOfUnit:NSDayCalendarUnit inUnit: NSEraCalendarUnit forDate:startDate];
     NSInteger endDay=[self ordinalityOfUnit:NSDayCalendarUnit  inUnit: NSEraCalendarUnit forDate:endDate];
     return endDay - startDay;
}
@end
```

通过为 _ordinalityOfUnit:_ 参数指定不同的 `NSCalendarUnit` 值，这种方法也适用于其他日历单位。例如，可以根据两个日期之间经过了多少次 1 月 1 日午夜 12:00 来计算年数。

不要使用这种方法比较秒数差，因为它会在 32 位平台上导致 `NSInteger` 溢出。该方法仅在两个日期处于同一纪元时有效（在公历中，这意味着两个日期必须同为公元日期或同为公元前日期）。如果确实需要跨越纪元边界比较日期，可以使用类似清单 14 中类别的方法。

__清单 14__　不同纪元中两个日期间的天数

```objc
@implementation NSCalendar (MyOtherMethod)
- (NSInteger)daysFromDate:(NSDate *)startDate toDate:(NSDate *)endDate {
     NSCalendarUnit units = NSEraCalendarUnit | NSYearCalendarUnit | NSMonthCalendarUnit | NSDayCalendarUnit;
     NSDateComponents *comp1 = [self components:units fromDate:startDate];
     NSDateComponents *comp2 = [self components:units fromDate endDate];
     [comp1 setHour:12];
     [comp2 setHour:12];
     NSDate *date1 = [self dateFromComponents: comp1];
     NSDate *date2 = [self dateFromComponents: comp2];
     return [[self components:NSDayCalendarUnit fromDate:date1 toDate:date2 options:0] day];
}
@end
```

该方法根据给定日期创建组件，然后将时间归一化并比较两个日期。这种计算的开销大于同一纪元内的日期比较。如果不需要跨越纪元边界，请改用[清单 13](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqmzwfvjvoni)所示的方法。

如果需要判断某个日期是否位于本周内（或任何其他单位内），可以使用 `NSCalendar` 的 [rangeOfUnit:startDate:interval:forDate:](https://developer.apple.com/documentation/foundation/nscalendar/1408013-range) 方法。清单 15 展示了一个用于判断给定日期是否位于本周内的方法。在本例中，一周定义为从星期日午夜到下一个星期六午夜前一刻的时间段（使用公历）。

__清单 15__　判断日期是否位于本周

```objc
- (BOOL)isDateThisWeek:(NSDate *)date {
     NSDate *start;
     NSTimeInterval extends;
     NSCalendar *calendar = [NSCalendar autoupdatingCurrentCalendar];
     NSDate *today = [NSDate date];
     BOOL success = [calendar rangeOfUnit:NSWeekCalendarUnit startDate:&start interval:&extends forDate:today];
     if(!success) {
         return NO;
     }

     NSTimeInterval dateInSecs = [date timeIntervalSinceReferenceDate];
     NSTimeInterval dayStartInSecs = [start timeIntervalSinceReferenceDate];

     return dateInSecs > dayStartInSecs && dateInSecs < (dayStartInSecs + extends)
}
```

该代码分别取得待测试日期和本周起点的 [NSTimeInterval](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/tdef/NSTimeInterval) 值，并用它们判断该日期是否位于本周。

基于周的日历按一年中的各周定义。它不使用日期的年、月、日，而是使用周年、周数和星期几来定义日期。

不过，当日历中的第一周与上一日历年的最后一周重叠时，情况会变得复杂。此时，日历有两个重要属性：

1. 一周的第一天是哪一天？
2. 年初附近的一周必须有多少天位于普通日历年内，才会被视为基于周的日历年中的第一周？

基于周的日历以一周的第一天作为一年的第一天。如果包含 1 月 1 日的那一周满足上述第二项所定义的条件，则优先将它作为第一周。

例如，假设在公历的基于周解释中，将星期一定义为一周的第一天。请看表 1 和表 2 所示的 2009/2010 年过渡：

__表 1__　2009 年 12 月日历

| 星期日 | 星期一 | 星期二 | 星期三 | 星期四 | 星期五 | 星期六 |
| --- | --- | --- | --- | --- | --- | --- |
| 20 | 21 | 22 | 23 | 24 | 25 | 26 |
| 27 | 28 | 29 | 30 | 31 |  |  |

__表 2__　2010 年 1 月日历

| 星期日 | 星期一 | 星期二 | 星期三 | 星期四 | 星期五 | 星期六 |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | 1 | 2 |
| 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| 10 | 11 | 12 | 13 | 14 | 15 | 16 |

由于一周的第一天是星期一，基于周的 2010 日历年可以从 12 月 28 日或 1 月 4 日开始。也就是说，普通日历中的 2009 年 12 月 30 日，在基于周的日历中可能属于 2010 日历年。

要在这两种可能性之间做出选择，需要使用第二项标准。12 月 28 日至 1 月 3 日这一周有 3 天位于 2010 年，而 1 月 4 日至 1 月 10 日这一周有 7 天位于 2010 年。

如果第一周的最少天数定义为 1、2 或 3，则 12 月 28 日所在周满足第一周标准，会成为基于周的 2010 日历年的第 1 周。否则，1 月 4 日所在周为第一周。

再举一个例子，假设你想定义一种基于周的日历，使日历年的第一周从某个特定星期几在该年首次出现时开始。

在[表 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqmzwfvjvomjx)中，1 月 4 日星期一是普通日历年中的第一个星期一，因此基于周的日历从这一天开始。换句话说，你要求基于周的日历第一周完全位于新的普通日历年内，也就是第一周的最少天数为 7。

[NSYearForWeekOfYearCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendar/unit/1408285-nsyearforweekofyearcalendarunit) 是当前日历在基于周的解释下的年份编号。上文所讨论的基于周日历的两个属性，分别对应 `NSCalendar` 的 [firstWeekday](https://developer.apple.com/documentation/foundation/nscalendar/1408310-firstweekday) 和 [minimumDaysInFirstWeek](https://developer.apple.com/documentation/foundation/nscalendar/1410186-minimumdaysinfirstweek) 属性。

[下一页](Using%20Time%20Zones.md) · [上一页](Calendars%2C%20Date%20Components%2C%20and%20Calendar%20Units.md)
