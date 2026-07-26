---
title: orientation
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/squareazimuth/orientation
source_url: 'https://developer.apple.com/documentation/swiftui/squareazimuth/orientation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/squareazimuth/orientation.json'
content_hash: 'sha256:6c8733f74ff18eaa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SquareAzimuth](../squareazimuth.md)

# orientation

<sub>Instance Property</sub>

A 3D rotation that is snapped to the center of one of the four sides.

<sub>visionOS</sub>

```swift
var orientation: Rotation3D { get }
```

## Discussion

The angle will be equal to `0°`, `90°`, `180°`, or `270°`.
