---
title: Date.FormatStyle
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle.json'
content_hash: 'sha256:2ad6936a491fd9e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Date](../date.md)

# Date.FormatStyle

<sub>Structure</sub>

A structure that creates a locale-appropriate string representation of a date instance and converts strings of dates and times into date instances.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct FormatStyle
```

## Overview

A date format style shares the date and time formatting pattern preferred by the user’s locale for formatting and parsing.

When you want to apply a specific formatting style to a single [Date](../date.md) instance, use [FormatStyle](formatstyle.md). For other instances, use the following:

- When working with date representations in ISO 8601 format, use [ISO8601FormatStyle](iso8601formatstyle.md).
- To represent an interval between two date instances, use [RelativeFormatStyle](relativeformatstyle.md).
- To represent two dates as a pair, for example to get output that looks like `10/21/1985 1:45 PM - 9/13/2015 6:33 PM`, use [IntervalFormatStyle](intervalformatstyle.md).

### Formatting String Representations of Dates and Times

[FormatStyle](formatstyle.md) provides a variety of localized presets and configuration options to create user-visible representations of dates and times from instances of [Date](../date.md).

When displaying a date to a user, use the [formatted(date:time:)](<formatted(date_time_).md>) instance method. Set the date and time styles of the date format style separately, according to your particular needs.

For example, to create a string with a full date and no time representation, set the [DateStyle](formatstyle/datestyle.md) to [complete](formatstyle/datestyle/complete.md) and the [TimeStyle](formatstyle/timestyle.md) to [omitted](formatstyle/timestyle/omitted.md). Conversely, to create a string representing only the time for the current locale and time zone, set the date style to [omitted](formatstyle/datestyle/omitted.md) and the time style to [complete](formatstyle/timestyle/complete.md), as the following code illustrates:

```swift
let birthday = Date()

birthday.formatted(date: .complete, time: .omitted) // Sunday, January 17, 2021
birthday.formatted(date: .omitted, time: .complete) // 4:03:12 p.m. CST
```

The results shown are for locale set to `en_US` and time zone set to `CST`.

You can create string representations of a [Date](../date.md) instance with various levels of brevity using preset date and time styles. The following example shows date styles of [long](formatstyle/datestyle/long.md), [abbreviated](formatstyle/datestyle/abbreviated.md), and [numeric](formatstyle/datestyle/numeric.md), and time styles of [shortened](formatstyle/timestyle/shortened.md), [standard](formatstyle/timestyle/standard.md), and [complete](formatstyle/timestyle/complete.md):

```swift
let birthday = Date()

birthday.formatted(date: .long, time: .shortened) // January 17, 2021, 4:03 PM
birthday.formatted(date: .abbreviated, time: .standard) // Jan 17, 2021, 4:03:12 PM
birthday.formatted(date: .numeric, time: .complete) // 1/17/2021, 4:03:12 PM CST

birthday.formatted() // Jan 17, 2021, 4:03 PM
```

The default date style is [abbreviated](formatstyle/datestyle/abbreviated.md) and the default time style is [shortened](formatstyle/timestyle/shortened.md).

For full customization of the string representation of a date, use the [formatted(_:)](<formatted(__).md>) instance method of [Date](../date.md) and provide a [FormatStyle](formatstyle.md) instance.

You can apply more customization of the date and time components and their representation in your app by appying a series of convenience modifiers to your format style. The following example applies a series of modifiers to the format style to precisely define the formatting of the year, month, day, hour, minute, and timezone components of the resulting string. The ordering of the date and time modifiers has no impact on the string produced.

```swift
// Call the .formatted method on an instance of Date passing in an instance of Date.FormatStyle.

let birthday = Date()

birthday.formatted(
    Date.FormatStyle()
        .year(.defaultDigits)
        .month(.abbreviated)
        .day(.twoDigits)
        .hour(.defaultDigits(amPM: .abbreviated))
        .minute(.twoDigits)
        .timeZone(.identifier(.long))
        .era(.wide)
        .dayOfYear(.defaultDigits)
        .weekday(.abbreviated)
        .week(.defaultDigits)
) 
// Sun, Jan 17, 2021 Anno Domini (week: 4), 11:18 AM America/Chicago
```

[FormatStyle](formatstyle.md) provides a convenient factory variable, [dateTime](../formatstyle/datetime.md), used to shorten the syntax when applying date and time modifiers to customize the format, as in the following example:

```swift
let localeArray = ["en_US", "sv_SE", "en_GB", "th_TH", "fr_BE"]
for localeID in localeArray {
    print(meetingDate.formatted(.dateTime
             .day(.twoDigits)
             .month(.wide)
             .weekday(.short)
             .hour(.conversationalTwoDigits(amPM: .wide))
             .locale(Locale(identifier: localeID))))
}

