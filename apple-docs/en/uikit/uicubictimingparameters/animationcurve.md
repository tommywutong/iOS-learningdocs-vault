---
title: animationCurve
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicubictimingparameters/animationcurve
source_url: 'https://developer.apple.com/documentation/uikit/uicubictimingparameters/animationcurve'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicubictimingparameters/animationcurve.json'
content_hash: 'sha256:f72afa04fc9aadcf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICubicTimingParameters](../uicubictimingparameters.md)

# animationCurve

<sub>Instance Property</sub>

The standard UIKit animation curve to use for timing.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var animationCurve: UIView.AnimationCurve { get }
```

## Discussion

If you initialized this object using an animation curve, this property reflects the curve you specified. If you initialized the object using the control points for a cubic Bézier curve, the value of this property is undefined.

## See Also

### Getting the timing parameters

- [controlPoint1](controlpoint1.md) — The first control point for the cubic Bézier curve.
- [controlPoint2](controlpoint2.md) — The second control point of the cubic Bézier curve.
