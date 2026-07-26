---
title: abbreviation
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nstimezone/abbreviation
source_url: 'https://developer.apple.com/documentation/foundation/nstimezone/abbreviation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstimezone/abbreviation.json'
content_hash: 'sha256:d6fcb73d451be100'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTimeZone](../nstimezone.md)

# abbreviation

<sub>Instance Property</sub>

The abbreviation for the receiver, such as “EDT” (Eastern Daylight Time).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var abbreviation: String? { get }
```

## Discussion

Invokes [- abbreviationForDate:](<abbreviation(for_).md>) with the current date as the argument.

## See Also

### Getting Time Zone Information

- [name](name.md) — The geopolitical region ID that identifies the receiver.
- [- abbreviationForDate:](<abbreviation(for_).md>) — Returns the abbreviation for the receiver at a given date.
- [secondsFromGMT](secondsfromgmt.md) — The current difference in seconds between the receiver and Greenwich Mean Time.
- [- secondsFromGMTForDate:](<secondsfromgmt(for_).md>) — Returns the difference in seconds between the receiver and Greenwich Mean Time at a given date.
- [data](data.md) — The data that stores the information used by the receiver.
- [timeZoneDataVersion](timezonedataversion.md) — Returns the time zone data version.
- [NameStyle](namestyle.md) — Constants you use to specify a style when presenting time zone names.
