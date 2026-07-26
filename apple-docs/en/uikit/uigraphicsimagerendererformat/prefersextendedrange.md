---
title: prefersExtendedRange
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+（12.0 起废弃）, iPadOS 10.0+（12.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS 10.0+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uigraphicsimagerendererformat/prefersextendedrange
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsimagerendererformat/prefersextendedrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsimagerendererformat/prefersextendedrange.json'
content_hash: 'sha256:85a4255fd0e9677e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsImageRendererFormat](../uigraphicsimagerendererformat.md)

# prefersExtendedRange

<sub>Instance Property</sub>

A Boolean value that specifies whether the bitmap context uses extended color.

> [!warning] Deprecated
> Use [preferredRange](preferredrange.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var prefersExtendedRange: Bool { get set }
```

## Discussion

If [true](../../swift/true.md), the underlying Core Graphics context is configured to support wide color; if [false](../../swift/false.md), the context is not.

The default is [true](../../swift/true.md) on devices that natively support wide color, and [false](../../swift/false.md) on those that do not.

## See Also

### Configuring the renderer attributes

- [opaque](opaque.md) — A Boolean value that indicates whether the underlying Core Graphics context has an alpha channel.
- [scale](scale.md) — The display scale of the image renderer context.
- [preferredRange](preferredrange.md) — The preferred color range of the image renderer context.
- [Range](range.md) — Constants that specify the color range of the image renderer context.
