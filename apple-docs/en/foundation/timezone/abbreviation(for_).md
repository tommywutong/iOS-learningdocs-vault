---
title: 'abbreviation(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/timezone/abbreviation(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/timezone/abbreviation(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/timezone/abbreviation%28for%3A%29.json'
content_hash: 'sha256:cb9cd1b38e6a3df3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [TimeZone](../timezone.md)

# abbreviation(for:)

<sub>Instance Method</sub>

Returns the abbreviation for the time zone at a given date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func abbreviation(for date: Date = Date()) -> String?
```

## Parameters

- `date` — The date to use for the calculation. The default value is the current date.

## Discussion

Note that the abbreviation may be different at different dates. For example, during daylight saving time the US/Eastern time zone has an abbreviation of “EDT.” At other times, its abbreviation is “EST.”

## See Also

### Getting Time Zone Information

- [identifier](identifier.md) — The geopolitical region identifier that identifies the time zone.
- [secondsFromGMT(for:)](<secondsfromgmt(for_).md>) — The current difference in seconds between the time zone and Greenwich Mean Time.
- [timeZoneDataVersion](timezonedataversion.md) — Returns the time zone data version.
