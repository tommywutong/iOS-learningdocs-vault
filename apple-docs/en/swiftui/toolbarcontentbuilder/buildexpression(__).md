---
title: 'buildExpression(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/toolbarcontentbuilder/buildexpression(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/toolbarcontentbuilder/buildexpression(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbarcontentbuilder/buildexpression%28_%3A%29.json'
content_hash: 'sha256:611b76b12cd26bee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarContentBuilder](../toolbarcontentbuilder.md)

# buildExpression(_:)

<sub>Type Method</sub>

Builds an expression within the builder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func buildExpression<Content>(_ content: Content) -> Content where Content : CustomizableToolbarContent
```

## See Also

### Building conditional toolbar content

- [buildIf(_:)](<buildif(__).md>)
- [buildEither(first:)](<buildeither(first_).md>)
- [buildEither(second:)](<buildeither(second_).md>)
- [buildLimitedAvailability(_:)](<buildlimitedavailability(__).md>)
