---
title: 'specificName(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/formatstyle/symbol/timezone/specificname(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/timezone/specificname(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/timezone/specificname%28_%3A%29.json'
content_hash: 'sha256:1e805df318b01a65'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Foundation](../../../../../foundation.md) · [Date](../../../../date.md) · [FormatStyle](../../../formatstyle.md) · [Symbol](../../symbol.md) · [TimeZone](../timezone.md)

# specificName(_:)

<sub>Type Method</sub>

Returns the specific, non-location representation of a timezone.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func specificName(_ width: Date.FormatStyle.Symbol.TimeZone.Width) -> Date.FormatStyle.Symbol.TimeZone
```

## Parameters

- `width` — Specifies the width of the string result.

## Return Value

A timezone format style appropriate for the locale and specified width.

## Discussion

The value falls back to the value of [localizedGMT(_:)](<localizedgmt(__).md>) with a `short` width if unavailable. For example, `PDT` ([Date.FormatStyle.Symbol.TimeZone.Width.short](width/short.md)), or `Pacific Daylight Time` ([Date.FormatStyle.Symbol.TimeZone.Width.long](width/long.md)).

## See Also

### Modifying a Time Zone

- [genericName(_:)](<genericname(__).md>) — Returns the generic, non-location representation of a timezone.
- [iso8601(_:)](<iso8601(__).md>) — Creates the ISO 8601 representation of the timezone with hours, minutes, and optional seconds.
- [localizedGMT(_:)](<localizedgmt(__).md>) — Returns the localized GMT format representation of a timezone.
- [identifier(_:)](<identifier(__).md>) — Returns the timezone identifier.
- [exemplarLocation](exemplarlocation.md) — The exemplar city for a timezone.
- [genericLocation](genericlocation.md) — The generic location representation of a timezone.
