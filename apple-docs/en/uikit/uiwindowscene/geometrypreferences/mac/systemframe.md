---
title: systemFrame
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscene/geometrypreferences/mac/systemframe
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/geometrypreferences/mac/systemframe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/geometrypreferences/mac/systemframe.json'
content_hash: 'sha256:f75e8368aa215770'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [UIKit](../../../../uikit.md) · [UIWindowScene](../../../uiwindowscene.md) · [GeometryPreferences](../../geometrypreferences.md) · [Mac](../mac.md)

# systemFrame

<sub>Instance Property</sub>

The preferred frame of the scene, in system coordinates.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var systemFrame: CGRect? { get set }
```

## Discussion

This property represents the preferred frame of the scene in the system coordinate space, where an origin of `(0, 0)` corresponds to the top-left corner of the main display. The default value is [CGRectNull](../../../../coregraphics/cgrectnull.md), which indicates no preferred frame.
