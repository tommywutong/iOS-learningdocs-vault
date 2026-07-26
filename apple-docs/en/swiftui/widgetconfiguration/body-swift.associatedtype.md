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
doc_path: /documentation/swiftui/widgetconfiguration/body-swift.associatedtype
source_url: 'https://developer.apple.com/documentation/swiftui/widgetconfiguration/body-swift.associatedtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/widgetconfiguration/body-swift.associatedtype.json'
content_hash: 'sha256:3182f0b5d8e1a7ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WidgetConfiguration](../widgetconfiguration.md)

# Body

<sub>Associated Type</sub>

The type of widget configuration representing the body of this configuration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
associatedtype Body : WidgetConfiguration
```

## Discussion

When you create a custom widget, Swift infers this type from your implementation of the required `body` property.

## See Also

### Implementing a widget

- [body](body-swift.property.md) — The content and behavior of this widget.
