---
title: timeZoneDataVersion
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nstimezone/timezonedataversion
source_url: 'https://developer.apple.com/documentation/foundation/nstimezone/timezonedataversion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstimezone/timezonedataversion.json'
content_hash: 'sha256:254f0d419b83e9b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTimeZone](../nstimezone.md)

# timeZoneDataVersion

<sub>Type Property</sub>

Returns the time zone data version.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var timeZoneDataVersion: String { get }
```

## Return Value

A string containing the time zone data version.

## See Also

### Getting Time Zone Information

- [name](name.md) — The geopolitical region ID that identifies the receiver.
- [abbreviation](abbreviation.md) — The abbreviation for the receiver, such as “EDT” (Eastern Daylight Time).
- [- abbreviationForDate:](<abbreviation(for_).md>) — Returns the abbreviation for the receiver at a given date.
- [secondsFromGMT](secondsfromgmt.md) — The current difference in seconds between the receiver and Greenwich Mean Time.
- [- secondsFromGMTForDate:](<secondsfromgmt(for_).md>) — Returns the difference in seconds between the receiver and Greenwich Mean Time at a given date.
- [data](data.md) — The data that stores the information used by the receiver.
- [NameStyle](namestyle.md) — Constants you use to specify a style when presenting time zone names.
