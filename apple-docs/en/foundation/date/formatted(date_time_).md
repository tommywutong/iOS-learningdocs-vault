---
title: 'formatted(date:time:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/formatted(date:time:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/formatted(date:time:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatted%28date%3Atime%3A%29.json'
content_hash: 'sha256:81136e388a21567f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Date](../date.md)

# formatted(date:time:)

<sub>Instance Method</sub>

Generates a locale-aware string representation of a date using specified date and time format styles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func formatted(date: Date.FormatStyle.DateStyle, time: Date.FormatStyle.TimeStyle) -> String
```

## Parameters

- `date` — The date format style to apply to the date.

- `time` — The time format style to apply to the date.

## Return Value

A string, formatted according to the specified date and time styles.

## Discussion

When displaying a date to a user, use the convenient [formatted(date:time:)](<formatted(date_time_).md>) instance method to customize the string representation of the date. Set the date and time styles of the date format style separately, according to your particular needs.

For example, to create a string with a full date and no time representation, set the [DateStyle](formatstyle/datestyle.md) to [complete](formatstyle/datestyle/complete.md) and the [TimeStyle](formatstyle/timestyle.md) to [omitted](formatstyle/timestyle/omitted.md). Conversely, to create a string representing only the time, set the date style to [omitted](formatstyle/datestyle/omitted.md) and the time style to [complete](formatstyle/timestyle/complete.md).

```swift
let birthday = Date()

birthday.formatted(date: .complete, time: .omitted) // Sunday, January 17, 2021
birthday.formatted(date: .omitted, time: .complete) // 4:03:12 PM CST
```

You can create string representations of a [Date](../date.md) instance with several levels of brevity using a variety of preset date and time styles. This example shows date styles of [long](formatstyle/datestyle/long.md), [abbreviated](formatstyle/datestyle/abbreviated.md), and [numeric](formatstyle/datestyle/numeric.md), and time styles of [shortened](formatstyle/timestyle/shortened.md), [standard](formatstyle/timestyle/standard.md), and [complete](formatstyle/timestyle/complete.md).

```swift
let birthday = Date()

birthday.formatted(date: .long, time: .shortened) // January 17, 2021, 4:03 PM
birthday.formatted(date: .abbreviated, time: .standard) // Jan 17, 2021, 4:03:12 PM
birthday.formatted(date: .numeric, time: .complete) // 1/17/2021, 4:03:12 PM CST

birthday.formatted() // Jan 17, 2021, 4:03 PM
```

The default date style is [abbreviated](formatstyle/datestyle/abbreviated.md) and the default time style is [shortened](formatstyle/timestyle/shortened.md).

For the default date formatting, use the [formatted()](<formatted().md>) method. To customize the formatted measurement string, use the [formatted(_:)](<formatted(__).md>) method and include a `Date.FormatStyle`.

For more information about formatting dates, see the [FormatStyle](formatstyle.md).

## See Also

### Formatting a Date

- [formatted()](<formatted().md>) — Generates a locale-aware string representation of a date using the default date format style.
- [formatted(_:)](<formatted(__).md>) — Generates a locale-aware string representation of a date using the specified date format style.
- [FormatStyle](formatstyle.md) — A structure that creates a locale-appropriate string representation of a date instance and converts strings of dates and times into date instances.
- [RelativeFormatStyle](relativeformatstyle.md) — A format style that forms locale-aware string representations of a relative date or time.
- [IntervalFormatStyle](intervalformatstyle.md) — A format style that creates string representations of date intervals.
- [ISO8601Format(_:)](<iso8601format(__).md>) — Generates a locale-aware string representation of a date using the ISO 8601 date format.
- [ISO8601FormatStyle](iso8601formatstyle.md) — A type that converts between dates and their ISO-8601 string representations.
