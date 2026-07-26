---
title: 'buildExpression(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/accessibilityrotorcontentbuilder/buildexpression(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/accessibilityrotorcontentbuilder/buildexpression(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessibilityrotorcontentbuilder/buildexpression%28_%3A%29.json'
content_hash: 'sha256:f878fbb049df1f1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AccessibilityRotorContentBuilder](../accessibilityrotorcontentbuilder.md)

# buildExpression(_:)

<sub>Type Method</sub>

Builds an expression within the builder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func buildExpression<Content>(_ content: Content) -> Content where Content : AccessibilityRotorContent
```

## See Also

### Building navigation content

- [buildBlock(_:)](<buildblock(__).md>)
- [buildIf(_:)](<buildif(__).md>)
