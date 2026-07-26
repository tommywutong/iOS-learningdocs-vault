---
title: abbreviationDictionary
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/timezone/abbreviationdictionary
source_url: 'https://developer.apple.com/documentation/foundation/timezone/abbreviationdictionary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/timezone/abbreviationdictionary.json'
content_hash: 'sha256:8ff550553aa1ab46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [TimeZone](../timezone.md)

# abbreviationDictionary

<sub>Type Property</sub>

Returns the mapping of abbreviations to time zone identifiers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var abbreviationDictionary: [String : String] { get set }
```

## See Also

### Creating a Time Zone

- [init(secondsFromGMT:)](<init(secondsfromgmt_).md>) — Returns a time zone initialized with a specific number of seconds from GMT.
- [knownTimeZoneIdentifiers](knowntimezoneidentifiers.md) — Returns an array of strings listing the identifier of all the time zones known to the system.
