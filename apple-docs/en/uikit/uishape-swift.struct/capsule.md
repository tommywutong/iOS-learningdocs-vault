---
title: capsule
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uishape-swift.struct/capsule
source_url: 'https://developer.apple.com/documentation/uikit/uishape-swift.struct/capsule'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uishape-swift.struct/capsule.json'
content_hash: 'sha256:792426f7e385e844'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIShape](../uishape-swift.struct.md)

# capsule

<sub>Type Property</sub>

Creates a capsule shape, a rounded rectangle with a corner radius equal to half the length of the rectangle’s smallest edge.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static var capsule: UIShape { get }
```

## See Also

### Creating a hover shape

- [rect](rect.md) — Creates a rectangular shape.
- [circle](circle.md) — Creates a circular shape, with a radius equal to half the length of the frame rectangle’s smallest edge.
- [rect(cornerRadius:cornerCurve:maskedCorners:)](<rect(cornerradius_cornercurve_maskedcorners_).md>) — Creates a rectangular shape with rounded corners, using the provided corner radius, corner curve, and rectangle corners.
- [fixedRect(_:cornerRadius:cornerCurve:maskedCorners:)](<fixedrect(__cornerradius_cornercurve_maskedcorners_).md>) — Creates a fixed rectangular shape that uses the provided rectangle as its shape, regardless of the frame that contains it.
- [UICornerCurve](../uicornercurve.md) — The corner curve to apply to a view.
