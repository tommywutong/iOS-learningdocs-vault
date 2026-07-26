---
title: coordinateSpace
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscene/geometry/coordinatespace
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/geometry/coordinatespace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/geometry/coordinatespace.json'
content_hash: 'sha256:8195f49df3b09f25'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWindowScene](../../uiwindowscene.md) · [Geometry](../geometry.md)

# coordinateSpace

<sub>Instance Property</sub>

The coordinate space of the scene

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var coordinateSpace: any UICoordinateSpace { get }
```

## See Also

### Accessing scene geometry

- [systemFrame](systemframe.md) — The current frame of the scene, in system coordinates.
- [interfaceOrientation](interfaceorientation.md) — The current interface orientation for the scene.
- [interfaceOrientationLocked](isinterfaceorientationlocked.md) — If the scene’s interface orientation is locked and preventing changes. To express a preference for this value, override  `UIViewController`’s `prefersInterfaceOrientationLocked`.
