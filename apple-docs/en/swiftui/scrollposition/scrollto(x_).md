---
title: 'scrollTo(x:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scrollposition/scrollto(x:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scrollposition/scrollto(x:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollposition/scrollto%28x%3A%29.json'
content_hash: 'sha256:97f6be6c8b444b1a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollPosition](../scrollposition.md)

# scrollTo(x:)

<sub>Instance Method</sub>

Scrolls the position of the scroll view to the x value you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func scrollTo(x: CGFloat)
```

## Discussion

The scroll view chooses the y value based on the content insets of the scroll view and will clamp this value to only scroll to the size of its actual content.
