---
title: 'multiple(factor:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/lineheight/multiple(factor:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/lineheight/multiple(factor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/lineheight/multiple%28factor%3A%29.json'
content_hash: 'sha256:dd39c004fe808335'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributedString](../../attributedstring.md) · [LineHeight](../lineheight.md)

# multiple(factor:)

<sub>Type Method</sub>

Constant line height based on a multiple of the point size.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func multiple(factor: CGFloat) -> AttributedString.LineHeight
```

## Discussion

Definines the line height based on the largest point size multiplied by `factor`, regardless of the effective ascent and descent of the fonts in use.
