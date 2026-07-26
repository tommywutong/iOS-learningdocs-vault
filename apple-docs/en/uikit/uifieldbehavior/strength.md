---
title: strength
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifieldbehavior/strength
source_url: 'https://developer.apple.com/documentation/uikit/uifieldbehavior/strength'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifieldbehavior/strength.json'
content_hash: 'sha256:6c7bac0a504bfe18'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFieldBehavior](../uifieldbehavior.md)

# strength

<sub>Instance Property</sub>

The strength of the field.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var strength: CGFloat { get set }
```

## Discussion

The default value of this property is `1.0`. The effect of this value is dependent on the type of field. In practice, the best approach for determining the strength of the field you want is to experiment with different values until you get the behavior you want.

## See Also

### Configuring the field attributes

- [position](position.md) — The position of the field in the reference coordinate system.
- [region](region.md) — The shape of the field.
- [falloff](falloff.md) — The rate of decay for the field strength.
- [minimumRadius](minimumradius.md) — The minimum distance at which to start calculating new values for the field.
- [direction](direction.md) — The direction of motion for a linear field.
- [smoothness](smoothness.md) — The smoothness of the noise used to generate the field.
- [animationSpeed](animationspeed.md) — The rate at which the animation should proceed.
