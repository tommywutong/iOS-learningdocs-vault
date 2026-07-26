---
title: format
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigraphicsrenderer/format
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsrenderer/format'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsrenderer/format.json'
content_hash: 'sha256:de958a47846fc9d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsRenderer](../uigraphicsrenderer.md)

# format

<sub>Instance Property</sub>

The format used to create the graphics renderer.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var format: UIGraphicsRendererFormat { get }
```

## Discussion

The property returns a copy of the [UIGraphicsRendererFormat](../uigraphicsrendererformat.md) instance used to create the graphics renderer.

## See Also

### Configuring the renderer

- [allowsImageOutput](allowsimageoutput.md) — A Boolean value specifying whether the renderer can create output images.
