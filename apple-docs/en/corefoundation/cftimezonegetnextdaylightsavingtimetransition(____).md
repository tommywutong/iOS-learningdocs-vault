---
title: 'CFTimeZoneGetNextDaylightSavingTimeTransition(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cftimezonegetnextdaylightsavingtimetransition(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cftimezonegetnextdaylightsavingtimetransition(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftimezonegetnextdaylightsavingtimetransition%28_%3A_%3A%29.json'
content_hash: 'sha256:111d63533927b64f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTimeZoneGetNextDaylightSavingTimeTransition(_:_:)

<sub>Function</sub>

Returns the time in a given time zone of the next daylight saving time transition after a given time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFTimeZoneGetNextDaylightSavingTimeTransition(_ tz: CFTimeZone!, _ at: CFAbsoluteTime) -> CFAbsoluteTime
```

## Parameters

- `tz` — The time zone to analyze.

- `at` — A time in `tz`.

## Return Value

The time in `tz` of the next daylight saving time transition after `at`.

## See Also

### Getting Daylight Savings Time Information

- [CFTimeZoneIsDaylightSavingTime](<cftimezoneisdaylightsavingtime(____).md>) — Returns whether or not a time zone is in daylight savings time at a specified date.
- [CFTimeZoneGetDaylightSavingTimeOffset](<cftimezonegetdaylightsavingtimeoffset(____).md>) — Returns the daylight saving time offset for a time zone at a given time.
