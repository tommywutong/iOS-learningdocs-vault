---
title: data
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nstimezone/data
source_url: 'https://developer.apple.com/documentation/foundation/nstimezone/data'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstimezone/data.json'
content_hash: 'sha256:2602fb16f4e4dd14'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTimeZone](../nstimezone.md)

# data

<sub>Instance Property</sub>

The data that stores the information used by the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var data: Data { get }
```

## Discussion

Treat this data as an opaque object.

## See Also

### Getting Time Zone Information

- [name](name.md) — The geopolitical region ID that identifies the receiver.
- [abbreviation](abbreviation.md) — The abbreviation for the receiver, such as “EDT” (Eastern Daylight Time).
- [- abbreviationForDate:](<abbreviation(for_).md>) — Returns the abbreviation for the receiver at a given date.
- [secondsFromGMT](secondsfromgmt.md) — The current difference in seconds between the receiver and Greenwich Mean Time.
- [- secondsFromGMTForDate:](<secondsfromgmt(for_).md>) — Returns the difference in seconds between the receiver and Greenwich Mean Time at a given date.
- [timeZoneDataVersion](timezonedataversion.md) — Returns the time zone data version.
- [NameStyle](namestyle.md) — Constants you use to specify a style when presenting time zone names.
