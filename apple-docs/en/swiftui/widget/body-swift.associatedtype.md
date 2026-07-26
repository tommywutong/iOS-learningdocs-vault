---
title: Body
framework: SwiftUI
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/widget/body-swift.associatedtype
source_url: 'https://developer.apple.com/documentation/swiftui/widget/body-swift.associatedtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/widget/body-swift.associatedtype.json'
content_hash: 'sha256:1836dcb5461b24be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Widget](../widget.md)

# Body

<sub>Associated Type</sub>

The type of configuration representing the content of the widget.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
associatedtype Body : WidgetConfiguration
```

## Discussion

When you create a custom widget, Swift infers this type from your implementation of the required [body](body-swift.property.md) property.

## See Also

### Implementing a widget

- [body](body-swift.property.md) — The content and behavior of the widget.
