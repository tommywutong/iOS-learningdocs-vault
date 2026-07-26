---
title: 'nextDaylightSavingTimeTransition(after:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nstimezone/nextdaylightsavingtimetransition(after:)'
source_url: 'https://developer.apple.com/documentation/foundation/nstimezone/nextdaylightsavingtimetransition(after:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstimezone/nextdaylightsavingtimetransition%28after%3A%29.json'
content_hash: 'sha256:7ac3e689c59e8590'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTimeZone](../nstimezone.md)

# nextDaylightSavingTimeTransition(after:)

<sub>Instance Method</sub>

Returns the next daylight saving time transition after a given date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nextDaylightSavingTimeTransition(after aDate: Date) -> Date?
```

## Parameters

- `aDate` — A date.

## Return Value

The next daylight saving time transition after `aDate`. Depending on the time zone of the receiver, this method may return a change of the time zone’s offset from GMT. Returns `nil` if the time zone of the receiver does not observe daylight savings time as of `aDate`.

## See Also

### Working with Daylight Savings

- [daylightSavingTime](isdaylightsavingtime.md) — A Boolean value that indicates whether the receiver is currently using daylight saving time.
- [- isDaylightSavingTimeForDate:](<isdaylightsavingtime(for_).md>) — Indicates whether the receiver uses daylight saving time on a given date.
- [daylightSavingTimeOffset](daylightsavingtimeoffset.md) — The current daylight saving time offset of the receiver.
- [- daylightSavingTimeOffsetForDate:](<daylightsavingtimeoffset(for_).md>) — Returns the daylight saving time offset for a given date.
- [nextDaylightSavingTimeTransition](nextdaylightsavingtimetransition.md) — The date of the next daylight saving time transition for the receiver.
