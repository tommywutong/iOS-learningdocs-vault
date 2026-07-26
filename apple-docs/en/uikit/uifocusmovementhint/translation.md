---
title: translation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusmovementhint/translation
source_url: 'https://developer.apple.com/documentation/uikit/uifocusmovementhint/translation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusmovementhint/translation.json'
content_hash: 'sha256:bedc820df41a5951'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusMovementHint](../uifocusmovementhint.md)

# translation

<sub>Instance Property</sub>

A vector to apply to a transform to match system interaction hinting.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var translation: CGVector { get }
```

## Discussion

This property represents an X,Y-axis translation expressed in points.

## See Also

### Transforming a hint

- [interactionTransform](interactiontransform.md) — A 3D transform that contains the combined transformations of perspective, rotation, and translation.
- [perspectiveTransform](perspectivetransform.md) — A 3D transform that represents a perspective matrix to be applied to match UIKit interaction hinting.
- [rotation](rotation.md) — A vector to apply to a transform to match system interaction hinting.
