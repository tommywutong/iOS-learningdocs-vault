---
title: 'timeZoneWithName:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nstimezone/timezonewithname:'
source_url: 'https://developer.apple.com/documentation/foundation/nstimezone/timezonewithname:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstimezone/timezonewithname%3A.json'
content_hash: 'sha256:424797e1f5686986'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTimeZone](../nstimezone.md)

# timeZoneWithName:

<sub>Type Method</sub>

Returns the time zone object identified by a given identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) timeZoneWithName:(NSString *) tzName;
```

## Parameters

- `tzName` — The ID for the time zone.

## Return Value

The time zone in the information directory with a name matching `tzName`. Returns `nil` if there is no match for the name.

## See Also

### Creating Time Zones

- [timeZoneWithName:data:](timezonewithname_data_.md) — Returns the time zone with a given identifier whose data has been initialized using given data.
- [- initWithName:](<init(name_).md>) — Returns a time zone initialized with a given identifier.
- [- initWithName:data:](<init(name_data_).md>) — Initializes a time zone with a given identifier and time zone data.
- [+ timeZoneWithAbbreviation:](<init(abbreviation_).md>) — Returns the time zone object identified by a given abbreviation.
- [+ timeZoneForSecondsFromGMT:](<init(forsecondsfromgmt_).md>) — Returns a time zone object offset from Greenwich Mean Time by a given number of seconds.
- [knownTimeZoneNames](knowntimezonenames.md) — Returns an array of strings listing the IDs of all the time zones known to the system.
- [abbreviationDictionary](abbreviationdictionary.md) — Returns a dictionary holding the mappings of time zone abbreviations to time zone names.
