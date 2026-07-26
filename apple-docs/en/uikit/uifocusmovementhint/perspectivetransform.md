---
title: perspectiveTransform
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusmovementhint/perspectivetransform
source_url: 'https://developer.apple.com/documentation/uikit/uifocusmovementhint/perspectivetransform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusmovementhint/perspectivetransform.json'
content_hash: 'sha256:bbcde950bf7c4405'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusMovementHint](../uifocusmovementhint.md)

# perspectiveTransform

<sub>Instance Property</sub>

A 3D transform that represents a perspective matrix to be applied to match UIKit interaction hinting.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var perspectiveTransform: CATransform3D { get }
```

## See Also

### Transforming a hint

- [interactionTransform](interactiontransform.md) — A 3D transform that contains the combined transformations of perspective, rotation, and translation.
- [rotation](rotation.md) — A vector to apply to a transform to match system interaction hinting.
- [translation](translation.md) — A vector to apply to a transform to match system interaction hinting.
