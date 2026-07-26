---
title: cubicTimingParameters
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitimingcurveprovider/cubictimingparameters
source_url: 'https://developer.apple.com/documentation/uikit/uitimingcurveprovider/cubictimingparameters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitimingcurveprovider/cubictimingparameters.json'
content_hash: 'sha256:069919cc2a539a88'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITimingCurveProvider](../uitimingcurveprovider.md)

# cubicTimingParameters

<sub>Instance Property</sub>

The cubic timing parameters to use.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var cubicTimingParameters: UICubicTimingParameters? { get }
```

## Discussion

Implement this property and use it to provide your custom cubic timing information. If the value of the [timingCurveType](timingcurvetype.md) property is [UITimingCurveTypeBuiltin](../uitimingcurvetype/builtin.md), [UITimingCurveTypeCubic](../uitimingcurvetype/cubic.md), or [UITimingCurveTypeComposed](../uitimingcurvetype/composed.md), you must return an object from this property. The object you return can specify one of the built-in UIKit curves, such as [UIViewAnimationCurveLinear](../uiview/animationcurve/linear.md), or it can specify a timing curve based on a custom Bézier path.

For more information about configuring this object, see [UICubicTimingParameters](../uicubictimingparameters.md).

## See Also

### Getting the timing information

- [timingCurveType](timingcurvetype.md) — The type of timing information to use.
- [springTimingParameters](springtimingparameters.md) — The spring-based timing parameters to use.
