---
title: classification
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/surfacesnappinginfo/classification
source_url: 'https://developer.apple.com/documentation/swiftui/surfacesnappinginfo/classification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/surfacesnappinginfo/classification.json'
content_hash: 'sha256:ce9de1d21700fc58'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SurfaceSnappingInfo](../surfacesnappinginfo.md)

# classification

<sub>Instance Property</sub>

A type that provides information about the surface classification the scene is snapped to. This property only has a value if the scene is snapped and `authorizationStatus` is `.authorized`.

<sub>visionOS</sub>

```swift
var classification: SurfaceClassification? { get }
```
