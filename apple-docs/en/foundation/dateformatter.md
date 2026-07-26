---
title: DateFormatter
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/dateformatter
source_url: 'https://developer.apple.com/documentation/foundation/dateformatter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dateformatter.json'
content_hash: 'sha256:dec66c99a0ee1633'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# DateFormatter

<sub>Class</sub>

A formatter that converts between dates and their textual representations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class DateFormatter
```

## Overview

Instances of [DateFormatter](dateformatter.md) create string representations of [NSDate](nsdate.md) objects, and convert textual representations of dates and times into [NSDate](nsdate.md) objects. For user-visible representations of dates and times, [DateFormatter](dateformatter.md) provides a variety of localized presets and configuration options. For fixed format representations of dates and times, you can specify a custom format string.

When working with date representations in ISO 8601 format, use [ISO8601DateFormatter](iso8601dateformatter.md) instead.

To represent an interval between two [NSDate](nsdate.md) objects, use [DateIntervalFormatter](dateintervalformatter.md) instead.

To represent a quantity of time specified by an [NSDateComponents](nsdatecomponents.md) object, use [DateComponentsFormatter](datecomponentsformatter.md) instead.

> [!tip] Tip
> In Swift, you can use [FormatStyle](date/formatstyle.md) or [VerbatimFormatStyle](date/verbatimformatstyle.md) rather than [DateFormatter](dateformatter.md). The [FormatStyle](formatstyle.md) API offers a declarative idiom for customizing the formatting of various types. Also, Foundation caches identical [FormatStyle](formatstyle.md) instances, so you don’t need to pass them around your app, or risk wasting memory with duplicate formatters.

### Working With User-Visible Representations of Dates and Times

When displaying a date to a user, you set the [dateStyle](dateformatter/datestyle.md) and [timeStyle](dateformatter/timestyle.md) properties of the date formatter according to your particular needs. For example, if you want to show the month, day, and year without showing the time, you would set the [dateStyle](dateformatter/datestyle.md) property to [NSDateFormatterLongStyle](dateformatter/style/long.md) and the [timeStyle](dateformatter/timestyle.md) property to [NSDateFormatterNoStyle](dateformatter/style/none.md). Conversely, if you want to show only the time, you would set the `dateStyle` property to [NSDateFormatterNoStyle](dateformatter/style/none.md) and the [timeStyle](dateformatter/timestyle.md) property to [NSDateFormatterShortStyle](dateformatter/style/short.md). Based on the values of the [dateStyle](dateformatter/datestyle.md) and [timeStyle](dateformatter/timestyle.md) properties, [DateFormatter](dateformatter.md) provides a representation of a specified date that is appropriate for a given locale.

**Swift**

```swift
let dateFormatter = DateFormatter()
dateFormatter.dateStyle = .medium
dateFormatter.timeStyle = .none
 
let date = Date(timeIntervalSinceReferenceDate: 118800)
 
// US English Locale (en_US)
dateFormatter.locale = Locale(identifier: "en_US")
print(dateFormatter.string(from: date)) // Jan 2, 2001
 
// French Locale (fr_FR)
dateFormatter.locale = Locale(identifier: "fr_FR")
print(dateFormatter.string(from: date)) // 2 janv. 2001
 
// Japanese Locale (ja_JP)
dateFormatter.locale = Locale(identifier: "ja_JP")
print(dateFormatter.string(from: date)) // 2001/01/02
```

**Objective-C**

```objc
NSDateFormatter *dateFormatter = [[NSDateFormatter alloc] init];
dateFormatter.dateStyle = NSDateFormatterMediumStyle;
dateFormatter.timeStyle = NSDateFormatterNoStyle;
 
NSDate *date = [NSDate dateWithTimeIntervalSinceReferenceDate:118800];
 
// US English Locale (en_US)
dateFormatter.locale = [[NSLocale alloc] initWithLocaleIdentifier:@"en_US"];
NSLog(@"%@", [dateFormatter stringFromDate:date]); // Jan 2, 2001
 
// French Locale (fr_FR)
dateFormatter.locale = [[NSLocale alloc] initWithLocaleIdentifier:@"fr_FR"];
NSLog(@"%@", [dateFormatter stringFromDate:date]); // 2 janv. 2001
 
// Japanese Locale (ja_JP)
dateFormatter.locale = [[NSLocale alloc] initWithLocaleIdentifier:@"ja_JP"];
NSLog(@"%@", [dateFormatter stringFromDate:date]); // 2001/01/02
```

If you need to define a format that cannot be achieved using the predefined styles, you can use the [- setLocalizedDateFormatFromTemplate:](<dateformatter/setlocalizeddateformatfromtemplate(__).md>) to specify a localized date format from a template.

**Swift**

```swift
let dateFormatter = DateFormatter()
let date = Date(timeIntervalSinceReferenceDate: 410220000)
 
// US English Locale (en_US)
dateFormatter.locale = Locale(identifier: "en_US")
dateFormatter.setLocalizedDateFormatFromTemplate("MMMMd") // set template after setting locale
print(dateFormatter.string(from: date)) // December 31
 
