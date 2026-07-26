---
title: 'buildBlock(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/controlwidgettemplatebuilder/buildblock(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/controlwidgettemplatebuilder/buildblock(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/controlwidgettemplatebuilder/buildblock%28_%3A%29.json'
content_hash: 'sha256:333a826cbfa03685'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ControlWidgetTemplateBuilder](../controlwidgettemplatebuilder.md)

# buildBlock(_:)

<sub>Type Method</sub>

Passes a single control widget template written as a child view through unmodified.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
@export(implementation) static func buildBlock<Content>(_ content: Content) -> some ControlWidgetTemplate where Content : ControlWidgetTemplate

```

## Discussion

An example of a single control widget template written as a child view is `{ ControlWidgetToggle(...) }`.
