---
title: 'buildOptional(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/widgetbundlebuilder/buildoptional(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/widgetbundlebuilder/buildoptional(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/widgetbundlebuilder/buildoptional%28_%3A%29.json'
content_hash: 'sha256:1759399b4d27853d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WidgetBundleBuilder](../widgetbundlebuilder.md)

# buildOptional(_:)

<sub>Type Method</sub>

Produces an optional widget for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func buildOptional(_ widget: (any Widget & _LimitedAvailabilityWidgetMarker)?) -> some Widget

```

## Discussion

Conditional statements in a [WidgetBundleBuilder](../widgetbundlebuilder.md) can contain an `if` statement but not an `else` statement, and the condition can only perform a compiler check for availability, like in the following code:

```swift
var body: some Widget {
    if #available(iOS 16, *) {
        WindowGroup {
            ContentView()
        }
    }
}
```

## See Also

### Bundling widgets

- [buildBlock()](<buildblock().md>) — Builds an empty Widget from a block containing no statements, `{ }`.
- [buildBlock(_:)](<buildblock(__).md>)
- [buildExpression(_:)](<buildexpression(__).md>) — Builds an expression within the builder.
- [buildLimitedAvailability(_:)](<buildlimitedavailability(__).md>) — Builds an availability check within the builder