// British English Locale (en_GB)
dateFormatter.locale = Locale(identifier: "en_GB")
dateFormatter.setLocalizedDateFormatFromTemplate("MMMMd") // // set template after setting locale
print(dateFormatter.string(from: date)) // 31 December
```

**Objective-C**

```objc
NSDateFormatter *dateFormatter = [[NSDateFormatter alloc] init];
NSDate *date = [NSDate dateWithTimeIntervalSinceReferenceDate:410220000];
 
// US English Locale (en_US)
dateFormatter.locale = [[NSLocale alloc] initWithLocaleIdentifier:@"en_US"];
[dateFormatter setLocalizedDateFormatFromTemplate:@"MMMMd"]; // set template after setting locale
NSLog(@"%@", [dateFormatter stringFromDate:date]); // December 31
 
// British English Locale (en_GB)
dateFormatter.locale = [[NSLocale alloc] initWithLocaleIdentifier:@"en_GB"];
[dateFormatter setLocalizedDateFormatFromTemplate:@"MMMMd"]; // set template after setting locale
NSLog(@"%@", [dateFormatter stringFromDate:date]); // 31 December
```

### Working With Fixed Format Date Representations

> [!important] Important
> In macOS 10.12 and later or iOS 10 and later, use the [ISO8601DateFormatter](iso8601dateformatter.md) class when working with ISO 8601 date representations.

When working with fixed format dates, such as RFC 3339, you set the [dateFormat](dateformatter/dateformat.md) property to specify a format string. For most fixed formats, you should also set the [locale](dateformatter/locale.md) property to a POSIX locale (`"en_US_POSIX"`), and set the [timeZone](dateformatter/timezone.md) property to UTC.

**Swift**

```swift
let RFC3339DateFormatter = DateFormatter()
RFC3339DateFormatter.locale = Locale(identifier: "en_US_POSIX")
RFC3339DateFormatter.dateFormat = "yyyy-MM-dd'T'HH:mm:ssZZZZZ"
RFC3339DateFormatter.timeZone = TimeZone(secondsFromGMT: 0)
 
/* 39 minutes and 57 seconds after the 16th hour of December 19th, 1996 with an offset of -08:00 from UTC (Pacific Standard Time) */
let string = "1996-12-19T16:39:57-08:00"
let date = RFC3339DateFormatter.date(from: string)
```

**Objective-C**

```objc
RFC3339DateFormatter = [[NSDateFormatter alloc] init];
RFC3339DateFormatter.locale = [NSLocale localeWithLocaleIdentifier:@"en_US_POSIX"];
RFC3339DateFormatter.dateFormat = @"yyyy-MM-dd'T'HH:mm:ssZZZZZ";
RFC3339DateFormatter.timeZone = [NSTimeZone timeZoneForSecondsFromGMT:0];
 
