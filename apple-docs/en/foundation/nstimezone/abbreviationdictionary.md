---
title: abbreviationDictionary
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nstimezone/abbreviationdictionary
source_url: 'https://developer.apple.com/documentation/foundation/nstimezone/abbreviationdictionary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstimezone/abbreviationdictionary.json'
content_hash: 'sha256:e230d815b4002ff0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTimeZone](../nstimezone.md)

# abbreviationDictionary

<sub>Type Property</sub>

Returns a dictionary holding the mappings of time zone abbreviations to time zone names.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var abbreviationDictionary: [String : String] { get set }
```

## Return Value

A dictionary holding the mappings of time zone abbreviations to time zone names.

## Discussion

Note that more than one time zone may have the same abbreviation—for example, US/Pacific and Canada/Pacific both use the abbreviation “PST.” In these cases, [abbreviationDictionary](abbreviationdictionary.md) chooses a single name to map the abbreviation to.

## See Also

### Creating Time Zones

- [- initWithName:](<init(name_).md>) — Returns a time zone initialized with a given identifier.
- [- initWithName:data:](<init(name_data_).md>) — Initializes a time zone with a given identifier and time zone data.
- [+ timeZoneWithAbbreviation:](<init(abbreviation_).md>) — Returns the time zone object identified by a given abbreviation.
- [+ timeZoneForSecondsFromGMT:](<init(forsecondsfromgmt_).md>) — Returns a time zone object offset from Greenwich Mean Time by a given number of seconds.
- [knownTimeZoneNames](knowntimezonenames.md) — Returns an array of strings listing the IDs of all the time zones known to the system.
