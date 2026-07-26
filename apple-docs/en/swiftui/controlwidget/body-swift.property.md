---
title: body
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/controlwidget/body-swift.property
source_url: 'https://developer.apple.com/documentation/swiftui/controlwidget/body-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/controlwidget/body-swift.property.json'
content_hash: 'sha256:c56334e1231dcdd8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ControlWidget](../controlwidget.md)

# body

<sub>Instance Property</sub>

The content and behavior of the control.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
@ControlWidgetConfigurationBuilder @MainActor @preconcurrency var body: Self.Body { get }
```

## Discussion

For any controls that you create, provide a computed `body` property that defines the control using some control widget configuration.

Swift infers the control’s [Body](body-swift.associatedtype.md) associated type based on the contents of the `body` property.
