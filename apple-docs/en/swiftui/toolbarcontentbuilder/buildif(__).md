---
title: 'buildIf(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/toolbarcontentbuilder/buildif(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/toolbarcontentbuilder/buildif(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbarcontentbuilder/buildif%28_%3A%29.json'
content_hash: 'sha256:0e3bc8e920f37134'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarContentBuilder](../toolbarcontentbuilder.md)

# buildIf(_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func buildIf<Content>(_ content: Content?) -> Content? where Content : CustomizableToolbarContent
```

## See Also

### Building conditional toolbar content

- [buildEither(first:)](<buildeither(first_).md>)
- [buildEither(second:)](<buildeither(second_).md>)
- [buildExpression(_:)](<buildexpression(__).md>) — Builds an expression within the builder.
- [buildLimitedAvailability(_:)](<buildlimitedavailability(__).md>)
