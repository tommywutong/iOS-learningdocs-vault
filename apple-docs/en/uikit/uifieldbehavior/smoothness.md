---
title: smoothness
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifieldbehavior/smoothness
source_url: 'https://developer.apple.com/documentation/uikit/uifieldbehavior/smoothness'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifieldbehavior/smoothness.json'
content_hash: 'sha256:4603c2ebca6da0cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFieldBehavior](../uifieldbehavior.md)

# smoothness

<sub>Instance Property</sub>

The smoothness of the noise used to generate the field.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var smoothness: CGFloat { get set }
```

## Discussion

For noise and turbulence fields, this value specifies the amount of noise or turbulence. The value of this property is in the range `0.0` to `1.0`, where `0.0` represents the maximum noise or turbulence and `1.0` represents the least amount of noise or turbulence.

## See Also

### Configuring the field attributes

- [position](position.md) — The position of the field in the reference coordinate system.
- [region](region.md) — The shape of the field.
- [strength](strength.md) — The strength of the field.
- [falloff](falloff.md) — The rate of decay for the field strength.
- [minimumRadius](minimumradius.md) — The minimum distance at which to start calculating new values for the field.
- [direction](direction.md) — The direction of motion for a linear field.
- [animationSpeed](animationspeed.md) — The rate at which the animation should proceed.
