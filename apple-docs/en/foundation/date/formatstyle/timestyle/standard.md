---
title: standard
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/timestyle/standard
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/timestyle/standard'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/timestyle/standard.json'
content_hash: 'sha256:280a1444689768f1'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Date](../../../date.md) · [FormatStyle](../../formatstyle.md) · [TimeStyle](../timestyle.md)

# standard

<sub>Type Property</sub>

A time style with all components except the time zone represented.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let standard: Date.FormatStyle.TimeStyle
```

## Discussion

A `standard` time style represents the hour, minute, second, and day period components in the format. For example, `9:54:29 PM.`

## See Also

### Modifying a Time Style

- [complete](complete.md) — A time style with all components represented.
- [omitted](omitted.md) — A time style with no time-related components represented.
- [shortened](shortened.md) — A shortened time style with only the hour, minute, and day period components represented.
