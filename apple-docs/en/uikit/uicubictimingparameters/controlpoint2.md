---
title: controlPoint2
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicubictimingparameters/controlpoint2
source_url: 'https://developer.apple.com/documentation/uikit/uicubictimingparameters/controlpoint2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicubictimingparameters/controlpoint2.json'
content_hash: 'sha256:6682600e79d206ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICubicTimingParameters](../uicubictimingparameters.md)

# controlPoint2

<sub>Instance Property</sub>

The second control point of the cubic Bézier curve.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var controlPoint2: CGPoint { get }
```

## Discussion

This parameter contains the point you specified at initialization time. If you initialized the object with a [AnimationCurve](../uiview/animationcurve.md) value instead, this property is set to [CGPointZero](../../coregraphics/cgpointzero.md).

## See Also

### Getting the timing parameters

- [animationCurve](animationcurve.md) — The standard UIKit animation curve to use for timing.
- [controlPoint1](controlpoint1.md) — The first control point for the cubic Bézier curve.
