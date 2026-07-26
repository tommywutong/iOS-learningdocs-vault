---
title: interfaceOrientation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscene/geometry/interfaceorientation
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/geometry/interfaceorientation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/geometry/interfaceorientation.json'
content_hash: 'sha256:e55360f206308989'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWindowScene](../../uiwindowscene.md) · [Geometry](../geometry.md)

# interfaceOrientation

<sub>Instance Property</sub>

The current interface orientation for the scene.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var interfaceOrientation: UIInterfaceOrientation { get }
```

## See Also

### Accessing scene geometry

- [systemFrame](systemframe.md) — The current frame of the scene, in system coordinates.
- [coordinateSpace](coordinatespace.md) — The coordinate space of the scene
- [interfaceOrientationLocked](isinterfaceorientationlocked.md) — If the scene’s interface orientation is locked and preventing changes. To express a preference for this value, override  `UIViewController`’s `prefersInterfaceOrientationLocked`.
