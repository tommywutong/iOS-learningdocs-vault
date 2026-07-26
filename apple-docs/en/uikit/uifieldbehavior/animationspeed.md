---
title: animationSpeed
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifieldbehavior/animationspeed
source_url: 'https://developer.apple.com/documentation/uikit/uifieldbehavior/animationspeed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifieldbehavior/animationspeed.json'
content_hash: 'sha256:b231d57399715668'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFieldBehavior](../uifieldbehavior.md)

# animationSpeed

<sub>Instance Property</sub>

The rate at which the animation should proceed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var animationSpeed: CGFloat { get set }
```

## Discussion

For noise and turbulence fields, this property contains the speed at which to animate the field. For all other fields, the value of this property is always `0.0`.

A value of `1.0` means the field animations occur at normal speed. Values less than `1.0` result in animations that are slower than normal, and values greater than `1.0` result in animations that are faster than normal. A value of `0.0` means that the field does not animate at all.

## See Also

### Configuring the field attributes

- [position](position.md) — The position of the field in the reference coordinate system.
- [region](region.md) — The shape of the field.
- [strength](strength.md) — The strength of the field.
- [falloff](falloff.md) — The rate of decay for the field strength.
- [minimumRadius](minimumradius.md) — The minimum distance at which to start calculating new values for the field.
- [direction](direction.md) — The direction of motion for a linear field.
- [smoothness](smoothness.md) — The smoothness of the noise used to generate the field.
