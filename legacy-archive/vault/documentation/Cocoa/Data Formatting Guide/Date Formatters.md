---
title: 数据格式化指南
apple_id: 10000029i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/Articles/dfDateFormatting10_4.html
archived_at: '2026-07-15T07:14:34.932947Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [数据格式化指南](Introduction%20to%20Data%20Formatting%20Programming%20Guide%20For%20Cocoa.md)


[下一页](Number%20Formatters.md)[上一页](Introduction%20to%20Data%20Formatting%20Programming%20Guide%20For%20Cocoa.md)

# 日期格式化器

使用日期格式化器创建日期的字符串表示形式、以及解析字符串以得到日期对象，主要有两个基本方法——分别是 [dateFromString:](https://developer.apple.com/documentation/foundation/dateformatter/1409994-date) 和 [stringFromDate:](https://developer.apple.com/documentation/foundation/nsdateformatter/1415810-stringfromdate)。如果你需要更精细地控制要解析的字符串范围，也可以使用 [getObjectValue:forString:range:error:](https://developer.apple.com/documentation/foundation/dateformatter/1409248-getobjectvalue)。

日期格式化器上有许多可以读取和设置的属性。向用户展示信息时，通常应直接使用 `NSDateFormatter` 的样式常量，来指定一组预定义的属性，从而决定格式化后的日期如何显示。但如果你需要以精确的格式生成日期的表示形式，就应该使用格式字符串。

如果你需要解析日期字符串，采取的方式同样取决于你的目标。如果要解析用户的输入，通常应使用样式常量以符合用户的预期。如果要解析从数据库或 Web 服务获取的日期，则应使用格式字符串。

在所有情况下，都应考虑到格式化器默认会使用用户的语言环境（[currentLocale](https://developer.apple.com/documentation/foundation/nslocale/1409990-currentlocale)），并叠加用户的个人偏好设置。如果你想使用用户的语言环境，但不想使用其个人设置，可以从当前用户的语言环境中获取语言环境 ID（[localeIdentifier](https://developer.apple.com/documentation/foundation/nslocale/1416263-localeidentifier)），并用它创建一个新的"标准"语言环境，然后将该标准语言环境设置为格式化器的 [locale](https://developer.apple.com/documentation/foundation/nsdateformatter/1411973-locale)。

`NSDateFormatter` 让你可以轻松地使用用户在系统偏好设置的"国际化"面板中配置的设置来格式化日期。`NSDateFormatter` 的样式常量——`NSDateFormatterNoStyle`、`NSDateFormatterShortStyle`、`NSDateFormatterMediumStyle`、`NSDateFormatterLongStyle` 和 `NSDateFormatterFullStyle`——指定了一组属性，用于按照用户的偏好设置决定日期的显示方式。

你可以分别使用 [setDateStyle:](https://developer.apple.com/documentation/foundation/nsdateformatter/1415411-datestyle) 和 [setTimeStyle:](https://developer.apple.com/documentation/foundation/nsdateformatter/1413467-timestyle) 独立指定日期格式化器中日期和时间部分的样式。[清单 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdgnrzfvjvomq) 演示了如何使用格式化器样式格式化日期。请注意其中使用 `NSDateFormatterNoStyle` 来抑制时间部分，从而只生成一个包含日期的字符串。

__清单 1__  使用格式化器样式格式化日期

```objc
NSDateFormatter *dateFormatter = [[NSDateFormatter alloc] init];
[dateFormatter setDateStyle:NSDateFormatterMediumStyle];
[dateFormatter setTimeStyle:NSDateFormatterNoStyle];

NSDate *date = [NSDate dateWithTimeIntervalSinceReferenceDate:162000];

NSString *formattedDateString = [dateFormatter stringFromDate:date];
NSLog(@"formattedDateString: %@", formattedDateString);
// 在 en_US 语言环境下的输出："formattedDateString: Jan 2, 2001"。
```


大体来说，有两种情况需要使用自定义格式：

1. 固定格式的字符串，例如 Internet 日期。
2. 用户可见的、且不匹配任何现有样式的元素

要为日期格式化器指定一个自定义的固定格式，可以使用 [setDateFormat:](https://developer.apple.com/documentation/foundation/dateformatter/1413514-dateformat)。格式字符串使用 Unicode 技术标准 #35 中的格式模式。该标准的版本会随操作系统版本而变化：

- OS X v10.9 和 iOS 7 使用 [tr35-31 版本](http://www.unicode.org/reports/tr35/tr35-31/tr35-dates.html#Date_Format_Patterns)。
- OS X v10.8 和 iOS 6 使用 [tr35-25 版本](http://www.unicode.org/reports/tr35/tr35-25.html#Date_Format_Patterns)。
- iOS 5 使用 [tr35-19 版本](http://www.unicode.org/reports/tr35/tr35-19.html#Date_Format_Patterns)。
- OS X v10.7 和 iOS 4.3 使用 [tr35-17 版本](http://www.unicode.org/reports/tr35/tr35-17.html#Date_Format_Patterns)。
- iOS 4.0、iOS 4.1 和 iOS 4.2 使用 [tr35-15 版本](http://www.unicode.org/reports/tr35/tr35-15.html#Date_Format_Patterns)。
- iOS 3.2 使用 [tr35-12 版本](http://www.unicode.org/reports/tr35/tr35-12.html#Date_Format_Patterns)。
- OS X v10.6、iOS 3.0 和 iOS 3.1 使用 [tr35-10 版本](http://unicode.org/reports/tr35/tr35-10.html#Date_Format_Patterns)。
- OS X v10.5 使用 [tr35-6 版本](http://unicode.org/reports/tr35/tr35-6.html#Date_Format_Patterns)。
- OS X v10.4 使用 [tr35-4 版本](http://unicode.org/reports/tr35/tr35-4.html#Date_Format_Patterns)。

尽管从原理上说格式字符串指定的是一种固定格式，但默认情况下 [NSDateFormatter](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateFormatter/Description.html#//apple_ref/occ/cl/NSDateFormatter) 仍然会考虑用户的偏好设置（包括语言环境设置）。使用格式字符串时，你必须注意以下几点：

- `NSDateFormatter` 会把你要解析的字符串中的数字，当作用户所选日历中的数字来处理。例如，如果用户选择了佛历，解析年份 `2010` 会得到一个在公历中对应 `1467` 年的 `NSDate` 对象。（关于不同历法系统及其用法的更多信息，请参阅 _[Date and Time Programming Guide](../Date%20and%20Time%20Programming%20Guide/About%20Dates%20and%20Times.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgazts2i)_。）
- 在 iOS 中，用户可以覆盖默认的上午/下午（AM/PM）与 24 小时制的设置。这可能导致 `NSDateFormatter` 重写你设置的格式字符串。

请注意，使用 Unicode 格式字符串格式时，应将格式字符串中的字面文本用单引号（`''`）括起来。

以下示例演示了如何使用格式字符串生成字符串：

```objc
NSDateFormatter *dateFormatter = [[NSDateFormatter alloc] init];
[dateFormatter setDateFormat:@"yyyy-MM-dd 'at' HH:mm"];

NSDate *date = [NSDate dateWithTimeIntervalSinceReferenceDate:162000];

NSString *formattedDateString = [dateFormatter stringFromDate:date];
NSLog(@"formattedDateString: %@", formattedDateString);
// 对于美式英语，输出可能是：
// formattedDateString: 2001-01-02 at 13:00
```

关于这个示例，有两点需要注意：

1. 它使用 `yyyy` 来指定年份部分。一个常见的错误是使用 `YYYY`。`yyyy` 指定的是日历年，而 `YYYY` 指定的是 ISO 年周历法中所使用的"周所在年份"。大多数情况下，`yyyy` 和 `YYYY` 得到的数字相同，但它们也可能不同。通常你应该使用日历年。
2. 时间的表示形式可能是 `13:00`。但在 iOS 中，如果用户已经把"24 小时制"关闭，时间可能会显示为 `1:00 pm`。

要显示只包含特定元素集合的日期，可以使用 [dateFormatFromTemplate:options:locale:](https://developer.apple.com/documentation/foundation/nsdateformatter/1408112-dateformatfromtemplate)]。该方法会根据你想要使用的日期分量生成一个格式字符串，并采用适合该用户的正确标点和顺序（即针对用户的语言环境和偏好进行了定制）。之后你就可以用这个格式字符串来创建格式化器。

例如，要创建一个使用当前语言环境显示今天的星期名、日期和月份的格式化器，可以这样写：

```objc
NSString *formatString = [NSDateFormatter dateFormatFromTemplate:@"EdMMM" options:0
                                          locale:[NSLocale currentLocale]];
NSDateFormatter *dateFormatter = [[NSDateFormatter alloc] init];
[dateFormatter setDateFormat:formatString];

NSString *todayString = [dateFormatter stringFromDate:[NSDate date]];
NSLog(@"todayString: %@", todayString);
```

要理解为什么需要这样做，可以考虑这样一种情况：你想显示星期名、日期和月份。你无法使用格式化器样式来创建这种日期表示形式（没有一种样式会省略年份）。但你也无法_轻松而一致地_使用格式字符串来正确创建这种表示形式。虽然乍看起来似乎很简单，但其中有一个复杂之处：来自美国的用户通常期望日期以"Mon, Jan 3"这样的形式呈现，而来自英国的用户则通常期望日期以"Mon 31 Jan"这样的形式呈现。

以下示例说明了这一点：

```objc
NSLocale *usLocale = [[NSLocale alloc] initWithLocaleIdentifier:@"en_US"];
NSString *usFormatString = [NSDateFormatter dateFormatFromTemplate:@"EdMMM" options:0 locale:usLocale];
NSLog(@"usFormatterString: %@", usFormatString);
// 输出：usFormatterString: EEE, MMM d。

NSLocale *gbLocale = [[NSLocale alloc] initWithLocaleIdentifier:@"en_GB"];
NSString *gbFormatString = [NSDateFormatter dateFormatFromTemplate:@"EdMMM" options:0 locale:gbLocale];
NSLog(@"gbFormatterString: %@", gbFormatString);
// 输出：gbFormatterString: EEE d MMM。
```


除了从 `NSFormatter` 继承来的方法（例如 [getObjectValue:forString:errorDescription:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSFormatter/Description.html#//apple_ref/occ/instm/NSFormatter/getObjectValue:forString:errorDescription:)）之外，`NSDateFormatter` 还添加了 `dateFromString:` 和 `getObjectValue:forString:range:error:`。这些方法让你可以更方便地在代码中直接使用 `NSDateFormatter` 对象，并以比 `NSString` 格式化更复杂、更便捷的方式将日期格式化为字符串。

[getObjectValue:forString:range:error:](https://developer.apple.com/documentation/foundation/dateformatter/1409248-getobjectvalue) 方法允许你指定要解析的字符串子范围，并返回实际被解析的字符串范围（如果解析失败，则指出失败发生的位置）。它还会返回一个 `NSError` 对象，其中可以包含比 `NSFormatter` 继承而来的 `getObjectValue:forString:errorDescription:` 方法所返回的失败字符串更丰富的信息。

如果你处理的是固定格式的日期，应先将日期格式化器的 _locale_ 设置为适合该固定格式的值。大多数情况下，最合适的语言环境是 `en_US_POSIX`——这是一个专门设计用来在不受用户和系统偏好设置影响的情况下、生成美式英语结果的语言环境。`en_US_POSIX` 在时间上也是不变的（如果未来某个时候美国改变了日期格式方式，`en_US` 会随之改变以反映新的行为，但 `en_US_POSIX` 不会），并且在不同平台之间也是一致的（`en_US_POSIX` 在 iPhone OS 上的行为与在 OS X 上以及其他平台上完全相同）。

一旦你将日期格式化器的语言环境设置为 `en_US_POSIX`，就可以接着设置日期格式字符串，此后该日期格式化器对所有用户都会表现出一致的行为。

[清单 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdgnrzfvjvoni) 展示了如何将 `NSDateFormatter` 用于上述两种角色。首先，它创建一个 `en_US_POSIX` 日期格式化器，使用固定的日期格式字符串和 UTC 时区来解析传入的 RFC 3339 日期字符串。接着，它创建一个标准的日期格式化器，将日期渲染为要展示给用户的字符串。

__清单 2__  解析 RFC 3339 日期时间

```objc
- (NSString *)userVisibleDateTimeStringForRFC3339DateTimeString:(NSString *)rfc3339DateTimeString {
    /*
      返回与指定的 RFC 3339 日期时间字符串对应的、用户可见的日期时间字符串。
      请注意，这并不能处理所有可能的 RFC 3339 日期时间字符串，只处理其中最常见的一种样式。
     */

    NSDateFormatter *rfc3339DateFormatter = [[NSDateFormatter alloc] init];
    NSLocale *enUSPOSIXLocale = [[NSLocale alloc] initWithLocaleIdentifier:@"en_US_POSIX"];

    [rfc3339DateFormatter setLocale:enUSPOSIXLocale];
    [rfc3339DateFormatter setDateFormat:@"yyyy'-'MM'-'dd'T'HH':'mm':'ss'Z'"];
    [rfc3339DateFormatter setTimeZone:[NSTimeZone timeZoneForSecondsFromGMT:0]];

    // 将 RFC 3339 日期时间字符串转换为 NSDate。
    NSDate *date = [rfc3339DateFormatter dateFromString:rfc3339DateTimeString];

    NSString *userVisibleDateTimeString;
    if (date != nil) {
        // 将日期对象转换为用户可见的日期字符串。
        NSDateFormatter *userVisibleDateFormatter = [[NSDateFormatter alloc] init];
        assert(userVisibleDateFormatter != nil);

        [userVisibleDateFormatter setDateStyle:NSDateFormatterShortStyle];
        [userVisibleDateFormatter setTimeStyle:NSDateFormatterShortStyle];

        userVisibleDateTimeString = [userVisibleDateFormatter stringFromDate:date];
    }
    return userVisibleDateTimeString;
}
```


创建一个日期格式化器并非一个廉价的操作。如果你可能会频繁使用某个格式化器，通常缓存单个实例要比反复创建和销毁多个实例更高效。一种做法是使用 `static` 变量。

[清单 3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdgnrzfvjvonq) 重新实现了[清单 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdgnrzfvjvoni) 中的方法，改为保留日期格式化器以供后续复用。

__清单 3__  使用缓存的格式化器解析 RFC 3339 日期时间

```objc
static NSDateFormatter *sUserVisibleDateFormatter = nil;

- (NSString *)userVisibleDateTimeStringForRFC3339DateTimeString:(NSString *)rfc3339DateTimeString {
    /*
      返回与指定的 RFC 3339 日期时间字符串对应的、用户可见的日期时间字符串。
      请注意，这并不能处理所有可能的 RFC 3339 日期时间字符串，只处理其中最常见的一种样式。
     */

    // 如果日期格式化器尚未设置好，就创建它们并缓存以供复用。
    static NSDateFormatter *sRFC3339DateFormatter = nil;
    if (sRFC3339DateFormatter == nil) {
        sRFC3339DateFormatter = [[NSDateFormatter alloc] init];
        NSLocale *enUSPOSIXLocale = [[NSLocale alloc] initWithLocaleIdentifier:@"en_US_POSIX"];

        [sRFC3339DateFormatter setLocale:enUSPOSIXLocale];
        [sRFC3339DateFormatter setDateFormat:@"yyyy'-'MM'-'dd'T'HH':'mm':'ss'Z'"];
        [sRFC3339DateFormatter setTimeZone:[NSTimeZone timeZoneForSecondsFromGMT:0]];
    }

    // 将 RFC 3339 日期时间字符串转换为 NSDate。
    NSDate *date = [rfc3339DateFormatter dateFromString:rfc3339DateTimeString];

    NSString *userVisibleDateTimeString;
    if (date != nil) {
        if (sUserVisibleDateFormatter == nil) {
            sUserVisibleDateFormatter = [[NSDateFormatter alloc] init];
            [sUserVisibleDateFormatter setDateStyle:NSDateFormatterShortStyle];
            [sUserVisibleDateFormatter setTimeStyle:NSDateFormatterShortStyle];
        }
        // 将日期对象转换为用户可见的日期字符串。
        userVisibleDateTimeString = [sUserVisibleDateFormatter stringFromDate:date];
    }
    return userVisibleDateTimeString;
}
```

如果你缓存了日期格式化器（或任何其他依赖于用户当前语言环境的对象），应订阅 [NSCurrentLocaleDidChangeNotification](https://developer.apple.com/documentation/foundation/nslocale/1418141-currentlocaledidchangenotificati) 通知，并在当前语言环境发生变化时更新你缓存的对象。[清单 3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdgnrzfvjvonq) 中的代码将 `sUserVisibleDateFormatter` 定义在方法之外，这样其他（此处未展示的）代码就可以在需要时更新它。相比之下，`sRFC3339DateFormatter` 是定义在方法内部的，因为按设计它并不依赖于用户的语言环境设置。

对于始终保证使用同一种日历的固定、非本地化格式的日期和时间，有时使用标准 C 库函数 `strptime_l` 和 `strftime_l` 会更简单、更高效。

请注意，C 库同样有"当前语言环境"这个概念。为了保证固定的日期格式，你应该将这些例程的 `loc` 参数传入 `NULL`。这会使它们使用 POSIX 语言环境（也称为 C 语言环境），它等效于 Cocoa 的 `en_US_POSIX` 语言环境，如下例所示。

```objc
struct tm  sometime;
const char *formatString = "%Y-%m-%d %H:%M:%S %z";
(void) strptime_l("2005-07-01 12:00:00 -0700", formatString, &sometime, NULL);
NSLog(@"NSDate is %@", [NSDate dateWithTimeIntervalSince1970: mktime(&sometime)]);
// 输出：NSDate is 2005-07-01 12:00:00 -0700
```

[下一页](Number%20Formatters.md)[上一页](Introduction%20to%20Data%20Formatting%20Programming%20Guide%20For%20Cocoa.md)
