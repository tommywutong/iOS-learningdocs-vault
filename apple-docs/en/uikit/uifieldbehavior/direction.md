---
title: direction
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifieldbehavior/direction
source_url: 'https://developer.apple.com/documentation/uikit/uifieldbehavior/direction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifieldbehavior/direction.json'
content_hash: 'sha256:ba4b8dcb0164986d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFieldBehavior](../uifieldbehavior.md)

# direction

<sub>Instance Property</sub>

The direction of motion for a linear field.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var direction: CGVector { get set }
```

## Discussion

Use this property to specify the direction of motion for velocity and linear gravity fields. For nondirectional fields, the default value of this property is a zero vector.

## See Also

### Configuring the field attributes

- [position](position.md) — The position of the field in the reference coordinate system.
- [region](region.md) — The shape of the field.
- [strength](strength.md) — The strength of the field.
- [falloff](falloff.md) — The rate of decay for the field strength.
- [minimumRadius](minimumradius.md) — The minimum distance at which to start calculating new values for the field.
- [smoothness](smoothness.md) — The smoothness of the noise used to generate the field.
- [animationSpeed](animationspeed.md) — The rate at which the animation should proceed.
