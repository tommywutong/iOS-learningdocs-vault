---
title: allowsImageOutput
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigraphicsrenderer/allowsimageoutput
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsrenderer/allowsimageoutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsrenderer/allowsimageoutput.json'
content_hash: 'sha256:a6d0e8572799d6cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsRenderer](../uigraphicsrenderer.md)

# allowsImageOutput

<sub>Instance Property</sub>

A Boolean value specifying whether the renderer can create output images.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var allowsImageOutput: Bool { get }
```

## Discussion

If [true](../../swift/true.md), this renderer can be used to generate [CGImage](../../coregraphics/cgimage.md) objects.

## See Also

### Configuring the renderer

- [format](format.md) — The format used to create the graphics renderer.
