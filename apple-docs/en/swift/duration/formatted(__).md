---
title: 'formatted(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/duration/formatted(_:)'
source_url: 'https://developer.apple.com/documentation/swift/duration/formatted(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/formatted%28_%3A%29.json'
content_hash: 'sha256:664ab46ca574e14c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Duration](../duration.md)

# formatted(_:)

<sub>Instance Method</sub>

Formats the duration, using the provided format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func formatted<S>(_ v: S) -> S.FormatOutput where S : FormatStyle, S.FormatInput == Duration
```

## Return Value

A localized, formatted string that describes the duration. For example, a duration of 1 hour, 30 minutes, and 56 seconds in the `en_US` locale with a [TimeFormatStyle](timeformatstyle.md) returns `1:30:56`. In the Finnish locale, this returns `1.30.56`.

## Discussion

Use this formatting method to apply a custom style when formatting a duration.

There are two format styles that apply to durations:

- [TimeFormatStyle](timeformatstyle.md) shows durations in a compact, numeric, localized form, like “2:03”.
- [UnitsFormatStyle](unitsformatstyle.md) shows durations with localized labeled components, like “2 min, 3 sec”.

The following example uses a custom [TimeFormatStyle](timeformatstyle.md) that shows hours, minutes, and seconds, and pads the hour part to a minimum of two characters. When it formats a two-second duration, this produces the string `00:00:02`.

```swift
let duration = Duration.seconds(2)
let style = Duration.TimeFormatStyle(pattern: .hourMinuteSecond(padHourToLength: 2))
let formatted = duration.formatted(style) // "00:00:02".
```

Instead of explicitly initializing styles, you can use `Swift/Duration/TimeFormatStyle/time(pattern:)` or `Swift/Duration/UnitsFormatStyle/units(allowed:width:maximumUnitCount:zeroValueUnits:valueLength:fractionalPart:)` in any call that expects a [FormatStyle](../../foundation/formatstyle.md) whose input type is [Duration](../duration.md). This allows you to rewrite the above example as follows:

```swift
let duration = Duration.seconds(2)
let formatted = duration.formatted(
    .time(pattern: .hourMinuteSecond(padHourToLength: 2))) // "00:00:02".
```

## See Also

### Formatting a duration

- [formatted()](<formatted().md>) — Formats the string using a localized hour-minute-second time pattern.
- [TimeFormatStyle](timeformatstyle.md) — A format style that shows durations in a compact, localized format with separators.
- [UnitsFormatStyle](unitsformatstyle.md) — A format style that shows durations with localized labeled components