// Th, November 12, 7 PM
// to 12 november 19
// Th 12 November, 19
// พฤ. 12 พฤศจิกายน 19
// je 12 novembre, 19 h
```

### Parsing Dates and Times

To parse a [Date](../date.md) instance from an input string, use a date parse strategy. For example:

```swift
let inputString = "Archive for month 8, archived on day 23 - complete."
let strategy = Date.ParseStrategy(format: "Archive for month \(month: .defaultDigits), archived on day \(day: .twoDigits) - complete.", locale: Locale(identifier: "en_US"), timeZone: TimeZone(abbreviation: "CDT")!)
if let date = try? Date(inputString, strategy: strategy) {
   print(date.formatted()) // "Aug 23, 2000 at 12:00 AM"
}
```

The time defaults to midnight local time unless explicitly defined.

The parse instance method attempts to parse a provided string into an instance of date using the source date format style. The function throws an error if it can’t parse the input string into a date instance.

You can use [FormatStyle](formatstyle.md) for round-trip formatting and parsing in a locale-aware manner. This date format style guides parsing the date instance from an input string, as the following code demonstrates:

```swift
let birthdayFormatStyle = Date.FormatStyle()
    .year(.defaultDigits)
    .month(.abbreviated)
    .day(.twoDigits)
    .hour(.defaultDigits(amPM: .abbreviated))
    .minute(.twoDigits)
    .timeZone(.identifier(.long))
    .era(.abbreviated)
    .weekday(.abbreviated)

let yourBirthdayString = "Mon, Feb 17, 1997 AD, 1:27 AM America/Chicago"

// Create a date instance from a string representation of a date.
let yourBirthday = try? birthdayFormatStyle.parse(yourBirthdayString)
// Feb 17, 1997 at 1:27 AM

```

The following round-trip date formatting example uses a date format style to create a locale-aware string representation of a date instance. Then, the date format style guides parsing the newly created string into a new date instance.

```swift
let myFormat = Date.FormatStyle()
    .year()
    .day()
    .month()
    .locale(Locale(identifier: "en_US"))
    
let dateString = Date().formatted(myFormat)
// "Feb 17, 2021" for the "en_US" locale

print(dateString) // Feb 17, 2021

