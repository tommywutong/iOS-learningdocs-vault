---
title: rotation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusmovementhint/rotation
source_url: 'https://developer.apple.com/documentation/uikit/uifocusmovementhint/rotation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusmovementhint/rotation.json'
content_hash: 'sha256:4acf1155f243c22c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusMovementHint](../uifocusmovementhint.md)

# rotation

<sub>Instance Property</sub>

A vector to apply to a transform to match system interaction hinting.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var rotation: CGVector { get }
```

## Discussion

This property represents an X,Y-axis translation expressed in radians.

## See Also

### Transforming a hint

- [interactionTransform](interactiontransform.md) — A 3D transform that contains the combined transformations of perspective, rotation, and translation.
- [perspectiveTransform](perspectivetransform.md) — A 3D transform that represents a perspective matrix to be applied to match UIKit interaction hinting.
- [translation](translation.md) — A vector to apply to a transform to match system interaction hinting.
