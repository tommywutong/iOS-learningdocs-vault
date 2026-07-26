---
title: default
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/texthighlightstyle/default
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/texthighlightstyle/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/texthighlightstyle/default.json'
content_hash: 'sha256:45a9ee55846b68d9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [TextHighlightStyle](../texthighlightstyle.md)

# default

<sub>Type Property</sub>

The default highlight style to apply to text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let `default`: NSAttributedString.TextHighlightStyle
```

## Discussion

Use this constant as the value for the [textHighlightStyle](../key/texthighlightstyle.md) attribute. The system applies the default highlight color to your text. To specify a different highlight color, add the [textHighlightColorScheme](../key/texthighlightcolorscheme.md) attribute to your text and set its value to the color you want.
