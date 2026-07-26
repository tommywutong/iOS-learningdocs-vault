---
title: 'nextDaylightSavingTimeTransition(after:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/timezone/nextdaylightsavingtimetransition(after:)'
source_url: 'https://developer.apple.com/documentation/foundation/timezone/nextdaylightsavingtimetransition(after:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/timezone/nextdaylightsavingtimetransition%28after%3A%29.json'
content_hash: 'sha256:c15a7fbae3c18f68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [TimeZone](../timezone.md)

# nextDaylightSavingTimeTransition(after:)

<sub>Instance Method</sub>

Returns the next daylight saving time transition after a given date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nextDaylightSavingTimeTransition(after date: Date) -> Date?
```

## Parameters

- `date` — A date.

## Return Value

The next daylight saving time transition after `date`. Depending on the time zone, this function may return a change of the time zone’s offset from GMT. Returns `nil` if the time zone of the receiver does not observe daylight savings time as of `date`.

## See Also

### Working with Daylight Savings

- [isDaylightSavingTime(for:)](<isdaylightsavingtime(for_).md>) — Returns a Boolean value that indicates whether the receiver uses daylight saving time at a given date.
- [daylightSavingTimeOffset(for:)](<daylightsavingtimeoffset(for_).md>) — Returns the daylight saving time offset for a given date.
- [nextDaylightSavingTimeTransition](nextdaylightsavingtimetransition.md) — The date of the next (after the current instant) daylight saving time transition for the time zone.
