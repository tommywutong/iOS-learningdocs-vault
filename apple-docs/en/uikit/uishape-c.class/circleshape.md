---
title: circleShape
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uishape-c.class/circleshape
source_url: 'https://developer.apple.com/documentation/uikit/uishape-c.class/circleshape'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uishape-c.class/circleshape.json'
content_hash: 'sha256:53a5d5c15b78e041'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIShape](../uishape-c.class.md)

# circleShape

<sub>Type Property</sub>

Creates a circular shape, with a radius equal to half the length of the frame rectangle’s smallest edge.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (class, nonatomic, readonly) UIShape * circleShape;
```

## See Also

### Creating a hover shape

- [rectShape](rectshape.md) — Creates a rectangular shape.
- [capsuleShape](capsuleshape.md) — Creates a capsule shape, a rounded rectangle with a corner radius equal to half the length of the rectangle’s smallest edge.
- [rectShapeWithCornerRadius:](rectshapewithcornerradius_.md) — Creates a rectangular shape with rounded corners, using the provided corner radius.
- [rectShapeWithCornerRadius:cornerCurve:](rectshapewithcornerradius_cornercurve_.md) — Creates a rectangular shape with rounded corners, using the provided corner radius and corner curve.
- [rectShapeWithCornerRadius:cornerCurve:maskedCorners:](rectshapewithcornerradius_cornercurve_maskedcorners_.md) — Creates a rectangular shape with rounded corners, using the provided corner radius, corner curve, and rectangle corners.
- [fixedRectShapeWithRect:](fixedrectshapewithrect_.md) — Creates a fixed rectangular shape that uses the provided rectangle as its shape, regardless of the frame that contains it.
- [fixedRectShapeWithRect:cornerRadius:](fixedrectshapewithrect_cornerradius_.md) — Creates a fixed rectangular shape with the provided corner radius, using the provided rectangle as its shape.
- [fixedRectShapeWithRect:cornerRadius:cornerCurve:maskedCorners:](fixedrectshapewithrect_cornerradius_cornercurve_maskedcorners_.md) — Creates a fixed rectangular shape with the provided corner radius and corner curve, using the provided rectangle as its shape.
- [UICornerCurve](../uicornercurve.md) — The corner curve to apply to a view.
