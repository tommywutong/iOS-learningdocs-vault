---
title: Body
framework: SwiftUI
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view/body-swift.associatedtype
source_url: 'https://developer.apple.com/documentation/swiftui/view/body-swift.associatedtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/body-swift.associatedtype.json'
content_hash: 'sha256:b82f940b3b0308bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# Body

<sub>Associated Type</sub>

The type of view representing the body of this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype Body : View
```

## Discussion

When you create a custom view, Swift infers this type from your implementation of the required [body](body-8kl5o.md) property.

## See Also

### Implementing a custom view

- [body](body-8kl5o.md) — The content and behavior of the view.
- [modifier(_:)](<modifier(__).md>) — Applies a modifier to a view and returns a new view.
- [Previews in Xcode](../previews-in-xcode.md) — Generate dynamic, interactive previews of your custom views.
