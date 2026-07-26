---
title: 'CFTimeZoneGetData(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cftimezonegetdata(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cftimezonegetdata(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftimezonegetdata%28_%3A%29.json'
content_hash: 'sha256:8c75e3dbbf138368'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTimeZoneGetData(_:)

<sub>Function</sub>

Returns the data that stores the information used by a time zone.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFTimeZoneGetData(_ tz: CFTimeZone!) -> CFData!
```

## Parameters

- `tz` — The time zone to analyze.

## Return Value

The data used to store `tz`. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1). May be `NULL` if the timezone does not have any data or use Olson data for its information.

## See Also

### Getting Information About Time Zones

- [CFTimeZoneGetName](<cftimezonegetname(__).md>) — Returns the geopolitical region name that identifies a given time zone.
- [CFTimeZoneCopyLocalizedName](<cftimezonecopylocalizedname(______).md>) — Returns the localized name of a given time zone.
- [CFTimeZoneGetSecondsFromGMT](<cftimezonegetsecondsfromgmt(____).md>) — Returns the difference in seconds between the receiver and Greenwich Mean Time (GMT) at the specified date.
