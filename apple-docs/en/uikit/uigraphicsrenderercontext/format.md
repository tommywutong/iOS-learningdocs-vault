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
doc_path: /documentation/uikit/uigraphicsrenderercontext/format
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsrenderercontext/format'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsrenderercontext/format.json'
content_hash: 'sha256:7b22d3a1a42f22b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsRendererContext](../uigraphicsrenderercontext.md)

# format

<sub>Instance Property</sub>

The format used to create the associated graphics renderer.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var format: UIGraphicsRendererFormat { get }
```

## Discussion

If you specified a format object when you initialized the current renderer ([UIGraphicsRenderer](../uigraphicsrenderer.md)) object, then this property provides access to that object. Otherwise, a default format object was created for you using the renderer initialization parameters, tuned to the current device.

## See Also

### Getting the drawing context

- [CGContext](cgcontext.md) — The underlying Core Graphics context.
