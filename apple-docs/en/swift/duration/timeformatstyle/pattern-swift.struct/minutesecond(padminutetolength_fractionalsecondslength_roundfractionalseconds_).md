---
title: 'minuteSecond(padMinuteToLength:fractionalSecondsLength:roundFractionalSeconds:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/duration/timeformatstyle/pattern-swift.struct/minutesecond(padminutetolength:fractionalsecondslength:roundfractionalseconds:)'
source_url: 'https://developer.apple.com/documentation/swift/duration/timeformatstyle/pattern-swift.struct/minutesecond(padminutetolength:fractionalsecondslength:roundfractionalseconds:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/timeformatstyle/pattern-swift.struct/minutesecond%28padminutetolength%3Afractionalsecondslength%3Aroundfractionalseconds%3A%29.json'
content_hash: 'sha256:cc3dcafc00837309'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Duration](../../../duration.md) · [TimeFormatStyle](../../timeformatstyle.md) · [Pattern](../pattern-swift.struct.md)

# minuteSecond(padMinuteToLength:fractionalSecondsLength:roundFractionalSeconds:)

<sub>Type Method</sub>

Returns a pattern to format a duration with minutes and seconds only, with the given unit configurations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func minuteSecond(padMinuteToLength: Int, fractionalSecondsLength: Int = 0, roundFractionalSeconds: FloatingPointRoundingRule = .toNearestOrEven) -> Duration.TimeFormatStyle.Pattern
```

## Parameters

- `padMinuteToLength` — Padding for the minute field. For example, setting this value to `2` formats five minutes as `05:00` in the `en_US` locale.

- `fractionalSecondsLength` — The length of the fractional seconds. For example, setting this value to `2` formats five minutes as `5:00.00` in the `en_US` locale.

- `roundFractionalSeconds` — The rule to use for rounding the seconds value, given the remaining fractional seconds value. Use one of the cases from the [FloatingPointRoundingRule](../../../floatingpointroundingrule.md) enumeration.

## Return Value

A [Pattern](../pattern-swift.struct.md) that formats a duration with minutes and seconds, using the given unit configurations.

## See Also

### Creating a pattern

- [hourMinute(padHourToLength:roundSeconds:)](<hourminute(padhourtolength_roundseconds_).md>) — Returns a pattern to format a duration with hours and minutes only, with the given unit configurations.
- [hourMinuteSecond(padHourToLength:fractionalSecondsLength:roundFractionalSeconds:)](<hourminutesecond(padhourtolength_fractionalsecondslength_roundfractionalseconds_).md>) — Returns a pattern to format a duration with hours, minutes, and seconds, with the given unit configurations.
