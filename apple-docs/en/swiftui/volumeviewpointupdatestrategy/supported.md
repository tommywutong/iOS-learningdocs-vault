---
title: supported
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/volumeviewpointupdatestrategy/supported
source_url: 'https://developer.apple.com/documentation/swiftui/volumeviewpointupdatestrategy/supported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/volumeviewpointupdatestrategy/supported.json'
content_hash: 'sha256:8f98d699484b1330'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VolumeViewpointUpdateStrategy](../volumeviewpointupdatestrategy.md)

# supported

<sub>Type Property</sub>

The action should only be run when the new viewpoint is equivalent to one of the values provided through [supportedVolumeViewpoints(_:)](<../view/supportedvolumeviewpoints(__).md>).

<sub>visionOS</sub>

```swift
static let supported: VolumeViewpointUpdateStrategy
```

## Discussion

The viewpoint will be equivalent to where the window bar and ornaments are presented for a volume.