/* 39 minutes and 57 seconds after the 16th hour of December 19th, 1996 with an offset of -08:00 from UTC (Pacific Standard Time) */
NSString *string = @"1996-12-19T16:39:57-08:00";
NSDate *date = [RFC3339DateFormatter dateFromString:string];
```

For more information, see [Technical Q&A QA1480 “NSDateFormatter and Internet Dates”](https://developer.apple.com/library/mac/qa/qa1480/).

### Thread Safety

On iOS 7 and later `NSDateFormatter` is thread safe.

In macOS 10.9 and later `NSDateFormatter` is thread safe so long as you are using the modern behavior in a 64-bit app.

On earlier versions of the operating system, or when using the legacy formatter behavior or running in 32-bit in macOS, `NSDateFormatter` is not thread safe, and you therefore must not mutate a date formatter simultaneously from multiple threads.

## Relationships

- **Inherits From**: [Formatter](formatter.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Converting Objects

- [- dateFromString:](<dateformatter/date(from_).md>) — Returns a date representation of a specified string that the system interprets using the receiver’s current settings.
- [- stringFromDate:](<dateformatter/string(from_).md>) — Returns a string representation of a specified date that the system formats using the receiver’s current settings.
- [+ localizedStringFromDate:dateStyle:timeStyle:](<dateformatter/localizedstring(from_datestyle_timestyle_).md>) — Returns a string representation of a specified date, that the system formats for the current locale using the specified date and time styles.
- [- getObjectValue:forString:range:error:](<dateformatter/getobjectvalue(__for_range_).md>) — Returns by reference a date representation of a specified string and its date range, as well as a Boolean value that indicates whether the system can parse the string.

### Managing Formats and Styles

- [dateStyle](dateformatter/datestyle.md) — The date style of the receiver.
- [timeStyle](dateformatter/timestyle.md) — The time style of the receiver.
- [dateFormat](dateformatter/dateformat.md) — The date format string used by the receiver.
- [- setLocalizedDateFormatFromTemplate:](<dateformatter/setlocalizeddateformatfromtemplate(__).md>) — Sets the date format from a template using the specified locale for the receiver.
- [+ dateFormatFromTemplate:options:locale:](<dateformatter/dateformat(fromtemplate_options_locale_).md>) — Returns a localized date format string representing the given date format components arranged appropriately for the specified locale.
- [formattingContext](dateformatter/formattingcontext.md) — The capitalization formatting context used when formatting a date.

### Managing Attributes

- [calendar](dateformatter/calendar.md) — The calendar for the receiver.
- [defaultDate](dateformatter/defaultdate.md) — The default date for the receiver.
- [locale](dateformatter/locale.md) — The locale for the receiver.
- [timeZone](dateformatter/timezone.md) — The time zone for the receiver.
- [twoDigitStartDate](dateformatter/twodigitstartdate.md) — The earliest date that can be denoted by a two-digit year specifier.
- [gregorianStartDate](dateformatter/gregorianstartdate.md) — The start date of the Gregorian calendar for the receiver.

### Managing Behavior Version

- [formatterBehavior](dateformatter/formatterbehavior.md) — The formatter behavior for the receiver.
- [defaultFormatterBehavior](dateformatter/defaultformatterbehavior.md) — Returns the default formatting behavior for instances of the class.

### Managing Natural Language Support

- [lenient](dateformatter/islenient.md) — A Boolean value that indicates whether the receiver uses heuristics when parsing a string.
- [doesRelativeDateFormatting](dateformatter/doesrelativedateformatting.md) — A Boolean value that indicates whether the receiver uses phrases such as “today” and “tomorrow” for the date component.

### Managing AM and PM Symbols

- [AMSymbol](dateformatter/amsymbol.md) — The AM symbol for the receiver.
- [PMSymbol](dateformatter/pmsymbol.md) — The PM symbol for the receiver.

### Managing Weekday Symbols

- [weekdaySymbols](dateformatter/weekdaysymbols.md) — The array of weekday symbols for the receiver.
- [shortWeekdaySymbols](dateformatter/shortweekdaysymbols.md) — The array of short weekday symbols for the receiver.
- [veryShortWeekdaySymbols](dateformatter/veryshortweekdaysymbols.md) — The array of very short weekday symbols for the receiver.
- [standaloneWeekdaySymbols](dateformatter/standaloneweekdaysymbols.md) — The array of standalone weekday symbols for the receiver.
- [shortStandaloneWeekdaySymbols](dateformatter/shortstandaloneweekdaysymbols.md) — The array of short standalone weekday symbols for the receiver.
- [veryShortStandaloneWeekdaySymbols](dateformatter/veryshortstandaloneweekdaysymbols.md) — The array of very short standalone weekday symbols for the receiver.

### Managing Month Symbols

- [monthSymbols](dateformatter/monthsymbols.md) — The month symbols for the receiver.
- [shortMonthSymbols](dateformatter/shortmonthsymbols.md) — The array of short month symbols for the receiver.
- [veryShortMonthSymbols](dateformatter/veryshortmonthsymbols.md) — The very short month symbols for the receiver.
- [standaloneMonthSymbols](dateformatter/standalonemonthsymbols.md) — The standalone month symbols for the receiver.
- [shortStandaloneMonthSymbols](dateformatter/shortstandalonemonthsymbols.md) — The short standalone month symbols for the receiver.
- [veryShortStandaloneMonthSymbols](dateformatter/veryshortstandalonemonthsymbols.md) — The very short month symbols for the receiver.

### Managing Quarter Symbols

- [quarterSymbols](dateformatter/quartersymbols.md) — The quarter symbols for the receiver.
- [shortQuarterSymbols](dateformatter/shortquartersymbols.md) — The short quarter symbols for the receiver.
- [standaloneQuarterSymbols](dateformatter/standalonequartersymbols.md) — The standalone quarter symbols for the receiver.
- [shortStandaloneQuarterSymbols](dateformatter/shortstandalonequartersymbols.md) — The short standalone quarter symbols for the receiver.

### Managing Era Symbols

- [eraSymbols](dateformatter/erasymbols.md) — The era symbols for the receiver.
- [longEraSymbols](dateformatter/longerasymbols.md) — The long era symbols for the receiver

### Deprecated

- [generatesCalendarDates](dateformatter/generatescalendardates.md) — Indicates whether the formatter generates the deprecated calendar date type.

### Constants

- [Style](dateformatter/style.md) — The following constants specify predefined format styles for dates and times.
- [Behavior](dateformatter/behavior.md) — Constants that specify the behavior `NSDateFormatter` should exhibit.

## See Also

### Dates and times

- [DateComponentsFormatter](datecomponentsformatter.md) — A formatter that creates string representations of quantities of time.
- [RelativeDateTimeFormatter](relativedatetimeformatter.md) — A formatter that creates locale-aware string representations of a relative date or time.
- [DateIntervalFormatter](dateintervalformatter.md) — A formatter that creates string representations of time intervals.
- [ISO8601DateFormatter](iso8601dateformatter.md) — A formatter that converts between dates and their ISO 8601 string representations.
