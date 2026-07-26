---
title: color
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisimpletextprintformatter/color
source_url: 'https://developer.apple.com/documentation/uikit/uisimpletextprintformatter/color'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisimpletextprintformatter/color.json'
content_hash: 'sha256:609e33eed6ca8bb9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISimpleTextPrintFormatter](../uisimpletextprintformatter.md)

# color

<sub>Instance Property</sub>

The color of the printed text.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var color: UIColor? { get set }
```

## Discussion

If the value of this property is `nil` (the default), UIKit uses a black color when printing.

## See Also

### Text attributes for printed content

- [font](font.md) — The font of the printed text.
- [textAlignment](textalignment.md) — The alignment of the printed text.
