---
title: named
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/relativeformatstyle/presentation-swift.struct/named
source_url: 'https://developer.apple.com/documentation/foundation/date/relativeformatstyle/presentation-swift.struct/named'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/relativeformatstyle/presentation-swift.struct/named.json'
content_hash: 'sha256:7f525db04f87ffea'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Date](../../../date.md) · [RelativeFormatStyle](../../relativeformatstyle.md) · [Presentation](../presentation-swift.struct.md)

# named

<sub>Type Property</sub>

A style that uses named styles to describe relative dates, such as “yesterday”, “last week”, or “next week”.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var named: Date.RelativeFormatStyle.Presentation { get }
```

## Discussion

The format uses the [numeric](numeric.md) style if a name isn’t available.

## See Also

### Modifying Relative Date Style Presentations

- [numeric](numeric.md) — A style that uses a numeric style to describe relative dates, such as “1 day ago” or “in 3 weeks”.
