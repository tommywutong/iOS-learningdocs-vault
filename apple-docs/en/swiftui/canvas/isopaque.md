---
title: isOpaque
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/canvas/isopaque
source_url: 'https://developer.apple.com/documentation/swiftui/canvas/isopaque'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/canvas/isopaque.json'
content_hash: 'sha256:8809690fd1d5c034'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Canvas](../canvas.md)

# isOpaque

<sub>Instance Property</sub>

A Boolean that indicates whether the canvas is fully opaque.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var isOpaque: Bool { get set }
```

## Discussion

You might be able to improve performance by setting this value to `true`, making the canvas is fully opaque. However, in that case, the result of drawing a non-opaque image into the canvas is undefined.

## See Also

### Managing opacity and color

- [colorMode](colormode.md) — The working color space and storage format of the canvas.
