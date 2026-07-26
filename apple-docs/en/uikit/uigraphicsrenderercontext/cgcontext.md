---
title: cgContext
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigraphicsrenderercontext/cgcontext
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsrenderercontext/cgcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsrenderercontext/cgcontext.json'
content_hash: 'sha256:3d83f687d19917ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsRendererContext](../uigraphicsrenderercontext.md)

# cgContext

<sub>Instance Property</sub>

The underlying Core Graphics context.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var cgContext: CGContext { get }
```

## Discussion

Use this property to gain access to the underlying Core Graphics context when you need more drawing functionality than is offered by UIKit and `UIGraphicsRendererContext`.

For an example of how and when to use the Core Graphics context in an image renderer, see [Using Core Graphics rendering functions](../uigraphicsimagerenderer.md#Using-Core-Graphics-rendering-functions) in [UIGraphicsImageRenderer](../uigraphicsimagerenderer.md).

## See Also

### Getting the drawing context

- [format](format.md) — The format used to create the associated graphics renderer.
