---
title: init()
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/concentricrectangle/init()
source_url: 'https://developer.apple.com/documentation/swiftui/concentricrectangle/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/concentricrectangle/init%28%29.json'
content_hash: 'sha256:2ff53b6be07c63c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ConcentricRectangle](../concentricrectangle.md)

# init()

<sub>Initializer</sub>

Creates a rectangle using the concentric corner style on each corner individually.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init()
```

## Discussion

The system may calculate a different radius for each corner. This can happen when the rectangle is not centered within the container shape, or the container shape’s corners have different radii.
