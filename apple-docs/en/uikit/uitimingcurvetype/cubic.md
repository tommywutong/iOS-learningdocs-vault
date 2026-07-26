---
title: UITimingCurveType.cubic
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitimingcurvetype/cubic
source_url: 'https://developer.apple.com/documentation/uikit/uitimingcurvetype/cubic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitimingcurvetype/cubic.json'
content_hash: 'sha256:271dcc3034615f3a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITimingCurveType](../uitimingcurvetype.md)

# UITimingCurveType.cubic

<sub>Case</sub>

Use a custom cubic Bézier curve. Specify the curve information using the [cubicTimingParameters](../uitimingcurveprovider/cubictimingparameters.md) property.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case cubic
```

## See Also

### Constants

- [UITimingCurveTypeBuiltin](builtin.md) — Use the built-in UIKit timing curves. Specify this value when you want to use one of the constants in the [AnimationCurve](../uiview/animationcurve.md) type. Specify the desired curve using the [cubicTimingParameters](../uitimingcurveprovider/cubictimingparameters.md) property.
- [UITimingCurveTypeSpring](spring.md) — Use a custom spring animation. Specify the desired curve using the [springTimingParameters](../uitimingcurveprovider/springtimingparameters.md) property.
- [UITimingCurveTypeComposed](composed.md) — Use a combination of timing parameters. This type of curve starts with the curve defined by the [cubicTimingParameters](../uitimingcurveprovider/cubictimingparameters.md) property and modifies it using the spring information in the [springTimingParameters](../uitimingcurveprovider/springtimingparameters.md) property.
