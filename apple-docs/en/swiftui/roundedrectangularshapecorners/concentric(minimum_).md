---
title: 'concentric(minimum:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/roundedrectangularshapecorners/concentric(minimum:)'
source_url: 'https://developer.apple.com/documentation/swiftui/roundedrectangularshapecorners/concentric(minimum:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/roundedrectangularshapecorners/concentric%28minimum%3A%29.json'
content_hash: 'sha256:fac4645c23843bd2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [RoundedRectangularShapeCorners](../roundedrectangularshapecorners.md)

# concentric(minimum:)

<sub>Type Method</sub>

Corner styles will be concentric with its container, varying the radius as needed in all four corners but never going below zero, or the provided minimum corner style, if provided.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func concentric(minimum: Edge.Corner.Style? = nil) -> RoundedRectangularShapeCorners
```
