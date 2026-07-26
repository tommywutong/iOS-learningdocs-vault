---
title: opaque
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigraphicsimagerendererformat/opaque
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsimagerendererformat/opaque'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsimagerendererformat/opaque.json'
content_hash: 'sha256:77aa9ec89b74ed21'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsImageRendererFormat](../uigraphicsimagerendererformat.md)

# opaque

<sub>Instance Property</sub>

A Boolean value that indicates whether the underlying Core Graphics context has an alpha channel.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var opaque: Bool { get set }
```

## Discussion

Setting the value of this property to [false](../../swift/false.md) specifies that the underlying Core Graphics context has an alpha channel, whereas [true](../../swift/true.md) indicates it does not. The default value is [false](../../swift/false.md).

A Core Graphics context requires an alpha channel to express transparency. Without an alpha channel a Core Graphics context is said to be opaque, i.e. without transparency.

## See Also

### Configuring the renderer attributes

- [scale](scale.md) — The display scale of the image renderer context.
- [preferredRange](preferredrange.md) — The preferred color range of the image renderer context.
- [Range](range.md) — Constants that specify the color range of the image renderer context.
- [prefersExtendedRange](prefersextendedrange.md) — A Boolean value that specifies whether the bitmap context uses extended color. _(deprecated)_
