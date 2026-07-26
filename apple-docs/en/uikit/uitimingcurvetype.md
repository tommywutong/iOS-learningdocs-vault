---
title: UITimingCurveType
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitimingcurvetype
source_url: 'https://developer.apple.com/documentation/uikit/uitimingcurvetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitimingcurvetype.json'
content_hash: 'sha256:e5d1192e3751e369'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITimingCurveType

<sub>Enumeration</sub>

Constants indicating the type of timing information to use.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum UITimingCurveType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UITimingCurveTypeBuiltin](uitimingcurvetype/builtin.md) — Use the built-in UIKit timing curves. Specify this value when you want to use one of the constants in the [AnimationCurve](uiview/animationcurve.md) type. Specify the desired curve using the [cubicTimingParameters](uitimingcurveprovider/cubictimingparameters.md) property.
- [UITimingCurveTypeCubic](uitimingcurvetype/cubic.md) — Use a custom cubic Bézier curve. Specify the curve information using the [cubicTimingParameters](uitimingcurveprovider/cubictimingparameters.md) property.
- [UITimingCurveTypeSpring](uitimingcurvetype/spring.md) — Use a custom spring animation. Specify the desired curve using the [springTimingParameters](uitimingcurveprovider/springtimingparameters.md) property.
- [UITimingCurveTypeComposed](uitimingcurvetype/composed.md) — Use a combination of timing parameters. This type of curve starts with the curve defined by the [cubicTimingParameters](uitimingcurveprovider/cubictimingparameters.md) property and modifies it using the spring information in the [springTimingParameters](uitimingcurveprovider/springtimingparameters.md) property.

### Initializers

- [init(rawValue:)](<uitimingcurvetype/init(rawvalue_).md>)
