---
title: position
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifieldbehavior/position
source_url: 'https://developer.apple.com/documentation/uikit/uifieldbehavior/position'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifieldbehavior/position.json'
content_hash: 'sha256:93ae4b6fa957b1a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFieldBehavior](../uifieldbehavior.md)

# position

<sub>Instance Property</sub>

The position of the field in the reference coordinate system.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var position: CGPoint { get set }
```

## Discussion

This property defines the center point of the field. The shape of the field around this point is defined by the [region](region.md) property.

## See Also

### Configuring the field attributes

- [region](region.md) — The shape of the field.
- [strength](strength.md) — The strength of the field.
- [falloff](falloff.md) — The rate of decay for the field strength.
- [minimumRadius](minimumradius.md) — The minimum distance at which to start calculating new values for the field.
- [direction](direction.md) — The direction of motion for a linear field.
- [smoothness](smoothness.md) — The smoothness of the noise used to generate the field.
- [animationSpeed](animationspeed.md) — The rate at which the animation should proceed.
