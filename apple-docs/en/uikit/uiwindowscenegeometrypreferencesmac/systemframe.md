---
title: systemFrame
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst 16.0+, tvOS, visionOS]
languages: [occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscenegeometrypreferencesmac/systemframe
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscenegeometrypreferencesmac/systemframe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscenegeometrypreferencesmac/systemframe.json'
content_hash: 'sha256:f28d8240228a6d48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [Mac](../uiwindowscene/geometrypreferences/mac.md)

# systemFrame

<sub>Instance Property</sub>

The preferred frame of the scene, in system coordinates.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, assign) CGRect systemFrame;
```

## Discussion

This property represents the preferred frame of the scene in the system coordinate space, where an origin of `(0, 0)` corresponds to the top-left corner of the main display. The default value is [CGRectNull](../../coregraphics/cgrectnull.md), which indicates no preferred frame.
