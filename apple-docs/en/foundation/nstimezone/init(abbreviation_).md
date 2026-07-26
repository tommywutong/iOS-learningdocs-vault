---
title: 'init(abbreviation:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nstimezone/init(abbreviation:)'
source_url: 'https://developer.apple.com/documentation/foundation/nstimezone/init(abbreviation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstimezone/init%28abbreviation%3A%29.json'
content_hash: 'sha256:7da88eb2077d3231'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTimeZone](../nstimezone.md)

# init(abbreviation:)

<sub>Initializer</sub>

Returns the time zone object identified by a given abbreviation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init?(abbreviation: String)
```

## Parameters

- `abbreviation` — An abbreviation for a time zone.

## Return Value

The time zone object identified by `abbreviation` determined by resolving the abbreviation to a name using the abbreviation dictionary and then returning the time zone for that name. Returns `nil` if there is no match for `abbreviation`.

## Discussion

In general, you are discouraged from using abbreviations except for unique instances such as “GMT”. Time Zone abbreviations are not standardized and so a given abbreviation may have multiple meanings—for example, “EST” refers to Eastern Time in both the United States and Australia

## See Also

### Related Documentation

- [Date and Time Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html#//apple_ref/doc/uid/10000039i)

### Creating Time Zones

- [- initWithName:](<init(name_).md>) — Returns a time zone initialized with a given identifier.
- [- initWithName:data:](<init(name_data_).md>) — Initializes a time zone with a given identifier and time zone data.
- [+ timeZoneForSecondsFromGMT:](<init(forsecondsfromgmt_).md>) — Returns a time zone object offset from Greenwich Mean Time by a given number of seconds.
- [knownTimeZoneNames](knowntimezonenames.md) — Returns an array of strings listing the IDs of all the time zones known to the system.
- [abbreviationDictionary](abbreviationdictionary.md) — Returns a dictionary holding the mappings of time zone abbreviations to time zone names.
