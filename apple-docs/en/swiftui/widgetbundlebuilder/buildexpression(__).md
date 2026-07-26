---
title: 'buildExpression(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/widgetbundlebuilder/buildexpression(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/widgetbundlebuilder/buildexpression(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/widgetbundlebuilder/buildexpression%28_%3A%29.json'
content_hash: 'sha256:4e62bc10792c4856'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WidgetBundleBuilder](../widgetbundlebuilder.md)

# buildExpression(_:)

<sub>Type Method</sub>

Builds an expression within the builder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func buildExpression<Content>(_ content: Content) -> Content where Content : Widget
```

## See Also

### Bundling widgets

- [buildBlock()](<buildblock().md>) — Builds an empty Widget from a block containing no statements, `{ }`.
- [buildBlock(_:)](<buildblock(__).md>)
- [buildLimitedAvailability(_:)](<buildlimitedavailability(__).md>) — Builds an availability check within the builder
- [buildOptional(_:)](<buildoptional(__).md>) — Produces an optional widget for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.
