---
title: font
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisimpletextprintformatter/font
source_url: 'https://developer.apple.com/documentation/uikit/uisimpletextprintformatter/font'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisimpletextprintformatter/font.json'
content_hash: 'sha256:37136524b99943b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISimpleTextPrintFormatter](../uisimpletextprintformatter.md)

# font

<sub>Instance Property</sub>

The font of the printed text.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var font: UIFont? { get set }
```

## Discussion

If the value of this property is `nil` (the default), UIKit uses the standard system font, 12 points.

## See Also

### Text attributes for printed content

- [color](color.md) — The color of the printed text.
- [textAlignment](textalignment.md) — The alignment of the printed text.
