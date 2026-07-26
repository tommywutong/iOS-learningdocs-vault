---
title: DateComponentsFormatter
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/datecomponentsformatter
source_url: 'https://developer.apple.com/documentation/foundation/datecomponentsformatter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponentsformatter.json'
content_hash: 'sha256:f277eef6c64135ee'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# DateComponentsFormatter

<sub>Class</sub>

A formatter that creates string representations of quantities of time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class DateComponentsFormatter
```

## Overview

An [DateComponentsFormatter](datecomponentsformatter.md) object takes quantities of time and formats them as a user-readable string. Use a date components formatter to create strings for your app’s interface. The formatter object has many options for creating both abbreviated and expanded strings. The formatter takes the current user’s locale and language into account when generating strings.

To use this class, create an instance, configure its properties, and call one of its methods to generate an appropriate string. The properties of this class let you configure the calendar and specify the date and time units you want displayed in the resulting string. The listing below shows how to configure a formatter to create the string “About 5 minutes remaining”.

**Swift**

```swift
let formatter = DateComponentsFormatter()
formatter.unitsStyle = .full
formatter.includesApproximationPhrase = true
formatter.includesTimeRemainingPhrase = true
formatter.allowedUnits = [.minute]
 
// Use the configured formatter to generate the string.
let outputString = formatter.string(from: 300.0)
```

**Objective-C**

```objc
NSDateComponentsFormatter *formatter = [[NSDateComponentsFormatter alloc] init];
formatter.unitsStyle = NSDateComponentsFormatterUnitsStyleFull;
formatter.includesApproximationPhrase = YES;
formatter.includesTimeRemainingPhrase = YES;
formatter.allowedUnits = NSCalendarUnitMinute;
 
// Use the configured formatter to generate the string.
NSString* outputString = [formatter stringFromTimeInterval:300.0];
```

The methods of this class may be called safely from any thread of your app. It is also safe to share a single instance of this class from multiple threads, with the caveat that you should not change the configuration of the object while another thread is using it to generate a string.

> [!tip] Tip
> In Swift, you can use [RelativeFormatStyle](date/relativeformatstyle.md) rather than [DateComponentsFormatter](datecomponentsformatter.md). The [FormatStyle](formatstyle.md) API offers a declarative idiom for customizing the formatting of various types. Also, Foundation caches identical [FormatStyle](formatstyle.md) instances, so you don’t need to pass them around your app, or risk wasting memory with duplicate formatters.

## Relationships

- **Inherits From**: [Formatter](formatter.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Formatting Values

- [- stringFromDateComponents:](<datecomponentsformatter/string(from_)-9exxn.md>) — Returns a formatted string based on the specified date component information.
- [- stringForObjectValue:](<datecomponentsformatter/string(for_).md>) — Returns a formatted string based on the date information in the specified object.
- [- stringFromDate:toDate:](<datecomponentsformatter/string(from_to_).md>) — Returns a formatted string based on the time difference between two dates.
- [- stringFromTimeInterval:](<datecomponentsformatter/string(from_)-7sj4j.md>) — Returns a formatted string based on the specified number of seconds.
- [+ localizedStringFromDateComponents:unitsStyle:](<datecomponentsformatter/localizedstring(from_unitsstyle_).md>) — Returns a localized string based on the specified date components and style option.

### Configuring the Formatter Options

- [allowedUnits](datecomponentsformatter/allowedunits.md) — The bitmask of calendrical units such as day and month to include in the output string.
- [allowsFractionalUnits](datecomponentsformatter/allowsfractionalunits.md) — A Boolean indicating whether non-integer units may be used for values.
- [calendar](datecomponentsformatter/calendar.md) — The default calendar to use when formatting date components.
- [collapsesLargestUnit](datecomponentsformatter/collapseslargestunit.md) — A Boolean value indicating whether to collapse the largest unit into smaller units when a certain threshold is met.
- [includesApproximationPhrase](datecomponentsformatter/includesapproximationphrase.md) — A Boolean value indicating whether the resulting phrase reflects an inexact time value.
- [includesTimeRemainingPhrase](datecomponentsformatter/includestimeremainingphrase.md) — A Boolean value indicating whether output strings reflect the amount of time remaining.
- [maximumUnitCount](datecomponentsformatter/maximumunitcount.md) — The maximum number of time units to include in the output string.
- [unitsStyle](datecomponentsformatter/unitsstyle-swift.property.md) — The formatting style for unit names.
- [zeroFormattingBehavior](datecomponentsformatter/zeroformattingbehavior-swift.property.md) — The formatting style for units whose value is 0.

### Constants

- [UnitsStyle](datecomponentsformatter/unitsstyle-swift.enum.md) — Constants for specifying how to represent quantities of time.
- [ZeroFormattingBehavior](datecomponentsformatter/zeroformattingbehavior-swift.struct.md) — Formatting constants for when values contain zeroes.

### Instance Properties

- [formattingContext](datecomponentsformatter/formattingcontext.md) — Not yet supported.
- [referenceDate](datecomponentsformatter/referencedate.md) — Where units have variable length (number of days in a month, number of hours in a day, etc.), `NSDateComponentsFormatter` will calculate as though counting from the date specified by the `referenceDate` in the appropriate calendar. Defaults to `[NSDate dateWithTimeIntervalSinceReferenceDate:0]` at the time of the `-stringForObjectValue:` call if not set. Set to `nil` to get the default behavior.

### Instance Methods

- [- getObjectValue:forString:errorDescription:](<datecomponentsformatter/getobjectvalue(__for_errordescription_).md>) — `NSDateComponentsFormatter` currently only implements formatting, not parsing. Until it implements parsing, this will always return `NO`.

## See Also

### Dates and times

- [DateFormatter](dateformatter.md) — A formatter that converts between dates and their textual representations.
- [RelativeDateTimeFormatter](relativedatetimeformatter.md) — A formatter that creates locale-aware string representations of a relative date or time.
- [DateIntervalFormatter](dateintervalformatter.md) — A formatter that creates string representations of time intervals.
- [ISO8601DateFormatter](iso8601dateformatter.md) — A formatter that converts between dates and their ISO 8601 string representations.
