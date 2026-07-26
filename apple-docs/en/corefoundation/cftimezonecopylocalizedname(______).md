---
title: 'CFTimeZoneCopyLocalizedName(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cftimezonecopylocalizedname(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cftimezonecopylocalizedname(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftimezonecopylocalizedname%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:28f41c31f49871e3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTimeZoneCopyLocalizedName(_:_:_:)

<sub>Function</sub>

Returns the localized name of a given time zone.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFTimeZoneCopyLocalizedName(_ tz: CFTimeZone!, _ style: CFTimeZoneNameStyle, _ locale: CFLocale!) -> CFString!
```

## Parameters

- `tz` — The time zone to analyze.

- `style` — The style for the returned name.

- `locale` — The locale for which to localize the returned name.

## Return Value

The name of `tz` localized for `locale`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Getting Information About Time Zones

- [CFTimeZoneGetName](<cftimezonegetname(__).md>) — Returns the geopolitical region name that identifies a given time zone.
- [CFTimeZoneGetSecondsFromGMT](<cftimezonegetsecondsfromgmt(____).md>) — Returns the difference in seconds between the receiver and Greenwich Mean Time (GMT) at the specified date.
- [CFTimeZoneGetData](<cftimezonegetdata(__).md>) — Returns the data that stores the information used by a time zone.
