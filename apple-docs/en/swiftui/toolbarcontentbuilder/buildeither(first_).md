---
title: 'buildEither(first:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/toolbarcontentbuilder/buildeither(first:)'
source_url: 'https://developer.apple.com/documentation/swiftui/toolbarcontentbuilder/buildeither(first:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbarcontentbuilder/buildeither%28first%3A%29.json'
content_hash: 'sha256:d50b5e067239f019'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarContentBuilder](../toolbarcontentbuilder.md)

# buildEither(first:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> _ConditionalContent<TrueContent, FalseContent> where TrueContent : CustomizableToolbarContent, FalseContent : CustomizableToolbarContent
```

## See Also

### Building conditional toolbar content

- [buildIf(_:)](<buildif(__).md>)
- [buildEither(second:)](<buildeither(second_).md>)
- [buildExpression(_:)](<buildexpression(__).md>) — Builds an expression within the builder.
- [buildLimitedAvailability(_:)](<buildlimitedavailability(__).md>)
