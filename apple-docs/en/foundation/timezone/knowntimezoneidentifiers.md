---
title: knownTimeZoneIdentifiers
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/timezone/knowntimezoneidentifiers
source_url: 'https://developer.apple.com/documentation/foundation/timezone/knowntimezoneidentifiers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/timezone/knowntimezoneidentifiers.json'
content_hash: 'sha256:c758d8293638de99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [TimeZone](../timezone.md)

# knownTimeZoneIdentifiers

<sub>Type Property</sub>

Returns an array of strings listing the identifier of all the time zones known to the system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var knownTimeZoneIdentifiers: [String] { get }
```

## See Also

### Creating a Time Zone

- [init(secondsFromGMT:)](<init(secondsfromgmt_).md>) — Returns a time zone initialized with a specific number of seconds from GMT.
- [abbreviationDictionary](abbreviationdictionary.md) — Returns the mapping of abbreviations to time zone identifiers.
