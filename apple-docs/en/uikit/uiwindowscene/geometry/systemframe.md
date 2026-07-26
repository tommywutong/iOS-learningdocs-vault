---
title: systemFrame
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 16.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscene/geometry/systemframe
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/geometry/systemframe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/geometry/systemframe.json'
content_hash: 'sha256:35973b800566bf81'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWindowScene](../../uiwindowscene.md) · [Geometry](../geometry.md)

# systemFrame

<sub>Instance Property</sub>

The current frame of the scene, in system coordinates.

<sub>Mac Catalyst</sub>

```swift
var systemFrame: CGRect { get }
```

## Discussion

This property represents the current frame of the scene in the system coordinate space, where an origin of `(0, 0)` corresponds to the top-left corner of the main display.

## See Also

### Accessing scene geometry

- [coordinateSpace](coordinatespace.md) — The coordinate space of the scene
- [interfaceOrientation](interfaceorientation.md) — The current interface orientation for the scene.
- [interfaceOrientationLocked](isinterfaceorientationlocked.md) — If the scene’s interface orientation is locked and preventing changes. To express a preference for this value, override  `UIViewController`’s `prefersInterfaceOrientationLocked`.
