---
title: preferredRange
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigraphicsimagerendererformat/preferredrange
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsimagerendererformat/preferredrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsimagerendererformat/preferredrange.json'
content_hash: 'sha256:27ccdf50fc15a07e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsImageRendererFormat](../uigraphicsimagerendererformat.md)

# preferredRange

<sub>Instance Property</sub>

The preferred color range of the image renderer context.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var preferredRange: UIGraphicsImageRendererFormat.Range { get set }
```

## Discussion

This property affects the pixel format of the image that the renderer produces.

Different pixel formats can store different color ranges. The system chooses the precise pixel format, but you can set this property to exclude certain formats that support larger or narrower color ranges than you need.

## See Also

### Configuring the renderer attributes

- [opaque](opaque.md) — A Boolean value that indicates whether the underlying Core Graphics context has an alpha channel.
- [scale](scale.md) — The display scale of the image renderer context.
- [Range](range.md) — Constants that specify the color range of the image renderer context.
- [prefersExtendedRange](prefersextendedrange.md) — A Boolean value that specifies whether the bitmap context uses extended color. _(deprecated)_
