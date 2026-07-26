---
title: DateIntervalFormatter
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/dateintervalformatter
source_url: 'https://developer.apple.com/documentation/foundation/dateintervalformatter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dateintervalformatter.json'
content_hash: 'sha256:cbaa491b1608b198'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# DateIntervalFormatter

<sub>Class</sub>

A formatter that creates string representations of time intervals.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class DateIntervalFormatter
```

## Overview

A [DateIntervalFormatter](dateintervalformatter.md) object creates user-readable strings from pairs of dates. Use a date interval formatter to create user-readable strings of the form _\<start\>_ `-` _\<end\>_ for your app’s interface, where _\<start\>_ and _\<end\>_ are date values that you supply. The formatter uses locale and language information, along with custom formatting options, to define the content of the resulting string. You can specify different styles for the date and time information in each date value.

To use this class, create an instance, configure its properties, and call the [- stringFromDate:toDate:](<dateintervalformatter/string(from_to_).md>) method to generate a string. The properties of this class let you configure the calendar and specify the style to apply to date and time values. Given a current date of January 16, 2015, Configuring the Formatter Options shows how to configure a formatter object and generate the string “1/16/15 - 1/17/15”.

Configuring a formatter object

**Swift**

```swift
let formatter = DateIntervalFormatter()
formatter.dateStyle = .short
formatter.timeStyle = .none

// Create two dates that are exactly 1 day apart.
let startDate = Date()
let endDate = Date(timeInterval: 86400, since: startDate)

// Use the configured formatter to generate the string.
let outputString = formatter.string(from: startDate, to: endDate)
```

**Objective-C**

```objc
NSDateIntervalFormatter* formatter = [[NSDateIntervalFormatter alloc] init];
formatter.dateStyle = NSDateIntervalFormatterShortStyle;
formatter.timeStyle = NSDateIntervalFormatterNoStyle;
 
// Create two dates that are exactly 1 day apart.
NSDate* startDate = [NSDate date];
NSDate* endDate = [NSDate dateWithTimeInterval:86400 sinceDate:startDate];
 
// Use the configured formatter to generate the string.
NSString* outputString = [formatter stringFromDate:startDate toDate:endDate];
```

> [!note] Note
> Always set to the [dateStyle](dateintervalformatter/datestyle.md) and [timeStyle](dateintervalformatter/timestyle.md) properties to appropriate values before generating any strings.

The [- stringFromDate:toDate:](<dateintervalformatter/string(from_to_).md>) method may be called safely from any thread of your app. It is also safe to share a single instance of this class from multiple threads, with the caveat that you should not change the configuration of the object while another thread is using it to generate a string.

> [!tip] Tip
> In Swift, you can use [IntervalFormatStyle](date/intervalformatstyle.md) rather than [DateIntervalFormatter](dateintervalformatter.md). The [FormatStyle](formatstyle.md) API offers a declarative idiom for customizing the formatting of various types. Also, Foundation caches identical [FormatStyle](formatstyle.md) instances, so you don’t need to pass them around your app, or risk wasting memory with duplicate formatters.

## Relationships

- **Inherits From**: [Formatter](formatter.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Formatting a String

- [- stringFromDate:toDate:](<dateintervalformatter/string(from_to_).md>) — Returns a formatted string based on the specified start and end dates.

### Configuring the Formatter Options

- [dateStyle](dateintervalformatter/datestyle.md) — The style to use when formatting day, month, and year information.
- [timeStyle](dateintervalformatter/timestyle.md) — The style to use when formatting hour, minute, and second information.
- [dateTemplate](dateintervalformatter/datetemplate.md) — The template for formatting one date and time value.
- [calendar](dateintervalformatter/calendar.md) — The calendar to use for date values.
- [locale](dateintervalformatter/locale.md) — The locale to use when formatting date and time values.
- [timeZone](dateintervalformatter/timezone.md) — The time zone with which to specify time values.

### Constants

- [Style](dateintervalformatter/style.md) — Formatting styles for individual date and time values.

### Instance Methods

- [- stringFromDateInterval:](<dateintervalformatter/string(from_).md>) — Returns a formatted string for the given date interval.

## See Also

### Dates and times

- [DateFormatter](dateformatter.md) — A formatter that converts between dates and their textual representations.
- [DateComponentsFormatter](datecomponentsformatter.md) — A formatter that creates string representations of quantities of time.
- [RelativeDateTimeFormatter](relativedatetimeformatter.md) — A formatter that creates locale-aware string representations of a relative date or time.
- [ISO8601DateFormatter](iso8601dateformatter.md) — A formatter that converts between dates and their ISO 8601 string representations.