if let anniversary = try? Date(dateString, strategy: myFormat) {
    print(anniversary.formatted(myFormat)) // Feb 17, 2021
    print(anniversary.formatted()) // 2/17/2021, 12:00 AM
} else {
    print("Can't parse string into date with this format.")
}
```

After this code executes, `anniversary` contains a [Date](../date.md) instance parsed from `dateString`.

### Applying Format Styles Repeatedly

Once you create a date format style, you can use it to format dates multiple times.

You can use a format style to parse a set of date instances from a set of string representations of dates. Then, use another format style, applied repeatedly, to produce more detailed string representations of those dates for a different locale. For example:

```swift
func formatIntroDates() {
   let inputFormat = Date.FormatStyle()
      .locale(Locale(identifier: "en_GB"))
      .year()
      .month()
      .day()
    // Parse string inputs into date instances.
    guard let productIntroDate = try? Date("9 Jan 2007", strategy: inputFormat) else { return }
    guard let anotherIntroDate = try? Date("27 Jan 2010", strategy: inputFormat) else { return }
    guard let conferenceDate = try? Date("7 Jun 2021", strategy: inputFormat) else { return }

    let outputFormat = Date.FormatStyle() // Define format style for string output.
        .locale(Locale(identifier: "en_US"))
        .year()
        .month(.wide)
        .day(.twoDigits)
        .weekday(.abbreviated)

    // Apply the output format on the three dates below.
    print(outputFormat.format(conferenceDate)) // Mon, June 07, 2021
    print(outputFormat.format(anotherIntroDate)) // Wed, January 27, 2010
    print(outputFormat.format(productIntroDate)) // Tue, January 09, 2007
}
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomConsumingRegexComponent](../../swift/customconsumingregexcomponent.md), [Decodable](../../swift/decodable.md), [DiscreteFormatStyle](../discreteformatstyle.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [FormatStyle](../formatstyle.md), [Hashable](../../swift/hashable.md), [ParseStrategy](../parsestrategy.md), [ParseableFormatStyle](../parseableformatstyle.md), [RegexComponent](../../swift/regexcomponent.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a Date Format Style

- [init(date:time:locale:calendar:timeZone:capitalizationContext:)](<formatstyle/init(date_time_locale_calendar_timezone_capitalizationcontext_).md>) — Creates an instance using the provided date, time, locale, calendar, time zone, and capitalization context.

### Specifying the Date Format

- [day(_:)](<formatstyle/day(__).md>) — Modifies the date format style to use the specified day format style.
- [dayOfYear(_:)](<formatstyle/dayofyear(__).md>) — Modifies the date format style to use the specified day of the year format style.
- [era(_:)](<formatstyle/era(__).md>) — Modifies the date format style to use the specified era format style.
- [month(_:)](<formatstyle/month(__).md>) — Modifies the date format style to use the specified month format style.
- [quarter(_:)](<formatstyle/quarter(__).md>) — Modifies the date format style to use the specified quarter format style.
- [week(_:)](<formatstyle/week(__).md>) — Modifies the date format style to use the specified week format style.
- [weekday(_:)](<formatstyle/weekday(__).md>) — Modifies the date format style to use the specified weekday format style.
- [year(_:)](<formatstyle/year(__).md>) — Modifies the date format style to use the specified year format style.
- [DateStyle](formatstyle/datestyle.md) — Type that defines date styles varied in length or components included.

### Specifying the Time Format

- [hour(_:)](<formatstyle/hour(__).md>) — Modifies the date format style to use the specified hour format style.
- [minute(_:)](<formatstyle/minute(__).md>) — Modifies the date format style to use the specified minute format style.
- [second(_:)](<formatstyle/second(__).md>) — Modifies the date format style to use the specified second format style.
- [secondFraction(_:)](<formatstyle/secondfraction(__).md>) — Modifies the date format style to use the specified second fraction format style.
- [timeZone(_:)](<formatstyle/timezone(__).md>) — Modifies the date format style to use the specified time zone format style.
- [TimeStyle](formatstyle/timestyle.md) — Type that defines time styles varied in length or components included.

### Modifying a Date Format Style

- [locale(_:)](<formatstyle/locale(__).md>) — Modifies the date format style to use the specified locale.
- [timeZone](formatstyle/timezone.md) — The time zone to use when formatting the date and time components.
- [calendar](formatstyle/calendar.md) — The calendar to use when formatting the date.
- [capitalizationContext](formatstyle/capitalizationcontext.md) — The capitalization context to use when formatting the date.
- [locale](formatstyle/locale.md) — The locale to use when formatting the date and time components.

### Applying Visual Attributes to Dates

- [attributed](formatstyle/attributed-swift.property.md) — An attributed format style created from the date format style. _(deprecated)_
- [AttributedStyle](attributedstyle.md) — A structure that creates a locale-appropriate attributed string representation of a date instance. _(deprecated)_

### Applying a Format Style

- [format(_:)](<formatstyle/format(__).md>) — Creates a locale-aware string representation from a date value.

### Parsing Dates

- [parse(_:)](<formatstyle/parse(__).md>) — Parses a string into a date.
- [parseStrategy](formatstyle/parsestrategy.md) — The strategy used to parse a string into a date.
- [ParseStrategy](parsestrategy.md) — Options for parsing string representations of dates to create a `Date` instance.

### Comparing Date Format Styles

- [==(_:_:)](<==(____).md>) — Returns true if the two `Date` values represent the same point in time.

### Supporting Symbols

- [Symbol](formatstyle/symbol.md) — Types that customize formatting templates either by using the date format style’s modifier functions or by constructing fixed-pattern date format strings.

### Structures

- [Attributed](formatstyle/attributed-swift.struct.md) — The type preserving attributed variant of this style.

### Instance Properties

- [attributedStyle](formatstyle/attributedstyle.md) — Return the type preserving attributed variant of this style.

### Default Implementations

- [CustomConsumingRegexComponent Implementations](formatstyle/customconsumingregexcomponent-implementations.md)
- [FormatStyle Implementations](formatstyle/formatstyle-implementations.md)
- [ParseStrategy Implementations](formatstyle/parsestrategy-implementations.md)
- [ParseableFormatStyle Implementations](formatstyle/parseableformatstyle-implementations.md)
- [RegexComponent Implementations](formatstyle/regexcomponent-implementations.md)

## See Also

### Applying date and time styles

- [dateTime](../formatstyle/datetime.md) — A style for formatting a date and time.
- [ISO8601FormatStyle](iso8601formatstyle.md) — A type that converts between dates and their ISO-8601 string representations.
- [verbatim(_:locale:timeZone:calendar:)](<../formatstyle/verbatim(__locale_timezone_calendar_).md>) — Returns a style for formatting a date with an explicitly-specified style.
- [VerbatimFormatStyle](verbatimformatstyle.md) — A style that formats a date with an explicitly-specified style.
- [interval](../formatstyle/interval.md) — A style for formatting a date interval.
- [IntervalFormatStyle](intervalformatstyle.md) — A format style that creates string representations of date intervals.
- [relative(presentation:unitsStyle:)](<../formatstyle/relative(presentation_unitsstyle_).md>) — Returns a style for formatting a date as relative to the current date.
- [RelativeFormatStyle](relativeformatstyle.md) — A format style that forms locale-aware string representations of a relative date or time.
- [components(style:fields:)](<../formatstyle/components(style_fields_).md>) — Returns a style for formatting a date interval in terms of specific date components.
- [ComponentsFormatStyle](componentsformatstyle.md) — A style for formatting a date interval in terms of specific date components.
