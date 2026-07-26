---
title: NSTimeZone.NameStyle
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nstimezone/namestyle
source_url: 'https://developer.apple.com/documentation/foundation/nstimezone/namestyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstimezone/namestyle.json'
content_hash: 'sha256:043027b4ff6acbb5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTimeZone](../nstimezone.md)

# NSTimeZone.NameStyle

<sub>Enumeration</sub>

Constants you use to specify a style when presenting time zone names.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NameStyle
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSTimeZoneNameStyleStandard](namestyle/standard.md) — Specifies a standard name style. For example, “Central Standard Time” for Central Time.
- [NSTimeZoneNameStyleShortStandard](namestyle/shortstandard.md) — Specifies a short name style. For example, “CST” for Central Time.
- [NSTimeZoneNameStyleDaylightSaving](namestyle/daylightsaving.md) — Specifies a daylight saving name style. For example, “Central Daylight Time” for Central Time.
- [NSTimeZoneNameStyleShortDaylightSaving](namestyle/shortdaylightsaving.md) — Specifies a short daylight saving name style.  For example, “CDT” for Central Time.
- [NSTimeZoneNameStyleGeneric](namestyle/generic.md) — Specifies a generic name style. For example, “Central Time” for Central Time.
- [NSTimeZoneNameStyleShortGeneric](namestyle/shortgeneric.md) — Specifies a generic time zone name. For example, “CT” for Central Time.

### Initializers

- [init(rawValue:)](<namestyle/init(rawvalue_).md>)

## See Also

### Getting Time Zone Information

- [name](name.md) — The geopolitical region ID that identifies the receiver.
- [abbreviation](abbreviation.md) — The abbreviation for the receiver, such as “EDT” (Eastern Daylight Time).
- [- abbreviationForDate:](<abbreviation(for_).md>) — Returns the abbreviation for the receiver at a given date.
- [secondsFromGMT](secondsfromgmt.md) — The current difference in seconds between the receiver and Greenwich Mean Time.
- [- secondsFromGMTForDate:](<secondsfromgmt(for_).md>) — Returns the difference in seconds between the receiver and Greenwich Mean Time at a given date.
- [data](data.md) — The data that stores the information used by the receiver.
- [timeZoneDataVersion](timezonedataversion.md) — Returns the time zone data version.
