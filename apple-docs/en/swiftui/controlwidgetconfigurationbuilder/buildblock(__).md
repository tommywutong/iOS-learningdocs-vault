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
doc_path: '/documentation/swiftui/controlwidgetconfigurationbuilder/buildblock(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/controlwidgetconfigurationbuilder/buildblock(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/controlwidgetconfigurationbuilder/buildblock%28_%3A%29.json'
content_hash: 'sha256:7bd30961c0d41ef0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ControlWidgetConfigurationBuilder](../controlwidgetconfigurationbuilder.md)

# buildBlock(_:)

<sub>Type Method</sub>

Passes a single control widget configuration written as a child control through unmodified.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
@export(implementation) static func buildBlock<Content>(_ content: Content) -> some ControlWidgetConfiguration where Content : ControlWidgetConfiguration

```

## Discussion

An example of a single control widget configuration written as a child view is `{ StaticControlConfiguration(...) }`.
