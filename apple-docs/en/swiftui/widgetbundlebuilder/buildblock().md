---
title: buildBlock()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/widgetbundlebuilder/buildblock()
source_url: 'https://developer.apple.com/documentation/swiftui/widgetbundlebuilder/buildblock()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/widgetbundlebuilder/buildblock%28%29.json'
content_hash: 'sha256:682e82ea79d1af51'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WidgetBundleBuilder](../widgetbundlebuilder.md)

# buildBlock()

<sub>Type Method</sub>

Builds an empty Widget from a block containing no statements, `{ }`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
static func buildBlock() -> some Widget

```

## See Also

### Bundling widgets

- [buildBlock(_:)](<buildblock(__).md>)
- [buildExpression(_:)](<buildexpression(__).md>) — Builds an expression within the builder.
- [buildLimitedAvailability(_:)](<buildlimitedavailability(__).md>) — Builds an availability check within the builder
- [buildOptional(_:)](<buildoptional(__).md>) — Produces an optional widget for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.
