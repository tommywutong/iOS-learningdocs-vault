---
title: 'CFTimeZoneGetSecondsFromGMT(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cftimezonegetsecondsfromgmt(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cftimezonegetsecondsfromgmt(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftimezonegetsecondsfromgmt%28_%3A_%3A%29.json'
content_hash: 'sha256:ce3dbf0bc627d15c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTimeZoneGetSecondsFromGMT(_:_:)

<sub>Function</sub>

Returns the difference in seconds between the receiver and Greenwich Mean Time (GMT) at the specified date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFTimeZoneGetSecondsFromGMT(_ tz: CFTimeZone!, _ at: CFAbsoluteTime) -> CFTimeInterval
```

## Parameters

- `tz` — The time zone to analyze.

- `at` — The date at which the interval is to be computed.

## Return Value

The difference in seconds between `tz` and GMT at the specified date, `at`.

## See Also

### Getting Information About Time Zones

- [CFTimeZoneGetName](<cftimezonegetname(__).md>) — Returns the geopolitical region name that identifies a given time zone.
- [CFTimeZoneCopyLocalizedName](<cftimezonecopylocalizedname(______).md>) — Returns the localized name of a given time zone.
- [CFTimeZoneGetData](<cftimezonegetdata(__).md>) — Returns the data that stores the information used by a time zone.
