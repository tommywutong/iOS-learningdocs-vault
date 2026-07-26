---
title: 'scrollTo(y:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scrollposition/scrollto(y:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scrollposition/scrollto(y:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollposition/scrollto%28y%3A%29.json'
content_hash: 'sha256:ffc6eefb54de70ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollPosition](../scrollposition.md)

# scrollTo(y:)

<sub>Instance Method</sub>

Scrolls the position of the scroll view to the y value you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func scrollTo(y: CGFloat)
```

## Discussion

The scroll view chooses the x value based on the content insets of the scroll view and will clamp this value to only scroll to the size of its actual content.
