---
title: knownTimeZoneNames
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nstimezone/knowntimezonenames
source_url: 'https://developer.apple.com/documentation/foundation/nstimezone/knowntimezonenames'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstimezone/knowntimezonenames.json'
content_hash: 'sha256:526e1a5d02052179'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTimeZone](../nstimezone.md)

# knownTimeZoneNames

<sub>Type Property</sub>

Returns an array of strings listing the IDs of all the time zones known to the system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var knownTimeZoneNames: [String] { get }
```

## Return Value

An array of strings listing the IDs of all the time zones known to the system.

## Discussion

An array of strings listing the IDs of all the time zones known to the system.

## See Also

### Creating Time Zones

- [- initWithName:](<init(name_).md>) — Returns a time zone initialized with a given identifier.
- [- initWithName:data:](<init(name_data_).md>) — Initializes a time zone with a given identifier and time zone data.
- [+ timeZoneWithAbbreviation:](<init(abbreviation_).md>) — Returns the time zone object identified by a given abbreviation.
- [+ timeZoneForSecondsFromGMT:](<init(forsecondsfromgmt_).md>) — Returns a time zone object offset from Greenwich Mean Time by a given number of seconds.
- [abbreviationDictionary](abbreviationdictionary.md) — Returns a dictionary holding the mappings of time zone abbreviations to time zone names.
