---
title: 'time(pattern:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/formatstyle/time(pattern:)'
source_url: 'https://developer.apple.com/documentation/foundation/formatstyle/time(pattern:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatstyle/time%28pattern%3A%29.json'
content_hash: 'sha256:8c99eb081d14d93b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FormatStyle](../formatstyle.md)

# time(pattern:)

<sub>Type Method</sub>

Returns a style for formatting a duration using a provided pattern.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func time(pattern: Duration.TimeFormatStyle.Pattern) -> Self
```

## Parameters

- `pattern` — A [Duration.TimeFormatStyle.Pattern](../../swift/duration/timeformatstyle/pattern-swift.struct.md) that specifies the units to include in the displayed string and the behavior of the units.

## Return Value

A duration time format style customized with the specified pattern.

## Discussion

Use the dot-notation form of this type method when the call point allows the use of [Duration.TimeFormatStyle](../../swift/duration/timeformatstyle.md). You typically do this when calling the [formatted(_:)](<../../swift/duration/formatted(__).md>) method of [Duration](../../swift/duration.md).

The following example creates a duration to represent 1 hour, 10 minutes, 32 seconds, and 400 milliseconds. It then uses [time(pattern:)](<time(pattern_).md>) to customize a [Duration.TimeFormatStyle](../../swift/duration/timeformatstyle.md) to show hours, minutes, and seconds, padding the hours part to two digits and limiting the fractional seconds to two digits. When used with the [formatted(_:)](<../../swift/duration/formatted(__).md>) method, the resulting string is `01:10:32.40`.

```swift
let duration = Duration.seconds(70 * 60 + 32) + Duration.milliseconds(400)
let format = duration.formatted(
    .time(pattern: .hourMinuteSecond(padHourToLength: 2,
                                     fractionalSecondsLength: 2)))
// format == "01:10:32.40"
```

## See Also

### Applying duration styles

- [timeDuration](timeduration.md) — A style for formatting a duration expressed as a range of dates.
- [ComponentsFormatStyle](../date/componentsformatstyle.md) — A style for formatting a date interval in terms of specific date components.
- [units(allowed:width:maximumUnitCount:zeroValueUnits:valueLength:fractionalPart:)](<units(allowed_width_maximumunitcount_zerovalueunits_valuelength_fractionalpart_).md>) — Returns a style for formatting a duration that uses the specified units.
- [units(allowed:width:maximumUnitCount:zeroValueUnits:valueLengthLimits:fractionalPart:)](<units(allowed_width_maximumunitcount_zerovalueunits_valuelengthlimits_fractionalpart_).md>) — Returns a style for formatting a duration range that uses the specified units, with padding/truncating behavior defined as a range.
