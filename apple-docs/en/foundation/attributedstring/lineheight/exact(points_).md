---
title: 'exact(points:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/lineheight/exact(points:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/lineheight/exact(points:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/lineheight/exact%28points%3A%29.json'
content_hash: 'sha256:1c89a1489dbd6a7c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributedString](../../attributedstring.md) · [LineHeight](../lineheight.md)

# exact(points:)

<sub>Type Method</sub>

Constant line height based on a fixed total.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func exact(points: CGFloat) -> AttributedString.LineHeight
```

## Discussion

Defines the line height as the exact given total (in points), regardless of the effective ascent and descent of the fonts in use.
