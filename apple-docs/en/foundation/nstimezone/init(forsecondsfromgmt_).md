---
title: 'init(forSecondsFromGMT:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nstimezone/init(forsecondsfromgmt:)'
source_url: 'https://developer.apple.com/documentation/foundation/nstimezone/init(forsecondsfromgmt:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstimezone/init%28forsecondsfromgmt%3A%29.json'
content_hash: 'sha256:1939b384e356d813'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTimeZone](../nstimezone.md)

# init(forSecondsFromGMT:)

<sub>Initializer</sub>

Returns a time zone object offset from Greenwich Mean Time by a given number of seconds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(forSecondsFromGMT seconds: Int)
```

## Parameters

- `seconds` — The number of seconds by which the new time zone is offset from GMT.

## Return Value

A time zone object offset from Greenwich Mean Time by `seconds`.

## Discussion

The name of the new time zone is GMT +/– the offset, in hours and minutes. Time zones created with this method never have daylight savings, and the offset is constant no matter the date.

## See Also

### Creating Time Zones

- [- initWithName:](<init(name_).md>) — Returns a time zone initialized with a given identifier.
- [- initWithName:data:](<init(name_data_).md>) — Initializes a time zone with a given identifier and time zone data.
- [+ timeZoneWithAbbreviation:](<init(abbreviation_).md>) — Returns the time zone object identified by a given abbreviation.
- [knownTimeZoneNames](knowntimezonenames.md) — Returns an array of strings listing the IDs of all the time zones known to the system.
- [abbreviationDictionary](abbreviationdictionary.md) — Returns a dictionary holding the mappings of time zone abbreviations to time zone names.
