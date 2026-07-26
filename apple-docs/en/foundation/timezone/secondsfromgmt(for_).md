---
title: 'secondsFromGMT(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/timezone/secondsfromgmt(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/timezone/secondsfromgmt(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/timezone/secondsfromgmt%28for%3A%29.json'
content_hash: 'sha256:d870445617f4d4f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [TimeZone](../timezone.md)

# secondsFromGMT(for:)

<sub>Instance Method</sub>

The current difference in seconds between the time zone and Greenwich Mean Time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func secondsFromGMT(for date: Date = Date()) -> Int
```

## Parameters

- `date` — The date to use for the calculation. The default value is the current date.

## See Also

### Getting Time Zone Information

- [identifier](identifier.md) — The geopolitical region identifier that identifies the time zone.
- [abbreviation(for:)](<abbreviation(for_).md>) — Returns the abbreviation for the time zone at a given date.
- [timeZoneDataVersion](timezonedataversion.md) — Returns the time zone data version.
