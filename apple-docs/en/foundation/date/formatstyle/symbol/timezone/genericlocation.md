---
title: genericLocation
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/symbol/timezone/genericlocation
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/timezone/genericlocation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/timezone/genericlocation.json'
content_hash: 'sha256:ff92b5d189dc98c9'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Foundation](../../../../../foundation.md) · [Date](../../../../date.md) · [FormatStyle](../../../formatstyle.md) · [Symbol](../../symbol.md) · [TimeZone](../timezone.md)

# genericLocation

<sub>Type Property</sub>

The generic location representation of a timezone.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var genericLocation: Date.FormatStyle.Symbol.TimeZone { get }
```

## Discussion

If the generic location is unavailable, the system provides the value of [localizedGMT(_:)](<localizedgmt(__).md>) with a `long` width. For example, `Los Angeles Time`.

## See Also

### Modifying a Time Zone

- [specificName(_:)](<specificname(__).md>) — Returns the specific, non-location representation of a timezone.
- [genericName(_:)](<genericname(__).md>) — Returns the generic, non-location representation of a timezone.
- [iso8601(_:)](<iso8601(__).md>) — Creates the ISO 8601 representation of the timezone with hours, minutes, and optional seconds.
- [localizedGMT(_:)](<localizedgmt(__).md>) — Returns the localized GMT format representation of a timezone.
- [identifier(_:)](<identifier(__).md>) — Returns the timezone identifier.
- [exemplarLocation](exemplarlocation.md) — The exemplar city for a timezone.
