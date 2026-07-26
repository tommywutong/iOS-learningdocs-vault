---
title: 'rectShapeWithCornerRadius:cornerCurve:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uishape-c.class/rectshapewithcornerradius:cornercurve:'
source_url: 'https://developer.apple.com/documentation/uikit/uishape-c.class/rectshapewithcornerradius:cornercurve:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uishape-c.class/rectshapewithcornerradius%3Acornercurve%3A.json'
content_hash: 'sha256:26af96834642e344'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIShape](../uishape-c.class.md)

# rectShapeWithCornerRadius:cornerCurve:

<sub>Type Method</sub>

Creates a rectangular shape with rounded corners, using the provided corner radius and corner curve.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) rectShapeWithCornerRadius:(CGFloat) cornerRadius cornerCurve:(UICornerCurve) cornerCurve;
```

## See Also

### Creating a hover shape

- [rectShape](rectshape.md) — Creates a rectangular shape.
- [capsuleShape](capsuleshape.md) — Creates a capsule shape, a rounded rectangle with a corner radius equal to half the length of the rectangle’s smallest edge.
- [circleShape](circleshape.md) — Creates a circular shape, with a radius equal to half the length of the frame rectangle’s smallest edge.
- [rectShapeWithCornerRadius:](rectshapewithcornerradius_.md) — Creates a rectangular shape with rounded corners, using the provided corner radius.
- [rectShapeWithCornerRadius:cornerCurve:maskedCorners:](rectshapewithcornerradius_cornercurve_maskedcorners_.md) — Creates a rectangular shape with rounded corners, using the provided corner radius, corner curve, and rectangle corners.
- [fixedRectShapeWithRect:](fixedrectshapewithrect_.md) — Creates a fixed rectangular shape that uses the provided rectangle as its shape, regardless of the frame that contains it.
- [fixedRectShapeWithRect:cornerRadius:](fixedrectshapewithrect_cornerradius_.md) — Creates a fixed rectangular shape with the provided corner radius, using the provided rectangle as its shape.
- [fixedRectShapeWithRect:cornerRadius:cornerCurve:maskedCorners:](fixedrectshapewithrect_cornerradius_cornercurve_maskedcorners_.md) — Creates a fixed rectangular shape with the provided corner radius and corner curve, using the provided rectangle as its shape.
- [UICornerCurve](../uicornercurve.md) — The corner curve to apply to a view.
