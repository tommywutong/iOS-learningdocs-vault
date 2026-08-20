---
title: 日期与时间编程指南
apple_id: 10000039i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/Articles/dtHist.html
archived_at: '2026-07-15T07:14:37.935391Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [日期与时间编程指南](About%20Dates%20and%20Times.md)


[下一页](Document%20Revision%20History.md) · [上一页](Using%20Time%20Zones.md)

# 历史日期

处理历史日期时会遇到许多现代日期中不存在的问题，包括并不存在的日期、年份编号从大到小推进的早期纪元（例如公历中的公元前日期），以及历法转换（例如从儒略历转换到公历）。

`NSGregorianCalendar` 所表示的儒略历和公历都没有 0 年。这意味着公元前 1 年 12 月 31 日的下一天是公元 1 年 1 月 1 日。系统提供的所有日历计算方法都会考虑这一点，但根据组件创建日期时，你可能需要自行注意。如果尝试创建年份为 0 的日期，得到的实际是公元前 1 年。此外，如果使用负年份值根据组件创建日期，系统会采用天文纪年法：0 对应公元前 1 年，-1 对应公元前 2 年，依此类推。例如，清单 17 中创建的两个日期等价地表示公元前 8 年 5 月 7 日。

__清单 17__　使用负年份表示公元前日期

```objc
NSCalendar *gregorian = [[NSCalendar alloc] initWithCalendarIdentifier:NSGregorianCalendar];

NSDateComponents *bceDateComponents = [[NSDateComponents alloc] init];
[bceDateComponents setMonth:5];
[bceDateComponents setDay:7];
[bceDateComponents setYear:8];
[bceDateComponents setEra:0];

NSDateComponents *astronomicalDateComponents = [[NSDateComponents alloc] init];
[astronomicalDateComponents setMonth:5];
[astronomicalDateComponents setDay:7];
[astronomicalDateComponents setYear:-7];

NSDate *bceDate = [gregorian dateFromComponents:bceDateComponents];
NSDate *astronomicalDate = [gregorian dateFromComponents:astronomicalDateComponents];
```


[NSCalendar](https://developer.apple.com/documentation/foundation/nscalendar) 对 1582 年 10 月从儒略历向公历的转换进行了建模。转换期间跳过了 10 天，也就是说，1582 年 10 月 4 日的下一天是 1582 年 10 月 15 日。系统提供的所有日历计算方法都会考虑这一点，但根据组件创建日期时，你可能需要自行注意。在空缺日期范围内创建的日期会向后顺延 10 天。例如，1582 年 10 月 8 日会存储为 1582 年 10 月 18 日。

有些国家在更晚的不同时期才采用公历。不过，为保持一致，无论地区如何，系统都将历法转换建模在同一时间。如果需要特定地区绝对准确的历史日期，可以从公历给出的日期中减去适当的天数。要减去的天数与儒略历中额外闰日的数量相对应。因此，每到整百年份，如果该年不是 400 的倍数，儒略历就会多出一个闰日。若要创建儒略历日期，必须从公历日期中减去正确的天数（16、17 世纪减 10 天，18 世纪减 11 天，19 世纪减 12 天，20、21 世纪减 13 天，依此类推）。还必须考虑公历中不存在的闰日。

在公历中，时间分为两个纪元：公元前和公元。在公元前纪元中，时间看起来是倒着推进的，即年份编号从大变小。不过，日和月仍按正常方向推进。例如，1 月 31 日的下一天是 2 月 1 日。因此，如果问公元前 7 年 12 月 31 日的下一天是哪一天，可能会令人困惑；正确答案是公元前 6 年 1 月 1 日。清单 18 展示了这个例子。

__清单 18__　公元前纪元中的明天

```objc
NSCalendar *gregorian = [[NSCalendar alloc] initWithCalendarIdentifier: NSGregorianCalendar];
NSDateComponents *dateBCEComps = [[NSDateComponents alloc] init];
[dateBCEComps setEra:0]; // 纪元 0 对应公元前
[dateBCEComps setMonth:12];
[dateBCEComps setDay:31];
[dateBCEComps setYear:7];

NSDate *dateBCE = [gregorian dateFromComponents:dateBCEComps];
NSDateComponents *offsetDate = [[NSDateComponents alloc] init];
[offsetDate setDay:1];
NSDate *dateBCE2 = [gregorian dateByAddingComponents: offsetDate toDate:dateBCE options:0];
```

这段代码执行后，`dateBCE2` 对应公元前 6 年 1 月 1 日。

[下一页](Document%20Revision%20History.md) · [上一页](Using%20Time%20Zones.md)
