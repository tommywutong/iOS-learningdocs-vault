---
title: 'scrollTo(point:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scrollposition/scrollto(point:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scrollposition/scrollto(point:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollposition/scrollto%28point%3A%29.json'
content_hash: 'sha256:d14023f65c7613ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollPosition](../scrollposition.md)

# scrollTo(point:)

<sub>Instance Method</sub>

Scrolls the position of the scroll view to the point you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func scrollTo(point: CGPoint)
```

## Discussion

The scroll view will clamp this value to only scroll to the size of its actual content.
