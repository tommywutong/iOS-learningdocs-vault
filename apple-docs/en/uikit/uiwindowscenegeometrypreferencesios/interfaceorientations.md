---
title: interfaceOrientations
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscenegeometrypreferencesios/interfaceorientations
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscenegeometrypreferencesios/interfaceorientations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscenegeometrypreferencesios/interfaceorientations.json'
content_hash: 'sha256:9544e742dcbcb0fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [iOS](../uiwindowscene/geometrypreferences/ios.md)

# interfaceOrientations

<sub>Instance Property</sub>

The preferred interface orientations for the scene.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, assign) UIInterfaceOrientationMask interfaceOrientations;
```

## Discussion

If you specify this value, the system automatically chooses an orientation from the intersection of these preferred orientations and the supported orientations.
