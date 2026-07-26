---
title: 'buildIf(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/accessibilityrotorcontentbuilder/buildif(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/accessibilityrotorcontentbuilder/buildif(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessibilityrotorcontentbuilder/buildif%28_%3A%29.json'
content_hash: 'sha256:27151e7cbd213cef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AccessibilityRotorContentBuilder](../accessibilityrotorcontentbuilder.md)

# buildIf(_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func buildIf<Content>(_ content: Content?) -> some AccessibilityRotorContent where Content : AccessibilityRotorContent

```

## See Also

### Building navigation content

- [buildBlock(_:)](<buildblock(__).md>)
- [buildExpression(_:)](<buildexpression(__).md>) — Builds an expression within the builder.
