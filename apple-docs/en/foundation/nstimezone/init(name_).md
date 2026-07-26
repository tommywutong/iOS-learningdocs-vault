---
title: 'init(name:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nstimezone/init(name:)'
source_url: 'https://developer.apple.com/documentation/foundation/nstimezone/init(name:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstimezone/init%28name%3A%29.json'
content_hash: 'sha256:f81a203d802e7307'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTimeZone](../nstimezone.md)

# init(name:)

<sub>Initializer</sub>

Returns a time zone initialized with a given identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(name tzName: String)
```

## Parameters

- `tzName` — The identifier for the time zone. Providing `nil` for this parameter raises an invalid argument exception.

## Return Value

A time zone object initialized with the identifier `tzName`.

## Discussion

If `tzName` is a known identifier, this method calls [- initWithName:data:](<init(name_data_).md>) with the appropriate data object.

## See Also

### Creating Time Zones

- [- initWithName:data:](<init(name_data_).md>) — Initializes a time zone with a given identifier and time zone data.
- [+ timeZoneWithAbbreviation:](<init(abbreviation_).md>) — Returns the time zone object identified by a given abbreviation.
- [+ timeZoneForSecondsFromGMT:](<init(forsecondsfromgmt_).md>) — Returns a time zone object offset from Greenwich Mean Time by a given number of seconds.
- [knownTimeZoneNames](knowntimezonenames.md) — Returns an array of strings listing the IDs of all the time zones known to the system.
- [abbreviationDictionary](abbreviationdictionary.md) — Returns a dictionary holding the mappings of time zone abbreviations to time zone names.
