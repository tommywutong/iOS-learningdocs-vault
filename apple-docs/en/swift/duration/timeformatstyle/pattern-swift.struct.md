---
title: Duration.TimeFormatStyle.Pattern
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/duration/timeformatstyle/pattern-swift.struct
source_url: 'https://developer.apple.com/documentation/swift/duration/timeformatstyle/pattern-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/timeformatstyle/pattern-swift.struct.json'
content_hash: 'sha256:059eff9c86ab8442'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Duration](../../duration.md) · [TimeFormatStyle](../timeformatstyle.md)

# Duration.TimeFormatStyle.Pattern

<sub>Structure</sub>

The units — including hours, minutes, or seconds — and the configuration of those units, used to format a duration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Pattern
```

## Overview

Use a pattern when initializing a [TimeFormatStyle](../timeformatstyle.md), or creating a time format style from the convenience method `Swift/Duration/TimeFormatStyle/time(pattern:)`.

Use the type properties [hourMinute](pattern-swift.struct/hourminute.md), [hourMinuteSecond](pattern-swift.struct/hourminutesecond.md), or [minuteSecond](pattern-swift.struct/minutesecond.md) to create patterns with default behavior. To customize how a pattern handles zero-padding and fractional parts, use one of the type methods that take these customizations as parameters.

## Relationships

- **Conforms To**: [Decodable](../../decodable.md), [Encodable](../../encodable.md), [Equatable](../../equatable.md), [Hashable](../../hashable.md), [Sendable](../../sendable.md), [SendableMetatype](../../sendablemetatype.md)

## Topics

### Creating a pattern

- [hourMinute(padHourToLength:roundSeconds:)](<pattern-swift.struct/hourminute(padhourtolength_roundseconds_).md>) — Returns a pattern to format a duration with hours and minutes only, with the given unit configurations.
- [hourMinuteSecond(padHourToLength:fractionalSecondsLength:roundFractionalSeconds:)](<pattern-swift.struct/hourminutesecond(padhourtolength_fractionalsecondslength_roundfractionalseconds_).md>) — Returns a pattern to format a duration with hours, minutes, and seconds, with the given unit configurations.
- [minuteSecond(padMinuteToLength:fractionalSecondsLength:roundFractionalSeconds:)](<pattern-swift.struct/minutesecond(padminutetolength_fractionalsecondslength_roundfractionalseconds_).md>) — Returns a pattern to format a duration with minutes and seconds only, with the given unit configurations.

### Using common patterns

- [hourMinute](pattern-swift.struct/hourminute.md) — A pattern to format a duration with hours and minutes only, with default padding and rounding behavior.
- [hourMinuteSecond](pattern-swift.struct/hourminutesecond.md) — A pattern to format a duration with hours, minutes, and seconds, with default padding and rounding behavior.
- [minuteSecond](pattern-swift.struct/minutesecond.md) — A pattern to format a duration with minutes and seconds only, with default padding and rounding behavior.

## See Also

### Creating a time format style

- [init(pattern:locale:)](<init(pattern_locale_).md>) — Creates a time format style using the provided pattern and optional locale.
