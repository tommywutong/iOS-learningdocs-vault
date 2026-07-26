---
title: exemplarLocation
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/symbol/timezone/exemplarlocation
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/timezone/exemplarlocation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/timezone/exemplarlocation.json'
content_hash: 'sha256:ee3a0f2e83689a4d'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Foundation](../../../../../foundation.md) · [Date](../../../../date.md) · [FormatStyle](../../../formatstyle.md) · [Symbol](../../symbol.md) · [TimeZone](../timezone.md)

# exemplarLocation

<sub>Type Property</sub>

The exemplar city for a timezone.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var exemplarLocation: Date.FormatStyle.Symbol.TimeZone { get }
```

## Discussion

If the exemplar city is unavailable, the system provides the localized exemplar city name for the special zone or `unknown`. For example, `Los Angeles`.

## See Also

### Modifying a Time Zone

- [specificName(_:)](<specificname(__).md>) — Returns the specific, non-location representation of a timezone.
- [genericName(_:)](<genericname(__).md>) — Returns the generic, non-location representation of a timezone.
- [iso8601(_:)](<iso8601(__).md>) — Creates the ISO 8601 representation of the timezone with hours, minutes, and optional seconds.
- [localizedGMT(_:)](<localizedgmt(__).md>) — Returns the localized GMT format representation of a timezone.
- [identifier(_:)](<identifier(__).md>) — Returns the timezone identifier.
- [genericLocation](genericlocation.md) — The generic location representation of a timezone.
