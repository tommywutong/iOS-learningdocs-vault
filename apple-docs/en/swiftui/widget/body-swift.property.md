---
title: body
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/widget/body-swift.property
source_url: 'https://developer.apple.com/documentation/swiftui/widget/body-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/widget/body-swift.property.json'
content_hash: 'sha256:b7349fa81ea19596'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Widget](../widget.md)

# body

<sub>Instance Property</sub>

The content and behavior of the widget.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency var body: Self.Body { get }
```

## Discussion

For any widgets that you create, provide a computed `body` property that defines the widget as a composition of SwiftUI views.

Swift infers the widget’s [Body](../scene/body-swift.associatedtype.md) associated type based on the contents of the `body` property.

## See Also

### Implementing a widget

- [Body](body-swift.associatedtype.md) — The type of configuration representing the content of the widget.
