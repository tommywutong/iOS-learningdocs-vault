---
title: UITimingCurveType.builtin
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitimingcurvetype/builtin
source_url: 'https://developer.apple.com/documentation/uikit/uitimingcurvetype/builtin'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitimingcurvetype/builtin.json'
content_hash: 'sha256:cd1a762ac42bffc5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITimingCurveType](../uitimingcurvetype.md)

# UITimingCurveType.builtin

<sub>Case</sub>

Use the built-in UIKit timing curves. Specify this value when you want to use one of the constants in the [AnimationCurve](../uiview/animationcurve.md) type. Specify the desired curve using the [cubicTimingParameters](../uitimingcurveprovider/cubictimingparameters.md) property.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case builtin
```

## See Also

### Constants

- [UITimingCurveTypeCubic](cubic.md) — Use a custom cubic Bézier curve. Specify the curve information using the [cubicTimingParameters](../uitimingcurveprovider/cubictimingparameters.md) property.
- [UITimingCurveTypeSpring](spring.md) — Use a custom spring animation. Specify the desired curve using the [springTimingParameters](../uitimingcurveprovider/springtimingparameters.md) property.
- [UITimingCurveTypeComposed](composed.md) — Use a combination of timing parameters. This type of curve starts with the curve defined by the [cubicTimingParameters](../uitimingcurveprovider/cubictimingparameters.md) property and modifies it using the spring information in the [springTimingParameters](../uitimingcurveprovider/springtimingparameters.md) property.
