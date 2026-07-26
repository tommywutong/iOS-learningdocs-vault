---
title: currentImage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigraphicsimagerenderercontext/currentimage
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsimagerenderercontext/currentimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsimagerenderercontext/currentimage.json'
content_hash: 'sha256:1a0c07494785eb13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsImageRendererContext](../uigraphicsimagerenderercontext.md)

# currentImage

<sub>Instance Property</sub>

The current state of the drawing context, expressed as an object that manages image data in your app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var currentImage: UIImage { get }
```

## Discussion

Use this property to access the current Core Graphics context as a [UIImage](../uiimage.md) object while providing drawing instructions for one of the drawing methods in [UIGraphicsImageRenderer](../uigraphicsimagerenderer.md).
