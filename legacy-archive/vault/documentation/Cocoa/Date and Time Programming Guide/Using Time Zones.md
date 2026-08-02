---
title: 日期与时间编程指南
apple_id: 10000039i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/Articles/dtTimeZones.html
archived_at: '2026-07-15T07:14:38.442324Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [日期与时间编程指南](About%20Dates%20and%20Times.md)


[下一页](Historical%20Dates.md) · [上一页](Performing%20Calendar%20Calculations.md)

# 使用时区

时区会给应用带来许多问题。请考虑以下情形：你人在纽约，此时是凌晨 12:30。你有一个应用，用来显示明天举行的所有美国职业棒球大联盟比赛。由于不同时区对“明天”的定义不同，这类情况必须谨慎处理。幸运的是，只需稍作规划并借助 `NSTimeZone` 类，就能大幅简化这项工作。

`NSTimeZone` 是一个抽象类，用于定义时区对象的行为。时区对象表示地缘政治区域，因此具有区域名称。时区对象还表示相对于格林尼治标准时间（GMT）的正负时间偏移量，以及相应的缩写（例如 `PST`）。

对于给定的 `NSDate` 对象，时区会影响日历对象所计算的日期组件值。你可以[创建](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39)一个 `NSTimeZone` 对象，并用它设置 `NSCalendar` 对象的时区。默认情况下，`NSCalendar` 在创建日历对象时使用应用（或进程）的默认时区。除非另行设置了默认时区，否则它就是“系统偏好设置”中配置的时区。

在大多数情况下，创建日期对象时应使用用户的默认时区。但有时也可能需要使用任意时区。例如，用户下周要去伦敦出差，可能希望指定某个约会采用格林尼治标准时间。`NSTimeZone` 提供了多个用于创建时区对象的类方法：[timeZoneWithName:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTimeZoneClassCluster/Description.html#//apple_ref/occ/clm/NSTimeZone/timeZoneWithName:)、[timeZoneWithAbbreviation:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTimeZoneClassCluster/Description.html#//apple_ref/occ/clm/NSTimeZone/timeZoneWithAbbreviation:) 和 [timeZoneForSecondsFromGMT:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTimeZoneClassCluster/Description.html#//apple_ref/occ/clm/NSTimeZone/timeZoneForSecondsFromGMT:)。在大多数情况下，`timeZoneWithName:` 会提供最准确的时区，因为它会针对夏令时进行调整；代价是你必须更精确地知道要为哪个地点创建时区。

要获取系统已知时区名称的完整列表，可以使用 `knownTimeZoneNames` 类方法：

```objc
NSArray *timeZoneNames = [NSTimeZone knownTimeZoneNames];
```


可以使用 [setDefaultTimeZone:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTimeZoneClassCluster/Description.html#//apple_ref/occ/clm/NSTimeZone/setDefaultTimeZone:) 在应用内设置默认时区。可以随时通过 `defaultTimeZone` 类方法访问该默认时区。使用 `localTimeZone` 类方法，可以获得一个会自动更新自身、以反映默认时区变化的时区对象。

时区在确定日期事件发生时间方面非常重要。以一个用于跟踪约会的简单日历应用为例。假设你住在芝加哥，星期二上午 10:00 要去看牙医，但星期日和星期一会待在纽约。创建该约会时，你考虑的是绝对时间，即美国中部时间上午 10:00；到了纽约后，由于所在时区不同，时间应显示为上午 11:00，但两者仍是同一个绝对时间。另一方面，如果创建一个每天早上 7:00 起床锻炼的日程，你不会希望仅仅因为前往都柏林出差，闹钟就在下午 1:00 响起；也不会希望因为身处洛杉矶，闹钟就在早上 5:00 响起。

[NSDate](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/cl/NSDate) 对象以绝对时间存储日期。例如，清单 16 中创建的 `date` 对象表示美国中部夏令时间下午 4:00、美国东部夏令时间下午 5:00，依此类推。

__清单 16__　使用特定时区根据组件创建日期

```objc
NSCalendar *gregorian = [[NSCalendar alloc] initWithCalendarIdentifier:NSGregorianCalendar];
[gregorian setTimeZone:[NSTimeZone timeZoneWithAbbreviation:@"CDT"]];
NSDateComponents *timeZoneComps = [[NSDateComponents alloc] init];
[timeZoneComps setHour:16];
// 指定适当的日、月和年
NSDate *date = [gregorian dateFromComponents:timeZoneComps];
```

如果需要创建一个独立于时区的日期，可以将该日期存储为 [NSDateComponents](https://developer.apple.com/documentation/foundation/nsdatecomponents) 对象，但同时必须存储对相应日历的某种引用。

在 iOS 中，`NSDateComponents` 对象可以包含日历、时区和日期对象。因此，可以将日历与组件一并存储。如果使用 `NSDateComponents` 类的 `date` 方法访问日期，请确保关联的时区是最新的。

`NSTimeZone` 类还提供了多个实例方法，用于确定夏令时信息：

- [isDaylightSavingTime](https://developer.apple.com/documentation/foundation/nstimezone/1387191-daylightsavingtime) 确定当前是否实行夏令时。
- [daylightSavingTimeOffset](https://developer.apple.com/documentation/foundation/nstimezone/1387235-daylightsavingtimeoffset) 确定当前的夏令时偏移量。对大多数时区来说，该值为零或一。
- [nextDaylightSavingTimeTransition](https://developer.apple.com/documentation/foundation/nstimezone/1387183-nextdaylightsavingtimetransition) 确定下一次夏令时切换发生的时间。

此外，还有名称类似的方法，用于确定特定日期的这些信息。如果应用需要跟踪事件和约会，可以使用这些信息提醒用户即将发生的夏令时切换。

[下一页](Historical%20Dates.md) · [上一页](Performing%20Calendar%20Calculations.md)
