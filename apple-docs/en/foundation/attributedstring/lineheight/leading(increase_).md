---
title: 'leading(increase:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/lineheight/leading(increase:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/lineheight/leading(increase:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/lineheight/leading%28increase%3A%29.json'
content_hash: 'sha256:6c53a2fb56d16f77'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributedString](../../attributedstring.md) · [LineHeight](../lineheight.md)

# leading(increase:)

<sub>Type Method</sub>

Constant line height based on point size and a fixed increase.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func leading(increase: CGFloat) -> AttributedString.LineHeight
```

## Discussion

Defines the line height based on the largest point size plus an `increase` (in points), regardless of the effective ascent and descent of the fonts in use.
