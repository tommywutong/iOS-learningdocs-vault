---
title: 'init(secondsFromGMT:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/timezone/init(secondsfromgmt:)'
source_url: 'https://developer.apple.com/documentation/foundation/timezone/init(secondsfromgmt:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/timezone/init%28secondsfromgmt%3A%29.json'
content_hash: 'sha256:e0d113a3da69e86d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [TimeZone](../timezone.md)

# init(secondsFromGMT:)

<sub>Initializer</sub>

Returns a time zone initialized with a specific number of seconds from GMT.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(secondsFromGMT seconds: Int)
```

## Parameters

- `seconds` — The number of seconds from GMT.

## Return Value

A time zone, or `nil` if a valid time zone could not be created from `seconds`.

## Discussion

Time zones created with this never have daylight savings and the offset is constant no matter the date. The identifier and abbreviation do NOT follow the POSIX convention (of minutes-west).

## See Also

### Creating a Time Zone

- [knownTimeZoneIdentifiers](knowntimezoneidentifiers.md) — Returns an array of strings listing the identifier of all the time zones known to the system.
- [abbreviationDictionary](abbreviationdictionary.md) — Returns the mapping of abbreviations to time zone identifiers.
