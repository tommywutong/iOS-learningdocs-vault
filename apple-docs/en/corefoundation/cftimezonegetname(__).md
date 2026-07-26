---
title: 'CFTimeZoneGetName(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cftimezonegetname(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cftimezonegetname(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftimezonegetname%28_%3A%29.json'
content_hash: 'sha256:7ef3feb5c89dbcf2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTimeZoneGetName(_:)

<sub>Function</sub>

Returns the geopolitical region name that identifies a given time zone.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFTimeZoneGetName(_ tz: CFTimeZone!) -> CFString!
```

## Parameters

- `tz` — The time zone to analyze.

## Return Value

A string containing the geopolitical region name that identifies `tz`. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## See Also

### Getting Information About Time Zones

- [CFTimeZoneCopyLocalizedName](<cftimezonecopylocalizedname(______).md>) — Returns the localized name of a given time zone.
- [CFTimeZoneGetSecondsFromGMT](<cftimezonegetsecondsfromgmt(____).md>) — Returns the difference in seconds between the receiver and Greenwich Mean Time (GMT) at the specified date.
- [CFTimeZoneGetData](<cftimezonegetdata(__).md>) — Returns the data that stores the information used by a time zone.
