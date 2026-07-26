---
title: 'init(name:data:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nstimezone/init(name:data:)'
source_url: 'https://developer.apple.com/documentation/foundation/nstimezone/init(name:data:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstimezone/init%28name%3Adata%3A%29.json'
content_hash: 'sha256:da0004a8a7346211'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTimeZone](../nstimezone.md)

# init(name:data:)

<sub>Initializer</sub>

Initializes a time zone with a given identifier and time zone data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(name tzName: String, data aData: Data?)
```

## Parameters

- `tzName` — The identifier for the time zone. Providing `nil` for this parameter raises an invalid argument exception.

- `aData` — This parameter is ignored.

## Discussion

As of macOS 10.6, the underlying implementation of this method has been changed to ignore the specified `data` parameter.

> [!important] Important
> You should not use this method. Instead, use [- initWithName:](<init(name_).md>) to initialize a time zone object with a given name.

## See Also

### Creating Time Zones

- [- initWithName:](<init(name_).md>) — Returns a time zone initialized with a given identifier.
- [+ timeZoneWithAbbreviation:](<init(abbreviation_).md>) — Returns the time zone object identified by a given abbreviation.
- [+ timeZoneForSecondsFromGMT:](<init(forsecondsfromgmt_).md>) — Returns a time zone object offset from Greenwich Mean Time by a given number of seconds.
- [knownTimeZoneNames](knowntimezonenames.md) — Returns an array of strings listing the IDs of all the time zones known to the system.
- [abbreviationDictionary](abbreviationdictionary.md) — Returns a dictionary holding the mappings of time zone abbreviations to time zone names.
