---
title: 'hourMinuteSecond(padHourToLength:fractionalSecondsLength:roundFractionalSeconds:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/duration/timeformatstyle/pattern-swift.struct/hourminutesecond(padhourtolength:fractionalsecondslength:roundfractionalseconds:)'
source_url: 'https://developer.apple.com/documentation/swift/duration/timeformatstyle/pattern-swift.struct/hourminutesecond(padhourtolength:fractionalsecondslength:roundfractionalseconds:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/timeformatstyle/pattern-swift.struct/hourminutesecond%28padhourtolength%3Afractionalsecondslength%3Aroundfractionalseconds%3A%29.json'
content_hash: 'sha256:cf350a2936f19826'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Duration](../../../duration.md) · [TimeFormatStyle](../../timeformatstyle.md) · [Pattern](../pattern-swift.struct.md)

# hourMinuteSecond(padHourToLength:fractionalSecondsLength:roundFractionalSeconds:)

<sub>Type Method</sub>

Returns a pattern to format a duration with hours, minutes, and seconds, with the given unit configurations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func hourMinuteSecond(padHourToLength: Int, fractionalSecondsLength: Int = 0, roundFractionalSeconds: FloatingPointRoundingRule = .toNearestOrEven) -> Duration.TimeFormatStyle.Pattern
```

## Parameters

- `padHourToLength` — Padding for the hour field. For example, setting this value to `2` formats one hour as `01:00` in `en_US` locale.

- `fractionalSecondsLength` — The length of the fractional seconds. For example, setting this value to `2` formats one hour as `1:00:00.00` in the `en_US` locale.

- `roundFractionalSeconds` — The rule to use for rounding the seconds value, given the remaining fractional seconds value. Use one of the cases from the [FloatingPointRoundingRule](../../../floatingpointroundingrule.md) enumeration.

## Return Value

A [Pattern](../pattern-swift.struct.md) that formats a duration with hours, minutes, and seconds, using the given unit configurations.

## See Also

### Creating a pattern

- [hourMinute(padHourToLength:roundSeconds:)](<hourminute(padhourtolength_roundseconds_).md>) — Returns a pattern to format a duration with hours and minutes only, with the given unit configurations.
- [minuteSecond(padMinuteToLength:fractionalSecondsLength:roundFractionalSeconds:)](<minutesecond(padminutetolength_fractionalsecondslength_roundfractionalseconds_).md>) — Returns a pattern to format a duration with minutes and seconds only, with the given unit configurations.
