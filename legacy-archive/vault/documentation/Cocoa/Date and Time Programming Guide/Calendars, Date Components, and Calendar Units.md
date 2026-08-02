---
title: 日期与时间编程指南
apple_id: 10000039i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/Articles/dtCalendars.html
archived_at: '2026-07-15T07:14:36.449447Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [日期与时间编程指南](About%20Dates%20and%20Times.md)


[下一页](Performing%20Calendar%20Calculations.md) · [上一页](Dates.md)

# 日历、日期组件与日历单位

日历对象封装了计时体系的信息，这类体系定义了一年的起点、长度和划分方式。你可以使用日历对象，在绝对时间与年、日或分钟等日期组件之间进行转换。

[NSCalendar](https://developer.apple.com/documentation/foundation/nscalendar) 实现了多种日历。它提供多种不同日历的数据，包括佛历、公历、希伯来历、伊斯兰历和日本历（支持哪些日历取决于操作系统版本；请查看 [NSLocale](https://developer.apple.com/documentation/foundation/nslocale) 类，以确定特定版本支持哪些日历）。`NSCalendar` 与 [NSDateComponents](https://developer.apple.com/documentation/foundation/nsdatecomponents) 类紧密相关，后者的实例描述了日历计算所需的日期组成元素。

日历由 `NSLocale` 中的常量指定。获取用户首选地区所用日历的最简便方式，是使用 `NSCalendar` 的 [currentCalendar](https://developer.apple.com/documentation/foundation/nscalendar/1408501-current) 方法；也可以使用 `NSLocaleCalendar` 键，从任意 `NSLocale` 对象获取默认日历。还可以通过指定所需日历的标识符，[创建](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39)任意日历对象。清单 3 展示了如何为日本历和当前用户创建日历对象。

__清单 3__　创建日历对象

```objc
NSCalendar *currentCalendar = [NSCalendar currentCalendar];

NSCalendar *japaneseCalendar = [[NSCalendar alloc]
                                initWithCalendarIdentifier:NSJapaneseCalendar];

NSCalendar *usersCalendar =
                      [[NSLocale currentLocale] objectForKey:NSLocaleCalendar];
```

这里，`usersCalendar` 与 `currentCalendar` 相等，但它们是不同的对象。

你可以使用 [NSDateComponents](https://developer.apple.com/documentation/foundation/nsdatecomponents) 对象表示日期的组成元素，例如年、日和小时。`NSDateComponents` 对象既可以保存绝对值，也可以保存单位数量（有关使用 `NSDateComponents` 指定单位数量的示例，请参阅[为日期添加组件](Performing%20Calendar%20Calculations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqmzwfvjvomy)）。要正确理解日期组件对象的含义，需要知道与之关联的日历及其用途。

日、周、星期、月和年的编号通常从 1 开始，但特定日历可能存在例外。序数出现时，也从 1 开始。某些日历可能需要将其基本单位概念映射到年/月/周/日/……这套命名中。单位的具体值由各日历定义，不一定与其他日历中同一单位的值一致。

清单 4 展示了如何创建日期组件对象。你可以使用该对象创建年单位为 2004、月单位为 5、日单位为 6 的日期（在公历中即 2004 年 5 月 6 日）。也可以用它为现有日期添加 2004 个年单位、5 个月单位和 6 个日单位。由于没有另行指定，`weekday` 的值未定义。

__清单 4__　创建日期组件对象

```objc
NSDateComponents *components = [[NSDateComponents alloc] init];
[components setDay:6];
[components setMonth:5];
[components setYear:2004];

NSInteger weekday = [components weekday]; // 未定义（== NSUndefinedDateComponent）
```


要将日期拆分为各个组成部分，请使用 `NSCalendar` 的 [components:fromDate:](https://developer.apple.com/documentation/foundation/nscalendar/1414841-components) 方法。除了日期本身之外，还需要指定 `NSDateComponents` 对象应返回哪些组件。为此，该方法接收一个由[日历单位](https://developer.apple.com/documentation/foundation/nscalendarunit)常量组成的位掩码。只需指定你感兴趣的组件，无需指定多余组件。清单 5 展示了如何计算今天是几号及星期几。

__清单 5__　获取日期的组件

```objc
NSDate *today = [NSDate date];
NSCalendar *gregorian = [[NSCalendar alloc]
                         initWithCalendarIdentifier:NSGregorianCalendar];
NSDateComponents *weekdayComponents =
                    [gregorian components:(NSDayCalendarUnit | NSWeekdayCalendarUnit) fromDate:today];
NSInteger day = [weekdayComponents day];
NSInteger weekday = [weekdayComponents weekday];
```

这样会得到日期的绝对组件。例如，如果请求 2010 年 11 月 7 日的年组件和日组件，年得到 2010，日得到 7。如果想知道这是一年中的第几天，则可以使用 `NSCalendar` 类的 [ordinalityOfUnit:inUnit:forDate:](https://developer.apple.com/documentation/foundation/nscalendar/1408595-ordinalityofunit) 方法。

也可以根据组件创建日期。你可以配置 `NSDateComponents` 实例来指定日期的各个组件，然后使用 `NSCalendar` 的 [dateFromComponents:](https://developer.apple.com/documentation/foundation/nscalendar/1407609-datefromcomponents) 方法创建相应的日期对象。可以根据需要或意愿提供任意数量的组件。若现有信息不足以计算绝对时间，日历通常会选用 `0`、`1` 等默认值，但具体选择因日历而异。如果提供的信息相互矛盾，日历会按自身规则消除歧义（这可能包括忽略一个或多个参数）。

清单 6 展示了如何创建一个日期对象，表示公历 2008 年 5 月的第一个星期一。

__清单 6__　根据组件创建日期

```objc
NSDateComponents *components = [[NSDateComponents alloc] init];
[components setWeekday:2]; // 星期一
[components setWeekdayOrdinal:1]; // 当月第一个星期一
[components setMonth:5]; // 五月
[components setYear:2008];
NSCalendar *gregorian = [[NSCalendar alloc]
                         initWithCalendarIdentifier:NSGregorianCalendar];
NSDate *date = [gregorian dateFromComponents:components];
```

要保证行为正确，必须确保所用组件对于该日历有意义。指定“超出范围”的组件会产生未定义行为，例如公历中的日值 `-6` 或 2 月 30 日。

你可能希望创建一个不包含年份等组件的日期对象，例如用于存储朋友的生日。虽然严格来说无法创建无年份日期，但可以使用日期组件创建一个未指定年份的日期对象，如清单 7 所示。

__清单 7__　创建无年份日期

```objc
NSDateComponents *components = [[NSDateComponents alloc] init];
[components setMonth:11];
[components setDay:7];
NSCalendar *gregorian = [[NSCalendar alloc]
                         initWithCalendarIdentifier:NSGregorianCalendar];
NSDate *birthday = [gregorian dateFromComponents:components];
```

请注意，此例中的 `birthday` 具有年份默认值，在这里是公元 1 年（但并不保证默认值始终是公元 1 年）。如果以后将该日期重新转换为组件，或使用 [NSDateFormatter](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateFormatter/Description.html#//apple_ref/occ/cl/NSDateFormatter) 对象显示它，请务必不要使用年份值（你的朋友可能不喜欢被标成如此高龄）。可以使用 `NSDateFormatter` 的 [dateFormatFromTemplate:options:locale:](https://developer.apple.com/documentation/foundation/nsdateformatter/1408112-dateformatfromtemplate) 方法创建无年份日期格式化器，使其适应用户的地区。有关日期格式化的更多信息，请参阅《[数据格式化指南](../Data%20Formatting%20Guide/Introduction%20to%20Data%20Formatting%20Programming%20Guide%20For%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgazds2i)》。

要将日期组件从一种日历转换到另一种日历——例如从公历转换到希伯来历——首先使用第一种日历根据组件创建日期对象，然后使用第二种日历将该日期拆分为组件。清单 8 展示了如何在不同日历之间转换日期组件。

__清单 8__　将日期组件从一种日历转换到另一种日历

```objc
NSDateComponents *comps = [[NSDateComponents alloc] init];
[comps setDay:6];
[comps setMonth:5];
[comps setYear:2004];

NSCalendar *gregorian = [[NSCalendar alloc]
                         initWithCalendarIdentifier:NSGregorianCalendar];
NSDate *date = [gregorian dateFromComponents:comps];
[comps release];
[gregorian release];

NSCalendar *hebrew = [[NSCalendar alloc]
                        initWithCalendarIdentifier:NSHebrewCalendar];
NSUInteger unitFlags = NSDayCalendarUnit | NSMonthCalendarUnit |
                              NSYearCalendarUnit;
NSDateComponents *components = [hebrew components:unitFlags fromDate:date];

NSInteger day = [components day]; // 15
NSInteger month = [components month]; // 9
NSInteger year = [components year]; // 5764
```

[下一页](Performing%20Calendar%20Calculations.md) · [上一页](Dates.md)
