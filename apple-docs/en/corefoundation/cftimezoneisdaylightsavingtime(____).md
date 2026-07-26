---
title: 'CFTimeZoneIsDaylightSavingTime(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cftimezoneisdaylightsavingtime(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cftimezoneisdaylightsavingtime(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftimezoneisdaylightsavingtime%28_%3A_%3A%29.json'
content_hash: 'sha256:9b3d4008d4658bac'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTimeZoneIsDaylightSavingTime(_:_:)

<sub>Function</sub>

Returns whether or not a time zone is in daylight savings time at a specified date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFTimeZoneIsDaylightSavingTime(_ tz: CFTimeZone!, _ at: CFAbsoluteTime) -> Bool
```

## Parameters

- `tz` — The time zone to analyze.

- `at` — The date in `tz` to test for daylight savings.

## Return Value

`true` if `tz` is in daylight savings time at `at`, otherwise `false`.

## See Also

### Getting Daylight Savings Time Information

- [CFTimeZoneGetDaylightSavingTimeOffset](<cftimezonegetdaylightsavingtimeoffset(____).md>) — Returns the daylight saving time offset for a time zone at a given time.
- [CFTimeZoneGetNextDaylightSavingTimeTransition](<cftimezonegetnextdaylightsavingtimetransition(____).md>) — Returns the time in a given time zone of the next daylight saving time transition after a given time.
