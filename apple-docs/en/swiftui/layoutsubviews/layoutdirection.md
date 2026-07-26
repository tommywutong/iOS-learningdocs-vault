---
title: layoutDirection
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/layoutsubviews/layoutdirection
source_url: 'https://developer.apple.com/documentation/swiftui/layoutsubviews/layoutdirection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/layoutsubviews/layoutdirection.json'
content_hash: 'sha256:565f5e97b254e21f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [LayoutSubviews](../layoutsubviews.md)

# layoutDirection

<sub>Instance Property</sub>

The layout direction inherited by the container view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var layoutDirection: LayoutDirection
```

## Discussion

SwiftUI supports both left-to-right and right-to-left directions. Read this property within a custom layout container to find out which environment the container is in.

In most cases, you don’t need to take any action based on this value. SwiftUI horizontally flips the x position of each view within its parent when the mode switches, so layout calculations automatically produce the desired effect for both directions.
