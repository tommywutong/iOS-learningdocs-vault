---
title: transform
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/manipulable/event/value-swift.struct/transform
source_url: 'https://developer.apple.com/documentation/swiftui/manipulable/event/value-swift.struct/transform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/manipulable/event/value-swift.struct/transform.json'
content_hash: 'sha256:ed813237c1921aca'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [SwiftUI](../../../../swiftui.md) · [Manipulable](../../../manipulable.md) · [Event](../../event.md) · [Value](../value-swift.struct.md)

# transform

<sub>Instance Property</sub>

The 3D affine transform of the manipulated view, or `nil` if the view doesn’t have a well-defined 3D affine transfrorm.

<sub>visionOS</sub>

```swift
let transform: AffineTransform3D?
```

## Discussion

A view may not have a well-defined 3D affine transform e.g. when it’s affected by a projection transform.

This transform is in the coordinate space configured in the view modifier.
