---
title: 'buildLimitedAvailability(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/widgetbundlebuilder/buildlimitedavailability(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/widgetbundlebuilder/buildlimitedavailability(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/widgetbundlebuilder/buildlimitedavailability%28_%3A%29.json'
content_hash: 'sha256:813154b4ce7841f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WidgetBundleBuilder](../widgetbundlebuilder.md)

# buildLimitedAvailability(_:)

<sub>Type Method</sub>

Builds an availability check within the builder

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
@export(implementation) static func buildLimitedAvailability(_ widget: some ControlWidget) -> any Widget & _LimitedAvailabilityWidgetMarker
```

## See Also

### Bundling widgets

- [buildBlock()](<buildblock().md>) — Builds an empty Widget from a block containing no statements, `{ }`.
- [buildBlock(_:)](<buildblock(__).md>)
- [buildExpression(_:)](<buildexpression(__).md>) — Builds an expression within the builder.
- [buildOptional(_:)](<buildoptional(__).md>) — Produces an optional widget for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.
