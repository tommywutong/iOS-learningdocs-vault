---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/worldscalingbehavior/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/worldscalingbehavior/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/worldscalingbehavior/automatic.json'
content_hash: 'sha256:2a6281a6794d6ae9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WorldScalingBehavior](../worldscalingbehavior.md)

# automatic

<sub>Type Property</sub>

The scaling behavior that is standard for the window’s style.

<sub>visionOS</sub>

```swift
static var automatic: WorldScalingBehavior { get }
```

## Discussion

By default, regular [WindowGroup](../windowgroup.md) windows have dynamic scaling, while windows with a [volumetric](../windowstyle/volumetric.md) window style use fixed scaling.
