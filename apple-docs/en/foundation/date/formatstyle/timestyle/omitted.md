---
title: omitted
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/timestyle/omitted
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/timestyle/omitted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/timestyle/omitted.json'
content_hash: 'sha256:468e3b11986dcde4'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Date](../../../date.md) · [FormatStyle](../../formatstyle.md) · [TimeStyle](../timestyle.md)

# omitted

<sub>Type Property</sub>

A time style with no time-related components represented.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let omitted: Date.FormatStyle.TimeStyle
```

## Discussion

If both the date style and time style are set to `omitted`, the time is represented using the default style of `shortened`.

## See Also

### Modifying a Time Style

- [complete](complete.md) — A time style with all components represented.
- [shortened](shortened.md) — A shortened time style with only the hour, minute, and day period components represented.
- [standard](standard.md) — A time style with all components except the time zone represented.
