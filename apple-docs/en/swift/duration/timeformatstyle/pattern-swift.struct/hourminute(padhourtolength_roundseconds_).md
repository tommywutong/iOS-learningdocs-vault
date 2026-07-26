---
title: 'hourMinute(padHourToLength:roundSeconds:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/duration/timeformatstyle/pattern-swift.struct/hourminute(padhourtolength:roundseconds:)'
source_url: 'https://developer.apple.com/documentation/swift/duration/timeformatstyle/pattern-swift.struct/hourminute(padhourtolength:roundseconds:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/timeformatstyle/pattern-swift.struct/hourminute%28padhourtolength%3Aroundseconds%3A%29.json'
content_hash: 'sha256:88f05a46a8ec9d67'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Duration](../../../duration.md) · [TimeFormatStyle](../../timeformatstyle.md) · [Pattern](../pattern-swift.struct.md)

# hourMinute(padHourToLength:roundSeconds:)

<sub>Type Method</sub>

Returns a pattern to format a duration with hours and minutes only, with the given unit configurations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func hourMinute(padHourToLength: Int, roundSeconds: FloatingPointRoundingRule = .toNearestOrEven) -> Duration.TimeFormatStyle.Pattern
```

## Parameters

- `padHourToLength` — Padding for the hour field. For example, setting this value to `2` formats one hour as `01:00` in the `en_US` locale.

- `roundSeconds` — The rule to use for rounding the minutes value, given the remaining seconds value. Use one of the cases from the [FloatingPointRoundingRule](../../../floatingpointroundingrule.md) enumeration.

## Return Value

A [Pattern](../pattern-swift.struct.md) that formats a duration with hours and minutes only, using the given unit configurations.

## See Also

### Creating a pattern

- [hourMinuteSecond(padHourToLength:fractionalSecondsLength:roundFractionalSeconds:)](<hourminutesecond(padhourtolength_fractionalsecondslength_roundfractionalseconds_).md>) — Returns a pattern to format a duration with hours, minutes, and seconds, with the given unit configurations.
- [minuteSecond(padMinuteToLength:fractionalSecondsLength:roundFractionalSeconds:)](<minutesecond(padminutetolength_fractionalsecondslength_roundfractionalseconds_).md>) — Returns a pattern to format a duration with minutes and seconds only, with the given unit configurations.
