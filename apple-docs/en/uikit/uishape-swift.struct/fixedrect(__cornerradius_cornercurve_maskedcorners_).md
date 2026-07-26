---
title: 'fixedRect(_:cornerRadius:cornerCurve:maskedCorners:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uishape-swift.struct/fixedrect(_:cornerradius:cornercurve:maskedcorners:)'
source_url: 'https://developer.apple.com/documentation/uikit/uishape-swift.struct/fixedrect(_:cornerradius:cornercurve:maskedcorners:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uishape-swift.struct/fixedrect%28_%3Acornerradius%3Acornercurve%3Amaskedcorners%3A%29.json'
content_hash: 'sha256:a28140682deac56b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIShape](../uishape-swift.struct.md)

# fixedRect(_:cornerRadius:cornerCurve:maskedCorners:)

<sub>Type Method</sub>

Creates a fixed rectangular shape that uses the provided rectangle as its shape, regardless of the frame that contains it.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static func fixedRect(_ rect: CGRect, cornerRadius: CGFloat = 0, cornerCurve: UICornerCurve = .automatic, maskedCorners: UIRectCorner = .allCorners) -> UIShape
```

## See Also

### Creating a hover shape

- [rect](rect.md) — Creates a rectangular shape.
- [capsule](capsule.md) — Creates a capsule shape, a rounded rectangle with a corner radius equal to half the length of the rectangle’s smallest edge.
- [circle](circle.md) — Creates a circular shape, with a radius equal to half the length of the frame rectangle’s smallest edge.
- [rect(cornerRadius:cornerCurve:maskedCorners:)](<rect(cornerradius_cornercurve_maskedcorners_).md>) — Creates a rectangular shape with rounded corners, using the provided corner radius, corner curve, and rectangle corners.
- [UICornerCurve](../uicornercurve.md) — The corner curve to apply to a view.
