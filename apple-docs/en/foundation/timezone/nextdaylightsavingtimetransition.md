---
title: nextDaylightSavingTimeTransition
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/timezone/nextdaylightsavingtimetransition
source_url: 'https://developer.apple.com/documentation/foundation/timezone/nextdaylightsavingtimetransition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/timezone/nextdaylightsavingtimetransition.json'
content_hash: 'sha256:7609cb00fb11b4f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [TimeZone](../timezone.md)

# nextDaylightSavingTimeTransition

<sub>Instance Property</sub>

The date of the next (after the current instant) daylight saving time transition for the time zone.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var nextDaylightSavingTimeTransition: Date? { get }
```

## Discussion

Depending on the time zone, the value of this property may represent a change of the time zone’s offset from GMT. The value is `nil` if the time zone does not currently observe daylight saving time.

## See Also

### Working with Daylight Savings

- [isDaylightSavingTime(for:)](<isdaylightsavingtime(for_).md>) — Returns a Boolean value that indicates whether the receiver uses daylight saving time at a given date.
- [daylightSavingTimeOffset(for:)](<daylightsavingtimeoffset(for_).md>) — Returns the daylight saving time offset for a given date.
- [nextDaylightSavingTimeTransition(after:)](<nextdaylightsavingtimetransition(after_).md>) — Returns the next daylight saving time transition after a given date.
