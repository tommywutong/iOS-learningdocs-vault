---
title: bounds
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigraphicsrendererformat/bounds
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsrendererformat/bounds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsrendererformat/bounds.json'
content_hash: 'sha256:49c760b410061f99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsRendererFormat](../uigraphicsrendererformat.md)

# bounds

<sub>Instance Property</sub>

The bounds of the graphics context.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var bounds: CGRect { get }
```

## Discussion

This value represents the bounds of every Core Graphics context that the associated graphics renderer creates.

If the graphics renderer itself creates a format object, the bounds are set to those provided to the renderer as part of the initializer.
