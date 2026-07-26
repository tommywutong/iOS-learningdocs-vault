---
title: interfaceOrientations
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscene/geometrypreferences/ios/interfaceorientations
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/geometrypreferences/ios/interfaceorientations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/geometrypreferences/ios/interfaceorientations.json'
content_hash: 'sha256:15f9269d922fb4a9'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [UIKit](../../../../uikit.md) · [UIWindowScene](../../../uiwindowscene.md) · [GeometryPreferences](../../geometrypreferences.md) · [iOS](../ios.md)

# interfaceOrientations

<sub>Instance Property</sub>

The preferred interface orientations for the scene.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var interfaceOrientations: UIInterfaceOrientationMask? { get set }
```

## Discussion

If you specify this value, the system automatically chooses an orientation from the intersection of these preferred orientations and the supported orientations.
