---
title: isInterfaceOrientationLocked
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscene/geometry/isinterfaceorientationlocked
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/geometry/isinterfaceorientationlocked'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/geometry/isinterfaceorientationlocked.json'
content_hash: 'sha256:019cfb7902c2a364'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWindowScene](../../uiwindowscene.md) · [Geometry](../geometry.md)

# isInterfaceOrientationLocked

<sub>Instance Property</sub>

If the scene’s interface orientation is locked and preventing changes. To express a preference for this value, override  `UIViewController`’s `prefersInterfaceOrientationLocked`.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isInterfaceOrientationLocked: Bool { get }
```

## See Also

### Accessing scene geometry

- [systemFrame](systemframe.md) — The current frame of the scene, in system coordinates.
- [coordinateSpace](coordinatespace.md) — The coordinate space of the scene
- [interfaceOrientation](interfaceorientation.md) — The current interface orientation for the scene.
