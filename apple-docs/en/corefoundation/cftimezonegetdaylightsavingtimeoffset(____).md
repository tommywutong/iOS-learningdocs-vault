---
title: 'CFTimeZoneGetDaylightSavingTimeOffset(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cftimezonegetdaylightsavingtimeoffset(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cftimezonegetdaylightsavingtimeoffset(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftimezonegetdaylightsavingtimeoffset%28_%3A_%3A%29.json'
content_hash: 'sha256:f35468e27bd5ed5c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTimeZoneGetDaylightSavingTimeOffset(_:_:)

<sub>Function</sub>

Returns the daylight saving time offset for a time zone at a given time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFTimeZoneGetDaylightSavingTimeOffset(_ tz: CFTimeZone!, _ at: CFAbsoluteTime) -> CFTimeInterval
```

## Parameters

- `tz` — The time zone to analyze.

- `at` — The time in `tz` to test for daylight saving time offset.

## Return Value

The daylight saving time offset for `tz` at `at`.

## See Also

### Getting Daylight Savings Time Information

- [CFTimeZoneIsDaylightSavingTime](<cftimezoneisdaylightsavingtime(____).md>) — Returns whether or not a time zone is in daylight savings time at a specified date.
- [CFTimeZoneGetNextDaylightSavingTimeTransition](<cftimezonegetnextdaylightsavingtimetransition(____).md>) — Returns the time in a given time zone of the next daylight saving time transition after a given time.
