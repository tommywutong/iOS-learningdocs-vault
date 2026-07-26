---
title: compression
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cimodtransition/compression
source_url: 'https://developer.apple.com/documentation/coreimage/cimodtransition/compression'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cimodtransition/compression.json'
content_hash: 'sha256:979f91e43bafa28e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIModTransition](../cimodtransition.md)

# compression

<sub>Instance Property</sub>

The amount of stretching applied to the mod hole pattern.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var compression: Float { get set }
```

## Discussion

Holes in the center aren’t distorted as much as those at the edge of the image.

## See Also

### Instance Properties

- [angle](angle.md) — The angle of the mod hole pattern.
- [center](center.md) — The x and y position to use as the center of the effect.
- [radius](radius.md) — The radius of the undistorted mod holes in the pattern.
