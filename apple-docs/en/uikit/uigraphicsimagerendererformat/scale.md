---
title: scale
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigraphicsimagerendererformat/scale
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsimagerendererformat/scale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsimagerendererformat/scale.json'
content_hash: 'sha256:922c7b98b5f3cfa5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsImageRendererFormat](../uigraphicsimagerendererformat.md)

# scale

<sub>Instance Property</sub>

The display scale of the image renderer context.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var scale: CGFloat { get set }
```

## Discussion

The display scale determines the number of pixels per point.

The default value is equal to the [scale](../uiscreen/scale.md) of the main screen.

## See Also

### Configuring the renderer attributes

- [opaque](opaque.md) — A Boolean value that indicates whether the underlying Core Graphics context has an alpha channel.
- [preferredRange](preferredrange.md) — The preferred color range of the image renderer context.
- [Range](range.md) — Constants that specify the color range of the image renderer context.
- [prefersExtendedRange](prefersextendedrange.md) — A Boolean value that specifies whether the bitmap context uses extended color. _(deprecated)_
